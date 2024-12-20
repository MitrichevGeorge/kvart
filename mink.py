import turtle

def minkowski_curve(turtle, length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 4.0
        minkowski_curve(turtle, length, depth-1)
        turtle.left(90)
        minkowski_curve(turtle, length, depth-1)
        turtle.right(90)
        minkowski_curve(turtle, length, depth-1)
        turtle.right(90)
        minkowski_curve(turtle, length, depth-1)
        minkowski_curve(turtle, length, depth-1)
        turtle.left(90)
        minkowski_curve(turtle, length, depth-1)
        turtle.left(90)
        minkowski_curve(turtle, length, depth-1)
        turtle.right(90)
        minkowski_curve(turtle, length, depth-1)

def draw_minkowski():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=1.0, height=1.0)

    minkowski_turtle = turtle.Turtle()
    minkowski_turtle.speed(0)
    minkowski_turtle.color("white")
    minkowski_turtle.hideturtle()

    screen.tracer(0)

    depth = 5
    length = 600

    minkowski_turtle.penup()
    minkowski_turtle.goto(-length / 2, 0)
    minkowski_turtle.pendown()

    minkowski_curve(minkowski_turtle, length, depth)

    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    draw_minkowski()
