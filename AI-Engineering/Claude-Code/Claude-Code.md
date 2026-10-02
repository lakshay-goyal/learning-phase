---
topic: Claude Code
domain: AI-Engineering
status: researched
updated: 2026-10-02
related: []
tags: [claude-code, agentic-coding, anthropic, terminal, sdd, mcp, subagents, hooks, plugins]
track: Claude Code
---

# Claude Code

> End-to-end agentic coding with Claude Code: setup → slash commands → code changes → memory → spec + plan → custom commands → skills → subagents → MCP → hooks → plugins → deploy. Finish it and you can ship a Flask feature solo: spec → plan → code → test → review → ship.

```mermaid
flowchart LR
  A[01 Foundations] --> B[02 Setup]
  B --> C[03 Slash Commands]
  C --> D[04 Code Changes]
  D --> E[05 Context Window]
  E --> F[06 Memory]
  F --> G[07 SDD + Plan]
  G --> H[08 Custom Commands]
  H --> I[09 Skills]
  I --> J[10 Subagents]
  J --> K[11 Custom Subagents]
  K --> L[12 MCP]
  L --> M[13 Hooks Deploy]
```

## How to use this track

1. Go in order `01 → 13`, 15–30 min per note. Each builds on the last. Demo app throughout is Spendly (Flask expense tracker).
2. Each note is learn-with-snippets; `context/Claude-Code.resources.md` goes deeper (beyond-scope only); `context/Claude-Code.build.md` proves it with mini-projects.
3. After each note you can: run one new real command (see table).

## Subtopics

| # | Note | Covers (plain words + payoff) |
|---|---|---|
| 01 | [[notes/01-Foundations-Vibe-Vs-Agentic|Foundations: Vibe vs Agentic]] | Vibe vs agentic, why Claude Code, Spendly project — you can explain your role as pilot |
| 02 | [[notes/02-Setup-Bash-Git-Ollama|Setup, Bash, Git, Ollama]] | Install, first run, Flask, Bash mode, git, free Ollama — you can run Spendly locally |
| 03 | [[notes/03-Slash-Commands-Sessions|Slash Commands & Sessions]] | 15 built-ins, sessions, models, permissions — you can drive sessions cleanly |
| 04 | [[notes/04-Making-Code-Changes|Making Code Changes]] | Edit + new pages + image→code + modal, @ mentions — you can land landing-page tasks |
| 05 | [[notes/05-Context-Window-Management|Context Window]] | 200k window, quadratic cost, compact/clear/subagents — you can keep quality high |
| 06 | [[notes/06-CLAUDE-md-Memory|CLAUDE.md & Memory]] | CLAUDE.md, .claude folder, 5 types, auto memory — you can persist project knowledge |
| 07 | [[notes/07-Spec-Driven-Plan-Mode|SDD + Plan Mode]] | Spec anatomy, tech design, 15-step workflow, plan/ultraplan — you can ship DB setup right |
| 08 | [[notes/08-Custom-Slash-Commands-Auth|Custom Commands & Auth]] | seed-user, seed-expense $ARGUMENTS, create-spec, register/login — you can automate repeats |
| 09 | [[notes/09-Skills|Skills]] | SKILL.md, progressive disclosure, skill-creator, merger — you can pack expertise |
| 10 | [[notes/10-Subagents|Subagents]] | Statelessness, math, advantages, built-ins — you can explain why helpers exist |
| 11 | [[notes/11-Custom-Subagents|Custom Subagents]] | Permissions, anatomy, test + review pipelines — you can design team specialists |
| 12 | [[notes/12-MCP-Integrations|MCP Integrations]] | SQLite/Figma/GitHub, top 10, minimal setup — you can plug outside tools in |
| 13 | [[notes/13-Hooks-Plugins-Deploy|Hooks, Plugins, Deploy]] | Harness, 7 hook uses, exit codes, plugin.json, Railway — you can enforce + distribute + deploy |

## Related

- [[../AI-Engineering|AI-Engineering]] · [[context/Claude-Code.resources]] · [[context/Claude-Code.build]]
