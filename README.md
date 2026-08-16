# optimization-benchmarks

> **⚠️ This project has been renamed and moved to [banana-bench](https://github.com/ak-rahul/banana-bench).**
> `optimization-benchmarks` is archived and no longer maintained under this name — all development,
> bug fixes, and new features continue at **banana-bench** (`pip install banana-bench`,
> `import banana_bench`). This repository is kept as a historical reference and redirect only.
> See the [banana-bench README](https://github.com/ak-rahul/banana-bench#readme) for why the name
> changed. Everything below describes the last released state of this package before the rename.

[![PyPI version](https://img.shields.io/pypi/v/optimization-benchmarks)](https://pypi.org/project/optimization-benchmarks/)
[![Python](https://img.shields.io/pypi/pyversions/optimization-benchmarks)](https://pypi.org/project/optimization-benchmarks/)
[![Downloads](https://pepy.tech/badge/optimization-benchmarks)](https://pepy.tech/project/optimization-benchmarks)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ak-rahul/optimization-benchmarks/blob/main/LICENSE.md)
[![Build Status](https://github.com/ak-rahul/optimization-benchmarks/actions/workflows/quality.yml/badge.svg)](https://github.com/ak-rahul/optimization-benchmarks/actions/workflows/quality.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive collection of 55+ standard mathematical benchmark functions for testing and evaluating optimization algorithms.

## 📚 Documentation

Detailed documentation is available in the `docs/` directory:

- **[User Guide & Examples](docs/USER_GUIDE.md)**: Detailed tutorials on metadata, benchmarking, and utilities.
- **[Function Reference](docs/BENCHMARK_FUNCTIONS.md)**: Complete guide to all 55+ functions with domains and global minima.
- **[Visualization Gallery](docs/VISUALIZATION.md)**: Examples of all plotting and analysis tools.
- **[API Reference](docs/API_REFERENCE.md)**: Class and function definitions.

## 🎯 Features

- **55+ Benchmark Functions**: Multimodal, Unimodal, and Special functions.
- **Rich Metadata**: Access bounds, dimensions, known minima programmatically.
- **Visualization**: 2D/3D plots, convergence tracking, and heatmaps.
- **Benchmarking Tools**: Automated testing with `BenchmarkRunner`.
- **Zero Core Dependencies**: Only NumPy is required.

## 📦 Installation

### From PyPI
```bash
pip install optimization-benchmarks
```

### From Source
```bash
git clone https://github.com/ak-rahul/optimization-benchmarks.git
cd optimization-benchmarks
pip install -e .
```

To install with visualization support:
```bash
pip install optimization-benchmarks[viz]
```

## 🚀 Quick Start

```python
import numpy as np
from optimization_benchmarks import ackley, BenchmarkRunner

# 1. Use a single function
x = np.zeros(5)
print(f"Ackley(0) = {ackley(x)}")

# 2. Run a benchmark suite
def my_optimizer(func, bounds):
    # Your optimization logic here...
    return np.zeros(len(bounds)), 0.0

runner = BenchmarkRunner(my_optimizer, "MyAlgo", n_runs=5)
results = runner.run_suite(functions=['sphere', 'ackley'])
```

For detailed usage, see the **[User Guide](docs/USER_GUIDE.md)**.
