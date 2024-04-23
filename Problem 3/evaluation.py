from typing import Any, List, Optional
from bbob import BBOB
import numpy as np


class Evaluation:
    def __init__(
        self,
        mh_name: str,
        solutions: List[Any],
        values: List[Any],
        total_evals: int,
        total_time: float,
        fail_msg: Optional[str],
    ):
        self.mh_name = mh_name
        self.solutions = solutions
        self.values = values
        self.iters = len(self.solutions)
        self.best_result = None if not self.solutions else self.solutions[-1]
        self.total_evals = total_evals
        self.total_time = total_time
        self.success = fail_msg is None
        self.fail_msg = fail_msg

    def __repr__(self) -> str:
        ans = (
            f"Evaluation of {self.mh_name}:\n"
            f"  best result --------------- {self.best_result}\n"
            f"  success ------------------- {self.success}\n"
            f"  iters --------------------- {self.iters}\n"
            f"  evals --------------------- {self.total_evals}\n"
            f"  time ---------------------- {self.total_time}\n"
        )
        if self.iters:
            ans += (
                f"  approx. evals per iter ---- {self.total_evals / self.iters}\n"
                f"  approx. iter time --------- {self.total_time / self.iters}\n"
            )
        if not self.success:
            ans += f"  fail reason: '{self.fail_msg}'\n"
        return ans

    def __str__(self) -> str:
        return repr(self)



def test_metaheuristic(
    mh: 'MetaHeuristic',
    max_evals: Optional[int] = None,
    max_iters: Optional[int] = None,
    max_time: Optional[float] = 5,
    *args,
    **kwargs,
):
    bbob = BBOB(seed=10)
    bbob_functions = [
        bbob.sphere_func(dim=2),
        bbob.ellipsodial_func(dim=2),
        bbob.rastrigin_func(dim=2),
        bbob.buche_rastrigin_func(dim=2),
        bbob.linear_slpoe_func(dim=2),
    ]

    for func in bbob_functions:
        print("\nTest\n")
        print(func, end="\n\n")
        ev = mh.evaluate(
            func.func,
            max_evals=max_evals,
            max_iters=max_iters,
            max_time=max_time,
            *args,
            **kwargs,
        )
        print(ev)

        print()
        print(f"Error: {abs(func.f_opt - func(ev.best_result))}")

        try:
            import matplotlib.pyplot as plt
            func.plot(show = False)
            sols = np.array(ev.solutions)
            values = np.array(ev.values)[..., None]
            points = np.hstack((sols, values))
            plt.plot(*list(points.T), '-o', color='blue')
            plt.show()
        except ImportError:
            pass