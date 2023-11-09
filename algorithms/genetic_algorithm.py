import numpy as np
import random
from utils.output import rez_output


def selection(population, fitnesses):
    """
    Selects parents for crossover based on roulette wheel selection.

    :parameter
    ----------
    population (List): The population of individuals.
    fitnesses (List): The fitness values of the individuals.

    :return
    -------
    List: The selected parents.
    """
    idx = np.random.choice(np.arange(len(population)), size=2, p=fitnesses / fitnesses.sum())
    return [population[i] for i in idx]


def crossover(parents):
    crossover_point = random.randint(1, len(parents[0]) - 1)
    return np.concatenate((parents[0][:crossover_point], parents[1][crossover_point:]))


def mutation(individual, mutation_rate):
    """
    Mutates an individual with an adaptive mutation strategy.

    :parameter
    ----------
    individual (List): The individual to be mutated.
    mutation_rate (float): The probability of mutation for each gene.
    min_values (List): The minimum values for each gene.
    max_values (List): The maximum values for each gene.

    :return
    -------
    List: The mutated individual.
    """

    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] += np.random.normal()
    return individual


def genetic_algorithm(function, points, num_generations=200, mutation_rate=0.02):
    """
    Performs a simple genetic algorithm for optimization.

    :param function: The function to be optimized.
    :param points: Initial points for the population.
    :param num_generations: Number of generations to run the genetic algorithm.
    :param mutation_rate: Probability of mutation for each individual.
    :return: A list of arrays representing the paths taken by the genetic algorithm.
             A list of strings representing the output of the genetic algorithm at each iteration.
    """
    population = points
    # print(population[0], type(population[0]))
    num_individuals = len(population)
    paths = []
    output = []

    for _ in range(num_generations):
        fitnesses = np.array([-function(individual) for individual in population])
        # Make sure all fitness values are positive
        fitnesses = [fitness if fitness > 0 else 0.0001 for fitness in fitnesses]
        fitnesses = np.array(fitnesses)
        fitnesses = fitnesses / fitnesses.sum()  # Normalize fitness values

        paths.append(population)
        # output.append([str(individual) + ' : ' + str(function(individual)) for individual in population])
        output.append([rez_output(individual, individual, function) for individual in population])
        new_population = []
        # Adjust the range to handle both even and odd numbers of individuals
        for _ in range(num_individuals // 2):
            parents = selection(population, fitnesses)
            child1 = mutation(crossover(parents), mutation_rate)
            child2 = mutation(crossover(parents[::-1]), mutation_rate)
            new_population.extend([child1, child2])

        # If there's an odd number of individuals, handle the last remaining individual
        if num_individuals % 2 != 0:
            parents = selection(population, fitnesses)
            child1 = mutation(crossover(parents), mutation_rate)
            new_population.append(child1)

        population = new_population
    print("_______________________________Genetic Algorithm_______________________________")
    print(len(paths), "____________LEN PATHS______________")
    print(paths)
    paths = np.array(paths)

    return paths, output
