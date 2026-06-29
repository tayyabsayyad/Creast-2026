---
marp: true
theme: default
paginate: true
size: 16:9
backgroundColor: #fffdf7
header: '🔢 Session 3 — Data Types, Operators & If/Else'
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

# 🔢 Session 3
## Data Types, Operators & If/Else

⏱️ **3 hours** &nbsp;•&nbsp; 🎚️ **Beginner+** &nbsp;•&nbsp; 💻 **Lots of hands-on!**

---

## 🎯 By the end, you can…

- ✅ Tell apart **int**, **float**, **string** — and convert between them
- ✅ Use **arithmetic**, **comparison**, **assignment** operators
- ✅ Understand **modulo `%`** and use it for even/odd
- ✅ Read/write **Booleans** and combine with `and` / `or` / `not`
- ✅ Make decisions with **`if` / `elif` / `else`**

---

## 🗓️ The 3-Hour Plan

| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Recall game (operators flashcards) |
| 0:15–0:50 | 📖 Data types + operators |
| 0:50–1:25 | 💻 **Lab A:** calculator, area, even/odd |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 📖 Booleans + if/elif/else |
| 2:10–2:45 | 🏆 Challenge: grade checker + traffic light |
| 2:45–3:00 | 📒 Recap + assignment |

---

<!-- _class: lead -->

# 🔔 Warm-up

Flash an operator → students **shout its meaning**:
`*` (times) · `%` (remainder) · `==` (equal?) · `!=` (not equal)

> ⚡ Lightning round:
> *"Is 7 bigger than 3? Is 4 equal to 4?"*

---

## 📦 Data Types

A **data type** is the *kind of value* a variable holds.

| Type | Means | Examples |
|---|---|---|
| **int** | whole numbers | `5`, `-10`, `0` |
| **float** | with a decimal | `3.14`, `-0.5`, `2.0` |
| **string** | text in quotes | `"Alice"`, `'hi'` |

```python
print(type(5))        # <class 'int'>
print(type(5.0))      # <class 'float'>
print(type("5"))      # <class 'str'>   ← text, not a number!
```

---

## 🔄 Converting between types

```python
age_text = "12"          # text
age = int(age_text)      # now a number → 12
price = float("9.5")     # → 9.5
score_text = str(100)    # number → text "100"
```

> ⚠️ This is **why** we wrote `int(input(...))` —
> input is always text, and you can't do math on text.

---

## ➕ Arithmetic operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | add | `5 + 3` → `8` |
| `-` | subtract | `10 - 4` → `6` |
| `*` | multiply | `2 * 7` → `14` |
| `/` | divide | `12 / 5` → `2.4` |
| `**` | power | `2 ** 3` → `8` |
| `%` | remainder (modulo) | `9 % 4` → `1` |

> 🤓 **Order of operations:** `*` `/` before `+` `-`. `2 + 3 * 4` = `14`.
> 🎯 **`%` is the leftover** — even numbers have `% 2 == 0`.

---

## ❓ Comparison operators

Ask a yes/no question:

| Operator | Meaning |
|---|---|
| `==` | equal to |
| `!=` | not equal to |
| `<` `>` | less / greater than |
| `<=` `>=` | less / greater than or equal |

> ⚠️ **`=` vs `==`** — one `=` **stores** (`x = 5`); two `==` **ask** (`x == 5`).
> Mixing them up is the #1 beginner bug!

---

## 💻 Lab A — A1. Full calculator

```python
a = float(input("First number: "))
b = float(input("Second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("Remainder:", a % b)
```

---

## A2. Area · A3. Even or odd

```python
length = float(input("Enter length: "))    # A2
width = float(input("Enter width: "))
area = length * width
print("Area =", area)
```
🔮 length `4`, width `5` → 👉 `Area = 20.0` (a float!) 🎯

```python
number = int(input("Enter a number: "))    # A3
print("Remainder when divided by 2 is:", number % 2)
```
> ✅ **Checkpoint:** everyone saw a decimal result from `/`.

---

<!-- _class: lead -->

# ☕ Break (10 min)

---

## 🤔 Booleans — True or False

```python
x = 5
y = 10
print(x < y)      # True
print(x == y)     # False
```

🔮 Will `x < y` print `5` or `True`?
👉 **`True`** — comparisons answer yes/no, not numbers. ✅

---

## Combining with `and` / `or` / `not`

```python
age = 15
print(age > 10 and age < 18)   # True  (both must be true)
print(age < 5 or age > 12)     # True  (at least one true)
print(not (age == 15))         # False (flips it)
```

> 🧠 `and` = both • `or` = at least one • `not` = the opposite.

---

## `if` / `elif` / `else` — making choices

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if b > a:
    print("b is greater than a")
elif a > b:
    print("a is greater than b")
else:
    print("a and b are equal")
```

- **`if`** → runs when its condition is `True`
- **`elif`** → "else if" — another condition
- **`else`** → runs when nothing matched

> 🔑 Each line ends with `:` and its block is **indented**. First match wins.

---

## Finish A3 as a real decision

```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")
```

🔮 input `6` → 👉 `number is even` (because `6 % 2 == 0`). 🟢

---

## 💻 Lab B — B1. Spiral patterns 🌀

```python
import turtle
t = turtle.Turtle()
t.shape("turtle"); t.color("red")
for x in range(13):
    t.forward(200)
    t.left(150)
turtle.done()
```

🎯 Try `range(100)` with `t.left(175)` and `t.speed(0)` — mesmerising!

---

## B2. Traffic light (decisions + turtle)

```python
import turtle
t = turtle.Turtle()
t.speed(5)
color = "red"          # try "yellow" or "green"
t.penup()
if color == "red":
    t.color("red")
elif color == "yellow":
    t.color("yellow")
elif color == "green":
    t.color("green")
t.pendown()
t.begin_fill(); t.circle(20); t.end_fill()
turtle.done()
```

---

## 🏆 Challenge — Grade checker

```python
marks = int(input("Enter marks (0-100): "))
if marks >= 90:
    print("Grade A 🌟")
elif marks >= 70:
    print("Grade B 👍")
elif marks >= 40:
    print("Grade C 🙂")
else:
    print("Fail — try again 💪")
```

🎯 *Extensions:* add "Grade A+" for `>= 95` • print "invalid" if marks > 100 or < 0.

---

## 🐞 Debugging Corner

| Oops | Fix |
|---|---|
| `if x = 5:` | use `==` → `if x == 5:` |
| `if x > 5` (no colon) | add `:` |
| code after `if` not indented | indent the block |
| comparing text to number | convert with `int()` first |

---

## 📒 Wrap-up

- **int / float / string** are different types; `int() float() str()` convert
- Operators: `+ - * / ** %` (math) and `== != < >` (compare)
- **Booleans** are `True`/`False`; combine with `and` / `or` / `not`
- **`if` / `elif` / `else`** choose what to do — colon + indentation required

---

## 🏠 Take-home Assignment 3

1. Ask for a **temperature**: `Hot` if > 30, `Cold` if < 10, else `Pleasant`.
2. Ask for two names → print whether **same** or **different**.
3. Ask for a number → print **positive, negative, or zero**.
4. **Bonus:** circle that is **green if even**, **red if odd**.

---

<!-- _class: lead -->

# 🎉 Great work!

➡️ **Next up:** Session 4 — Loops Deep Dive (`for` & `while`) 🔁
