# Session 5: Five rings, drawn with coordinates
import turtle

t = turtle.Turtle()
t.pensize(6)

# top row
t.color("blue")
t.penup(); t.goto(-100, -25); t.pendown(); t.circle(51)

t.color("black")
t.penup(); t.goto(10, -25); t.pendown(); t.circle(51)

t.color("red")
t.penup(); t.goto(120, -25); t.pendown(); t.circle(51)

# bottom row
t.color("yellow")
t.penup(); t.goto(-40, -80); t.pendown(); t.circle(51)

t.color("green")
t.penup(); t.goto(70, -80); t.pendown(); t.circle(51)

turtle.done()
