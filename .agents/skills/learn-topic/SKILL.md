---
name: learn-topic
description: "Deep-research a topic into one Domain/Topic folder (3 files) + index + log."
invocation: model
---

# Learn-Topic

Turn "research X" into one concise, visual, human-reviewable package. Compress — never dump.

## Start

1. Read `AGENTS.md`, `.agents/taxonomy.json`, `index.md`.
2. Pick domain from taxonomy (niche → nest one deeper, e.g. `AI-Engineering/RAG/<Slug>/`).
3. Web-research: prioritize docs → papers → popular connected blogs → production OSS repos (stars + recent commits + real users). Record misses honestly.

## Write (exactly 3 files, from templates)

- `<Domain>/<Slug>/README.md` ← `.agents/templates/topic-readme.md`
- `<Domain>/<Slug>/resources.md` ← `.agents/templates/topic-resources.md`
- `<Domain>/<Slug>/build.md` ← `.agents/templates/topic-build.md`

Keep budgets in `.agents/config.json`. One Mermaid diagram in README. Wikilinks ≤ budget.
`related` ≤ 4, only to notes that exist.

Must cover the six: resources, OSS codebase (pinned commit, reading guide — go to the
repo, don't tutorial-hell), assignment (3 levels in `build.md`), use cases, AI-era
leverage scenarios, missed aspects.

## Finish

1. Set frontmatter `status: researched`, `updated: <today>`.
2. Add one row to `index.md`, append one line to `log.md`, create/update `<Domain>/_MOC.md` (≤30 lines).
3. Run `python3 .agents/bin/check.py` and fix failures. Report: what was researched,
paths, what was inspected vs UNVERIFIED/NOT INSPECTED, limits.

Never mark `human-reviewed` — human flips that checkbox in `build.md`.
