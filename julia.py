import pygame
import numpy as np

# Параметры экрана
width, height = 800, 800

# Параметры множества Жюлиа́
zoom = 1
moveX, moveY = 0.0, 0.0
max_iter = 255

# Константа c для множества Жюлиа́
cX, cY = -0.7, 0.27015

def julia_set(width, height, zoom, moveX, moveY, cX, cY, max_iter):
    julia = np.zeros((width, height, 3), dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + moveX
            zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + moveY
            i = max_iter
            while zx * zx + zy * zy < 4 and i > 1:
                tmp = zx * zx - zy * zy + cX
                zy, zx = 2.0 * zx * zy + cY, tmp
                i -= 1
            julia[x, y] = (i << 21) + (i << 10) + i * 8
    return julia

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Множество Жюлиа́")

# Создание множества Жюлиа́
julia = julia_set(width, height, zoom, moveX, moveY, cX, cY, max_iter)
julia_surface = pygame.surfarray.make_surface(julia)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отображение множества Жюлиа́
    screen.blit(julia_surface, (0, 0))
    pygame.display.flip()

pygame.quit()
