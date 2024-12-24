import turtle

def cesaro_curve(t, order, size, angle):
    """
    Функция для рисования фрактала Цезаря.
    
    :param t: объект черепашки
    :param order: порядок рекурсии
    :param size: длина линии
    :param angle: угол поворота
    """
    if order == 0:
        t.forward(size)
    else:
        cesaro_curve(t, order - 1, size / 2, angle)
        t.left(angle)
        cesaro_curve(t, order - 1, size / 2, angle)
        t.right(2 * angle)
        cesaro_curve(t, order - 1, size / 2, angle)
        t.left(angle)
        cesaro_curve(t, order - 1, size / 2, angle)

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

# Параметры фрактала Цезаря
order = 5  # порядок рекурсии
size = 600  # длина линии
angle = 85  # угол поворота

# Рисование фрактала Цезаря
cesaro_curve(t, order, size, angle)

# Обновление экрана для отображения всех рисунков
screen.update()

# Завершение рисования
turtle.done()
