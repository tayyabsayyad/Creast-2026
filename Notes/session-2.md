# 🖍️ Session 2 — Pen Magic & Loops

> ⬅️ [Session 1](session-1.md) &nbsp;|&nbsp; 🏠 [Home](README.md) &nbsp;|&nbsp; Next ➡️ [Session 3: Data Types & If/Else](session-3.md)
>
> ⏱️ **Duration:** 3 hours &nbsp;•&nbsp; 🎚️ **Level:** Beginner &nbsp;•&nbsp; 💻 **Lots of hands-on!**

### 🎯 Learning objectives
- [ ] Control the pen: **up/down, size, colour, speed, shape**
- [ ] **Fill** shapes with colour using `begin_fill()` / `end_fill()`
- [ ] Use **colour names and hex codes** (`"#FF5733"`)
- [ ] Understand **why repeating code is bad** (the DRY idea)
- [ ] Write a **`for` loop** with `range()` and use correct **indentation**

### 🗓️ 3-Hour Plan
| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Recap quiz + "You are the turtle" body game |
| 0:15–0:50 | 📖 Pen commands + fill |
| 0:50–1:25 | 💻 **Lab A:** smiley face + flag |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 📖 Loops + 💻 **Lab B:** loop patterns |
| 2:10–2:45 | 🏆 Challenge: colourful circle row |
| 2:45–3:00 | 📒 Recap + assignment |

---

## 🔔 Warm-up (15 min)

Quick recall (shout the answers!):
- What two lines start **every** turtle program?
- How do we make the turtle go forward? Turn left?
- What does `int()` do?

