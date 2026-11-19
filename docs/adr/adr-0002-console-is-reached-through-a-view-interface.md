# ADR-0002 The console is reached through a view interface

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [UC-001], [SD-001], [DCD-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-019: Go | [b31f4b3] |

---

## Context

The game reads the Players' choices and shows the Board on a terminal. Many solutions of fellow participants call `input` and `print` inside the game loop, which makes the loop hard to test without a real terminal and mixes the rules of the game with the way they are shown. The assignment's names `print_board` and `play_game` must stay available. The forces are testability (S01), a game that S02 can read top to bottom, and the layering of the `clean-architecture` skill, which says that the Presentation layer holds the entry points and that the inner layers define the interfaces the outer layers implement. Two options were evaluated: the use case calls `input` and `print` itself, or the use case calls an interface `GameView` that the Presentation implements. The default presentation pattern for a command line, one command per use case, applies to both.

## Decision

The use case `GameUseCase` talks to the Players only through the interface `GameView` that the Application owns; `ConsoleView` in the Presentation implements it with `input` and `print`, and `PlayGameCommand.play_game` builds the view and hands it to the use case.

## Consequences

**Positive:**

- The whole flow of a game, including invalid moves and playing again, is tested with a scripted view and no terminal.
- The rules and the flow have no `print` or `input`, so the Domain and the Application depend on nothing outside.
- A later interface (a graphical one, for example) needs a new view only.

**Negative:**

- One more class and one more file than a plain loop, which is more to read for a small game.
- The assignment's `play_game()` takes no argument, so it is a thin function in the Presentation that builds the view; the use case is `run_game(view)`.

## Affected Artifacts

- [UC-001] — the use case is the flow the view serves
- [SD-001] — the lifelines `GameUseCase` and `ConsoleView` and the calls between them
- [DCD-001] — the interface `GameView` and its implementation `ConsoleView`

---

[UC-001]: ../use-cases/uc-001/uc.md
[SD-001]: ../use-cases/uc-001/sd.md
[DCD-001]: ../dcd.md
[b31f4b3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/b31f4b369e5e2228605a7241d1d616a68a5108ce
