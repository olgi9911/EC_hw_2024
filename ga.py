import sys
import numpy as np
import matplotlib.pyplot as plt

from BinaryGA import BinaryGA
from RealValuedGA import RealValuedGA

def ga(config):
    if config.representation == 'binary':
        ga = BinaryGA(config.dimension, config.population_size, config.crossover_method, config.cross_prob, config.mut_prob, config.num_generations)
    else:
        ga = RealValuedGA(config.dimension, config.population_size, config.crossover_method, config.cross_prob, config.mut_prob, config.num_generations)
        
    fitness_record = ga.runner()
    return