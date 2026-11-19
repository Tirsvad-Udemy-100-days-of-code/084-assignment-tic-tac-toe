"""@file test_scripted_play.py
@brief Tests of the helper that plays a game from the command line (screenshots)."""

import pytest

from scripted_play import scripted_game

WIN = ["1", "4", "2", "5", "3", "n"]


def test_the_answers_are_shown_after_their_prompts(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert scripted_game(WIN) == 0
    out = capsys.readouterr().out
    assert "Player X, choose a cell (1-9): 1\n" in out
    assert "Player X wins!" in out
    assert "Play again? (y/n): n\n" in out


def test_the_game_ends_cleanly_when_the_answers_are_used_up(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert scripted_game(["1"]) == 0
    assert "Goodbye." in capsys.readouterr().out
