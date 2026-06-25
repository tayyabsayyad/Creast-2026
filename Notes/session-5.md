# 🗺️ Session 5 — The Turtle Map, Functions & Animation

> ⬅️ [Session 4](session-4.md) &nbsp;|&nbsp; 🏠 [Home](README.md) &nbsp;|&nbsp; Next ➡️ [Session 6: Fireworks & Final Project](session-6.md)
>
> ⏱️ **Duration:** 3 hours &nbsp;•&nbsp; 🎚️ **Level:** Intermediate &nbsp;•&nbsp; 💻 **Lots of hands-on!**

### 🎯 Learning objectives
- [ ] Use the **coordinate system** (`goto`, where (0,0) is)
- [ ] Control the **screen**: size, background, title
- [ ] **Write your own commands** with functions (`def`) — the big new idea! 🛠️
- [ ] Pass **parameters** to a function to make it flexible
- [ ] Make a simple **spinning animation** and add **text** to a drawing

### 🗓️ 3-Hour Plan
| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Musical chairs / coordinate guessing game |
| 0:15–0:50 | 📖 Coordinates + screen control |
| 0:50–1:25 | 💻 **Lab A:** Olympic rings + square animation |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 📖 **Functions (`def`)** + 💻 **Lab B** |
| 2:10–2:45 | 🏆 Challenge: build a House 🏠 |
| 2:45–3:00 | 📒 Recap + the H-O-P-E mini-test |

---

## 🔔 Warm-up (15 min)
Play a quick game, then a **coordinate guessing** activity: draw a big `+` on the board
with (0,0) in the middle. Call out points like `(100, 100)` and have students point to
where on the board the turtle would go. 🗺️

---

## 🗺️ Part 1 — The Turtle Map & Screen (Concept Block A)

The turtle screen is a giant map. **The middle is `(0, 0)`.**

```
                 +y (up)
                  ↑
                  |
   (-x) ←---------+---------→ +x (right)
        left      | (0,0)    right
                  ↓
                 -y (down)
```
- Right → x **bigger** (+) • Left → x **smaller** (−)
- Up → y **bigger** (+) • Down → y **smaller** (−)

`t.goto(100, 100)` jumps to the top-right; `t.goto(-100, -100)` → bottom-left.

🔮 Where is `t.goto(0, -150)`? <details><summary>👉</summary>Straight **down** from the centre. (x stays 0, y is negative) ⬇️</details>

### Controlling the whole window
```python
screen = turtle.Screen()
screen.setup(500, 500)        # window size in pixels
screen.bgcolor("lightblue")   # background colour
screen.title("My Art")        # window title bar
```

