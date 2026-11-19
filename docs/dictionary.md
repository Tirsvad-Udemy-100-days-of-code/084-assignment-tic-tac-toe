# Domain Dictionary (PO and IT terms)

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001], [DM-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-013: Go | [b31f4b3] |

---

## Purpose and Scope

Maps each Product Owner (PO) term to its professional IT term. PO language: English (`en`); domain: IT (`it`). The dictionary covers every concept of [DM-001] and the actor of [UCD-001].

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| Board | en | `board` | The grid of three rows and three columns on which a Game is played; in the code, an object that holds nine cells | DM, UC, US | OC, SD, DCD |
| Cell | en | `cell` | One of the nine places of the Board; in the code, one entry of the board, found by its number from 1 to 9 | DM, UC, US | OC, SD, DCD |
| Game | en | `game` | One play of Tic Tac Toe from an empty Board to a Result | DM, UC, US | OC, SD, DCD |
| Mark | en | `mark` | The symbol `X` or `O` that a Player puts in a Cell; in the code, a string of length one | DM, UC, US | OC, SD, DCD |
| Move | en | `move` | A Player's choice of one Cell for their Mark; in the code, the number of the chosen cell | DM, UC, US | OC, SD, DCD |
| Player | en | `player` | One of the two people who play, first or second | UCD, DM, UC, US, SSD | OC, SD, DCD |
| Result | en | `result` | How a Game ended: a win for a Player or a draw; in the code, the winning mark or none | DM, UC, US | OC, SD, DCD |
| Winning Line | en | `line` | Any of the eight lines of three Cells: a row, a column or a diagonal; in the code, a tuple of three cell numbers | DM, UC, US | OC, SD, DCD |

## Rules

- The Domain Model, use cases and user stories use the PO term; the Operation Contract, Sequence Diagram, Design Class Diagram and ERD use the IT term.
- One IT term per PO term and one PO term per IT term; no synonyms.
- Rows are in ascending order of the PO term (case-insensitive, by the alphabet of the PO language), so a term is found without searching.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[DM-001]: ./domain-model.md
[UCD-001]: ./use-case-diagram.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
