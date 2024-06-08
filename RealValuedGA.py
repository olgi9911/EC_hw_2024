import numpy as np
import matplotlib.pyplot as plt

class RealValuedGA:
    def __init__(self, dimension, population_size, crossover_method, cross_prob, mut_prob, num_generations, n=2, alpha=0.2):
        self.dimension = dimension
        self.population_size = population_size
        self.crossover_method = crossover_method
        self.cross_prob = cross_prob
        self.mut_prob = mut_prob
        self.num_generations = num_generations
        self.n = n
        self.alpha = alpha

    def init_population(self):
        return np.random.uniform(low=-512, high=511, size=(self.population_size, self.dimension))
    
    def fitness(self, gene):      
        return self.schwefel(gene)
    
    def crossover(self, selected_population, crossover_method):
        children = np.zeros(selected_population.shape)
        for i in range(0, self.population_size, 2):
            parent1, parent2 = selected_population[i], selected_population[i + 1] # consecutive pair
            if np.random.random() < self.cross_prob:
                if crossover_method == 'uniform':
                    mask = np.random.randint(2, size=selected_population.shape[1])
                    child1 = parent1.copy()
                    child2 = parent2.copy()
                    for j in range(selected_population.shape[1]):
                        if mask[j] == 1:
                            child1[j], child2[j] = parent2[j], parent1[j]
                else: # whole arithmetic
                    child1 = self.alpha * parent1 + (1 - self.alpha) * parent2
                    child2 = self.alpha * parent2 + (1 - self.alpha) * parent1

                children[i] = child1
                children[i + 1] = child2
            else:
                children[i] = parent1
                children[i + 1] = parent2

        return children
    
    def mutate(self, children):
        mask = np.random.random(children.shape[0]) < self.mut_prob
        for i in range(children.shape[0]):
            if mask[i] == 1:
                children[i] = np.random.uniform(low=-512, high=511)
        return children
    
    def select(self, population, population_fitness):
        selected_population = np.zeros(population.shape)
        for idx in range(self.population_size):
            candidates = np.random.choice(self.population_size, size=self.n, replace=False)
            candidate_fitness = [population_fitness[i] for i in candidates]
            selected_idx = np.argmin(candidate_fitness)
            selected_population[idx] = population[selected_idx]

        return selected_population
    
    def survivor_select(self, population, children):
        combined_population = np.vstack((population, children))
        combined_fitness = np.zeros(combined_population.shape[0])
        #print(combined_population)
        for i in range(combined_population.shape[0]):
            combined_fitness[i] = self.fitness(combined_population[i])
        sorted_idx = np.argsort(combined_fitness)
        return combined_population[sorted_idx[:self.population_size]] # elitism
    
    def schwefel(self, x):
        return 418.98291 * self.dimension - np.sum(x * np.sin(np.sqrt(np.abs(x))))
    
    def runner(self):
        population = self.init_population()
        #best_solution = None
        best_fitness = float('inf')
        population_fitness = np.zeros(self.population_size)
        fitness_record = np.zeros(self.num_generations)
        for gen in range(self.num_generations):
            for i in range(self.population_size):
                population_fitness[i] = self.fitness(population[i])

            min_idx = np.argmin(population_fitness)
            if population_fitness[min_idx] < best_fitness:
                best_fitness = population_fitness[min_idx]
                #best_solution = population[min_idx]
            
            selected_population = self.select(population, population_fitness)
            children = self.crossover(selected_population, self.crossover_method)
            children = self.mutate(children)
            population = self.survivor_select(population, children)

            fitness_record[gen] = best_fitness
        
        print(best_fitness)
        return fitness_record