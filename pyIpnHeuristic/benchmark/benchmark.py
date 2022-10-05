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
        f1 = sum([math.cos(xi) ** 4 for xi in x])
        f2 = 2 * reduce(lambda a, b: a * b, [math.cos(xi) ** 2 for xi in x])
        f3 = math.sqrt(sum([(i + 1) * (x[i] ** 2) for i in range(len(x))]))
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
        return - (math.sqrt(n) ** n) * reduce(lambda a, b: a * b, x)

    def h1(*x):
        return sum([xi ** 2 for xi in x]) - 1

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
        return 5.3578547 * x[2] ** 2 + 0.8356891 * x[0] * x[4] + 37.293239 * x[0] - 40792.141

    def g1(*x):
        return 85.334407 + 0.0056858 * x[1] * x[4] + 0.0006262 * x[0] * x[3] - 0.0022053 * x[2] * x[4] - 92

    def g2(*x):
        return - 85.334407 - 0.0056858 * x[1] * x[4] - 0.0006262 * x[0] * x[3] + 0.0022053 * x[2] * x[4]

    def g3(*x):
        return 80.51249 + 0.0071317 * x[1] * x[4] + 0.0029955 * x[0] * x[1] + 0.0021813 * x[2] ** 2 - 110

    def g4(*x):
        return - 80.51249 - 0.0071317 * x[1] * x[4] - 0.0029955 * x[0] * x[1] - 0.0021813 * x[2] ** 2 + 90

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
        return 3.0 * x[0] + 0.000001 * x[0] ** 3 + 2 * x[1] + (0.000002 / 3.0) * x[1] ** 3

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
        return (x[0] - 10.0) ** 3 + (x[1] - 20.0) ** 3

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
        return (x[0] ** 2 + x[1] ** 2 + x[0] * x[1] - 14 * x[0] - 16 * x[1] + (x[2] - 10) ** 2 +
                4 * (x[3] - 5) ** 2 + (x[4] - 3) ** 2 + 2 * (x[5] - 1) ** 2 + 5 * x[6] ** 2 +
                7 * (x[7] - 11) ** 2 + 2 * (x[8] - 10) ** 2 + (x[9] - 7) ** 2 + 45)

    def g1(*x):
        return -105 + 4 * x[0] + 5 * x[1] - 3 * x[6] + 9 * x[7]

    def g2(*x):
        return 10 * x[0] - 8 * x[1] - 17 * x[6] + 2 * x[7]

    def g3(*x):
        return - 8 * x[0] + 2 * x[1] + 5 * x[8] - 2 * x[9] - 12

    def g4(*x):
        return 3 * (x[0] - 2) ** 2 + 4 * (x[1] - 3) ** 2 + 2 * x[2] ** 2 - 7 * x[3] - 120

    def g5(*x):
        return 5 * x[0] ** 2 + 8 * x[1] + (x[2] - 6) ** 2 - 2 * x[3] - 40

    def g6(*x):
        return x[0] ** 2 + 2 * (x[1] - 2) ** 2 - 2 * x[0] * x[1] + 14 * x[4] - 6 * x[5]

    def g7(*x):
        return 0.5 * (x[0] - 8) ** 2 + 2 * (x[1] - 4) ** 2 + 3 * x[4] ** 2 - x[5] - 30

    def g8(*x):
        return - 3 * x[0] + 6 * x[1] + 12 * (x[8] - 8) ** 2 - 7 * x[9]

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
    def objective_function(*x):
        return - (math.sin(2 * math.pi * x[0]) ** 3) * math.sin(2 * math.pi * x[1]) / \
               (x[0] ** 3 * (x[0] + x[1]))

    def g1(*x):
        return x[0] ** 2 - x[1] + 1

    def g2(*x):
        return 1 - x[0] + (x[1] - 4) ** 2

    ranges = [[0, 10], [0, 10]]

    x_best = [1.22797135260752599, 4.24537336612274885]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G08,
        "x": x_best,
        "fx": fx_best
    }


