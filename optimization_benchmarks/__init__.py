"""
Optimization Benchmark Functions Package.

This package provides a collection of standard benchmark functions commonly used
in evaluating and comparing optimization algorithms:contentReference[oaicite:0]{index=0}. It includes
classic functions such as Ackley, Rastrigin, Rosenbrock, etc. These functions
originate from well-known test suites (e.g., the MVF library:contentReference[oaicite:1]{index=1} and CEC
benchmark sets).

Each function is exposed as a module-level function (e.g., `ackley`, `rastrigin`),
and also wrapped in a `BenchmarkFunction` instance for registry lookup.
Use the `get_function(name)` helper to retrieve a function by name.

References:
    Opfunu: A Python library of benchmark functions:contentReference[oaicite:2]{index=2}.
    Adorio (2005): MVF library of test functions:contentReference[oaicite:3]{index=3}.
"""
from .functions import (
    ackley, beale, bohachevsky1, bohachevsky2, booth, box_betts,
    branin, branin2, camel3, camel6, chichinadze, colville,
    corana, easom, eggholder, exp2, fraudenstein_roth, gear,
    goldstein_price, griewank, himmelblau, holzman1, holzman2,
    hosaki, hyperellipsoid, katsuura, kowalik, langerman,
    lennard_jones, leon, levy, maxmod, matyas, mccormick,
    michalewicz, multimod, rastrigin, rastrigin2, rosenbrock,
    rosenbrock_ext1, rosenbrock_ext2, schaffer1, schaffer2,
    schwefel1_2, schwefel2_21, schwefel2_22, schwefel2_26,
    schwefel3_2, sphere, sphere2, step, step2, stretched_v,
    sum_squares, trecanni, trefethen4, watson, xor, zettl,
    zimmerman,
)

class BenchmarkFunction:
    """
    Wrapper class for optimization benchmark functions.

    Each instance wraps a Python function that takes a NumPy array and returns a float.
    Instances can be called like a function to evaluate the benchmark.
    """
    def __init__(self, func):
        self._func = func
        self.name = func.__name__
        self.__doc__ = func.__doc__

    def __call__(self, x):
        return self._func(x)

    def __repr__(self):
        return f"<BenchmarkFunction {self.name}>"

# Populate the global registry of functions (name -> BenchmarkFunction instance)
FUNCTIONS = {
    fn.__name__.lower(): BenchmarkFunction(fn) for fn in (
        ackley, beale, bohachevsky1, bohachevsky2, booth, box_betts,
        branin, branin2, camel3, camel6, chichinadze, colville,
        corana, easom, eggholder, exp2, fraudenstein_roth, gear,
        goldstein_price, griewank, himmelblau, holzman1, holzman2,
        hosaki, hyperellipsoid, katsuura, kowalik, langerman,
        lennard_jones, leon, levy, maxmod, matyas, mccormick,
        michalewicz, multimod, rastrigin, rastrigin2, rosenbrock,
        rosenbrock_ext1, rosenbrock_ext2, schaffer1, schaffer2,
        schwefel1_2, schwefel2_21, schwefel2_22, schwefel2_26,
        schwefel3_2, sphere, sphere2, step, step2, stretched_v,
        sum_squares, trecanni, trefethen4, watson, xor, zettl,
        zimmerman
    )
}

def get_function(name: str) -> BenchmarkFunction:
    """
    Retrieve a benchmark function by name (case-insensitive).
    Raises KeyError if the function is not found.
    """
    key = name.lower()
    if key not in FUNCTIONS:
        raise KeyError(f"No benchmark function named '{name}'.")
    return FUNCTIONS[key]

# Public API
__all__ = [
    "ackley", "beale", "bohachevsky1", "bohachevsky2", "booth",
    "box_betts", "branin", "branin2", "camel3", "camel6",
    "chichinadze", "colville", "corana", "easom", "eggholder",
    "exp2", "fraudenstein_roth", "gear", "goldstein_price", "griewank",
    "himmelblau", "holzman1", "holzman2", "hosaki", "hyperellipsoid",
    "katsuura", "kowalik", "langerman", "lennard_jones", "leon",
    "levy", "maxmod", "matyas", "mccormick", "michalewicz",
    "multimod", "rastrigin", "rastrigin2", "rosenbrock",
    "rosenbrock_ext1", "rosenbrock_ext2", "schaffer1", "schaffer2",
    "schwefel1_2", "schwefel2_21", "schwefel2_22", "schwefel2_26",
    "schwefel3_2", "sphere", "sphere2", "step", "step2",
    "stretched_v", "sum_squares", "trecanni", "trefethen4", "watson",
    "xor", "zettl", "zimmerman", "get_function"
]
