# 🐢 Session 1 — Meet the Computer & Your First Turtle

> 🏠 [Home](README.md) &nbsp;|&nbsp; Next ➡️ [Session 2: Pen Magic & Loops](session-2.md)
>
> ⏱️ **Duration:** 3 hours &nbsp;•&nbsp; 🎚️ **Level:** Absolute beginner &nbsp;•&nbsp; 💻 **Lots of hands-on!**

### 🎯 Learning objectives — by the end, students can…
- [ ] Explain what a computer does (**input → process → output**)
- [ ] Say **why** we need a programming language
- [ ] Use `print()` to show messages and `#` comments to leave notes
- [ ] Store values in **variables** and do math with them
- [ ] Read user input with `input()` and convert it with `int()` / `float()`
- [ ] Draw lines and basic shapes with the **turtle**

### 🗓️ 3-Hour Plan at a glance
| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Warm-up: Housie / "Have you used a computer?" |
| 0:15–0:50 | 📖 What is a computer + how we talk to it |
| 0:50–1:25 | 💻 **Lab A:** print, variables, a calculator |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 📖 Meet the turtle + 💻 **Lab B:** shapes |
| 2:10–2:45 | 🏆 Challenge: draw your initials + a happy face |
| 2:45–3:00 | 📒 Recap + take-home assignment |

---

## 🔔 Warm-up (15 min)

Play a quick round of **Housie** with tech words (Python, Turtle, CPU, Binary, Keyboard…)
to get everyone excited. Then ask the room:

> 💬 **Have you used a computer? When? Where? Why?**
> Point to the **CPU, monitor, mouse, keyboard** — what is each one for?

---

## 🤖 Part 1 — What is a computer? (Concept Block A)

A **computer** is a machine that:

```
   INPUT  ➡️   PROCESS   ➡️   OUTPUT
 (you give)  (it thinks)   (it shows)
```

🥤 **The banana milkshake!**
| Milkshake | Computer |
|---|---|
| Put banana + milk + sugar | **Input** (you give data) |
| Mixer spins | **Process** (work happens) |
| Tasty shake comes out | **Output** (information comes out) |

> 💬 **Discuss:** A calculator, a video game, and a weather app — what is the *input*,
> *process*, and *output* for each? (Let students shout answers!)

### 🗣️ How do we talk to a computer?

Tell the computer *"open paint!"* in English or Hindi… ❌ it won't understand!

- Computers only understand **0s and 1s** (called **binary**). 🔢
- Writing 0s and 1s by hand is *super* hard for humans.
- ✅ So we use a **programming language** — **Python** — as the middle language:
  easy for us to read, and the computer can follow it.

> 🧠 **Coding / Programming** = giving the computer a clear list of instructions.

### How does our code actually run?
```
You WRITE code  →  press RUN  →  computer DOES it  →  you SEE the result
```
We'll write in a **Python sandbox** (online) — **Text mode** for words/numbers, and
**Turtle mode** for drawings.

---

## ⌨️ Part 2 — Your first Python words

### `print()` — make the computer *say* something
```python
print("Hello, world!")
```
**Output:** `Hello, world!`

You can print **several things** at once, separated by commas:
```python
print("My name is", "Asha", "and I am", 10, "years old")
```
**Output:** `My name is Asha and I am 10 years old`

> 💡 Commas add a **space** automatically between items. Handy!

### `#` comments — notes for humans
```python
# This line is a note. Python ignores it.
print("Python skips the line above")   # you can also note at the end of a line
```
> 🧠 Comments don't change what the program does — they just **explain** it to people.

### Variables — labelled boxes that store a value 📦
```python
num1 = 15        # a box called num1 holds 15
num2 = 6         # a box called num2 holds 6
total = num1 + num2
print("sum =", total)
```
🔮 **Predict the output!**
<details><summary>👉 Answer</summary>

`sum = 21` &nbsp; (because 15 + 6 = 21) 🎉
</details>

**📛 Naming rules for boxes:**
- ✅ use clear names: `age`, `score`, `total`
- ✅ no spaces — use `first_name`, not `first name`
- ❌ don't use Python's special words like `print` or `sum` as box names
- ⚠️ `Age` and `age` are **different** boxes (capital letters matter!)

### `input()` — ask the user a question
```python
name = input("What is your name? ")
print("Hello,", name, "! Welcome 🎉")
```

> ⚠️ **Big idea:** `input()` **always** gives back **text**, even if you type `5`.

```python
x = input("Type a number: ")
y = input("Type another number: ")
total = int(x) + int(y)      # int() turns text "5" into the number 5
print("The sum is:", total)
```
🔮 **What if we forget `int()`** and type `5` and `3`?
<details><summary>👉 Answer</summary>

You'd get `53`, not `8`! Without `int()`, Python glues the **text** together:
`"5" + "3"` → `"53"`. The `int()` makes them real numbers. 🔢
</details>

**The 3 converters:** `int()` → whole number • `float()` → decimal number • `str()` → text

---

## 💻 Lab A — Hands-on (35 min) · *Text mode*

> 🛠️ Type each program, **run it**, then do the "Make it yours" change.

**A1. Greeter**
```python
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hi", name + "!", "Next year you will be", int(age) + 1)
```
🎯 *Make it yours:* also ask their favourite colour and print it.