def get_pg09() -> dict:
    """
    Problem G09
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return (x[0] - 10) ** 2 + 5 * (x[1] - 12) ** 2 + x[2] ** 4 + 3 * (x[3] - 11) ** 2 + \
               10 * x[4] ** 6 + 7 * x[5] ** 2 + x[6] ** 4 - 4 * x[5] * x[6] - 10 * x[5] - 8 * x[6]

    def g1(*x):
        return - 127 + 2 * x[0] ** 2 + 3 * x[1] ** 4 + x[2] + 4 * x[3] ** 2 + 5 * x[4]

    def g2(*x):
        return - 282 + 7 * x[0] + 3 * x[1] + 10 * x[2] ** 2 + x[3] - x[4]

    def g3(*x):
        return - 196 + 23 * x[0] + x[1] ** 2 + 6 * x[5] ** 2 - 8 * x[6]

    def g4(*x):
        return 4 * x[0] ** 2 + x[1] ** 2 - 3 * x[0] * x[1] + 2 * x[2] ** 2 + 5 * x[5] - 11 * x[6]

    ranges = [[-10, 10] for _ in range(7)]

    x_best = [2.33049935147405174, 1.95137236847114592, -0.477541399510615805,
              4.36572624923625874, -0.624486959100388983, 1.03813099410962173,
              1.5942266780671519]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G09,
        "x": x_best,
        "fx": fx_best
    }


def get_pg10() -> dict:
    """
    Problem G10
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return x[0] + x[1] + x[2]

    def g1(*x):
        return - 1 + 0.0025 * (x[3] + x[5])

    def g2(*x):
        return - 1 + 0.0025 * (x[4] + x[6] - x[3])

    def g3(*x):
        return - 1 + 0.01 * (x[7] - x[4])

    def g4(*x):
        return - x[0] * x[5] + 833.33252 * x[3] + 100 * x[0] - 83333.333

    def g5(*x):
        return - x[1] * x[6] + 1250 * x[4] + x[1] * x[3] - 1250 * x[3]

    def g6(*x):
        return - x[2] * x[7] + 1250000 + x[2] * x[4] - 2500 * x[4]

    ranges = [[100, 10000], [1000, 10000], *[[10, 1000] for _ in range(5)]]

    x_best = [579.306685017979589, 1359.97067807935605, 5109.97065743133317, 182.01769963061534,
              295.601173702746792, 217.982300369384632, 286.41652592786852, 395.601173702746735]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4, g5, g6],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G10,
        "x": x_best,
        "fx": fx_best
    }


def get_pg11() -> dict:
    """
    Problem G11
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return x[0] ** 2 + (x[1] - 1) ** 2

    def h1(*x):
        return x[1] - x[0] ** 2

    ranges = [[-1, 1], [-1, 1]]

    x_best = [-0.707036070037170616, 0.500000004333606807,
              0.707036070037170616, 0.500000004333606807]

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
    def objective_function(*x):
        return - (100 - (x[0] - 5) ** 2 - (x[1] - 5) ** 2 - (x[2] - 5) ** 2) / 100

    def g1(*x):
        return min([(x[0] - p) ** 2 + (x[1] - q) ** 2 + (x[2] - r) ** 2 - 0.0625
                    for p in range(1, 10)
                    for q in range(1, 10)
                    for r in range(1, 10)])

    ranges = [[0, 10] for _ in range(3)]

    x_best = [5, 5, 5]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G12,
        "x": x_best,
        "fx": fx_best
    }


def get_pg13() -> dict:
    """
    Problem G13
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return math.exp(reduce(lambda a, b: a * b, x))

    def h1(*x):
        return sum([xi ** 2 for xi in x]) - 10

    def h2(*x):
        return x[1] * x[2] - 5 * x[3] * x[4]

    def h3(*x):
        return x[0] ** 3 + x[1] ** 3 + 1

    ranges = [[-2.3, 2.3], [-2.3, 2.3], *[[-3.2, 3.2] for _ in range(3)]]

    x_best = [-1.71714224003, 1.59572124049468, 1.8272502406271,
              -0.763659881912867, -0.76365986736498]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1, h2, h3],
        "ranges": ranges,
        "markdown": PROBLEM_G13,
        "x": x_best,
        "fx": fx_best
    }


def get_pg14() -> dict:
    """
    Problem G14
    :return dict: Returns problem parameters
    """
    constants = [-6.089, -17.164, -34.054, -5.914, -24.721,
                 -14.986, -24.1, -10.708, -26.662, -22.179]

    def objective_function(*x, c: list = constants):
        return sum([x[i] * (c[i] + math.log(x[i] / sum(x))) for i in range(len(x))])

    def h1(*x):
        return x[0] + 2 * x[1] + 2 * x[2] + x[5] + x[9] - 2

    def h2(*x):
        return x[3] + 2 * x[4] + x[5] + x[6] - 1

    def h3(*x):
        return x[2] + x[6] + x[7] + 2 * x[8] + x[9] - 1

    ranges = [[0, 10] for _ in range(10)]

    x_best = [0.0406684113216282, 0.147721240492452, 0.783205732104114, 0.00141433931889084,
              0.485293636780388, 0.000693183051556082, 0.0274052040687766, 0.0179509660214818,
              0.0373268186859717, 0.0968844604336845]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1, h2, h3],
        "ranges": ranges,
        "markdown": PROBLEM_G14,
        "x": x_best,
        "fx": fx_best
    }


