# Decisions — why, not what

| Date | Decision | Reason | Rejected alternative |
|---|---|---|---|
| 2026-10-02 | 3 files per topic, evidence in `.agents/evidence/` | Keeps Obsidian graph neat; machine proof stays out of the reading path | 7-file research package (hop hell) |
| 2026-10-02 | Offline-default gate, `--probe` opt-in for URL checks | Vault must verify without network; live checks are warnings-first | Always-online gate (flaky) |
| 2026-10-02 | Tracks: hub `<Track>.md` + N subtopic triples, budgets README≤350/build≤250/resources≤150/hub≤150 | User syllabus needs full coverage + hub navigation; 3-file cap could not hold 35 items | Single mega-note (unsearchable) / 12 flat topics (no navigator) |
| 2026-10-02 | Descriptive filenames HARD RULE: `<Slug>.md` + `<Slug>.resources.md` + `<Slug>.build.md`, banned generic list in config, gate fails violations | Obsidian graph/search shows filenames — 8× README.md nodes unreadable; user explicitly banned readme/build/sources-only names | Keep README triple + rely on frontmatter titles (invisible in graph) |
