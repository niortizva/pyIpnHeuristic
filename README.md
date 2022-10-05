# PyIpnHeuristic

pyIpnHeuristic is a pure Python implementation of some heuristic algorithms for the National
Polytechnic Institute of Mexico. For more information on pyIpnHeuristic, visit the GitHub project page
[pyIpnHeuristic](https://github.com/niortizva/pyIpnHeuristic)

## Benchmark 

Benchmark problems were taken from [Liang et al. 2006](https://www.researchgate.net/publication/216301032_Problem_definitions_and_evaluation_criteria_for_the_CEC_2006_special_session_on_constrained_real-parameter_optimization).
Check out the benchmark [doc](BENCHMARK.md) to for problems description.

Import benchmark problems as follows:

```python
# Import the benchmark problem methods
# get_pg01, get_pg02, get_pg03, get_pg04, get_pg05,
# get_pg06, get_pg07, get_pg08, get_pg09, get_pg10,
# get_pg11, get_pg12, get_pg13, get_pg14, get_pg15,
# get_pg16, get_pg17, get_pg18, get_pg19, get_pg20,
# get_pg21, get_pg22, get_pg23, get_pg24
from pyIpnHeuristic.benchmark import get_pg01

# get_pg[*problem]() returns problem parameters as:
#    {
#        objective_function": <class 'function'>,
#        "gx": [<class 'function'>, <class 'function'>, ...], # Soft Restrictions
#        "hx": [<class 'function'>, <class 'function'>, ...], # Hard Restrictions
#        "ranges": [[inf(x1), sup(x1)], ..., [inf(xd), sup(xd)]], # List of Ranges for each variable
#        "markdown": "PROBLEM X", # Markdown Problem description 
#        "x": x_best, # Best values
#        "fx": fx_best # Best solution value
#    }
problem = get_pg01()

objective_function = problem.get("objective_function")
gx = problem.get("gx")
hx = problem.get("hx")
ranges = problem.get("ranges")
markdown = problem.get("markdown")
x_best = problem.get("x")
fx_best = problem.get("fx")
```
