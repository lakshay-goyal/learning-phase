# Glossary

One term, one meaning. Add here before using a new load-bearing word.

**Harness**
: This vault's instructions + skills + templates + `check.py` taken together.
_Avoid:_ framework, scaffolding.

**Topic**
: One bounded concept with one folder `<Domain>/<Topic-Slug>/` and 3 files.
Not a file, not a domain. _Avoid:_ note, module, course.
In a track there are no per-subtopic folders: all notes live together in `notes/`
as `<Slug>.md` files; resources + build live together in `context/`, once per track.

**Track resources**
: ONE `context/<Track>.resources.md` per track — only for going beyond the listed
scope. If the notes + mini-projects covered it, the reader never opens this file.
_Avoid:_ per-subtopic resource dumps.

**Track build**
: ONE `context/<Track>.build.md` per track — 2–3 mini-projects over the whole topic
(real ship-able things touching ≥3 subtopics) + pinned OSS repos. Not homework,
not one-subtopic drills. _Avoid:_ small assignments, per-subtopic build files.

**Domain**
: Top-level folder from `.agents/taxonomy.json` (e.g. `AI-Engineering`).
_Avoid:_ category, field.

**Raw source**
: Immutable file under `raw/`. LLM reads, never edits. _Avoid:_ reference note.

**Wiki page**
: LLM-maintained markdown under a topic folder, track hub, or folder-named domain hub.
_Avoid:_ raw dump, clip.

**Index**
: `.agents/index.md` — content catalog (hidden from reading view), one row per topic. _Avoid:_ log, domain hub.

**Log**
: `.agents/log.md` — append-only timeline (hidden from reading view). _Avoid:_ index.

**Domain hub**
: `<Domain>/<Domain>.md` — map of tracks for one populated domain (links its track hubs + sibling domain hubs, never notes), ≤30 lines.
_Avoid:_ index.

**Research status**
: `draft` (LLM working) → `researched` (LLM done, needs human read) →
`human-reviewed` (human only). Never `validated`/`mastered`.
_Avoid:_ progress, completion.

**NEAT graph**
: Link budget — README links ≤10 wikilinks total, `related` ≤4 real notes.
Prevents the Pati-graph (everything linked to everything). _Avoid:_ full mesh.

**Karpathy-style**
: Intuition first, plain words before jargon, one mental model + one concrete
example. If intuition section needs the mechanism section to be understood, rewrite.
Beginner-first extension: fresher with zero background, no storytelling, snippet beats
paragraph (1–5 lines + expected output per concept), jargon defined inline in 5–8 words.

**Beginner-first**
: Every wiki output assumes zero prior knowledge: plain words, one idea per block,
minimal text + maximum runnable snippets, real job use case + ≥1 edge case per subtopic,
each section ends with something the reader can now DO. _Avoid:_ jargon dumps, storytelling, generic filler.
