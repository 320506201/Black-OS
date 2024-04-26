import turtle

t = turtle.Turtle()

t.color("red")
t.pencolor("orange")
t.speed(0)

t.penup()
t.pendown()

for i in range (60):
    t.circle(150)
    t.right(6)

turtle.done()