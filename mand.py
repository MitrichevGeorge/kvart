import pygame
import numpy as np

# Настройка параметров окна
width, height = 1100, 800
max_iter = 256

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Фрактал Мандельброта")

# Определение цветов
colors = [pygame.Color(0, 0, 0)]
for i in range(1, max_iter):
    color = pygame.Color(0, 0, 0)
    color.hsva = (i % 256, 100, 100)
    colors.append(color)

# Функция для вычисления фрактала Мандельброта
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Главная функция для рисования фрактала
def draw_mandelbrot():
    for x in range(width):
        for y in range(height):
            c = complex(-2 + (x / width) * 3, -1.5 + (y / height) * 3)
            m = mandelbrot(c, max_iter)
            if m >= max_iter:
                m = max_iter - 1
            color = colors[m]
            screen.set_at((x, y), color)
    pygame.display.update()

# Основной цикл программы
running = True
draw_mandelbrot()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
