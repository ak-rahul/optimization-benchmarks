import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from optimization_benchmarks import BENCHMARK_SUITE, get_all_functions  # noqa: E402


def generate_benchmark_docs():
    """Generate detailed markdown documentation for all benchmark functions."""

    lines = [
        "# Benchmark Functions Reference",
        "",
        "This document provides a detailed reference for all benchmark functions available in the package.",
        "",
        "## Summary",
        "",
        f"Total functions: {len(get_all_functions())}",
        "",
        "| Function | Dimensions | Domain | Global Minimum |",
        "|----------|------------|--------|----------------|",
    ]

    # Sort functions alphabetically
    sorted_functions = sorted(BENCHMARK_SUITE.items())

    # Generate Table of Contents / Summary Table
    for name, info in sorted_functions:
        dim = f"{info['default_dim']}D"
        # Format bounds nicely
        bounds = info["bounds"]
        if len(set(bounds)) == 1:
            # All dimensions have same bounds
            b = bounds[0]
            domain = f"[{b[0]}, {b[1]}]^n"
        else:
            domain = "Varies"

        known_min = f"{info['known_minimum']:.6g}"

        lines.append(f"| [{name}](#{name}) | {dim} | {domain} | {known_min} |")

    lines.append("")
    lines.append("## Detailed Descriptions")
    lines.append("")

    # Generate Detail Sections
    for name, info in sorted_functions:
        func = info["function"]
        doc = func.__doc__ or "No description available."
        # Clean up docstring
        doc = "\n".join([line.strip() for line in doc.split("\n") if line.strip()])

        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"**Default Dimension:** {info['default_dim']}")
        lines.append(f"**Known Minimum:** {info['known_minimum']}")
        if info["optimal_point"] is not None:
            lines.append(f"**Optimal Point:** `x = {info['optimal_point']}`")

        lines.append("")
        lines.append("#### Description")
        lines.append(doc)
        lines.append("")
        lines.append("#### Code Example")
        lines.append("```python")
        lines.append(f"from optimization_benchmarks import {name}")
        lines.append("import numpy as np")
        lines.append("")
        lines.append(f"# Run {name}")
        lines.append(f"x = np.zeros({info['default_dim']})")
        lines.append(f"result = {name}(x)")
        lines.append(f"print(f'result: {{result}}')")
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")

    output_file = project_root / "docs" / "BENCHMARK_FUNCTIONS.md"
    output_file.parent.mkdir(exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Documentation generated at {output_file}")


if __name__ == "__main__":
    generate_benchmark_docs()
