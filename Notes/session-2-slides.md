---
marp: true
theme: default
paginate: true
size: 16:9
backgroundColor: #fffdf7
header: '🖍️ Session 2 — Pen Magic & Loops'
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

# 🖍️ Session 2
## Pen Magic & Loops

⏱️ **3 hours** &nbsp;•&nbsp; 🎚️ **Beginner** &nbsp;•&nbsp; 💻 **Lots of hands-on!**

---

## 🎯 By the end, you can…

- ✅ Control the pen: **up/down, size, colour, speed, shape**
- ✅ **Fill** shapes with `begin_fill()` / `end_fill()`
- ✅ Use **colour names and hex codes** (`"#FF5733"`)
- ✅ Understand **why repeating code is bad** (the DRY idea)
- ✅ Write a **`for` loop** with `range()` and correct **indentation**

---

## 🗓️ The 3-Hour Plan

| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Recap quiz + "You are the turtle" game |
| 0:15–0:50 | 📖 Pen commands + fill |
| 0:50–1:25 | 💻 **Lab A:** smiley face + flag |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 📖 Loops + 💻 **Lab B:** loop patterns |
| 2:10–2:45 | 🏆 Challenge: colourful circle row |
| 2:45–3:00 | 📒 Recap + assignment |

---

<!-- _class: lead -->

# 🔔 Warm-up

Quick recall — **shout the answers!**
- What two lines start **every** turtle program?
- How do we go forward? Turn left?
- What does `int()` do?

🕹️ **"You are the turtle!"** — act out commands like a robot:
`stand up()` · `hands up()` · `hands down()` · `sit down()`
*You just ran a program with your body!* 🤖

---

## ✏️ Pen Magic

Like a real pen: **lift**, move, then **put down**.

| Command | What it does |
|---|---|
| `t.penup()` | ✋ lift the pen — move, don't draw |
| `t.pendown()` | ✍️ drop the pen — draw again |
| `t.pensize(5)` | make the line **thicker** |
| `t.pencolor("red")` | change the **line** colour |
| `t.speed(5)` | speed (0 = fastest, 1 = slow, 10 = fast) |
| `t.shape("turtle")` | turtle / arrow / circle / square |

---

## 🎨 Two ways to name a colour

```python
t.pencolor("blue")        # 1) by name
t.pencolor("#FF5733")     # 2) by hex code (a secret colour recipe!)
```

> 🌈 Try `#FF0000` (red), `#00FF00` (green), `#0000FF` (blue).
> Mixing **Red-Green-Blue** makes **every** colour a screen can show!

---

## 🥪 Filling shapes — the sandwich

```python
t.fillcolor("yellow")
t.begin_fill()      # 🥪 top slice — start colouring
t.circle(50)        # 🍅 the filling — your shape
t.end_fill()        # 🥪 bottom slice — stop colouring
```

> 💡 Shortcut: `t.color("black", "yellow")` sets
> **outline = black** and **fill = yellow** at once.

---

## 💻 Lab A — A1. Smiley face 🙂

```python
import turtle
t = turtle.Turtle()
t.speed(5)

t.penup(); t.goto(0, -100); t.pendown()      # yellow face
t.pensize(5); t.pencolor("black"); t.fillcolor("yellow")
t.begin_fill(); t.circle(100); t.end_fill()

t.penup(); t.goto(-35, 30); t.pendown()      # left eye
t.pensize(3); t.fillcolor("white")
t.begin_fill(); t.circle(15); t.end_fill()
```

---

## A1. Smiley face — eyes & smile

```python
t.penup(); t.goto(35, 30); t.pendown()       # right eye
t.begin_fill(); t.circle(15); t.end_fill()

t.penup(); t.goto(-50, -20); t.pendown()     # smile 😊
t.pensize(5); t.setheading(-60)
t.circle(50, 120)

turtle.done()
```

> 💡 `t.circle(50, 120)` draws only **part** of a circle (120°) — a perfect smile!
🎯 *Make it yours:* blue eyes, a bigger face, add a nose dot.

