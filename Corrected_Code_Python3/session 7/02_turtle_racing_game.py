# Session 7: Mini project 2 - Turtle racing game
import turtle
from random import randint

# --- draw the race track ---
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-140, 140)

for j in range(15):
    t.write(j, align="center")
    t.right(90)
    for num in range(8):            # 8 vertical dashes
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
    t.penup()
    t.backward(160)
    t.left(90)
    t.forward(20)

# --- four players ---
plyr1 = turtle.Turtle()
plyr1.color("magenta")
plyr1.shape("turtle")
plyr1.penup()
plyr1.goto(-160, 100)
plyr1.pendown()
for turn in range(10):
    plyr1.right(36)

plyr2 = turtle.Turtle()
plyr2.color("red")
plyr2.shape("turtle")
plyr2.penup()
plyr2.goto(-160, 70)
plyr2.pendown()
for turn in range(10):
    plyr2.left(36)

plyr3 = turtle.Turtle()
plyr3.color("green")
plyr3.shape("turtle")
plyr3.penup()
plyr3.goto(-160, 40)
plyr3.pendown()
for turn in range(10):
    plyr3.left(36)

plyr4 = turtle.Turtle()
plyr4.color("blue")
plyr4.shape("turtle")
plyr4.penup()
plyr4.goto(-160, 10)
plyr4.pendown()
for turn in range(10):
    plyr4.right(36)

# --- the race: everyone moves a random amount ---
for turn in range(100):
    plyr1.forward(randint(1, 5))
    plyr2.forward(randint(1, 5))
    plyr3.forward(randint(1, 5))
    plyr4.forward(randint(1, 5))

turtle.done()
