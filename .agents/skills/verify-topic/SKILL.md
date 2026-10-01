---
name: verify-topic
description: "Independently review one topic package; write verdicts to reviews/ without editing it."
invocation: user
---

# Verify-Topic

Independent evaluator (generator ≠ evaluator). Read-only on the topic.

1. Read `<Domain>/<Slug>/` (3 files) + receipt in `.agents/evidence/`.
2. Check: explanation correct + compressed? visual accurate? ≥5 resources with trust
labels + connectedness? repo pinned, genuine (push/license/tests), study path real?
assignments doable? AI scenarios concrete? placeholders absent?
3. Write `.agents/reviews/<slug>-YYYY-MM-DD.md` with per-section Accept/Revise + fixes.
Never edit the topic. Never flip `human-reviewed`.
4. Append `## [YYYY-MM-DD] lint | verify <slug> | <Accept|Revise>` to `.agents/log.md`.
