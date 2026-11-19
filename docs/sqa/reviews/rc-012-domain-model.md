# Review Record: DM-001 against QC-DM-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [DM-001], [QC-DM-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | pending |

---

## Artifact Under Review

- Instance reviewed: [DM-001]
- Checklist used: [QC-DM-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Uses ubiquitous/business language throughout; no technical or implementation jargon (e.g. no "table", "class", "pointer") | Pass | The concepts are Game, Board, Cell, Player, Mark, Move, Winning Line and Result; none is a technical term. |
| 2 | Multiplicities on associations are correct and complete (e.g. `1..*`, `0..1`) | Pass | Every association in the diagram and in the Association Table has a multiplicity. |
| 3 | No operation/method signatures shown — attributes and associations only | Pass | The diagram shows attributes and associations only. |
| 4 | Associations are named with an unambiguous reading direction | Pass | Every association has a name with a reading direction (for example "is played on >"). |
| 5 | Generalization/specialization used correctly, reflecting true "is-a" relationships, not misused for code reuse | Pass | There is no generalization, so none can be misused. |
| 6 | Every concept traces to a noun phrase found in the use cases or glossary | Pass | Every concept has a source in [UC-001] in the Concept Table. |
| 7 | Attributes are simple domain data (no foreign-key-like references or object pointers modeled as attributes) | Pass | The attributes are simple data (played on, size, row, column, turn order, symbol, order, name, outcome); no object reference is an attribute. |
| 8 | The Purpose names the concerns (`CN-NNN`) the Domain Model answers and the stakeholders it serves, so its viewpoint is stated | Pass | The Purpose names the concern CN-001 of [SA-001] and the stakeholders S01 and the domain experts. |
| 9 | No technical solution names: only conceptual classes of the Product Owner's world, never a file, an environment variable, a setting source, a database, a table, an API, a service, a cache or any other mechanism | Pass | No file, setting, database, table, API, service or cache is named. |
| 10 | No empty concept: every concept has at least one attribute and at least one association | Pass | Every concept has at least one attribute and at least one association (Game: played on and four associations; Cell: row and column and four associations). |
| 11 | A Domain Model written for one use case reuses the concepts, attributes, associations and names of the project Domain Model, and its additions and changes are added to the project Domain Model | N-A | This is the project Domain Model itself; the criterion does not apply to it. |
| 12 | The software is a black box and a normal person can read the model: no concept or attribute exists only because the software exists (a run, command, option, mode, step, exit code, log, session, question, prompt, summary or other screen or tool element); no attribute is computed from other concepts, and none is an identifier or a storage type; every concept in the Concept Table has a one-sentence definition in everyday words with no IT term | Pass | A reader who has not seen the software understands the model: every concept is a part of the game on a table; no attribute is computed or an identifier, and each definition is one sentence in everyday words. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table of DM-001 has `Language | en` and `Domain | it`; neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `it` is a row of the domain list of `docs/artifact-registry.md`. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The prose and the table cells are English; only IDs, file names, commands and code names are code. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives the register of this type; the text is written for that reader. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The text uses the terms of the dictionary [DICT-001] (Player, Board, Cell, Mark, Move, Winning Line, Result, Game) in one meaning each and no synonym. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are the framework's English ones. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `<name>.<language>.md` exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | This is the first version, so there is no earlier language or domain to compare; the Version History row records it. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The reviewer reads English and knows the IT domain and checked the terms against the dictionary [DICT-001]; the check is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out where first used or are established names (README, Doxygen, pytest, UML). |

## Overall Verdict

Go — every Mandatory criterion of [QC-DM-001] and [QC-LANG-001] passes or does not apply; the document is Accepted. Full review.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[DICT-001]: ../../dictionary.md
[DM-001]: ../../domain-model.md
[QC-DM-001]: ../../../framework/qc/artifacts/qc-domain-model.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[SA-001]: ../../stakeholder-analysis.md
[UC-001]: ../../use-cases/uc-001/uc.md
