"""
Quick test script for v0.3.0 installation
"""

print("Testing optimization-benchmarks v0.3.0 installation...\n")

# Test 1: Import package
print("1. Testing package import...")
try:
    import optimization_benchmarks
    print(f"   ✓ Package version: {optimization_benchmarks.__version__}")
    assert optimization_benchmarks.__version__ == "0.3.0"
except Exception as e:
    print(f"   ✗ Failed: {e}")
    exit(1)

# Test 2: Check tqdm
print("\n2. Testing tqdm dependency...")
try:
    import tqdm
    print(f"   ✓ tqdm available: {tqdm.__version__}")
except ImportError:
    print("   ✗ tqdm not installed!")
    exit(1)

# Test 3: Progress bars
print("\n3. Testing progress bars...")
try:
    from optimization_benchmarks import BenchmarkRunner
    import numpy as np
    
    def simple_opt(func, bounds, max_iter=10):
        x = np.random.uniform(bounds[0][0], bounds[0][1], len(bounds))
        return x, func(x)
    
    runner = BenchmarkRunner(simple_opt, show_progress=True, verbose=False, n_runs=2)
    results = runner.run_suite(functions=['sphere'])
    print("   ✓ Progress bars working!")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    exit(1)

# Test 4: Heatmap (if matplotlib available)
print("\n4. Testing heatmap visualization...")
try:
    from optimization_benchmarks import plot_search_heatmap
    import matplotlib.pyplot as plt
    
    points = np.random.uniform(-5, 5, (20, 2))
    fig = plot_search_heatmap('sphere', points, bins=5)
    plt.close(fig)
    print("   ✓ Heatmap visualization working!")
except ImportError:
    print("   ⚠ Matplotlib not available (optional)")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    exit(1)

# Test 5: Save plot
print("\n5. Testing multi-format export...")
try:
    from optimization_benchmarks import plot_function_2d, save_plot
    import os
    
    fig = plot_function_2d('sphere')
    files = save_plot('test_export', formats=['png'])
    
    assert os.path.exists('test_export.png')
    os.remove('test_export.png')
    plt.close(fig)
    print("   ✓ Multi-format export working!")
except ImportError:
    print("   ⚠ Matplotlib not available (optional)")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    exit(1)

print("\n" + "="*60)
print("✓ ALL TESTS PASSED! v0.3.0 is ready!")
print("="*60)
