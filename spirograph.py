from turtle import Turtle,Screen
import random

tk = Turtle()
screen = Screen()

screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g= random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


tk.speed("fastest")
def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tk.color(random_color())
        tk.circle(100)
        
        tk.setheading(tk.heading() +size_of_gap)


spirograph(5)
screen.exitonclick()

