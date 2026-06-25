# Session 7: Random walk animation
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")

t = turtle.Turtle()
t.color("red")
t.shape("turtle")
t.speed(0)
t.penup()
t.goto(0, 0)
t.pendown()

colors = ["red", "yellow", "blue", "green", "pink", "white"]

while True:
    t.color(random.choice(colors))
    t.setheading(random.randint(0, 360))
    t.forward(random.randint(20, 50))
