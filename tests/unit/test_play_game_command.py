"""@file test_play_game_command.py
@brief Tests of the command (PlayGameCommand of DCD-001)."""

import io

import pytest

from tic_tac_toe import play_game
from tic_tac_toe.presentation.commands.play_game_command import main
from tic_tac_toe.presentation.constants import EXIT_OK


def test_play_game_plays_to_the_end(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr("sys.stdin", io.StringIO("1\n4\n2\n5\n3\nn\n"))
    play_game()
    assert "Player X wins!" in capsys.readouterr().out


def test_main_returns_the_exit_code(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("sys.stdin", io.StringIO("1\n4\n2\n5\n3\nn\n"))
    assert main() == EXIT_OK


def test_main_ends_cleanly_at_the_end_of_input(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr("sys.stdin", io.StringIO(""))
    assert main() == EXIT_OK
    assert "Goodbye." in capsys.readouterr().out


def test_main_ends_cleanly_on_an_interrupt(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    def interrupt(_prompt: str) -> str:
        raise KeyboardInterrupt

    monkeypatch.setattr("builtins.input", interrupt)
    assert main() == EXIT_OK
    assert "Goodbye." in capsys.readouterr().out
