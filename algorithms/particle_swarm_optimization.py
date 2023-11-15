def particle_swarm_optimization(function, points, n_iterations=100, w=0.5, c1=1, c2=1):
    """
    Particle Swarm Optimization (PSO) algorithm adapted for the existing application structure.

    :param function: The function to be minimized.
    :param points: Initial points for the particles, used to determine the number of particles and dimensions.
    :param n_iterations: Number of iterations to run the algorithm.
    :param w: Inertia weight, to control the momentum of the particle.
    :param c1: Cognitive coefficient, for particle's own best position.
    :param c2: Social coefficient, for swarm's global best position.
    :return: The paths of particles and a string with the best position and value.
    """
    import numpy as np

    n_particles = len(points)
    n_dimensions = points.shape[1]
    bounds = np.array([np.min(points, axis=0), np.max(points, axis=0)])

    # Initialize the swarm's positions and velocities
    particles = np.random.uniform(bounds[0], bounds[1], (n_particles, n_dimensions))
    velocities = np.random.uniform(-1, 1, (n_particles, n_dimensions))

    # Initialize best positions and values for each particle and the swarm
    personal_best_positions = particles.copy()
    personal_best_values = np.array([function(x) for x in particles])
    global_best_position = personal_best_positions[np.argmin(personal_best_values)]
    global_best_value = np.min(personal_best_values)

    paths = [np.zeros((n_iterations, n_dimensions)) for _ in range(n_particles)]

    for iteration in range(n_iterations):
        for i in range(n_particles):
            # Update each particle's velocity and position
            r1, r2 = np.random.rand(2)
            velocities[i] = (w * velocities[i] +
                             c1 * r1 * (personal_best_positions[i] - particles[i]) +
                             c2 * r2 * (global_best_position - particles[i]))
            particles[i] += velocities[i]

            # Clamp the positions within bounds
            particles[i] = np.clip(particles[i], bounds[0], bounds[1])

            # Update personal and global bests
            current_value = function(particles[i])
            if current_value < personal_best_values[i]:
                personal_best_positions[i] = particles[i]
                personal_best_values[i] = current_value

                if current_value < global_best_value:
                    global_best_position = particles[i]
                    global_best_value = current_value

            # Track the path of each particle
            paths[i][iteration, :] = particles[i]

    output = f'Best finding minimum: [X: {global_best_position[0]:.2f}, Y: {global_best_position[1]:.2f}],' \
             f' Z: {global_best_value:.2f}'

    return paths, output
