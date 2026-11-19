"""@file test_console_view.py
@brief Tests of the terminal view (ConsoleView of DCD-001)."""

import pytest

from tic_tac_toe.domain.board import Board
from tic_tac_toe.presentation.console_view import ConsoleView


def test_show_board_prints_the_drawing(capsys: pytest.CaptureFixture[str]) -> None:
    ConsoleView().show_board(Board())
    assert " 1 | 2 | 3" in capsys.readouterr().out


def test_ask_move_names_the_player(monkeypatch: pytest.MonkeyPatch) -> None:
    prompts: list[str] = []

    def fake_input(prompt: str) -> str:
        prompts.append(prompt)
        return "5"

    monkeypatch.setattr("builtins.input", fake_input)
    assert ConsoleView().ask_move("O") == "5"
    assert "Player O" in prompts[0]


def test_show_invalid_move_gives_the_reason(capsys: pytest.CaptureFixture[str]) -> None:
    ConsoleView().show_invalid_move("that cell is already taken")
    assert "that cell is already taken" in capsys.readouterr().out


def test_show_result_for_a_win_and_a_draw(capsys: pytest.CaptureFixture[str]) -> None:
    ConsoleView().show_result("X")
    ConsoleView().show_result(None)
    out = capsys.readouterr().out
    assert "Player X wins!" in out
    assert "draw" in out


def test_ask_play_again_returns_the_answer(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: "y")
    assert ConsoleView().ask_play_again() == "y"
