# Changelog

## [0.2.0] - 2025-12-06

### Added
- **New `utils` module** with helper functions:
  - `normalize_bounds()` - Universal bounds normalization
  - `generate_random_point()` - Smart random point generation
  - `check_bounds()` - Bounds validation
  - `scale_to_unit()` / `scale_from_unit()` - Coordinate transformations
  - `clip_to_bounds()` - Point clipping
  - `get_bounds_range()` / `get_bounds_center()` - Bounds utilities
  - `generate_grid_points()` - Grid generation
  - `calculate_distance_to_optimum()` - Distance metrics

- **New `visualization` module** (requires matplotlib):
  - `plot_function_2d()` - 2D contour plots
  - `plot_function_3d()` - 3D surface plots
  - `plot_convergence()` - Convergence tracking
  - `plot_trajectory_2d()` - Optimization path visualization
  - `plot_algorithm_comparison()` - Multi-algorithm comparison
  - `plot_benchmark_summary()` - Comprehensive result summaries

- **New `benchmarking` module** with systematic testing tools:
  - `BenchmarkRunner` class - Automated algorithm testing
  - `quick_benchmark()` - Fast benchmarking function
  - Automatic result aggregation and statistics
  - CSV/JSON export functionality
  - Multi-run support with statistical analysis

- **Examples directory** with complete usage demonstrations
- Optional dependency group `[viz]` for visualization features
- Comprehensive test suite for new modules

### Changed
- Updated `__init__.py` to export new utilities
- Enhanced documentation with visualization and benchmarking examples
- Improved package metadata in `pyproject.toml`

### Dependencies
- Added optional `matplotlib>=3.3.0` for visualization features
- Core functionality remains dependency-free (only numpy required)

## [0.1.1] - 2025-10-17

### Added
- Added `BENCHMARK_SUITE` metadata dictionary with complete function information
- New helper functions: `get_function_info()`, `get_all_functions()`, `get_bounds()`, `get_function_list()`
- Metadata includes bounds, dimensions, known minima, and optimal points for all 55 functions
- Simplified benchmarking without manual specification of bounds

### Changed
- Improved documentation with metadata usage examples

## [0.1.0] - 2025-10-16

### Added
- Initial release with 55 benchmark functions
- Command-line interface (optbench)
- Comprehensive test suite
- Full academic citations
