from IPython.display import display_markdown
from .md import PROBLEM_G06


def get_pg06() -> list:
    """
    Problem G06
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
