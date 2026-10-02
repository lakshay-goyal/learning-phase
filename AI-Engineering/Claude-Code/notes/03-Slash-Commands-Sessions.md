---
topic: Slash Commands Sessions
domain: AI-Engineering
status: researched
updated: 2026-10-02
related: ["[[../Claude-Code]]", "[[02-Setup-Bash-Git-Ollama|Setup]]"]
tags: [claude-code, slash-commands, sessions, models, permissions]
---

# Slash Commands & Sessions

> Slash commands are one-word shortcuts (tiny text starting with / that runs a full workflow). Sessions are one conversation = one task.

## 1. Intuition

Typing full prompts for repeat jobs wastes time. `/model` beats "please show me models so I can switch". A **session** (single chat from `claude` to `/exit`) holds history, folder, ID, auto-save.

```bash
/type-then-tab
# expected output: press / lists all commands, arrows to pick
```

> You can now: explain why one word beats one paragraph.

## 2. How it works

- **Two kinds** — built-in (ships with tool: `/exit`, `/model`) vs custom (you make: `/seed-user`).
  ```text
  /<name> -> saved prompt -> workflow runs
  # expected output: command executes without retyping
  ```
- **Sessions** — ID + full history + folder, saved to `~/.claude/projects/`.
  ```bash
  claude -r
  # expected output: list to resume (from terminal, before starting)
  ```
- **Inside resume** — `/resume` picks a past session from inside a running one.
  ```text
  /resume
  # expected output: picker, Enter to jump
  ```
- **Core 5 to learn first** — `/exit` closes, `/rename intro-session` names, `/btw` side-asks without history, `/export file.md` saves, `/usage` shows tokens.
  ```text
  /btw What is Jinja templating in Flask?
  # expected output: parallel answer, Space dismisses, never enters context
  ```
- **Models** — Opus 4.6 ($5/$25, 1M in, 128k out, slow smart) for planning; Sonnet 4.6 ($3/$15, 1M in, 64k out) for code; Haiku 4.5 ($1/$5, 200k in, 64k out, fastest). Pattern: Opus plans → Sonnet builds.
  ```text
  /model
  # expected output: opus-4-6 / sonnet-4-6 / haiku-4-5 picker
  ```
- **Usage trio** — `/usage` (session + weekly), `/extra-usage` ($5/$10 top-up), `/stats` (tokens, models, streak), `/insights` (HTML report: rights/wrongs + next workflows).
  ```text
  /usage
  # expected output: current session + weekly limit numbers
  ```
- **Config + permissions** — `/config` toggles auto-compact, thinking, progress bar, turn time, permission mode, update channel. `/permissions` tabs Allow/Ask(default)/Deny/Workspace; scopes local-project / global-project (in `.claude/`) / user. Tools: Read, Write, Bash, Web Search.
  ```text
  /permissions
  # expected output: 4 tabs, be strict with Allow list
  ```
- **Theme + voice** — `/theme` dark/light; `/voice` hold Space to speak, `/voice` again to off.
  ```text
  /theme
  # expected output: appearance picker
  ```

> You can now: run a clean one-task session and check cost before limits hit.

## 3. Visual

```mermaid
flowchart LR
  A[/ + picker] --> B[Session: ID + history + folder]
  B --> C[One task + rename + btw + export]
  C --> D[Opus plan -> Sonnet build]
  D --> E[usage + config + permissions]
```

PDF art: session file tree under `~/.claude/projects/`, `/btw` parallel bubble, model price table.

## 4. Use cases

| Use case | When to use (concrete example) | When NOT to / edge case |
|---|---|---|
| Name + isolate work | `/rename landing-improvements` per feature | One mega-session for 4 features — quadratic cost + mixing; fix: new session per feature |
| Side doubt mid-feature | `/btw What is Jinja?` while building auth | Ask in main chat — pollutes context; fix: `/btw` then Space |
| Pre-refactor safety | `/export before-refactor.md` before big change | Skip export — lose history; fix: export habit |
| Edge case: Allow-all danger | Putting Bash in Allow to skip prompts | Malicious/typo `rm -rf` runs free; fix: keep Ask default, Allow only safe reads |

## 5. AI-era leverage

- **Cost guard:** stop surprise caps mid-demo.
  ```text
  Ask AI: "I run /usage and see 70% weekly used. Should I /compact, /clear, or buy /extra-usage for a 2-hour auth task? Decide in 3 lines."
  ```
- **Session hygiene bot:** enforce naming + commits.
  ```text
  Ask AI: "Make me a 4-line session start checklist: rename, pull, branch, commit rule. I will paste it every time."
  ```

## 6. Limits & tradeoffs

- Too many sessions = lost history — breaks as: fix needs old context — instead do: `/resume` + good names, export key ones.
- `/insights` HTML is advice, not truth — breaks as: following every suggestion — instead do: pick one workflow to try.
- Voice needs mic + quiet — breaks as: noisy mis-transcribe — instead do: type for exact file paths.
- Open aspects: code tasks in [[04-Making-Code-Changes|04 Changes]]; context math in [[05-Context-Window-Management|05 Context]]; sources in [[../context/Claude-Code.resources]].

## 7. Related

- [[../Claude-Code|Claude Code hub]] · [[02-Setup-Bash-Git-Ollama|02 Setup]] · [[04-Making-Code-Changes|04 Changes]] · [[../context/Claude-Code.resources]] · [[../context/Claude-Code.build]]
