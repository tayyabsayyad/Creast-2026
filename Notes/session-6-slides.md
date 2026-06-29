---
marp: true
theme: default
paginate: true
size: 16:9
backgroundColor: #fffdf7
header: '🎆 Session 6 — Randomness, Animation & Final Project'
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

# 🎆 Session 6
## Randomness, Animation & Final Project

⏱️ **3 hours** &nbsp;•&nbsp; 🎚️ **Intermediate+** &nbsp;•&nbsp; 💻 **Lots of hands-on!**

---

## 🎯 By the end, you can…

- ✅ Use the **`random`** module (`randint`, `choice`)
- ✅ Build a **`while True`** animation loop
- ✅ Make movement **smooth** with `tracer(0)` + `update()`
- ✅ Read position with `xcor()` / `ycor()` and react to it
- ✅ Combine **functions + loops + randomness** into a finished piece

---

## 🗓️ The 3-Hour Plan

| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Dice game → "what is random?" |
| 0:15–0:50 | 📖 `random` + fireworks |
| 0:50–1:25 | 💻 **Lab A:** fireworks & random walk |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 📖 Animation loop + 💻 **Lab B:** moving ball |
| 2:10–2:45 | 🏆 **Final Test:** moon-lit sky 🌙 |
| 2:45–3:00 | 📒 Recap + assignment |

---

<!-- _class: lead -->

# 🔔 Warm-up

🎲 Roll a real dice a few times —
*can anyone predict the next number?*

**No!** That's **randomness**.
Computers can roll dice too.

---

## 🎲 The `random` toolbox

```python
import random
print(random.randint(1, 6))                      # 🎲 1–6 (both ends included)
print(random.choice(["red", "blue", "green"]))   # 🎨 picks one at random
```

| Command | Gives you |
|---|---|
| `random.randint(a, b)` | a random whole number `a` to `b` |
| `random.choice(mylist)` | a random item from a list |

> 🧠 Run it a few times — different answers each time!

---

## 🎆 Fireworks animation

Each firework = a **random spot** + **20 sparks** in random directions & colours.

```python
import turtle, random
t = turtle.Turtle(); screen = turtle.Screen()
screen.bgcolor("black")               # night sky 🌃
t.speed(0); t.hideturtle()
colors = ["red", "yellow", "blue", "green", "orange", "pink", "white"]

for f in range(8):                    # 8 fireworks
    x = random.randint(-200, 200); y = random.randint(-150, 200)
    t.penup(); t.goto(x, y); t.pendown()
    for i in range(20):               # 20 sparks each
        t.color(random.choice(colors))
        t.setheading(random.randint(0, 360))
        t.forward(50); t.backward(50) # out then back → star-burst ✨
screen.done()
```
> 💡 A **loop-inside-a-loop** (8 fireworks × 20 sparks).

---

## 💻 Lab A — A2. Random walk 🚶

```python
import turtle, random
wn = turtle.Screen(); wn.bgcolor("black")
t = turtle.Turtle()
t.color("red"); t.shape("turtle"); t.speed(0)
t.penup(); t.goto(0, 0); t.pendown()

colors = ["red", "yellow", "blue", "green", "pink", "white"]
while True:
    t.color(random.choice(colors))
    t.setheading(random.randint(0, 360))
    t.forward(random.randint(20, 50))
```

> 🌈 `while True:` runs **forever** (until you close the window).
> ✅ **Checkpoint:** everyone *gets* randomness — every run is different!

---

<!-- _class: lead -->

# ☕ Break (10 min)

---

## ⚽ Smooth animation

Draw **frame by frame**. Three new tricks:
- `screen.tracer(0)` → turn **off** auto-drawing
- `screen.update()` → show the next frame
- `t.clear()` → erase the old drawing first

```python
import turtle
screen = turtle.Screen(); screen.setup(600, 600)
screen.bgcolor("green"); screen.tracer(0)
t = turtle.Turtle()
t.color("orange"); t.speed(0); t.width(2); t.hideturtle()
t.penup(); t.goto(-250, 0); t.pendown()
```

---

## The animation loop

```python
while True:
    t.clear()                 # erase old ball
    t.fillcolor("orange")
    t.begin_fill(); t.circle(20); t.end_fill()   # draw ball
    screen.update()           # show this frame
    t.forward(1)              # nudge right
    if t.xcor() > 300:        # off the right edge?
        t.goto(-250, 0)       # jump back to the left 🔁
```

> 🧠 `t.xcor()` gives the **x** position. The `if` detects "off-screen" — that's game logic! 🕹️
🎯 Make a **diamond:** `t.circle(30, steps=4)` 💎

---

## 🏆 FINAL TEST — Full moon sky 🌙⭐

> **Task:** draw a full-moon sky with at least 4 stars.

| Item | Marks |
|---|---|
| Moon in the right position | 10 |
| Each of 3 stars roughly placed | 10 each |
| **Total** | **40** |

**The smart way — reuse the `draw_star` function from Session 5!** ⭐

---

## Final Test — the code

```python
import turtle
t = turtle.Turtle(); t.speed(5)
screen = turtle.Screen(); screen.bgcolor("black")

def star(x, y, size):              # reusable star stamp
    t.penup(); t.goto(x, y); t.pendown()
    t.color("white"); t.begin_fill()
    for i in range(5):
        t.forward(size); t.right(144)
    t.end_fill()

star(-250, 250, 100); star(40, 250, 30)
star(40, -50, 60);    star(-140, -50, 30)

t.penup(); t.goto(-80, 40); t.pendown()        # the full moon 🌕
t.color("white"); t.begin_fill(); t.circle(40); t.end_fill()
t.hideturtle(); turtle.done()
```
> 🌟 The **function** turned 4 messy star-drawings into 4 tidy lines!

---

## 🐞 Debugging Corner

| Oops | Fix |
|---|---|
| animation flickers / jumps | add `screen.tracer(0)` and `screen.update()` |
| old ball not erased | call `t.clear()` at the top of the loop |
| ball drifts off, never returns | check the `if t.xcor() > 300:` reset |
| `random` not defined | add `import random` at the top |

---

## 📒 Wrap-up

- `random.randint()` / `random.choice()` add **surprise** 🎲
- `while True:` repeats forever; `tracer(0)` + `update()` make it **smooth**
- `t.xcor()` / `t.ycor()` read position → react with `if` (game logic!)
- **Functions** make big drawings tidy (the star stamp!)

---

## 🏠 Take-home Assignment 6

1. Make fireworks fire **12** times with **5** colours.
2. Make the moving ball **faster** (`t.forward(3)`) and **change its colour**.
3. Add a **5th star** to your moon sky.
4. **Bonus:** make the ball **bounce back** (when `xcor() > 300`, `t.setheading(180)`).

---

<!-- _class: lead -->

# 🎉 Great work!

➡️ **Next up:** Session 7 — Randomness & the Racing Game 🏁
