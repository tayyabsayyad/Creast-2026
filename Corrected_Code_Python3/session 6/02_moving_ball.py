# Session 6: A moving ball (mini project 1)
import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("green")
screen.tracer(0)              # turn off auto-animation; we update manually

t = turtle.Turtle()
t.color("orange")
t.speed(0)
t.width(2)
t.hideturtle()
t.penup()
t.goto(-250, 0)
t.pendown()

while True:
    t.clear()                 # erase the previous ball
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(20)              # draw the ball
    t.end_fill()
    screen.update()
    t.forward(1)              # move forward a little
    if t.xcor() > 300:        # off the right edge? jump back to the left
        t.goto(-250, 0)
