import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції

def f(x):
    return x**2

a, b = 0, 2  # Межі інтегрування

# Метод Монте-Карло
N = 10000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

under_curve = y_rand <= f(x_rand)
integral_monte_carlo = (b - a) * f(b) * np.sum(under_curve) / N

# Аналітичний розрахунок інтегралу
result_quad, error = spi.quad(f, a, b)

# Візуалізація
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.scatter(x_rand, y_rand, c=under_curve, cmap='coolwarm', s=1, alpha=0.3)
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Метод Монте-Карло: {integral_monte_carlo:.6f}, Quad: {result_quad:.6f}')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
plt.grid()
plt.show()

# Висновки
print(f"Метод Монте-Карло: {integral_monte_carlo:.6f}")
print(f"Аналітичний інтеграл (quad): {result_quad:.6f}")
print(f"Абсолютна помилка: {abs(integral_monte_carlo - result_quad):.6f}")