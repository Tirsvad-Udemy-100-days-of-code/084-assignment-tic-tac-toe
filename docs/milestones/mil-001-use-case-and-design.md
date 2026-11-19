# MIL-001 Use case and design

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-004: Go | [b31f4b3] |

---

## Purpose

Decides whether the design is complete enough for code to be written: the user story, the use case and the artifacts that lead from the use case to the Design Class Diagram. No code is written before this gateway is passed.

## Deliverable

The user story US-001, the Use Case Diagram UCD-001, the use case UC-001, the Domain Model DM-001, the Domain Dictionary DICT-001, the System Sequence Diagram SSD-001, the Operation Contract OC-001, the Sequence Diagram SD-001, the Design Class Diagram DCD-001 and the decision records ADR-0001 and ADR-0002, each with its review record. The project needs no Entity Relationship Diagram, because the program stores nothing.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Each design artifact has a review record with the verdict `Go` and its latest Version History row is `Accepted` | All eleven artifacts | Any artifact without `Go` |
| 2 | Every diagram renders on the PlantUML server (`bash framework/scripts/render-diagrams.sh`) | 0 failed | Any failed diagram |
| 3 | Every method of the Design Class Diagram appears in its method traceability table and traces to a message of the Sequence Diagram | 100 % | Any method without a trace |
| 4 | Every postcondition of the Operation Contract is covered in the Postcondition Coverage table of the Sequence Diagram | 100 % | Any postcondition not covered |
| 5 | Every concept of the Domain Model has a row in the Domain Dictionary | 100 % | Any concept missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First gateway; the Business Case, the Stakeholder Analysis and the Project Plan are written with it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 objective 3, success criterion 2; story US-001 | CN-001, CN-004 |

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
| 1 | Write the user story and the use case diagram | Write US-001 with its acceptance criteria and UCD-001 with the one actor and the one use case, so that the use case has a source and a boundary. | No | |
| 2 | Write the use case | Write UC-001 Play a Game of Tic Tac Toe in the fully dressed format, with the extensions for an invalid move, a win, a draw and playing again, and the business rules of the game. | No | |
| 3 | Write the Domain Model and the dictionary | Write DM-001 with the concepts Game, Board, Cell, Player, Mark, Move, Winning Line and Result, and DICT-001 with the PO term and the IT term of each. | No | |
| 4 | Write the System Sequence Diagram and the Operation Contract | Write SSD-001 with the system operations `startGame` and `makeMove`, and OC-001 with their postconditions and the exceptions for an occupied or unknown position. | No | |
| 5 | Write the Sequence Diagram and the decision records | Write SD-001, which realises the contract across the layers Presentation, Application and Domain, ADR-0001, which records that an invalid move is rejected and the same player is asked again, and ADR-0002, which records the console presentation pattern. | No | |
| 6 | Write the Design Class Diagram | Write DCD-001 with the classes, the method traceability and the dependency check, so that code can follow it method by method. | No | |
| 7 | Render the diagrams | Check every PlantUML diagram on the PlantUML server and fix syntax errors. | No | |
| 8 | Review the artifacts | Review each artifact against its QC checklist and record an `RC-*`; fix findings until each says `Go`. | No | |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
