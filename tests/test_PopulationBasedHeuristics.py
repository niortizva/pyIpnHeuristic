from pyIpnHeuristic import PopulationBasedHeuristics
from pyIpnHeuristic.examples import get_pg06


def objective_function(*x):
    return (x[0] - 10)**3 + (x[1] - 20)**3

def g1(*x):
    return -(x[0] - 5)**2 - (x[1] - 5)**2 + 100

def g2(*x):
    return (x[0] - 6)**2 + (x[1] - 5)**2 - 82.81


def test_populationBasedHeuristics():

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
