# 🔢 Session 3 — Data Types, Operators & If/Else

> ⬅️ [Session 2](session-2.md) &nbsp;|&nbsp; 🏠 [Home](README.md) &nbsp;|&nbsp; Next ➡️ [Session 4: Loops Deep Dive](session-4.md)
>
> ⏱️ **Duration:** 3 hours &nbsp;•&nbsp; 🎚️ **Level:** Beginner+ &nbsp;•&nbsp; 💻 **Lots of hands-on!**

### 🎯 Learning objectives
- [ ] Tell apart **int**, **float**, and **string** — and convert between them
- [ ] Use **arithmetic**, **comparison**, and **assignment** operators
- [ ] Understand **modulo `%`** and use it for even/odd
- [ ] Read and write **Booleans** (`True`/`False`) and combine them with `and` / `or` / `not`
- [ ] Make decisions with **`if` / `elif` / `else`** and correct **indentation**

### 🗓️ 3-Hour Plan
| Time | What we do |
|---|---|
| 0:00–0:15 | 🔔 Recall game (operators flashcards) |
| 0:15–0:50 | 📖 Data types + operators |
| 0:50–1:25 | 💻 **Lab A:** calculator & area, even/odd |
| 1:25–1:35 | ☕ Break |
| 1:35–2:10 | 📖 Booleans + if/elif/else |
| 2:10–2:45 | 🏆 Challenge: grade checker + traffic light |
| 2:45–3:00 | 📒 Recap + assignment |

---

## 🔔 Warm-up (15 min)
Flash an operator, students shout its meaning: `*` (times), `%` (remainder), `==` (equal?),
`!=` (not equal). Then a lightning round: *"Is 7 bigger than 3? Is 4 equal to 4?"*

---

## 📦 Part 1 — Data Types & Operators (Concept Block A)

A **data type** is the *kind of value* a variable holds.

| Type | Means | Examples |
|---|---|---|
| **int** | whole numbers | `5`, `-10`, `0` |
| **float** | numbers **with** a decimal | `3.14`, `-0.5`, `2.0` |
| **string** | text in quotes | `"Alice"`, `'hi'` |

🔬 You can **ask** Python a value's type:
```python
print(type(5))        # <class 'int'>
print(type(5.0))      # <class 'float'>
print(type("5"))      # <class 'str'>   ← it's text, not a number!
```

### Converting between types
```python
age_text = "12"          # text
age = int(age_text)      # now a number → 12
price = float("9.5")     # → 9.5
score_text = str(100)    # number → text "100"
```
> ⚠️ This is **why** we wrote `int(input(...))` — input is always text, and you can't do
> math on text.

### ➕ Arithmetic operators
| Operator | Meaning | Example |
|---|---|---|
| `+` | add | `5 + 3` → `8` |
| `-` | subtract | `10 - 4` → `6` |
| `*` | multiply | `2 * 7` → `14` |
| `/` | divide | `12 / 5` → `2.4` |
| `**` | power | `2 ** 3` → `8` |
| `%` | remainder (modulo) | `9 % 4` → `1` |

> 🤓 **Order of operations:** Python does `*` and `/` **before** `+` and `-` — just like maths.
> `2 + 3 * 4` = `14`, not `20`. Use brackets to be sure: `(2 + 3) * 4` = `20`.

> 🎯 **`%` is the leftover.** `9 % 4 = 1`. It's perfect for "is this even?" — an even
> number has `% 2 == 0`.

### Comparison operators (ask a yes/no question)
| Operator | Meaning |
|---|---|
| `==` | equal to |
| `!=` | not equal to |
| `<` `>` | less / greater than |
| `<=` `>=` | less / greater than or equal |

> ⚠️ **`=` vs `==`** — one `=` **stores** (`x = 5`); two `==` **ask** (`x == 5`). Mixing
> them up is the #1 beginner bug!

---

## 💻 Lab A — Numbers in action (35 min)

**A1. Full calculator**
```python
a = float(input("First number: "))
b = float(input("Second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("Remainder:", a % b)
```

**A2. Area of a rectangle** 📐
```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area =", area)
```
🔮 length `4`, width `5` → output? <details><summary>👉</summary>`Area = 20.0` (a float, because of `float()`). 🎯</details>

