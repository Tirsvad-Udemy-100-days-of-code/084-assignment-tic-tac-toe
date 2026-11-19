# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>No checklist exists for the matrix; accepted by S01 (autonomous, not independent) | [f014079] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [PP-001], [UCD-001] | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001], [UCD-001], [UC-001], [DICT-001] | [RC-002] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-003] |
| [MIL-001] | Milestone | en | it | [BC-001], [PP-001] | [US-001], [UCD-001], [UC-001], [DM-001], [DICT-001], [SSD-001], [OC-001], [SD-001], [DCD-001], [ADR-0001], [ADR-0002] | [RC-004] |
| [MIL-002] | Milestone | en | it | [BC-001], [PP-001] | [MIL-003] | [RC-020] |
| [MIL-003] | Milestone | en | it | [BC-001], [PP-001], [DCD-001] | source code, [MIL-004] | [RC-006], [RC-021] |
| [MIL-004] | Milestone | en | it | [BC-001], [PP-001], [MIL-003] | README, scripts, [MIL-005] | [RC-007], [RC-023] |
| [MIL-005] | Milestone | en | it | [BC-001], [PP-001], [MIL-004] | WIKI, [TM-001] | [RC-008] |
| [US-001] | User Story | en | it | [BC-001], [UCD-001] | [UC-001], [MIL-003] | [RC-009] |
| [UCD-001] | Use Case Diagram | en | it | [SA-001], [BC-001] | [US-001], [UC-001] | [RC-010] |
| [UC-001] | Use Case | en | it | [UCD-001], [US-001], [SA-001] | [DM-001], [SSD-001], [ADR-0001], [ADR-0002] | [RC-011] |
| [DM-001] | Domain Model | en | it | [UC-001], [UCD-001] | [SSD-001], [OC-001], [DCD-001], [DICT-001] | [RC-012] |
| [DICT-001] | Domain Dictionary | en | it | [BC-001], [SA-001], [DM-001] | [OC-001], [DCD-001], README, WIKI | [RC-013] |
| [SSD-001] | System Sequence Diagram | - | - | [UC-001], [DM-001] | [OC-001] | [RC-014] |
| [OC-001] | Operation Contract | - | - | [SSD-001], [DM-001] | [SD-001], [ADR-0001] | [RC-015] |
| [SD-001] | Sequence Diagram | - | - | [OC-001], [DCD-001] | [DCD-001], source code | [RC-016] |
| [DCD-001] | Design Class Diagram | - | - | [DM-001], [SD-001], [DICT-001] | source code, [ADR-0002] | [RC-017] |
| [ADR-0001] | Architecture Decision Record | - | - | [UC-001], [OC-001], [SD-001] | source code | [RC-018] |
| [ADR-0002] | Architecture Decision Record | - | - | [UC-001], [SD-001], [DCD-001] | source code | [RC-019] |
| Source code (`src/`, `tests/`) | Source code | - | - | [DCD-001], [ADR-0001], [ADR-0002], [MIL-003] | README, WIKI | [RC-021] |
| Scripts (`scripts/`) | Source code | - | - | [MIL-004] | README, WIKI | [RC-023] |
| README | Documentation | en | it | [MIL-004], [DICT-001] | WIKI | [RC-022] |
| WIKI (`docs/wiki/`) | Wiki | en, da, ms | it | [MIL-005], README, [DICT-001] | - | [RC-024] |
| [TM-001] | Traceability Matrix | - | - | [BC-001] | - | - |
| RC-001 to RC-024 | SQA Review Record | - | - | the reviewed instance and its checklist | - | - |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [UC-001], [OC-001], [SD-001], [DCD-001] | [ADR-0001] | none; the tests in `tests/` and the code review [RC-021] | Covered |
| CN-002 | [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | - | none; the review records [RC-001] to [RC-024] | Covered |
| CN-003 | README, [MIL-004] | - | none; [RC-022] and `framework/scripts/check-readme.sh` | Covered |
| CN-004 | [DCD-001], source code | - | none; [RC-021] (criterion 10) and the tests | Covered |
| CN-005 | README, WIKI | - | none; [RC-022], [RC-024] | Covered |
| CN-006 | [MIL-003] criterion 7 | - | none; `dependencies = []` in `pyproject.toml`, [RC-021] (criterion 13) | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | [MIL-002], [RC-020] | Criterion 9 of [MIL-002] said no file may contain the two-letter word for the tool, but `AGENTS.md` and `.gitignore` do; the criterion was reworded | RC-005 (deleted) | Closed | [RC-020] |

## Coverage Notes

- `-` in Upstream means the row is foundational; in Downstream it means nothing is built on it yet; in Last Reviewed it means no review record exists for it (the Traceability Matrix and the review records are not reviewed by a checklist).
- No Test Plan (`TP`) exists: the quality checks of the concerns are the tests of the project and the review records. This is a deliberate gap in the artifact set, not in the concerns.
- The type `Documentation` (README) and `Wiki` have no artifact ID; they are listed by name and reviewed in [RC-022] and [RC-024].
- RC-005 was deleted after the full re-review [RC-020] superseded it.
- Criterion 14 of [RC-024] and its Danish and Malay language criteria are open; they are listed in its action items.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-use-case-and-design.md
[MIL-002]: ../milestones/mil-002-foundation.md
[MIL-003]: ../milestones/mil-003-game.md
[MIL-004]: ../milestones/mil-004-screenshots-and-readme.md
[MIL-005]: ../milestones/mil-005-wiki.md
[US-001]: ../user-stories.md
[UCD-001]: ../use-case-diagram.md
[UC-001]: ../use-cases/uc-001/uc.md
[DM-001]: ../domain-model.md
[DICT-001]: ../dictionary.md
[SSD-001]: ../use-cases/uc-001/ssd.md
[OC-001]: ../use-cases/uc-001/oc.md
[SD-001]: ../use-cases/uc-001/sd.md
[DCD-001]: ../dcd.md
[ADR-0001]: ../adr/adr-0001-invalid-moves-are-rejected.md
[ADR-0002]: ../adr/adr-0002-console-is-reached-through-a-view-interface.md
[TM-001]: ./traceability-matrix.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-use-case-and-design.md
[RC-006]: ./reviews/rc-006-mil-003-game.md
[RC-007]: ./reviews/rc-007-mil-004-screenshots-and-readme.md
[RC-008]: ./reviews/rc-008-mil-005-wiki.md
[RC-009]: ./reviews/rc-009-user-story.md
[RC-010]: ./reviews/rc-010-use-case-diagram.md
[RC-011]: ./reviews/rc-011-use-case.md
[RC-012]: ./reviews/rc-012-domain-model.md
[RC-013]: ./reviews/rc-013-dictionary.md
[RC-014]: ./reviews/rc-014-ssd.md
[RC-015]: ./reviews/rc-015-operation-contract.md
[RC-016]: ./reviews/rc-016-sequence-diagram.md
[RC-017]: ./reviews/rc-017-dcd.md
[RC-018]: ./reviews/rc-018-adr-0001-invalid-moves-are-rejected.md
[RC-019]: ./reviews/rc-019-adr-0002-console-view-interface.md
[RC-020]: ./reviews/rc-020-mil-002-foundation.md
[RC-021]: ./reviews/rc-021-mil-003-game-code.md
[RC-022]: ./reviews/rc-022-readme.md
[RC-023]: ./reviews/rc-023-mil-004-scripts.md
[RC-024]: ./reviews/rc-024-wiki.md
[f014079]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/f01407984492ea93f20ba7951af6f4d142c87da4
