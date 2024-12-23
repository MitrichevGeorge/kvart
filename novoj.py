import pygame
import numpy as np

# Параметры экрана
width, height = 800, 800

# Параметры множества Новой
zoom = 1
moveX, moveY = 0.0, 0.0
max_iter = 255

def nova_set(width, height, zoom, moveX, moveY, max_iter):
    nova = np.zeros((width, height, 3), dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + moveX
            zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + moveY
            i = max_iter
            while zx * zx + zy * zy < 4 and i > 1:
                r = zx * zx - zy * zy
                zx, zy = r - 1 / (r * zx - zx * zy * zy), zy - 1 / (r * zy - 2 * zx * zy * zy)
                i -= 1
            nova[x, y] = (i << 21) + (i << 10) + i * 8
    return nova

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Множество Новой")

# Создание множества Новой
nova = nova_set(width, height, zoom, moveX, moveY, max_iter)
nova_surface = pygame.surfarray.make_surface(nova)

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отображение множества Новой
    screen.blit(nova_surface, (0, 0))
    pygame.display.flip()

pygame.quit()
