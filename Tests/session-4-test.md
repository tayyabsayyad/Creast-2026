# 🔁 Session 4 — MCQ Test

> **Topic:** Loops Deep Dive (`for` & `while`)
> **Total:** 10 questions × 1 mark = 10 marks &nbsp;•&nbsp; ⏱️ 15 min
>
> Name: ______________________  Date: ____________

---

**1. What does `range(4)` produce?**
- A) 1, 2, 3, 4
- B) 0, 1, 2, 3
- C) 0, 1, 2, 3, 4
- D) 4, 3, 2, 1

**2. What numbers does `range(2, 11, 2)` give?**
- A) 2, 3, 4, 5, 6
- B) 2, 4, 6, 8, 10
- C) 2, 11, 2
- D) 1, 2, 3 … 11

**3. What does this print?**
```python
for n in range(5, 0, -1):
    print(n)
```
- A) 0 1 2 3 4
- B) 1 2 3 4 5
- C) 5 4 3 2 1
- D) 5 4 3 2 1 0

**4. What is the value of `total` after this loop?**
```python
total = 0
for n in range(1, 6):
    total = total + n
```
- A) `6`
- B) `15`
- C) `21`
- D) `5`

**5. A `while` loop keeps running…**
- A) exactly 10 times
- B) as long as its condition is True
- C) only once
- D) forever, always

**6. What causes an *infinite loop* in a `while` loop?**
- A) Using `range()`
- B) The counter never changes, so the condition stays True
- C) Forgetting to import turtle
- D) Using too many colours

**7. When should you use a `for` loop instead of a `while` loop?**
- A) When you know *how many* times to repeat
- B) When you wait *until* something happens
- C) Never use `for`
- D) Only for turtles

**8. What does this nested loop print?**
```python
for row in range(2):
    for star in range(3):
        print("*", end="")
    print()
```
- A) `**` then `**`
- B) `***` then `***`
- C) `******`
- D) `*` six times on one line

**9. In a nested loop, the inner loop…**
- A) runs once for the whole program
- B) finishes completely for *each* turn of the outer loop
- C) never runs
- D) runs only on the last outer turn

**10. The program freezes and never stops. What is the most likely cause?**
- A) A `for` loop with `range(3)`
- B) A `while` loop whose counter is not changing
- C) Too many `print()` statements
- D) A missing colour

---

<details><summary>🔑 Answer Key (teacher)</summary>

| Q | Ans | Why |
|---|---|---|
| 1 | **B** | Starts at 0, stops *before* 4 |
| 2 | **B** | Start 2, stop before 11, step 2 |
| 3 | **C** | Counts down from 5 to 1 |
| 4 | **B** | 1+2+3+4+5 = 15 |
| 5 | **B** | `while` repeats while the condition is True |
| 6 | **B** | The counter must change to eventually stop |
| 7 | **A** | `for` = known count; `while` = until a condition |
| 8 | **B** | 3 stars per row, 2 rows |
| 9 | **B** | Inner finishes fully for each outer turn |
| 10 | **B** | Missing counter change = infinite loop |

**Score: ___ / 10**
</details>
