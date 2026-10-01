---
topic: <Human Title>
domain: <Domain-Id>
status: researched
updated: YYYY-MM-DD
related: []
---

# <Human Title> — Build

_Single topics only. In a track, subtopics get NO build file — use `track-build.md` once at track level (mini-projects over the whole track)._

> Prove it by doing. Beginner-first: every task lists exact commands + what you should see + one common error and its fix.

## Production codebase to study (1–3, pinned — required)

| Repo | Signals (stars / users / last push / license) | Commit | Study guide (real file path, end-to-end trace) |
|---|---|---|---|
| [org/repo](https://github.com/org/repo) | e.g. 12k★, used by X, push 2026-09, MIT | `abc1234` | Read `src/a.py` → `src/b.py`; trace one request flow |

NOT INSPECTED if not opened — say so. Tutorial repos fail the gate's spirit; prefer deployed, tested codebases.
Study guide must be followable by a fresher: file path → what to look at (function name) → what to try changing.

## Assignments (do 1, skip tutorial-hell)

_Beginner rule: each assignment = goal in 1 line + exact steps with commands + expected output + 1 common mistake + fix. No paragraph briefs._

1. **Small (2–4h):** <goal in plain words>
   ```bash
   <step 1 command>
   <step 2 command>
   # you should see: <1 line>
   # if you see <common error>: fix with <command>
   ```
2. **Medium (1–2d):** <goal in plain words>
   ```bash
   <key commands only, 3–6 lines>
   # you should see: <1 line>
   ```
3. **Client-ready:** … (who pays / who benefits + what demo you show them)

## Ideas, use cases & missed aspects

- AI-era scenario: … (who + task + why this tech fits + 1 prompt/command)
- Real use case: … (job task where this earns money/saves time)
- Edge case you might've missed: … (what breaks + minimal repro snippet + fix)
  ```bash
  <3-line repro of the edge case>
  ```

## Human feedback (only human edits)

- [ ] I read README + opened 1 resource + 1 repo file
- [ ] Flip all 3 files to `human-reviewed` when done. Date: …
- [ ] I can explain this to a fresher with one snippet: …
- Notes: …
