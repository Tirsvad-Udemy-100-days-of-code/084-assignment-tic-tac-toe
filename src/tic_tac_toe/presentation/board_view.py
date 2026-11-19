"""@file board_view.py
@brief The drawing of the board (BoardView of DCD-001).
"""

from tic_tac_toe.domain.board import Board
from tic_tac_toe.domain.constants import BOARD_SIZE, EMPTY_CELL

## @brief The line drawn between two rows of the board.
_ROW_SEPARATOR = "\n" + "+".join(["---"] * BOARD_SIZE) + "\n"


def render_board(board: Board) -> str:
    """@brief Draw the board as text.

    A cell with a mark shows the mark; an empty cell shows its number, so the
    players can see what to choose.

    @param board The board to draw.
    @return The three rows, separated by lines.
    """
    shown = [
        mark if mark != EMPTY_CELL else str(number)
        for number, mark in enumerate(board.marks(), start=1)
    ]
    rows = [
        "|".join(f" {cell} " for cell in shown[start : start + BOARD_SIZE]).rstrip()
        for start in range(0, len(shown), BOARD_SIZE)
    ]
    return _ROW_SEPARATOR.join(rows)


def print_board(board: Board) -> None:
    """@brief Print the board.

    @param board The board to print.
    """
    print(render_board(board))
