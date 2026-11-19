# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [UCD-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-001: Go | [b31f4b3] |

---

## Executive Summary

This project turns the Day 84 assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" ("Assignment: Tic Tac Toe", a text-based version of the game for two players) into a readable, runnable and tested Python repository. It delivers a small Python package with the assignment's function names, a command-line game, a README, and a three-language wiki (English, Danish, Bahasa Malaysia) that explains what each lecture step teaches, with one screenshot of the program per step. The code is written only from accepted design artifacts: a use case, its Sequence Diagram and the Design Class Diagram. The project proceeds because it is small, needs no external data or runtime dependency, and serves both the course participant and the people who compare solutions.

## Methodological and Standards Foundation

The project follows the Software Quality Assurance (SQA) and Quality Control (QC) framework mounted at `framework/`: artifacts are reviewed against their QC checklists, and quality criteria are tagged with ISO/IEC 25010:2023 characteristics. Domain modelling and design follow Larman's *Applying UML and Patterns* (use case, Domain Model, System Sequence Diagram, Operation Contract, Sequence Diagram, Design Class Diagram). Source code follows the Python conventions of the `coding-conventions` skill and the layering of the `clean-architecture` skill. Source comments use the Doxygen style.

## Problem Statement

The assignment is one sentence on the course platform: build a text-based version of Tic Tac Toe, in about 90 minutes. A participant who solves it has a script that lives on a laptop: no instructions to run it, no tests, no design that explains the choices made and no way for others to compare their solution with it. Many fellow participants have submitted a solution, so the value is in the process and in readable code, which a bare script does not record.

## Business Opportunity

A clean repository makes the solution reusable as a reference for other course participants and as a portfolio piece, and a wiki records what was learned in each step in three languages.

## Objectives

1. Provide a Python package with the assignment's functions `print_board`, `check_winner`, `is_board_full` and `play_game`, with the marks and the winning lines in `constants.py`.
2. Provide a text-based game for two players that runs from the command line: draw the board, take turns, reject invalid moves, announce a win or a draw and offer another game.
3. Write no code without a use case: the use case, its Domain Model, System Sequence Diagram, Operation Contract, Sequence Diagram and the Design Class Diagram are accepted before the first line of code, and every function traces to a method of the Design Class Diagram.
4. Provide automated tests (pytest) that check the board, the winner rule, the draw rule and the game from the command line against the use case and the Operation Contract.
5. Provide a README from the framework template with set-up, run and test instructions, including how to create and use a local `.venv` and `python -m pip install --upgrade pip`.
6. Provide a wiki in English, Danish and Bahasa Malaysia with a Getting Started guide for Linux and Windows and a page per lecture step that explains what was gained, each with a screenshot of the program (not of the lecture).
7. Document the source with Doxygen comments and provide a `Doxyfile` that builds without warnings.
8. Publish the repository with a description and topics, and scan with opengrep before every push.

## Scope

### In Scope

- The Day 84 assignment "Tic Tac Toe", summarised in words.
- The use case, the design artifacts and their reviews.
- A Python package under `src/`, tests under `tests/`, the Doxyfile, the README and the wiki under `docs/wiki/`.
- `pyproject.toml`, a Python `.gitignore`, a `.venv` guide, `.editorconfig`, `.env.example`.
- Screenshots of the program's own output for each lecture step, produced in a Docker container (Linux), never of the lecture.
- A local scan with opengrep before every push.
- The repository description and topics on the git host.

### Out of Scope

- Other days of the bootcamp.
- A computer opponent, a graphical or web interface, a network game, a score that is kept between runs, and boards larger than 3 by 3.
- Screenshots or text copied from the lecture or the course platform; the lecture is only summarised.
- Anything that reads or imports `.env`: the file holds the personal tokens used for the git host and is never part of the program.

## Expected Benefits

### Tangible Benefits

- A repository that runs with three commands and passes its tests.
- A step-by-step, three-language wiki that can be reused as a pattern for later days.

### Intangible Benefits

