# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-002: Go | pending |

---

## Purpose

This analysis names the people the Tic Tac Toe project serves, how much power and interest each has, and what each needs from the result. It uses the power/interest grid and maps concerns to FURPS+ attributes.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad (private) | HIGH | HIGH | Manage Closely | A correct, finished assignment that is worth sharing |
| S02 | Udemy coursists | Fellow participants of the bootcamp who share code and compare solutions | Udemy (public) | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | GitHub (public) | LOW | MEDIUM | Keep Informed | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts every plan and owns the repository; power and interest are both high.
- **Keep Informed (S02, S03):** cannot change the project but judge its usefulness; they are served by documentation, not by consultation. S03 is rated MEDIUM interest because it browses rather than runs the code, and is kept informed in the same way as S02.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The game follows the rules of Tic Tac Toe and is tested | Functionality |
| CN-002 | S01 | Work follows the plan-first process with traceable reviews and one pull request per step | Supportability |
| CN-003 | S02 | Code can be run from the README without guessing | Usability |
| CN-004 | S02 | Function names match the assignment (`print_board`, `check_winner`, `is_board_full`, `play_game`) | Usability |
| CN-005 | S03 | The repository explains itself: description, topics, README, wiki | Usability |
| CN-006 | S03 | No runtime dependencies and no hidden set-up | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat with S01 | At plan acceptance and at the end of the run | Plan dry run and run summary | All milestones |
| CR-002 | README | Each milestone that changes behaviour | Set-up, run and test instructions | MIL-004 |
| CR-003 | Wiki in English, Danish and Bahasa Malaysia | Once, after the README | Getting Started guide for Linux and Windows, one page per lecture step | MIL-005 |
| CR-004 | Repository description and topics | Once | Public summary for S02 and S03 | MIL-002 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no dependencies; S01 wants tests and screenshots | S03, S01 | The program has no runtime dependency; test and screenshot tools are development extras only |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | [BC-001] objectives 1 to 4 |
| S02 | CN-003, CN-004 | [BC-001] objectives 1, 5 and 6 |
| S03 | CN-005, CN-006 | [BC-001] objectives 6 and 8 |

## Sign-Off

Accepted by S01 when the plan is accepted in chat; reviewed in autonomous mode, not independent.

---

[BC-001]: ./business-case.md
