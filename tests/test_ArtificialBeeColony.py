from pyIpnHeuristic.artificialBeeColony import ArtificialBeeColony
from pyIpnHeuristic.benchmark import get_pg06


def test_artificial_bee_colony():
    problem_parameters = get_pg06()

    artificial_bee_colony = ArtificialBeeColony(
        problem_parameters.get("objective_function"),
        soft_constrains=problem_parameters.get("gx"),
        hard_constrains=problem_parameters.get("hx"),
        ranges=problem_parameters.get("ranges"),
        population_size=5,
        mr=0.3,
        max_trials=3,
        epsilon=10 ** -4,
    )

    artificial_bee_colony.search(iterations=200000, save_history=False)

    print(artificial_bee_colony.population[-1])

    return artificial_bee_colony.population
