import turtle

def dragon_curve(turtle, length, depth, sign=1):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= (2 ** 0.5)
        turtle.left(45 * sign)
        dragon_curve(turtle, length, depth-1, 1)
        turtle.right(90 * sign)
        dragon_curve(turtle, length, depth-1, -1)
        turtle.left(45 * sign)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=1.0, height=1.0)

    dragon_turtle = turtle.Turtle()
    dragon_turtle.speed(0)
    dragon_turtle.color("white")
    dragon_turtle.hideturtle()  

    screen.tracer(0)

    depth = 14 
    length = 600

    
    dragon_turtle.penup()
    dragon_turtle.goto(-length / 2, 0)
    dragon_turtle.pendown()

    dragon_curve(dragon_turtle, length, depth)

    screen.update()  
    screen.mainloop()

if __name__ == "__main__":
    main()
