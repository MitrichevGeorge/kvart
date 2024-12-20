import turtle

def koch_snowflake(turtle, length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(turtle, length, depth-1)
        turtle.left(60)
        koch_snowflake(turtle, length, depth-1)
        turtle.right(120)
        koch_snowflake(turtle, length, depth-1)
        turtle.left(60)
        koch_snowflake(turtle, length, depth-1)

def draw_snowflake():
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    snowflake = turtle.Turtle()
    snowflake.speed(0)
    snowflake.color("white")
    snowflake.hideturtle()
    
    screen.tracer(0)
    
    length = 300 
    depth = 4    
    
    for _ in range(3):
        koch_snowflake(snowflake, length, depth)
        snowflake.right(120)
    
    screen.update()
    
    screen.mainloop()

if __name__ == "__main__":
    draw_snowflake()
