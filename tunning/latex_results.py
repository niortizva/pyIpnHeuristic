from pyIpnHeuristic.artificialBeeColony import ArtificialBeeColony
from pyIpnHeuristic.particleSwarmOptimization import ParticleSwarmOptimization
from pyIpnHeuristic.differentialEvolution import DifferentialEvolution
from pyIpnHeuristic.harmonySearch import HarmonySearch
from pyIpnHeuristic.hybridModifiedPsoAndEd import HybridModifiedPsoAndEd
from pyIpnHeuristic import benchmark
import json
import statistics

DOC = r"""\documentclass[10pt, a4paper]{{book}}

\usepackage{{amsmath}}
\usepackage{{longtable}}
\usepackage{{geometry}}
\geometry{{
    total={{170mm,257mm}},
    left=20mm,
    top=20mm,
}}

\title{{
    Heuristic Algorithms \\
    \large Achieved Results for {algorithm_name}\\
}}
\author{{Nicolás Ortiz Valencia}}

\begin{{document}}

\maketitle

{doc}

\end{{document}}"""

TABLE_1 = r"""
\begin{{center}}
\begin{{longtable}}{{l l l l}}
FES & $5 \times 10^{{3}}$ & $5 \times 10^{{4}}$ & $5 \times 10^{{5}}$ \\
\hline
Best & {:.4f} & {:.4f} & {:.4f} \\
Median & {:.4f} & {:.4f} & {:.4f} \\
Worst & {:.4f} & {:.4f} & {:.4f} \\
$v$ & {:.4f} & {:.4f} & {:.4f} \\
Mean & {:.4f} & {:.4f} & {:.4f} \\
std & {:.4f} & {:.4f} & {:.4f} \\
\caption{{ Error Values Problem {problem_name} using {algorithm_name} }}
\end{{longtable}}
\end{{center}}
"""

TABLE_2 = r"""
\begin{{center}}
\begin{{longtable}}{{l l l l l l l l l l}}
\textbf{{Max FES}} & \textbf{{Prob.}} & \textbf{{Best}} & \textbf{{Median}} & \textbf{{Worst}} & \textbf{{Mean}} & \textbf{{Std}} & \textbf{{FR}} & \textbf{{SR}} & \textbf{{SP}} \\
\hline
{lines}
\caption{{ {algorithm_name}. Number of FES to achieve the fixed accuracy level ($f(\mathbf{{x}}) - f(\mathbf{{x}}^{{*}}) \leq 0.0001$), Success Rate, Feasible Rate and Success Performance }}
\end{{longtable}}
\end{{center}}
"""

LINE_TABLE_2 = r"""{} & {} & {:.4f} & {:.4f} & {:.4f} & {:.4f} & {:.4f} & {:.4f} & {:.4f} & {:.4f} \\
"""


def calculate_v(trials, h_length, epsilon):
    Hx = sum([trial["hx"] + epsilon for trial in trials]) / h_length if h_length != 0 else 0
    Gx = sum([trial["gx"] for trial in trials])
    return Gx + Hx


def find_algorithm_class(algorithm_name):
    if algorithm_name == "Artificial Bee Colony":
        return ArtificialBeeColony
    elif algorithm_name == "Particle Swarm Optimization":
        return ParticleSwarmOptimization
    elif algorithm_name == "Differential Evolution":
        return DifferentialEvolution
    elif algorithm_name == "Harmony Search":
        return HarmonySearch
    elif algorithm_name == "Hybrid Modified PSO with Differential Evolution":
        return HybridModifiedPsoAndEd


def find_best_fes(history, fx):
    for h in history:
        if abs(h["fx"] - fx) <= 0.0001:
            return h["fes"]
    return history[-1]["fes"]


