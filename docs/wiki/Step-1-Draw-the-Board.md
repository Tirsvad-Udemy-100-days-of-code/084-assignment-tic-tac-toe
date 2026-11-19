# Step 1: Draw the board

**English** · [Dansk](Step-1-Draw-the-Board-da) · [Bahasa Melayu](Step-1-Draw-the-Board-ms)

## What this step builds

A board of nine cells, and `print_board(board)`, which draws three rows of three cells with lines between them. An empty cell shows its number, so a player can see which number to type.

## What the program shows

![Screenshot of the program's output (1)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-1-draw-the-board.png)

The screenshot is made by `scripts/make_screenshots.py` in a Docker container, from the code of this repository.

## What was gained

- **Model the data, then show it.** The board is nine cells in a list, numbered 1 to 9. How it looks is a separate function, so the rules never depend on the drawing.
- **Build text from data.** `enumerate(..., start=1)` pairs each cell with its number, a list slice cuts the cells into rows, and `join` and f-strings put the rows together.
- **Name your numbers.** `BOARD_SIZE` and `EMPTY_CELL` live in `constants.py`, so no magic number is hidden in the code.
- **Document as you go.** Every function has a short comment that says what it does, and Doxygen builds the documentation from it.

## How it works

```python
def render_board(board: Board) -> str:
    shown = [
        mark if mark != EMPTY_CELL else str(number)
        for number, mark in enumerate(board.marks(), start=1)
    ]
    rows = [
        "|".join(f" {cell} " for cell in shown[start : start + BOARD_SIZE]).rstrip()
        for start in range(0, len(shown), BOARD_SIZE)
    ]
    return _ROW_SEPARATOR.join(rows)
```

## Try it

Draw an empty board and a board with two marks:

```bash
python -c "from tic_tac_toe import print_board
from tic_tac_toe.domain.board import Board
board = Board()
print_board(board)
board.place('X', 5)
board.place('O', 1)
print()
print_board(board)"
```

Previous: [Getting started](Getting-Started) · Next: [Step 2: Take a turn](Step-2-Take-a-Turn)
