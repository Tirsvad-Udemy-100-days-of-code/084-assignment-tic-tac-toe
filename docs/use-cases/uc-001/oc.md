# Operation Contract

## Metadata
| Key | Value |
| --- | --- |
| ID | OC-001 |
| CrossReference | [SSD-001], [DM-001], [DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-015: Go | [b31f4b3] |

---

## Contract: startGame

| Item | Value |
| --- | --- |
| Operation | `startGame(): board` |
| Traces to | message 1 `startGame` in [SSD-001] |
| Domain Model concepts | `game`, `board`, `cell`, `player`, `mark`; associations "is played on", "is played by", "is divided into", "plays with" ([DM-001]) |

**Preconditions**

- None: the program is running.

**Postconditions**

- A `game` instance was created.
- A `board` instance was created and associated with `game` ("is played on").
- Nine `cell` instances, numbered 1 to 9, were created and associated with `board` ("is divided into"); none shows a `mark`.
- Two `player` instances were created and associated with `game` ("is played by"); the first `player` plays with the `mark` `X` and the second with the `mark` `O`.
- The first `player` is the one whose `move` is next.

**Exceptions**

None.

## Contract: makeMove

| Item | Value |
| --- | --- |
| Operation | `makeMove(choice: str): (board, result)` |
| Traces to | message 2 `makeMove` in [SSD-001] |
| Domain Model concepts | `game`, `board`, `cell`, `player`, `mark`, `move`, `line`, `result`; associations "is made of", "fills", "shows", "makes", "runs through", "ends with", "names as winner", "is decided by" ([DM-001]) |

**Preconditions**

- A `game` exists and has no `result`.
- `choice` is the text of the number of a `cell` of the `board` of `game` (1 to 9), and that `cell` shows no `mark`.

**Postconditions**

- A `move` instance was created, associated with `game` ("is made of"), with the `player` whose `move` was next ("makes") and with the `cell` whose number is `choice` ("fills").
- The `cell` was associated with the `mark` of that `player` ("shows").
- If a `line` of `board` runs through three `cells` that all show the `mark` of that `player`, a `result` instance was created, associated with `game` ("ends with"), with that `player` ("names as winner") and with that `line` ("is decided by").
- Otherwise, if every `cell` of `board` shows a `mark`, a `result` instance was created and associated with `game` ("ends with"), with no winner and no `line`: a draw.
- Otherwise the other `player` is the one whose `move` is next.

**Exceptions**

| Condition (failing precondition) | Outcome |
| --- | --- |
| `choice` is not a whole number, or is outside 1 to 9 | No `move` instance was created, no `cell` changed, the same `player` is still next, and an `InvalidMoveError` that gives the reason was signalled ([ADR-0001]) |
| The `cell` whose number is `choice` already shows a `mark` | No `move` instance was created, no `cell` changed, the same `player` is still next, and an `InvalidMoveError` that gives the reason was signalled ([ADR-0001]) |

## Contract: chooseAnotherGame

| Item | Value |
| --- | --- |
| Operation | `chooseAnotherGame(answer: str): bool` |
| Traces to | message 3 `chooseAnotherGame` in [SSD-001] |
| Domain Model concepts | `game`, `result` ([DM-001]) |

**Preconditions**

- A `game` exists and has a `result`.

**Postconditions**

- If `answer` is `y` or `yes`, in any case, a new `game` was created with its `board`, `cells` and `players` as in `startGame`, and `true` is returned.
- Otherwise no `game` instance was created and `false` is returned.

**Exceptions**

None: every `answer` other than yes is no.

---

[SSD-001]: ./ssd.md
[DM-001]: ../../domain-model.md
[DICT-001]: ../../dictionary.md
[ADR-0001]: ../../adr/adr-0001-invalid-moves-are-rejected.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
