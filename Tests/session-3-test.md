# 🔢 Session 3 — MCQ Test

> **Topic:** Data Types, Operators & If/Else
> **Total:** 10 questions × 1 mark = 10 marks &nbsp;•&nbsp; ⏱️ 15 min
>
> Name: ______________________  Date: ____________

---

**1. Which value is a `float`?**
- A) `5`
- B) `"hello"`
- C) `3.14`
- D) `True`

**2. What does `type("5")` tell you?**
- A) It's an `int`
- B) It's a `str` (string / text)
- C) It's a `float`
- D) It's a `bool`

**3. Which function turns the text `"12"` into the number `12`?**
- A) `str("12")`
- B) `float("12")`
- C) `int("12")`
- D) `text("12")`

**4. What is the result of `9 % 4`?**
- A) `2`
- B) `1`
- C) `2.25`
- D) `36`

**5. What does `2 + 3 * 4` equal in Python?**
- A) `20`
- B) `14`
- C) `24`
- D) `9`

**6. Which operator *asks* "are these equal?"**
- A) `=`
- B) `==`
- C) `=!`
- D) `><`

**7. What does this print?**
```python
x = 5
y = 10
print(x < y)
```
- A) `5`
- B) `10`
- C) `True`
- D) `False`

**8. What does `not (age == 15)` give when `age = 15`?**
- A) `True`
- B) `False`
- C) `15`
- D) Error

**9. What does this code print when the input is `6`?**
```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")
```
- A) `number is even`
- B) `number is odd`
- C) `6`
- D) Error

**10. In `if / elif / else`, how does Python check the conditions?**
- A) Bottom to top, runs all matches
- B) Top to bottom, runs the *first* match only
- C) In a random order
- D) Only the `else` runs

---

<details><summary>🔑 Answer Key (teacher)</summary>

| Q | Ans | Why |
|---|---|---|
| 1 | **C** | A float has a decimal point |
| 2 | **B** | Quotes make it text (a string) |
| 3 | **C** | `int()` converts text to a whole number |
| 4 | **B** | 9 ÷ 4 = 2 remainder **1** |
| 5 | **B** | `*` happens before `+`: 3×4=12, +2 = 14 |
| 6 | **B** | `==` compares; `=` stores |
| 7 | **C** | A comparison answers True/False |
| 8 | **B** | `age == 15` is True, `not True` = False |
| 9 | **A** | 6 % 2 == 0, so it's even |
| 10 | **B** | Top to bottom, stops at the first match |

**Score: ___ / 10**
</details>
