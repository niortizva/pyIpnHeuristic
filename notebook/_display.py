from typing import List
from matplotlib import pyplot as plt


def display_performance_results(history: List[dict]) -> None:
    """
    Displays Algorithm Performance Plot
    :return None:
    """
    plt.rcParams['figure.figsize'] = [10, 10]
    
    t = len(history)
    iterations = [history[i]["iteration"] for i in range(len(history))]
    fx = [history[i]["fx"] for i in range(t)]
    xi_x_best = [history[i]["||xi-X||"] for i in range(t)]
    fxi_fx_best = [history[i]["fxi - Fx"] for i in range(t)]
    
    fig, axs = plt.subplots(3, 1)
    
    axs[0].plot(iterations, fx)
    axs[0].set_title('Objective Function Performance')
    axs[0].grid()
    
    axs[1].plot(iterations, xi_x_best)
    axs[1].set_title('Xi vs X Best')
    axs[1].grid()
    
    axs[2].plot(iterations, fxi_fx_best)
    axs[2].set_title('Fxi vs Fx best')
    axs[2].grid()

    plt.show()
