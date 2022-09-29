from functools import reduce
import math
from .constants import *


def get_pg01() -> dict:
    """
    Problem G01
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return 5 * sum([x[i] for i in range(4)]) - 5 * sum([x[i] for i in range(4)]) - \
               sum([x[i] for i in range(4, 13)])

    def g1(*x):
        return 2 * x[0] + 2 * x[1] + x[9] + x[10] - 10
    
    def g2(*x):
        return 2 * x[0] + 2 * x[2] + x[9] + x[11] - 10
    
    def g3(*x):
        return 2 * x[1] + 2 * x[2] + x[10] + x[11] - 10

    def g4(*x):
        return - 8 * x[0] + x[9]
    
    def g5(*x):
        return - 8 * x[1] + x[10]
    
    def g6(*x):
        return - 8 * x[2] + x[11]
    
    def g7(*x):
        return - 2 * x[3] - x[4] + x[9]
    
    def g8(*x):
        return - 2 * x[5] - x[6] + x[10]
    
    def g9(*x):
        return - 2 * x[7] - x[8] + x[11]

    ranges = [*[[0, 1] for _ in range(9)], *[[0, 100] for _ in range(9, 12)], [0, 1]]

    x_best = [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4, g5, g6, g7, g8, g9],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G01,
        "x": x_best,
        "fx": fx_best
    }


def get_pg02(n: int = 20) -> dict:
    """
    Problem G02
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        f1 = sum([math.cos(xi)**4 for xi in x])
        f2 = 2*reduce(lambda a, b: a * b, [math.cos(xi)**2 for xi in x])
        f3 = math.sqrt(sum([(i+1)*(x[i]**2) for i in range(len(x))]))
        return - abs((f1 - f2) / f3)
    
    def g1(*x):
        return 0.75 - reduce(lambda a, b: a * b, x)
    
    def g2(*x):
        return sum(x) - 7.5 * n
    
    ranges = [[0, 10] for _ in range(n)]

    x_best = [3.16246061572185, 3.12833142812967, 3.09479212988791, 3.06145059523469, 3.02792915885555,
              2.99382606701730, 2.95866871765285, 2.92184227312450, 0.49482511456933, 0.48835711005490,
              0.48231642711865, 0.47664475092742, 0.47129550835493, 0.46623099264167, 0.46142004984199,
              0.45683664767217, 0.45245876903267, 0.44826762241853, 0.44424700958760, 0.44038285956317]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G02,
        "x": x_best,
        "fx": fx_best
    }


def get_pg03(n: int = 10) -> dict:
    """
    Problem G03
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return - (math.sqrt(n)**n) * reduce(lambda a, b: a * b, x)
    
    def h1(*x):
        return sum([xi**2 for xi in x]) - 1
    
    ranges = [[0, 1] for _ in range(n)]

    if n == 10:
        x_best = [0.31624357647283069, 0.316243577414338339, 0.316243578012345927, 0.316243575664017895,
                  0.316243578205526066, 0.31624357738855069, 0.316243575472949512, 0.316243577164883938,
                  0.316243578155920302, 0.316243576147374916]

        fx_best = objective_function(*x_best)
    else:
        x_best = None
        fx_best = None
    
    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1],
        "ranges": ranges,
        "markdown": PROBLEM_G03,
        "x": x_best,
        "fx": fx_best
    }


def get_pg04() -> dict:
    """
    Problem G04
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return 5.3575847 * x[2]**2 + 0.835689 * x[0] * x[4] + 37.293239 * x[0] - 40792.141
    
    def g1(*x):
        return 85.334407 + 0.0056858 * x[1] * x[4] + 0.0006262 * x[0] * x[3] - 0.0022053 * x[2] * x[4] - 92
    
    def g2(*x):
        return - 85.334407 - 0.0056858 * x[1] * x[4] - 0.0006262 * x[0] * x[3] + 0.0022053 * x[2] * x[4]
    
    def g3(*x):
        return 80.51249 + 0.0071317 * x[1] * x[4] + 0.0029955 * x[0] * x[1] + 0.0021813 * x[2]**2 - 110
    
    def g4(*x):
        return - 80.51249 - 0.0071317 * x[1] * x[4] - 0.0029955 * x[0] * x[1] - 0.0021813 * x[2]**2 + 90
    
    def g5(*x):
        return 9.300961 + 0.0047026 * x[2] * x[4] + 0.0012547 * x[0] * x[2] + 0.0019085 * x[2] * x[3] - 25
    
    def g6(*x):
        return - 9.300961 - 0.0047026 * x[2] * x[4] - 0.0012547 * x[0] * x[2] - 0.0019085 * x[2] * x[3] + 20
    
    ranges = [[78, 102], [33, 45], *[[27, 45] for _ in range(3)]]

    x_best = [78, 33, 29.9952560256815985, 45, 36.7758129057882073]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4, g5, g6],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G04,
        "x": x_best,
        "fx": fx_best
    }


