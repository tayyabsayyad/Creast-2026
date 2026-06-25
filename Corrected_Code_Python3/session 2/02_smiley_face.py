# Session 2: Build a smiley face step by step
import turtle

pen = turtle.Turtle()
pen.speed(5)

# Step 1: yellow face
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.pensize(5)
pen.pencolor("black")
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# Step 2: left eye
pen.penup()
pen.goto(-35, 30)
pen.pendown()
pen.pensize(3)
pen.fillcolor("white")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Step 3: right eye
pen.penup()
pen.goto(35, 30)
pen.pendown()
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Step 4: smile (a semi-circle)
pen.penup()
pen.goto(-50, -20)
pen.pendown()
pen.pensize(5)
pen.setheading(-60)
pen.circle(50, 120)

turtle.done()
