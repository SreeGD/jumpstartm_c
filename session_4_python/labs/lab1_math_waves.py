# Lab 1 — Math Waves
# Session 4: Python Basics + Matplotlib
#
# Concepts: imports, variables, numpy arrays, plotting
# Run: python lab1_math_waves.py

import numpy as np
import matplotlib.pyplot as plt

# ─────────────────────────────────────────
# PART 1: Python as a calculator
# ─────────────────────────────────────────

print("=== Python as a Calculator ===")
print(2 ** 10)          # 2 to the power of 10
print(17 % 5)           # modulo (remainder) — Student knows this from ciphers!
print(round(3.14159, 2))
print(abs(-42))

# Math functions
print(np.sqrt(144))     # square root
print(np.pi)            # π
print(np.e)             # Euler's number


# ─────────────────────────────────────────
# PART 2: Plot sin and cos waves
# ─────────────────────────────────────────
# np.linspace(start, stop, num_points) — creates evenly spaced numbers
# Like the x-axis of a graph

x = np.linspace(0, 4 * np.pi, 500)   # 0 to 4π, 500 points

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y_sin, color='#e94560', linewidth=2, label='sin(x)')
plt.plot(x, y_cos, color='#00d4aa', linewidth=2, label='cos(x)')

plt.axhline(0, color='white', linewidth=0.5)  # x-axis
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.title('Sine and Cosine Waves — Same Functions from Class 12')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────
# PART 3: Plot a quadratic — like JEE prep
# ─────────────────────────────────────────

x = np.linspace(-10, 10, 400)
y = x**2 - 5*x + 6      # same as: y = x² - 5x + 6

# Find roots (where y = 0)
# By factoring: (x-2)(x-3) = 0, so roots are x=2 and x=3
roots_x = [2, 3]
roots_y = [0, 0]

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='#e94560', linewidth=2, label='y = x² - 5x + 6')
plt.scatter(roots_x, roots_y, color='#00d4aa', s=100, zorder=5, label='Roots (2, 3)')
plt.axhline(0, color='white', linewidth=0.5)
plt.axvline(0, color='white', linewidth=0.5)
plt.ylim(-5, 30)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Function — Find the Roots Visually')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("Roots of x² - 5x + 6 are x=2 and x=3")
print("Verify:", (2**2 - 5*2 + 6), (3**2 - 5*3 + 6))


# ─────────────────────────────────────────
# CHALLENGE
# ─────────────────────────────────────────
# 1. Plot tan(x) — what happens near π/2? Why?
# 2. Plot y = x³ - 3x on the same axes as y = x² - 5x + 6
# 3. Find and plot the derivative of sin(x) — what is it?
#    Verify visually that the derivative of sin is cos.
