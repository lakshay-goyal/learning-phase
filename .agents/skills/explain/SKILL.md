---
name: explain
description: "Answer a question in chat only. Creates no files."
invocation: user
---

# Explain

Answer in chat. Create zero files, change zero files.

Rules:
1. No scaffolding, no topic folder, no index/log touch.
2. Concise, humane, one small Mermaid block only if it clarifies.
3. End with one line: say `research this` if they want it saved as a topic package.
4. Cite what you actually read; mark the rest UNVERIFIED.

When wrong skill: "research / teach me / go deeper / save" → `learn-topic`;
"check health / orphans" → `lint-wiki`.

Done when: question answered, `git status --short` unchanged (or vault file list unchanged).
