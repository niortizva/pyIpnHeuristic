from pyIpnHeuristic.harmonySearch import HarmonySearch
from pyIpnHeuristic.examples import get_pg06


def test_harmonySearch():

    objective_function, g, h, ranges = get_pg06()

    ranges = [[13, 100], [0, 100]]
            
    harmonySearch = HarmonySearch(
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

    harmonySearch.search(iterations=100000, save_history=True)
    
    return harmonySearch.population
