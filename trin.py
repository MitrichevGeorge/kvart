import turtle

def draw_triangle(t, vertices):
    """
    Функция для рисования треугольника.
    
    :param t: объект черепашки
    :param vertices: список координат вершин треугольника
    """
    t.penup()
    t.goto(vertices[0][0], vertices[0][1])
    t.pendown()
    t.goto(vertices[1][0], vertices[1][1])
    t.goto(vertices[2][0], vertices[2][1])
    t.goto(vertices[0][0], vertices[0][1])

def get_centroid(vertices):
    """
    Функция для нахождения центра масс треугольника.
    
    :param vertices: список координат вершин треугольника
    :return: координаты центра масс
    """
    x = (vertices[0][0] + vertices[1][0] + vertices[2][0]) / 3
    y = (vertices[0][1] + vertices[1][1] + vertices[2][1]) / 3
    return x, y

def recursive_triangle(t, vertices, order):
    """
    Функция для рекурсивного рисования фрактала треугольника.
    
    :param t: объект черепашки
    :param vertices: список координат вершин треугольника
    :param order: порядок рекурсии
    """
    if order == 0:
        draw_triangle(t, vertices)
    else:
        # Найти центр масс текущего треугольника
        centroid = get_centroid(vertices)
        
        # Разделить треугольник на три новых треугольника
        for i in range(3):
            new_vertices = [vertices[i], vertices[(i+1) % 3], centroid]
            recursive_triangle(t, new_vertices, order - 1)

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")  # черный фон
screen.setup(width=1.0, height=1.0)  # окно на весь экран
screen.tracer(0)  # моментальная отрисовка

# Настройка черепашки
t = turtle.Turtle()
t.speed(0)  # максимальная скорость черепашки
t.color("white")  # цвет черепашки

# Вершины начального треугольника
vertices = [[-200, -100], [0, 200], [200, -100]]

# Параметры фрактала
order = 4  # порядок рекурсии

# Рисование фрактала треугольника
recursive_triangle(t, vertices, order)

# Обновление экрана для отображения всех рисунков
screen.update()

# Завершение рисования
turtle.done()
