# Session 5: Spinning effect, screen colour and comments
import turtle

screen = turtle.Screen()
screen.bgcolor("pink")

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
for i in range(200):
    t.right(10)          # rotates the turtle 10 degrees -> spinning effect

turtle.done()