**A2. Two-number calculator**
```python
a = int(input("First number: "))
b = int(input("Second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
```
🎯 *Make it yours:* add a line that prints the **remainder** using `a % b`.

**✅ Checkpoint:** Everyone has run A1 and A2 and seen real output. Help anyone stuck on
quotes `" "` or missing brackets `( )`.

---

## ☕ Break (10 min)

---

## 🐢 Part 3 — Meet the Turtle! (Concept Block B)

The **turtle** is an imaginary pen 🖍️. You give it commands — *go forward, turn, change
colour* — and it draws on screen. Switch the sandbox to **Turtle mode** and try:

```python
import turtle          # bring in the turtle tools

t = turtle.Turtle()    # 't' is our turtle
t.shape("turtle")      # make it look like a turtle
t.color("red")         # paint it red
t.forward(100)         # walk forward 100 steps, drawing a line

turtle.done()          # keep the window open
```

> 🔑 **Every turtle program** starts with `import turtle` + `t = turtle.Turtle()` and
> ends with `turtle.done()`. Memorise this skeleton!

**The four movement commands** (act them out with your body! 🤖):
| Command | Turtle does |
|---|---|
| `t.forward(100)` | walk ahead 100 steps |
| `t.backward(100)` | walk back 100 steps |
| `t.left(90)` | spin left 90° |
| `t.right(90)` | spin right 90° |

---

## 💻 Lab B — Shape gallery (35 min) · *Turtle mode*

**B1. A small dot & a line**
```python
import turtle
t = turtle.Turtle()
t.dot(20, "red")     # a dot
t.forward(150)       # a line
turtle.done()
```

**B2. A square** 🟥
```python
import turtle
t = turtle.Turtle()
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
turtle.done()
```
> 💡 Notice we typed the **same two lines 4 times**. Remember this — next session we'll
> learn a magic shortcut called a **loop**! 🔁

**B3. A triangle** 🔺
```python
import turtle
t = turtle.Turtle()
t.forward(100); t.left(120)
t.forward(100); t.left(120)
t.forward(100); t.left(120)
turtle.done()
```
🔮 **Why 120°, not 90°?** <details><summary>👉</summary> A triangle's outside turns add up to 360°, and 360 ÷ 3 = 120. (A square: 360 ÷ 4 = 90!) 📐</details>

**✅ Checkpoint:** Everyone has a square **and** a triangle on screen.

---

## 🏆 Challenge (35 min)

**Pick one (or do both!):**

1. **Your initials** ✍️ — draw the first letter of your name using `forward`, `left`,
   `right`, and `t.goto()`.
2. **A happy face** 🙂
```python
import turtle
t = turtle.Turtle()
t.circle(80)                                   # face
t.penup(); t.goto(-30, 100); t.pendown(); t.dot(15)   # left eye
t.penup(); t.goto(30, 100);  t.pendown(); t.dot(15)   # right eye
t.penup(); t.goto(-40, 60); t.pendown()
t.setheading(-60); t.circle(50, 120)           # smile
turtle.done()
```
🎯 *Extensions for fast finishers:* give the face a colour, add a nose dot, make it bigger.

---

## 🐞 Debugging Corner — fix these!
| Oops | Fix |
|---|---|
| `print(Hello)` | put text in quotes → `print("Hello")` |
| `print("Hi"` | close the bracket → `print("Hi")` |
| turtle window flashes & closes | add `turtle.done()` at the end |
| `5 + "3"` error | convert: `5 + int("3")` |

---

## 📒 Wrap-up (5 min)
- Computer = **input → process → output** 🥤
- We use **Python** because computers only know 0s and 1s
- `print()` shows • variables store • `input()` asks • `int()`/`float()` convert
- The turtle draws with `forward`, `left`, `right`, `dot`, `circle`
- Always end turtle programs with `turtle.done()`

## 🏠 Take-home Assignment 1
1. **Text mode:** write code to **subtract 5 from 25** and print the answer.
2. **Text mode:** ask the user for two numbers and print their **product**.
3. **Turtle mode:** show the turtle in **your favourite colour**.
4. **Bonus:** draw a **rectangle** (hint: sides 150, 80, 150, 80).

<details><summary>🔑 Facilitator answer key (try first!)</summary>

```python
# Q1
print("answer is", 25 - 5)

# Q2
a = int(input("num 1: ")); b = int(input("num 2: "))
print("product is", a * b)

# Q3
import turtle
t = turtle.Turtle(); t.shape("turtle"); t.color("blue")
turtle.done()

# Q4 rectangle
import turtle
t = turtle.Turtle()
t.forward(150); t.left(90)
t.forward(80);  t.left(90)
t.forward(150); t.left(90)
t.forward(80);  t.left(90)
turtle.done()
```
</details>

<details><summary>🧑‍🏫 Facilitator notes — timing & tips</summary>

- **Watch for:** missing quotes, missing `( )`, capital-letter variable mismatches.
- **Common win:** changing the turtle's colour gets big smiles — let them explore colours.
- **Support:** pair a confident student with one who's slower at typing.
- **Fast finishers:** ask them to draw a **pentagon** (5 sides, turn 72°) — leads into loops.
- **Energy:** Lab B is the highlight; keep Part 1 snappy so you reach the turtle with energy.
</details>

➡️ **Next up:** [Session 2 — Pen Magic & Loops](session-2.md)
