# Session 6: Final test - full moon sky with stars
import turtle

t = turtle.Turtle()
t.speed(5)
screen = turtle.Screen()
screen.bgcolor("black")

def star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# stars
star(-250, 250, 100)
star(40, 250, 30)
star(40, -50, 60)
star(-140, -50, 30)

# full moon
t.penup()
t.goto(-80, 40)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(40)
t.end_fill()

t.hideturtle()
turtle.done()
