---
marp: true
theme: default
paginate: true
size: 16:9
backgroundColor: #fffdf7
header: '🗺️ Session 5 — Turtle Map, Functions & Animation'
style: |
  section {
    font-size: 26px;
    padding: 50px 60px;
  }
  h1 {
    color: #2e7d32;
    font-size: 48px;
  }
  h2 {
    color: #1565c0;
    font-size: 38px;
  }
  code {
    background: #f3f3f3;
    border-radius: 6px;
  }
  pre {
    background: #9bb835;
    border-radius: 10px;
    font-size: 22px;
  }
  table {
    font-size: 24px;
  }
  section.lead {
    text-align: center;
  }
  section.lead h1 {
    font-size: 60px;
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _header: '' -->

# 🗺️ Session 5
## The Turtle Map, Functions & Animation

⏱️ **3 hours** &nbsp;•&nbsp; 🎚️ **Intermediate** &nbsp;•&nbsp; 💻 **Lots of hands-on!**

---

## 🎯 By the end, you can…

- ✅ Use the **coordinate system** (`goto`, where (0,0) is)
- ✅ Control the **screen**: size, background, title
- ✅ **Write your own commands** with functions (`def`) 🛠️
- ✅ Pass **parameters** to make a function flexible
- ✅ Make a simple **spinning animation** and add **text**

---

## 🗓️ The 3-Hour Plan

| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Coordinate guessing game |
| 0:15–0:50 | 📖 Coordinates + screen control |
| 0:50–1:25 | 💻 **Lab A:** Olympic rings + animation |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 📖 **Functions (`def`)** + 💻 **Lab B** |
| 2:10–2:45 | 🏆 Challenge: build a House 🏠 |
| 2:45–3:00 | 📒 Recap + the H-O-P-E mini-test |

---

## 🗺️ The Turtle Map

The turtle screen is a giant map. **The middle is `(0, 0)`.**

```
                 +y (up)
                  ↑
   (-x) ←---------+---------→ +x (right)
        left      | (0,0)    right
                  ↓
                 -y (down)
```

- Right → x **bigger** (+) • Left → x **smaller** (−)
- Up → y **bigger** (+) • Down → y **smaller** (−)

🔮 Where is `t.goto(0, -150)`? 👉 Straight **down** from the centre. ⬇️

---

## 🖼️ Controlling the whole window

```python
screen = turtle.Screen()
screen.setup(500, 500)        # window size in pixels
screen.bgcolor("lightblue")   # background colour
screen.title("My Art")        # window title bar
```

> 🟦 **Pixels** are tiny coloured dots. `setup(500, 500)` = 500 wide & tall.

Two more handy commands:
- `t.write("Hello", font=("Arial", 20, "normal"))` — write **text**
- `t.hideturtle()` — make the turtle **vanish** for clean art

---

## 💻 Lab A — A1. Olympic rings 🥇

```python
import turtle
t = turtle.Turtle()
t.pensize(6)
t.color("blue");   t.penup(); t.goto(-100, -25); t.pendown(); t.circle(51)
t.color("black");  t.penup(); t.goto(10, -25);   t.pendown(); t.circle(51)
t.color("red");    t.penup(); t.goto(120, -25);  t.pendown(); t.circle(51)
t.color("yellow"); t.penup(); t.goto(-40, -80);  t.pendown(); t.circle(51)
t.color("green");  t.penup(); t.goto(70, -80);   t.pendown(); t.circle(51)
turtle.done()
```

---

## A2. Square animation · A3. Spinning turtle 🌀

```python
import turtle
t = turtle.Turtle(); screen = turtle.Screen()
screen.setup(400, 500); screen.bgcolor("yellow")
t.pencolor("dark blue"); t.pensize(6)
for i in range(4):
    t.forward(120); t.right(90)
t.penup(); t.setpos(-100, 90)
t.write("My Square Animation", font=("Times New Roman", 20, "normal"))
t.hideturtle(); turtle.done()
```

```python
for i in range(200):     # A3 — spin 10° at a time
    t.right(10)
```
> ✅ **Checkpoint:** rings drawn; everyone can predict where a `goto` lands.

---

<!-- _class: lead -->

# ☕ Break (10 min)

---

## 🛠️ Functions: make your OWN commands!

A **function** is a reusable command you define once and use many times.

```python
def say_hello():            # define a command
    print("Hello!")
    print("Welcome 🎉")

say_hello()                 # CALL it — runs the two lines
say_hello()                 # call again
```

> 🔑 `def name():` defines it. The **indented** lines are what it does.
> Nothing happens until you **call** it with `name()`.

---

## Parameters — make a function flexible

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
draw_square(100)            # big square — same command!
turtle.done()
```

> 🧠 Write the square logic **once**, reuse it forever. The grown-up DRY rule. 🌟

---

## 💻 Lab B — B1. A reusable star stamp ⭐

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
> 💡 We reuse this exact function in Session 6!

---

## B2. Many polygons with one function

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

🎯 *Make it yours:* add a `color` parameter so each polygon is a different colour.

---

## 🏆 Challenge — Build a House 🏠

A house = **triangle roof** + **square wall** + **door**.

```python
import turtle
t = turtle.Turtle()

t.color("black", "brown")          # 🔺 Roof
t.begin_fill()
for i in range(3):
    t.forward(-200); t.right(120)
t.end_fill()

t.color("black", "gray")           # ⬜ Wall (shares roof base)
t.begin_fill()
for i in range(3):
    t.right(90); t.forward(200)
t.end_fill()
```

🎯 *Extensions:* add a **window**, a **sun**, or your name with `t.write`.

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

> Full `O`, `P`, `E` solutions are in `Corrected_Code_Python3/session 5/`.

---

## 🐞 Debugging Corner

| Oops | Fix |
|---|---|
| defined a function, nothing happens | you forgot to **call** it: `my_func()` |
| `draw_square()` missing argument | pass the value: `draw_square(50)` |
| lines run that shouldn't | check what's indented **inside** `def` |
| shape at wrong spot | `penup()` before `goto`, `pendown()` after |

---

## 📒 Wrap-up

- The screen is a **map**: middle `(0,0)`, right/up positive
- `screen.setup/bgcolor/title` control the window; pixels are the dots
- **Functions (`def`)** let you build your **own commands** and reuse them
- **Parameters** make functions flexible (`draw_square(size)`)
- `t.write()` adds text; `t.hideturtle()` cleans up

---

## 🏠 Take-home Assignment 5

1. Write `draw_triangle(size)` and draw 3 triangles of different sizes.
2. Use `draw_star` to stamp **4 stars** at different spots.
3. Draw a house and add at least **one window**.
4. **Bonus:** write `draw_flower()` (loop + circle petals).

---

<!-- _class: lead -->

# 🎉 Great work!

➡️ **Next up:** Session 6 — Fireworks, Moving Ball & Final Project 🎆
