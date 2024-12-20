import matplotlib.pyplot as plt
import numpy as np

def logistic_map(r, x):
    return r * x * (1 - x)

def draw_logistic_map(r_min, r_max, num_points, num_iterations, last_iterations):
    r_values = np.linspace(r_min, r_max, num_points)
    x = 1e-5 * np.ones(num_points)  # начальные значения

    plt.figure(figsize=(10, 6))
    for _ in range(num_iterations):
        x = logistic_map(r_values, x)
        if _ >= (num_iterations - last_iterations):
            plt.plot(r_values, x, ',k', alpha=0.25)  # рисуем последние итерации

    plt.title("Фрактал Логистической карты")
    plt.xlabel("Параметр роста (r)")
    plt.ylabel("Популяция")
    plt.show()

# Параметры
r_min = 2.5
r_max = 4.0
num_points = 10000
num_iterations = 1000
last_iterations = 100

draw_logistic_map(r_min, r_max, num_points, num_iterations, last_iterations)
