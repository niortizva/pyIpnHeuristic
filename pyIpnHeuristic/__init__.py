from abc import abstractmethod
from functools import reduce
from typing import Callable, Any, List
import random
from .benchmark import *
from copy import copy


class PopulationBasedHeuristics(object):
    """
    Population Based Heuristic Algorithm Template Class.
    """

    def __init__(self, objective_function: Callable[..., Any], soft_constrains: List[Callable[..., Any]] = None,
                 hard_constrains: List[Callable[..., Any]] = None, ranges: list = None, population_size: int = 32,
                 smooth: bool = False, epsilon: float = 10**-4, **params):
        r"""
        Initialize Population Based Heuristic algorithm.
        
        e.g.,
        
        objective_function:
        
        .. code-block:: python
            def objective_function(*x):
                return x[0]**2 + x_[1]**2
        
        soft_constrains $g_{i} (x) <= 0$:

        .. code-block:: python
            def g1(*x) -> float or int:
                return x[0]
                
            def g2(*x) -> float or int:
                return x[1]
            
            soft_constrains = [g1, g2]
        
        hard_constrains $h_{i} (x) == 0$:

        .. code-block:: python
            def h1(*x) -> float or int:
                return x[0]
                
            def h2(*x) -> float or int:
                return x[1]
            
            hard_constrains = [h1, h2]
            
        ranges:
            
            variables ranges:
        
        .. code-block:: python
            ranges = [[0, 100], [0, 90]]

        :param FunctionType objective_function: Method to evaluate objective function
        :param list[FunctionType] soft_constrains: List of Soft constrains methods
        :param list[FunctionType] hard_constrains: List of Hard constrains methods
        :param list[list[float, float]] ranges: List of variables ranges
        :return None:
        """
        self.objective_function = objective_function
        self.soft_constrains = soft_constrains
        self.hard_constrains = hard_constrains
        self.ranges = ranges
        self.dimension = len(ranges)
        self.population_size = population_size
        self.population: List[dict] = []
        self.history: List[dict] = []
        self.smooth: bool = smooth
        self.epsilon: float = epsilon
        self.custom_population: list = []
        self.function_evaluations: int = 0
        self.max_function_evaluations: int = params.get("max_fes", 10**10)
        
        # Check if population has enough size
        if self.population_size <= 0:
            raise ValueError("""
            Population size is not valid. Population size
            must be greater than 0
            """)

    def set_custom_population(self, custom_population: list) -> None:
        """
        Sets custom initial population
        :custom_population list: Custom initial population
        :return None:
        """
        self.custom_population = custom_population
        
    def create_individual(self) -> dict:
        """
        Creates individual randomly
        :return dict: Random individual
        """
        return {
            "x": [random.uniform(min(ri), max(ri))
                  for ri in self.ranges],
            "fx": None,
            "gx": None,
            "hx": None,
        }
    
    def fix_ranges(self, individual: dict) -> dict:
        """
        Fix ranges of an individual

        Checks if and individual is in the search space, if not replace it with a new random one
        :param dict individual: Individual
        :return dict: Fixed Individual
        """
        for j in range(self.dimension):
            sup = max(self.ranges[j])
            inf = min(self.ranges[j])
            x_j = individual["x"][j]
            if x_j < inf or x_j > sup:
                individual["x"][j] = random.uniform(inf, sup)
        return individual
        
    def create_population(self) -> List[dict]:
        r"""
        Creates population randomly
        
        e.g.,
        
        [
            { "x": [0.10, 0.20], fx: None, gx: None, hx: None },
            { "x": [0.05, 0.02], fx: None, gx: None, hx: None },
            { "x": [0.85, 0.72], fx: None, gx: None, hx: None }
        ]
        :custom_population list: Custom population
        :return list[dict]: Random population
        """
        if self.custom_population:
            return self.custom_population
        return [
            self.create_individual()
            for _ in range(self.population_size)
        ]
    
    def evaluate_population(self, population: List[dict]) -> List[dict]:
        r"""
        Evaluates objective function and constrains for a given population
        
        e.g.,

        Population:
        .. code-block:: json
        [
            { "x": [0.10, 0.20], fx: None, gx: None, hx: None },
            { "x": [0.05, 0.02], fx: None, gx: None, hx: None },
            { "x": [0.85, 0.72], fx: None, gx: None, hx: None }
        ]

        Evaluated population:

        .. code-block:: json
        [
            { "x": [0.10, 0.20], fx: 10.340, gx: 0, hx: 3.282 },
            { "x": [0.05, 0.02], fx: 1.0010, gx: 0, hx: -0.01 },
            { "x": [0.85, 0.72], fx: -35.02, gx: 0, hx: 5.439 }
        ]
        :return list[dict]: Return evaluated population
        """
        return list(map(self.evaluate_individual, population))

    def update_fes(self):
        self.function_evaluations += 1
    
    def evaluate_individual(self, individual: dict) -> dict:
        """
        Evaluates objective function and constrains for a single individual
        :param dict individual: Individual
        :return dict: Evaluated Individual
        """
        self.update_fes()
        individual["fx"] = self.objective_function(*individual["x"])
        individual["gx"] = sum([gi(*individual["x"]) * (gi(*individual["x"]) > 0)
                               for gi in self.soft_constrains])
        if self.smooth:
            individual["hx"] = sum([(abs(hi(*individual["x"])) - self.epsilon) * 
                                    (abs(hi(*individual["x"])) > self.epsilon)
                                    for hi in self.hard_constrains])
        else:
            individual["hx"] = sum([abs(hi(*individual["x"])) * (hi(*individual["x"]) != 0) 
                                    for hi in self.hard_constrains])
        individual["fes"] = copy(self.function_evaluations)
            
        return individual

    def get_best(self, population: List[dict], exclude_list: list = []) -> dict:
        """
        Gets the best individual for a given population using DEB conditions
        :population List[dict]: Population list
        :exclude_list list: List of excluded indexes
        :return dict: Best individual
        """
        pop = [{**population[j], "index": j} for j in range(len(population))
               if j not in exclude_list]
        return reduce(self.comparison, pop)
    
    @staticmethod
    def comparison(xi: dict, xj: dict) -> dict:
        """
        Compares to vectors evaluating DEB conditions
        :param dict xi: Vector i
        :param dict xj: Vector j
        :return dict: Return best vector based on DEB conditions
        """
        svr_i = xi["gx"] + xi["hx"]
        svr_j = xj["gx"] + xj["hx"]
        if svr_i <= 0 and svr_j <= 0:
            if xi["fx"] < xj["fx"]:
                return xi
            else:
                return xj
        elif svr_i > 0 and svr_j > 0:
            if svr_i < svr_j:
                return xi
            else:
                return xj
        else:
            if svr_i <= 0:
                return xi
            else:
                return xj
            
    @abstractmethod
    def population_enhancement(self) -> None:
        pass
    
    @abstractmethod
    def stop_condition(self) -> None:
        pass
    
    def save_history(self, iteration: int) -> None:
        """
        Save search data
        :param int iteration: Current iteration
        :return None:
        """
        best_individual = self.get_best(self.population)
        self.history.append({**best_individual, "iteration": iteration + 1,
                             "fes": self.function_evaluations})
    
    def search(self, iterations: int = 100, save_history: bool = False):
        """
        Search method
        :param int iterations: Number of iterations
        :param bool save_history: If True algorthm will store each iteration data
        :return None:
        """
        self.history = []
        initial_population = self.create_population()
        self.population = copy(self.evaluate_population(initial_population))
        for iteration in range(iterations):
            if self.stop_condition():
                break
            self.population_enhancement()
            if save_history:
                self.save_history(iteration)
            if self.function_evaluations > self.max_function_evaluations:
                break


if __name__ == "__main__":
    pass
    