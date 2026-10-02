---
topic: Context Window Management
domain: AI-Engineering
status: researched
updated: 2026-10-02
related: ["[[../Claude-Code]]", "[[10-Subagents|Subagents]]"]
tags: [claude-code, context-window, tokens, compact, subagents]
---

# Context Window Management

> Context window = working memory (tokens the model sees at once). Every turn resends all history, so cost grows fast (square-like). One feature = one fresh session.

## 1. Intuition

LLMs (text predictors with no memory) forget unless app resends history. Long chats = resend everything each time. **Tokens** (tiny text chunks billed) pile up.

```text
/context
# expected output: shows % used, e.g. 68% of 200k
```

> You can now: check your memory meter before quality drops.

## 2. How it works

- **Facts** — ~200k Sonnet, ~1M Opus 4.6. Fresh per session. Inputs (your text + code + images) + outputs (answers + tool logs) both burn. Replies cost ~6x your words.
  ```text
  /context -> 120k/150k usable -> quality dips
  # expected output: warning zone 120-130k
  ```
- **Quadratic math** — each turn n resends all before. 10 turns × 200 tokens = 11,000 not 2,000. Formula n(n+1)/2 × b.
  ```text
  40-turn mega (4 feats): 820 units. 4x10-turn fresh: 220 units. Save ~73%.
  # expected output: 4x cheaper + cleaner focus
  ```
- **What fills it** — system ~6k + tools ~8k + CLAUDE.md tiny + history ~45% (replies culprit) + file/Bash outputs + skills/MCP + 33k reserved for summaries. Usable ~150k.
  ```bash
  cat .claudeignore
  # node_modules/ .venv/ dist/ build/ *.log .env
  # expected output: junk Claude must never read
  ```
- **When full** — 120k degrade → 75-92% auto-compact (auto summary, lossy, mid-task, no control) → repeat compacts corrupt → hard stop at buffer full.
  ```text
  /compact
  # expected output: manual summary at safe gap, Ctrl+O to review
  ```
- **Fixes** — `/compact` at 70-75% between tasks; subagents (child helpers with own 200k, return summary, parallel); `/clear` wipes chat; new session per feature.
  ```text
  /clear
  # expected output: history deleted, same session ID
  ```
- **Habits** — one session per feature; `/context` often; sharp prompts (vague = long exploring answers); isolates to subagents; `.claudeignore` junk.
  ```bash
  printf "node_modules/\n.venv/\ndist/\n.env\n" > .claudeignore
  # expected output: smaller, faster reads
  ```
- **Terminal vs GUI** — CLI full power; VS Code/Desktop/Web limited. Memory, hooks, subagents need terminal.
  ```bash
  claude
  # expected output: full slash + hooks + /agents available
  ```

> You can now: keep every session lean and cheap.

## 3. Visual

```mermaid
flowchart LR
  A[Turn 1: 200] --> B[Turn 2: resend + new = 400]
  B --> C[Turn 10: 2000 linear vs 11000 actual]
  C --> D{70% full?}
  D -->|yes| E[/compact or fresh session]
  D -->|no| F[Keep + subagents for heavy]
```

PDF tables: per-turn 200→2000, 1×40 vs 4×10 save 73%, 200k−6k−8k−33k≈150k usable.

## 4. Use cases

| Use case | When to use (concrete example) | When NOT to / edge case |
|---|---|---|
| Feature start | New session + `/rename db-setup`, pull + branch | Reuse landing session for DB — mixing + 4x cost; fix: fresh session |
| Mid-task bloat | `/context` → 72% → `/compact` between tasks | Compact mid-edit — loses active plan; fix: pause at milestone |
| Explore big repo | Delegate to subagent, keep main lean | Paste 30k codebase each turn — $1.14/8 turns; fix: 500-token plan back |
| Edge case: auto-compact mid-auth | Summary drops password rule | Auth breaks silently; fix: manual compact + review + spec on disk |

## 5. AI-era leverage

- **Token saver:** split work before overpay.
  ```text
  Ask AI: "This chat is 65% full. Summarize done vs pending in 5 lines so I can /compact safely."
  ```
- **Prompt sharpener:** cut exploring answers.
  ```text
  Ask AI: "Rewrite my vague prompt into @ files + must/must-not + 5-line scope to save tokens."
  ```

## 6. Limits & tradeoffs

- Compaction is lossy — breaks as: details vanish — instead do: specs + CLAUDE.md on disk survive; chat does not.
- `/clear` is nuclear — breaks as: needed history gone — instead do: `/export` first.
- Subagents add hops — breaks as: tiny task slower — instead do: direct for 2-line fixes.
- Open aspects: memory files in [[06-CLAUDE-md-Memory|06 Memory]]; subagent math in [[10-Subagents|10 Subagents]].

## 7. Related

- [[../Claude-Code|Claude Code hub]] · [[04-Making-Code-Changes|04 Changes]] · [[10-Subagents|10 Subagents]] · [[../context/Claude-Code.resources]] · [[../context/Claude-Code.build]]
