# MIL-004 Screenshots and README

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-007: Go | [b31f4b3] |

---

## Purpose

Decides whether a reader can run the game from the README alone and sees what each lecture step builds: one screenshot of the program's own output per step, and a README from the framework template.

## Deliverable

`scripts/make_screenshots.py`, four screenshots in `docs/images/` (draw the board, take a turn, find the winner or a draw, loop with play again), and `README.md` with overview, requirements, `.venv` set-up, run, tests, Doxygen, the four screenshots and a short summary of the lecture in words.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/images/` holds one screenshot per lecture step | 4 files | Fewer |
| 2 | Every screenshot is produced by `scripts/make_screenshots.py` in a Docker container, not on the desktop of the host | Script and container | Any manual or desktop capture |
| 3 | No screenshot or text of the lecture is in the README | 0 | Any |
| 4 | `bash framework/scripts/check-readme.sh` | Exit code 0 | Any finding |
| 5 | The README states how to create and use `.venv`, `python -m pip install --upgrade pip`, how to run the game and how to run the tests | All four | Any missing |
| 6 | `bash scripts/scan.sh` (opengrep) and `python -m pytest` | 0 findings, exit code 0 | Any finding or failure |
| 7 | The README review record | `Go` | Any other verdict |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The screenshots show the program, so it exists and is tested first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 objectives 5 and 6, success criterion 5 | CN-003, CN-005 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-21 — inside the Business Case constraint (completion by 2026-11-22).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Generate step screenshots in a container | `scripts/make_screenshots.py` runs the program in a Docker container (Linux, Python 3.13, no desktop) for each step with scripted input, captures the text output and renders one PNG per step into `docs/images/`; nothing starts on the host's desktop (`framework/process/gui-testing.md`). | No | |
| 2 | Write the README | Create `README.md` from the framework template with overview, requirements, `.venv` set-up, run, tests, Doxygen and the four screenshots, and a short summary of the lecture in words. | No | |
| 3 | Check the README | Run `bash framework/scripts/check-readme.sh` and fix findings. | No | |
| 4 | Run the checks and record the reviews | Run opengrep and the tests, review the README, then record the `RC-*` records. | No | |

---

[BC-001]: ../business-case.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
