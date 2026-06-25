# Session 3: Traffic light (using if / elif)
import turtle

t = turtle.Turtle()
t.speed(5)
color = "red"          # try "yellow" or "green"
t.penup()

if color == "red":
    t.color("red")
elif color == "yellow":
    t.color("yellow")
elif color == "green":
    t.color("green")

t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

turtle.done()
