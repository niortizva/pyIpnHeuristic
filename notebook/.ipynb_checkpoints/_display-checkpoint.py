from typing import List
from matplotlib import pyplot as plt

def display_performance_results(history: List[dict]) -> None:
    """
    Displays Algorithm Performace Plot
    :return None:
    """
    plt.rcParams['figure.figsize'] = [10, 5]
    
    t = len(history)
    iterations = [history[i]["iteration"] for i in range(len(history))]
    fx = [history[i]["fx"] for i in range(t)]
    x1 = [history[i]["x"][0] for i in range(t)]
    x2 = [history[i]["x"][1] for i in range(t)]

    plt.plot(iterations, fx)
    plt.title("Objective Function Performance")
    plt.ylabel("Objective Function Value")
    plt.xlabel("Iteration")
    plt.grid()

    plt.show()
