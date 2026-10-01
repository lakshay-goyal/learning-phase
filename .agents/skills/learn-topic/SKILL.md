---
name: learn-topic
description: "Deep-research a topic into one Domain/Topic folder (3 files) or a full Domain/Track (hub + subtopics) + receipts + index + log."
invocation: model
---

# Learn-Topic

Turn "research X" into one in-depth package. Deep process, complete output.
Small question → single topic. Whole syllabus → track.

## Start (clock in)

1. Read `.agents/AGENTS.md`, `.agents/taxonomy.json`, `.agents/index.md`, `.agents/feature_list.json`.
2. One track at a time (WIP=1). Set matching feature `in-progress` or add one with
(id, behavior, verification=`python3 .agents/bin/check.py`, state).
3. Pick domain from taxonomy. Syllabus with ≥3 parts → track at `<Domain>/<Track>/`,
subtopics `<Domain>/<Track>/01-Slug/`, hub `<Domain>/<Track>/<Track>.md`.

## Research protocol (depth is mandatory, dumping is forbidden)

1. Order: official docs → papers → most-linked blogs → GitHub (stars + recent push +
real users + license). Prefer sources that cite each other — record connectedness.
2. Open ≥5 sources per track (≥1 per subtopic where possible). For each repo candidate check:
last push <12mo, tests/CI present, real file paths noted. Never invent file paths or
SHAs — open the repo or mark NOT INSPECTED.
3. Classify every link OPENED <date> or UNVERIFIED + reason. Version-pin repos (short SHA).
4. Complete: cover every syllabus item the user listed. Cut trivia, never cut listed scope.

## Write (hub + 3 folder-named files per subtopic, from templates)

- Hub `<Track>/<Track>.md` from `track-hub.md`: purpose, map, subtopic table with links.
- Each subtopic `<Track>/NN-Slug/NN-Slug.md`, `NN-Slug.resources.md`, `NN-Slug.build.md` — template headings exactly. NEVER `README.md` / `resources.md` / `build.md` (hard rule: gate fails banned filenames).
- Must cover the six: resources, pinned OSS codebase + reading guide, 3 assignments,
use cases, AI-leverage scenarios, missed aspects. One Mermaid diagram per main file + hub.
- Subtopic mains link up to `[[../<Track>]]` hub + sideways to siblings.
Frontmatter `status: researched`. Never `human-reviewed`.

## Finish (evidence before claims)

1. Write receipt per subtopic `.agents/evidence/<domain>-<track>-<slug>.json`
(lowercase, `/`→`-`): `{slug, date, checks: ["python3 .agents/bin/check.py"], result}` —
result `pass` only if gate passed.
2. One row per subtopic + one track row in `.agents/index.md`, one
`## [YYYY-MM-DD] research | Topic | path` line per subtopic in `.agents/log.md`,
update `<Domain>/_MOC.md`, set feature back to `blocked`/`done` with evidence paths.
3. Run `python3 .agents/bin/check.py` (default gate) then optionally `--probe` for live
URL warnings. Report: opened vs UNVERIFIED, repos inspected vs NOT INSPECTED, limits.
4. Suggest `verify-topic` for an independent check — do not self-certify quality.
