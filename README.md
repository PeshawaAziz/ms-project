# Mathematical Software Project

This repository contains the implementation of various numerical methods and data analysis tasks using Python. This project was developed as part of the "Mathematical Software" course.

## 🚀 Features

The project is divided into three main computational tasks:

### 1. Interpolation Analysis
- Implementation of **Lagrange Interpolation** and **Cubic Spline Interpolation**.
- Comparison of the two methods using visual plots (`scipy.interpolate`).
- Accurate derivation of polynomial coefficients.

### 2. Data Processing & Visualization
- Automated reading of execution time data from Excel files (`pandas`).
- Dynamic data insertion (adding 700KB test cases).
- Visualization of algorithm performance using:
  - Linear Scale Plots
  - Logarithmic Scale Plots
  - Bar Charts for total execution time.
- Statistical analysis (mean, min, max) of algorithm runtimes.

### 3. Numerical Integration
- Calculation of the integral for $f(x) = e^{x^2}$ in the interval $[0, 1]$.
- Implementation and comparison of:
  - **Trapezoidal Rule**
  - **Simpson's Rule**
  - **Gaussian Quadrature (5-point)**

## 📁 Repository Structure

- `problem-1/`: Python scripts and outputs for Interpolation.
- `problem-2/`: Python scripts and charts for Data Analysis.
- `problem-3/`: Numerical integration implementations.
- `report.tex`: LaTeX source file for the final project report.
- `report.pdf`: PDF file for the final project report.

## 🛠 Requirements

To run the scripts, you need Python 3.x and the following libraries:
```bash
pip install numpy pandas matplotlib scipy openpyxl
