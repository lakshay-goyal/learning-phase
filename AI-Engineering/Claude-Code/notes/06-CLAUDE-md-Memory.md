---
topic: CLAUDE md Memory
domain: AI-Engineering
status: researched
updated: 2026-10-02
related: ["[[../Claude-Code]]", "[[05-Context-Window-Management|Context]]"]
tags: [claude-code, claude-md, memory, rules, auto-memory]
---

# CLAUDE.md & Memory

> CLAUDE.md is a saved intro note (project file Claude reads every session). Auto memory is Claude's own diary. Both fix statelessness (forgetting yesterday).

## 1. Intuition

Re-explaining project each chat is slow + error-prone. One file with facts = no repeat. **.claude folder** (config box for skills, commands, agents) holds the rest.

```bash
/init
# expected output: auto CLAUDE.md drafted (only ~30% good, you add 70%)
```

> You can now: stop retyping project rules every session.

## 2. How it works

- **Make it** — manual `CLAUDE.md` CAPITALS at root, or `/init` scan then prune. Commit it.
  ```bash
  ls CLAUDE.md && git add CLAUDE.md
  # expected output: file present + staged
  ```
- **6 ideal parts + roadmap** — overview line, architecture (routers/services/schemas), style (type hints, small funcs), libs (use X, not Y), commands (`pip install`, `uvicorn`, `pytest`), critical no-dos (don't touch database.py, no auto UUIDs) + route table Done/Pending.
  ```markdown
  # Spendly
  Routes in app.py, logic in database/db.py. Use parameterized SQL only.
  # expected output: Claude follows without asking
  ```
- **.claude layout** — `settings.local.json` (personal perms), `commands/` (slash), `rules/` (split topics, lazy), `skills/`, `agents/`.
  ```bash
  ls .claude/
  # expected output: settings.local.json commands/ rules/ skills/ agents/
  ```
- **5 file types** — root `./CLAUDE.md` (every session, shared), `.claude/CLAUDE.md` (same), `CLAUDE.local.md` (personal, gitignored), `~/.claude/CLAUDE.md` (all projects), `folder/CLAUDE.md` (lazy when there).
  ```bash
  cat .claude/CLAUDE.md
  # expected output: team rules loaded each session
  ```
- **Good habits** — start /init then cut junk; only universal rules; IMPORTANT once max; <200 lines (more = worse following); living doc; "fix once → codify"; audit monthly.
  ```bash
  wc -l CLAUDE.md
  # expected output: under 200 lines
  ```
- **Big file fixes** — split to `.claude/rules/code-style.md` etc (lazy per topic); `@docs/api.md` imports (loads on ref); subfolder CLAUDE.md for multi-area.
  ```markdown
  See @docs/api-guidelines.md
  # expected output: loads only when referenced
  ```
- **Auto memory** — Claude silently saves IST timezone, INR not USD etc to `~/.claude/projects/<name>/memory/memory.md` (top 200 lines load). Add via "Update your memory" or `/memory` (project/user/auto options).
  ```text
  /memory
  # expected output: 3 choices + toggle, open memory.md
  ```

> You can now: set up persistent + auto memory that survives restarts.

## 3. Visual

```mermaid
flowchart LR
  A[New session] --> B[Load CLAUDE.md + memory.md top 200]
  B --> C[Lazy: rules + subfolder on demand]
  C --> D[Work + save learnings]
  D --> E[Refresh CLAUDE.md after feature]
```

PDF tables: project vs global .claude, 5 types matrix, 3 big-file fixes, memory trio (programmer vs Claude writes).

## 4. Use cases

| Use case | When to use (concrete example) | When NOT to / edge case |
|---|---|---|
| Repeat mistake | Add "parameterized SQL only, PRAGMA foreign_keys=ON" after first injection bug | Dump feature spec — bloats every session; fix: keep universal only |
| Multi-area repo | `billing/CLAUDE.md` for billing rules | One 500-line root — adherence drops; fix: split + @ imports |
| Personal quirk | `CLAUDE.local.md` for sandbox URL, gitignored | Commit secrets — leak; fix: local only + gitignore |
| Edge case: memory overload | memory.md >200 lines, old INR rule stale | Wrong currency persists; fix: prune monthly |

## 5. AI-era leverage

- **Mistake catcher:** turn fix into rule.
  ```text
  Ask AI: "Claude used f-string SQL again. Write a 2-line CLAUDE.md rule + 1-line memory entry to stop it."
  ```
- **Onboarder:** generate starter then trim.
  ```text
  Ask AI: "Review this /init CLAUDE.md. Delete fluff, keep commands, style, no-dos. Keep under 120 lines."
  ```

## 6. Limits & tradeoffs

- Auto 30% only — breaks as: trusting raw /init — instead do: add workflows, constraints, roadmap yourself.
- Too many IMPORTANTS — breaks as: none matter — instead do: one truly critical flag.
- Memory is local — breaks as: new laptop = blank — instead do: commit CLAUDE.md, copy memory.md manually.
- Open aspects: skills pack procedures in [[09-Skills|09 Skills]]; enforcement via hooks in [[12-Hooks-Plugins-Deploy|12 Hooks]].

## 7. Related

- [[../Claude-Code|Claude Code hub]] · [[05-Context-Window-Management|05 Context]] · [[09-Skills|09 Skills]] · [[../context/Claude-Code.resources]] · [[../context/Claude-Code.build]]
