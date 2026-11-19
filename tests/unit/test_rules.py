"""@file test_rules.py
@brief Tests of the rules: check_winner, is_board_full, next_mark (OC-001)."""

import pytest

from tic_tac_toe.domain.board import Board
from tic_tac_toe.domain.constants import MARK_O, MARK_X, WINNING_LINES
from tic_tac_toe.domain.rules import check_winner, is_board_full, next_mark


def board_with(mark: str, numbers: tuple[int, ...]) -> Board:
    board = Board()
    for number in numbers:
        board.place(mark, number)
    return board


@pytest.mark.parametrize("line", WINNING_LINES)
def test_every_winning_line_wins(line: tuple[int, int, int]) -> None:
    board = board_with(MARK_X, line)
    assert check_winner(board, MARK_X)
    assert not check_winner(board, MARK_O)


@pytest.mark.parametrize("line", WINNING_LINES)
def test_two_cells_of_a_line_do_not_win(line: tuple[int, int, int]) -> None:
    assert not check_winner(board_with(MARK_X, line[:2]), MARK_X)


def test_a_line_of_mixed_marks_does_not_win() -> None:
    board = Board()
    board.place(MARK_X, 1)
    board.place(MARK_O, 2)
    board.place(MARK_X, 3)
    assert not check_winner(board, MARK_X)
    assert not check_winner(board, MARK_O)


def test_an_empty_board_has_no_winner_and_is_not_full() -> None:
    board = Board()
    assert not check_winner(board, MARK_X)
    assert not is_board_full(board)


def test_a_board_with_a_free_cell_is_not_full() -> None:
    board = board_with(MARK_X, (1, 2, 3, 4, 5, 6, 7, 8))
    assert not is_board_full(board)


def test_a_board_with_nine_marks_is_full() -> None:
    board = board_with(MARK_X, (1, 3, 4, 8, 9))
    for number in (2, 5, 6, 7):
        board.place(MARK_O, number)
    assert is_board_full(board)
    assert not check_winner(board, MARK_X)
    assert not check_winner(board, MARK_O)


def test_next_mark_alternates() -> None:
    assert next_mark(MARK_X) == MARK_O
    assert next_mark(MARK_O) == MARK_X
