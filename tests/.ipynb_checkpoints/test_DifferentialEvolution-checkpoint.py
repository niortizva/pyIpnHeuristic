from pyIpnHeuristic.differentialEvolution import DifferentialEvolution
from pyIpnHeuristic.examples import get_pg06


def test_differentialEvolution():

    objective_function, g, h, ranges = get_pg06()

    ranges = [[13, 100], [0, 100]]
            
    differentialEvolution = DifferentialEvolution(
        objective_function,
        soft_constrains=g,
        hard_constrains=h,
        ranges=ranges,
        population_size=4,
        f=0.50,
        cr=0.10,
        epsilon=10**-4,
    )

    differentialEvolution.search(iterations=100000, save_history=True)
    
    return differentialEvolution.population
