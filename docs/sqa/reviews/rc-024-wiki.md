# Review Record: WIKI against QC-WIKI-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-024 |
| CrossReference | [WIKI], [QC-WIKI-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go-with-conditions (autonomous, not independent) | pending |

---

## Artifact Under Review

- Instance reviewed: [WIKI]
- Checklist used: [QC-WIKI-001] and [QC-LANG-001]
- Scope: full review of docs/wiki (English, Danish and Bahasa Malaysia)
- Language and domain: en (PO language), da and ms (added languages) / it
- Language reviewer: none yet; a reader of Danish and a reader of Bahasa Malaysia are needed (see the action items)
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | The sidebar starts with the title `**Tic Tac Toe wiki**`, then one list of the English pages, `Home` first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | The list links all seven English pages (Home, Getting-Started, Step-1 to Step-4, Summary); a script that read the 109 internal links of the 22 files found no link to a missing page. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | The wiki has no related wikis, so it has no `**Related**` section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | The last section is `**Languages**` with `English: [Home](Home)`, `Dansk: [Hjem](Home-da)` and `Bahasa Melayu: [Utama](Home-ms)`. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once; the sidebar has no list per language. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written and kept by hand in `docs/wiki/`, not produced by a generator, so it needs no generator comment. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line at the top, so the sidebar is not the only way to switch language. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | The wiki exists in English and in Danish and Bahasa Malaysia; the PO language is `en` (the registry), so English is the minimum and the other two are added on top. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | The 7 English pages have 7 Danish and 7 Malay pages: 21 pages plus the sidebar, 22 files; a script compared the sets. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line, the current language in bold and a link to the same page in the two others (for example `[English](Step-3-Find-the-Winner) · **Dansk** · [Bahasa Melayu](Step-3-Find-the-Winner-ms)`). |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Danish pages are named `<Page>-da.md` and Malay pages `<Page>-ms.md`, both BCP 47 codes; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Code blocks, commands, file names, function names and IDs are the same in the three languages; only the text around them is translated. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | The published wiki is checked after the merge (task 7 of [MIL-005]); until then this cannot be Pass. A delta re-review of this criterion follows the check. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional; the layout rules did not change in this wiki. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | `docs/wiki/` is flat: the 21 pages and `_Sidebar.md` are directly in it, and the languages are told apart by the file name. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | N-A | The wiki pages are not artifacts with a Metadata table; the language is stated by the file name (`-da`, `-ms`, or no suffix for English) and by the language line on each page. The PO language `en` and the domain `it` are those of the registry. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | The codes `en`, `da` and `ms` are BCP 47 codes; the domain `it` is a row of the domain list of `docs/artifact-registry.md`. |
| 3 | The content (prose and table cells) is written in the stated language | Pending | The English pages are written in English (Pass). The Danish and Malay pages are written in those languages, but no reader of Danish or of Bahasa Malaysia has checked them yet; the reviewer wrote them and cannot judge them as an independent reader. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives the register of the wiki as readers of the repository; the text assumes a course participant who can read basic Python and explains the rest. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pending | The English pages use the terms of the dictionary [DICT-001] (player, board, cell, mark, move, winning line, result, game). The Danish and Malay terms (spiller, bræt, felt, mærke; pemain, papan, petak, tanda) are the translator's choice and need a reader of each language. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Section headings and statuses of the English pages are English; the headings of the translations are in their language on purpose, because they are content of the wiki and no script reads them. IDs (ADR-0001, ADR-0002), code and commands stay English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `<name>.<language>.md` exists; translations are named `<Page>-<code>.md` as `framework/process/wiki.md` says, which is the wiki's own rule and not a twin. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | This is the first version of the wiki; the language and domain did not change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pending | A reader competent in the domain and in Danish, and one in Bahasa Malaysia, has not yet confirmed the pages. The English pages are checked by the reviewer, who reads English and knows the IT domain; this is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (ADR, venv, Doxygen, pytest, Docker) are established names or are explained on the page where they appear. |

## Overall Verdict

Go-with-conditions — Mandatory criterion 14 and criteria 3, 5 and 9 of [QC-LANG-001] are Pending, so the verdict is Go-with-conditions, which criterion 4 of [MIL-005] allows. The English wiki passes every applicable criterion. Criterion 14 is closed by a delta re-review after the merge; criteria 3, 5 and 9 for the Danish and Malay pages stay Pending until a reader of each language has checked them. Autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Close criterion 14 with a delta re-review after the merge, once the published wiki, its sidebar and its links have been read on the git host | S01 | 2026-11-20 |
| Have a reader of Danish and a reader of Bahasa Malaysia check criteria 3, 5 and 9 of QC-LANG-001 for the `-da` and `-ms` pages, and correct what they find | S01 | Before the wiki is shared beyond the course (no date set) |

---

[DICT-001]: ../../dictionary.md
[MIL-005]: ../../milestones/mil-005-wiki.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[WIKI]: ../../wiki/Home.md
