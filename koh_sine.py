import turtle

def quadratic_curve(turtle, length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 2.0
        quadratic_curve(turtle, length, depth-1)
        turtle.left(90)
        quadratic_curve(turtle, length, depth-1)
        turtle.right(90)
        quadratic_curve(turtle, length, depth-1)
        turtle.right(90)
        quadratic_curve(turtle, length, depth-1)
        turtle.left(90)
        quadratic_curve(turtle, length, depth-1)

def draw_quadratic_curve():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=1.0, height=1.0)

    curve_turtle = turtle.Turtle()
    curve_turtle.speed(0)
    curve_turtle.color("white")
    curve_turtle.hideturtle()

    screen.tracer(0)

    depth = 6
    length = 60

    curve_turtle.penup()
    curve_turtle.goto(-length*2, 0)
    curve_turtle.pendown()

    quadratic_curve(curve_turtle, length, depth)

    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    draw_quadratic_curve()
