import turtle

t = turtle.Turtle()

t.color("red")
t.pencolor("orange")
t.shape("turtle")
t.speed(0)

t.penup()
t.goto(100,100)
t.pendown()

t.begin_fill()
for i in range (36):
    for i in range (4):
        t.forward(200)
        t.left(90)
    t.right(10)
t.end_fill()

turtle.done()