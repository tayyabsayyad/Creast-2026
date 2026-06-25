# Session 3: An interesting pattern (try changing 175 to other numbers)
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.speed(10)              # 1:slowest 3:slow 5:normal 10:fast 0:fastest
for x in range(100):
    t.forward(200)
    t.left(175)

turtle.done()
