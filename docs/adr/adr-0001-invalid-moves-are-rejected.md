# ADR-0001 Invalid moves are rejected

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [UC-001], [OC-001], [SD-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-018: Go | [b31f4b3] |

---

## Context

A Player may choose a Cell that is already taken, a number outside 1 to 9 or something that is not a number (for example `x` or an empty line). The assignment does not say what the game must do. Three options exist: skip the turn of the Player (the Player loses the Move), end the game with an error, or reject the Move and ask the same Player again. Skipping a turn punishes a typing mistake and changes who wins. Ending the game throws away a game that two people are playing. The forces are fairness between the Players (S01), a game that S02 can play without it breaking, and a simple use case that is easy to test.

## Decision

The game rejects a Move that is not allowed with an `InvalidMoveError` that gives the reason, tells the Player why, and asks the same Player again; the Board never changes and the turn is never lost.

## Consequences

**Positive:**

- A typing mistake never changes the Board or the turn, so the game stays fair.
- The behaviour is easy to test: one error type, three reasons, and a scripted game that mixes bad and good input.
- The error is specific, so the use case does not need to catch every `ValueError`.

**Negative:**

- A Player who cannot or will not choose a free Cell keeps being asked; the Players end the program with an interrupt or the end of input (extension *a of [UC-001]).
- The use case has a loop inside the loop of the turns.

## Affected Artifacts

- [UC-001] — extension 4a and the business rule for step 4a follow this decision
- [OC-001] — the exceptions of `makeMove`
- [SD-001] — the `create(reason)` message and the alternative of `makeMove`

---

[UC-001]: ../use-cases/uc-001/uc.md
[OC-001]: ../use-cases/uc-001/oc.md
[SD-001]: ../use-cases/uc-001/sd.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
