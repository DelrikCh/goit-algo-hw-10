import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def monte_carlo_integration(a, b, func, num_points):
    """
    Parameters:
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.
        func (function): The function to be integrated.
        num_points (int): Number of random points to generate.

    Returns:
        float: Approximated value of the integral.
    """
    # Generate random points
    x_values = np.random.uniform(a, b, num_points)
    y_values = np.random.uniform(0, func(b), num_points)

    # Count points inside the area under the curve
    points_inside = sum(1 for x, y in zip(
        x_values, y_values) if 0 <= y <= func(x))

    # Calculate the integral approximation
    integral_approximation = (points_inside / num_points) * ((b - a) * func(b))

    return integral_approximation


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Обчислення значень визначених інтегралів
quad_integral, _ = quad(f, a, b)
monte_carlo_integral = monte_carlo_integration(a, b, f, 10**6)
print("Значення аналітичного інтеграла:", quad_integral)
print("Значення інтеграла методом Монте-Карло:", monte_carlo_integral)
print("Похибка:", abs(quad_integral - monte_carlo_integral))


# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
