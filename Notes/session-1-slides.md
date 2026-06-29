---
marp: true
theme: default
paginate: true
size: 16:9
backgroundColor: #fffdf7
header: '🐢 Session 1 — Meet the Computer & Your First Turtle'
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

# 🐢 Session 1
## Meet the Computer & Your First Turtle

⏱️ **3 hours** &nbsp;•&nbsp; 🎚️ **Absolute beginner** &nbsp;•&nbsp; 💻 **Lots of hands-on!**

---

## 🎯 By the end, you can…

- ✅ Explain what a computer does (**input → process → output**)
- ✅ Say **why** we need a programming language
- ✅ Use `print()` to show messages and `#` comments to leave notes
- ✅ Store values in **variables** and do math with them
- ✅ Read user input with `input()` and convert with `int()` / `float()`
- ✅ Draw lines and shapes with the **turtle**

---

## 🗓️ The 3-Hour Plan

| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Warm-up: Housie / "Used a computer?" |
| 0:15–0:50 | 📖 What is a computer + how we talk to it |
| 0:50–1:25 | 💻 **Lab A:** print, variables, calculator |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 📖 Meet the turtle + 💻 **Lab B:** shapes |
| 2:10–2:45 | 🏆 Challenge: initials + happy face |
| 2:45–3:00 | 📒 Recap + take-home assignment |

---

<!-- _class: lead -->

# 🔔 Warm-up

Quick round of **Housie** with tech words
*(Python, Turtle, CPU, Binary, Keyboard…)*

> 💬 Have you used a computer? **When? Where? Why?**
> Point to the **CPU, monitor, mouse, keyboard** — what is each for?

---

## 🤖 What is a computer?

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
| Tasty shake comes out | **Output** (info comes out) |

---

## 🤔 Discuss!

> A **calculator**, a **video game**, and a **weather app** —
> what is the *input*, *process*, and *output* for each?

🗣️ *Let students shout answers!*

---

## 🗣️ How do we talk to a computer?

Tell the computer *"open paint!"* in English or Hindi… ❌ it won't understand!

- Computers only understand **0s and 1s** (**binary**) 🔢
- Writing 0s and 1s by hand is *super* hard for humans
- ✅ So we use a **programming language** — **Python** — as the middle language

> 🧠 **Coding / Programming** = giving the computer a clear list of instructions.

---

## ⚙️ How does our code run?

```
You WRITE code → press RUN → computer DOES it → you SEE the result
```

We'll write in a **Python sandbox** (online):

- 📝 **Text mode** — for words & numbers
- 🐢 **Turtle mode** — for drawings

---

## ⌨️ `print()` — make the computer *say* something

```python
print("Hello, world!")
```
**Output:** `Hello, world!`

Print **several things** at once, separated by commas:

```python
print("My name is", "Asha", "and I am", 10, "years old")
```
**Output:** `My name is Asha and I am 10 years old`

> 💡 Commas add a **space** automatically between items. Handy!

---

## `#` comments — notes for humans

```python
# This line is a note. Python ignores it.
print("Python skips the line above")   # note at the end too
```

> 🧠 Comments don't change what the program does —
> they just **explain** it to people.

---

## 📦 Variables — labelled boxes that store a value

```python
num1 = 15        # a box called num1 holds 15
num2 = 6         # a box called num2 holds 6
total = num1 + num2
print("sum =", total)
```

🔮 **Predict the output!**

<!-- Reveal on click in class -->
👉 `sum = 21` &nbsp; (because 15 + 6 = 21) 🎉

---

## 📛 Naming rules for boxes

- ✅ use clear names: `age`, `score`, `total`
- ✅ no spaces — use `first_name`, not `first name`
- ❌ don't use Python's special words like `print` or `sum`
- ⚠️ `Age` and `age` are **different** boxes — capitals matter!

---

## ❓ `input()` — ask the user a question

```python
name = input("What is your name? ")
print("Hello,", name, "! Welcome 🎉")
```

> ⚠️ **Big idea:** `input()` **always** gives back **text**,
> even if you type `5`.

---

## 🔢 Convert text into numbers

```python
x = input("Type a number: ")
y = input("Type another number: ")
total = int(x) + int(y)      # int() turns text "5" into number 5
print("The sum is:", total)
```

🔮 **What if we forget `int()`** and type `5` and `3`?

👉 You'd get `53`, not `8`! Without `int()`, Python glues the **text**:
`"5" + "3"` → `"53"`

**The 3 converters:** `int()` whole • `float()` decimal • `str()` text

---

<!-- _class: lead -->

