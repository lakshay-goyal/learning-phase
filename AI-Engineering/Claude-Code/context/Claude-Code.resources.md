---
topic: Claude Code
domain: AI-Engineering
status: researched
updated: 2026-10-02
related: []
tags: [claude-code, resources]
track: Claude Code
---

# Claude Code — Resources

> The ONLY resources file for this whole track. You only need it to go BEYOND the listed subtopics. If the notes + mini-projects covered what you need, close this file.

## Connected reading path

| # | Type | Title | Status | Why this one (beginner payoff in 1 line) |
|---|---|---|---|---|
| 1 | docs | [Claude Code overview](https://code.claude.com/docs/en/overview) | OPENED 2026-10-02 | Start here: install + first session in 10 min |
| 2 | docs | [Memory: CLAUDE.md + auto memory](https://code.claude.com/docs/en/memory) | OPENED 2026-10-02 | Project memory, rules, imports that survive sessions |
| 3 | docs | [Subagents](https://code.claude.com/docs/en/subagents) | OPENED 2026-10-02 | Isolated helpers with models, tools, scopes |
| 4 | docs | [Hooks guide: automate actions](https://code.claude.com/docs/en/hooks-guide) | OPENED 2026-10-02 | Deterministic guards: format, block, notify with snippets |
| 5 | docs | [MCP: connect tools](https://code.claude.com/docs/en/mcp) | OPENED 2026-10-02 | stdio vs http, scopes, minimal-server rule |
| 6 | docs | [Skills: extend Claude](https://code.claude.com/docs/en/skills) | OPENED 2026-10-02 | SKILL.md + progressive disclosure + merger with commands |
| 7 | docs | [Plugins overview](https://code.claude.com/docs/en/plugins/overview) | OPENED 2026-10-02 | Pack skills+hooks+agents+MCP into one install |
| 8 | docs | [Extend Claude Code](https://code.claude.com/docs/en/features-overview) | OPENED 2026-10-02 | Map of when to use memory vs skill vs MCP vs hook |
| 9 | repo | [anthropics/claude-code](https://github.com/anthropics/claude-code) | OPENED 2026-10-02 | Official CLI source: commands, perms, hooks wiring |
| 10 | repo | [anthropics/skills](https://github.com/anthropics/skills) | OPENED 2026-10-02 | Official skill packs + template to copy |
| 11 | repo | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | OPENED 2026-10-02 | Reference MCP servers: sqlite, github, fetch patterns |
| 12 | guide | [Hooks mastery + subagents](https://github.com/disler/claude-code-hooks-mastery) | UNVERIFIED — indexed community repo, lists hook payloads + agent files | Hook recipes + status lines when official docs feel thin |

Status ∈ `OPENED <date>` (you read it) / `UNVERIFIED — <reason>`. Dead links fail the gate — fix or remove.

## Papers

Skip — track is tool-practice, not research. Official docs + 3 pinned repos are canonical. No paper adds a new mechanism beyond hooks/MCP/subagent isolation.

## Source ledger (required)

- Searched (queries): Claude Code official documentation; CLAUDE.md hooks MCP subagents docs; anthropics claude-code github repo
- Opened (≥5): 11 above (rows 1-11, 2026-10-02 via webfetch/API) · Skipped with reason: Medium/YouTube walkthroughs, opinionated best-setup blogs (docs already canonical + versioned)
- Connectedness: overview links memory/skills/subagents/MCP/hooks/plugins; memory cites hooks for enforcement; hooks-guide cites skills/subagents/plugins; MCP cites plugins for bundling; repos cite docs in READMEs
- Beginner starter: row #1 above — gives a working snippet in <10 min
