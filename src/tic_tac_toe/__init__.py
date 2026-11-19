"""@file __init__.py
@brief The package `tic_tac_toe`: a text-based Tic Tac Toe game for two players.

Exports the names of the assignment: `print_board`, `check_winner`,
`is_board_full` and `play_game`.
"""

from tic_tac_toe.domain.rules import check_winner, is_board_full
from tic_tac_toe.presentation.board_view import print_board
from tic_tac_toe.presentation.commands.play_game_command import play_game

__all__ = ["check_winner", "is_board_full", "play_game", "print_board"]
