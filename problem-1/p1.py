import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

x_points = np.array([0, 1, 2, 3, 4, 5])
y_points = np.array([1, 3, 2, 5, 4, 6])

poly_lagrange = lagrange(x_points, y_points)
print("--- Lagrange Polynomial ---")
print(poly_lagrange)
print("\n")

spline_cubic = CubicSpline(x_points, y_points)
print("--- Cubic Spline Coefficients ---")
print(spline_cubic.c)
print("\n")

x_continuous = np.linspace(0, 5, 100)
y_lagrange = poly_lagrange(x_continuous)
y_spline = spline_cubic(x_continuous)

plt.figure(figsize=(8, 6))
plt.scatter(x_points, y_points, color='red', label='Data Points', zorder=5)
plt.plot(x_continuous, y_lagrange, label='Lagrange Interpolation', linestyle='--')
plt.plot(x_continuous, y_spline, label='Cubic Spline', linestyle='-')

plt.title('Comparison of Lagrange and Cubic Spline Interpolation')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

