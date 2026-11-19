"""@file test_command_line.py
@brief Runs `python -m tic_tac_toe` as a subprocess (UC-001 scenarios)."""

import subprocess
import sys

X_WINS = "1\n4\n2\n5\n3\n"
DRAW = "1\n2\n3\n5\n4\n6\n8\n7\n9\n"


def run_program(stdin: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "tic_tac_toe"],
        input=stdin,
        capture_output=True,
        text=True,
        check=False,
    )


def test_main_scenario_ends_in_a_win() -> None:
    result = run_program(X_WINS + "n\n")
    assert result.returncode == 0
    assert "Player X wins!" in result.stdout
    assert result.stderr == ""


def test_a_full_board_ends_in_a_draw() -> None:
    result = run_program(DRAW + "n\n")
    assert result.returncode == 0
    assert "It is a draw." in result.stdout


def test_extension_4a_a_move_that_is_not_allowed_is_asked_again() -> None:
    result = run_program("1\n1\nabc\n12\n4\n2\n5\n3\nn\n")
    assert result.returncode == 0
    assert result.stdout.count("Not allowed:") == 3
    assert "that cell is already taken" in result.stdout
    assert "that is not a whole number" in result.stdout
    assert "the number must be from 1 to 9" in result.stdout
    assert "Player X wins!" in result.stdout


def test_extension_9a_another_game_starts_with_an_empty_board() -> None:
    result = run_program(X_WINS + "yes\n" + DRAW + "n\n")
    assert result.returncode == 0
    assert "Player X wins!" in result.stdout
    assert "It is a draw." in result.stdout
    assert result.stdout.count(" 1 | 2 | 3\n") == 2


def test_extension_star_a_end_of_input_ends_without_a_result() -> None:
    result = run_program("1\n")
    assert result.returncode == 0
    assert "Goodbye." in result.stdout
    assert "wins" not in result.stdout
