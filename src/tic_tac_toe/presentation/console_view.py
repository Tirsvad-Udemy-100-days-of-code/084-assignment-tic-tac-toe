"""@file console_view.py
@brief The terminal as a view of the game (ConsoleView of DCD-001, ADR-0002).
"""

from tic_tac_toe.domain.board import Board
from tic_tac_toe.presentation.board_view import print_board
from tic_tac_toe.presentation.constants import (
    MESSAGE_DRAW,
    MESSAGE_INVALID_MOVE,
    MESSAGE_WIN,
    PROMPT_MOVE,
    PROMPT_PLAY_AGAIN,
)


class ConsoleView:
    """@brief Implements `GameView` with `print` and `input`."""

    def show_board(self, board: Board) -> None:
        """@brief Print the board, after an empty line.

        @param board The board to show.
        """
        print()
        print_board(board)

    def ask_move(self, mark: str) -> str:
        """@brief Ask a player for a cell.

        @param mark The mark of the player whose turn it is.
        @return What the player typed.
        """
        return input(PROMPT_MOVE.format(mark=mark))

    def show_invalid_move(self, reason: str) -> None:
        """@brief Print why the move is not allowed.

        @param reason The reason, in words for the player.
        """
        print(MESSAGE_INVALID_MOVE.format(reason=reason))

    def show_result(self, result: str | None) -> None:
        """@brief Print how the game ended.

        @param result The mark of the winner, or None for a draw.
        """
        print(MESSAGE_DRAW if result is None else MESSAGE_WIN.format(mark=result))

    def ask_play_again(self) -> str:
        """@brief Ask whether the players want another game.

        @return What the players typed.
        """
        return input(PROMPT_PLAY_AGAIN)
