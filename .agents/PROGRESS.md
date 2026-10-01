# Progress — updated 2026-10-02

## Current state

Harness v4 (tracks: hub + subtopics, budgets README350/build250/hub150; HARD RULE: folder-named files, banned generic basenames fail the gate). Git track live:
`DevOps/Git/Git.md` hub + 8 subtopics (fundamentals → commits → branches → merge →
undo → internals → gh → glab), files named `<Slug>.md` / `<Slug>.resources.md` /
`<Slug>.build.md` so the Obsidian graph shows real titles. Bookkeeping stays in `.agents/`, out of the reading view.

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
