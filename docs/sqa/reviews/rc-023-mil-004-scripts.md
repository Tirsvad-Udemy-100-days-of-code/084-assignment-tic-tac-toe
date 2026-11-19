# Review Record: MIL-004 against QC-PY-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-023 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | [049c211] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-PY-001]
- Scope: full review of scripts/make_screenshots.py and scripts/scripted_play.py
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules, functions, variables and constants follow PEP 8 casing (`make_screenshots`, `run_in_container`, `render`, `STEPS`, `Step`); ruff reports no finding. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`run_in_container`, `scripted_game`, `load_font`); the only short names are loop variables of one line. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check` and `ruff check` on `scripts` report no finding; the one suppression is `# nosemgrep` on the `subprocess.run` call, with a comment that says why (the command is a constant of this file). |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy` (strict) reports no issue in 33 files, including `scripts/` and the tests; every function has annotations. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `load_font` catches `OSError` only, to try the next font, and raises `SystemExit` with a message when none is found; `scripted_input` raises `EOFError from None` when the answers are used up, which is how the game ends; no bare or silent `except`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default argument and no shadowed builtin. |
| 7 | Files, locks and connections are managed with context managers | Pass | Files are written with `Path.write_text` and `Image.save`, which close the file; the container is started with `subprocess.run`, which waits for it and removes it (`--rm`). |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class and function has a Doxygen docstring; `doxygen Doxyfile` builds `src` only, so the scripts follow the same style without being part of that build. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | These are command-line scripts: `print` is their output to the person who runs them (`wrote <file>`, the game's board), not diagnostics, and nothing secret or personal is printed. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | The scripts are development tools and are not classes of the design; [DCD-001] describes the game in `src/`, the milestone [MIL-004] lists them as deliverables, so this deviation is recorded here. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/unit/test_scripted_play.py` and `tests/unit/test_make_screenshots.py` test the helper and the drawing without Docker, in an order-free way; the Docker run itself is checked by running the script, which writes the four images that are read in the README. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy` runs in strict mode without error; no `Any` is used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | The script needs Pillow, which is declared in the `dev` extra of `pyproject.toml`; the game has no runtime dependency. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The steps, their commands and the image names are defined once in `STEPS`; the layout numbers are constants at the top of the file. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | The scripts import the game's package and Pillow only; the game imports nothing from `scripts/`. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | `make_screenshots.py` has the functions of the steps (run, draw, write) with one reason to change each; `scripted_play.py` only feeds answers to the game. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | N-A | The layered folder structure applies to the game in `src/`; `scripts/` holds the tools of the repository, as the milestone [MIL-002] defines. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | File names are English `snake_case` with letters, digits and `_` only; the images are `step-N-name.png` with `-`, which the criterion allows. |

## Overall Verdict

Go — every Mandatory criterion of [QC-PY-001] passes or does not apply for `scripts/make_screenshots.py` and `scripts/scripted_play.py`. The four screenshots in `docs/images/` are made by the script in a Docker container (`python:3.13-slim`), not on the desktop, and show the program's own output. Criteria 1, 2 and 6 of [MIL-004] are met. Autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[DCD-001]: ../../dcd.md
[MIL-002]: ../../milestones/mil-002-foundation.md
[MIL-004]: ../../milestones/mil-004-screenshots-and-readme.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[049c211]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/049c21147a1110e4dd8f9e7e3b9c8c298b721f9d
