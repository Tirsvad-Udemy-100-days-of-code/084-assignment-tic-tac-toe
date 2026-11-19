"""@file test_board.py
@brief Tests of the Board (OC-001: startGame and makeMove)."""

import pytest

from tic_tac_toe.domain.board import Board
from tic_tac_toe.domain.constants import (
    CELL_COUNT,
    EMPTY_CELL,
    MARK_O,
    MARK_X,
    REASON_OUT_OF_RANGE,
    REASON_TAKEN,
)
from tic_tac_toe.domain.errors import InvalidMoveError


def test_new_board_has_nine_empty_cells() -> None:
    assert Board().marks() == (EMPTY_CELL,) * CELL_COUNT


def test_place_puts_the_mark_in_the_cell() -> None:
    board = Board()
    board.place(MARK_X, 5)
    assert board.cell_at(5) == MARK_X
    assert board.marks().count(MARK_X) == 1


def test_a_placed_cell_is_not_free() -> None:
    board = Board()
    assert board.is_free(1)
    board.place(MARK_X, 1)
    assert not board.is_free(1)


def test_place_in_a_taken_cell_is_rejected_and_changes_nothing() -> None:
    board = Board()
    board.place(MARK_X, 3)
    before = board.marks()
    with pytest.raises(InvalidMoveError) as error:
        board.place(MARK_O, 3)
    assert error.value.reason == REASON_TAKEN
    assert board.marks() == before


@pytest.mark.parametrize("number", [0, -1, 10, 100])
def test_a_number_outside_the_board_is_rejected(number: int) -> None:
    board = Board()
    with pytest.raises(InvalidMoveError) as error:
        board.place(MARK_X, number)
    assert error.value.reason == REASON_OUT_OF_RANGE
    assert board.marks() == (EMPTY_CELL,) * CELL_COUNT


def test_cell_at_rejects_a_number_outside_the_board() -> None:
    with pytest.raises(InvalidMoveError):
        Board().cell_at(10)
