PROBLEM_G01: str = r"""## Problem G01:
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

PROBLEM_G02: str = r"""## Problem G02:
Minimize: 
$$f(\mathbf{x}) = -\left| \frac{\sum_{i=1}^{n}\cos^{4}({x_i}) - 
2\prod_{i=1}^{n}\cos^2(x_i)}{\sqrt{\sum_{i=1}^{n}i x_{i}^{2}}} \right|$$
subject to:
$$g_1(\mathbf{x}) = 0.75 - \prod_{i=1}^{n} x_i \leq 0 $$
$$g_2(\mathbf{x}) = \sum_{i=1}^{n} x_i - 7.5n \leq 0 $$
where: $n=20$ and $0 \leq x_i \leq 10$ $(i=1, \ldots, n)$"""

PROBLEM_G03: str = r"""## Problem G03:
Minimize: 
$$f(\mathbf{x}) = - \left( \sqrt{n}\right)^{n} \prod_{i=1}^{n} x_i$$
subject to:
$$h_1(\mathbf{x}) = \sum_{i=1}^{n} x_i^{2} - 1 = 0$$
where: $n=10$ and $0 \leq x_i \leq 1$ $(i=1, \ldots, n)$"""

PROBLEM_G04: str = r"""## Problem G04:
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

PROBLEM_G05: str = r"""## Problem G05:
Minimize: 
$$f(\mathbf{x}) = 3x_1 + 0.000001x_1^{3} + 2x_2 + (0.000002/3)x_2^{3} $$
subject to:
$$g_1(\mathbf{x}) = -x_4 + x_3 -0.55 \leq 0$$
$$g_2(\mathbf{x}) = -x_3 + x_4 -0.55 \leq 0$$
$$h_1(\mathbf{x}) = 1000 \sin(-x_3 - 0.25) + 1000 \sin(x_4 - 0.25) + 894.8 - x_1 = 0$$
$$h_2(\mathbf{x}) = 1000 \sin(x_3 - 0.25) + 1000 \sin(x_3 - x_4 - 0.25) + 894.8 - x_2 = 0$$
$$h_3(\mathbf{x}) = 1000 \sin(x_4 - 0.25) + 1000 \sin(x_4 - x_3 - 0.25) + 1294.8 = 0$$
where: $0 \leq x_i \leq 1200$ $(i=1,2)$ and $-0.55 \leq x_i \leq 0.55$ $(i=3,4)$"""

PROBLEM_G06: str = r"""## Problem G06:
Minimize: 
$$f(\mathbf{x}) = (x_1 - 10)^3 + (x_2 - 20)^3$$
subject to:
$$g_1(\mathbf{x}) = -(x_1-5)^2 - (x_2-5)^2 + 100 \leq 0 $$
$$g_2(\mathbf{x}) = (x_1-6)^2 + (x_2-5)^2 - 82.81 \leq 0 $$
where: $13 \leq x_1 \leq 100$, $0 \leq x_2 \leq 100$"""

PROBLEM_G07: str = r"""## Problem G07:
Minimize:
$$f(\mathbf{x}) = x_1^{2} + x_2^{2} + x_1 x_2 - 14x_1 -16x_2 
+ (x_3 - 10)^{2} + 4(x_4 - 5)^{2} + (x_5 -3)^{2} + 2(x_6-1)^{2}
+ 5x_7^{2} + 7(x_8 - 11)^{2} + 2(x_9 - 10)^2 + (x_{10} -7)^2 + 45
$$
subject to:
$$g_1(\mathbf{x}) = -105 + 4x_1 + 5x_2 - 3x_7 + 9x_8 \leq 0$$
$$g_2(\mathbf{x}) = 10x_1 - 8x_2 - 17x_7 + 2x_8 \leq 0$$
$$g_3(\mathbf{x}) = -8x_1 + 2x_2 + 5x_9 - 2x_{10} - 12 \leq 0$$
$$g_4(\mathbf{x}) = 3(x_1 -2)^{2} + 4(x_2 - 3)^{2} + 2x_3^{2} - 7x_4 - 120 \leq 0$$
$$g_5(\mathbf{x}) = 5x_1^{2} + 8x_2 + (x_3 - 6)^{2} - 2x_4 - 40 \leq 0$$
$$g_6(\mathbf{x}) = x_1^{2} + 2(x_2 - 2)^{2} - 2x_1 x_2 + 14x_5 - 6x_6 \leq 0$$
$$g_7(\mathbf{x}) = 0.5(x_2-8)^2 + 2(x_2 -4)^2 - 3x_5^{2} -x_6 - 30 \leq 0$$
$$g_8(\mathbf{x}) = -3x_1 + 6x_2 + 12(x_9 - 8)^{2} - 7x_{10} \leq 0$$
where: $-10 \leq x_i \leq 10$ $(i=1,\ldots,10)$"""

