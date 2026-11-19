"""@file board.py
@brief The board with its nine cells (Board of DCD-001).
"""

from tic_tac_toe.domain.constants import (
    CELL_COUNT,
    EMPTY_CELL,
    REASON_OUT_OF_RANGE,
    REASON_TAKEN,
)
from tic_tac_toe.domain.errors import InvalidMoveError


class Board:
    """@brief Nine cells, numbered 1 to 9 from left to right and from top to bottom."""

    def __init__(self) -> None:
        """@brief Create a board on which no mark has been placed."""
        ## @brief The marks of the nine cells, in the order of their numbers.
        self._cells: list[str] = [EMPTY_CELL] * CELL_COUNT

    def cell_at(self, number: int) -> str:
        """@brief Return what a cell holds.

        @param number The number of the cell, from 1 to 9.
        @return The mark in the cell, or `EMPTY_CELL`.
        @throws InvalidMoveError The number is not the number of a cell.
        """
        if not 1 <= number <= CELL_COUNT:
            raise InvalidMoveError(REASON_OUT_OF_RANGE)
        return self._cells[number - 1]

    def is_free(self, number: int) -> bool:
        """@brief Tell whether no mark has been placed in a cell.

        @param number The number of the cell, from 1 to 9.
        @return True when the cell is empty.
        @throws InvalidMoveError The number is not the number of a cell.
        """
        return self.cell_at(number) == EMPTY_CELL

    def place(self, mark: str, number: int) -> None:
        """@brief Put a mark in a free cell.

        @param mark The mark of the player who moves.
        @param number The number of the cell, from 1 to 9.
        @throws InvalidMoveError The number is not the number of a cell, or the cell
                is taken; the board does not change.
        """
        if not self.is_free(number):
            raise InvalidMoveError(REASON_TAKEN)
        self._cells[number - 1] = mark

    def marks(self) -> tuple[str, ...]:
        """@brief Return the nine cells in order.

        @return What each cell holds, cell 1 first.
        """
        return tuple(self._cells)
