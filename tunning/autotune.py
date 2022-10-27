from pyIpnHeuristic.modifiedHarmonySearch import ModifiedHarmonySearch
from pyIpnHeuristic.artificialBeeColony import ArtificialBeeColony
from pyIpnHeuristic.particleSwarmOptimization import ParticleSwarmOptimization
from pyIpnHeuristic.differentialEvolution import DifferentialEvolution
from pyIpnHeuristic.harmonySearch import HarmonySearch
from pyIpnHeuristic.hybridModifiedPsoAndEd import HybridModifiedPsoAndEd
from pyIpnHeuristic.benchmark import\
    get_pg01, get_pg02, get_pg03, get_pg04,\
    get_pg05, get_pg06, get_pg07, get_pg08,\
    get_pg09, get_pg10, get_pg11, get_pg12,\
    get_pg13, get_pg14, get_pg15, get_pg16,\
    get_pg17, get_pg18, get_pg19, get_pg20,\
    get_pg21, get_pg22, get_pg23, get_pg24
import json


def tune_function(algorithm, problem_parameters, pop_size, params):
    def objective_function(*x, get_algorithm=False):
        # iterations = 5 * 10**3
        iterations = 50
        algorithm_params = {key: xi for param, xi in zip(params, x) for key in param.keys()}
        algorithm_class = algorithm["class"](
            problem_parameters[1].get("objective_function"),
            soft_constrains=problem_parameters[1].get("gx"),
            hard_constrains=problem_parameters[1].get("hx"),
            ranges=problem_parameters[1].get("ranges"),
            population_size=pop_size,
            epsilon=10 ** -4,
            smooth=True,
            max_fes=5 * 10**9,
            **algorithm_params
        )

        algorithm_class.search(iterations=iterations, save_history=True)
        best = algorithm_class.history[-1]
        error = abs(best["fx"] - problem_parameters[1]["fx"]) / abs(problem_parameters[1]["fx"])
        if get_algorithm:
            return algorithm_class
        else:
            return error

    return objective_function


def tuning():
    problems = [("pg01", get_pg01()), ("pg02", get_pg02()), ("pg03", get_pg03()), ("pg04", get_pg04()),
                ("pg05", get_pg05()), ("pg06", get_pg06()), ("pg07", get_pg07()), ("pg08", get_pg08()),
                ("pg09", get_pg09()), ("pg10", get_pg10()), ("pg11", get_pg11()), ("pg12", get_pg12()),
                ("pg13", get_pg13()), ("pg14", get_pg14()), ("pg15", get_pg15()), ("pg16", get_pg16()),
                ("pg17", get_pg17()), ("pg18", get_pg18()), ("pg19", get_pg19()), ("pg20", get_pg20()),
                ("pg21", get_pg21()), ("pg22", get_pg22()), ("pg23", get_pg23()), ("pg24", get_pg24())]

    problems_populations = [13, 20, 10, 5, 4, 4, 10, 4, 7, 8, 4, 4, 5, 10, 4, 5, 6, 9, 15, 24, 7, 22, 9, 4]

    algorithms = [
        {
            "name": "Artificial Bee Colony",
            "class": ArtificialBeeColony,
            "params": [
                {"mr": [0, 1]},
            ]
        },
        {
            "name": "Particle Swarm Optimization",
            "class": ParticleSwarmOptimization,
            "params": [
                {"w": [0, 1]},
                {"c1": [0, 2]},
                {"c2": [0, 2]}
            ]
        },
        {
            "name": "Differential Evolution",
            "class": DifferentialEvolution,
            "params": [
                {"f": [-1, 1]},
                {"cr": [0, 1]},
            ]
        },
        {
            "name": "Harmony Search",
            "class": HarmonySearch,
            "params": [
                {"hcmr": [0, 1]},
                {"par": [0, 1]},
                {"alpha": [-1, 1]},
            ]
        },
        {
            "name": "Hybrid Modified PSO with Differential Evolution",
            "class": HybridModifiedPsoAndEd,
            "params": [
                {"w": [0, 1]},
                {"c1": [0, 2]},
                {"c2": [0, 2]},
                {"f": [0, 1]},
                {"cr": [0, 1]},
            ]
        },
    ]

    tunner_json = []

    for algorithm in algorithms:
        for problem_parameters, population_size in zip(problems, problems_populations):
            objective_function = tune_function(algorithm, problem_parameters, population_size,
                                               algorithm["params"])
            algorithm_params_ranges = [value for param in algorithm["params"] for value in param.values()]
            tunner = ModifiedHarmonySearch(
                objective_function,
                soft_constrains=[],
                hard_constrains=[],
                ranges=algorithm_params_ranges,
                population_size=5,
                hcmr=0.95,
                par=0.10,
                epsilon=10 ** -4,
                alpha=10 ** -2
            )
            tunner.search(iterations=200, save_history=True)
            solution = tunner.population[-1]["x"]
            solution_params = {key: float("{:.4f}".format(xi)) for param, xi in zip(algorithm["params"], solution)
                               for key in param.keys()}
            algorithm_class = objective_function(*solution, get_algorithm=True)
            _error = abs(problem_parameters[1]["fx"] - problem_parameters[1]["objective_function"](
                *algorithm_class.history[-1]["x"])) / abs(problem_parameters[1]["fx"])
            print(r"""algorithm: {}, problem: {}, error: {:.3f} % - Done!""".format(
                algorithm["name"], problem_parameters[0], 100 * _error))
            tunner_json.append({
                "algorithm": algorithm["name"],
                "problem_name": problem_parameters[0],
                "population_size": population_size,
                "error": objective_function(*tunner.history[-1]["x"]),
                "*fx": problem_parameters[1]["fx"],
                "fx": problem_parameters[1]["objective_function"](
                    *algorithm_class.history[-1]["x"]),
                "solution": {**solution_params},
            })

    # Serializing json
    json_object = json.dumps(tunner_json, indent=4)

    # Writing to sample.json
    with open("tunner_json.json", "w") as tunner_json_file:
        tunner_json_file.write(json_object)


if __name__ == "__main__":
    tuning()
