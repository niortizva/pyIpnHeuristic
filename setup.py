"""
    MIT License

    Copyright (c) 2022 National Politecnic Institute

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
from setuptools import find_packages, setup

setup(
    name='pyIpnHeuristic',
    packages=find_packages(exclude=['tests']),
    version='0.2.2',
    description='pyIpnHeuristic is a pure Python implementation of some heuristic algorithms',
    long_description="""pyIpnHeuristic is a pure Python implementation of some heuristic algorithms for the National
    Polytechnic Institute of Mexico. For more information on pyIpnHeuristic, visit the `GitHub project page 
    <https://github.com/niortizva/pyIpnHeuristic>`_.""",
    author='Nicolas Ortiz',
    author_email='nortizv2100@alumno.ipn.com',
    maintainer='Nicolas Ortiz',
    maintainer_email='nortizv2100@alumno.ipn.com',
    url='https://github.com/niortizva/pyIpnHeuristic',
    license='BSD 3-Clause License',
    classifiers=[
        'Development Status :: Development',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
