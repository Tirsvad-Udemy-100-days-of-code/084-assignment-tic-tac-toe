# Review Record: MIL-003 against QC-PY-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-021 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | [faea764] |

---

## Artifact Under Review

- Instance reviewed: [MIL-003]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules, functions and variables are `snake_case` (`check_winner`, `play_round`), classes `PascalCase` (`Board`, `ConsoleView`, `InvalidMoveError`) and constants `UPPER_SNAKE` (`WINNING_LINES`, `MARK_X`); ruff rule set `E, F, I, UP, B` raises no finding. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose in the dictionary's terms (`mark`, `cell`, `board`, `winning line`, `move`); the only short names are `err` in an `except` clause and loop variables of one line. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check src tests` reports 29 files already formatted; `ruff check src tests` reports no finding; the code has no `noqa` and no `type: ignore`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy src tests` (strict, set in `pyproject.toml`) reports no issue in 29 files; every function, including `__init__` and the tests, has parameter and return annotations, `-> None` where nothing is returned. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | The only `except` clauses name `ValueError` (re-raised as `InvalidMoveError ... from err`), `InvalidMoveError` (shown to the player, who is asked again) and `(EOFError, KeyboardInterrupt)` (the planned end of the program of UC-001 extension *a); none is bare or silent. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No default argument is mutable and no builtin is shadowed; `Board` creates its list in `__init__`. |
| 7 | Files, locks and connections are managed with context managers | N-A | The program opens no file, lock or connection. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class and function has a Doxygen docstring with `@brief`, `@param`, `@return` and `@throws` where they apply; `doxygen Doxyfile` with `WARN_AS_ERROR = YES` reports no warning. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No logging is needed: the program has no diagnostics. `print` and `input` are the game's user interface and sit only in the Presentation (`ConsoleView`, `BoardView`, `PlayGameCommand`), behind the interface `GameView` of ADR-0002; nothing secret or personal is read or printed. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | Every class and function of `src/` (31 definitions) is a row or a name in the method traceability table of [DCD-001]; a script that compares the two found none missing. The functions of the design that are module-level are the `<<module>>` classes of the diagram (`Rules`, `GameUseCase`, `BoardView`, `GameConstants`); the export of `print_board`, `check_winner`, `is_board_full` and `play_game` in `__init__.py` is the assignment's required API, not a new class. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 81 tests in `tests/unit` and `tests/integration` pass in 0.5 s; they are named for the behaviour (`test_a_full_board_without_a_line_is_a_draw`), use a scripted view or a subprocess with scripted input, and need no network and no order. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy` runs in strict mode without error; the code uses no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `pyproject.toml` has `dependencies = []`; the dev tools (pytest, ruff, mypy, pillow) are in the `dev` extra, with a lower bound, and each is used (pillow by the screenshot script of MIL-004). |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The winning lines, marks, size and reasons are defined once in `domain/constants.py`, the prompts and messages once in `presentation/constants.py`, and the words for yes once in `application/constants.py`; the rule for a winner is `check_winner` only, and `ConsoleView` and the tests import the constants rather than copy them. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` imports nothing from `application` or `presentation`; `application` imports `domain` and defines the port `GameView`; `presentation` imports both; there is no import cycle (the package imports in `__init__.py` follow the same direction). |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Each class has one reason to change (`Board` the cells, `Rules` the rules, `GameUseCase` the flow, `ConsoleView` the terminal); `GameView` is a narrow protocol of five methods, the use case receives its implementation, and `ConsoleView` honours the protocol (mypy checks it). |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | `src/tic_tac_toe/` has the layers `domain`, `application` and `presentation`; there is no `infrastructure` layer because the game stores nothing and calls no outside service, which is not a merged layer but one with nothing to hold; `tests/` has `unit` and `integration`; the `e2e` folder is not needed, because the integration tests already run the whole program as a subprocess. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All folders and files are English `snake_case` with letters, digits and `_` only (`play_game_command.py`, `invalid_move_error.py`). |

## Overall Verdict

Go — every Mandatory criterion of [QC-PY-001] passes or does not apply, so criterion 8 of the milestone ([MIL-003]) is met. The code review is autonomous and not independent. The code is reviewed against the Design Class Diagram [DCD-001] and the decisions [ADR-0001] and [ADR-0002].

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[ADR-0001]: ../../adr/adr-0001-invalid-moves-are-rejected.md
[ADR-0002]: ../../adr/adr-0002-console-is-reached-through-a-view-interface.md
[DCD-001]: ../../dcd.md
[MIL-003]: ../../milestones/mil-003-game.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[faea764]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/faea764ea7a3bf62656a362a6378d4eacfe2d9b8
