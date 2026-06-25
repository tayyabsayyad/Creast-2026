# Session 2: Pen commands - move without drawing, then change thickness/colour
import turtle

pen = turtle.Turtle()
pen.speed(3)

# PART 1: a normal-thickness red square
pen.pensize(3)
pen.pencolor("red")
pen.penup()          # lift pen -> no drawing while moving
pen.goto(-100, 0)
pen.pendown()        # lower pen -> start drawing
for i in range(4):
    pen.forward(80)
    pen.left(90)

# PART 2: move without drawing
pen.penup()
pen.goto(100, 0)

# PART 3: a thicker blue square
pen.pensize(8)
pen.pencolor("blue")
pen.pendown()
for i in range(4):
    pen.forward(80)
    pen.left(90)

turtle.done()
