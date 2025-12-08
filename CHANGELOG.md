# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2025-12-08

### Added
- **Progress Bars**: tqdm integration for visual progress tracking during benchmarking
  - Added `show_progress` parameter to `BenchmarkRunner`
  - Real-time progress display for functions and runs
  - Customizable progress bar descriptions

- **Heatmap Visualization**: New `plot_search_heatmap()` function
  - Visualize where optimization algorithms search in the function landscape
  - Customizable bin sizes and color schemes
  - Overlay on function contours for better insights

- **Multi-Format Export**: Export plots to multiple formats simultaneously
  - New `save_plot()` utility function
  - Support for PNG, SVG, PDF, EPS formats
  - Configurable DPI for raster formats
  - Added `formats` parameter to all plotting functions

- **Enhanced Color Schemes**: Expanded colormap options
  - Added 9 colormap choices: viridis, plasma, inferno, magma, cividis, coolwarm, jet, rainbow, turbo
  - Better documentation for colormap usage

- **Batch Plotting**: New `batch_plot_functions()` for generating multiple plots
  - Generate all function plots at once
  - Consistent styling across all plots
  - Automatic file naming and organization

### Changed
- Updated `tqdm` as core dependency (>=4.65.0)
- Enhanced progress reporting in `BenchmarkRunner`
- Improved plot aesthetics with better default settings
- Updated documentation with new feature examples

### Fixed
- Minor bug fixes in visualization module
- Improved error handling in export functions

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
