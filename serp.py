import turtle

def sierpinski_triangle(turtle, depth, length):
    if depth == 0:
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        length /= 2
        sierpinski_triangle(turtle, depth-1, length)
        turtle.forward(length)
        sierpinski_triangle(turtle, depth-1, length)
        turtle.backward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.right(60)
        sierpinski_triangle(turtle, depth-1, length)
        turtle.left(60)
        turtle.backward(length)
        turtle.right(60)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=1.0, height=1.0)

    tri_turtle = turtle.Turtle()
    tri_turtle.speed(0)
    tri_turtle.color("white")
    tri_turtle.hideturtle()

    screen.tracer(0)
    depth = 7
    length = 600
    
    tri_turtle.penup()
    tri_turtle.goto(-length/2, -length/2)
    tri_turtle.pendown()

    sierpinski_triangle(tri_turtle, depth, length)

    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    main()
