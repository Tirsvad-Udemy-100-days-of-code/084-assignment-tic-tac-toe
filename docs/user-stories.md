# User Stories

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [BC-001], [UCD-001], [UC-001], [MIL-003] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-009: Go | [b31f4b3] |

---

## Purpose and Scope

This document holds the candidate user story of the Tic Tac Toe game. It covers the epic "play a game of Tic Tac Toe" of the Day 84 assignment, delivered by [MIL-003] and traced to the objectives 1 to 4 of [BC-001].

## Story List

### US-001.01 — Play a game of Tic Tac Toe

- **Statement:** **As a** Player (S01, S02), **I want** to play a game of Tic Tac Toe against another Player on the same keyboard, **so that** I can see who gets three of their Marks in a line first, or that nobody does.
- **Acceptance Criteria:**
  - Given a new game, when it starts, then the Board is empty and the Player with the Mark `X` moves first.
  - Given the Players move in turn, when a Player chooses a free Cell by its number from 1 to 9, then the Board shows that Player's Mark in the Cell and the other Player is next.
  - Given a Player has three of their Marks in a row, a column or a diagonal, when the Move is made, then the game ends and the Result names that Player as the winner.
  - Given all nine Cells hold a Mark and no Player has a Winning Line, when the last Move is made, then the game ends and the Result is a draw.
  - Given a Player chooses a Cell that is taken, a number outside 1 to 9 or something that is not a number, when the Move is made, then the Player is told why the Move is not allowed, the Board does not change and the same Player is asked again.
  - Given a game has ended, when the Players say yes to another game, then a new game starts with an empty Board; when they say anything else, the program ends.
- **Traces to:** [UC-001]; epic [MIL-003].
- **Priority (MoSCoW):** Must — it is the whole assignment.
- **Size:** fits one iteration.

## INVEST Check

Independent (the only story), Negotiable (the wording of the messages and the way to say yes are open to S01), Valuable (the assignment's goal), Estimable, Small (one use case with three system operations), Testable (every acceptance criterion is a given/when/then). No exception.

---

[BC-001]: ./business-case.md
[UCD-001]: ./use-case-diagram.md
[UC-001]: ./use-cases/uc-001/uc.md
[MIL-003]: ./milestones/mil-003-game.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
