from pyIpnHeuristic.artificialBeeColony import ArtificialBeeColony
from pyIpnHeuristic.benchmark import get_pg06


def test_artificial_bee_colony():
    problem_parameters = get_pg06()

    artificial_bee_colony = ArtificialBeeColony(
        problem_parameters.get("objective_function"),
        soft_constrains=problem_parameters.get("gx"),
        hard_constrains=problem_parameters.get("hx"),
        ranges=problem_parameters.get("ranges"),
        population_size=4,
        mr=0.5,
        smooth=True,
        max_trials=4,
        epsilon=10 ** -4,
    )

    artificial_bee_colony.search(iterations=10000, save_history=True)

    print(artificial_bee_colony.history[-1])

    return artificial_bee_colony.population
