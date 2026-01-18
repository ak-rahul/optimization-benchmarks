import time
from typing import Callable

import numpy as np
import pytest
from scipy.spatial.transform import Rotation

from optimization_benchmarks import (
    BenchmarkRunner,
    NoisyFunction,
    RotatedFunction,
    ShiftedFunction,
    ackley,
    rastrigin,
    sphere,
)


def test_noisy_function():
    # Test that noise makes results non-deterministic
    noisy_sphere = NoisyFunction(sphere, scale=1.0)
    x = np.zeros(5)

    val1 = noisy_sphere(x)
    val2 = noisy_sphere(x)

    assert val1 != val2, "Noisy function should be non-deterministic"

    # Test seed reproducibility
    noisy1 = NoisyFunction(sphere, scale=1.0, seed=42)
    noisy2 = NoisyFunction(sphere, scale=1.0, seed=42)

    assert noisy1(x) == noisy2(x), "Seeded noise should be reproducible"


def test_shifted_function():
    shift = np.array([1.0, 1.0])
    shifted_sphere = ShiftedFunction(sphere, shift=shift)

    # Optimum should be at [1, 1], so value there should be 0
    assert np.isclose(shifted_sphere(shift), 0.0), "Shifted sphere should be 0 at shift vector"

    # Value at original optimum [0, 0] should be sphere([-1, -1]) = 2
    assert np.isclose(shifted_sphere(np.zeros(2)), 2.0), "Shifted sphere calculation incorrect"


def test_rotated_function():
    # 2D rotation of 90 degrees
    matrix = np.array([[0, -1], [1, 0]])
    rotated_rastrigin = RotatedFunction(rastrigin, matrix=matrix)

    x = np.array([1.0, 0.0])
    # Rotated x should be [0, 1]
    # rastrigin([0, 1]) should equal rotated_rastrigin([1, 0])

    val_rot = rotated_rastrigin(x)
    val_orig = rastrigin(np.array([0.0, 1.0]))

    assert np.isclose(val_rot, val_orig), "Rotated function evaluation incorrect"


def test_parallel_benchmarking():
    # We use a dummy function that sleeps to test speedup,
    # but for unit tests we just check correctness and that it runs without error.

    def my_optimizer(func, bounds, **kwargs):
        return np.zeros(len(bounds)), 0.0

    # Test serial
    runner_serial = BenchmarkRunner(my_optimizer, n_runs=2, n_jobs=1, verbose=False)
    results_serial = runner_serial.run_suite(functions=["sphere"])
    assert len(results_serial) == 1
    assert results_serial[0]["n_runs"] == 2

    # Test parallel
    runner_parallel = BenchmarkRunner(my_optimizer, n_runs=2, n_jobs=2, verbose=False)
    results_parallel = runner_parallel.run_suite(functions=["sphere"])
    assert len(results_parallel) == 1
    assert results_parallel[0]["n_runs"] == 2
    assert results_parallel[0]["success_rate"] == 1.0
