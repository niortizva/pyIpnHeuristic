from . import PopulationBasedHeuristics
from random import random, uniform
from copy import copy


class ParticleSwarmOptimization(PopulationBasedHeuristics):
    """
    Particle Swarm Optimization Algorithm
    """

    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        # Particle Swarm Optimization
        self.w = params.get("w", 0.1)
        self.c1 = params.get("c1", 0.2)
        self.c2 = params.get("c2", 0.2)
        # Initialize Population Velocity
        self.velocity = []
        self.particles_best_values = []

    def compute_velocity(self, xi_best_value: dict, xi: dict, vi: list, g: dict) -> list:
        """
        Computes new velocity
        :xi_best_value dict: Best particle value
        :xi dict: Current particle
        :vi list: Current particle velocity
        :g dict: Current best particle
        :return list: new velocity
        """
        return [self.w * vi[j] +
                self.c1 * random() * (xi_best_value["x"][j] - xi["x"][j]) +
                self.c2 * random() * (g["x"][j] - xi["x"][j]) for j in range(self.dimension)]

    def population_enhancement(self) -> None:
        """
        Population Enhancement Method
        :return None:
        """
        if len(self.velocity) == 0:
            self.velocity = [[uniform(-abs(max(ri) - min(ri)), abs(max(ri) - min(ri)))
                              for ri in self.ranges] for _ in self.population]
            self.particles_best_values = [particle for particle in self.population]

        # Get best vector
        g = self.get_best(self.population)

        # Calculate new particle velocity
        self.velocity = copy([
            self.compute_velocity(xi_best_value, xi, vi, g)
            for xi_best_value, xi, vi in zip(self.particles_best_values, self.population, self.velocity)])

        # Calculate new particle position
        self.population = copy(self.evaluate_population([
            self.fix_ranges({
                "x": [xi["x"][j] + vi[j] for j in range(self.dimension)]
            }) for xi, vi in zip(self.population, self.velocity)]))

        # Update particles best values
        self.particles_best_values = copy([
            self.comparison(pi, xi) for pi, xi in zip(self.particles_best_values, self.population)])

    def stop_condition(self) -> bool:
        return False


if __name__ == "__main__":
    pass
