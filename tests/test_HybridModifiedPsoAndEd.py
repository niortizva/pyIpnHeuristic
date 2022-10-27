from pyIpnHeuristic.hybridModifiedPsoAndEd import HybridModifiedPsoAndEd
from pyIpnHeuristic.benchmark import get_pg06


def test_hybrid_modified_pso_and_ed():
    problem_parameters = get_pg06()

    hybrid_modified_pso_and_ed = HybridModifiedPsoAndEd(
        problem_parameters.get("objective_function"),
        soft_constrains=problem_parameters.get("gx"),
        hard_constrains=problem_parameters.get("hx"),
        ranges=problem_parameters.get("ranges"),
        population_size=5,
        w=0.2,
        c1=0.3,
        c2=0.3,
        f=0.1,
        cr=0.8,
        pso_trials=1,
        de_trials=1,
        epsilon=10 ** -4
    )

    hybrid_modified_pso_and_ed.search(iterations=10000, save_history=True)

    print(hybrid_modified_pso_and_ed.history[-1])

    return hybrid_modified_pso_and_ed.population
