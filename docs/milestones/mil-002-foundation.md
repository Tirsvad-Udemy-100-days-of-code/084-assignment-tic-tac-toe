# MIL-002 Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-005: Go | [b31f4b3] |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Go/No-Go criterion 9 names the files the framework supplies and the prescribed ignore line<br>Reviewed in RC-020: Go | [c7e3d42] |

---

## Purpose

Decides whether the repository is set up well enough to hold code: Python project configuration, ignore rules, editor settings, the Doxygen configuration, the local security scan, a set-up guide and a public description with topics. It contains no source code.

## Deliverable

A repository with `pyproject.toml`, a Python `.gitignore`, `.editorconfig`, `.env.example`, a `Doxyfile`, `scripts/scan.sh` for opengrep, a README skeleton with the `.venv` guide, and a description with topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"` succeed in a fresh `.venv` on Python 3.13 | Exit code 0 | Any error |
| 2 | `pyproject.toml` lists no runtime dependency | `dependencies = []` | Any entry |
| 3 | `bash scripts/scan.sh` (opengrep) reports no finding | 0 findings | Any finding |
| 4 | `.env` is ignored by git and not tracked | `git check-ignore .env` prints it and `git ls-files .env` prints nothing | Not ignored or tracked |
| 5 | `bash framework/scripts/check-editorconfig.sh` | Exit code 0 | Any finding |
| 6 | The repository has a description and at least five topics on the git host | Both set | Either missing |
| 7 | The README skeleton documents creating and using `.venv` and `python -m pip install --upgrade pip` for Linux and Windows | Both present | Either missing |
| 8 | No Python file exists under `src/` or `tests/`; each folder holds only a `.gitkeep` placeholder | No `.py` file | Any `.py` file |
| 9 | No file written by this project (outside `AGENTS.md`, `.agents/`, `.claude/` and `framework/`, which the framework supplies) names or credits an automated assistant; the one allowed match is the ignore line `/docs/ai-prompts/`, the path the framework prescribes for the prompt log | 0 other matches | Any other match |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | The configuration does not depend on the design; both are needed before MIL-003 |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 objectives 5, 7 and 8, success criteria 6, 7 and 9 | CN-003, CN-005, CN-006 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-19 — inside the Business Case constraint (completion by 2026-11-22).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml | Configure the project for Python 3.13 or newer with no runtime dependency, and pytest, ruff, mypy and pillow as development extras, so S02 and S03 can install it with one command. | No | |
| 2 | Add Python .gitignore | Ignore `.venv`, caches, Doxygen output, `.env` and the prompt log, so secrets and build output never reach the repository. | No | |
| 3 | Add Doxyfile | Add a `Doxyfile` for the Python sources with Doxygen-style comments, output to an ignored folder, and document the command in the README. | No | |
| 4 | Add .editorconfig and .env.example | Copy the framework's baseline `.editorconfig` (with the Python block) and add an `.env.example` with empty placeholders only; the program never reads `.env`. | No | |
| 5 | Add the opengrep scan script | Add `scripts/scan.sh` that runs `~/.opengrep/cli/latest/opengrep.exe` with the Python and secrets rules, and run it before every push. | No | |
| 6 | Write the .venv set-up guide | Document creating and activating `.venv` on Linux and Windows, `python -m pip install --upgrade pip` and installing the project, in the README skeleton built from the framework template. | No | |
| 7 | Set repository description and topics | Use the git host's API with the repository token from `.env` (never printed, never on a command line) to set the description and topics of the repository named by `origin`. | No | |

---

[BC-001]: ../business-case.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
[c7e3d42]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/c7e3d42d922a2ed8db7d7a794ed7dc52ab03dc91
