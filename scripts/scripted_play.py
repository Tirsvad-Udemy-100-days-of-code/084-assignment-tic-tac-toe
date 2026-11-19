"""@file scripted_play.py
@brief Play the game with answers given on the command line.

Each answer is shown after its prompt, the way a terminal shows what a player
types, so a captured game can be read from top to bottom. It is a helper for the
screenshots; the game itself does not know about it.

Usage:
    python scripts/scripted_play.py ANSWER [ANSWER ...]
"""

import sys
from unittest.mock import patch

from tic_tac_toe.presentation.commands.play_game_command import main as play


def scripted_game(answers: list[str]) -> int:
    """@brief Play the game with the given answers.

    @param answers What the players type, one answer for each prompt.
    @return The exit code of the game.
    """
    queue = iter(answers)

    def scripted_input(prompt: str = "") -> str:
        """@brief Answer a prompt from the queue and show the answer."""
        try:
            answer = next(queue)
        except StopIteration:
            raise EOFError from None
        print(f"{prompt}{answer}")
        return answer

    with patch("builtins.input", scripted_input):
        return play()


if __name__ == "__main__":
    sys.exit(scripted_game(sys.argv[1:]))
