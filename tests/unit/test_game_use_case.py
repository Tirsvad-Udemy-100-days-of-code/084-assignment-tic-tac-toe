"""@file test_game_use_case.py
@brief Tests of the use case with a scripted view (UC-001, OC-001, ADR-0002)."""

import pytest

from tic_tac_toe.application.use_cases.game_use_case import (
    parse_number,
    play_round,
    run_game,
    wants_another_game,
)
from tic_tac_toe.domain.board import Board
from tic_tac_toe.domain.constants import (
    MARK_O,
    MARK_X,
    REASON_NOT_A_NUMBER,
    REASON_OUT_OF_RANGE,
    REASON_TAKEN,
)
from tic_tac_toe.domain.errors import InvalidMoveError


class ScriptedView:
    """A view that answers from a script and records what it was told."""

    def __init__(self, moves: list[str], answers: list[str] | None = None) -> None:
        self.moves = list(moves)
        self.answers = list(answers or [])
        self.boards: list[tuple[str, ...]] = []
        self.marks_asked: list[str] = []
        self.reasons: list[str] = []
        self.results: list[str | None] = []

    def show_board(self, board: Board) -> None:
        self.boards.append(board.marks())

    def ask_move(self, mark: str) -> str:
        self.marks_asked.append(mark)
        return self.moves.pop(0)

    def show_invalid_move(self, reason: str) -> None:
        self.reasons.append(reason)

    def show_result(self, result: str | None) -> None:
        self.results.append(result)

    def ask_play_again(self) -> str:
        return self.answers.pop(0)


X_WINS = ["1", "4", "2", "5", "3"]
DRAW = ["1", "2", "3", "5", "4", "6", "8", "7", "9"]


def test_x_moves_first_and_the_marks_alternate() -> None:
    view = ScriptedView(X_WINS)
    play_round(view)
    assert view.marks_asked == [MARK_X, MARK_O, MARK_X, MARK_O, MARK_X]


def test_first_board_shown_is_empty() -> None:
    view = ScriptedView(X_WINS)
    play_round(view)
    assert set(view.boards[0]) == {" "}


def test_a_line_of_three_wins() -> None:
    assert play_round(ScriptedView(X_WINS)) == MARK_X


def test_the_second_player_can_win() -> None:
    assert play_round(ScriptedView(["1", "4", "2", "5", "9", "6"])) == MARK_O


def test_a_full_board_without_a_line_is_a_draw() -> None:
    assert play_round(ScriptedView(DRAW)) is None


def test_the_board_is_shown_again_after_the_last_move() -> None:
    view = ScriptedView(X_WINS)
    play_round(view)
    assert view.boards[-1].count(MARK_X) == 3


@pytest.mark.parametrize(
    ("bad", "reason"),
    [
        ("x", REASON_NOT_A_NUMBER),
        ("", REASON_NOT_A_NUMBER),
        ("1.5", REASON_NOT_A_NUMBER),
        ("0", REASON_OUT_OF_RANGE),
        ("10", REASON_OUT_OF_RANGE),
        ("-3", REASON_OUT_OF_RANGE),
        ("1", REASON_TAKEN),
    ],
)
def test_a_move_that_is_not_allowed_is_rejected_and_the_same_player_is_asked(
    bad: str, reason: str
) -> None:
    view = ScriptedView(["1", bad, "4", "2", "5", "3"])
    assert play_round(view) == MARK_X
    assert view.reasons == [reason]
    assert view.marks_asked[1:3] == [MARK_O, MARK_O]


def test_the_board_does_not_change_after_a_rejected_move() -> None:
    view = ScriptedView(["5", "5", "1", "9", "2", "8", "3"])
    play_round(view)
    assert view.boards[1] == view.boards[2]


@pytest.mark.parametrize("answer", ["y", "Y", "yes", "YES", " Yes "])
def test_yes_answers_start_another_game(answer: str) -> None:
    assert wants_another_game(answer)


@pytest.mark.parametrize("answer", ["n", "no", "", "maybe", "yep"])
def test_other_answers_end_the_program(answer: str) -> None:
    assert not wants_another_game(answer)


def test_parse_number_accepts_a_whole_number_with_spaces() -> None:
    assert parse_number(" 7 ") == 7


def test_parse_number_rejects_text() -> None:
    with pytest.raises(InvalidMoveError) as error:
        parse_number("seven")
    assert error.value.reason == REASON_NOT_A_NUMBER


def test_run_game_plays_again_on_yes_and_stops_on_no() -> None:
    view = ScriptedView(X_WINS + DRAW, ["yes", "n"])
    run_game(view)
    assert view.results == [MARK_X, None]


def test_run_game_stops_after_one_game_on_no() -> None:
    view = ScriptedView(X_WINS, ["no"])
    run_game(view)
    assert view.results == [MARK_X]
