---
topic: CLAUDE md Memory
domain: AI-Engineering
status: researched
updated: 2026-10-02
related: ["[[../Claude-Code]]"]
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

### Write it

- **/init then prune** — auto-draft is ~30% right; you add workflows + taboos, then commit it like code.

  ```bash
  ls CLAUDE.md && git add CLAUDE.md
  # expected output: file present + staged
  ```

- **Six parts + roadmap** — overview, architecture, style, libs, commands, never-dos — plus a Done/Pending route table.

  ```markdown
  # Spendly
  Routes in app.py, logic in database/db.py. Use parameterized SQL only.
  # expected output: Claude follows without asking
  ```

### Shape it

- **Five homes** — root + `.claude/` shared every session; `.local` private; `~/.claude` global; subfolders lazy.

  ```bash
  cat .claude/CLAUDE.md
  # expected output: team rules loaded each session
  ```

- **Full map** — project side plus machine side; "claude25" = `CLAUDE.md`, "claude local" = `CLAUDE.local.md`; `analysis.json` is not a real file (see `settings.local.json`, `.mcp.json`).

  ```text
  my-project/
  ├── CLAUDE.md                  # team memory, committed
  ├── CLAUDE.local.md            # your private notes, gitignored
  ├── .mcp.json                  # team MCP servers (project ROOT, not in .claude/)
  └── .claude/
      ├── settings.json          # team settings, committed
      ├── settings.local.json    # your overrides, gitignored
      ├── commands/              # legacy slash prompts, e.g. seed-user.md
      ├── skills/                # expertise packs: <name>/SKILL.md
      ├── agents/                # subagents: <name>.md
      ├── rules/                 # topic + path-scoped rules: *.md
      ├── hooks/                 # event scripts: *.sh, *.py
      └── output-styles/         # custom reply styles: *.md

  ~/.claude/                      # your machine, all projects
  ├── CLAUDE.md                  # personal memory
  ├── settings.json              # your defaults
  ├── skills/ agents/ commands/ output-styles/  # personal packs
  ├── themes/                    # custom terminal themes
  ├── plugins/                   # installed plugins
  └── projects/<project>/memory/ # Claude's auto diary
  # expected output: you can point at any path and say who writes it + if git tracks it
  ```

- **Short by design** — under 200 lines, IMPORTANT at most once; split topics to `rules/`, `@`-import shared docs.

  ```markdown
  See @docs/api-guidelines.md
  # expected output: loads only when referenced
  ```

### Remember

- **Living doc + diary** — refresh after each feature, audit monthly; auto memory notes silently, top 200 lines load.

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

Also tabulated: project vs global .claude, 5 types matrix, 3 big-file fixes, memory trio (programmer vs Claude writes).

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

- Open aspects: skills pack procedures in [[09-Skills|09 Skills]]; enforcement via hooks in [[13-Hooks|13 Hooks]].

## 7. Related

- [[../Claude-Code|Claude Code hub]] · [[../context/Claude-Code.resources]] · [[../context/Claude-Code.build]]
