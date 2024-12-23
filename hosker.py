import turtle

def gosper_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
        return

    length /= 3
    gosper_curve(t, length, depth - 1)
    t.left(60)
    gosper_curve(t, length, depth - 1)
    t.right(120)
    gosper_curve(t, length, depth - 1)
    gosper_curve(t, length, depth - 1)
    t.right(60)
    gosper_curve(t, length, depth - 1)
    t.left(120)
    gosper_curve(t, length, depth - 1)
    t.left(60)
    gosper_curve(t, length, depth - 1)

def main():
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    screen.bgcolor("black")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("white")

    depth = 5
    length = 1200

    t.penup()
    t.goto(-1, 100)
    t.pendown()

    gosper_curve(t, length, depth)
    screen.update()

    screen.exitonclick()

if __name__ == "__main__":
    main()
