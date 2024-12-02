import math

def f(x):
    return math.exp(2 * math.sin(x)) - 2 * x - 1

def f_prime(x):
    return 2 * math.exp(2 * math.sin(x)) * math.cos(x) - 2

x0 = 0.1
iterations = 9

x_newton = x0
for _ in range(iterations):
    x_newton -= f(x_newton) / f_prime(x_newton)

x_modified_newton = x0
for _ in range(iterations):
    x_modified_newton -= 2 * f(x_modified_newton) / f_prime(x_modified_newton)

print("Newton's method result:", x_newton)
print("Modified Newton's method result:", x_modified_newton)


