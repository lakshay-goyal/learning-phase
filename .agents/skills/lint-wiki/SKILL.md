---
name: lint-wiki
description: "Health-check wiki links, budgets, orphans, index and log drift."
invocation: user
---

# Lint-Wiki

Keep the wiki neat without re-researching.

1. Run `python3 .agents/bin/check.py`. Fix: broken `[[links]]`, over-budget files,
missing Mermaid, missing index rows, `related` > 4, extra files in topic folders.
2. Orphans: any topic README with zero inbound links (outside its own folder) gets
either a `related` backlink from the closest topic or a row-check in its domain MOC.
Don't mesh everything — one inbound is enough.
3. Stale: `updated` > 90 days → set `status: draft`, append `log.md` line, leave
content for human to re-trigger via `learn-topic`.
4. Append `## [YYYY-MM-DD] lint | <result>` to `log.md`. Re-run `check.py` clean.

Don't change explanations, don't add topics, don't touch `raw/`.
