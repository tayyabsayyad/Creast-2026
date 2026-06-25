# 🎆 Session 6 — Randomness, Animation & Final Project

> ⬅️ [Session 5](session-5.md) &nbsp;|&nbsp; 🏠 [Home](README.md) &nbsp;|&nbsp; Next ➡️ [Session 7: The Racing Game](session-7.md)
>
> ⏱️ **Duration:** 3 hours &nbsp;•&nbsp; 🎚️ **Level:** Intermediate+ &nbsp;•&nbsp; 💻 **Lots of hands-on!**

### 🎯 Learning objectives
- [ ] Use the **`random`** module (`randint`, `choice`)
- [ ] Build a **`while True`** animation loop
- [ ] Make movement **smooth** with `tracer(0)` + `update()`
- [ ] Read the turtle's position with `xcor()` / `ycor()` and react to it
- [ ] Combine **functions + loops + randomness** into a finished piece

### 🗓️ 3-Hour Plan
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

## 🔔 Warm-up (15 min)
Roll a real dice a few times — *can anyone predict the next number?* No! That's
**randomness**. Computers can roll dice too. 🎲

---

## 🎲 Part 1 — The `random` toolbox (Concept Block A)

```python
import random
print(random.randint(1, 6))          # 🎲 a random whole number 1–6 (both ends included)
print(random.choice(["red", "blue", "green"]))   # 🎨 picks one at random
```
| Command | Gives you |
|---|---|
| `random.randint(a, b)` | a random whole number from `a` to `b` |
| `random.choice(mylist)` | a random item from a list |

> 🧠 Run it a few times — different answers each time! That unpredictability makes games
> and art exciting.

### 🎆 Fireworks animation
Each firework = a **random spot** + **20 sparks** in **random directions & colours**:
```python
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")        # night sky 🌃
t.speed(0); t.hideturtle()

colors = ["red", "yellow", "blue", "green", "orange", "pink", "white"]

for f in range(8):             # 8 fireworks
    x = random.randint(-200, 200)
    y = random.randint(-150, 200)
    t.penup(); t.goto(x, y); t.pendown()
    for i in range(20):        # 20 sparks each
        t.color(random.choice(colors))
        t.setheading(random.randint(0, 360))
        t.forward(50)
        t.backward(50)         # back to centre → star-burst ✨
screen.done()
```
> 💡 Each spark goes **out then back**, so they share one centre — that's the burst shape!
> Notice the **loop-inside-a-loop** (8 fireworks × 20 sparks).

---

## 💻 Lab A — Random art (35 min)

**A1. Run the fireworks** above. 🎯 Then: change `8` to `12`, add a colour to the list.

**A2. Random walk** 🚶 — the turtle wanders forever:
```python
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.color("red"); t.shape("turtle"); t.speed(0)
t.penup(); t.goto(0, 0); t.pendown()

colors = ["red", "yellow", "blue", "green", "pink", "white"]
while True:
    t.color(random.choice(colors))
    t.setheading(random.randint(0, 360))
    t.forward(random.randint(20, 50))
```
> 🌈 `while True:` runs **forever** (until you close the window). Every run looks different!

**✅ Checkpoint:** everyone has seen a different fireworks/walk each run — they *get* randomness.

---

## ☕ Break (10 min)

---

## ⚽ Part 2 — Smooth animation (Concept Block B)

To animate smoothly we draw **frame by frame**. Three new tricks:
- `screen.tracer(0)` → turn **off** auto-drawing so *we* control each frame
- `screen.update()` → show the next frame
- `t.clear()` → erase the old drawing before the new one

```python
import turtle
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("green")
screen.tracer(0)              # we update the screen ourselves

t = turtle.Turtle()
t.color("orange"); t.speed(0); t.width(2); t.hideturtle()
t.penup(); t.goto(-250, 0); t.pendown()

while True:                   # the animation loop
    t.clear()                 # erase old ball
    t.fillcolor("orange")
    t.begin_fill(); t.circle(20); t.end_fill()   # draw ball
    screen.update()           # show this frame
    t.forward(1)              # nudge right
    if t.xcor() > 300:        # off the right edge?
        t.goto(-250, 0)       # jump back to the left 🔁
```
> 🧠 `t.xcor()` gives the turtle's **x** position. We use an `if` to detect "off-screen"
> and reset — that's game logic! 🕹️

🎯 **Cool change:** turn the ball into a **diamond** → replace `t.circle(20)` with
`t.circle(30, steps=4)`. 💎

---

## 🏆 FINAL TEST (35 min) — Full moon sky 🌙⭐

> **Task:** draw a **full-moon sky with at least 4 stars**.
>
> | Item | Marks |
> |---|---|
> | Moon in the right position | 10 |
> | Each of 3 stars roughly placed | 10 each |
> | **Total** | **40** |

**The smart way — use the `draw_star` function from Session 5!** ⭐
```python
import turtle
t = turtle.Turtle()
t.speed(5)
screen = turtle.Screen()
screen.bgcolor("black")

def star(x, y, size):              # our reusable star stamp
    t.penup(); t.goto(x, y); t.pendown()
    t.color("white")
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# four stars, different sizes & spots
star(-250, 250, 100)
star(40, 250, 30)
star(40, -50, 60)
star(-140, -50, 30)

# the full moon 🌕
t.penup(); t.goto(-80, 40); t.pendown()
t.color("white")
t.begin_fill(); t.circle(40); t.end_fill()

t.hideturtle()
turtle.done()
```
> 🌟 See how the **function** turned 4 messy star-drawings into 4 tidy lines? That's the
> payoff from Session 5!

🎯 *Extensions:* add more stars in a **loop** with random positions, or add a "Good Night"
title with `t.write`.

---

## 🐞 Debugging Corner
| Oops | Fix |
|---|---|
| animation flickers / jumps | add `screen.tracer(0)` and `screen.update()` |
| old ball not erased | call `t.clear()` at the top of the loop |
| ball drifts off and never returns | check the `if t.xcor() > 300:` reset |
| `random` not defined | add `import random` at the top |

---

## 📒 Wrap-up (5 min)
- `random.randint()` / `random.choice()` add **surprise** 🎲
- `while True:` repeats forever; `tracer(0)` + `update()` make it **smooth**
- `t.xcor()` / `t.ycor()` read position → react with `if` (game logic!)
- **Functions** make big drawings tidy (the star stamp!)

## 🏠 Take-home Assignment 6
1. Make fireworks fire **12** times with **5** colours of your choice.
2. Make the moving ball move **faster** (`t.forward(3)`) and **change its colour**.
3. Add a **5th star** to your moon sky.
4. **Bonus:** make the ball **bounce back** instead of jumping (hint: when `xcor() > 300`,
   turn it around with `t.setheading(180)`).

<details><summary>🔑 Facilitator answer key (bounce idea)</summary>

```python
# inside the while loop, replace the reset with a bounce:
if t.xcor() > 250:
    t.setheading(180)        # face left
if t.xcor() < -250:
    t.setheading(0)          # face right
```
</details>

<details><summary>🧑‍🏫 Facilitator notes</summary>

- This is a **big payoff** session — celebrate the fireworks and the moon sky out loud.
- Re-introduce the **star function** explicitly: "remember `draw_star` from last time?"
- `tracer(0)`/`update()` is abstract — say "we're the film director deciding when to show
  each picture." Show the ball **without** `tracer(0)` first so they see the flicker.
- **Final test:** have interns mark per the rubric; absent students complete missed labs first.
- **Fast finishers:** the bounce bonus and random-loop stars.
</details>

➡️ **Next up:** [Session 7 — Randomness & the Racing Game](session-7.md)
