# Session 2: Make a staircase using a loop
import turtle

pen = turtle.Turtle()
pen.pencolor("green")
for i in range(5):
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.right(90)

turtle.done()
