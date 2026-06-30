# 🎆 Session 6 — MCQ Test

> **Topic:** Randomness, Animation & Final Project
> **Total:** 10 questions × 1 mark = 10 marks &nbsp;•&nbsp; ⏱️ 15 min
>
> Name: ______________________  Date: ____________

---

**1. What does `random.randint(1, 6)` return?**
- A) Always `6`
- B) A random whole number from 1 to 6
- C) A list of numbers
- D) The number 1.6

**2. What does `random.choice(["red", "blue", "green"])` do?**
- A) Prints all three colours
- B) Picks one of the colours at random
- C) Sorts the colours
- D) Removes a colour

**3. Before using `random.randint()`, you must write…**
- A) `import turtle`
- B) `import random`
- C) `from turtle import random`
- D) nothing

**4. What does `while True:` do?**
- A) Runs the loop once
- B) Never runs the loop
- C) Runs the loop forever (until you close the window)
- D) Runs the loop only if a number is True

**5. Which two commands work together to make animation smooth?**
- A) `penup()` and `pendown()`
- B) `tracer(0)` and `update()`
- C) `begin_fill()` and `end_fill()`
- D) `forward()` and `backward()`

**6. Why do we call `t.clear()` at the top of an animation loop?**
- A) To change the background colour
- B) To erase the old drawing before drawing the new frame
- C) To stop the program
- D) To make the turtle faster

**7. What does `t.xcor()` give you?**
- A) The turtle's colour
- B) The turtle's x (horizontal) position
- C) The number of loops
- D) A random number

**8. In the moving-ball code, what does this `if` do?**
```python
if t.xcor() > 300:
    t.goto(-250, 0)
```
- A) Stops the ball
- B) When the ball goes off the right edge, jump it back to the left
- C) Makes the ball bigger
- D) Changes the ball's colour

**9. In the fireworks code, each spark goes `forward(50)` then `backward(50)`. Why?**
- A) To make the sparks share one centre point (the burst shape)
- B) To slow the program down
- C) To change colour
- D) It is a mistake

**10. In the moon-sky final test, using a `star(x, y, size)` function instead of repeating code is good because…**
- A) it makes the program longer
- B) it turns many messy lines into a few tidy, reusable lines
- C) functions draw faster
- D) it removes the need for colours

---

<details><summary>🔑 Answer Key (teacher)</summary>

| Q | Ans | Why |
|---|---|---|
| 1 | **B** | `randint(1, 6)` → random whole number, both ends included |
| 2 | **B** | `choice` picks one random item from a list |
| 3 | **B** | You must `import random` first |
| 4 | **C** | `while True:` loops forever |
| 5 | **B** | `tracer(0)` + `update()` control each frame |
| 6 | **B** | `clear()` erases the old frame |
| 7 | **B** | `xcor()` reads the x position |
| 8 | **B** | Detects off-screen and resets — game logic |
| 9 | **A** | Out-and-back shares one centre → starburst |
| 10 | **B** | Functions make big drawings tidy and reusable |

**Score: ___ / 10**
</details>
