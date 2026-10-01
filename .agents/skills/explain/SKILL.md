---
name: explain
description: "Answer a question in chat only. Creates no files."
invocation: user
---

# Explain

Answer in chat. Create zero files, change zero files.

Rules:
1. No scaffolding, no topic folder, no index/log touch.
2. Beginner-first: plain words, zero jargon. Define any must-use term in 5–8 words inline. No storytelling — straight to the point.
3. Snippet-first: minimal text, lead with the smallest runnable example (1–5 lines) + 1 line expected output. Then 3–5 short bullets max (1–2 lines each). Never 5 paragraphs where one snippet teaches it.
4. Always include: 1 real use case (when to use it at work) + 1 edge case / common mistake (what breaks + fix with snippet).
5. End with two lines: one-line win (`You can now: ...`), then say `research this` if they want it saved as a topic package.
6. Cite what you actually read; mark the rest UNVERIFIED.

When wrong skill: "research / teach me / go deeper / save" → `learn-topic`;
"check health / orphans" → `lint-wiki`.

Done when: question answered, `git status --short` unchanged (or vault file list unchanged).
