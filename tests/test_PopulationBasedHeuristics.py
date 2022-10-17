from pyIpnHeuristic import PopulationBasedHeuristics
from pyIpnHeuristic.benchmark import get_pg01


def test_population_based_heuristics():

    problem_parameters = get_pg01()
    
    # Test Algorithm Class
    class Algorithm(PopulationBasedHeuristics):
        def __init__(self, *arg, **args):
            super().__init__(*arg, **args)

        def population_enhancement(self):
            pass

        def stop_condition(self):
            return False
            
    algorithm = Algorithm(
        problem_parameters.get("objective_function"),
        soft_constrains=problem_parameters.get("gx"),
        hard_constrains=problem_parameters.get("hx"),
        ranges=problem_parameters.get("ranges"),
        population_size=2
    )
    
    p = algorithm.create_population()
    
    return p, algorithm.evaluate_population(p)
