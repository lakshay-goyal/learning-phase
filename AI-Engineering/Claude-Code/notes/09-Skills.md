---
topic: Skills Guide
domain: AI-Engineering
status: researched
updated: 2026-10-02
related: ["[[../Claude-Code]]", "[[08-Custom-Slash-Commands-Auth|Commands]]"]
tags: [claude-code, skills, progressive-disclosure, skill-creator]
---

# Skills

> Skills = folders that make Claude a specialist (workflows + files on demand). Fixes 5 prompt pains: retype, context burn, no bundle, no share, no compose.

## 1. Intuition

General AI knows PowerPoint but not your fonts/layouts. **Progressive disclosure** (show info only when needed) keeps context light: Level 1 names, Level 2 body, Level 3 files.

```bash
ls .claude/skills/frontend-design/SKILL.md
# expected output: skill entry file present
```

> You can now: say when a prompt needs to become a skill.

## 2. How it works

- **Why prompts fail** — retype each time; 20k tokens always burn; can't attach PDFs/scripts; no version/share; 3-in-1 confuses model.
  ```text
  Long prompt every time = 20k tokens burned always
  # expected output: slow + costly vs skill loads on need
  ```
- **Folder** — `ppt-generator/SKILL.md` (must) + `scripts/` (code) + `resources/` (refs) + `assets/` (templates/fonts). Only SKILL.md required.
  ```bash
  mkdir -p .claude/skills/ppt-generator/scripts
  # expected output: skill skeleton ready
  ```
- **SKILL.md 2 parts** — frontmatter `name` (id) + `description` (when to fire, most vital); body steps, patterns, pitfalls, links like `[Run plot.py](./scripts/plot.py)`.
  ```markdown
  ---
  name: docx
  description: Use when making .docx with company style
  ---
  # expected output: triggers only on that intent
  ```
- **Levels** — L1 all descriptions at start (~10 lines); L2 full body on match; L3 scripts/templates when body points. 10 skills = 10 lines until needed.
  ```text
  Successfully loaded skill: frontend-design
  # expected output: confirms L2 loaded
  ```
- **Scopes** — personal `~/.claude/skills/` (all projects) vs project `<repo>/.claude/skills/` (team, git). Don't trust random community (key leaks); prefer official repo.
  ```bash
  ls ~/.claude/skills/
  # expected output: your personal packs
  ```
- **Make it** — manual folder+MD (ok but hard); skill-creator (recommended: + → Skills → creator → 3 Qs: do/trigger/done → copy to skill path); install community (risky). Test + iterate 4-5x. Restart to use (`claude -r`).
  ```bash
  claude -r
  # expected output: new skill listed under /
  ```
- **Profile demo** — no-skill: big Category card, default fonts, large cards. With frontend-design: merged table, better type, compact. Plan: baseline → skill → rebuild → compare.
  ```text
  /frontend-design Build profile page per theme
  # expected output: tighter layout per skill rules
  ```
- **Merger** — commands merged into skills. Type `/` sees all. Old `.claude/commands/` retiring. Auto (Claude picks) vs manual (you type). Stop auto: `disable-model-invocation: true`.
  ```markdown
  ---
  disable-model-invocation: true
  ---
  # expected output: only runs when you type /name
  ```

> You can now: create, test, and gate a skill.

## 3. Visual

```mermaid
flowchart LR
  A[L1: 10 descriptions] --> B{Intent matches?}
  B -->|yes| C[L2: body loads]
  C --> D[L3: scripts/templates on link]
  D --> E[Compose: pdf->tables->ppt chain]
```

PDF tables: PPT gap, 5 prompt fails, prompts vs skills, folder contents, 3 levels, personal vs project, fixes, profile diff, command vs skill triggers.

## 4. Use cases

| Use case | When to use (concrete example) | When NOT to / edge case |
|---|---|---|
| Team frontend style | `frontend-design` for every page | One-off page — skill overhead; fix: prompt only |
| EDA pack (Rahul) | Skew >1.5 flag, leakage >0.95 red | Generic EDA — misses domain; fix: encode rules in body |
| Chain tasks | make-ppt links extract-tables links read-pdf | One giant prompt — confused; fix: 3 small skills composing |
| Edge case: auto fires wrong | Skill hijacks unrelated chat | Annoying; fix: `disable-model-invocation: true` |

## 5. AI-era leverage

- **Skill drafter:** answer 3 Qs fast.
  ```text
  Ask AI: "Draft SKILL.md for <task>. Ask me: what it does, when to trigger, what done looks like. Then output frontmatter + 5 steps."
  ```
- **Share pack:** version team knowledge.
  ```text
  Ask AI: "List files for ppt-generator skill: SKILL.md + 1 script + 1 template. Give mkdir + git add commands."
  ```

## 6. Limits & tradeoffs

- 4-5 iterations to solid — breaks as: first draft flaky — instead do: test on real prompts, refine.
- Untrusted skills leak keys — breaks as: random install steals env — instead do: read SKILL.md + scripts first.
- Body stays in context after load — breaks as: long body = recurring cost — instead do: concise steps, link details to L3.
- Open aspects: distribute via [[12-Hooks-Plugins-Deploy|12 Plugins]]; isolate via [[10-Subagents|10 Subagents]].

## 7. Related

- [[../Claude-Code|Claude Code hub]] · [[08-Custom-Slash-Commands-Auth|08 Commands]] · [[10-Subagents|10 Subagents]] · [[../context/Claude-Code.resources]] · [[../context/Claude-Code.build]]
