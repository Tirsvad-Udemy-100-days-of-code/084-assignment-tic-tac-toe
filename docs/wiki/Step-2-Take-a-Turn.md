# Step 2: Take a turn

**English** · [Dansk](Step-2-Take-a-Turn-da) · [Bahasa Melayu](Step-2-Take-a-Turn-ms)

## What this step builds

The player whose turn it is types the number of a cell. The game puts the mark there and draws the board again. A choice that is not allowed is refused with the reason, and the same player is asked again.

## What the program shows

![Screenshot of the program's output (2)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-2-take-a-turn.png)

The screenshot is made by `scripts/make_screenshots.py` in a Docker container, from the code of this repository.

## What was gained

- **Read input and turn it into a number.** `input()` gives text; `int()` turns it into a number and fails with `ValueError` when it is not one.
- **Check what you were given.** Three things can be wrong: not a number, outside 1 to 9, or a cell that is taken. Each is its own reason in one error type, `InvalidMoveError`.
- **Raise your own exception.** The error keeps the cause with `raise ... from`, and the board never changes when a move is refused (decision ADR-0001).
- **Loop with `while True` and `continue`.** After a refused move the same player is asked again, so a typing mistake never costs a turn.
- **Keep the screen apart from the rules.** The use case talks to a `GameView` interface, so the whole flow is tested with a scripted view and no keyboard (decision ADR-0002).

## How it works

```python
def parse_number(choice: str) -> int:
    try:
        return int(choice.strip())
    except ValueError as err:
        raise InvalidMoveError(REASON_NOT_A_NUMBER) from err
```

```python
def place(self, mark: str, number: int) -> None:
    if not self.is_free(number):
        raise InvalidMoveError(REASON_TAKEN)
    self._cells[number - 1] = mark
```

## Try it

Play a game with a mistake of each kind (the answers are `1`, `x`, `1` and `5`):

```bash
python scripts/scripted_play.py 1 x 1 5
```

Previous: [Step 1: Draw the board](Step-1-Draw-the-Board) · Next: [Step 3: Find the winner or a draw](Step-3-Find-the-Winner)
