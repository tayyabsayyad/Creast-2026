# 🔁 Session 4 — Loops Deep Dive (`for` & `while`)

> ⬅️ [Session 3](session-3.md) &nbsp;|&nbsp; 🏠 [Home](README.md) &nbsp;|&nbsp; Next ➡️ [Session 5: The Turtle Map & Animation](session-5.md)
>
> ⏱️ **Duration:** 3 hours &nbsp;•&nbsp; 🎚️ **Level:** Intermediate &nbsp;•&nbsp; 💻 **Lots of hands-on!**

### 🎯 Learning objectives
- [ ] Use `range(start, stop, step)` confidently
- [ ] Loop through a **list**
- [ ] Build an **accumulator** (a running total)
- [ ] Write a **`while`** loop with a counter — and avoid **infinite loops**
- [ ] Use **nested loops** to make patterns and turtle art

### 🗓️ 3-Hour Plan
| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Recall: if/elif + "climb 200 stairs" story |
| 0:15–0:50 | 📖 `for` loop in depth (range, lists, totals) |
| 0:50–1:25 | 💻 **Lab A:** tables, countdown, polygon family |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 📖 `while` loops + nested loops |
| 2:10–2:45 | 🏆 Challenge: draw the Sun ☀️ |
| 2:45–3:00 | 📒 Recap + assignment |

---

## 🔔 Warm-up (15 min)
Recall the voting check from last session. Then the **robot story**: *"Tell a robot to
climb 200 stairs — left leg up, forward, down, right leg up, forward, down…"* — would you
write that 200 times? 😵 **No!** That's what loops are for.

```python
age = int(input("Enter age: "))
if age < 18:
    print("go home")
elif age == 18:
    print("congrats")
else:
    print("go vote")
```

---

## 🔢 Part 1 — The `for` loop, up close (Concept Block A)

`range()` builds a sequence of numbers for the loop to walk through.

```python
for x in range(4):
    print(x)
```
**Output:** `0  1  2  3`  → 😲 starts at **0**, stops **before** 4!

| `range(...)` | Numbers |
|---|---|
| `range(4)` | 0, 1, 2, 3 |
| `range(1, 5)` | 1, 2, 3, 4 |
| `range(2, 11, 2)` | 2, 4, 6, 8, 10 (step of 2) |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 (counting down) |

### Looping a list
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print("I like", x)
```

### Accumulator — a running total 🧮
```python
total = 0
for n in range(1, 6):    # 1..5
    total = total + n    # keep adding
print("Total is", total)
```
🔮 What's the total? <details><summary>👉</summary>`15` (1+2+3+4+5). The `total` box grows each loop. 🧮</details>

---

## 💻 Lab A — Loop drills (35 min)

**A1. Multiplication table**
```python
num = int(input("Which table? "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```
🎯 *Make it yours:* print only **even** results, or tables for 2 *and* 3.

**A2. Rocket countdown** 🚀
```python
for n in range(5, 0, -1):
    print(n)
print("Blast off! 🚀")
```

**A3. Polygon family** — one loop, many shapes:
```python
import turtle
t = turtle.Turtle()
sides = 6                 # try 3, 4, 5, 8...
for i in range(sides):
    t.forward(80)
    t.left(360 / sides)
turtle.done()
```

**✅ Checkpoint:** everyone printed a times-table and drew at least one polygon.

---

## ☕ Break (10 min)

---

## ⏳ Part 2 — `while` loops & nested loops (Concept Block B)

A **`while`** loop repeats *as long as* a condition is true (Hindi: **जब तक** — "until").

```python
punch = 1
while punch <= 3:
    print("puuuunncccchhhhh")
    punch = punch + 1      # 🔑 the counter MUST change
```
**Output:** prints "punch" 3 times.

> ⚠️ **Infinite-loop danger!** Forget `punch = punch + 1` and the loop never stops. 😱
> Every `while` needs something that eventually makes the condition **False**.

### `for` vs `while` — when to use which?
| Use a `for` loop when… | Use a `while` loop when… |
|---|---|
| you know **how many** times | you repeat **until** something happens |
| counting through a range/list | waiting for a condition to change |

### Draw a square with `while`
```python
import turtle
t = turtle.Turtle()
steps = 1
while steps <= 4:
    t.forward(100)
    t.right(90)
    steps = steps + 1
turtle.done()
```

### Nested loops — a loop inside a loop 🪆
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

## 🏆 Challenge (35 min) — Draw the Sun ☀️

Build it step by step. First the body, then **loop** the rays:
```python
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.pencolor("orange")
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)            # the sun's body
t.end_fill()

for _ in range(18):      # 18 rays around the sun
    t.right(90)
    t.forward(90)
    t.backward(90)
    t.left(90)
    t.circle(100, 20)    # move along the circle to the next ray spot
turtle.done()
```
> 🌟 `_` is a loop variable we don't need to use — coders name it `_` to say "just counting."

🎯 *Extensions:* try `range(36)` for more rays • change ray length `90` • make a **spiral**
with a nested idea: `for i in range(50): t.forward(i); t.left(20)`.

---

## 🐞 Debugging Corner
| Oops | Fix |
|---|---|
| program never stops (frozen) | your `while` counter isn't changing — add `x = x + 1` |
| `range(5)` gave 0–4, not 1–5 | use `range(1, 6)` |
| nested loop prints one long line | add a `print()` after the inner loop |
| shape's rays overlap | check the `forward`/`backward` distances match |

---

## 📒 Wrap-up (5 min)
- `range(start, stop, step)` — starts at 0 by default, stops **before** stop
- A `for` loop can walk a **list**; an **accumulator** keeps a running total
- A `while` loop repeats **until** a condition is false — change the counter!
- **Nested loops** = a loop inside a loop, great for grids and patterns

## 🏠 Take-home Assignment 4
1. Print the **5-times table** up to 5 × 12.
2. Use a `while` loop to print numbers **10 down to 1**.
3. Use **nested loops** to print a triangle of stars:
   ```
   *
   **
   ***
   ****
   ```
4. **Bonus:** add up all numbers from 1 to 100 with a loop and print the total.

<details><summary>🔑 Facilitator answer key</summary>

```python
# Q2
n = 10
while n >= 1:
    print(n)
    n = n - 1

# Q3
for row in range(1, 5):
    for star in range(row):
        print("*", end="")
    print()

# Q4
total = 0
for n in range(1, 101):
    total = total + n
print(total)        # 5050
```
</details>

<details><summary>🧑‍🏫 Facilitator notes</summary>

- **Infinite loops will happen** — that's a teaching moment, not a disaster. Show how to
  stop the program, then find the missing counter line together.
- Nested loops are the hardest idea today — use the **star grid** and physically point at
  "inner finishes for each outer."
- **Fast finishers:** the spiral extension and Q4 sum.
- **Support:** Q1 and Q2 are enough for strugglers; the star triangle is the stretch.
- Connect back: "the Sun's rays are just a loop, like the polygon."
</details>

➡️ **Next up:** [Session 5 — The Turtle Map & Animation](session-5.md)
