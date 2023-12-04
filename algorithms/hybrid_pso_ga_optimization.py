import numpy as np

from algorithms.genetic_algorithm import genetic_algorithm
from algorithms.particle_swarm_optimization import particle_swarm_optimization


def hybrid_pso_ga_optimization(function, initial_points, pso_iterations=100, ga_iterations=30, w=0.5, c1=1, c2=1,
                               mutation_rate=0.02, mutation_scale=0.1):
    """
    Hybrid Particle Swarm Optimization and Genetic Algorithm.

    :param function: The function to be minimized.
    :param initial_points: Initial points for the algorithm.
    :param pso_iterations: Number of iterations for the PSO phase.
    :param ga_iterations: Number of iterations for the GA phase.
    :param w: Inertia weight for PSO.
    :param c1: Cognitive coefficient for PSO.
    :param c2: Social coefficient for PSO.
    :param mutation_rate: Probability of mutation for GA.
    :param mutation_scale: Scale of normal distribution for mutation in GA.
    :return: The best position and value found by the hybrid algorithm.
    """

    # PSO Phase
    pso_paths, _ = particle_swarm_optimization(function, initial_points, n_iterations=pso_iterations, w=w, c1=c1, c2=c2)
    pso_final_positions = [path[-1] for path in pso_paths]

    # GA Phase
    ga_paths, ga_output = genetic_algorithm(function, pso_final_positions, num_generations=ga_iterations,
                                            mutation_rate=mutation_rate, mutation_scale=mutation_scale)

    combined_paths = np.concatenate((pso_paths, ga_paths), axis=1)

    return combined_paths, ga_output
