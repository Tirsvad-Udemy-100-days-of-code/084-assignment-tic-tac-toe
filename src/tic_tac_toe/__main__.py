"""@file __main__.py
@brief Makes `python -m tic_tac_toe` play a game.
"""

import sys

from tic_tac_toe.presentation.commands.play_game_command import main

if __name__ == "__main__":
    sys.exit(main())
