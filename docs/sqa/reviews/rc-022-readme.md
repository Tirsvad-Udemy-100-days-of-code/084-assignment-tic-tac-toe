# Review Record: README against QC-LANG-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-022 |
| CrossReference | [README], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | pending |

---

## Artifact Under Review

- Instance reviewed: [README]
- Checklist used: [QC-LANG-001]
- Scope: full review against QC-LANG-001 only
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | N-A | The README follows the framework's README template, which has no Metadata table; the language `en` and the domain `it` are those of the project in `docs/artifact-registry.md`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | N-A | The README has no `Language` or `Domain` row to check; the registry states `en` (a BCP 47 code) and `it` (a row of its domain list) for the project. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The prose and the table cells are English; only commands, file names and code names are code. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The reader is a course participant or a visitor of the repository (S02, S03): the text explains how to set up, run and test, and assumes no knowledge of the project documents. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The README uses the terms of the dictionary [DICT-001] in one meaning (player, board, cell, mark, game); the file and the tool names are project tooling. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | The section headings are those of the framework README template, in English and in its order; `bash framework/scripts/check-readme.sh` exits with 0. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `README.<language>.md` exists beside it. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | This is the first full version of the README; the language and domain did not change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The reviewer reads English and knows the IT domain and checked the game terms against [DICT-001]; the check is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out where first used or are established names (opengrep, Doxygen, pytest, venv, PNG). |

## Overall Verdict

Go — every Mandatory criterion of [QC-LANG-001] passes or does not apply (the framework has no checklist for a README, so its structure is checked by `framework/scripts/check-readme.sh`, exit code 0). The README has the `.venv` set-up with `python -m pip install --upgrade pip`, how to run the game, how to run the tests, the Doxygen build and the four steps with their screenshots in words and images only, and no lecture material. Criterion 7 of [MIL-004] is met. Autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[DICT-001]: ../../dictionary.md
[MIL-004]: ../../milestones/mil-004-screenshots-and-readme.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[README]: ../../../README.md
