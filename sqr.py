import turtle

def sierpinski_carpet(turtle, depth, length, x, y):
    if depth == 0:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(length)
            turtle.right(90)
        turtle.end_fill()
    else:
        new_length = length / 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                   
                    continue
                sierpinski_carpet(turtle, depth-1, new_length, x + i*new_length, y - j*new_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")  
    screen.setup(width=1.0, height=1.0)

    carpet_turtle = turtle.Turtle()
    carpet_turtle.speed(0)
    carpet_turtle.color("white")
    carpet_turtle.hideturtle()  

    screen.tracer(0)

    depth = 5
    length = 600

   
    x = -length / 2
    y = length / 2

    screen.tracer(2)
    sierpinski_carpet(carpet_turtle, depth, length, x, y)
    screen.update()  
    
    screen.mainloop()

if __name__ == "__main__":
    main()
