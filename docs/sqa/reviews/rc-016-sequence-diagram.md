# Review Record: SD-001 against QC-SD-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [SD-001], [QC-SD-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | [b31f4b3] |

---

## Artifact Under Review

- Instance reviewed: [SD-001]
- Checklist used: [QC-SD-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Message passing strictly follows UML sync/async/return arrow syntax | Pass | The diagrams use solid arrows for calls and dashed arrows for returns. |
| 2 | GRASP/GoF patterns applied and explicitly annotated where used (e.g. Controller, Observer, Mediator, Factory) | Pass | The Pattern Annotations table names Controller, Information Expert, Low Coupling, Protected Variations and Adapter. |
| 3 | Lifelines show activation bars matching actual processing time/call nesting | Pass | Activation bars follow the call nesting of `play_game`, `run_game`, the view calls and `place`. |
| 4 | Object creation and destruction shown with correct UML notation (`create`/`destroy` messages, X on lifeline) | Pass | `Board`, `ConsoleView` and `InvalidMoveError` are shown with `create` messages. |
| 5 | Diagram realizes the postconditions of a specific Operation Contract | Pass | Each of the three sequences has a Postcondition Coverage table that lists every postcondition of its contract. |
| 6 | Responsibility assignment favors low coupling/high cohesion (no god-object receiving all messages) | Pass | No object receives all messages; the Responsibility Check says why. |
| 7 | Loop, alt, and opt combined fragments used correctly for conditional/repeated behavior | Pass | The `loop` and `alt` fragments show the repeated turns, the invalid move, the win, the draw and the next turn. |
| 8 | Each exception of the realized Operation Contract is shown as an `alt` or `opt` fragment, or its absence is justified | Pass | The two exceptions of `makeMove` are the `alt` of the invalid move. |
| 9 | The Purpose names the concerns (`CN-NNN`) the Sequence Diagram answers and the stakeholders it serves, so its viewpoint is stated | Pass | The Purpose names the concerns CN-001, CN-003 and CN-004 of [SA-001] and the stakeholders S01 and S02. |
| 10 | When the design uses a layered architecture (Clean, Hexagonal, Onion or similar), the lifelines are grouped by layer and calls across a layer boundary go through the inner layer's interface | Pass | The lifelines are in boxes for Presentation, Application and Domain; the use case calls the view through the interface `GameView` of [ADR-0002]. |
| 11 | When the design uses a layered architecture, each layer is drawn in its fixed pastel colour: Delivery `#FADADD`, Application `#FFF3B0`, Domain `#CDEFD3`, Infrastructure `#D4E4F7` | Pass | The boxes use the fixed colours: Presentation `#FADADD`, Application `#FFF3B0` and Domain `#CDEFD3`. |

## Overall Verdict

Go — every Mandatory criterion of [QC-SD-001] passes or does not apply; the document is Accepted. Full review.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[ADR-0002]: ../../adr/adr-0002-console-is-reached-through-a-view-interface.md
[OC-001]: ../../use-cases/uc-001/oc.md
[QC-SD-001]: ../../../framework/qc/artifacts/qc-sequence-diagram.md
[SA-001]: ../../stakeholder-analysis.md
[SD-001]: ../../use-cases/uc-001/sd.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
