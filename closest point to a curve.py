import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


# Distance function
def objective_function(vars, point):
    x, y = vars
    return (x - point[0]) ** 2 + (y - point[1]) ** 2


# curve function
def constraint(vars):
    x, y = vars
    return x**2 + 4 * y - 25


# Initial guess for the variables
initial_guess = [10, 0]

# Define the bounds for x and y
bounds = [(None, None), (None, None)]

# Define the constraint
constraint_definition = {"type": "eq", "fun": constraint}


def get_result(point):

    # Minimize the objective function with the constraint
    result = minimize(
        objective_function,
        initial_guess,
        args=(point,),
        bounds=bounds,
        constraints=constraint_definition,
    )

    # Extract the optimal values
    x_optimal, y_optimal = result.x

    # Print the result
    print("Closest point:", (x_optimal, y_optimal))
    print("Minimum distance:", np.sqrt(result.fun))

    # Plotting the contour of the constraint function
    X = np.linspace(-10, 10, 400)
    Y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(X, Y)
    Z = constraint([X, Y])  # Directly access the constraint function
    plt.contour(X, Y, Z, levels=[0], colors="r")

    # Plotting the two points
    plt.plot(point[0], point[1], "go", label="observer point")
    plt.plot(x_optimal, y_optimal, "bo", label="Closest point")

    # Plotting the dotted line between the points
    plt.plot([point[0], x_optimal], [point[1], y_optimal], "k--", label="Dotted Line")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot of curve and Points")
    plt.axis("equal")
    plt.legend()
    plt.grid(True)
    plt.show()


point = (1, -5)
get_result(point)
