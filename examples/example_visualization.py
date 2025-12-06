"""
Example: Visualization Features

This script demonstrates all visualization capabilities of the package.
"""

import numpy as np
import matplotlib.pyplot as plt
from optimization_benchmarks.visualization import (
    plot_function_2d,
    plot_function_3d,
    plot_convergence,
    plot_trajectory_2d,
    plot_algorithm_comparison,
    plot_benchmark_summary
)


def main():
    print("=" * 70)
    print("VISUALIZATION EXAMPLES")
    print("=" * 70)
    
    # 1. 2D Contour Plot
    print("\n1. Creating 2D contour plot of Ackley function...")
    fig = plot_function_2d('ackley', resolution=100, show_optimum=True)
    plt.savefig('ackley_2d.png', dpi=300, bbox_inches='tight')
    print("   Saved as 'ackley_2d.png'")
    plt.close()
    
    # 2. 3D Surface Plot
    print("\n2. Creating 3D surface plot of Rastrigin function...")
    fig = plot_function_3d('rastrigin', resolution=50, elevation=30, azimuth=45)
    plt.savefig('rastrigin_3d.png', dpi=300, bbox_inches='tight')
    print("   Saved as 'rastrigin_3d.png'")
    plt.close()
    
    # 3. Convergence Plot
    print("\n3. Creating convergence plot...")
    history = np.logspace(2, -2, 100)  # Simulated convergence
    fig = plot_convergence(
        history,
        function_name='sphere',
        known_minimum=0.0,
        log_scale=True
    )
    plt.savefig('convergence.png', dpi=300, bbox_inches='tight')
    print("   Saved as 'convergence.png'")
    plt.close()
    
    # 4. Trajectory Plot
    print("\n4. Creating trajectory plot...")
    t = np.linspace(0, 2*np.pi, 50)
    trajectory = np.column_stack([5*np.cos(t)*np.exp(-t/3), 5*np.sin(t)*np.exp(-t/3)])
    fig = plot_trajectory_2d('sphere', trajectory, resolution=50)
    plt.savefig('trajectory.png', dpi=300, bbox_inches='tight')
    print("   Saved as 'trajectory.png'")
    plt.close()
    
    # 5. Algorithm Comparison
    print("\n5. Creating algorithm comparison plot...")
    results = {
        'Algorithm A': {
            'sphere': {'error': 0.001, 'time': 1.2},
            'ackley': {'error': 0.01, 'time': 1.5},
            'rastrigin': {'error': 0.1, 'time': 2.0}
        },
        'Algorithm B': {
            'sphere': {'error': 0.01, 'time': 0.8},
            'ackley': {'error': 0.05, 'time': 1.0},
            'rastrigin': {'error': 0.5, 'time': 1.5}
        }
    }
    fig = plot_algorithm_comparison(results, metric='error')
    plt.savefig('algorithm_comparison.png', dpi=300, bbox_inches='tight')
    print("   Saved as 'algorithm_comparison.png'")
    plt.close()
    
    # 6. Benchmark Summary
    print("\n6. Creating benchmark summary plot...")
    benchmark_results = [
        {'function': 'sphere', 'error': 0.001, 'time': 1.0},
        {'function': 'ackley', 'error': 0.01, 'time': 1.5},
        {'function': 'rastrigin', 'error': 0.1, 'time': 2.0},
        {'function': 'rosenbrock', 'error': 1.0, 'time': 2.5},
        {'function': 'griewank', 'error': 0.05, 'time': 1.8}
    ]
    fig = plot_benchmark_summary(benchmark_results)
    plt.savefig('benchmark_summary.png', dpi=300, bbox_inches='tight')
    print("   Saved as 'benchmark_summary.png'")
    plt.close()
    
    print("\n" + "=" * 70)
    print("✓ All visualization examples completed!")
    print("=" * 70)


if __name__ == '__main__':
    main()
