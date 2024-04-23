import random
import sys
import threading
import time
import types
import numpy as np
from abc import ABC, abstractmethod
from typing import Any, Callable, Optional
from evaluation import Evaluation


class MetaHeuristic(ABC):
    @abstractmethod
    def solve(self, obj_fuc: Callable, *args, **kwargs) -> Any:
        """Solves a problem given an objective function"""
        raise NotImplementedError()

    def on_new_solution(self, sol: Any, val: Any):
        """This function is called every time a new solution is found"""

    def evaluate(
        self,
        obj_func: Callable,
        max_evals: Optional[int] = None,
        max_iters: Optional[int] = None,
        max_time: Optional[float] = None,
        check_every: float = 0.00001,
        verbose: bool = True,
        *args,
        **kwargs,
    ) -> Evaluation:
        if verbose:
            print(f"Evaluating {self.__class__.__name__}", flush=True)
        evals = 0
        solutions = []
        values = []
        fail_msg = None

        def _obj_func(*args, **kwargs):
            nonlocal evals
            nonlocal fail_msg

            if fail_msg is not None:
                sys.exit(0)

            if max_evals is not None and evals == max_evals:
                fail_msg = "Obj. function max evaluation exceeded."
                sys.exit(0)

            evals += 1
            return obj_func(*args, **kwargs)

        def _solve_func():
            nonlocal solutions
            nonlocal values
            nonlocal fail_msg
            sol = self.solve(_obj_func, *args, **kwargs)
            if isinstance(sol, types.GeneratorType):
                for s, v in sol:
                    if verbose:
                        print(" " * 100, end="\r")
                        print(
                            f"{time.time() - t0:.3f}s - Last value: {v} - Last solution: {s}",
                            end="\r",
                            flush=True,
                        )
                    self.on_new_solution(s, v)
                    solutions.append(s)
                    values.append(v)
                    if max_iters is not None and len(solutions) == max_iters:
                        fail_msg = "Max iterations exceeded."
                        sys.exit(0)
            elif isinstance(sol, tuple) and len(sol) == 2:
                solutions = [sol[0]]
                values = [sol[1]]
            else:
                raise ValueError(
                    "The 'solve' function must return tuples of size 2: (solution, value)."
                )
            print()

        proc = threading.Thread(target=_solve_func)

        t0 = time.time()
        proc.start()
        if max_time is not None:
            t1 = time.time()
            failed = True
            while t1 - t0 < max_time:
                if not proc.is_alive():
                    failed = False
                    break
                time.sleep(check_every)
                t1 = time.time()
            if failed:
                fail_msg = "Max time exceeded."
        else:
            proc.join()
            t1 = time.time()

        total_time = t1 - t0

        res = Evaluation(
            self.__class__.__name__,
            solutions=solutions,
            values=values,
            total_evals=evals,
            total_time=total_time,
            fail_msg=fail_msg,
        )
        return res


# Particle Swarm Optimization
class PSO(MetaHeuristic):
    def __init__(self) -> None:
        self.hpos = None
        super().__init__()
    
    class Particle:
        def __init__(self, pos, speed, inertia=0.5, cognitive_coeff=0.5, social_coeff=0.6):
            assert len(pos) == len(speed), "The particle position and speed must be the same length"
            self.pos = pos
            self.speed = speed
            self.best_pos = pos
            self.dim = len(pos)
            
            self.inertia = inertia
            self.cog_coeff = cognitive_coeff
            self.soc_coeff = social_coeff

        def upd_speed(self, global_best):
                rp = random.random()
                rg = random.random()
                self.speed = self.inertia*self.speed + self.cog_coeff*rp*(self.best_pos-self.pos) + self.soc_coeff*rg*(global_best - self.pos)
    
        def upd_pos(self):
            self.pos += self.speed            

        def upd_best_pos(self):
            self.best_pos = self.pos
            
        def __str__(self) -> str:
            return str(self.pos)
        
    
    def stop_condition(self, t) -> bool:
        return t > 3000
        
    def get_init_pop(self, sol_dim, pop_size):        
        init_pop = [
            PSO.Particle(
                # TODO: change (-5, 5) by the correct search zone
                pos=np.array([random.uniform(0, 3) for _ in range(sol_dim)]),
                speed=np.zeros(sol_dim)
            )
            for i in range(pop_size)
        ]
        return init_pop
    
    def is_best_sol(self, x, y, obj_func: Callable):
        if obj_func(x) < obj_func(y):
            return True
        else:
            return False
    
    def solve(self, obj_func: Callable, sol_dim, pop_size=random.randint(6, 10), verbose=False) -> np.any:
        # generate the initial population
        sols = self.get_init_pop(sol_dim, pop_size)
        
        # search the best position
        global_best = None        
        for sol in sols:
            if global_best is None or self.is_best_sol(sol.pos, global_best, obj_func):
                global_best = sol.pos
        
        t = 0
        while(not self.stop_condition(t)):
            if verbose:
                print(f'\n======== Iteracion {t} =========')
                print(f'Best sol: {global_best}')
                print(f'Cand sol: {[x.pos for x in sols]}')
            
            for p in sols:
                p.upd_speed(global_best)
                p.upd_pos()
                if self.is_best_sol(p.best_pos, p.pos, obj_func):
                    p.upd_best_pos()
                if self.is_best_sol(p.best_pos, global_best, obj_func):
                    global_best = p.best_pos
            t += 1
                    
        return (global_best, obj_func(global_best))