# 💻 Lab A
## Hands-on (35 min) · *Text mode*

> 🛠️ Type each program, **run it**,
> then do the "Make it yours" change.

---

## A1. Greeter

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hi", name + "!", "Next year you will be", int(age) + 1)
```

🎯 *Make it yours:* also ask their favourite colour and print it.

---

## A2. Two-number calculator

```python
a = int(input("First number: "))
b = int(input("Second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
```

🎯 *Make it yours:* add a line printing the **remainder** using `a % b`.

> ✅ **Checkpoint:** Everyone has run A1 and A2 and seen real output.
> Help anyone stuck on quotes `" "` or brackets `( )`.

---

<!-- _class: lead -->

# ☕ Break (10 min)

---

## 🐢 Meet the Turtle!

The **turtle** is an imaginary pen 🖍️. You give it commands and it draws on screen.

```python
import turtle          # bring in the turtle tools

t = turtle.Turtle()    # 't' is our turtle
t.shape("turtle")      # make it look like a turtle
t.color("red")         # paint it red
t.forward(100)         # walk forward 100 steps, drawing

turtle.done()          # keep the window open
```

> 🔑 Every turtle program starts with `import turtle` + `t = turtle.Turtle()`
> and ends with `turtle.done()`. **Memorise this skeleton!**

---

## 🤖 The four movement commands

*Act them out with your body!*

| Command | Turtle does |
|---|---|
| `t.forward(100)` | walk ahead 100 steps |
| `t.backward(100)` | walk back 100 steps |
| `t.left(90)` | spin left 90° |
| `t.right(90)` | spin right 90° |

---

<!-- _class: lead -->

# 💻 Lab B
## Shape gallery (35 min) · *Turtle mode*

---

## B1. A dot & a line

```python
import turtle
t = turtle.Turtle()
t.dot(20, "red")     # a dot
t.forward(150)       # a line
turtle.done()
```

---

## B2. A square 🟥

```python
import turtle
t = turtle.Turtle()
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
turtle.done()
```

> 💡 Notice we typed the **same two lines 4 times**.
> Next session we'll learn a magic shortcut called a **loop**! 🔁

---

## B3. A triangle 🔺

```python
import turtle
t = turtle.Turtle()
t.forward(100); t.left(120)
t.forward(100); t.left(120)
t.forward(100); t.left(120)
turtle.done()
```

🔮 **Why 120°, not 90°?**
👉 A triangle's outside turns add up to 360°, and 360 ÷ 3 = 120.
*(A square: 360 ÷ 4 = 90!)* 📐

> ✅ **Checkpoint:** Everyone has a square **and** a triangle on screen.

---

<!-- _class: lead -->

# 🏆 Challenge (35 min)

Pick one (or do both!)

---

## Challenge 1 — Your initials ✍️

Draw the first letter of your name using
`forward`, `left`, `right`, and `t.goto()`.

## Challenge 2 — A happy face 🙂

```python
import turtle
t = turtle.Turtle()
t.circle(80)                                          # face
t.penup(); t.goto(-30, 100); t.pendown(); t.dot(15)   # left eye
t.penup(); t.goto(30, 100);  t.pendown(); t.dot(15)   # right eye
t.penup(); t.goto(-40, 60); t.pendown()
t.setheading(-60); t.circle(50, 120)                  # smile
turtle.done()
```

🎯 *Extensions:* give the face a colour, add a nose dot, make it bigger.

---

## 🐞 Debugging Corner — fix these!

| Oops | Fix |
|---|---|
| `print(Hello)` | put text in quotes → `print("Hello")` |
| `print("Hi"` | close the bracket → `print("Hi")` |
| turtle window flashes & closes | add `turtle.done()` at the end |
| `5 + "3"` error | convert: `5 + int("3")` |

---

## 📒 Wrap-up

- Computer = **input → process → output** 🥤
- We use **Python** because computers only know 0s and 1s
- `print()` shows • variables store • `input()` asks • `int()`/`float()` convert
- The turtle draws with `forward`, `left`, `right`, `dot`, `circle`
- Always end turtle programs with `turtle.done()`

---

## 🏠 Take-home Assignment 1

1. **Text mode:** write code to **subtract 5 from 25** and print the answer.
2. **Text mode:** ask for two numbers and print their **product**.
3. **Turtle mode:** show the turtle in **your favourite colour**.
4. **Bonus:** draw a **rectangle** (hint: sides 150, 80, 150, 80).

---

<!-- _class: lead -->

# 🎉 Great work!

➡️ **Next up:** Session 2 — Pen Magic & Loops 🔁
