# 🏁 Session 7 — The Racing Game & Capstone

> ⬅️ [Session 6](session-6.md) &nbsp;|&nbsp; 🏠 [Home](README.md)
>
> ⏱️ **Duration:** 3 hours &nbsp;•&nbsp; 🎚️ **Level:** Intermediate+ &nbsp;•&nbsp; 🏆 **Project day!**

### 🎯 Learning objectives
- [ ] Manage **several turtle objects** at once
- [ ] Build a multi-part program **step by step**
- [ ] Use **randomness** to drive a game
- [ ] (Stretch) detect a **winner** with a condition
- [ ] Plan and present a **capstone** project 🎤

### 🗓️ 3-Hour Plan
| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Recap `randint` + a random-walk re-run |
| 0:15–0:50 | 📖 Multiple turtles + build the track |
| 0:50–1:25 | 💻 **Lab A:** add 4 players & race |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 🛠️ Stretch: winner detection / your own twist |
| 2:10–2:45 | 🏆 **Capstone:** pick & build your own project |
| 2:45–3:00 | 🎤 Showcase + certificates + feedback |

---

## 🔔 Warm-up (15 min)
```python
from random import randint
print(randint(4, 8))     # run a few times — different each time
```
> 🆕 `from random import randint` lets us write just `randint(...)`. A handy shortcut!

Re-run last session's **random walk** for fun, then ask: *"How could we make FOUR turtles
move at once?"* — that's today's game! 🏁

---

## 🐢🐢 Part 1 — Many turtles, one screen (Concept Block A)

Until now we made **one** turtle (`t`). But we can make as many as we like — each is its
own object with its own colour, shape, and position:
```python
import turtle
red_t  = turtle.Turtle(); red_t.color("red")
blue_t = turtle.Turtle(); blue_t.color("blue")
red_t.forward(100)        # only the red turtle moves
blue_t.left(90); blue_t.forward(100)
turtle.done()
```
> 🧠 Think of each turtle as a **separate player** with its own pen.

### Build the race track 🛣️
```python
import turtle
from random import randint

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-140, 140)

for j in range(15):
    t.write(j, align="center")     # number each lane line
    t.right(90)
    for num in range(8):           # 8 little dashes (nested loop!)
        t.penup(); t.forward(10)
        t.pendown(); t.forward(10)
    t.penup()
    t.backward(160)
    t.left(90)
    t.forward(20)
```
> 🔁 Spot the **nested loop** and the **functions/skills** from earlier sessions all coming
> together. You already know every piece!

---

## 💻 Lab A — The Racing Game (35 min)

**Part 2 — Add 4 players** (each its own turtle at the start line):
```python
# Player 1
plyr1 = turtle.Turtle()
plyr1.color("magenta"); plyr1.shape("turtle")
plyr1.penup(); plyr1.goto(-160, 100); plyr1.pendown()
for turn in range(10):
    plyr1.right(36)        # a fun spin-in entrance 🌀

# Player 2
plyr2 = turtle.Turtle()
plyr2.color("red"); plyr2.shape("turtle")
plyr2.penup(); plyr2.goto(-160, 70); plyr2.pendown()
for turn in range(10):
    plyr2.left(36)

# Player 3
plyr3 = turtle.Turtle()
plyr3.color("green"); plyr3.shape("turtle")
plyr3.penup(); plyr3.goto(-160, 40); plyr3.pendown()
for turn in range(10):
    plyr3.left(36)

# Player 4
plyr4 = turtle.Turtle()
plyr4.color("blue"); plyr4.shape("turtle")
plyr4.penup(); plyr4.goto(-160, 10); plyr4.pendown()
for turn in range(10):
    plyr4.right(36)
```

**Part 3 — START THE RACE!** 🚦 (each turn, every turtle jumps a random 1–5 steps)
```python
for turn in range(100):
    plyr1.forward(randint(1, 5))
    plyr2.forward(randint(1, 5))
    plyr3.forward(randint(1, 5))
    plyr4.forward(randint(1, 5))
turtle.done()
```
🔮 Who wins? <details><summary>👉</summary>**Nobody can predict it!** 🎲 Each step is random, so the winner changes every race.</details>

> 📄 The full joined-up game is in
> [`../Corrected_Code_Python3/session 7/02_turtle_racing_game.py`](../Corrected_Code_Python3/).

**✅ Checkpoint:** every student has a 4-turtle race running.

---

## ☕ Break (10 min)

---

## 🛠️ Part 2 — Make it YOUR game (Stretch, 35 min)

Pick one or more upgrades:

**1. Add a 5th racer** at `goto(-160, -20)` in a new colour. 🐢

**2. Announce a winner** (stretch — uses `xcor` + `if`):
```python
# after the race loop, find who went furthest
positions = {
    "magenta": plyr1.xcor(),
    "red":     plyr2.xcor(),
    "green":   plyr3.xcor(),
    "blue":    plyr4.xcor(),
}
winner = max(positions, key=positions.get)

msg = turtle.Turtle(); msg.hideturtle(); msg.penup()
msg.goto(0, -150)
msg.write("Winner: " + winner + "! 🏆", align="center", font=("Arial", 18, "bold"))
turtle.done()
```

**3. Change the rules:** make one turtle faster (`randint(1, 8)`), or a longer track.

---

## 🏆 Capstone Project (35 min) — Build your own!

Choose a project and use **everything** you've learned (shapes, loops, if/else, functions,
randomness, coordinates). Ideas:

| Project | Skills it uses |
|---|---|
| 🏞️ **Scenery** (sun, house, trees, river) | shapes, functions, coordinates |
| 🎯 **Random art generator** | loops + `random` colours & angles |
| 🌃 **Night sky** (moon + many random stars) | functions + loops + random |
| 🚦 **Animated traffic light** | if/else + colours |
| 🏁 **Your own race** (animals, cars) | multiple turtles + random |
| ✍️ **Write your full name** in shapes | coordinates + functions |

> 🧑‍🎨 **Plan first!** Sketch on paper, list the shapes, then code one piece at a time and
> run often.

---

## 🎤 Showcase & Wrap-up (15 min)
- Each student shows their screen and says **one thing they're proud of**. 👏
- Hand out **certificates / prizes** and collect **feedback**.

---

## 🐞 Debugging Corner
| Oops | Fix |
|---|---|
| all turtles draw on top of each other | give each its own `goto(...)` start |
| only one turtle moves | check you used `plyr2`, `plyr3`… not `plyr1` everywhere |
| race ends instantly | increase `range(100)` and step size |
| `randint` not defined | add `from random import randint` |

---

## 📒 What you learned across the whole course 🎓
- ✅ Talked to a computer with **Python** (`print`, `input`, variables)
- ✅ Drew with the **turtle**; used **loops** and **if/else**
- ✅ Built your **own commands** with **functions**
- ✅ Used **coordinates**, **animation**, and **randomness**
- ✅ Combined it all into a **game** and a **capstone project**!

> 🌟 **Keep going!** Every big game and app began with someone drawing a little square —
> exactly like you did in Session 1. The turtle is just the beginning. 🚀

🏠 [Back to Home](README.md)
