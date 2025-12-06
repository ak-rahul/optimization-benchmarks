"""
Example: Benchmarking Utilities

This script demonstrates how to use the benchmarking tools.
"""

import numpy as np
from optimization_benchmarks import BenchmarkRunner, quick_benchmark
from optimization_benchmarks.utils import normalize_bounds, generate_random_point, clip_to_bounds


def simple_random_search(func, bounds, max_iter=1000):
    """Simple random search optimizer."""
    bounds = normalize_bounds(bounds, len(bounds))
    bounds_array = np.array(bounds)
    
    best_x = generate_random_point(bounds)
    best_cost = func(best_x)
    
    for _ in range(max_iter):
        x = generate_random_point(bounds)
        cost = func(x)
        
        if cost < best_cost:
            best_cost = cost
            best_x = x
    
    return best_x, best_cost


def simple_hill_climbing(func, bounds, max_iter=1000):
    """Simple hill climbing optimizer."""
    bounds = normalize_bounds(bounds, len(bounds))
    bounds_array = np.array(bounds)
    
    # Start from center
    current_x = (bounds_array[:, 0] + bounds_array[:, 1]) / 2
    current_cost = func(current_x)
    
    best_x = current_x.copy()
    best_cost = current_cost
    
    step_size = 0.1
    
    for _ in range(max_iter):
        # Generate neighbor
        neighbor_x = current_x + np.random.randn(len(bounds)) * step_size
        neighbor_x = clip_to_bounds(neighbor_x, bounds)
        
        neighbor_cost = func(neighbor_x)
        
        # Accept if better
        if neighbor_cost < current_cost:
            current_x = neighbor_x
            current_cost = neighbor_cost
            
            if current_cost < best_cost:
                best_x = current_x.copy()
                best_cost = current_cost
        
        # Adaptive step size
        step_size *= 0.99
    
    return best_x, best_cost


def main():
    print("=" * 90)
    print("BENCHMARKING EXAMPLES")
    print("=" * 90)
    
    # Example 1: Quick Benchmark
    print("\n1. Quick Benchmark (Random Search)")
    print("-" * 90)
    
    results = quick_benchmark(
        simple_random_search,
        function_names=['sphere', 'ackley', 'rastrigin'],
        n_runs=5,
        max_iter=500
    )
    
    # Example 2: Detailed Benchmark with BenchmarkRunner
    print("\n\n2. Detailed Benchmark (Hill Climbing)")
    print("-" * 90)
    
    runner = BenchmarkRunner(
        algorithm=simple_hill_climbing,
        algorithm_name='HillClimbing',
        n_runs=10,
        seed=42,
        verbose=True
    )
    
    results = runner.run_suite(
        functions=['sphere', 'ackley', 'rastrigin', 'rosenbrock', 'griewank'],
        max_iter=1000
    )
    
    # Save results
    runner.save_results('hill_climbing_results.csv', format='csv')
    runner.save_results('hill_climbing_results.json', format='json')
    
    # Get summary statistics
    stats = runner.get_summary_stats()
    
    print("\n\n3. Summary Statistics")
    print("-" * 90)
    print(f"Algorithm: {stats['algorithm']}")
    print(f"Total tests: {stats['n_results']}")
    print(f"Successful: {stats['n_successful']}")
    print(f"Success rate: {stats['success_rate']*100:.1f}%")
    print(f"Mean error: {stats['error_mean']:.6f}")
    print(f"Median error: {stats['error_median']:.6f}")
    print(f"Total time: {stats['time_total']:.2f}s")
    print(f"Mean time: {stats['time_mean']:.2f}s")
    
    print("\n" + "=" * 90)
    print("✓ Benchmarking examples completed!")
    print("=" * 90)


if __name__ == '__main__':
    main()