**A3. Even or odd** (the `%` trick)
```python
number = int(input("Enter a number: "))
print("Remainder when divided by 2 is:", number % 2)
```
🎯 *Make it yours:* we'll turn this into a real decision after the break.

**✅ Checkpoint:** everyone ran the calculator and saw a decimal result from `/`.

---

## ☕ Break (10 min)

---

## 🤔 Part 2 — Booleans & Decisions (Concept Block B)

### Booleans — True or False
```python
x = 5
y = 10
print(x < y)      # True
print(x == y)     # False
```
🔮 will `x < y` print `5` or `True`? <details><summary>👉</summary>**`True`** — comparisons answer yes/no, not numbers. ✅</details>

### Combining conditions with `and` / `or` / `not`
```python
age = 15
print(age > 10 and age < 18)   # True  (both must be true)
print(age < 5 or age > 12)     # True  (at least one true)
print(not (age == 15))         # False (flips it)
```
> 🧠 `and` = both • `or` = at least one • `not` = the opposite.

### `if` / `elif` / `else` — making choices
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
- **`elif`** → "else if" — checks another condition
- **`else`** → runs when nothing above matched

> 🔑 Each condition line ends with **`:`** and its block is **indented**. Python checks
> them **top to bottom** and runs the **first** match only.

### Finish A3 as a real decision:
```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")
```
🔮 input `6` → ? <details><summary>👉</summary>`number is even` (because `6 % 2 == 0`). 🟢</details>

---

## 💻 Lab B + 🏆 Challenge (combined, 35 min)

**B1. Spiral patterns** — change the numbers, get new art:
```python
import turtle
t = turtle.Turtle()
t.shape("turtle"); t.color("red")
for x in range(13):
    t.forward(200)
    t.left(150)
turtle.done()
```
🎯 Try `range(100)` with `t.left(175)` and `t.speed(0)` — mesmerising! 🌀

**B2. Traffic light** (decisions + turtle):
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

**🏆 Challenge — Grade checker:**
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
🎯 *Extensions:* add a "Grade A+" for `>= 95` • print "invalid" if marks are above 100 or below 0.

---

## 🐞 Debugging Corner
| Oops | Fix |
|---|---|
| `if x = 5:` | use `==` to compare → `if x == 5:` |
| `if x > 5` (no colon) | add `:` |
| code after `if` not indented | indent the block |
| comparing text to number | convert with `int()` first |

---

## 📒 Wrap-up (5 min)
- **int / float / string** are different types; `int() float() str()` convert them
- Operators: `+ - * / ** %` (math) and `== != < >` (compare)
- **Booleans** are `True`/`False`; combine with `and` / `or` / `not`
- **`if` / `elif` / `else`** choose what to do — colon + indentation required

## 🏠 Take-home Assignment 3
1. Ask for a **temperature** and print: `Hot` if > 30, `Cold` if < 10, else `Pleasant`.
2. Ask for two names and print whether they are the **same** or **different**.
3. Ask for a number and print whether it is **positive, negative, or zero**.
4. **Bonus:** draw a circle that is **green if a number is even**, **red if odd**.

<details><summary>🔑 Facilitator answer key</summary>

```python
# Q1
temp = float(input("Temperature: "))
if temp > 30:
    print("Hot")
elif temp < 10:
    print("Cold")
else:
    print("Pleasant")

# Q3
n = int(input("Number: "))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")

# Q4
import turtle
n = int(input("Number: "))
t = turtle.Turtle()
if n % 2 == 0:
    t.color("green")
else:
    t.color("red")
t.begin_fill(); t.circle(50); t.end_fill()
turtle.done()
```
</details>

<details><summary>🧑‍🏫 Facilitator notes</summary>

- **Hammer `=` vs `==`** — show the error message that `if x = 5:` produces.
- Use the **flashcard warm-up** again at the break to re-energise.
- **Fast finishers:** ask them to add `and`/`or` to the grade checker (e.g. distinction band).
- **Support:** let strugglers do only the even/odd + traffic light; the grade checker is the stretch goal.
- Emphasise Python checks conditions **top-to-bottom and stops at the first match**.
</details>

➡️ **Next up:** [Session 4 — Loops Deep Dive (`for` & `while`)](session-4.md)