def get_pg05() -> dict:
    """
    Problem G05
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return 3 * x[0] + 0.000001 * x[0]**3 + 2 * x[1] + (0.000002/3) * x[1]**3
    
    def g1(*x):
        return - x[3] + x[2] - 0.55
    
    def g2(*x):
        return - x[2] + x[3] - 0.55
    
    def h1(*x):
        return 1000 * math.sin(- x[2] - 0.25) + 1000 * math.sin(- x[3] - 0.25) + 894.8 - x[0]
    
    def h2(*x):
        return 1000 * math.sin(x[2] - 0.25) + 1000 * math.sin(x[2] - x[3] - 0.25) + 894.8 - x[0]
    
    def h3(*x):
        return 1000 * math.sin(x[3] - 0.25) + 1000 * math.sin(x[3] - x[2] - 0.25) + 1924.8
    
    ranges = [[0, 1200], [0, 1200], [-0.55, 0.55], [-0.55, 0.55]]

    x_best = [679.945148297028709, 1026.06697600004691, 0.118876369094410433, -0.39623348521517826]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2],
        "hx": [h1, h2, h3],
        "ranges": ranges,
        "markdown": PROBLEM_G05,
        "x": x_best,
        "fx": fx_best
    }


def get_pg06() -> dict:
    """
    Problem G06
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return (x[0] - 10) ** 3 + (x[1] - 20) ** 3

    def g1(*x):
        return -(x[0] - 5) ** 2 - (x[1] - 5) ** 2 + 100

    def g2(*x):
        return (x[0] - 6) ** 2 + (x[1] - 5) ** 2 - 82.81

    ranges = [[13, 100], [0, 100]]

    x_best = [14.09500000000000064, 0.8429607892154795668]

    fx_best = objective_function(*x_best)

    return {
            "objective_function": objective_function,
            "gx": [g1, g2],
            "hx": [],
            "ranges": ranges,
            "markdown": PROBLEM_G06,
            "x": x_best,
            "fx": fx_best
    }


def get_pg07() -> dict:
    """
    Problem G07
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return (x[0]**2 + x[1]**2 + x[0] * x[1] - 14 * x[0] - 16 * x[1] + (x[2] - 10)**2 + 
                4 * (x[3] - 5)**2 + (x[4] - 3)**2 + 2 * (x[5] - 1)**2 + 5 * x[6]**2 + 
                7 * (x[7] - 11)**2 + 2 * (x[8] - 10)**2 + (x[9] - 7)**2 + 45)
    
    def g1(*x):
        return -105 + 4 * x[0] + 5 * x[1] - 3 * x[6] + 9 * x[7]
    
    def g2(*x):
        return 10 * x[0] - 8 * x[1] - 17 * x[6] + 2 * x[7]
    
    def g3(*x):
        return - 8 * x[0] + 2 * x[1] + 5 * x[8] - 2 * x[9] - 12
    
    def g4(*x):
        return 3 * (x[0] - 2)**2 + 4 * (x[1] - 3)**2 + 2 * x[2]**2 - 7 * x[3] - 120
    
    def g5(*x):
        return 5 * x[0]**2 + 8 * x[1] + (x[2] - 6)**2 - 2 * x[3] - 40
    
    def g6(*x):
        return x[0]**2 + 2 * (x[1] - 2)**2 - 2 * x[0] * x[1] + 14 * x[4] - 6 * x[5]
    
    def g7(*x):
        return 0.5 * (x[0] - 8)**2 + 2 * (x[1] - 4)**2 + 3 * x[4]**2 - x[5] - 30
    
    def g8(*x):
        return - 3 * x[0] + 6 * x[1] + 12 * (x[8] - 8)**2 - 7 * x[9]
    
    ranges = [[-10, 10] for _ in range(10)]

    x_best = [2.17199634142692, 2.3636830416034, 8.77392573913157, 5.09598443745173,
              0.990654756560493, 1.43057392853463, 1.32164415364306, 9.82872576524495,
              8.2800915887356, 8.3759266477347]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4, g5, g6, g7, g8],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G07,
        "x": x_best,
        "fx": fx_best
    }


def get_pg08() -> dict:
    """
    Problem G08
    :return dict: Returns problem parameters
    """
    pass


def get_pg09() -> dict:
    """
    Problem G09
    :return dict: Returns problem parameters
    """
    pass


def get_pg10() -> dict:
    """
    Problem G10
    :return dict: Returns problem parameters
    """
    pass


def get_pg11() -> dict:
    """
    Problem G11
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return x[0]**2 + (x[1] - 1)**2
    
    def h1(*x):
        return x[1] - x[0]**2
    
    ranges = [[-1, 1], [-1, 1]]

    x_best = ([-0.707036070037170616, 0.500000004333606807],
              [0.707036070037170616, 0.500000004333606807])

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1],
        "ranges": ranges,
        "markdown": PROBLEM_G11,
        "x": x_best,
        "fx": fx_best
    }


def get_pg12() -> dict:
    """
    Problem G12
    :return dict: Returns problem parameters
    """
    pass


def get_pg13() -> dict:
    """
    Problem G13
    :return dict: Returns problem parameters
    """
    pass


def get_pg14() -> dict:
    """
    Problem G14
    :return dict: Returns problem parameters
    """
    pass


def get_pg15() -> dict:
    """
    Problem G15
    :return dict: Returns problem parameters
    """
    pass


def get_pg16() -> dict:
    """
    Problem G16
    :return dict: Returns problem parameters
    """
    pass


def get_pg17() -> dict:
    """
    Problem G17
    :return dict: Returns problem parameters
    """
    pass


def get_pg18() -> dict:
    """
    Problem G18
    :return dict: Returns problem parameters
    """
    pass


def get_pg19() -> dict:
    """
    Problem G19
    :return dict: Returns problem parameters
    """
    pass


def get_pg20() -> dict:
    """
    Problem G20
    :return dict: Returns problem parameters
    """
    pass


def get_pg21() -> dict:
    """
    Problem G21
    :return dict: Returns problem parameters
    """
    pass


def get_pg22() -> dict:
    """
    Problem G22
    :return dict: Returns problem parameters
    """
    pass


def get_pg23() -> dict:
    """
    Problem G23
    :return dict: Returns problem parameters
    """
    pass


def get_pg24() -> dict:
    """
    Problem G24
    :return dict: Returns problem parameters
    """
    pass
