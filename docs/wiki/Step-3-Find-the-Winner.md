# Step 3: Find the winner or a draw

**English** · [Dansk](Step-3-Find-the-Winner-da) · [Bahasa Melayu](Step-3-Find-the-Winner-ms)

## What this step builds

After every move the game asks `check_winner(board, mark)` whether the mark has a row, a column or a diagonal. If not, `is_board_full(board)` tells whether the game is a draw. Otherwise the other player is next.

## What the program shows

![Screenshot of the program's output (3)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-3-find-the-winner.png)

The screenshot is made by `scripts/make_screenshots.py` in a Docker container, from the code of this repository.

## What was gained

- **Let data carry the rules.** The eight winning lines are a tuple of tuples; the check is one `any` over them with one `all` inside, with no long chain of `if`.
- **Order the checks.** The winner is tested before the full board, because the last move can win on a full board.
- **Return a value that says it all.** `play_round` returns the winner's mark, or `None` for a draw, and the caller decides what to show.
- **Test every case.** `pytest.mark.parametrize` runs one test for each of the eight lines, so a typo in the table cannot hide.

## How it works

```python
WINNING_LINES = (
    (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
    (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
    (1, 5, 9), (3, 5, 7),             # diagonals
)

def check_winner(board: Board, mark: str) -> bool:
    return any(
        all(board.cell_at(number) == mark for number in line) for line in WINNING_LINES
    )

def is_board_full(board: Board) -> bool:
    return EMPTY_CELL not in board.marks()
```

## Try it

Finish a game with a win and a game with a draw, and show the end of each:

```bash
python scripts/scripted_play.py 1 4 2 5 3 n | tail -n 8
python scripts/scripted_play.py 1 2 3 5 4 6 8 7 9 n | tail -n 9
```

Previous: [Step 2: Take a turn](Step-2-Take-a-Turn) · Next: [Step 4: Play again](Step-4-Play-Again)
