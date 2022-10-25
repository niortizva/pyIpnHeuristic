from pyIpnHeuristic.modifiedHarmonySearch import ModifiedHarmonySearch
from pyIpnHeuristic.benchmark import get_pg06


def test_harmony_search():
    problem_parameters = get_pg06()

    modified_harmony_search = ModifiedHarmonySearch(
        problem_parameters.get("objective_function"),
        soft_constrains=problem_parameters.get("gx"),
        hard_constrains=problem_parameters.get("hx"),
        ranges=problem_parameters.get("ranges"),
        population_size=5,
        hcmr=0.95,
        par=0.10,
        epsilon=10 ** -4,
        alpha=10 ** -2
    )

    modified_harmony_search.search(iterations=2, save_history=False)

    print(modified_harmony_search.population[-1])

    return modified_harmony_search.population
