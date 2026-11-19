"""@file play_game_command.py
@brief The command of the use case and the composition root (PlayGameCommand).
"""

from tic_tac_toe.application.use_cases.game_use_case import run_game
from tic_tac_toe.presentation.console_view import ConsoleView
from tic_tac_toe.presentation.constants import EXIT_OK, MESSAGE_GOODBYE


def play_game() -> None:
    """@brief Play games on the terminal until the players do not want another one."""
    run_game(ConsoleView())


def main() -> int:
    """@brief Entry point: play, and end cleanly on the end of input or an interrupt.

    @return `EXIT_OK`.
    """
    try:
        play_game()
    except (EOFError, KeyboardInterrupt):
        print()
        print(MESSAGE_GOODBYE)
    return EXIT_OK
