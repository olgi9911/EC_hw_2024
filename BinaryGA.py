import numpy as np
import matplotlib.pyplot as plt

class BinaryGA:
    def __init__(self, dimension, population_size, crossover_method, cross_prob, mut_prob, num_generations, n=2, gray_code=True):
        self.dimension = dimension
        self.population_size = population_size
        self.crossover_method = crossover_method
        self.cross_prob = cross_prob
        self.mut_prob = mut_prob
        self.num_generations = num_generations
        self.n = n
        self.gray_code = gray_code

    def init_population(self):
        return np.random.randint(2, size=(self.population_size, 10 * self.dimension))
    
    def fitness(self, gene):
        x = np.zeros(self.dimension)
        for idx in range(self.dimension):
            bit_array = gene[idx*10:(idx+1)*10]
            bit_string = "".join(str(i) for i in bit_array)
            '''
            # 2's complement
            if bit_string[0] == '1':
                inverted_bits = "".join("1" if bit == "0" else "0" for bit in bit_string)
                inverted_num = int(inverted_bits, 2)
                x[idx] = -(inverted_num + 1)
            else:
                x[idx] = int(bit_string, 2)
            '''
            n = int(bit_string, 2)
            
            if self.gray_code:
                # Gray code
                mask = n
                while mask != 0:
                    mask >>= 1
                    n ^= mask
            x[idx] = n - 512
            
        return self.schwefel(x)
    
    def crossover(self, selected_population, crossover_method):
        children = np.zeros(selected_population.shape, dtype='int')
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
                else: # two-point
                    crossover_point = np.sort(np.random.choice(selected_population.shape[1], size=2, replace=False))
                    child1 = parent1.copy()
                    child2 = parent2.copy()
                    child1[crossover_point[0] : crossover_point[1]] = parent2[crossover_point[0] : crossover_point[1]]
                    child2[crossover_point[0] : crossover_point[1]] = parent1[crossover_point[0] : crossover_point[1]]

                children[i] = child1
                children[i + 1] = child2
            else:
                children[i] = parent1
                children[i + 1] = parent2

        return children
        
    def mutate(self, children):
        mask = np.random.random(children.shape) < self.mut_prob
        return children ^ mask
    
    def select(self, population, population_fitness):
        selected_population = np.zeros(population.shape, dtype='int')
        for idx in range(self.population_size):
            candidates = np.random.choice(self.population_size, size=self.n, replace=False)
            candidate_fitness = [population_fitness[i] for i in candidates]
            selected_idx = np.argmin(candidate_fitness)
            selected_population[idx] = population[selected_idx]

        return selected_population
    
    def survivor_select(self, population, children):
        combined_population = np.vstack((population, children))
        combined_fitness = np.zeros(combined_population.shape[0])

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
