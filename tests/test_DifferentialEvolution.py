from pyIpnHeuristic.differentialEvolution import DifferentialEvolution
from pyIpnHeuristic.benchmark import get_pg06


def test_differential_evolution():

    objective_function, g, h, ranges = get_pg06()
            
    differential_evolution = DifferentialEvolution(
        objective_function,
        soft_constrains=g,
        hard_constrains=h,
        ranges=ranges,
        population_size=4,
        f=0.50,
        cr=0.10,
        epsilon=10**-4,
    )

    differential_evolution.search(iterations=100000, save_history=True)
    
    return differential_evolution.population
