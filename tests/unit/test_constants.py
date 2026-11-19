"""@file test_constants.py
@brief Tests of the constants of the game (GameConstants of DCD-001)."""

from tic_tac_toe.domain.constants import (
    BOARD_SIZE,
    CELL_COUNT,
    MARK_O,
    MARK_X,
    WINNING_LINES,
)


def test_board_has_nine_cells() -> None:
    assert BOARD_SIZE == 3
    assert CELL_COUNT == 9


def test_marks_differ() -> None:
    assert len({MARK_X, MARK_O}) == 2


def test_there_are_eight_distinct_winning_lines() -> None:
    assert len(WINNING_LINES) == 8
    assert len(set(WINNING_LINES)) == 8


def test_every_line_has_three_cells_of_the_board() -> None:
    for line in WINNING_LINES:
        assert len(set(line)) == 3
        assert all(1 <= number <= CELL_COUNT for number in line)
