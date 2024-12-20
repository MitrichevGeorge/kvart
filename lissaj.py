import turtle
import math

def draw_lissajous(a, b, delta, num_points):
    turtle.penup()
    for i in range(num_points + 1):
        t = 2 * math.pi * i / num_points
        x = 200 * math.sin(a * t + delta)
        y = 200 * math.sin(b * t)
        if i == 0:
            turtle.goto(x, y)
            turtle.pendown()
        else:
            turtle.goto(x, y)

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
turtle.color("white")
screen.tracer(0)

draw_lissajous(3, 2, math.pi / 2, 1000)

screen.update()
turtle.done()