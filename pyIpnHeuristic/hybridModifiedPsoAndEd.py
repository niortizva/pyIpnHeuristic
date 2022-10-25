from . import PopulationBasedHeuristics
from . differentialEvolution import DifferentialEvolution
from random import random, choice
from copy import copy


class HybridModifiedPsoAndEd(PopulationBasedHeuristics):
    """
    Hybrid Modified Particle Swarm Optimization with Differential Evolution Algorithm
    """

    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        # Particle Swarm Parameters
        self.w = params.get("w", 0.1)
        self.c1 = params.get("c1", 0.2)
        self.c2 = params.get("c2", 0.2)
        # Initialize PSO
        self.pso_trials: int = params.get("pso_trials", 5)
        self.index_list = [i for i in range(self.population_size)]
        self.velocity = [[0.0 for _ in range(self.dimension)]
                         for _ in range(self.population_size)]
        # Differential Evolution parameters
        self.differential_evolution = DifferentialEvolution(
            self.objective_function,
            soft_constrains=self.soft_constrains,
            hard_constrains=self.hard_constrains,
            ranges=self.ranges,
            population_size=self.population_size,
            f=params.get("f", 0.5),
            cr=params.get("cr", 0.8),
            epsilon=self.epsilon,
        )
        self.de_trials: int = params.get("de_trials", 5)

        self.index_list = [i for i in range(self.population_size)]

    def compute_velocity(self, xi: dict, vi: list, g1: dict, g2: dict, x_index: int) -> list:
        """
        Computes new velocity
        :xi_best_value dict: The best particle value
        :xi dict: Current particle
        :vi list: Current particle velocity
        :g1 dict: Current best particle
        :g2 dict: Current best particle excluding g1
        :return list: new velocity
        """
        r = choice(list(set(self.index_list) - {x_index}))
        xr = self.population[r]
        v_best = [g1i - g2i for g1i, g2i in zip(g1["x"], g2["x"])]
        v_rand = [xij - xrj for xij, xrj in zip(xi["x"], xr["x"])] if self.comparison(xi, xr) == xi else\
            [xrj - xij for xij, xrj in zip(xi["x"], xr["x"])]
        return [self.w * vi[j] +
                self.c1 * random() * (v_best[j] - vi[j]) +
                self.c2 * random() * (v_rand[j] - vi[j]) for j in range(self.dimension)]

    def update_position(self, xi: dict, vi: list) -> dict:
        """
        Updates Particle Position
        :xi dict: Particle
        :vi list: Particle Velocity
        :return dict: New particle position
        """
        new_position = self.evaluate_individual(self.fix_ranges({
            "x": [xi["x"][j] + vi[j] for j in range(self.dimension)]
        }))
        # Add selection step
        return self.comparison(xi, new_position)

    def population_enhancement(self) -> None:
        """
        Population Enhancement Method
        :return None:
        """
        for _ in range(self.pso_trials):
            # Get best vector
            g1 = self.get_best(self.population)
            g2 = self.get_best(self.population, exclude_list=[g1["index"]])

            # Calculate new particle velocity
            self.velocity = [self.compute_velocity(xi, vi, g1, g2, i)
                             for xi, vi, i in zip(self.population, self.velocity, self.index_list)]

            # Calculate new particle position
            self.population = [self.update_position(xi, vi)
                               for xi, vi in zip(self.population, self.velocity)]

        # Differential Evolution Step
        self.differential_evolution.set_custom_population(self.population)
        self.differential_evolution.search(iterations=self.de_trials)

        self.population = copy(self.differential_evolution.population)

    def stop_condition(self) -> bool:
        return False


if __name__ == "__main__":
    pass
