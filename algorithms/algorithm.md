
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
