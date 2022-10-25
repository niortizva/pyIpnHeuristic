from typing import List
from . import PopulationBasedHeuristics
from random import random, choice, uniform
from copy import copy


class ArtificialBeeColony(PopulationBasedHeuristics):
    """
    Artificial Bee Colony Algorithm
    """

    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        # Artificial Bee Colony parameters
        self.max_trials = params.get("max_trials", 4)
        self.mr = params.get("mr", 0.6)
        self.index_list = [i for i in range(self.population_size)]

    def new_vector(self, xi: dict, i: int) -> dict:
        """
        Generates new vector from a food source xi
        :param dict xi: Current food source
        :param int i: Current food source index
        :return dict: New food source
        """
        r = choice(list(set(self.index_list) - {i}))
        x_rand = self.population[r]
        return self.fix_ranges({
            "x": [xi["x"][j] + uniform(-1, 1) * (xi["x"][j] - x_rand["x"][j]) if random() < self.mr else xi["x"][j]
                  for j in range(self.dimension)]
        })

    def new_vector_from_best(self, xi: dict, x_best: dict) -> dict:
        """
        Generates new vector from a food source xi
        :param dict xi: Current food source
        :param dict x_best: The best current food source
        :return dict: New food source
        """
        return self.fix_ranges({
            "x": [xi["x"][j] + uniform(-1, 1) * (xi["x"][j] - x_best["x"][j]) if random() < self.mr else xi["x"][j]
                  for j in range(self.dimension)]
        })

    def smart_fight(self, xi: dict, x_best: dict, i: int):
        """
        Generates new vector from a food source xi and from a random vector
        :param dict xi: Current food source
        :param dict x_best: The best current food source
        :param int i: Current food source index
        :return dict: New food source
        """
        phi = random()
        r = choice(list(set(self.index_list) - {i}))
        x_rand = self.population[r]
        return self.fix_ranges({
            "x": [xi["x"][j] + phi * (x_rand["x"][j] - xi["x"][j]) +
                  (1 - phi) * (x_best["x"][j] - xi["x"][j])
                  for j in range(self.dimension)]
        })

    def mutation(self) -> List[dict]:
        """
        New candidate solutions generation
        :return List[dict]: Returns new candidate solutions
        """
        return self.evaluate_population([self.new_vector(self.population[i], i)
                                         for i in range(self.population_size)])

    def workers(self, worker_bee: dict, bee: dict) -> dict:
        """
        Compares worker bee against current bee
        :worker_bee dict: Created worker bee
        :bee dict: Current bee
        :return dict: New bee
        """
        if self.comparison(bee, worker_bee)["x"] != bee["x"]:
            return {**worker_bee, "trials": 0}
        else:
            return {
                **bee,
                "trials": bee.get("trials", 0) + 1
            }

    def onlookers(self, bee: dict, best_bee: dict) -> dict:
        """
        Creates and compares onlooker bee against current bee
        :bee dict: Current bee
        :best_bee dict: Current best bee
        :return dict: New bee
        """
        onlooker_bee = self.evaluate_individual(self.new_vector_from_best(bee, best_bee))
        return self.workers(onlooker_bee, bee)

    def scouts(self, bee: dict, best_bee: dict) -> dict:
        """
        Creates and compares scout bee against current bee
        :bee dict: Current bee
        :best_bee dict: Current best bee
        :return dict: New bee
        """
        if bee.get("trials", 0) >= self.max_trials:
            scout_bee = self.new_vector_from_best(bee, best_bee)
            return {**scout_bee, "trials": 0}
        return bee

    def population_enhancement(self) -> None:
        """
        Population Enhancement Method
        :return None:
        """
        # Workers phase
        workers_mutation_matrix = self.mutation()
        workers_population = [self.workers(worker_bee, bee)
                              for worker_bee, bee in zip(workers_mutation_matrix, self.population)]

        # Onlookers phase
        best_bee = self.get_best(workers_population)
        onlookers_population = [self.onlookers(bee, best_bee) for bee in workers_population]

        # Scouts Phase
        best_bee = self.get_best(onlookers_population)
        self.population = self.evaluate_population([self.scouts(bee, best_bee) for bee in self.population])

    def stop_condition(self) -> bool:
        return False


if __name__ == "__main__":
    pass
