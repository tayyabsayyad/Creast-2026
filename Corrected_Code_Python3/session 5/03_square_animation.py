# Session 5: "My Square Animation" + hiding the turtle
import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(400, 500)
screen.bgcolor("yellow")

t.pencolor("dark blue")
t.pensize(6)
t.shape("turtle")

# draw the square
for i in range(4):
    t.forward(120)
    t.right(90)

# write the title
t.penup()
t.setpos(-100, 90)
t.write("My Square Animation", font=("Times New Roman", 20, "normal"))
t.hideturtle()           # t.ht() also works

turtle.done()
