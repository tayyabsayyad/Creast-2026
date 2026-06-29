---
marp: true
theme: default
paginate: true
size: 16:9
backgroundColor: #fffdf7
header: '🏁 Session 7 — The Racing Game & Capstone'
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

# 🏁 Session 7
## The Racing Game & Capstone

⏱️ **3 hours** &nbsp;•&nbsp; 🎚️ **Intermediate+** &nbsp;•&nbsp; 🏆 **Project day!**

---

## 🎯 By the end, you can…

- ✅ Manage **several turtle objects** at once
- ✅ Build a multi-part program **step by step**
- ✅ Use **randomness** to drive a game
- ✅ *(Stretch)* detect a **winner** with a condition
- ✅ Plan and present a **capstone** project 🎤

---

## 🗓️ The 3-Hour Plan

| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Recap `randint` + random-walk re-run |
| 0:15–0:50 | 📖 Multiple turtles + build the track |
| 0:50–1:25 | 💻 **Lab A:** add 4 players & race |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 🛠️ Stretch: winner detection / your twist |
| 2:10–2:45 | 🏆 **Capstone:** build your own project |
| 2:45–3:00 | 🎤 Showcase + certificates + feedback |

---

<!-- _class: lead -->

# 🔔 Warm-up

```python
from random import randint
print(randint(4, 8))     # run a few times — different each time
```

🆕 `from random import randint` lets us write just `randint(...)`.

> *"How could we make FOUR turtles move at once?"*
> — that's today's game! 🏁

---

## 🐢🐢 Many turtles, one screen

Each turtle is its own object with its own colour, shape, position:

```python
import turtle
red_t  = turtle.Turtle(); red_t.color("red")
blue_t = turtle.Turtle(); blue_t.color("blue")
red_t.forward(100)        # only the red turtle moves
blue_t.left(90); blue_t.forward(100)
turtle.done()
```

> 🧠 Think of each turtle as a **separate player** with its own pen.

---

## 🛣️ Build the race track

```python
import turtle
from random import randint

t = turtle.Turtle(); t.speed(0)
t.penup(); t.goto(-140, 140)

for j in range(15):
    t.write(j, align="center")     # number each lane line
    t.right(90)
    for num in range(8):           # 8 little dashes (nested loop!)
        t.penup(); t.forward(10)
        t.pendown(); t.forward(10)
    t.penup(); t.backward(160)
    t.left(90); t.forward(20)
```

> 🔁 Spot the **nested loop** — every skill from earlier sessions coming together!

---

## 💻 Lab A — Add 4 players

```python
plyr1 = turtle.Turtle()
plyr1.color("magenta"); plyr1.shape("turtle")
plyr1.penup(); plyr1.goto(-160, 100); plyr1.pendown()
for turn in range(10):
    plyr1.right(36)        # a fun spin-in entrance 🌀

plyr2 = turtle.Turtle()
plyr2.color("red"); plyr2.shape("turtle")
plyr2.penup(); plyr2.goto(-160, 70); plyr2.pendown()
for turn in range(10):
    plyr2.left(36)
```

> …repeat for `plyr3` at `y=40` (green) and `plyr4` at `y=10` (blue).

---

## 🚦 START THE RACE!

Each turn, every turtle jumps a random 1–5 steps:

```python
for turn in range(100):
    plyr1.forward(randint(1, 5))
    plyr2.forward(randint(1, 5))
    plyr3.forward(randint(1, 5))
    plyr4.forward(randint(1, 5))
turtle.done()
```

🔮 Who wins?
👉 **Nobody can predict it!** 🎲 The winner changes every race.

> 📄 Full game: `Corrected_Code_Python3/session 7/02_turtle_racing_game.py`
> ✅ **Checkpoint:** every student has a 4-turtle race running.

---

<!-- _class: lead -->

# ☕ Break (10 min)

---

## 🛠️ Make it YOUR game (Stretch)

**1. Add a 5th racer** at `goto(-160, -20)` in a new colour. 🐢

**2. Announce a winner** (uses `xcor` + `max`):

```python
positions = {
    "magenta": plyr1.xcor(), "red": plyr2.xcor(),
    "green":   plyr3.xcor(), "blue": plyr4.xcor(),
}
winner = max(positions, key=positions.get)

msg = turtle.Turtle(); msg.hideturtle(); msg.penup()
msg.goto(0, -150)
msg.write("Winner: " + winner + "! 🏆", align="center", font=("Arial", 18, "bold"))
turtle.done()
```

**3. Change the rules:** make one turtle faster (`randint(1, 8)`), or a longer track.

---

## 🏆 Capstone Project — Build your own!

Use **everything**: shapes, loops, if/else, functions, randomness, coordinates.

| Project | Skills it uses |
|---|---|
| 🏞️ **Scenery** (sun, house, trees) | shapes, functions, coordinates |
| 🎯 **Random art generator** | loops + `random` colours & angles |
| 🌃 **Night sky** (moon + stars) | functions + loops + random |
| 🚦 **Animated traffic light** | if/else + colours |
| 🏁 **Your own race** (cars, animals) | multiple turtles + random |
| ✍️ **Write your full name** in shapes | coordinates + functions |

> 🧑‍🎨 **Plan first!** Sketch on paper, list shapes, code one piece at a time, run often.

---

## 🎤 Showcase & Wrap-up

- Each student shows their screen and says **one thing they're proud of**. 👏
- Hand out **certificates / prizes** and collect **feedback**.

---

## 🐞 Debugging Corner

| Oops | Fix |
|---|---|
| all turtles draw on top of each other | give each its own `goto(...)` start |
| only one turtle moves | check you used `plyr2`, `plyr3`… everywhere |
| race ends instantly | increase `range(100)` and step size |
| `randint` not defined | add `from random import randint` |

---

## 🎓 What you learned across the course

- ✅ Talked to a computer with **Python** (`print`, `input`, variables)
- ✅ Drew with the **turtle**; used **loops** and **if/else**
- ✅ Built your **own commands** with **functions**
- ✅ Used **coordinates**, **animation**, and **randomness**
- ✅ Combined it all into a **game** and a **capstone**!

---

<!-- _class: lead -->

# 🌟 Keep going!

Every big game and app began with someone drawing a little square —
exactly like you did in **Session 1**.

The turtle is just the beginning. 🚀
