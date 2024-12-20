import turtle

depth = 6
length = 600

def hilbert_curve(t, depth, angle, length):
    if depth == 0:
        return

    t.right(angle)
    hilbert_curve(t, depth - 1, -angle, length)
    t.forward(length)
    t.left(angle)
    hilbert_curve(t, depth - 1, angle, length)
    t.forward(length)
    hilbert_curve(t, depth - 1, angle, length)
    t.left(angle)
    t.forward(length)
    hilbert_curve(t, depth - 1, -angle, length)
    t.right(angle)

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1.0, height=1.0)
screen.tracer(0)

t = turtle.Turtle()
t.color("white")
t.speed(0)
t.penup()
t.goto(-length / 2, length / 2)
t.pendown()
t.hideturtle()

side_length = length / (2 ** depth - 1)
hilbert_curve(t, depth, 90, side_length)

screen.update()
turtle.done()
