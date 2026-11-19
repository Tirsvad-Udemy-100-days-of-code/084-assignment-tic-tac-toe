"""@file constants.py
@brief The constants of the game (GameConstants of DCD-001).
"""

from typing import Final

## @brief The number of rows, and of columns, of the board.
BOARD_SIZE: Final = 3

## @brief The number of cells of the board.
CELL_COUNT: Final = BOARD_SIZE * BOARD_SIZE

## @brief What a cell holds while no mark has been placed in it.
EMPTY_CELL: Final = " "

## @brief The mark of the first player.
MARK_X: Final = "X"

## @brief The mark of the second player.
MARK_O: Final = "O"

## @brief The eight lines of three cell numbers (rows, columns, diagonals).
WINNING_LINES: Final[tuple[tuple[int, int, int], ...]] = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7),
)

## @brief The reason given when the choice is not a whole number.
REASON_NOT_A_NUMBER: Final = "that is not a whole number"

## @brief The reason given when the number is not the number of a cell.
REASON_OUT_OF_RANGE: Final = "the number must be from 1 to 9"

## @brief The reason given when the cell already holds a mark.
REASON_TAKEN: Final = "that cell is already taken"
