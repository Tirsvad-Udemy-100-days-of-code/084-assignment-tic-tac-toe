"""@file rules.py
@brief The rules that decide a game (Rules of DCD-001).
"""

from tic_tac_toe.domain.board import Board
from tic_tac_toe.domain.constants import EMPTY_CELL, MARK_O, MARK_X, WINNING_LINES


def check_winner(board: Board, mark: str) -> bool:
    """@brief Tell whether a mark has a winning line.

    @param board The board to look at.
    @param mark The mark of the player.
    @return True when a row, a column or a diagonal holds three of the mark.
    """
    return any(
        all(board.cell_at(number) == mark for number in line) for line in WINNING_LINES
    )


def is_board_full(board: Board) -> bool:
    """@brief Tell whether every cell holds a mark.

    @param board The board to look at.
    @return True when no cell is empty; without a winner this is a draw.
    """
    return EMPTY_CELL not in board.marks()


def next_mark(mark: str) -> str:
    """@brief Return the mark of the other player.

    @param mark The mark of the player who has just moved.
    @return `MARK_O` after `MARK_X`, otherwise `MARK_X`.
    """
    return MARK_O if mark == MARK_X else MARK_X
