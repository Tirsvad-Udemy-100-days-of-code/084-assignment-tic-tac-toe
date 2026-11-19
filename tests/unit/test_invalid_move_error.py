"""@file test_invalid_move_error.py
@brief Tests of InvalidMoveError (ADR-0001)."""

import pytest

from tic_tac_toe.domain.errors import InvalidMoveError


def test_error_keeps_the_reason() -> None:
    error = InvalidMoveError("because")
    assert error.reason == "because"
    assert str(error) == "because"


def test_error_is_a_value_error() -> None:
    with pytest.raises(ValueError):
        raise InvalidMoveError("because")
