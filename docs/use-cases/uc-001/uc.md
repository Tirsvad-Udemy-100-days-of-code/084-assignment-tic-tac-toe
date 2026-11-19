# UC-001 Play a Game of Tic Tac Toe

## Metadata
| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [UCD-001], [US-001], [SA-001], [DM-001], [SSD-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-011: Go | pending |

---

**Format:** Fully Dressed

## Fully Dressed

- **Scope:** Tic Tac Toe system
- **Level:** user-goal
- **Primary Actor:** Player, as named in [UCD-001]
- **Stakeholders and Interests:**
  - S01 — gets a correct, finished assignment that is worth sharing
  - S02 — plays the game and compares it with their own; expects the assignment's function names
  - S03 — browses the repository; expects it to explain itself and to need no dependency
- **Preconditions:** Two Players are at the same keyboard.
- **Postconditions (success guarantee):** The game has a Result: a win for one Player or a draw. Nothing is stored.

### Main Success Scenario

1. The Player starts a Game.
2. The system shows an empty Board; the Player with the Mark `X` is first.
3. The system asks the Player whose turn it is for a Cell.
4. The Player chooses a free Cell by its number.
5. The system puts the Player's Mark in the Cell and shows the Board.
6. The system checks whether the Player has a Winning Line; if not, and a Cell is still free, it gives the turn to the other Player and the use case continues at step 3.
7. The system tells the Players the Result: the winner, or a draw.
8. The system asks whether the Players want another Game.
9. The Players say no and the system ends.

### Extensions (Alternative / Exception Flows)

- 4a. The chosen Cell is taken, the number is outside 1 to 9 or the answer is not a number:
  1. The system tells the Player why the Move is not allowed.
  2. The Board does not change, and the use case continues at step 3 with the same Player.
- 9a. The Players say yes to another Game:
  1. The use case continues at step 2 with an empty Board.
- \*a. The Players end the program at any time (end of input or an interrupt):
  1. The system ends without a Result.

### Special Requirements / Business Rules

| Step | Rule |
| --- | --- |
| 2 | The Board has nine Cells numbered 1 to 9, from left to right and from top to bottom; the Player with the Mark `X` is first and the Marks alternate |
| 4 | A Move chooses exactly one Cell by its number |
| 4a | A Move that is not allowed is rejected and the same Player is asked again; the turn is never lost and the Board never changes (decision [ADR-0001]) |
| 6 | A Winning Line is any of the eight lines of three Cells: three rows, three columns and two diagonals |
| 6 | The Result is a draw when all nine Cells hold a Mark and no Player has a Winning Line |
| 9 | Only the answers `y` and `yes`, in any case, mean yes; every other answer means no |

### Open Issues

None.

---

[UCD-001]: ../../use-case-diagram.md
[US-001]: ../../user-stories.md
[SA-001]: ../../stakeholder-analysis.md
[DM-001]: ../../domain-model.md
[SSD-001]: ./ssd.md
[ADR-0001]: ../../adr/adr-0001-invalid-moves-are-rejected.md
