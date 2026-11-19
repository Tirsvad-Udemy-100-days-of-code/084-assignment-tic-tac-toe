"""@file constants.py
@brief The texts and the exit code of the terminal (PresentationConstants of DCD-001).
"""

from typing import Final

## @brief The question for a move; `{mark}` is the mark of the player.
PROMPT_MOVE: Final = "Player {mark}, choose a cell (1-9): "

## @brief The question after a game.
PROMPT_PLAY_AGAIN: Final = "Play again? (y/n): "

## @brief The result for a win; `{mark}` is the mark of the winner.
MESSAGE_WIN: Final = "Player {mark} wins!"

## @brief The result for a draw.
MESSAGE_DRAW: Final = "It is a draw."

## @brief The message for a move that is not allowed; `{reason}` says why.
MESSAGE_INVALID_MOVE: Final = "Not allowed: {reason}."

## @brief The message when the players end the program.
MESSAGE_GOODBYE: Final = "Goodbye."

## @brief The exit code of the program.
EXIT_OK: Final = 0
