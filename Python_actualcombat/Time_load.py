import turtle
import time

T = turtle.Turtle()
T.pensize(5)
T.pencolor("red")
T.speed(0)
a = -100

def draw_circle():
    global a
    while True:
        while a != 100:
            T.penup()
            T.goto(a,-100)
            T.pendown()
            T.circle(100)
            T.clear()
            a +=1
            time.sleep(0.05)
        a =-100

draw_circle()