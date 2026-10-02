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
5. Value filter: if the user asked for a specific subject, go deep on what earns them
money / saves time / unblocks their job — not a generic overview. Every subtopic must
contain at least one concrete job-task payoff.

## Beginner-first writing rules (mandatory, every file)

Reader = fresher, zero prior knowledge, low attention span. No storytelling.

1. **Plain words first.** No jargon, no AI buzzwords. If a technical term is unavoidable,
define it inline in 5–8 words in brackets on first use. If the Intuition section needs
the mechanism section to be understood, rewrite it.
2. **Snippet beats paragraph.** Minimal text, maximum examples. Every concept gets a
minimal runnable snippet (1–5 lines) + 1 line of expected output. Never write 5+
lines of prose where a snippet + 1 line would teach it.
3. **One idea per block.** 5–8 bullets max per section, 1–2 lines per bullet. Short
sections. End Intuition and each major section with a 1-line win: `> You can now: ...`.
4. **Real use cases + edge cases.** Use-cases table = real job tasks (when to use with
example command + when NOT to + what breaks + fix). Every subtopic includes ≥1 edge
case / common-mistake row and ≥1 edge-case snippet in build.md.
5. **Concrete AI leverage.** No generic "AI can help" lines. Each scenario = who +
task + why this tech fits + one copy-paste prompt/command.
6. **No context dumps.** Don't front-load background. Teach the smallest useful thing
first, link the rest to resources/build instead of pasting it.
7. **Dopamine = payoff, not praise.** No extra "well done" sections. Value comes from
each section ending with something the reader can now DO (run, fix, decide, demo).

## Write (v5: hub + ONE resources + ONE build per topic/track, note-only subtopics)

Single topic at `<Domain>/<Slug>/`: `<Slug>.md` + `<Slug>.resources.md` + `<Slug>.build.md` (template headings exactly).

Track at `<Domain>/<Track>/`:

```text
<Domain>/<Track>/
├── <Track>.md                              # from track-hub.md: purpose, map, notes table with links
├── notes/01-Slug.md                        # note only — all notes together, no folders per subtopic
├── notes/02-Slug.md                        # note only
├── context/<Track>.resources.md            # from track-resources.md: ONE file, beyond-scope deepening only
└── context/<Track>.build.md                 # from track-build.md: ONE file, mini-projects over the whole track
```

- Notes use `topic-readme.md` headings exactly; each links up to `[[../<Track>]]` hub + `[[../context/<Track>.resources]]` + `[[../context/<Track>.build]]` + sideways to siblings as `[[<Slug>|Title]]`. NEVER per-subtopic folders, NEVER `README.md` / `resources.md` / `build.md` (hard rule: gate fails banned filenames and retired folders).
- Resources rule: this file exists ONLY for going beyond the listed subtopics. If the notes + mini-projects covered it, the reader should never need to open it. One file per track: top ≤12 across ALL subtopics, row 1 = 10-min starter.
- Build rule: mini-projects (2–3), each a real ship-able thing touching ≥3 subtopics — not homework, not one-subtopic drills. Each = goal in 1 line + exact commands + what done looks like + 1 common mistake + fix + who benefits. Plus 1–3 pinned OSS repos with reading guide.
- Must cover the six: resources, pinned OSS codebase + reading guide, mini-projects, use cases, AI-leverage scenarios, missed aspects. One Mermaid diagram per note + hub.
Frontmatter `status: researched`. Never `human-reviewed`.

## Finish (evidence before claims)

1. Write ONE receipt per topic/track `.agents/evidence/<domain>-<slug>.json`
(lowercase, `/`→`-`): `{slug, date, checks: ["python3 .agents/bin/check.py"], result}` —
result `pass` only if gate passed. (Legacy per-subtopic receipts stay untouched until that track migrates.)
2. One row per subtopic + one track row in `.agents/index.md`, one
`## [YYYY-MM-DD] research | Topic | path` line per subtopic in `.agents/log.md`,
update `<Domain>/<Domain>.md` (create it when the domain's first track lands), set feature back to `blocked`/`done` with evidence paths.
2. One row per subtopic + one track row in `.agents/index.md`, one
`## [YYYY-MM-DD] research | Topic | path` line per subtopic in `.agents/log.md`,
update `<Domain>/<Domain>.md` (create it when the domain's first track lands), set feature back to `blocked`/`done` with evidence paths.
3. Run `python3 .agents/bin/check.py` (default gate) then optionally `--probe` for live
URL warnings. Report: opened vs UNVERIFIED, repos inspected vs NOT INSPECTED, limits.
4. Suggest `verify-topic` for an independent check — do not self-certify quality.
