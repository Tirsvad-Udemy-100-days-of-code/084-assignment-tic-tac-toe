# Step 4: Play again

**English** · [Dansk](Step-4-Play-Again-da) · [Bahasa Melayu](Step-4-Play-Again-ms)

## What this step builds

`play_game()` wraps the game in a loop. After the result it asks whether to play again; `y` or `yes` starts a game on an empty board and any other answer ends the program.

## What the program shows

![Screenshot of the program's output (4)](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/raw/branch/main/docs/images/step-4-play-again.png)

The screenshot is made by `scripts/make_screenshots.py` in a Docker container, from the code of this repository.

## What was gained

- **Wrap a game in a loop.** A new `Board` for each game is the whole reset; there is no state to clean up.
- **Normalise the answer.** `.strip().lower()` makes `Y`, `yes` and ` YES ` mean yes, and every other answer means no.
- **End cleanly.** The end of the input or `Ctrl+C` stops the program with a short goodbye and exit code 0, not a traceback.
- **Make a package runnable.** `__main__.py` lets `python -m tic_tac_toe` start the game, and the function names of the assignment stay available from the package.

## How it works

```python
def run_game(view: GameView) -> None:
    while True:
        view.show_result(play_round(view))
        if not wants_another_game(view.ask_play_again()):
            return
```

## Try it

Play two games in a row, a win and then a draw:

```bash
python scripts/scripted_play.py 1 4 2 5 3 y 1 2 3 5 4 6 8 7 9 n | grep -E 'wins|draw|Play again'
```

Previous: [Step 3: Find the winner or a draw](Step-3-Find-the-Winner) · Next: [Summary](Summary)
