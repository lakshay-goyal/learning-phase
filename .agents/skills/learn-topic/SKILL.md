---
name: learn-topic
description: "Deep-research a topic into one Domain/Topic folder (3 files) + receipt + index + log."
invocation: model
---

# Learn-Topic

Turn "research X" into one in-depth but compressed package. Deep process, concise output.

## Start (clock in)

1. Read `.agents/AGENTS.md`, `.agents/taxonomy.json`, `.agents/index.md`, `.agents/feature_list.json`.
2. One topic at a time (WIP=1). Set matching feature `in-progress` or add one with
(id, behavior, verification=`python3 .agents/bin/check.py`, state).
3. Pick domain from taxonomy (niche → nest one deeper).

## Research protocol (depth is mandatory, dumping is forbidden)

1. Order: official docs → papers → most-linked blogs → GitHub (stars + recent push +
real users + license). Prefer sources that cite each other — record connectedness.
2. Open ≥5 sources. For each repo candidate check: last push <12mo, tests/CI present,
real file paths noted. Never invent file paths or SHAs — open the repo or mark NOT INSPECTED.
3. Classify every link OPENED <date> or UNVERIFIED + reason. Version-pin repos (short SHA).
4. Compress: README ~800–1200 words. Cut anything that doesn't change what the human builds.

## Write (exactly 3 files, from templates)

- `<Domain>/<Slug>/README.md`, `resources.md`, `build.md` — follow template headings exactly.
- Must cover the six: resources, pinned OSS codebase + reading guide, 3 assignments,
use cases, AI-leverage scenarios, missed aspects. One Mermaid diagram in README.
- Frontmatter `status: researched`. Never `human-reviewed`.

## Finish (evidence before claims)

1. Write receipt `.agents/evidence/<domain>-<slug>.json` (lowercase, `/`→`-`):
`{slug, date, checks: ["python3 .agents/bin/check.py"], result}` — result `pass` only if gate passed.
2. One row in `.agents/index.md`, one `## [YYYY-MM-DD] research | Topic | path` line in `.agents/log.md`,
update `<Domain>/_MOC.md`, set feature back to `blocked`/`done` with evidence path.
3. Run `python3 .agents/bin/check.py` (default gate) then optionally `--probe` for live
URL warnings. Report: opened vs UNVERIFIED, repos inspected vs NOT INSPECTED, limits.
4. Suggest `verify-topic` for an independent check — do not self-certify quality.
