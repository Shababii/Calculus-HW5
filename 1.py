# Given values
N = 100  # Total number of people
q = 0.95  # Probability that any one person tests negative

def average_tests(x):
    return N * (1 - q**x + 1/x)

x_values = [x / 100 for x in range(100, 15001)]  # From 1 to 150 in steps of 0.01
t_values = [average_tests(x) for x in x_values]

min_index = t_values.index(min(t_values))
optimal_x = x_values[min_index]
min_tests = t_values[min_index]

print(f"Optimal group size (x): {optimal_x:.2f}")
print(f"Minimum average number of tests: {min_tests:.2f}")




