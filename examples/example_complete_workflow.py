"""
Example: Complete Workflow

This script demonstrates a complete optimization workflow combining
all features: optimization, benchmarking, and visualization.
"""

import numpy as np
import matplotlib.pyplot as plt
from optimization_benchmarks import (
    BenchmarkRunner,
    get_function_info,
    normalize_bounds,
    generate_random_point,
    clip_to_bounds,
    plot_function_2d,
    plot_convergence,
    plot_trajectory_2d,
    plot_benchmark_summary
)


def simulated_annealing(func, bounds, max_iter=1000, temp=100, cooling=0.99, return_history=False):
    """
    Simulated Annealing optimizer with history tracking.
    """
    bounds = normalize_bounds(bounds, len(bounds))
    bounds_array = np.array(bounds)
    
    # Initialize
    current_x = generate_random_point(bounds)
    current_cost = func(current_x)
    
    best_x = current_x.copy()
    best_cost = current_cost
    
    # History tracking
    history = [best_cost]
    trajectory = [best_x.copy()]
    
    current_temp = temp
    
    for iteration in range(max_iter):
        # Generate neighbor
        step_size = 0.1 * (bounds_array[:, 1] - bounds_array[:, 0]) * (current_temp / temp)
        neighbor_x = current_x + np.random.randn(len(bounds)) * step_size
        neighbor_x = clip_to_bounds(neighbor_x, bounds)
        
        # Evaluate
        neighbor_cost = func(neighbor_x)
        
        # Acceptance criterion
        delta = neighbor_cost - current_cost
        if delta < 0 or (current_temp > 1e-10 and np.random.random() < np.exp(-delta / current_temp)):
            current_x = neighbor_x
            current_cost = neighbor_cost
            
            if current_cost < best_cost:
                best_x = current_x.copy()
                best_cost = current_cost
                trajectory.append(best_x.copy())
        
        history.append(best_cost)
        current_temp *= cooling
    
    if return_history:
        return best_x, best_cost, {'history': history, 'trajectory': np.array(trajectory)}
    else:
        return best_x, best_cost


def main():
    print("=" * 90)
    print("COMPLETE WORKFLOW EXAMPLE")
    print("=" * 90)
    
    # Step 1: Visualize test function
    print("\n[Step 1] Visualizing test function...")
    fig = plot_function_2d('sphere', resolution=100, show_optimum=True)
    plt.savefig('workflow_function.png', dpi=300, bbox_inches='tight')
    print("   ✓ Saved 'workflow_function.png'")
    plt.close()
    
    # Step 2: Run single optimization with visualization
    print("\n[Step 2] Running single optimization...")
    info = get_function_info('sphere')
    func = info['function']
    bounds = normalize_bounds(info['bounds'], 2)
    
    best_x, best_cost, extras = simulated_annealing(
        func, bounds,
        max_iter=500,
        temp=50,
        cooling=0.99,
        return_history=True
    )
    
    print(f"   Best cost found: {best_cost:.6f}")
    print(f"   Best point: {best_x}")
    
    # Step 3: Plot convergence
    print("\n[Step 3] Plotting convergence...")
    fig = plot_convergence(
        extras['history'],
        function_name='sphere',
        known_minimum=0.0,
        log_scale=True
    )
    plt.savefig('workflow_convergence.png', dpi=300, bbox_inches='tight')
    print("   ✓ Saved 'workflow_convergence.png'")
    plt.close()
    
    # Step 4: Plot trajectory
    print("\n[Step 4] Plotting optimization trajectory...")
    fig = plot_trajectory_2d('sphere', extras['trajectory'], resolution=50)
    plt.savefig('workflow_trajectory.png', dpi=300, bbox_inches='tight')
    print("   ✓ Saved 'workflow_trajectory.png'")
    plt.close()
    
    # Step 5: Run comprehensive benchmark
    print("\n[Step 5] Running comprehensive benchmark...")
    
    # Wrapper that doesn't return history (for benchmarking)
    def sa_wrapper(f, b, **kw):
        return simulated_annealing(f, b, return_history=False, **kw)
    
    runner = BenchmarkRunner(
        algorithm=sa_wrapper,
        algorithm_name='SimulatedAnnealing',
        n_runs=5,
        seed=42,
        verbose=True
    )
    
    # Test on multiple functions
    test_functions = [
        'sphere', 'ackley', 'rastrigin', 'rosenbrock', 'griewank',
        'beale', 'booth', 'himmelblau', 'easom', 'goldstein_price'
    ]
    
    results = runner.run_suite(
        functions=test_functions,
        max_iter=2000,
        temp=100,
        cooling=0.99
    )
    
    # Step 6: Save results
    print("\n[Step 6] Saving results...")
    runner.save_results('workflow_results.csv', format='csv')
    runner.save_results('workflow_results.json', format='json')
    print("   ✓ Saved 'workflow_results.csv'")
    print("   ✓ Saved 'workflow_results.json'")
    
    # Step 7: Visualize benchmark summary
    print("\n[Step 7] Creating benchmark summary visualization...")
    fig = plot_benchmark_summary(results)
    plt.savefig('workflow_benchmark_summary.png', dpi=300, bbox_inches='tight')
    print("   ✓ Saved 'workflow_benchmark_summary.png'")
    plt.close()
    
    # Step 8: Display summary statistics
    print("\n[Step 8] Summary Statistics")
    print("-" * 90)
    stats = runner.get_summary_stats()
    print(f"Algorithm: {stats['algorithm']}")
    print(f"Functions tested: {len(test_functions)}")
    print(f"Total runs: {stats['n_results']}")
    print(f"Successful runs: {stats['n_successful']}")
    print(f"Success rate: {stats['success_rate']*100:.1f}%")
    print(f"\nError Statistics:")
    print(f"  Mean:   {stats['error_mean']:.6f}")
    print(f"  Median: {stats['error_median']:.6f}")
    print(f"  Min:    {stats['error_min']:.6f}")
    print(f"  Max:    {stats['error_max']:.6f}")
    print(f"\nTime Statistics:")
    print(f"  Total:  {stats['time_total']:.2f}s")
    print(f"  Mean:   {stats['time_mean']:.2f}s")
    print(f"  Median: {stats['time_median']:.2f}s")
    
    print("\n" + "=" * 90)
    print("✓ COMPLETE WORKFLOW FINISHED!")
    print("=" * 90)
    print("\nGenerated files:")
    print("  - workflow_function.png")
    print("  - workflow_convergence.png")
    print("  - workflow_trajectory.png")
    print("  - workflow_benchmark_summary.png")
    print("  - workflow_results.csv")
    print("  - workflow_results.json")
    print("\n" + "=" * 90)


if __name__ == '__main__':
    main()
