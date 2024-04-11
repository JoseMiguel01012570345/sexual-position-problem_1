import numpy as np
import sys

participants =np.array([1,2])
postures =np.array([i for i in range(0,10)])

P = len(participants)
Po = len(postures)

people_energy=np.abs(np.random.randn(P,Po))

people_pleasure=np.abs(np.random.randn(P,Po))


time_for_postures=np.abs(np.random.randn(Po))*3

energy_retrieved_after_posture=np.abs(np.random.randn(P,Po))*10

pleasure_given_by_posture=np.abs(np.random.randn(P,Po))*10

initial_energy =np.abs(np.random.randn(P))*10
initial_pleasure=np.abs(np.random.randn(P))*1

orgasm_treshold=(np.abs(np.random.randn(P))+1)*5
#TODO maximize the pleasure of the lowest pleasure given after sexual act


#model: we are trying to maximize the pleasure of the lowest pleasure given after all participants reach orgasm

# so the objetive function is max min(people_posture_pleasure[i,Po]*participants[i])
# SA 
# people_posture_energy[i,j] >= 0 forall participants and postures
# people_posture_energy[i,Po] >= orgasm_treshold[i] for all participants
#

print(f'participants: {P}')
print(f'postures: {Po}')

print('\n\n\n')



print(f'initial energy : {initial_energy}')
print('\n\n\n')
print(f'initial pleasure : {initial_pleasure}')
print('\n\n\n')

print(f'pleasure given by position per time unit: {pleasure_given_by_posture}')
print('\n\n\n')
print(f'energy retrieved by position per time unit: {energy_retrieved_after_posture}')
print('\n\n\n')

print(f'orgasm treshold: {orgasm_treshold}')
print('\n\n\n')
print('\n\n\n')
print('\n\n\n')


def objective_function(time_for_posture_config):

    for i in range(0,P):
        for j in range(0,Po):
            people_energy[i,j]=0
            if j ==0:
                people_energy[i,j] = initial_energy[i] - energy_retrieved_after_posture[i,j]*time_for_posture_config[j]
                people_pleasure[i,j] =initial_pleasure[i] + pleasure_given_by_posture[i,j]*time_for_posture_config[j]
            else:
                people_energy[i,j] = people_energy[i,j-1] - energy_retrieved_after_posture[i,j]*time_for_posture_config[j]
                people_pleasure[i,j] =people_pleasure[i,j-1] + pleasure_given_by_posture[i,j]*time_for_posture_config[j]



    for i in range(0,P):
        for j in range(0,Po):
            if people_energy[i,j] <= 0:
                return sys.float_info.min

    for i in range(0,P):
        if people_pleasure[i,Po-1] < orgasm_treshold[i]:
                return sys.float_info.min

    for i in range(Po):
        if time_for_posture_config[i] <=0:
                return sys.float_info.min
    return min(people_pleasure[:,Po-1])




