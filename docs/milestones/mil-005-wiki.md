# MIL-005 Three-language wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-008: Go | [b31f4b3] |

---

## Purpose

Decides whether the wiki explains what each lecture step gained, in English, Danish and Bahasa Malaysia, with the same page set in each language and a screenshot per step.

## Deliverable

`docs/wiki/` with `Home`, `Getting-Started` (Linux and Windows), four step pages, `Summary` and `_Sidebar` in English, and the same pages with the suffixes `-da` and `-ms`; the traceability matrix; the review record of the wiki.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The page set of `docs/wiki/` is the same in `en`, `da` and `ms` | 3 of 3 | Any page missing |
| 2 | Every step page has its screenshot from `docs/images/` and a section on what was gained | 4 of 4 per language | Any missing |
| 3 | No screenshot or text of the lecture is in the wiki | 0 | Any |
| 4 | The wiki review record against `QC-WIKI-001` and `QC-LANG-001` | `Go` (the criteria that need a reader of the language stay `Pending` and the verdict is `Go-with-conditions` until a reader has checked them) | `No-Go` |
| 5 | The framework check scripts and opengrep | 0 findings | Any finding |
| 6 | After the merge, the published wiki shows every page and the sidebar | All pages | Any missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | The wiki uses the screenshots and mirrors the README |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 objective 6, success criterion 4 and 5 | CN-003, CN-005 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-22 — the Business Case constraint (completion by 2026-11-22).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki | `Home`, `Getting-Started` (Linux and Windows), the four step pages, `Summary` and `_Sidebar`, with what was gained in each step and its screenshot. | No | |
| 2 | Write the Danish wiki | The same pages in Danish (`-da`), with the language line on each page. | No | |
| 3 | Write the Bahasa Malaysia wiki | The same pages in Bahasa Malaysia (`-ms`), with the language line on each page. | No | |
| 4 | Review the wiki | Review against `QC-WIKI-001` and `QC-LANG-001` and record the `RC-*`; fix findings. | No | |
| 5 | Write the traceability matrix | Create `docs/sqa/traceability-matrix.md` that lists every document and its latest review. | No | |
| 6 | Run the framework checks | Run the check scripts and opengrep and fix findings. | No | |
| 7 | Verify the published wiki | After the merge, read the wiki on the git host and check that the sidebar and all pages are there. | No | |

---

[BC-001]: ../business-case.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
