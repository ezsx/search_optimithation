import numpy as np
import random
import logging


def bee_swarm_optimization(function, points, num_generations=50, num_scouts=5, limit=10):
    """
    Performs a Bee Swarm Optimization (BSO) algorithm for optimization.

    :param function: The function to be optimized.
    :param points: Initial points for the population.
    :param num_generations: Number of generations to run the BSO algorithm.
    :param num_scouts: Number of scout bees to be used.
    :param limit: The limit for the abandonment counter.
    :return: A list of arrays representing the paths taken by the BSO algorithm.
             A string representing the best finding minimum.
    """
    population = points
    num_individuals = len(population)
    paths = []
    trial_counters = np.zeros(num_individuals)  # Counter for abandonment

    for _ in range(num_generations):
        # Fitness calculation (adjusted for minimization)
        fitnesses = np.array([1 / (1 + function(individual)) for individual in population])

        # Employed bee phase
        for i in range(num_individuals):
            candidate = mutation(population[i], np.random.rand())
            if function(candidate) < function(population[i]):
                population[i] = candidate
                trial_counters[i] = 0
            else:
                trial_counters[i] += 1

        # Calculate probabilities for onlooker bees
        fitness_sum = np.sum(fitnesses)
        probabilities = fitnesses / fitness_sum if fitness_sum != 0 else np.ones(num_individuals) / num_individuals

        # Onlooker bee phase
        for _ in range(num_individuals):
            i = np.random.choice(range(num_individuals), p=probabilities)
            candidate = mutation(population[i], np.random.rand())
            if function(candidate) < function(population[i]):
                population[i] = candidate
                trial_counters[i] = 0
            else:
                trial_counters[i] += 1

        # Scout bee phase
        scouts_indices = np.where(trial_counters > limit)[0]
        for i in scouts_indices:
            population[i] = np.random.uniform(np.min(points, axis=0), np.max(points, axis=0))
            trial_counters[i] = 0

        paths.append(population.copy())

    logging.info("Bee Swarm Optimization algorithm finished")
    best_index = np.argmin([function(individual) for individual in population])
    best_individual = population[best_index]
    output = f'Best finding minimum: [X: {best_individual[0]:.2f}, Y: {best_individual[1]:.2f}],' \
             f' Z: {function(best_individual):.2f}'
    return np.array(paths), output


# Just example mutation function, can be enhanced in the future
def mutation(individual, mutation_scale):
    """
    Mutates an individual.

    :parameter
    ----------
    individual (List): The individual to be mutated.
    mutation_scale (float): Scale of the uniform distribution for mutation.

    :return
    -------
    List: The mutated individual.
    """
    return individual + mutation_scale * (np.random.uniform(-1, 1, size=individual.shape))

