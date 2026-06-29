---
marp: true
theme: default
paginate: true
size: 16:9
backgroundColor: #fffdf7
header: '🔁 Session 4 — Loops Deep Dive'
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

# 🔁 Session 4
## Loops Deep Dive — `for` & `while`

⏱️ **3 hours** &nbsp;•&nbsp; 🎚️ **Intermediate** &nbsp;•&nbsp; 💻 **Lots of hands-on!**

---

## 🎯 By the end, you can…

- ✅ Use `range(start, stop, step)` confidently
- ✅ Loop through a **list**
- ✅ Build an **accumulator** (a running total)
- ✅ Write a **`while`** loop with a counter — avoid **infinite loops**
- ✅ Use **nested loops** for patterns and turtle art

---

## 🗓️ The 3-Hour Plan

| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Recall if/elif + "climb 200 stairs" story |
| 0:15–0:50 | 📖 `for` loop in depth (range, lists, totals) |
| 0:50–1:25 | 💻 **Lab A:** tables, countdown, polygons |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 📖 `while` loops + nested loops |
| 2:10–2:45 | 🏆 Challenge: draw the Sun ☀️ |
| 2:45–3:00 | 📒 Recap + assignment |

---

<!-- _class: lead -->

# 🔔 Warm-up

🤖 **The robot story:** *"Tell a robot to climb 200 stairs —
left leg up, forward, down, right leg up, forward, down…"*

Would you write that 200 times? 😵
**No!** That's what loops are for.

---

## 🔢 The `for` loop, up close

`range()` builds a sequence of numbers to walk through.

```python
for x in range(4):
    print(x)
```
**Output:** `0  1  2  3` → 😲 starts at **0**, stops **before** 4!

| `range(...)` | Numbers |
|---|---|
| `range(4)` | 0, 1, 2, 3 |
| `range(1, 5)` | 1, 2, 3, 4 |
| `range(2, 11, 2)` | 2, 4, 6, 8, 10 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 (down) |

---

## Looping a list · Accumulator 🧮

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print("I like", x)
```

```python
total = 0
for n in range(1, 6):    # 1..5
    total = total + n    # keep adding
print("Total is", total)
```

🔮 What's the total? 👉 `15` (1+2+3+4+5). The box grows each loop. 🧮

---

## 💻 Lab A — A1. Multiplication table

```python
num = int(input("Which table? "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

🎯 *Make it yours:* print only **even** results, or tables for 2 *and* 3.

---

## A2. Countdown · A3. Polygon family

```python
for n in range(5, 0, -1):       # 🚀 Rocket countdown
    print(n)
print("Blast off! 🚀")
```

```python
import turtle                    # one loop, many shapes
t = turtle.Turtle()
sides = 6                 # try 3, 4, 5, 8...
for i in range(sides):
    t.forward(80)
    t.left(360 / sides)
turtle.done()
```
> ✅ **Checkpoint:** everyone printed a times-table and drew a polygon.

---

<!-- _class: lead -->

# ☕ Break (10 min)

---

## ⏳ The `while` loop

Repeats *as long as* a condition is true (Hindi: **जब तक** — "until").

```python
punch = 1
while punch <= 3:
    print("puuuunncccchhhhh")
    punch = punch + 1      # 🔑 the counter MUST change
```

> ⚠️ **Infinite-loop danger!** Forget `punch = punch + 1` and it never stops. 😱
> Every `while` needs something that eventually makes the condition **False**.

---

## `for` vs `while` — which one?

| Use a `for` loop when… | Use a `while` loop when… |
|---|---|
| you know **how many** times | you repeat **until** something happens |
| counting through a range/list | waiting for a condition to change |

```python
import turtle                # square with while
t = turtle.Turtle()
steps = 1
while steps <= 4:
    t.forward(100)
    t.right(90)
    steps = steps + 1
turtle.done()
```

---

## Nested loops — a loop inside a loop 🪆

```python
for row in range(3):        # 3 rows
    for star in range(5):   # 5 stars per row
        print("*", end="")  # stay on the same line
    print()                 # newline after each row
```

**Output:**
```
*****
*****
*****
```

> 🧠 The **inner** loop finishes completely for **each** turn of the **outer** loop.

---

## 🏆 Challenge — Draw the Sun ☀️

```python
import turtle
t = turtle.Turtle()
t.shape("turtle"); t.pencolor("orange"); t.fillcolor("yellow")
t.begin_fill()
t.circle(100)            # the sun's body
t.end_fill()

for _ in range(18):      # 18 rays around the sun
    t.right(90)
    t.forward(90)
    t.backward(90)
    t.left(90)
    t.circle(100, 20)    # move along to the next ray spot
turtle.done()
```

> 🌟 `_` is a loop variable we don't need — it just says "just counting."
🎯 try `range(36)` for more rays • change ray length `90`.

---

## 🐞 Debugging Corner

| Oops | Fix |
|---|---|
| program never stops (frozen) | `while` counter isn't changing — add `x = x + 1` |
| `range(5)` gave 0–4, not 1–5 | use `range(1, 6)` |
| nested loop prints one long line | add a `print()` after the inner loop |
| shape's rays overlap | check `forward`/`backward` distances match |

---

## 📒 Wrap-up

- `range(start, stop, step)` — starts at 0, stops **before** stop
- A `for` loop can walk a **list**; an **accumulator** keeps a running total
- A `while` loop repeats **until** false — change the counter!
- **Nested loops** = a loop inside a loop, great for grids & patterns

---

## 🏠 Take-home Assignment 4

1. Print the **5-times table** up to 5 × 12.
2. Use a `while` loop to print numbers **10 down to 1**.
3. Use **nested loops** to print a star triangle:
   ```
   *
   **
   ***
   ****
   ```
4. **Bonus:** add up all numbers 1 to 100 and print the total.

---

<!-- _class: lead -->

# 🎉 Great work!

➡️ **Next up:** Session 5 — The Turtle Map, Functions & Animation 🗺️
