# Session 5: A house (roof triangle + wall square + door)
import turtle

t = turtle.Turtle()

# Roof: a brown triangle with black outline
t.color("black", "brown")
t.begin_fill()
for i in range(3):
    t.forward(-200)
    t.right(120)
t.end_fill()

# Wall: a grey square with black outline (shares the roof base as its top side)
t.color("black", "gray")
t.begin_fill()
for i in range(3):
    t.right(90)
    t.forward(200)
t.end_fill()

# Door
t.color("black")
t.pensize(4)
t.penup()
t.goto(-120, -100)
t.pendown()
t.right(90)
t.forward(50)        # left side
t.right(90)
t.forward(100)       # top
t.penup()
t.goto(-120, -100)
t.pendown()
t.forward(100)       # right side

turtle.done()
