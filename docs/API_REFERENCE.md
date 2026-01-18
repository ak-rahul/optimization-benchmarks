# API Reference

This document provides detailed API documentation for the core components of `optimization-benchmarks`.

## Core Components

### `BenchmarkRunner`

The `BenchmarkRunner` class is the main engine for systematically testing optimization algorithms.

```python
from optimization_benchmarks import BenchmarkRunner
```

#### Constructor

```python
BenchmarkRunner(
    algorithm: Callable,
    algorithm_name: Optional[str] = None,
    n_runs: int = 1,
    seed: Optional[int] = None,
    verbose: bool = True,
    show_progress: bool = True
)
```

**Parameters:**
- `algorithm`: Callable with signature `func(f, bounds, **kwargs) -> (best_x, best_cost)`.
- `algorithm_name`: String name for the report.
- `n_runs`: Number of independent runs per function (default: 1).
- `seed`: Random seed for reproducibility.
- `verbose`: Print progress to stdout.
- `show_progress`: Show tqdm progress bars (default: True).
- `n_jobs`: Number of parallel jobs (v0.4.0).
  - `None` or `1`: Serial execution.
  - `-1`: Use all available CPU cores.
  - `int > 1`: Use specific number of cores.

#### Methods

**`run_suite(functions=None, dimensions=None, **kwargs)`**

Run the benchmark suite on selected functions.

- `functions`: List of function names (e.g., `['sphere', 'ackley']`). If None, runs all 55+ functions.
- `dimensions`: Dictionary mapping function names to custom dimensions (e.g., `{'sphere': 10}`).
- `**kwargs`: Additional arguments passed to your optimization algorithm.

**Returns:** A list of result dictionaries.

**`save_results(filepath, format='csv')`**

Save benchmark results to a file.
- `format`: 'csv' or 'json'.

**`get_summary_stats()`**

Returns a dictionary containing aggregate statistics (mean error, success rate, etc.).

### `Wrappers` (v0.4.0)

Wrappers modify the behavior of benchmark functions. They follow the decorator pattern and are callable like normal functions.

**`NoisyFunction(func, noise_type='gaussian', scale=0.1, seed=None)`**
- `func`: The benchmark function to wrap.
- `noise_type`: 'gaussian' (normal distribution) or 'uniform'.
- `scale`: Standard deviation (for gaussian) or half-width (for uniform).
- `seed`: Integer seed for reproducible noise. Uses a local random number generator.

**`ShiftedFunction(func, shift)`**
- `func`: The benchmark function to wrap.
- `shift`: List or array of shift values. Must match function dimension.
  - New global minimum location: $x^* + \text{shift}$

**`RotatedFunction(func, matrix)`**
- `func`: The benchmark function to wrap.
- `matrix`: An orthogonal rotation matrix ($n \times n$).
  - Evaluates $f(M \cdot x)$.

### `quick_benchmark`

A helper function for rapid testing without creating a class instance.

```python
from optimization_benchmarks import quick_benchmark

results = quick_benchmark(
    my_optimizer,
    function_names=['sphere', 'ackley'],
    n_runs=5,
    max_iter=100
)
```

## Utility Functions

### Bounds & Geometry

**`normalize_bounds(bounds, dim)`**
Converts various bound formats into a standard list of `(min, max)` tuples.

**`check_bounds(point, bounds)`**
Returns `True` if point is within bounds.

**`clip_to_bounds(point, bounds)`**
Constrains a point to lie within the specified bounds.

**`generate_random_point(bounds, method='uniform')`**
Generates a random point within bounds. Methods: `'uniform'`, `'normal'`, `'center_biased'`.

### Metadata Access

**`get_all_functions()`**
Returns a list of all available function names.

**`get_function_info(name)`**
Returns a dictionary with keys: `function`, `bounds`, `default_dim`, `known_minimum`, `optimal_point`.

## Type Hints

The package is fully typed. You can import types for static analysis:

```python
from typing import Callable, Tuple
import numpy as np

OptimizerType = Callable[
    [Callable[[np.ndarray], float], List[Tuple[float, float]]], 
    Tuple[np.ndarray, float]
]
```
