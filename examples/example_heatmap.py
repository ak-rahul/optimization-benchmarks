"""
Example: Search Heatmap Visualization

This example demonstrates the new heatmap feature in v0.3.0,
showing where an optimization algorithm searches in the function space.
"""

import numpy as np
from optimization_benchmarks import plot_search_heatmap
import matplotlib.pyplot as plt


def simple_random_search(func, bounds, max_iter=100):
    """
    Simple random search algorithm (for demonstration).
    Collects all evaluated points for heatmap visualization.
    """
    points_history = []
    
    best_x = None
    best_cost = np.inf
    
    for i in range(max_iter):
        # Generate random point
        x = np.array([
            np.random.uniform(bounds[j][0], bounds[j][1])
            for j in range(len(bounds))
        ])
        
        # Evaluate
        cost = func(x)
        
        # Store point
        points_history.append(x.copy())
        
        # Update best
        if cost < best_cost:
            best_cost = cost
            best_x = x.copy()
    
    return best_x, best_cost, np.array(points_history)


def example_basic_heatmap():
    """Basic heatmap example."""
    print("=" * 60)
    print("Example 1: Basic Heatmap")
    print("=" * 60)
    
    # Run optimizer
    from optimization_benchmarks import sphere
    bounds = [(-5, 5), (-5, 5)]
    
    best_x, best_cost, points = simple_random_search(sphere, bounds, max_iter=200)
    
    print(f"Best solution: {best_x}")
    print(f"Best cost: {best_cost:.6f}")
    print(f"Points evaluated: {len(points)}")
    
    # Plot heatmap
    fig = plot_search_heatmap('sphere', points, bins=30)
    plt.show()


def example_multiple_functions():
    """Heatmap for multiple functions."""
    print("\n" + "=" * 60)
    print("Example 2: Multiple Functions")
    print("=" * 60)
    
    functions = ['sphere', 'ackley', 'rastrigin', 'rosenbrock']
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.flatten()
    
    for idx, func_name in enumerate(functions):
        print(f"\nTesting {func_name}...")
        
        # Get function
        from optimization_benchmarks import get_function_info
        info = get_function_info(func_name)
        func = info['function']
        
        # Normalize bounds
        from optimization_benchmarks import normalize_bounds
        bounds = normalize_bounds(info['bounds'], 2)
        
        # Run optimizer
        best_x, best_cost, points = simple_random_search(func, bounds, max_iter=150)
        
        print(f"  Best cost: {best_cost:.6f}")
        print(f"  Points evaluated: {len(points)}")
        
        # Create subplot
        plt.sca(axes[idx])
        plot_search_heatmap(func_name, points, bins=25, show_function=True)
    
    plt.tight_layout()
    plt.show()


def example_comparison():
    """Compare search patterns of different strategies."""
    print("\n" + "=" * 60)
    print("Example 3: Strategy Comparison")
    print("=" * 60)
    
    def random_search(func, bounds, max_iter=100):
        """Pure random search."""
        points = []
        best_x, best_cost = None, np.inf
        
        for _ in range(max_iter):
            x = np.array([np.random.uniform(b[0], b[1]) for b in bounds])
            cost = func(x)
            points.append(x)
            if cost < best_cost:
                best_cost = cost
                best_x = x
        
        return best_x, best_cost, np.array(points)
    
    def grid_search(func, bounds, grid_size=10):
        """Grid search."""
        points = []
        best_x, best_cost = None, np.inf
        
        x_vals = np.linspace(bounds[0][0], bounds[0][1], grid_size)
        y_vals = np.linspace(bounds[1][0], bounds[1][1], grid_size)
        
        for x in x_vals:
            for y in y_vals:
                point = np.array([x, y])
                cost = func(point)
                points.append(point)
                if cost < best_cost:
                    best_cost = cost
                    best_x = point
        
        return best_x, best_cost, np.array(points)
    
    # Test on Ackley function
    from optimization_benchmarks import ackley
    bounds = [(-5, 5), (-5, 5)]
    
    # Run both strategies
    _, _, random_points = random_search(ackley, bounds, max_iter=100)
    _, _, grid_points = grid_search(ackley, bounds, grid_size=10)
    
    # Plot comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    plt.sca(ax1)
    plot_search_heatmap('ackley', random_points, bins=20)
    ax1.set_title('Random Search Strategy', fontsize=14, fontweight='bold')
    
    plt.sca(ax2)
    plot_search_heatmap('ackley', grid_points, bins=20)
    ax2.set_title('Grid Search Strategy', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.show()


def example_save_formats():
    """Save heatmap in multiple formats."""
    print("\n" + "=" * 60)
    print("Example 4: Save in Multiple Formats")
    print("=" * 60)
    
    from optimization_benchmarks import rastrigin, save_plot
    
    bounds = [(-5, 5), (-5, 5)]
    best_x, best_cost, points = simple_random_search(rastrigin, bounds, max_iter=200)
    
    # Create plot
    fig = plot_search_heatmap('rastrigin', points)
    
    # Save in multiple formats
    files = save_plot('rastrigin_heatmap', formats=['png', 'svg', 'pdf'])
    
    print(f"\nSaved {len(files)} files:")
    for f in files:
        print(f"  ✓ {f}")
    
    plt.close(fig)


if __name__ == "__main__":
    print("🗺️  Heatmap Visualization Examples - v0.3.0\n")
    
    # Run examples
    example_basic_heatmap()
    example_multiple_functions()
    example_comparison()
    example_save_formats()
    
    print("\n" + "=" * 60)
    print("✓ All examples completed!")
    print("=" * 60)
