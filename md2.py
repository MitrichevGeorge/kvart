import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize

def mandelbrot(c, max_iter):
    """
    Функция для вычисления значения множества Мандельброта.
    c: Комплексное число.
    max_iter: Максимальное количество итераций.
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def create_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    """
    Функция для создания изображения множества Мандельброта.
    width: Ширина изображения.
    height: Высота изображения.
    x_min, x_max: Диапазон значений по оси x.
    y_min, y_max: Диапазон значений по оси y.
    max_iter: Максимальное количество итераций.
    """
    image = np.zeros((height, width))
    for row in range(height):
        for col in range(width):
            x = x_min + (x_max - x_min) * col / (width - 1)
            y = y_min + (y_max - y_min) * row / (height - 1)
            c = complex(x, y)
            image[row, col] = mandelbrot(c, max_iter)
    return image

# Параметры изображения
width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 256

# Создание множества Мандельброта
mandelbrot_image = create_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

# Создание пользовательской цветовой карты
colors = [(0, 0, 0.5), (1, 1, 1), (1, 0.5, 0), (0, 0, 0)]
cmap = LinearSegmentedColormap.from_list('custom_mandelbrot', colors, N=256)

# Нормализация для увеличения контраста
norm = Normalize(vmin=0, vmax=max_iter)

# Отображение изображения
plt.imshow(mandelbrot_image, extent=(x_min, x_max, y_min, y_max), cmap=cmap, norm=norm)
plt.colorbar()
plt.title("Множество Мандельброта")
plt.show()