# 🖍️ Session 2 — MCQ Test

> **Topic:** Pen Magic & Loops
> **Total:** 10 questions × 1 mark = 10 marks &nbsp;•&nbsp; ⏱️ 15 min
>
> Name: ______________________  Date: ____________

---

**1. What does `t.penup()` do?**
- A) Makes the line thicker
- B) Lifts the pen so the turtle moves without drawing
- C) Changes the pen colour
- D) Ends the program

**2. Which command makes the turtle's line thicker?**
- A) `t.pensize(5)`
- B) `t.speed(5)`
- C) `t.bigpen()`
- D) `t.thick(5)`

**3. Which is a correct way to set a colour using a hex code?**
- A) `t.pencolor(FF5733)`
- B) `t.pencolor("#FF5733")`
- C) `t.pencolor(hex 5733)`
- D) `t.colorcode(255)`

**4. To colour the inside of a shape, you must use…**
- A) only `begin_fill()`
- B) only `end_fill()`
- C) both `begin_fill()` and `end_fill()`
- D) `t.color()` only

**5. What does the "DRY" rule mean?**
- A) Don't Run Yet
- B) Don't Repeat Yourself
- C) Double Run Year
- D) Draw Right Yourself

**6. How many times does this loop run?**
```python
for i in range(4):
    t.forward(100)
    t.left(90)
```
- A) 1
- B) 4
- C) 90
- D) 100

**7. What is missing for this loop to work?**
```python
for i in range(3)
    print("Hello")
```
- A) A colon `:` after `range(3)`
- B) Quotes around `range`
- C) Another `for`
- D) Nothing, it works

**8. Why must the lines inside a loop be indented?**
- A) To make the code look pretty
- B) So Python knows which lines are *inside* the loop
- C) Indentation is optional in Python
- D) To make the program run faster

**9. In the polygon code below, what shape do you get with `sides = 3`?**
```python
sides = 3
angle = 360 / sides
for i in range(sides):
    t.forward(80)
    t.left(angle)
```
- A) A square
- B) A circle
- C) A triangle
- D) A hexagon

**10. Which spelling does Python accept for colour commands?**
- A) `t.colour("red")`
- B) `t.color("red")`
- C) `t.Color("red")`
- D) `t.COLOUR("red")`

---

<details><summary>🔑 Answer Key (teacher)</summary>

| Q | Ans | Why |
|---|---|---|
| 1 | **B** | `penup()` lifts the pen — move without drawing |
| 2 | **A** | `pensize()` sets line thickness |
| 3 | **B** | Hex colours go in quotes with a `#` |
| 4 | **C** | Fill is a sandwich: begin_fill … end_fill |
| 5 | **B** | DRY = Don't Repeat Yourself |
| 6 | **B** | `range(4)` repeats 4 times |
| 7 | **A** | Every `for` line ends with a colon `:` |
| 8 | **B** | Indentation marks the loop body |
| 9 | **C** | 3 sides, 360/3 = 120° turns = triangle |
| 10 | **B** | Python uses the American spelling `color` |

**Score: ___ / 10**
</details>
