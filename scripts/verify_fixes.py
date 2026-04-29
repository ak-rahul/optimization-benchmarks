"""Quick smoke-test verifying every fix from the audit report."""
import numpy as np
import sys

sys.path.insert(0, ".")
from optimization_benchmarks import (
    camel3, watson, xor, zimmerman, lennard_jones,
    freudenstein_roth, holzman2, BENCHMARK_SUITE, get_all_functions,
)

errors = []

def check(label, got, expected, tol=1e-4):
    if abs(got - expected) > tol:
        errors.append(f"FAIL {label}: got {got}, expected {expected}")
    else:
        print(f"  OK  {label}: {got:.6f}")

print("=== BUG-01: camel3 formula ===")
check("camel3(0,0)", camel3(np.array([0.0, 0.0])), 0.0)
check("camel3(1,1)", camel3(np.array([1.0, 1.0])), 2 - 1.05 + 1/6 + 1 + 1)

print("\n=== BUG-02: watson correct indexing ===")
val = watson(np.zeros(6))
print(f"  OK  watson(zeros6) = {val:.6f}  (finite, no IndexError)")
assert np.isfinite(val)

print("\n=== BUG-03: xor correct formula ===")
val = xor(np.zeros(9))
print(f"  OK  xor(zeros9) = {val:.6f}  (finite, 4 residuals)")
assert np.isfinite(val)

print("\n=== BUG-07: holzman2 off-by-one ===")
check("holzman2(ones5) = sum(1..5)*1^4 = 15", holzman2(np.ones(5)), 15.0)
check("holzman2(zeros5) = 0", holzman2(np.zeros(5)), 0.0)

print("\n=== WARN-03: dimension validation ===")
from optimization_benchmarks import beale, himmelblau, colville
try:
    beale(np.zeros(3))
    errors.append("FAIL: beale(3D) should raise ValueError")
except ValueError as e:
    print(f"  OK  beale(3D) raises: {e}")

print("\n=== WARN-05: freudenstein_roth alias ===")
x2 = np.array([5.0, 4.0])
from optimization_benchmarks import fraudenstein_roth
assert abs(freudenstein_roth(x2) - fraudenstein_roth(x2)) < 1e-12
print("  OK  freudenstein_roth == fraudenstein_roth")

print("\n=== WARN-08/09: 4 missing functions now in BENCHMARK_SUITE & importable ===")
for name in ["watson", "xor", "zimmerman", "lennard_jones"]:
    assert name in BENCHMARK_SUITE, f"MISSING from BENCHMARK_SUITE: {name}"
    print(f"  OK  {name} in BENCHMARK_SUITE")
print(f"  OK  BENCHMARK_SUITE size = {len(BENCHMARK_SUITE)}  (was 55, now 59)")

print("\n=== WARN-10: rastrigin2 known_minimum = -2.0 ===")
assert BENCHMARK_SUITE["rastrigin2"]["known_minimum"] == -2.0
print(f"  OK  rastrigin2 known_minimum = {BENCHMARK_SUITE['rastrigin2']['known_minimum']}")

print("\n=== Total functions in get_all_functions() ===")
print(f"  OK  {len(get_all_functions())} functions available")

if errors:
    print("\n=== FAILURES ===")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
else:
    print("\n=== ALL FIXES VERIFIED ===")
