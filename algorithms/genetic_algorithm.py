import numpy as np
import random
import logging


def tournament_selection(population, fitnesses, tournament_size=3):
    """
    Selects parents for crossover based on tournament selection.

    :parameter
    ----------
    population (List): The population of individuals.
    fitnesses (List): The fitness values of the individuals.
    tournament_size (int): The size of the tournament.

    :return
    -------
    List: The selected parents.
    """
    selected_indices = np.random.choice(range(len(population)), tournament_size, replace=False)
    tournament_fitnesses = [fitnesses[i] for i in selected_indices]
    winner_index = selected_indices[np.argmax(tournament_fitnesses)]
    return population[winner_index]


def uniform_crossover(parent1, parent2, crossover_rate=0.5):
    """
    Performs uniform crossover on two parents.

    :parameter
    ----------
    parent1, parent2 (List): The parents to crossover.
    crossover_rate (float): The probability of each gene being swapped.

    :return
    -------
    List: The child.
    """
    child = []
    for gene1, gene2 in zip(parent1, parent2):
        child.append(gene1 if random.random() < crossover_rate else gene2)
    return child


def mutation(individual, mutation_rate, mutation_scale=0.1):
    """
    Mutates an individual.

    :parameter
    ----------
    individual (List): The individual to be mutated.
    mutation_rate (float): The probability of mutation for each gene.
    mutation_scale (float): Scale of the normal distribution for mutation.

    :return
    -------
    List: The mutated individual.
    """
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] += np.random.normal(scale=mutation_scale)
    return individual


def genetic_algorithm(function, points, num_generations=30, mutation_rate=0.02, mutation_scale=0.1):
    """
    Performs a genetic algorithm for optimization.

    :param function: The function to be optimized.
    :param points: Initial points for the population.
    :param num_generations: Number of generations to run the genetic algorithm.
    :param mutation_rate: Probability of mutation for each individual.
    :param mutation_scale: Scale of normal distribution for mutation.
    :return: A list of arrays representing the paths taken by the genetic algorithm.
    """
    population = points
    num_individuals = len(population)
    paths = []

    for _ in range(num_generations):
        # Fitness calculation (adjusted for minimization)
        fitnesses = np.array([1 / (1 + function(individual)) for individual in population])

        paths.append(population)
        new_population = []

        # Main loop of the genetic algorithm
        while len(new_population) < num_individuals:
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)

            if random.random() < 0.9:  # Crossover probability
                child = uniform_crossover(parent1, parent2)
            else:
                child = parent1 if random.random() < 0.5 else parent2

            child = mutation(child, mutation_rate, mutation_scale)
            new_population.append(child)

        population = new_population

    logging.info("Genetic algorithm finished")
    # the best finding minimum
    founded_minimum = paths[-1][-1]
    output = f'Best finding minimum: [X: {founded_minimum[0]:.2f}, Y: {founded_minimum[1]:.2f}],' \
             f' Z: {function(founded_minimum):.2f}'
    return np.array(paths), output
