from pyIpnHeuristic.harmonySearch import HarmonySearch
from pyIpnHeuristic.benchmark import get_pg06


def test_harmony_search():

    problem_parameters = get_pg06()
            
    harmony_search = HarmonySearch(
        problem_parameters.get("objective_function"),
        soft_constrains=problem_parameters.get("gx"),
        hard_constrains=problem_parameters.get("hx"),
        ranges=problem_parameters.get("ranges"),
        population_size=5,
        hcmr=0.95,
        par=0.10,
        epsilon=10**-4,
        alpha=10**-2
    )

    harmony_search.search(iterations=10000, save_history=True)

    print(harmony_search.history[-1])
    
    return harmony_search.population
