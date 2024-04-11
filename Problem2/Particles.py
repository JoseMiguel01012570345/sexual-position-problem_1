"""
   Modeling particles
"""
import random

class Particle:

    def __init__(self,orders_indices,initial_speed,social_inercy,personal_inercy,fitness) -> None:
        self.position = orders_indices
        self.personal_best = orders_indices
        self.speed = initial_speed
        self.personal_inercy = personal_inercy
        self.global_inercy = social_inercy
        self.personal_best_score = fitness(self.position)
    
    def update_speed(self,global_best):
          r1 = random.random()
          r2 = random.random()

          self.speed = self.speed + self.personal_inercy*r1*(self.personal_best-self.position) + self.global_inercy*r2*(global_best-self.position)
    def update_position(self,fitness):

         self.position = self.position + self.speed
         current_fitness = fitness(self.position)
         if current_fitness < self.personal_best_score:
              self.personal_best=self.position
              self.personal_best_score = current_fitness
    def __str__(self) -> str:
         return str(self.position)
