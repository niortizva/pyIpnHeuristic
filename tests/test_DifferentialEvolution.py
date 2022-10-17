from pyIpnHeuristic.differentialEvolution import DifferentialEvolution
from pyIpnHeuristic.benchmark import get_pg06


def test_differential_evolution():

    problem_parameters = get_pg06()
            
    differential_evolution = DifferentialEvolution(
        problem_parameters.get("objective_function"),
        soft_constrains=problem_parameters.get("gx"),
        hard_constrains=problem_parameters.get("hx"),
        ranges=problem_parameters.get("ranges"),
        population_size=10,
        f=0.50,
        cr=0.10,
        epsilon=10**-4,
    )

    differential_evolution.search(iterations=100000, save_history=False)

    print(differential_evolution.population[-1])
    
    return differential_evolution.population
