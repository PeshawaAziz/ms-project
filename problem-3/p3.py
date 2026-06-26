import numpy as np
from scipy.integrate import trapezoid, simpson, fixed_quad

def f(x):
    return np.exp(x**2)

a = 0
b = 1

n_points = 101
x_vals = np.linspace(a, b, n_points)
y_vals = f(x_vals)

trap_result = trapezoid(y_vals, x_vals)
print(f"Trapezoidal Rule Result: {trap_result:.6f}")

simp_result = simpson(y_vals, x=x_vals)
print(f"Simpson's Rule Result:   {simp_result:.6f}")

gauss_result, _ = fixed_quad(f, a, b, n=5)
print(f"Gaussian (5-point) Result: {gauss_result:.6f}")

