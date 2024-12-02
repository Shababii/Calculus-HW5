import math

def f(x):
    return math.exp(2 * math.sin(x)) - 2 * x - 1

def f_prime(x):
    return 2 * math.exp(2 * math.sin(x)) * math.cos(x) - 2

def f_double_prime(x):
    return 4 * math.exp(2 * math.sin(x)) * math.cos(x)**2 - 2 * math.exp(2 * math.sin(x)) * math.sin(x)

print("f(0) =", f(0))
print("f'(0) =", f_prime(0))
print("f''(0) =", f_double_prime(0))
