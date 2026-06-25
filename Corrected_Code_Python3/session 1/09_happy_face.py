# Session 1: Make a happy face
import turtle

t = turtle.Turtle()

# Face
t.circle(80)

# Eyes
t.penup()
t.goto(-30, 100)
t.pendown()
t.dot(15)

t.penup()
t.goto(30, 100)
t.pendown()
t.dot(15)

# Smile
t.penup()
t.goto(-40, 60)
t.pendown()
t.setheading(-60)
t.circle(50, 120)

turtle.done()
