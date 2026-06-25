# Session 4: Draw a sun (loop the rays)
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pencolor("orange")
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

for _ in range(18):
    t.right(90)
    t.forward(90)
    t.backward(90)
    t.left(90)
    t.circle(100, 20)

turtle.done()
