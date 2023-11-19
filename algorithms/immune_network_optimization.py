import numpy as np
import random
import logging


def affinity(population, function):
    """
    Calculate the affinity of each antibody in the population.
    Affinity is inversely related to the objective function value.

    :param population: List of antibodies (solutions).
    :param function: The objective function to be optimized.
    :return: List of affinity values.
    """
    return [1 / (1 + function(individual)) for individual in population]


def clonal_selection(population, fitnesses, clone_rate):
    """
    Generate clones for each antibody based on their affinity.

    :param population: List of antibodies (solutions).
    :param fitnesses: List of affinity values.
    :param clone_rate: The number of clones to be generated for an antibody.
    :return: List of cloned antibodies.
    """
    clones = []
    for individual, fitness in zip(population, fitnesses):
        num_clones = int(clone_rate * fitness / max(fitnesses))
        clones.extend([individual.copy() for _ in range(num_clones)])
    return clones


def hypermutation(clones, mutation_rate):
    """
    Apply hypermutation to clones.

    :param clones: List of cloned antibodies.
    :param mutation_rate: Hypermutation rate.
    :return: List of mutated clones.
    """
    for clone in clones:
        if random.random() < mutation_rate:
            clone += np.random.normal(0, 1, size=len(clone))
    return clones


def remove_duplicates(clones, function):
    """
    Removes duplicate clones, keeping the one with the best fitness.

    :param clones: List of cloned antibodies.
    :param function: The objective function to be optimized.
    :return: A list of unique clones.
    """
    unique = {}
    for clone in clones:
        key = tuple(clone)
        if key not in unique or function(clone) < function(unique[key]):
            unique[key] = clone
    return list(unique.values())


def immune_network_optimization(function, points, num_generations=100, clone_rate=10, mutation_rate=0.1):
    """
    Performs an optimization using an Artificial Immune Network.
    """
    population = points
    paths = []

    for _ in range(num_generations):
        # Calculate affinity (fitness)
        fitnesses = affinity(population, function)

        # Clonal selection
        clones = clonal_selection(population, fitnesses, clone_rate)

        # Hypermutation
        mutated_clones = hypermutation(clones, mutation_rate)

        # Evaluate the mutated clones and keep the best
        mutated_clones.sort(key=function)
        unique_clones = remove_duplicates(mutated_clones, function)

        # Select the best unique mutated clones to form a new population
        population = unique_clones[:len(population)]
        print(population)

        # Record only the unique individuals in the path
        paths.append(population)

    logging.info("Artificial Immune Network optimization finished")
    best_individual = min(population, key=function)
    output = f'Best finding minimum: [X: {best_individual[0]:.2f}, Y: {best_individual[1]:.2f}], Z: {function(best_individual):.2f}'
    return np.array(paths), output
