# Review Record: WIKI against QC-WIKI-001 (criterion 14)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-025 |
| CrossReference | [WIKI], [QC-WIKI-001], [RC-024] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go-with-conditions (autonomous, not independent) | [65c8230] |

---

## Artifact Under Review

- Instance reviewed: [WIKI]
- Checklist used: [QC-WIKI-001]
- Scope: delta re-review of criterion 14 only. Reason: [RC-024] left it Pending because the wiki is published to the git host by the merge. Earlier record: [RC-024]
- Language and domain: en, da and ms / it
- Language reviewer: none yet (see [RC-024])
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | After the merge of pull request 43 the host listed 22 wiki pages (21 pages and `_Sidebar`); the content of each, read through the host's API, equals the file in `docs/wiki/`. All 21 page addresses that the pages and the sidebar link to were fetched from the host and returned a wiki page. The sidebar and the language line render in the browser (checked on `Step-3-Find-the-Winner-da`: the title, the page list once, the `Languages` section last). The four screenshots load from the repository (status 200, `image/png`, width 1000). |

## Overall Verdict

Go-with-conditions — criterion 14 passes. The wiki stays Go-with-conditions because the Danish and Malay pages still wait for a reader of each language (criteria 3, 5 and 9 of [QC-LANG-001] in [RC-024]). The first action item of [RC-024] is closed by this record.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Have a reader of Danish and a reader of Bahasa Malaysia check criteria 3, 5 and 9 of QC-LANG-001 for the `-da` and `-ms` pages (open since [RC-024]) | S01 | Before the wiki is shared beyond the course (no date set) |

---

[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[RC-024]: ./rc-024-wiki.md
[WIKI]: ../../wiki/Home.md
[65c8230]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/084-assignment-tic-tac-toe/commit/65c8230457f46b2d7642af9365ac188ac9d930ac