> 🟦 **Pixels:** the screen is made of tiny coloured dots called **pixels** ("picture
> elements"). `setup(500, 500)` means 500 pixels wide and tall.

### Two more handy commands
- `t.write("Hello", font=("Arial", 20, "normal"))` — write **text**
- `t.hideturtle()` (or `t.ht()`) — make the turtle **vanish** so art looks clean

---

## 💻 Lab A — Place things by coordinate (35 min)

**A1. Olympic rings** 🥇 (each ring at its own `goto`):
```python
import turtle
t = turtle.Turtle()
t.pensize(6)
t.color("blue");  t.penup(); t.goto(-100, -25); t.pendown(); t.circle(51)
t.color("black"); t.penup(); t.goto(10, -25);   t.pendown(); t.circle(51)
t.color("red");   t.penup(); t.goto(120, -25);  t.pendown(); t.circle(51)
t.color("yellow"); t.penup(); t.goto(-40, -80); t.pendown(); t.circle(51)
t.color("green");  t.penup(); t.goto(70, -80);  t.pendown(); t.circle(51)
turtle.done()
```

**A2. "My Square Animation" with a title + spin:**
```python
import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(400, 500)
screen.bgcolor("yellow")
t.pencolor("dark blue"); t.pensize(6); t.shape("turtle")

for i in range(4):            # the square
    t.forward(120)
    t.right(90)

t.penup(); t.setpos(-100, 90)
t.write("My Square Animation", font=("Times New Roman", 20, "normal"))
t.hideturtle()
turtle.done()
```

**A3. Spinning turtle** 🌀 (a taste of animation):
```python
import turtle
screen = turtle.Screen()
screen.bgcolor("pink")
t = turtle.Turtle()
t.shape("turtle"); t.color("blue")
for i in range(200):
    t.right(10)               # spin 10° at a time
turtle.done()
```

**✅ Checkpoint:** rings drawn and everyone can predict where a `goto` lands.

---

## ☕ Break (10 min)

---

## 🛠️ Part 2 — Functions: make your OWN commands! (Concept Block B)

So far we've used commands like `t.forward()` and `t.circle()`. **Now we build our own!**

A **function** is a reusable command you define once and use many times.

```python
def say_hello():            # define a command called say_hello
    print("Hello!")
    print("Welcome 🎉")

say_hello()                 # CALL it — runs the two lines
say_hello()                 # call again — runs them again
```
> 🔑 `def name():` defines it. The **indented** lines are what it does. Nothing happens
> until you **call** it with `name()`.

### Parameters — make a function flexible
A **parameter** is an input you hand to your function:
```python
import turtle
t = turtle.Turtle()

def draw_square(size):      # 'size' is a parameter
    for i in range(4):
        t.forward(size)
        t.left(90)

draw_square(50)             # small square
t.penup(); t.forward(120); t.pendown()
draw_square(100)            # big square — same command, different size!
turtle.done()
```
> 🧠 **Why functions are awesome:** write the square logic **once**, reuse it forever.
> This is the grown-up version of the DRY rule. 🌟

---

## 💻 Lab B — Function practice (part of Block B)

**B1. A reusable star stamp** ⭐ (we'll reuse this in Session 6!):
```python
import turtle
t = turtle.Turtle()

def draw_star(x, y, size):
    t.penup(); t.goto(x, y); t.pendown()
    t.color("gold")
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

draw_star(-100, 0, 60)      # stamp a star here
draw_star(100, 50, 40)      # and another, smaller, there!
turtle.done()
```

**B2. Many polygons with one function:**
```python
import turtle
t = turtle.Turtle()

def polygon(sides, length):
    for i in range(sides):
        t.forward(length)
        t.left(360 / sides)

polygon(3, 80)              # triangle
polygon(6, 50)              # hexagon
turtle.done()
```

🎯 *Make it yours:* add a `color` parameter to `polygon` so each one is a different colour.

---

## 🏆 Challenge (35 min) — Build a House 🏠

A house = a **triangle roof** + a **square wall** + a **door**.
```python
import turtle
t = turtle.Turtle()

# 🔺 Roof: brown triangle, black outline
t.color("black", "brown")
t.begin_fill()
for i in range(3):
    t.forward(-200)
    t.right(120)
t.end_fill()

# ⬜ Wall: grey square (shares the roof base as its top side → only 3 more sides)
t.color("black", "gray")
t.begin_fill()
for i in range(3):
    t.right(90)
    t.forward(200)
t.end_fill()

# 🚪 Door
t.color("black"); t.pensize(4)
t.penup(); t.goto(-120, -100); t.pendown()
t.right(90); t.forward(50)
t.right(90); t.forward(100)
t.penup(); t.goto(-120, -100); t.pendown()
t.forward(100)
turtle.done()
```
🎯 *Extensions:* add a **window** (small square), a **sun** in the corner, or write your
name above the house with `t.write`.

---

## ✍️ Mini-test (if time) — Write H · O · P · E
Each letter in a **new tab**, 10 marks each. Letter `H`:
```python
import turtle
t = turtle.Turtle()
t.shape("turtle"); t.pensize(10); t.pencolor("red")
t.penup(); t.goto(-30, 50); t.pendown()
t.right(90); t.forward(200)
t.goto(-30, -50); t.goto(50, -50); t.goto(50, 50); t.goto(50, -140)
turtle.done()
```
> Full `O`, `P`, `E` solutions are in [`../Corrected_Code_Python3/session 5/`](../Corrected_Code_Python3/).

---

## 🐞 Debugging Corner
| Oops | Fix |
|---|---|
| defined a function but nothing happens | you forgot to **call** it: `my_func()` |
| `draw_square()` error: missing argument | pass the value: `draw_square(50)` |
| lines run that shouldn't | check what's indented **inside** `def` vs outside |
| shape drawn at wrong spot | `penup()` before `goto`, `pendown()` after |

---

## 📒 Wrap-up (5 min)
- The screen is a **map**: middle `(0,0)`, right/up positive
- `screen.setup/bgcolor/title` control the window; pixels are the dots
- **Functions (`def`)** let you build your **own commands** and reuse them
- **Parameters** make functions flexible (`draw_square(size)`)
- `t.write()` adds text; `t.hideturtle()` cleans up

## 🏠 Take-home Assignment 5
1. Write a function `draw_triangle(size)` and use it to draw 3 triangles of different sizes.
2. Use your `draw_star` function to stamp **4 stars** at different spots.
3. Draw a house and add at least **one window**.
4. **Bonus:** write a function `draw_flower()` that draws a circle of petals (loop + circle).

<details><summary>🔑 Facilitator answer key</summary>

```python
# Q1
import turtle
t = turtle.Turtle()
def draw_triangle(size):
    for i in range(3):
        t.forward(size)
        t.left(120)
draw_triangle(50)
t.penup(); t.forward(100); t.pendown()
draw_triangle(100)
turtle.done()

# Q4 simple flower
import turtle
t = turtle.Turtle()
def draw_flower():
    for i in range(12):
        t.circle(50)
        t.left(30)
draw_flower()
turtle.done()
```
</details>

<details><summary>🧑‍🏫 Facilitator notes</summary>

- **Functions are the leap of the course.** Use the analogy: "a function is like teaching
  the turtle a *new word*. Once it knows `draw_square`, you just say it."
- Stress **define vs call** — many will define and wonder why nothing draws.
- The **star function** is deliberately the same one used in Session 6's final test — point
  that out so they see why functions matter.
- **Fast finishers:** add a `color` parameter; draw a row of houses with a loop + function.
- **Support:** B1 (one function, call it twice) is the must-reach goal.
</details>

➡️ **Next up:** [Session 6 — Fireworks, Moving Ball & Final Project](session-6.md)