---

## A2. A simple flag 🚩

```python
import turtle
t = turtle.Turtle()
t.speed(6)
colors = ["orange", "white", "green"]
y = 60
for c in colors:
    t.penup(); t.goto(-100, y); t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    for i in range(2):
        t.forward(200); t.right(90)
        t.forward(40);  t.right(90)
    t.end_fill()
    y = y - 40
turtle.done()
```

---

<!-- _class: lead -->

# ☕ Break (10 min)

---

## 🔁 Loops: your repeat superpower

Acting out `stand / hands up / hands down / sit` **3 times** = 12 lines. Exhausting! 😩

> 🧠 **The DRY rule:** *Don't Repeat Yourself.*
> If you're copy-pasting, there's a better way — a **loop**.

```python
for i in range(3):     # ← repeat 3 times. NOTE the colon :
    print("Hello")     # ← indented lines run each time
    print("again")
```

- `range(3)` → runs **3 times** • colon `:` is required
- **Indented** lines (4 spaces) are the loop's *body*

---

## 🔑 Indentation is not decoration

```python
for i in range(3):
    stand_up()
    hands_up()
    hands_down()
    sit_down()
```

4 lines instead of 12! 🎉

> 🔑 Indentation is how Python knows what's *inside* the loop.
> Lines that aren't indented run **after** the loop finishes.

---

## 💻 Lab B — B1. A square, the loop way

```python
import turtle
t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.left(90)
turtle.done()
```

*Compare to last session's 8 lines!*

---

## B2. A staircase 🪜

```python
import turtle
t = turtle.Turtle()
t.pencolor("green")
for i in range(5):
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
turtle.done()
```

🔮 **Predict:** how many steps?
👉 **5** — `range(5)` repeats the up-and-across pattern 5 times. 🪜

---

## B3. Polygon explorer

Change ONE number to get new shapes:

```python
import turtle
t = turtle.Turtle()
sides = 5                 # try 3, 4, 6, 8 ...
angle = 360 / sides       # the turn at each corner
for i in range(sides):
    t.forward(80)
    t.left(angle)
turtle.done()
```

🎯 *Make it yours:* `sides = 8` octagon. What about `sides = 12`? 😮
> ✅ **Checkpoint:** everyone has drawn at least two polygons.

---

## 🏆 Challenge — Colourful circle row

```python
import turtle
t = turtle.Turtle()
colors = ["red", "orange", "yellow", "green", "blue"]
for c in colors:
    t.fillcolor(c)
    t.begin_fill(); t.circle(30); t.end_fill()
    t.penup(); t.forward(70); t.pendown()   # move along
turtle.done()
```

🎯 *Extensions:* make 7 circles 🌈 • each bigger than the last • draw them going **down**.

---

## 🐞 Debugging Corner

| Oops | Fix |
|---|---|
| `for i in range(4)` (no colon) | add `:` at the end |
| loop body not indented | push inside lines in (4 spaces) |
| shape not filled | need **both** `begin_fill()` and `end_fill()` |
| `t.colour(...)` error | spell it `color` (American) |

---

## 📒 Wrap-up

- `penup()` / `pendown()` move **without / with** drawing
- `begin_fill()` … `end_fill()` colour **inside** a shape 🎨
- Colours can be **names** or **hex codes**
- A **`for` loop** repeats code — no more copy-paste!
- Loop body must be **indented**; loop line ends with `:`

---

## 🏠 Take-home Assignment 2

1. **Filled circle:** draw a filled circle of radius 50.
2. **Outline vs filled:** one circle *without* fill, one *with* — note the difference.
3. **Fill pattern:** use a **loop** for **5 filled circles** of different colours in a row.
4. **Bonus:** draw a **hexagon** (6 sides) using a loop.

---

<!-- _class: lead -->

# 🎉 Great work!

➡️ **Next up:** Session 3 — Data Types, Operators & If/Else 🔢
