"""@file game_view.py
@brief What the use case needs to show and ask (GameView of DCD-001, ADR-0002).
"""

from typing import Protocol

from tic_tac_toe.domain.board import Board


class GameView(Protocol):
    """@brief The interface through which the use case talks to the players."""

    def show_board(self, board: Board) -> None:
        """@brief Show the board.

        @param board The board to show.
        """
        ...

    def ask_move(self, mark: str) -> str:
        """@brief Ask a player for a cell.

        @param mark The mark of the player whose turn it is.
        @return What the player gave, unchecked.
        """
        ...

    def show_invalid_move(self, reason: str) -> None:
        """@brief Tell the player why the move is not allowed.

        @param reason The reason, in words for the player.
        """
        ...

    def show_result(self, result: str | None) -> None:
        """@brief Tell the players how the game ended.

        @param result The mark of the winner, or None for a draw.
        """
        ...

    def ask_play_again(self) -> str:
        """@brief Ask whether the players want another game.

        @return What the players answered, unchecked.
        """
        ...