- Practice in building a small project from scratch with a design, tests, documentation and a repeatable set-up.
- A pattern for a course assignment that follows the framework's plan-first workflow.

## Strategic Alignment

The project supports the course participant's goal of completing the bootcamp with work worth sharing, and it practises the framework's plan-first workflow on a small project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The rules are correct | A row, a column or a diagonal of one symbol is a win; a full board without a winner is a draw; 100 % of the tests pass | `python -m pytest` exit code 0 |
| 2 | Code follows the design | 100 % of the functions in `src/` appear in the method traceability table of the Design Class Diagram, and the code review record says `Go` | review record of the code |
| 3 | The game is playable | A scripted game from the command line ends in a win, and another in a draw, with exit code 0 | integration tests |
| 4 | Documentation languages | 3 of 3 wiki languages with the same page set | file listing of `docs/wiki/` |
| 5 | Screenshots | One screenshot per lecture step, in the README and in each wiki language, none from the lecture | file listing of `docs/images/` and review of the wiki |
| 6 | Security scan | 0 findings from opengrep before each push | opengrep exit code |
| 7 | Runtime dependencies | 0 | `dependencies` in `pyproject.toml` is empty |
| 8 | Source documentation | Doxygen builds with 0 warnings | `doxygen Doxyfile` output |
| 9 | Repository is published | Description and at least 5 topics set | the git host's API |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| A personal token leaks into the repository | Account compromise | `.env` is ignored by git, is never read by the project code, is never printed or put on a command line, and the opengrep secrets rules scan every push |
| Lecture or platform content is copied into the README or wiki | A copyright problem | The lecture is only summarised; the screenshots are of the program's own output, produced from the code |
| Screenshots drift from the code | The documentation misleads | One script regenerates all screenshots from the code |
| The assignment text is one sentence and its downloadable resources are not available to the author, so the expected function names and lecture steps are not given | S02 may expect other names or steps | The names follow the solutions that fellow participants share; the steps are the four build-up steps of the game; both are recorded in the Project Plan's Open Issues and are changed on S01's word |
| Every document is reviewed in autonomous mode, so the author and the reviewer are not independent | A defect is missed | Each review record says `Mode: autonomous, not independent`, and the end-of-run summary lists every review for challenge |

## Assumptions

- S01 is the Product Owner, developer and reviewer.
- The Product Owner (PO) language is English and the PO domain is IT (information technology).
- "Python greater than 3.13" means Python 3.13 or newer (`requires-python = ">=3.13"`); Python 3.13 is installed on the machine of S01.
- The repository is the one named by the `origin` remote of this checkout, in the organisation `Tirsvad-Udemy-100-days-of-code`; the address with underscores in the request redirects to that organisation.
- "A screenshot for each lecture step" means a screenshot of the program's output for each step, since screenshots of the lecture are not allowed.
- The lecture steps are four: draw the board, take a turn, find the winner or a draw, and loop with play again. The assignment's own function names are `print_board`, `check_winner`, `is_board_full` and `play_game`.

## Constraints

- Target completion: 2026-11-22.
- No code without a use case: code is written only from the accepted use case, Sequence Diagram and Design Class Diagram.
- Python 3.13 or newer, a local `.venv`, configuration in `pyproject.toml`, tests with pytest, constants in `constants.py`.
- Folder structure `src/`, `tests/`, `docs/`.
- No runtime dependencies; development tools are development extras.
- One branch and one pull request per milestone, tracked by issues.
- Tokens are read from `.env` for personal use only; they are never printed, committed, imported or tested.
- Wiki in English, Danish and Bahasa Malaysia.
- No artifact of the project, and no commit message, names or credits an automated assistant.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About four working days of effort by S01; no licence or hosting cost | A shareable, tested reference solution with its design and a three-language explanation; the justification is qualitative because the project has no revenue |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment and owns the result |
| S02 | Runs and compares the code |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, needs no data or dependency and serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[UCD-001]: ./use-case-diagram.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
