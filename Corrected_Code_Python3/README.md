# Move the Turtle — Corrected Code (Python 3)

All programs from Sessions 1–7, fixed to run on **Python 3** with correct
indentation. Every file was checked with `python3 -m compileall` and compiles
cleanly. Each file is one self-contained program — open it and run.

## How to run
- **Online (recommended for class):** trinket.io/python or replit.com — both are
  Python 3 with turtle support. Paste one file, press Run.
- **On a computer:** `python3 "session 1/03_first_turtle.py"`

## What was changed from the originals
1. **`print "..."` → `print("...")`** everywhere (Python 2 → Python 3). This was
   the main reason Session 1 / 3 code failed.
2. **Indentation restored** on loops that lost it on the slides (sun, moving ball,
   race track).
3. **`sum` renamed to `total`** in the add programs — `sum` is a built-in and
   shadowing it teaches a bad habit.
4. **Session 4 cookies output** corrected to real Python 3 output
   (`I have 5 cookies...`, not the Python 2 tuple form).
5. **`turtle.done()` added** to every drawing program so the window stays open.
6. Moon-sky and happy-face refactored slightly with a small helper so the repeated
   star/eye code is easier to read (optional — revert if you prefer it flat).

## Notes for the two "infinite loop" programs
- `session 6/02_moving_ball.py` and `session 7/01_random_walk.py` use
  `while True:` — they run until you close the window. That is intended.

## Folder map
```
session 1/  basics, first turtle, shapes, happy face, assignment answers
session 2/  pen commands, smiley face, staircase loop
session 3/  area, booleans, spirals, if/elif, traffic light
session 4/  voting/even-odd/marks, for & while loops, sun
session 5/  olympic rings, animation, house, HOPE letters
session 6/  fireworks, moving ball, moon-sky final test
session 7/  random walk, turtle racing game
```
