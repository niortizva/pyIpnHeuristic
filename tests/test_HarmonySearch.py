from pyIpnHeuristic.harmonySearch import HarmonySearch
from pyIpnHeuristic.benchmark import get_pg06


def test_harmony_search():

    objective_function, g, h, ranges = get_pg06()
            
    harmony_search = HarmonySearch(
        objective_function,
        soft_constrains=g,
        hard_constrains=h,
        ranges=ranges,
        population_size=2,
        hcmr=0.95,
        par=0.10,
        epsilon=10**-4,
        alpha=10**-2
    )

    harmony_search.search(iterations=100000, save_history=True)
    
    return harmony_search.population
