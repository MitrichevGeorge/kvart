import turtle

def draw_koch_segment(length, depth):
    if depth == 0:
        turtle.forward(length)
        return
    length /= 3
    draw_koch_segment(length, depth - 1)
    turtle.left(60)
    draw_koch_segment(length, depth - 1)
    turtle.right(120)
    draw_koch_segment(length, depth - 1)
    turtle.left(60)
    draw_koch_segment(length, depth - 1)

def draw_koch_snowflake(length, depth):
    for _ in range(5):
        draw_koch_segment(length, depth)
        turtle.right(72)

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
turtle.color("white")
screen.tracer(0)

turtle.penup()
turtle.goto(-200, 300)
turtle.pendown()

draw_koch_snowflake(300, 4)

screen.update()
turtle.done()