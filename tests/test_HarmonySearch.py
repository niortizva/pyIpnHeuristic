from pyIpnHeuristic.harmonySearch import HarmonySearch
from pyIpnHeuristic.benchmark import get_pg01


def test_harmony_search():

    problem_parameters = get_pg01()
            
    harmony_search = HarmonySearch(
        problem_parameters.get("objective_function"),
        soft_constrains=problem_parameters.get("gx"),
        hard_constrains=problem_parameters.get("hx"),
        ranges=problem_parameters.get("ranges"),
        population_size=2,
        hcmr=0.95,
        par=0.10,
        epsilon=10**-4,
        alpha=10**-2
    )

    harmony_search.search(iterations=100000, save_history=True)
    
    return harmony_search.population