🕹️ **"You are the turtle!"** — students stand and act out commands like a robot:
```
stand up()      hands up()      hands down()      sit down()
```
You just *ran a program with your body!* 🤖 (We'll come back to this for loops.)

---

## ✏️ Part 1 — Pen Magic (Concept Block A)

When you write with a real pen and want to start somewhere new, you **lift** the pen,
move, then **put it down**. The turtle works the same way!

| Command | What it does |
|---|---|
| `t.penup()` | ✋ lift the pen — move but **don't** draw |
| `t.pendown()` | ✍️ drop the pen — draw again |
| `t.pensize(5)` | make the line **thicker** |
| `t.pencolor("red")` | change the **line** colour |
| `t.speed(5)` | move speed (0 = fastest, 1 = slow, 10 = fast) |
| `t.shape("turtle")` | turtle / arrow / circle / square / triangle |

### 🎨 Two ways to name a colour
```python
t.pencolor("blue")        # 1) by name
t.pencolor("#FF5733")     # 2) by hex code (a secret colour recipe!)
```
> 🌈 Try the hex codes `#FF0000` (red), `#00FF00` (green), `#0000FF` (blue).
> Mixing Red-Green-Blue makes **every** colour a screen can show!

### Filling shapes — the sandwich 🥪
```python
t.fillcolor("yellow")
t.begin_fill()      # 🥪 top slice — start colouring
t.circle(50)        # 🍅 the filling — your shape
t.end_fill()        # 🥪 bottom slice — stop colouring
```
> 💡 Shortcut: `t.color("black", "yellow")` sets **outline = black** and **fill = yellow** at once.

**Live demo (teacher):** draw a filled red circle, then change the fill to blue. Ask the
class to predict each result before you run it.

---

## 💻 Lab A — Build & fill (35 min)

**A1. Smiley face — build it in 4 steps** 🙂
```python
import turtle
t = turtle.Turtle()
t.speed(5)

# Step 1: yellow face
t.penup(); t.goto(0, -100); t.pendown()
t.pensize(5)
t.pencolor("black")
t.fillcolor("yellow")
t.begin_fill(); t.circle(100); t.end_fill()

# Step 2: left eye
t.penup(); t.goto(-35, 30); t.pendown()
t.pensize(3); t.fillcolor("white")
t.begin_fill(); t.circle(15); t.end_fill()

# Step 3: right eye
t.penup(); t.goto(35, 30); t.pendown()
t.begin_fill(); t.circle(15); t.end_fill()

# Step 4: smile 😊
t.penup(); t.goto(-50, -20); t.pendown()
t.pensize(5); t.setheading(-60)
t.circle(50, 120)

turtle.done()
```
> 💡 `t.circle(50, 120)` draws only **part** of a circle (120° of it) — a perfect smile!

🎯 *Make it yours:* blue eyes, a bigger face (`circle(150)`), or add a nose dot.

**A2. A simple flag** 🚩 (three filled stripes)
```python
import turtle
t = turtle.Turtle()
t.speed(6)
colors = ["orange", "white", "green"]   # we'll loop this properly in Lab B!
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

**✅ Checkpoint:** everyone has a smiley on screen and understands the fill sandwich.

---

## ☕ Break (10 min)

---

## 🔁 Part 2 — Loops: your repeat superpower (Concept Block B)

Remember acting out `stand up / hands up / hands down / sit down`? Now do it **3 times**.
Writing all 12 lines is exhausting! 😩

> 🧠 **The DRY rule:** *Don't Repeat Yourself.* If you're copy-pasting the same lines,
> there's a better way — a **loop**.

### Anatomy of a `for` loop
```python
for i in range(3):     # ← repeat 3 times. NOTE the colon :
    print("Hello")     # ← indented lines run each time
    print("again")
```
- `range(3)` makes the loop run **3 times**
- The **colon `:`** is required
- The **indented** lines (pushed in 4 spaces) are the loop's *body*

So the body game becomes:
```python
for i in range(3):
    stand_up()
    hands_up()
    hands_down()
    sit_down()
```
4 lines instead of 12! 🎉

> 🔑 **Indentation is not decoration** — it's how Python knows what's *inside* the loop.
> Lines that aren't indented run **after** the loop finishes.

---

## 💻 Lab B — Loop patterns (35 min)

**B1. A square — the loop way** (compare to last session's 8 lines!)
```python
import turtle
t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.left(90)
turtle.done()
```

**B2. A staircase** 🪜
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
🔮 **Predict:** how many steps? <details><summary>👉</summary> **5** — `range(5)` repeats the up-and-across pattern 5 times. 🪜</details>

**B3. Polygon explorer** — change ONE number to get new shapes:
```python
import turtle
t = turtle.Turtle()
sides = 5                 # try 3, 4, 6, 8 ...
angle = 360 / sides       # the turtle's turn at each corner
for i in range(sides):
    t.forward(80)
    t.left(angle)
turtle.done()
```
🎯 *Make it yours:* set `sides = 8` for an octagon. What about `sides = 12`? 😮

**✅ Checkpoint:** every student has changed `sides` and drawn at least two polygons.

---

## 🏆 Challenge (35 min) — Colourful circle row

Use a **loop + a colour list** to draw 5 filled circles in a row:
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
🎯 *Extensions:* make 7 circles 🌈 • make each circle bigger than the last •
draw them going **down** instead of across.

---

## 🐞 Debugging Corner
| Oops | Fix |
|---|---|
| `for i in range(4)` (no colon) | add `:` at the end |
| loop body not indented | push the inside lines in (4 spaces) |
| shape not filled | you need **both** `begin_fill()` and `end_fill()` |
| `t.colour(...)` error | spell it `color` (American spelling) |

---

## 📒 Wrap-up (5 min)
- `penup()` / `pendown()` move **without / with** drawing
- `begin_fill()` … `end_fill()` colour **inside** a shape 🎨
- Colours can be **names** or **hex codes**
- A **`for` loop** repeats code — no more copy-paste!
- Code inside a loop must be **indented**, and the loop line ends with `:`

## 🏠 Take-home Assignment 2
1. **Filled circle:** choose any fill colour and draw a filled circle of radius 50.
2. **Outline vs filled:** draw one circle *without* fill and one *with* fill — note the difference.
3. **Fill pattern:** use a **loop** to draw **5 filled circles of different colours** in a row.
4. **Bonus:** draw a **hexagon** (6 sides) using a loop.

<details><summary>🔑 Facilitator answer key</summary>

```python
# Q1
import turtle
t = turtle.Turtle()
t.fillcolor("purple")
t.begin_fill(); t.circle(50); t.end_fill()
turtle.done()

# Q4 hexagon
import turtle
t = turtle.Turtle()
for i in range(6):
    t.forward(70)
    t.left(60)            # 360 / 6 = 60
turtle.done()
```
(Q2 & Q3 solutions match the Challenge code above.)
</details>

<details><summary>🧑‍🏫 Facilitator notes — timing & tips</summary>

- **Biggest stumbling block:** indentation. Show side-by-side a loop with the body
  indented vs not, and run both so they *see* the difference.
- **Demo trick:** lower `t.speed()` for the smiley so students watch each step draw.
- **Fast finishers:** in B3, ask "what shape do you get with `sides = 360`?" (a circle!).
- **Support:** give a printed copy of the smiley code so slower typists don't fall behind.
- **Tie-in:** keep referencing the body game — "this loop = doing the exercise 3 times."
</details>

➡️ **Next up:** [Session 3 — Data Types, Operators & If/Else](session-3.md)
