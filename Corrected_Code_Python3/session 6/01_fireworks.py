# Session 6: Fireworks animation
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

t.speed(0)
t.hideturtle()

colors = ["red", "yellow", "blue", "green", "orange", "pink", "white"]

for f in range(8):                       # 8 fireworks
    x = random.randint(-200, 200)
    y = random.randint(-150, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(20):                  # 20 spark lines per firework
        t.color(random.choice(colors))
        t.setheading(random.randint(0, 360))
        t.forward(50)
        t.backward(50)

screen.done()