PROBLEM_G08: str = r"""## Problem G08
Minimize:
$$f(\mathbf{x}) = - \frac{ \sin^{3}(2\pi x_1) \sin (2\pi x_2) }{ x_1^{3} (x_1 + x_2) }$$
subject to:
$$g_1 (\mathbf{x}) = x_1^{2} - x_2 + 1 \leq 0$$
$$g_2 (\mathbf{x}) = 1 - x_1 + (x_2 - 4)^{2} \leq 0$$
where: $0 \leq x_1 \leq 10$ and $0 \leq x_2 \leq 10$"""

PROBLEM_G09: str = r"""## Problem G09
Minimize:
$$f(\mathbf{x}) = (x_1 - 10)^2 + 5 (x_2 -12)^2 + x_3^{4} + 3(x_4 - 11)^2
+ 10 x_5^{6} + 7x_6^{2} + x_7^{4} - 4x_6 x_7 - 10x_6 - 8x_7
$$
subject to:
$$g_1 (\mathbf{x}) = -127 + 2x_1^{2} 3x_2^{4} + x_3 + 4x_4^{2} + 5x_5 \leq 0$$
$$g_2 (\mathbf{x}) = -282 + 7x_1 + 3x_2 + 10x_3^{2} + x_4 - x_5 \leq 0$$
$$g_3 (\mathbf{x}) = -196 + 23x_1 + x_2^{2} + 6x_6^{2} - 8x_7 \leq 0$$
$$g_4 (\mathbf{x}) = 4x_1^{2} + x_2^{2} - 3x_1 x_2 + 2x_3^{2} + 5x_6 - 11x_7 \leq 0$$
where: $-10 \leq x_1 \leq 10$ ($i=1,\ldots,7$)"""

PROBLEM_G10: str = r"""## Problem G10
Minimize:
$$f(\mathbf{x}) = x_1 + x_2 + x_3$$
subject to:
$$g_1 (\mathbf{x}) = -1 + 0.0025 (x_4 + x_6) \leq 0$$
$$g_2 (\mathbf{x}) = -1 + 0.0025 (x_5 + x_7 - x_4) \leq 0$$
$$g_3 (\mathbf{x}) = -1 + 0.01 (x_8 - x_5) \leq 0$$
$$g_4 (\mathbf{x}) = -x_1 x_6 + 833.33252x_4 + 100x_1 - 83333.333 \leq 0$$
$$g_5 (\mathbf{x}) = -x_1 x_7 + 1250 x_5 + x_2 x_4 - 1250 x_4 \leq 0$$
$$g_6 (\mathbf{x}) = -x_3 x_8 + 1250000 + x_3 x_5 - 2500 x_5 \leq 0$$
where: $100 \leq x_1 \leq 10000$, $1000 \leq x_i \leq 10000$ ($i=2,3$) and
$10 \leq x_i \leq 1000$ ($i=4,\ldots,8$)"""

PROBLEM_G11: str = r"""## Problem G11:
Minimize: 
$$f(\mathbf{x}) = x_1^{2} + (x_{2} - 1)^{2}$$
subject to:
$$h_1(\mathbf{x}) = x_2 -x_{1}^{2} \leq 0 $$
where: $-1 \leq x_1 \leq 1$, $-1 \leq x_2 \leq 1$"""

PROBLEM_G12: str = r"""## Problem G12
Minimize: 
$$f(\mathbf{x}) = -(100 - (x_1 - 5)^{2} - (x_2 - 5)^{2} - (x_3 - 5)^{2}) / 100$$
subject to:
$$g_1(\mathbf{x}) = (x_1 - p)^{2} + (x_2 - q)^{2} + (x_3 - r)^{2} - 0.0625 \leq 0 $$
where: $0 \leq x_i \leq 10$ ($i=1,2,3$) and $p,q,r = 1,2,\ldots,9$"""

PROBLEM_G13: str = r"""## Problem G13
Minimize:
$$f(\mathbf{x}) = e^{x_1 x_2 x_3 x_4 x_5}$$
subject to:
$$h_1 (\mathbf{x}) = x_1^{2} + x_2^{2} + x_3^{2} + x_4^{2} + x_5^{2} - 10 = 0$$
$$h_2 (\mathbf{x}) = x_2 x_3 - 5 x_4 x_5 = 0$$
$$h_3 (\mathbf{x}) = x_1^{3} + x_2^{3} + 1 = 0$$
where: $-2.3 \leq x_i \leq 2.3$ ($i=1,2$) and $-3.2 \leq x_i \leq 3.2$ ($i=3,4,5$)"""

