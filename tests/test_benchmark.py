from pyIpnHeuristic.benchmark import *


def test_benchmark():
    problems = [get_pg01, get_pg02, get_pg03, get_pg04, get_pg05,
                get_pg06, get_pg07, get_pg08, get_pg09, get_pg10,
                get_pg11, get_pg12, get_pg13, get_pg14, get_pg15,
                get_pg16, get_pg17, get_pg18, get_pg19, get_pg20,
                get_pg21, get_pg22, get_pg23, get_pg24]

    solutions = [-15.0000000000000, -0.80361910412559, -1.00050010001000,
                 -3.066553867178332 * 10**4, 5126.4967140071, -6961.81387558015,
                 24.30620906818, -0.0958250414180359, 680.630057374402,
                 7049.24802052867, 0.7499, -1.0000000000000, 0.053941514041898,
                 -47.7648884594915, 961.715022289961, -1.90515525853479,
                 8853.534016, -0.866025403784439, 32.6555929502463,
                 0.204979, 193.724510070035, 236.430975504001,
                 -400.055099999999584, -5.50801327159536]

    implemented = [1, 2, 3, 4,
                   5, 6, 7, 8,
                   9, 10, 11, 12,
                   13, 14, 15,
                   17, 18, 19, 20,
                   21, 24]

    for i in range(24):
        if i + 1 in implemented:
            problem_parameters = problems[i]()
            fx_best = problem_parameters["fx"]
            if format(fx_best, '.6f') != format(solutions[i], '.6f'):
                raise ValueError("Problem G{i}: FAILED, {fx_calc} != {fx_real}".format(
                    i=i+1, fx_calc=format(fx_best, '.6f'), fx_real=format(solutions[i], '.6f')))

            # Test Soft Restrictions
            for j in range(len(problem_parameters["gx"])):
                gj = problem_parameters["gx"][j]
                try:
                    gj(*problem_parameters["x"])
                except Exception as exc:
                    print("Problem {i} Soft restriction {j}: FAILED".format(i=i+1, j=j+1))
                    raise Exception("{}".format(exc))

            # Test Hard Restriction
            for j in range(len(problem_parameters["hx"])):
                hj = problem_parameters["hx"][j]
                try:
                    hj(*problem_parameters["x"])
                except Exception as exc:
                    print("Problem {i} Hard restriction {j}: FAILED".format(i=i + 1, j=j + 1))
                    raise Exception("{}".format(exc))

    return
