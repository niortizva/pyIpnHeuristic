from IPython.display import display_markdown
from functools import reduce
import math


def get_pg01() -> list:
    """
    Problem G01
    :return list: Returns problem parameters
    """
    problem_g01: str = r"""## Problem G01:
Minimize: 
$$f(\mathbf{x}) = 5\sum_{i=1}^{4} x_i - 5 \sum_{i=1}^{4} x_i^2 - \sum_{i=5}^{13} x_i$$
subject to:
$$g_1(\mathbf{x}) = 2 x_1 + 2 x_2 + x_{10} + x_{11} - 10 \leq 0 $$
$$g_2(\mathbf{x}) = 2 x_1 + 2 x_2 + x_{10} + x_{12} - 10 \leq 0 $$
$$g_3(\mathbf{x}) = 2 x_2 + 2 x_3 + x_{11} + x_{12} - 10 \leq 0 $$
$$g_4(\mathbf{x}) = -8x_1 + x_{10} \leq 0 $$
$$g_5(\mathbf{x}) = -8x_2 + x_{11} \leq 0 $$
$$g_6(\mathbf{x}) = -8x_3 + x_{12} \leq 0 $$
$$g_7(\mathbf{x}) = -2x_4 -x_5 + x_{10} \leq 0 $$
$$g_8(\mathbf{x}) = -2x_6 -x_7 + x_{11} \leq 0 $$
$$g_9(\mathbf{x}) = -2x_8 -x_9 + x_{12} \leq 0 $$
where: $0 \leq x_i \leq 1$ ($i=1,\ldots.9,13$) and $0 \leq x_i \leq 100$ ($i=10,11,12$)"""

    display_markdown(problem_g01, raw=True)

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
    problem_g02: str = r"""## Problem G02:
Minimize: 
$$f(\mathbf{x}) = -\left| \frac{\sum_{i=1}^{n}\cos^{4}({x_i}) - 
2\prod_{i=1}^{n}\cos^2(x_i)}{\sqrt{\sum_{i=1}^{n}i x_{i}^{2}}} \right|$$
subject to:
$$g_1(\mathbf{x}) = 0.75 - \prod_{i=1}^{n} x_i \leq 0 $$
$$g_2(\mathbf{x}) = \sum_{i=1}^{n} x_i - 7.5n \leq 0 $$
where: $n=20$ and $0 \leq x_i \leq 10$ $(i=1, \ldots, n)$"""

    display_markdown(problem_g02, raw=True)
    
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
    problem_g03: str = r"""## Problem G03:
Minimize: 
$$f(\mathbf{x}) = - \left( \sqrt{n}\right)^{n} \prod_{i=1}^{n} x_i$$
subject to:
$$h_1(\mathbf{x}) = \sum_{i=1}^{n} x_i^{2} - 1 = 0$$
where: $n=10$ and $0 \leq x_i \leq 1$ $(i=1, \ldots, n)$"""
    
    display_markdown(problem_g03, raw=True)
    
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
    problem_g04: str = r"""## Problem G04:
Minimize:
$$f(\mathbf{x}) = 5.3575847 x_3^{2} + 0.835689 x_1 x_5 + 37.293239 x_1 - 40792.141$$
subject to:
$$g_1(\mathbf{x}) = 85.334407 + 0.0056858x_2 x_5 + 0.0006262x_1 x_4 - 0.0022053x_3 x_5 - 92 \leq 0$$
$$g_2(\mathbf{x}) = -85.334407 - 0.0056858x_2 x_5 - 0.0006262x_1 x_4 + 0.0022053x_3 x_5 \leq 0$$
$$g_3(\mathbf{x}) = 80.51249 + 0.0071317x_2 x_5 + 0.0029955x_1 x_2 + 0.0021813x_3^{2} - 110 \leq 0$$
$$g_4(\mathbf{x}) = -80.51249 - 0.0071317x_2 x_5 - 0.0029955x_1 x_2 - 0.0021813x_3^{2} + 90 \leq 0$$
$$g_5(\mathbf{x}) = 9.300961 + 0.0047026x_3 x_5 + 0.0012547x_1 x_3 + 0.0019085x_3 x_4 - 25 \leq 0$$
$$g_6(\mathbf{x}) = -9.300961 - 0.0047026x_3 x_5 - 0.0012547x_1 x_3 - 0.0019085x_3 x_4 + 20 \leq 0$$
where: $78 \leq x_1 \leq 102$, $33 \leq x_2 \leq 45$ and $27 \leq x_i \leq 45$ $(i=3,4,5)$"""

    display_markdown(problem_g04, raw=True)
    
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
    problem_g05: str = r"""## Problem G05:
Minimize: 
$$f(\mathbf{x}) = 3x_1 + 0.000001x_1^{3} + 2x_2 + (0.000002/3)x_2^{3} $$
subject to:
$$g_1(\mathbf{x}) = -x_4 + x_3 -0.55 \leq 0$$
$$g_2(\mathbf{x}) = -x_3 + x_4 -0.55 \leq 0$$
$$h_1(\mathbf{x}) = 1000 \sin(-x_3 - 0.25) + 1000 \sin(x_4 - 0.25) + 894.8 - x_1 = 0$$
$$h_2(\mathbf{x}) = 1000 \sin(x_3 - 0.25) + 1000 \sin(x_3 - x_4 - 0.25) + 894.8 - x_2 = 0$$
$$h_3(\mathbf{x}) = 1000 \sin(x_4 - 0.25) + 1000 \sin(x_4 - x_3 - 0.25) + 1294.8 = 0$$
where: $0 \leq x_i \leq 1200$ $(i=1,2)$ and $-0.55 \leq x_i \leq 0.55$ $(i=3,4)$"""

    display_markdown(problem_g05, raw=True)
    
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
    problem_g06: str = r"""## Problem G06:
Minimize: 
$$f(\mathbf{x}) = (x_1 - 10)^3 + (x_2 - 20)^3$$
subject to:
$$g_1(\mathbf{x}) = -(x_1-5)^2 - (x_2-5)^2 + 100 \leq 0 $$
$$g_2(\mathbf{x}) = (x_1-6)^2 + (x_2-5)^2 - 82.81 \leq 0 $$
where: $13 \leq x_1 \leq 100$, $0 \leq x_2 \leq 100$"""

    display_markdown(problem_g06, raw=True)

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
    problem_g11 = r"""## Problem G11:
Minimize: 
$$f(\mathbf{x}) = x_1^{2} + (x_{2} - 1)^{2}$$
subject to:
$$h_1(\mathbf{x}) = x_2 -x_{1}^{2} \leq 0 $$
where: $-1 \leq x_1 \leq 1$, $-1 \leq x_2 \leq 1$"""
    
    display_markdown(problem_g11, raw=True)
    
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