def get_pg15() -> dict:
    """
    Problem G15
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return 1000 - x[0] ** 2 - 2 * x[1] ** 2 - x[2] ** 2 - x[0] * x[1] - x[0] * x[2]

    def h1(*x):
        return x[0] ** 2 + x[1] ** 2 + x[2] ** 2 - 25

    def h2(*x):
        return 8 * x[0] + 14 * x[1] + 7 * x[2] - 56

    ranges = [[0, 10] for _ in range(3)]

    x_best = [3.51212812611795133, 0.216987510429556135, 3.55217854929179921]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1, h2],
        "ranges": ranges,
        "markdown": PROBLEM_G15,
        "x": x_best,
        "fx": fx_best
    }


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
    def objective_function(*x):
        f1 = 30 * x[0] * (0 <= x[0] < 300) + 31 * x[0] * (300 <= x[0] < 400)
        f2 = 28 * x[1] * (0 <= x[1] < 100) + 29 * x[1] * (100 <= x[1] < 200) + 30 * x[1] * (200 <= x[1] < 1000)
        return f1 + f2

    def h1(*x):
        return - x[0] + 300 - math.cos(1.48477 - x[5]) * (x[2] * x[3]) / 131.078 + \
               math.cos(1.47588) * (0.90798 * x[2] ** 2) / 131.078

    def h2(*x):
        return - x[1] - math.cos(1.48477 + x[5]) * (x[2] * x[3]) / 131.078 + \
               math.cos(1.47588) * (0.90798 * x[3] ** 2) / 131.078

    def h3(*x):
        return - x[4] - math.cos(1.48477 + x[5]) * (x[2] * x[3]) / 131.078 + \
               math.sin(1.47588) * (0.90798 * x[3] ** 2) / 131.078

    def h4(*x):
        return 200 - math.sin(1.48477 - x[5]) * (x[2] * x[3]) / 131.078 + \
               math.sin(1.47588) * (0.90798 * x[2] ** 2) / 131.078

    ranges = [[0, 400], [0, 1000], [340, 420], [340, 420], [-1000, 1000]]

    x_best = [201.784467214523659, 99.9999999999999005, 383.071034852773266,
              420.0, -10.9076584514292652, 0.0731482312084287128]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1, h2, h3, h4],
        "ranges": ranges,
        "markdown": PROBLEM_G17,
        "x": x_best,
        "fx": fx_best
    }


def get_pg18() -> dict:
    """
    Problem G18
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return - 0.5 * (x[0] * x[3] - x[1] * x[2] + x[2] * x[8] - x[4] * x[8] +
                        x[4] * x[7] - x[5] * x[6])

    def g1(*x):
        return x[2]**2 + x[3]**2 - 1

    def g2(*x):
        return x[8]**2 - 1

    def g3(*x):
        return x[4]**2 + x[5]**2 - 1

    def g4(*x):
        return x[0]**2 + (x[1] - x[8])**2 - 1

    def g5(*x):
        return (x[0] - x[4])**2 + (x[1] - x[5])**2 - 1

    def g6(*x):
        return (x[0] - x[6])**2 + (x[1] - x[7])**2 - 1

    def g7(*x):
        return (x[2] - x[4])**2 + (x[3] - x[5])**2 - 1

    def g8(*x):
        return (x[2] - x[6])**2 + (x[3] - x[7])**2 - 1

    def g9(*x):
        return x[6]**2 + (x[7] - x[9])**2 - 1

    def g10(*x):
        return x[1] * x[2] - x[0] * x[3]

    def g11(*x):
        return - x[2] * x[8]

    def g12(*x):
        return x[4] * x[8]

    def g13(*x):
        return x[5] * x[6] - x[4] * x[7]

    ranges = [*[[-10, 10] for _ in range(8)], [0, 20]]

    x_best = [-0.657776192427943163, -0.153418773482438542, 0.323413871675240938,
              -0.946257611651304398, -0.657776194376798906, -0.753213434632691414,
              0.323413874123576972, -0.346462947962331735, 0.59979466285217542]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G18,
        "x": x_best,
        "fx": fx_best
    }


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
