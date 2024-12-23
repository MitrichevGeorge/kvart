import pygame
import random

# Параметры экрана
width, height = 800, 800

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Множество Барнсли")
screen.fill((0, 0, 0))

# Функция для рисования множества Барнсли
def draw_barnsley_fern(screen, iterations):
    x, y = 0, 0
    for _ in range(iterations):
        r = random.random()
        if r < 0.01:
            x_new = 0
            y_new = 0.16 * y
        elif r < 0.86:
            x_new = 0.85 * x + 0.04 * y
            y_new = -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x_new = 0.2 * x - 0.26 * y
            y_new = 0.23 * x + 0.22 * y + 1.6
        else:
            x_new = -0.15 * x + 0.28 * y
            y_new = 0.26 * x + 0.24 * y + 0.44
        x, y = x_new, y_new
        
        # Преобразование координат для отображения на экране
        x_disp = int(width / 2 + x * width / 10)
        y_disp = int(height - y * height / 10)
        screen.set_at((x_disp, y_disp), (0, 255, 0))

# Рисование множества Барнсли
draw_barnsley_fern(screen, 100000)

# Обновление экрана
pygame.display.flip()

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
