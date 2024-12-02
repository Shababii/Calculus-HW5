import math

x0 = 0.15

x_newton = x0
for _ in range(9):
    x_newton -= (8 * x_newton**3 - 3 * x_newton**2 + 1) / (24 * x_newton**2 - 6 * x_newton)

x_modified_newton = x0
for _ in range(9):
    x_modified_newton -= 2 * (8 * x_modified_newton**3 - 3 * x_modified_newton**2 + 1) / (24 * x_modified_newton**2 - 6 * x_modified_newton)

print(f"Part c: Newton's method x9: {x_newton}")
print(f"Part c: Modified Newton's method x9: {x_modified_newton}")


