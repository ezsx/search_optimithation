# 3

### Theory Behind Genetic Algorithms (GAs)

Genetic Algorithms (GAs) are a family of computational algorithms inspired by the principles of natural selection and genetics. These algorithms emulate the process of evolution, where the fittest individuals are selected for reproduction to produce the next generation of solutions. GAs are particularly useful in optimization and search problems, where they evolve solutions to complex problems through mechanisms akin to biological evolution.

### Key Concepts in Genetic Algorithms

GAs are built on several key concepts derived from evolutionary biology:

1. **Population**: A set of potential solutions, where each individual represents a point in the solution space.
2. **Fitness**: A measure of how good a solution is, often determined by an objective or cost function.
3. **Selection**: A process to choose individuals based on their fitness to create offspring for the next generation.
4. **Crossover (Recombination)**: Combining parts of two or more individuals to create new offspring.
5. **Mutation**: Introducing random changes to an individual to maintain diversity within the population and explore new solution spaces.

### Implementation of Genetic Algorithm

The provided genetic algorithm code is an implementation of these principles, tailored for optimization problems:

1. **Initialization**: The algorithm starts with an initial population of solutions (`points`), representing different candidates.

2. **Fitness Calculation**: Each individual's fitness is calculated based on the provided function. In optimization, fitness often corresponds to how well a solution minimizes or maximizes the objective function.

3. **Selection - Tournament Selection**: This step involves selecting individuals for reproduction. Tournament selection randomly chooses a subset of the population and selects the best among them based on fitness. This process is repeated to select parents.

4. **Crossover - Uniform Crossover**: Offspring are created by combining features of two parents. In uniform crossover, each gene (solution component) is chosen from either parent with a certain probability (`crossover_rate`), creating a mix of both parents' traits.

5. **Mutation**: To introduce variability and avoid premature convergence, offspring may undergo mutation with a certain probability (`mutation_rate`). Mutation involves altering some genes of the offspring, guided by a normal distribution (`mutation_scale`).

6. **Generation Update**: After creating a new generation of solutions, the process of evaluation, selection, crossover, and mutation repeats for a specified number of generations (`num_generations`).

7. **Termination and Output**: The algorithm concludes after the predetermined number of generations. The best solution found during these iterations is reported as the output, showcasing the path the algorithm took to reach this solution.

In the implementation provided, the GA is designed for minimization problems, where the fitness is inversely related to the function's value. The algorithm's effectiveness in finding optimal or near-optimal solutions stems from its ability to balance exploration (searching new areas) and exploitation (refining existing solutions) of the search space.

# 4

### Theory Behind Particle Swarm Optimization (PSO)

Particle Swarm Optimization (PSO) is a computational method used for finding optimal solutions in various types of problems. It is inspired by the social behavior of birds and fish. In PSO, each individual, referred to as a "particle," represents a potential solution in a multi-dimensional space. The movement of these particles is guided by their own experience and the experience of their companions, mimicking the social behavior of flocks or schools.

### Principles of PSO

The fundamental principles of PSO are based on the following concepts:

1. **Particle Representation**: Each particle in the swarm represents a potential solution.
2. **Velocity**: Particles move through the solution space with a velocity that dynamically adjusts based on their experience and that of their neighbors.
3. **Position Update**: The position of each particle is updated based on its velocity, reflecting the search for better solutions.
4. **Personal Best**: Every particle remembers the best position it has ever visited, which guides its future movements.
5. **Global Best**: The best position found by any particle in the swarm influences the movement of all particles.

### Implementation of PSO Algorithm

In the provided PSO algorithm, the process of finding the optimal solution involves the following steps:

1. **Initialization**: The swarm of particles is initialized with random positions and velocities. The number of particles and their dimensionality are defined by the input parameters.

2. **Evaluation**: Each particle's position is evaluated using a provided objective function to determine the quality of the solution.

3. **Update Personal and Global Bests**: Particles update their personal best position if their new position is better. The best of these positions is considered the global best.

4. **Velocity Update**: Each particle's velocity is updated based on a combination of its current velocity, the distance from its personal best, and the distance from the global best. This update includes random factors to introduce diversity in the search.

5. **Position Update**: Particles move to new positions based on their updated velocities, searching for better solutions.

6. **Iteration**: The evaluation, update, and movement steps are repeated for a set number of iterations, allowing the swarm to explore the solution space.

7. **Termination**: The algorithm stops after a predetermined number of iterations. The best solution found during these iterations is reported.

In the given implementation, the PSO algorithm is adaptable to a variety of optimization problems. It leverages parameters like inertia weight, cognitive coefficient, and social coefficient to balance exploration and exploitation in the search process. The algorithm's effectiveness lies in its simplicity and ability to find good solutions in complex search spaces.



# 5

### Theory Behind Bee Swarm Optimization

Bee Swarm Optimization (BSO), more commonly known as Artificial Bee Colony (ABC), is an optimization algorithm inspired by the intelligent foraging behavior of honey bees. It was introduced by Karaboga in 2005 to optimize numerical problems. The algorithm simulates the process of bees finding and exploiting food sources, which in the context of optimization, corresponds to finding the optimal solutions in a search space.

In nature, honey bees are divided into three groups based on their roles:

