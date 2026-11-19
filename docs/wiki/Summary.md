# Summary

**English** · [Dansk](Summary-da) · [Bahasa Melayu](Summary-ms)

Four steps took a blank file to a tested game. This page puts them side by side.

## The steps side by side

| Step | What you built | The function | The skill |
| --- | --- | --- | --- |
| [Step 1](Step-1-Draw-the-Board) | The board and its drawing | `print_board` | Lists, slicing, f-strings and constants |
| [Step 2](Step-2-Take-a-Turn) | A turn with checked input | `play_round`, `parse_number` | Input, exceptions and loops |
| [Step 3](Step-3-Find-the-Winner) | The winner and the draw | `check_winner`, `is_board_full` | Data-driven rules, `any` and `all` |
| [Step 4](Step-4-Play-Again) | Playing again, and a clean end | `play_game` | Loops, exit codes and packages |

## How the code is laid out

The code follows a small design: the **Domain** (`Board`, the rules and the constants) knows nothing about the screen, the **Application** (the use case and the `GameView` interface) runs a game, and the **Presentation** (the console view and the command) talks to the players. Because of this, 86 tests run the game without a keyboard.

## Where to go from here

- Play against the computer: add a function that picks a free cell, then a better one that blocks a win.
- Make the board bigger, for example 4 by 4, and change `BOARD_SIZE` and `WINNING_LINES` only.
- Keep a score over several games.
- Draw the board in a window; only a new view is needed, as the use case already talks to an interface.
