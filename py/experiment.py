import sys
import numpy as np
import matplotlib.pyplot as plt

from BinaryGA import BinaryGA
from RealValuedGA import RealValuedGA

ga = BinaryGA(100, 100, 'uniform', 0.9, 0.1, 500)
trial_fitness_record = np.zeros((30, 500))
for i in range(10):
    trial_fitness_record[i] = ga.runner()

average_fitness_record = np.average(trial_fitness_record, axis=0)

plt.figure(dpi=300)
plt.plot(average_fitness_record, label='p_c = 0.9')

ga = BinaryGA(100, 100, 'uniform', 0.7, 0.1, 500)
trial_fitness_record = np.zeros((30, 500))
for i in range(10):
    trial_fitness_record[i] = ga.runner()

average_fitness_record = np.average(trial_fitness_record, axis=0)
plt.plot(average_fitness_record, label='p_c = 0.7')

ga = BinaryGA(100, 100, 'uniform', 0.5, 0.1, 500)
trial_fitness_record = np.zeros((30, 500))
for i in range(10):
    trial_fitness_record[i] = ga.runner()

average_fitness_record = np.average(trial_fitness_record, axis=0)
plt.plot(average_fitness_record, label='p_c = 0.5')

ga = BinaryGA(100, 100, 'uniform', 0.3, 0.1, 500)
trial_fitness_record = np.zeros((30, 500))
for i in range(10):
    trial_fitness_record[i] = ga.runner()

average_fitness_record = np.average(trial_fitness_record, axis=0)
plt.plot(average_fitness_record, label='p_c = 0.3')

ga = BinaryGA(100, 100, 'uniform', 0.1, 0.1, 500)
trial_fitness_record = np.zeros((30, 500))
for i in range(10):
    trial_fitness_record[i] = ga.runner()

average_fitness_record = np.average(trial_fitness_record, axis=0)
plt.plot(average_fitness_record, label='p_c = 0.1')

'''
ga = RealValuedGA(10, 100, 'uniform', 0.9, 0.1, 500)
trial_fitness_record = np.zeros((30, 500))
for i in range(30):
    trial_fitness_record[i] = ga.runner()

average_fitness_record = np.average(trial_fitness_record, axis=0)
plt.plot(average_fitness_record, label='Uniform Real-valued GA')

ga = RealValuedGA(10, 100, 'whole arithmetic', 0.9, 0.1, 500)
trial_fitness_record = np.zeros((30, 500))
for i in range(30):
    trial_fitness_record[i] = ga.runner()

average_fitness_record = np.average(trial_fitness_record, axis=0)
plt.plot(average_fitness_record, label='Whole Arithmetic Real-valued GA')
'''
plt.xlabel('Generations')
plt.ylabel('f(x)')
#plt.ylim(0, 1250)
plt.legend()
plt.savefig('anytime.png')
