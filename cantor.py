import pygame

# Параметры экрана
width, height = 800, 600

# Параметры множества Кантора
depth = 6
initial_length = 600
initial_position = 50
gap = 20

def draw_cantor_set(screen, x, y, length, depth):
    if depth == 0:
        return
    pygame.draw.line(screen, (255, 255, 255), (x, y), (x + length, y), 5)
    y += gap
    draw_cantor_set(screen, x, y, length / 3, depth - 1)
    draw_cantor_set(screen, x + 2 * length / 3, y, length / 3, depth - 1)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Множество Кантора")
screen.fill((0, 0, 0))

# Рисование множества Кантора
draw_cantor_set(screen, (width - initial_length) / 2, initial_position, initial_length, depth)

# Обновление экрана
pygame.display.flip()

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
