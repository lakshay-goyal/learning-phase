---
name: verify-topic
description: "Independently review one topic package; write verdicts to reviews/ without editing it."
invocation: user
---

# Verify-Topic

Independent evaluator (generator ≠ evaluator). Read-only on the topic.

1. Read the topic: single (`<Domain>/<Slug>/` triple) or track (hub + `notes/` + `context/`, ONE `<Track>.resources.md` + ONE `<Track>.build.md`) + receipt in `.agents/evidence/` (one per topic/track).
2. Check: notes correct + beginner-friendly (plain words, jargon defined inline, fresher can follow Intuition)? snippet per concept (1–5 lines + expected output, no paragraph-where-snippet-fits)? visual accurate + matches snippets? notes all in `notes/`, no per-subtopic folders, context holds exactly the two track files? track resources = beyond-scope deepening only, ≥5 entries with trust
labels + connectedness + row 1 is a 10-min starter? track build = mini-projects over the whole topic (real ship-able things, exact commands + done-state + common error + fix, not homework) + repo pinned, genuine (push/license/tests), study path fresher-followable?
AI scenarios concrete (who + task + copy-paste prompt, no generic lines)? use cases real job tasks + ≥1 edge case? placeholders absent?
3. Write `.agents/reviews/<slug>-YYYY-MM-DD.md` with per-section Accept/Revise + fixes.
Never edit the topic. Never flip `human-reviewed`.
4. Append `## [YYYY-MM-DD] lint | verify <slug> | <Accept|Revise>` to `.agents/log.md`.