PROBLEM_G14: str = r"""## Problem G14
Minimize:
$$f(\mathbf{x}) = \sum_{i=1}^{10} x_i \left( c_i + \ln \frac{x_i}{\sum_{j=1}^{10} x_j} \right)$$
subject to:
$$h_1(\mathbf{x}) = x_1 + 2 x_2 + 2 x_3 + x_6 + x_{10} - 2 = 0 $$
$$h_2(\mathbf{x}) = x_4 + 2 x_5 + x_6 + x_7 - 1 = 0 $$
$$h_3(\mathbf{x}) = x_3 + x_7 + x_8 + 2 x_9 + x_{10} - 1 = 0 $$
where: $0 < x_i \leq 10$ ($i=1,\ldots,10$) and $c_1 = -6.089$, $c_2 = -17.164$, $c_3 = -34.054$,
$c_4 = -5.914$, $c_5 = -24.721$, $c_6 = -14.986$, $c_7 = -24.1$, $c_8 = -10.708$, $c_9 = -26.662$ and
$c_{10} = -22.179$"""

PROBLEM_G15: str = r"""## Problem G15
Minimize:
$$f(\mathbf{x}) = 1000 - x_1^{2} - 2x_2^{2} - x_3^{2} - x_1 x_2 - x_1 x_3$$
subject to:
$$h_1(\mathbf{x}) = x_1^{2} + x_2^{2} + x_3^{2} - 25 = 0 $$
$$h_2(\mathbf{x}) = 8x_1 + 14x_2 + 7x_3 - 56 = 0 $$
where: $0 < x_i \leq 10$ ($i=1,2,3$)"""

PROBLEM_G17: str = r"""## Problem G17
Minimize:
$$f(\mathbf{x}) = f_1(x_1) + f_2(x_2)$$
where:
$$ f_1(x_1) = \left\lbrace \begin{array}{l l}
30 x_1 & 0\leq x_1 < 300 \\
31x_1 & 300 \leq x_1 < 400 \end{array} \right. $$

$$ f_2(x_2) = \left\lbrace \begin{array}{l l}
28 x_2 & 0\leq x_2 < 100 \\
29 x_2 & 100\leq x_2 < 200 \\
30 x_2 & 200\leq x_2 < 1000 \end{array} \right. $$
subject to:
$$h_1(\mathbf{x}) = - x_1 + 300 - \frac{x_3 x_4}{131.078} \cos (1.48477 - x_6) + 
\frac{0.90798 x_3^{2}}{131.078} \cos (1.47588) = 0 $$
$$h_2(\mathbf{x}) = - x_2 - \frac{x_3 x_4}{131.078} \cos (1.48477 + x_6) + 
\frac{0.90798 x_4^{2}}{131.078} \cos (1.47588) = 0 $$
$$h_3(\mathbf{x}) = - x_5 - \frac{x_3 x_4}{131.078} \sin (1.48477 + x_6) + 
\frac{0.90798 x_4^{2}}{131.078} \sin (1.47588) = 0 $$
$$h_4(\mathbf{x}) = 200 - \frac{x_3 x_4}{131.078} \sin (1.48477 - x_6) + 
\frac{0.90798 x_3^{2}}{131.078} \sin (1.47588) = 0 $$

where: $0 \leq x_1 \leq 300$, $0 \leq x_2 \leq 1000$, $340 \leq x_3 \leq 420$,
$340 \leq x_4 \leq 420$, $-1000 \leq x_5 \leq 1000$ and $0 \leq x_6 \leq 0.5236$"""

PROBLEM_G18: str = r"""## Problem G18
Minimize:
$$f(\mathbf{x}) = -0.5 (x_1 x_4 - x_2 x_3 + x_3 x_9 - x_5 x_9 + x_5 x_8 - x_6 x_7)$$
subject to:
$$g_1(\mathbf{x}) = x_3^{2} + x_4^{2} - 1 \leq 0$$
$$g_2(\mathbf{x}) = x_9^{2} - 1 \leq 0$$
$$g_3(\mathbf{x}) = x_5^{2} + x_6^{2} - 1 \leq 0$$
$$g_4(\mathbf{x}) = x_1^{2} + (x_2 - x_9)^{2} - 1 \leq 0$$
$$g_5(\mathbf{x}) = (x_1 - x_5)^{2} + (x_2 - x_6)^{2} - 1 \leq 0$$
$$g_6(\mathbf{x}) = (x_1 - x_7)^{2} + (x_2 - x_8)^{2} - 1 \leq 0$$
$$g_7(\mathbf{x}) = (x_3 - x_5)^{2} + (x_4 - x_6)^{2} - 1 \leq 0$$
$$g_8(\mathbf{x}) = (x_3 - x_7)^{2} + (x_4 - x_8)^{2} - 1 \leq 0$$
$$g_9(\mathbf{x}) = x_7^{2} + (x_8 - x_9)^{2} - 1 \leq 0$$
$$g_10(\mathbf{x}) = x_2 x_3 - x_1 x_4 \leq 0$$
$$g_11(\mathbf{x}) = - x_3 x_9 \leq 0$$
$$g_12(\mathbf{x}) = x_5 x_9 \leq 0$$
$$g_13(\mathbf{x}) = x_6 x_7 - x_5 x_8 \leq 0$$
where: $-10 \leq x_i \leq 10$ ($i=1,\ldots,8$) and $0 \leq x_9 \leq 20$"""
