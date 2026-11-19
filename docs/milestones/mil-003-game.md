# MIL-003 Game

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-006: Go | [b31f4b3] |

---

## Purpose

Decides whether the game works as the use case says: a tested `tic_tac_toe` package and command line, written from the accepted design (use case, Sequence Diagram and Design Class Diagram).

## Deliverable

The package `tic_tac_toe` under `src/` with the functions `print_board`, `check_winner`, `is_board_full` and `play_game`, the constants in `constants.py`, the command `python -m tic_tac_toe`, unit and integration tests under `tests/`, Doxygen comments on every module, class and function, and the code review record.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` | Exit code 0 | Any failing test |
| 2 | Every function in `src/` appears in the method traceability table of DCD-001 | 100 % | Any function without a row |
| 3 | `ruff check`, `ruff format --check` and `mypy --strict` on `src/` and `tests/` | 0 findings | Any finding |
| 4 | `doxygen Doxyfile` | 0 warnings | Any warning |
| 5 | A scripted game from the command line ends in a win, and another in a draw | Exit code 0, result announced | Any other result |
| 6 | `bash scripts/scan.sh` (opengrep) | 0 findings | Any finding |
| 7 | `pyproject.toml` lists no runtime dependency | `dependencies = []` | Any entry |
| 8 | The code review record against `QC-PY-001` | `Go` | Any other verdict |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The use case and its design artifacts are accepted before the first line of code |
| MIL-002 | The project configuration, the scan and the Doxyfile are in place |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 objectives 1 to 4 and 7, success criteria 1, 2, 3, 6, 7 and 8; story US-001 | CN-001, CN-004 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-20 — inside the Business Case constraint (completion by 2026-11-22).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Define the game constants | Create `constants.py` with the board size, the empty cell, the marks `X` and `O` and the eight winning lines, as the class `GameConstants` of the design. | Yes | UC-001, DCD-001 |
| 2 | Implement the Board | Create the Board in the Domain: nine cells, a check that a cell is free, and placing a mark in the cell with a number from 1 to 9. | Yes | SD-001, DCD-001 |
| 3 | Implement check_winner | Create `check_winner(board, mark)` in the Domain: true when a row, a column or a diagonal holds three of the mark. | Yes | OC-001, SD-001, DCD-001 |
| 4 | Implement is_board_full | Create `is_board_full(board)` in the Domain: true when no cell is empty, so a full board without a winner is a draw. | Yes | OC-001, SD-001, DCD-001 |
| 5 | Implement print_board | Create `print_board(board)` in the Presentation: draw the three rows with the mark or the number of each cell. | Yes | SD-001, DCD-001 |
| 6 | Implement play_game | Create the use case `play_game` in the Application: alternate the players, reject an invalid move as ADR-0001 decides, announce a win or a draw and offer another game. | Yes | UC-001, OC-001, SD-001, ADR-0001 |
| 7 | Implement the command | Create the console command and `__main__.py`, so `python -m tic_tac_toe` plays a game on the terminal and exits with 0, as ADR-0002 decides. | Yes | UC-001, DCD-001, ADR-0002 |
| 8 | Write unit tests | Test the constants, the Board, `check_winner` (every winning line), `is_board_full`, `print_board` and `play_game` with scripted input, with pytest. | Yes | OC-001 |
| 9 | Write integration tests | Run `python -m tic_tac_toe` as a subprocess with scripted input for a win, a draw, an invalid move and playing again. | Yes | UC-001 |
| 10 | Add Doxygen comments and build the documentation | Every module, class and function has a Doxygen comment; `doxygen Doxyfile` reports no warning. | No | |
| 11 | Lint and type-check | `ruff` and `mypy --strict` pass on `src/` and `tests/`. | No | |
| 12 | Review the code | Review the code against `QC-PY-001` and the Design Class Diagram and record the `RC-*`; fix findings until it says `Go`. | No | |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
