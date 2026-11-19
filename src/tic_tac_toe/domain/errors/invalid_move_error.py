"""@file invalid_move_error.py
@brief The error for a move that is not allowed (InvalidMoveError of DCD-001).
"""


class InvalidMoveError(ValueError):
    """@brief A move that is not allowed; the reason says why (ADR-0001)."""

    def __init__(self, reason: str) -> None:
        """@brief Create the error.

        @param reason Why the move is not allowed, in words for the player.
        """
        super().__init__(reason)
        ## @brief Why the move is not allowed, in words for the player.
        self.reason = reason
