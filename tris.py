import turtle

def trisection_triangle_koch(t, order, size):
    """
    Функция для рисования трисектрис триангулярной кривой Коха.
    
    :param t: объект черепашки
    :param order: порядок рекурсии
    :param size: длина линии
    """
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        trisection_triangle_koch(t, order - 1, size)
        t.left(60)
        trisection_triangle_koch(t, order - 1, size)
        t.right(120)
        trisection_triangle_koch(t, order - 1, size)
        t.left(60)
        trisection_triangle_koch(t, order - 1, size)

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")  # черный фон
screen.setup(width=1.0, height=1.0)  # окно на весь экран
screen.tracer(0)  # моментальная отрисовка

# Настройка черепашки
t = turtle.Turtle()
t.speed(0)  # максимальная скорость черепашки
t.color("white")  # цвет черепашки
t.penup()
t.goto(-300, 0)
t.pendown()

# Параметры трисектрис триангулярной кривой Коха
order = 6  # порядок рекурсии
size = 900  # длина линии

# Рисование трисектрис триангулярной кривой Коха
trisection_triangle_koch(t, order, size)

# Обновление экрана для отображения всех рисунков
screen.update()

# Завершение рисования
turtle.done()
