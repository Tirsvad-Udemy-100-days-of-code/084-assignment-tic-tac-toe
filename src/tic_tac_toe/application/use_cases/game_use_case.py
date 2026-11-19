"""@file game_use_case.py
@brief The use case "Play a Game of Tic Tac Toe" (GameUseCase of DCD-001, UC-001).
"""

from tic_tac_toe.application.constants import YES_ANSWERS
from tic_tac_toe.application.ports.game_view import GameView
from tic_tac_toe.domain.board import Board
from tic_tac_toe.domain.constants import MARK_X, REASON_NOT_A_NUMBER
from tic_tac_toe.domain.errors import InvalidMoveError
from tic_tac_toe.domain.rules import check_winner, is_board_full, next_mark


def parse_number(choice: str) -> int:
    """@brief Turn what a player gave into a number.

    @param choice The text the player gave.
    @return The whole number in the text.
    @throws InvalidMoveError The text is not a whole number.
    """
    try:
        return int(choice.strip())
    except ValueError as err:
        raise InvalidMoveError(REASON_NOT_A_NUMBER) from err


def wants_another_game(answer: str) -> bool:
    """@brief Tell whether an answer means yes.

    @param answer What the players answered.
    @return True for `y` and `yes` in any case; every other answer means no.
    """
    return answer.strip().lower() in YES_ANSWERS


def play_round(view: GameView) -> str | None:
    """@brief Play one game from an empty board to its result.

    The first player has `MARK_X`. A move that is not allowed is shown with its
    reason and the same player is asked again (ADR-0001).

    @param view The view that shows the board and asks for the moves.
    @return The mark of the winner, or None for a draw.
    """
    board = Board()
    mark = MARK_X
    while True:
        view.show_board(board)
        try:
            board.place(mark, parse_number(view.ask_move(mark)))
        except InvalidMoveError as err:
            view.show_invalid_move(err.reason)
            continue
        if check_winner(board, mark):
            view.show_board(board)
            return mark
        if is_board_full(board):
            view.show_board(board)
            return None
        mark = next_mark(mark)


def run_game(view: GameView) -> None:
    """@brief Play games until the players do not want another one.

    @param view The view that shows the board and asks the players.
    """
    while True:
        view.show_result(play_round(view))
        if not wants_another_game(view.ask_play_again()):
            return
