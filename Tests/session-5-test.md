# 🗺️ Session 5 — MCQ Test

> **Topic:** The Turtle Map, Functions & Animation
> **Total:** 10 questions × 1 mark = 10 marks &nbsp;•&nbsp; ⏱️ 15 min
>
> Name: ______________________  Date: ____________

---

**1. On the turtle screen, where is the point `(0, 0)`?**
- A) Top-left corner
- B) Bottom-right corner
- C) The middle of the screen
- D) There is no `(0, 0)`

**2. Where does `t.goto(0, -150)` move the turtle?**
- A) Straight up
- B) Straight down from the centre
- C) To the right
- D) To the top-left

**3. What does `screen.setup(500, 500)` do?**
- A) Sets the background colour
- B) Sets the window size to 500 × 500 pixels
- C) Draws a 500-sided shape
- D) Repeats the screen 500 times

**4. What is a "pixel"?**
- A) A type of turtle
- B) A tiny coloured dot that makes up the screen
- C) A Python keyword
- D) A kind of loop

**5. Which keyword is used to *define* your own function?**
- A) `func`
- B) `def`
- C) `define`
- D) `function`

**6. After defining `say_hello()`, why might nothing happen?**
- A) Functions never run
- B) You defined it but didn't *call* it with `say_hello()`
- C) You forgot `import turtle`
- D) Functions need a colour

**7. In `def draw_square(size):`, what is `size`?**
- A) A colour
- B) A parameter (an input to the function)
- C) The function's name
- D) A loop

**8. What does this code draw?**
```python
def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

draw_square(50)
draw_square(100)
```
- A) One square
- B) Two squares of different sizes
- C) A triangle
- D) Nothing

**9. Which command writes text on the screen?**
- A) `t.print("Hi")`
- B) `t.say("Hi")`
- C) `t.write("Hi")`
- D) `t.text("Hi")`

**10. What does `t.hideturtle()` do?**
- A) Deletes the drawing
- B) Makes the turtle arrow vanish so the art looks clean
- C) Stops the program
- D) Changes the turtle's colour

---

<details><summary>🔑 Answer Key (teacher)</summary>

| Q | Ans | Why |
|---|---|---|
| 1 | **C** | The middle of the map is (0, 0) |
| 2 | **B** | x stays 0, y is negative → straight down |
| 3 | **B** | `setup` sets the window size in pixels |
| 4 | **B** | Pixels are the tiny dots on the screen |
| 5 | **B** | `def` defines a function |
| 6 | **B** | You must *call* a function to run it |
| 7 | **B** | `size` is a parameter — an input |
| 8 | **B** | Same command, two different sizes |
| 9 | **C** | `t.write()` writes text |
| 10 | **B** | `hideturtle()` hides the turtle cursor |

**Score: ___ / 10**
</details>
