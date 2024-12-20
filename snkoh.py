import turtle

def koch_curve(turtle, length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_curve(turtle, length, depth-1)
        turtle.left(90)
        koch_curve(turtle, length, depth-1)
        turtle.right(90)
        koch_curve(turtle, length, depth-1)
        turtle.right(90)
        koch_curve(turtle, length, depth-1)
        turtle.left(90)
        koch_curve(turtle, length, depth-1)

def draw_koch():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=1.0, height=1.0)

    koch_turtle = turtle.Turtle()
    koch_turtle.speed(0)
    koch_turtle.color("white")
    koch_turtle.hideturtle()

    screen.tracer(0)

    depth = 6
    length = 600

    koch_turtle.penup()
    koch_turtle.goto(-length / 2, 0)
    koch_turtle.pendown()

    koch_curve(koch_turtle, length, depth)

    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    draw_koch()
