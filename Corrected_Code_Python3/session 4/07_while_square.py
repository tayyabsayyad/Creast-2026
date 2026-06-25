# Session 4: Draw a square with a while loop
import turtle

t = turtle.Turtle()
steps = 1
while steps <= 4:
    t.forward(100)
    t.right(90)
    steps = steps + 1

turtle.done()
