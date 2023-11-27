import numpy as np
import random


def bacterial_foraging_optimization(function, points, n_iterations=100, step_size=0.1, swim_length=4,
                                    reproduction_rate=0.5, elimination_prob=0.25):
    """
    Bacterial Foraging Optimization Algorithm (BFOA) adapted for the existing application structure.

    :param function: The function to be minimized.
    :param points: Initial points for the bacteria, used to determine the number of bacteria and dimensions.
    :param n_iterations: Number of iterations to run the algorithm.
    :param step_size: Step size for bacteria movement.
    :param swim_length: Length of the swim in chemotaxis step.
    :param reproduction_rate: Rate at which bacteria reproduce.
    :param elimination_prob: Probability of elimination and dispersal.
    :return: The paths of bacteria and a string with the best position and value.
    """
    n_bacteria = len(points)
    n_dimensions = points.shape[1]
    bounds = np.array([np.min(points, axis=0), np.max(points, axis=0)])

    # Initialize bacteria positions
    bacteria = np.copy(points)
    health = np.array([function(bacterium) for bacterium in bacteria])
    best_position = bacteria[np.argmin(health)]
    best_value = np.min(health)

    paths = [np.zeros((n_iterations, n_dimensions)) for _ in range(n_bacteria)]

    for iteration in range(n_iterations):
        # Chemotaxis
        for i in range(n_bacteria):
            for _ in range(swim_length):
                # Tumble and swim
                direction = np.random.uniform(-1, 1, n_dimensions)
                direction /= np.linalg.norm(direction)
                new_position = bacteria[i] + step_size * direction
                new_position = np.clip(new_position, bounds[0], bounds[1])
                new_value = function(new_position)

                if new_value < health[i]:
                    bacteria[i] = new_position
                    health[i] = new_value

                if health[i] < best_value:
                    best_position = bacteria[i]
                    best_value = health[i]

            paths[i][iteration, :] = bacteria[i]

        # Reproduction
        sorted_indices = np.argsort(health)
        surviving = sorted_indices[:n_bacteria // 2]
        bacteria = np.copy(bacteria[surviving])
        health = np.copy(health[surviving])
        bacteria = np.append(bacteria, bacteria, axis=0)  # Duplicate
        health = np.append(health, health, axis=0)

        # Elimination and dispersal
        for i in range(n_bacteria):
            if random.random() < elimination_prob:
                bacteria[i] = np.random.uniform(bounds[0], bounds[1], n_dimensions)
                health[i] = function(bacteria[i])

    output = f'Best finding minimum: [X: {best_position[0]:.2f}, Y: {best_position[1]:.2f}],' \
             f' Z: {best_value:.2f}'

    return paths, output
