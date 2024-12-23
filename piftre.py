import turtle

def draw_pythagoras_tree(t, length, depth):
    if depth == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)
    t.left(45)
    draw_pythagoras_tree(t, length / 2**0.5, depth - 1)
    t.right(90)
    draw_pythagoras_tree(t, length / 2**0.5, depth - 1)
    t.left(45)
    t.backward(length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("white")
    t.left(90)

    depth = 10
    length = 100

    draw_pythagoras_tree(t, length, depth)
    screen.update()

    screen.exitonclick()

if __name__ == "__main__":
    main()
