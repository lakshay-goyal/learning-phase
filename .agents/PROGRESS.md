# Progress — updated 2026-10-02

## Current state

Harness v6 (tracks: hub + `notes/<Slug>.md` per subtopic + `context/<Track>.resources.md` + `context/<Track>.build.md` — no per-subtopic folders. Resources = beyond-scope deepening only. Build = whole-topic mini-projects, not homework. Budgets README350/build250/hub150; HARD RULE: folder-named files, banned generic basenames fail the gate; per-subtopic triples inside a v5 track fail the gate. Legacy Git track grandfathered with migrate warning). Style HARD RULE (rule 12): beginner-first, snippet-first — plain words, zero jargon, snippet per concept + expected output, real job use cases + ≥1 edge case per subtopic, no storytelling, no context dumps, each section ends with something the reader can now DO. Git track live:
`DevOps/Git/Git.md` hub + `notes/` (8 notes: fundamentals → commits → branches → merge →
undo → internals → gh → glab) + `context/` (`Git.resources.md` + `Git.build.md`),
files self-describing (`notes/01-Fundamentals.md`, …)
so the Obsidian graph shows real titles. Bookkeeping stays in `.agents/`, out of the reading view.

## In flight

Nothing. (WIP = 1: one track at a time. Git track done; next track unqueued.)

## Blocked

Nothing.

## Next session starts

```bash
cat .agents/PROGRESS.md
python3 .agents/bin/check.py
```

## Last green baseline

`python3 .agents/bin/check.py` → [v2] 0 topics, VCR 1/1=1.00, 0 errors (2026-10-02). Dead keys: none.
