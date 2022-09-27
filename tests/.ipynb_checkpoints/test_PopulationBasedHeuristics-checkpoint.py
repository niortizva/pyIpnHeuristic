from pyIpnHeuristic import PopulationBasedHeuristics
from pyIpnHeuristic.benchmark import get_pg06


def test_population_based_heuristics():

    objective_function, g, h, ranges = get_pg06()
    
    # Test Algorithm Class
    class Algorithm(PopulationBasedHeuristics):
        def __init__(self, *arg, **args):
            super().__init__(*arg, **args)
            
    ranges = [[13, 100], [0, 100]]
            
    algorithm = Algorithm(
        objective_function,
        soft_constrains=g,
        hard_constrains=h,
        ranges=ranges,
        population_size=2
    )
    
    p = algorithm.create_population()
    
    return p, algorithm.evaluate_population(p)
