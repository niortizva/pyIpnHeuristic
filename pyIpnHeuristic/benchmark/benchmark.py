from IPython.display import display_markdown
from functools import reduce
import math
from .constants import *


def get_pg01() -> list:
    """
    Problem G01
    :return list: Returns problem parameters
    """
    display_markdown(PROBLEM_G01, raw=True)

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

    return [objective_function, [g1, g2, g3, g4, g5, g6, g7, g8, g9], [], ranges]


def get_pg02(n: int = 20) -> list:
    """
    Problem G02
    :return list: Returns problem parameters
    """
    display_markdown(PROBLEM_G02, raw=True)
    
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
    
    return [objective_function, [g1, g2], [], ranges]


def get_pg03(n: int = 10) -> list:
    """
    Problem G03
    :return list: Returns problem parameters
    """
    display_markdown(PROBLEM_G03, raw=True)
    
    def objective_function(*x):
        return - (math.sqrt(n)**n) * reduce(lambda a, b: a * b, x)
    
    def h1(*x):
        return sum([xi**2 for xi in x]) - 1
    
    ranges = [[0, 1] for _ in range(n)]
    
    return [objective_function, [], [h1], ranges]


def get_pg04() -> list:
    """
    Problem G04
    :return list: Returns problem parameters
    """
    display_markdown(PROBLEM_G04, raw=True)
    
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
    
    return [objective_function, [g1, g2, g3, g4, g5, g6], [], ranges]


def get_pg05() -> list:
    """
    Problem G05
    :return list: Returns problem parameters
    """
    display_markdown(PROBLEM_G05, raw=True)
    
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
    
    return [objective_function, [g1, g2], [h1, h2, h3], ranges]


def get_pg06() -> list:
    """
    Problem G06
    :return list: Returns problem parameters
    """
    display_markdown(PROBLEM_G06, raw=True)

    def objective_function(*x):
        return (x[0] - 10) ** 3 + (x[1] - 20) ** 3

    def g1(*x):
        return -(x[0] - 5) ** 2 - (x[1] - 5) ** 2 + 100

    def g2(*x):
        return (x[0] - 6) ** 2 + (x[1] - 5) ** 2 - 82.81

    ranges = [[13, 100], [0, 100]]

    return [objective_function, [g1, g2], [], ranges]


def get_pg07() -> list:
    """
    Problem G07
    :return list: Returns problem parameters
    """
    pass


def get_pg08() -> list:
    """
    Problem G08
    :return list: Returns problem parameters
    """
    pass


def get_pg09() -> list:
    """
    Problem G09
    :return list: Returns problem parameters
    """
    pass


def get_pg10() -> list:
    """
    Problem G10
    :return list: Returns problem parameters
    """
    pass


def get_pg11() -> list:
    """
    Problem G11
    :return list: Returns problem parameters
    """
    display_markdown(PROBLEM_G11, raw=True)
    
    def objective_function(*x):
        return x[0]**2 + (x[1] - 1)**2
    
    def h1(*x):
        return x[1] - x[0]**2
    
    ranges = [[-1, 1], [-1, 1]]
    
    return [objective_function, [], [h1], ranges]


def get_pg12() -> list:
    """
    Problem G12
    :return list: Returns problem parameters
    """
    pass


def get_pg13() -> list:
    """
    Problem G13
    :return list: Returns problem parameters
    """
    pass


def get_pg14() -> list:
    """
    Problem G14
    :return list: Returns problem parameters
    """
    pass


def get_pg15() -> list:
    """
    Problem G15
    :return list: Returns problem parameters
    """
    pass


def get_pg16() -> list:
    """
    Problem G16
    :return list: Returns problem parameters
    """
    pass


def get_pg17() -> list:
    """
    Problem G17
    :return list: Returns problem parameters
    """
    pass


def get_pg18() -> list:
    """
    Problem G18
    :return list: Returns problem parameters
    """
    pass


def get_pg19() -> list:
    """
    Problem G19
    :return list: Returns problem parameters
    """
    pass


def get_pg20() -> list:
    """
    Problem G20
    :return list: Returns problem parameters
    """
    pass


def get_pg21() -> list:
    """
    Problem G21
    :return list: Returns problem parameters
    """
    pass


def get_pg22() -> list:
    """
    Problem G22
    :return list: Returns problem parameters
    """
    pass


def get_pg23() -> list:
    """
    Problem G23
    :return list: Returns problem parameters
    """
    pass


def get_pg24() -> list:
    """
    Problem G24
    :return list: Returns problem parameters
    """
    pass
