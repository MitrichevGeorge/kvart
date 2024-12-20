import turtle

def levy_curve(turtle, length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        turtle.left(45)
        levy_curve(turtle, length / (2 ** 0.5), depth - 1)
        turtle.right(90)
        levy_curve(turtle, length / (2 ** 0.5), depth - 1)
        turtle.left(45)

def draw_levy():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=1.0, height=1.0)

    levy_turtle = turtle.Turtle()
    levy_turtle.speed(0)
    levy_turtle.color("white")
    levy_turtle.hideturtle()

    screen.tracer(0)

    depth = 14
    length = 300

    levy_turtle.penup()
    levy_turtle.goto(-length / 2, 0)
    levy_turtle.pendown()

    levy_curve(levy_turtle, length, depth)

    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    draw_levy()
