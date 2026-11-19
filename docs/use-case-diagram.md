# Use Case Diagram

## Metadata
| Key | Value |
| --- | --- |
| ID | UCD-001 |
| CrossReference | [SA-001], [BC-001], [US-001], [UC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-010: Go | pending |

---

## Purpose and Scope

The system boundary is the Tic Tac Toe program: the part of the repository that lets two Players play a game on the keyboard. The Player takes part in the game and sees the Board and the Result. The README, the wiki and the screenshots are documentation, not part of the system boundary.

## Diagram

```plantuml
@startuml
left to right direction
actor "Player" <<Actor>> as A1
rectangle "Tic Tac Toe" <<System>> {
  usecase "Play a Game of Tic Tac Toe" as UC1
}
A1 --> UC1
@enduml
```

Crossings of the chosen layout: 0 (one actor, one use case, one association).

## Actor Table

| Actor | Stereotype | Stakeholder ID (SA) | Goals (use cases) |
| --- | --- | --- | --- |
| Player | `<<Actor>>` | S01, S02 | Play a Game of Tic Tac Toe |

Two people share the keyboard and are both the actor Player, one after the other. S03 browses the repository and does not run the system, so it is not an actor.

## Use Case Table

| Use Case | Actor(s) | Goal | Source story | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- | --- |
| [UC-001] Play a Game of Tic Tac Toe | Player | Play a game to a win or a draw, and play another if wanted | [US-001] | Must | It is the whole assignment ([BC-001] objective 2) |

## Role Matrix

There is one primary actor (Player), so no role matrix is needed.

## Relationships

There is no `<<include>>` or `<<extend>>` relationship: the system has one use case.

---

[SA-001]: ./stakeholder-analysis.md
[BC-001]: ./business-case.md
[US-001]: ./user-stories.md
[UC-001]: ./use-cases/uc-001/uc.md
