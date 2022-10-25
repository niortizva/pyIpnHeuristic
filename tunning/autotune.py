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

DOC = r"""
\\documentclass{{book}}
\\usepackage{{amsmath}}

\\begin{{document}}

{doc}

\\end{{document}}"""

SECTION_TITLE = r"""
\\section*{{{algorithm_name} Achieved Results}}
"""

TABLE_1 = r"""\\begin{{table}}[h!]
    \\centering
    \\begin{{tabular}}{{l l l l}}
        FES & $5 \\times 10^{{3}}$ & $5 \\times 10^{{4}}$ & $5 \\times 10^{{5}}$ \\\\
        \\hline
        Best & {best_10_3:.4f} & {best_10_4:.4f} & {best_10_5:.4f} \\\\
        Median & {median_10_3:.4f} & {median_10_4:.4f} & {meadian_10_5:.4f} \\\\
        Worst & {worst_10_3:.4f} & {worst_10_4:.4f} & {worst_10_5:.4f} \\\\
        $c$ & {c_10_3} & {c_10_4} & {c_10_5} \\\\
        $v$ & {v_10_3:.4f} & {v_10_4:.4f} & {v_10_5:.4f} \\\\
        Mean & {mean_10_3:.4f} & {mean_10_4:.4f} & {mean_10_5:.4f} \\\\
        std & {std_10_3:.4f} & {std_10_4:.4f} & {std_10_5:.4f} \\\\
    \\end{{tabular}}
    \\caption{{Error Values Problem {problem_name}}}
\\end{{table}}"""

TABLE_2 = r"""
\\begin{{table}}[h!]
    \\centering
    \\begin{{tabular}}{{l l l l}}
        \\textbf{{Prob.}} & \\textbf{{Best}} & \\textbf{{Median}} & \\textbf{{Worst}} & \\textbf{{Mean}} & \\textbf{{Std}} & \\textbf{{Feasible Rate}} & \\textbf{{Success Rate}} & \\textbf{{Success Performance}} \\
        \\hline
        {lines}
    \\end{{tabular}}
    \\caption{{Number of FES to achieve the fixed accuracy level ($f(\\mathbf{{x}}) - f(\\mathbf{{x}}*) \\leq 0.0001$), Success Rate, Feasible Rate and Success Performance.}}
\\end{{table}}"""

LINE_TABLE_2 = r"""{problem_name} & {best} & {median} & {worst} & {mean} & {std} & {feasible_rate} & {success_rate} & {success_performance} \\\\"""


def tune_function(algorithm, problem_parameters, pop_size, params):
    # iterations = 5 * 10**3
    iterations = 100

    def objective_function(*x):
        algorithm_params = {key: xi for param, xi in zip(params, x) for key in param.keys()}
        algorithm_class = algorithm(
            problem_parameters.get("objective_function"),
            soft_constrains=problem_parameters.get("gx"),
            hard_constrains=problem_parameters.get("hx"),
            ranges=problem_parameters.get("ranges"),
            population_size=pop_size,
            epsilon=10 ** -4,
            smooth=True,
            **algorithm_params
        )
        try:
            algorithm_class.search(iterations=iterations)
            return abs(algorithm_class.population[-1]["fx"] - problem_parameters["fx"]) / abs(problem_parameters["fx"])
        except:
            return 1.0

    return objective_function


def tuning():
    problems = [("pg01", get_pg01()), ("pg02", get_pg02()), ("pg03", get_pg03()), ("pg04", get_pg04()),
                ("pg05", get_pg05()), ("pg06", get_pg06()), ("pg07", get_pg07()), ("pg08", get_pg08()),
                ("pg09", get_pg09()), ("pg10", get_pg10()), ("pg11", get_pg11()), ("pg12", get_pg12()),
                ("pg13", get_pg13()), ("pg14", get_pg14()), ("pg15", get_pg15()), ("pg16", get_pg16()),
                ("pg17", get_pg17()), ("pg18", get_pg18()), ("pg19", get_pg19()), ("pg20", get_pg20()),
                ("pg21", get_pg21()), ("pg22", get_pg22()), ("pg23", get_pg23()), ("pg24", get_pg24())]

    iterations_list = [5 * 10**3, 5 * 10**4, 5 * 10**5]
    problems_populations = [13, 20, 10, 5, 4, 3, 10, 3, 7, 8, 3, 3, 5, 10, 3, 5, 6, 9, 15, 24, 7, 22, 9, 3]

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
    for problem_parameters, population_size in zip(problems, problems_populations):
        for algorithm in algorithms:
            objective_function = tune_function(algorithm, problem_parameters[1], population_size, algorithm["params"])
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
            tunner.search(iterations=10)
            solution = tunner.population[-1]["x"]
            solution_params = {key: xi for param, xi in zip(algorithm["params"], solution) for key in param.keys()}
            tunner_json.append({
                "problem_name": problem_parameters[0],
                **solution_params
            })
    with open("tunner_json.json", "w") as tunner_json_file:
        json.dumps(tunner_json_file)


if __name__ == "__main__":
    tuning()
