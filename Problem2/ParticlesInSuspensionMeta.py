from Particles import Particle

from Problem2 import time_for_postures,objective_function

import numpy as np
import random
import math

def fitness(solution):
    return objective_function(solution)


num_particles =100
particles = []


global_best =time_for_postures
global_best_fitness = fitness(time_for_postures)

for i in range(0,num_particles):
    initial_solutions =  global_best
    particles.append(Particle(initial_solutions,np.zeros(len(time_for_postures)),random.random()*10,random.random()*10,fitness))


num_iterations = 1000

for i in range(num_iterations):
    for particle in particles:
        particle.update_speed(global_best)
        particle.update_position(fitness)
        #particle.position =  np.clip(np.abs(np.round(particle.position)),0,len(time_for_postures)-1)
        particle_fitness = fitness(particle.position)
        if particle_fitness >= global_best_fitness:
            global_best = particle.position
            global_best_fitness = particle_fitness

print('resultados de particulas en suspension: ')
print('\t the maximun pleassure of the lowest pleassured participant is : ',global_best_fitness)
print('\t the aproximated best times for the positions are : ',global_best)