1. **Employed Bees**: They are associated with specific food sources and their primary role is to exploit these sources. In BSO, they represent solutions that are being improved upon iteration by iteration.

2. **Onlooker Bees**: They wait in the hive and choose food sources based on information shared by employed bees. They represent a probabilistic selection of solutions based on fitness, where better solutions have higher chances of being selected for further exploration.

3. **Scout Bees**: They are sent out to find new food sources when existing ones are exhausted. In BSO, they represent random search for new solutions when current solutions cannot be improved further, preventing the algorithm from being stuck in local optima.

The algorithm has a few key steps:

- **Initialization**: A population of solutions (food sources) is generated randomly.
  
- **Employed Bee Phase**: Each employed bee evaluates the fitness of its solution and then attempts to find a better solution (nectar amount) in its neighborhood. If successful, the bee memorizes the new solution and forgets the old one.

- **Onlooker Bee Phase**: After all employed bees have completed their search, they share the nectar information with onlooker bees. Onlookers then probabilistically choose food sources (solutions) to exploit, favoring those with higher nectar (better fitness).

- **Scout Bee Phase**: If a food source becomes depleted (the solution cannot be improved further for a certain number of trials), the employed bee associated with it becomes a scout and randomly searches for a new food source (new random solution).

- **Abandonment and Replacement**: If a solution cannot be improved upon within a specified limit (known as the "limit" in the algorithm), it is abandoned, and a new solution is generated randomly to replace it.

### Implementation

The implementation of BSO in Python follows the above theoretical framework:

1. **Initialization**: The initial population is generated based on provided points.

2. **Fitness Evaluation**: The fitness of each individual is calculated. For minimization problems, fitness is often taken as the reciprocal of the function value.

3. **Employed Bee Phase**: Solutions are mutated slightly to explore their neighborhood. If the new solution is better, it is kept; otherwise, the counter for that solution is increased.

4. **Onlooker Bee Phase**: Solutions are probabilistically selected based on fitness. The same mutation and selection process as in the employed bee phase is applied.

5. **Scout Bee Phase**: Solutions that haven't improved for a number of iterations beyond the `limit` are replaced with new random solutions, simulating the scout bee's behavior.

6. **Abandonment and Replacement**: Solutions that can't be improved are replaced, ensuring diversity in the population and avoiding local optima.

7. **Output Generation**: The paths (historical best solutions) and the final best solution are returned. This output can be used for analysis or visual representation of the algorithm's performance.

By maintaining a balance between local exploitation and global exploration, BSO can effectively navigate the search space and often find good solutions to complex optimization problems.

# 6

### Theory Behind Artificial Immune Systems (AIS)

Artificial Immune Systems (AIS) are a class of biologically inspired computing algorithms based on the principles and processes of the vertebrate immune system. The immune system is a robust, adaptive system that learns to recognize and combat pathogens. AIS algorithms take inspiration from this system, particularly the mechanisms of recognition, learning, and memory. One of the key concepts in AIS is the clonal selection principle, which explains how the immune system adapts to new, unknown pathogens by selecting and cloning certain types of immune cells that can recognize and neutralize these threats.

### Clonal Selection Principle

The clonal selection principle forms the basis of several AIS algorithms, including the clonal selection algorithm and the artificial immune network (AIN) algorithm. It involves the following steps:

1. **Recognition**: Detection of pathogens by immune cells (antibodies).
2. **Selection**: Selection of those immune cells that can recognize the pathogens effectively.
3. **Cloning**: Cloning of the selected cells.
4. **Mutation**: Introduction of mutations in the cloned cells to create a diverse set of cells.
5. **Memory**: Retention of the most effective cells for faster response in the future.

### Implementation of AIS Algorithm

In the context of optimization problems, the AIS algorithm can be seen as a metaphor where the solutions to the problem are akin to the antibodies, and the objective function represents the antigen. The algorithm aims to evolve a set of solutions that are best suited to minimize (or maximize) the objective function.

Here is how the AIS algorithm is implemented, inspired by the clonal selection principle:

1. **Initialization**: A population of candidate solutions (antibodies) is randomly generated within the search space.

2. **Affinity Calculation**: The affinity (or fitness) of each candidate solution is evaluated based on the objective function. In optimization, higher affinity corresponds to better solutions.

3. **Clonal Selection**: Based on their affinity, candidate solutions are selected to undergo cloning. This step promotes the propagation of higher-quality solutions.

4. **Hypermutation**: Clones of the candidate solutions are subjected to a mutation process, which introduces variations. The rate of mutation is typically inversely proportional to the affinity — better solutions undergo fewer mutations to preserve their quality, while worse solutions are more drastically altered in the hope of discovering better ones.

5. **Selection**: After mutation, the population is reassessed, and a subset of the best-performing solutions is selected to form the new generation.

6. **Diversity Introduction**: To avoid premature convergence to local optima, some degree of diversity is introduced by randomly replacing a portion of the population with new candidate solutions.

7. **Iteration**: The process is repeated for a number of generations, or until a convergence criterion is met.

In the given implementation, the AIS algorithm is particularly tailored for minimization problems. It utilizes a sort operation to rank the mutated clones based on the objective function and selects the best to form the new population. Furthermore, unique solutions are maintained to visualize the convergence process clearly.
