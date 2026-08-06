"""Monte Carlo integration of exp(-x**2) on the interval [-1, 1]."""

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

NUM_SAMPLES = 100_000
RANDOM_SEED = 42


def integration_function(x: np.ndarray | float) -> np.ndarray | float:
    """Return the value of the function selected for integration."""
    return np.exp(-(x**2))


def monte_carlo_simulation(a, b, num_experiments, num_samples=NUM_SAMPLES) -> float:
    """Estimate the area under the function using hit-or-miss sampling.

    The function generates random points inside the rectangle bounded by
    ``x = a``, ``x = b``, ``y = 0``, and ``y = 1``. It returns the average
    area estimate across all requested experiments.
    """
    rng = np.random.default_rng(RANDOM_SEED)
    y_min = 0
    y_max = 1

    total_area = 0

    for _ in range(num_experiments):
        points = rng.uniform(
            [a, y_min],
            [b, y_max],
            size=(num_samples, 2),
        )

        x_values = points[:, 0]
        y_values = points[:, 1]

        inside = y_values <= integration_function(x_values)
        area = (b - a) * (y_max - y_min) * np.mean(inside)

        total_area += area

    return total_area / num_experiments


def quad_integral(a: float, b: float) -> tuple[float, float]:
    """Return the integral and estimated absolute error from SciPy quad."""
    result, error = spi.quad(integration_function, a, b)
    return result, error


def draw_diagram(a: float, b: float) -> None:
    """Draw the function and shade the area being integrated."""
    x = np.linspace(a - 0.1, b + 0.1, 400)
    y = integration_function(x)

    _, ax = plt.subplots()
    ax.plot(x, y, "r", linewidth=2, label="f(x) = exp(-x**2)")

    ix = np.linspace(a, b)
    iy = integration_function(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3, label="Area under the curve")

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([min(y) - 0.1, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Integration diagram: f(x) = exp(-x**2) from {str(a)} to {str(b)}")
    ax.legend()
    ax.grid()
    plt.show()


def main() -> None:
    """Calculate the integral, print the comparison, and display the graph."""
    a = -1
    b = 1

    monte_carlo_result = monte_carlo_simulation(a, b, 10)
    quad_result, quad_error = quad_integral(a, b)
    absolute_error = abs(monte_carlo_result - quad_result)

    print(f"Function: exp(-x**2), interval: [{a}, {b}]")
    print(f"Monte Carlo estimate: {monte_carlo_result:.10f}")
    print(f"SciPy quad result: {quad_result:.10f}")
    print(f"SciPy quad estimated error: {quad_error:.10e}")
    print(f"Absolute difference: {absolute_error:.10f}")

    draw_diagram(a, b)


if __name__ == "__main__":
    main()
