"""@file test_board_view.py
@brief Tests of the drawing of the board (BoardView of DCD-001)."""

import pytest

from tic_tac_toe import print_board
from tic_tac_toe.domain.board import Board
from tic_tac_toe.domain.constants import MARK_O, MARK_X
from tic_tac_toe.presentation.board_view import render_board

EMPTY_DRAWING = " 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9"


def test_an_empty_board_shows_the_cell_numbers() -> None:
    assert render_board(Board()) == EMPTY_DRAWING


def test_a_mark_replaces_the_number_of_its_cell() -> None:
    board = Board()
    board.place(MARK_X, 1)
    board.place(MARK_O, 5)
    assert render_board(board).splitlines()[0] == " X | 2 | 3"
    assert render_board(board).splitlines()[2] == " 4 | O | 6"


def test_print_board_prints_the_drawing(capsys: pytest.CaptureFixture[str]) -> None:
    print_board(Board())
    assert capsys.readouterr().out == EMPTY_DRAWING + "\n"
