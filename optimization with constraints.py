from scipy.optimize import minimize


# Define the objective function
def objective_function(vars):
    x, y = vars
    return (x - 2) ** 2 + (y - 4) ** 2


# Define the constraint function
def constraint(vars):
    x, y = vars
    return x + y - 5


# Initial guess for the variables
initial_guess = [0, 0]

# Define the bounds for x and y
bounds = [(None, None), (None, None)]

# Define the constraint
constraint_definition = {"type": "eq", "fun": constraint}

# Minimize the objective function with the constraint
result = minimize(
    objective_function, initial_guess, bounds=bounds, constraints=constraint_definition
)

# Extract the optimal values
x_optimal, y_optimal = result.x

# Print the result
print("Optimal value of x:", x_optimal)
print("Optimal value of y:", y_optimal)
print("Minimum value of f(x, y):", result.fun)