def create_latex(algorithms_json, selected_algorithm):
    epsilon = 10 ** -4
    latex_tex = ""
    lines_table_2_tex = ""
    for algorithm_test in algorithms_json:
        if selected_algorithm == algorithm_test["algorithm"]:
            problem_parameters = getattr(benchmark, "get_{}".format(algorithm_test["problem_name"]))()
            trials = []
            best = []
            median = []
            worst = []
            v = []
            mean = []
            std = []
            c = []
            lines_table_2 = ""
            for tex_iteration, max_fes in [(r"$5 \\times 10^3$", 5 * 10**3), (r"$5 \\times 10^4$", 5 * 10**4),
                                           (r"$5 \\times 10^5$", 5 * 10**5)]:
                algorithm_class = find_algorithm_class(algorithm_test["algorithm"])(
                    problem_parameters.get("objective_function"),
                    soft_constrains=problem_parameters.get("gx"),
                    hard_constrains=problem_parameters.get("hx"),
                    ranges=problem_parameters.get("ranges"),
                    population_size=algorithm_test.get("population_size"),
                    epsilon=epsilon,
                    smooth=True,
                    max_fes=max_fes,
                    **algorithm_test["solution"]
                )
                fes_record = []
                for _ in range(30):
                    algorithm_class.search(iterations=10**5, save_history=True)
                    history = algorithm_class.history
                    trials.append(algorithm_class.history[-1])
                    fes_record.append({
                        "is_feasible": 1 if list(filter(lambda x: x["gx"] <= 0 and x["hx"] <= 0, history)) else 0,
                        "is_success": 1 * (abs(history[-1]["fx"] - problem_parameters.get("fx")) <= 0.0001),
                        "fes": find_best_fes(history, problem_parameters.get("fx"))
                    })
                feasible_rate = sum([record["is_feasible"] for record in fes_record]) / 30
                success_rate = sum([record["is_success"] for record in fes_record]) / 30
                success_performance = (
                        statistics.mean([record["fes"] for record in fes_record]) * 30 /
                        sum([record["is_success"] for record in fes_record]))\
                    if sum([record["is_success"] for record in fes_record]) > 0 else -1
                error_list = [abs(trial["fx"] - problem_parameters["fx"]) for trial in trials]
                best_trial = algorithm_class.get_best(trials)
                best.append(abs(best_trial["fx"] - problem_parameters["fx"]))
                print(r"""algorithm: {}, problem: {}, max_fes: {} - Done!""".format(
                    selected_algorithm, algorithm_test["problem_name"], max_fes))
                median.append(statistics.median(error_list))
                worst.append(abs(algorithm_class.get_best([
                    {**trial, "fx": -trial["fx"], "hx": -trial["hx"], "gx": -trial["gx"]}
                    for trial in trials])["fx"] - problem_parameters["fx"]))
                v.append(calculate_v(trials, len(problem_parameters.get("hx")), epsilon))
                mean.append(statistics.mean(error_list))
                std.append(statistics.stdev(error_list))

                lines_table_2 += LINE_TABLE_2.format(
                    max_fes,
                    algorithm_test["problem_name"],
                    min(error_list),
                    statistics.median(error_list),
                    worst[-1],
                    statistics.mean(error_list),
                    statistics.stdev(error_list),
                    "{:.3f} %".format(100 * feasible_rate),
                    "{:.3f} %".format(100 * success_rate),
                    success_performance,
                )
            tex_params = best + median + worst + v + mean + std
            latex_tex += TABLE_1.format(*tex_params, problem_name=algorithm_test["problem_name"],
                                        algorithm_name=algorithm_test["algorithm"])
            lines_table_2_tex += TABLE_2.format(lines=lines_table_2, algorithm_name=algorithm_test["algorithm"])

    tex_doc = DOC.format(algorithm_name=selected_algorithm, doc=latex_tex + lines_table_2_tex)
    with open("tex_docs/{} results.tex".format(selected_algorithm), "w") as tex_file:
        tex_file.write(tex_doc)


if __name__ == "__main__":
    with open("tunner_json.json", "r") as tunner_json:
        json_params = json.load(tunner_json)
        create_latex(json_params, "Artificial Bee Colony")
        create_latex(json_params, "Particle Swarm Optimization")
        create_latex(json_params, "Differential Evolution")
        create_latex(json_params, "Harmony Search")
        create_latex(json_params, "Hybrid Modified PSO with Differential Evolution")
