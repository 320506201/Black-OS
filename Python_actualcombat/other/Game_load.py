import turtle
import time

T = turtle.Turtle()
T.hideturtle()
T.pensize(5)
T.pencolor("orange")

def game_load(all):
    T.penup()
    T.goto( -200,0)
    T.pendown()
    for i in range(400):
        T.forward(1)
    T.penup()
    T.goto( -60,-200)
    T.pendown()
    T.write("Game is ready!",font=("宋体",15,"normal"))
    time.sleep(2)

game_load(20)
T.clear()
print("hi")
while True:
    a = input()
    if a == "exit":
        quit()
    print(a)