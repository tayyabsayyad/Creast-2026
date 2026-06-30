# 🏁 Session 7 — MCQ Test

> **Topic:** The Racing Game & Capstone
> **Total:** 10 questions × 1 mark = 10 marks &nbsp;•&nbsp; ⏱️ 15 min
>
> Name: ______________________  Date: ____________

---

**1. How many turtles can you create on one screen?**
- A) Only one
- B) Exactly two
- C) As many as you like — each is its own object
- D) Only four

**2. What does this code do?**
```python
red_t  = turtle.Turtle(); red_t.color("red")
blue_t = turtle.Turtle(); blue_t.color("blue")
red_t.forward(100)
```
- A) Both turtles move forward
- B) Only the red turtle moves forward
- C) Only the blue turtle moves forward
- D) Nothing moves

**3. What does `from random import randint` let you do?**
- A) Use `randint(...)` without writing `random.` first
- B) Import the whole turtle module
- C) Make the program random-coloured
- D) Nothing useful

**4. In the racing game, what makes each turtle move forward each turn?**
- A) A fixed number of steps
- B) `randint(1, 5)` — a random number of steps
- C) The user types the distance
- D) They all move the same amount

**5. Why can't you predict who wins the race?**
- A) The turtles are too slow
- B) Each step is random, so the result changes every race
- C) The first turtle always wins
- D) The track is too short

**6. In the race track code, the dashes are drawn using…**
- A) a single command
- B) a nested loop (a loop inside a loop)
- C) the `if` statement
- D) a function called `dash()`

**7. To stop turtles from drawing on top of each other, you should…**
- A) give each turtle its own `goto(...)` start position
- B) use only one colour
- C) remove `turtle.done()`
- D) make the track shorter

**8. What does this winner-detection line do?**
```python
winner = max(positions, key=positions.get)
```
- A) Picks the turtle with the smallest x position
- B) Picks the turtle that travelled the furthest (largest x)
- C) Picks a random turtle
- D) Stops the race

**9. Only one turtle moves in your race. What is the most likely bug?**
- A) You used `plyr1` everywhere instead of `plyr2`, `plyr3`…
- B) You forgot to import turtle
- C) The track is too long
- D) You used too many colours

**10. For the capstone project, which skills can you combine?**
- A) Only loops
- B) Only the turtle's colour
- C) Shapes, loops, if/else, functions, randomness and coordinates
- D) Only `print()`

---

<details><summary>🔑 Answer Key (teacher)</summary>

| Q | Ans | Why |
|---|---|---|
| 1 | **C** | Each `turtle.Turtle()` is a separate object |
| 2 | **B** | Commands only affect the named turtle |
| 3 | **A** | The import lets you call `randint()` directly |
| 4 | **B** | Each turn it jumps a random 1–5 steps |
| 5 | **B** | Randomness makes the winner change each race |
| 6 | **B** | The dashes use a nested loop |
| 7 | **A** | Give each turtle its own start `goto` |
| 8 | **B** | `max` with `.get` finds the furthest turtle |
| 9 | **A** | Re-using `plyr1` is the classic bug |
| 10 | **C** | The capstone combines everything learned |

**Score: ___ / 10**
</details>
