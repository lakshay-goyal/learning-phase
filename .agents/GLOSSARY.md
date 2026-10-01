# Glossary

One term, one meaning. Add here before using a new load-bearing word.

**Harness**
: This vault's instructions + skills + templates + `check.py` taken together.
_Avoid:_ framework, scaffolding.

**Topic**
: One bounded concept with one folder `<Domain>/<Topic-Slug>/` and 3 files.
Not a file, not a domain. _Avoid:_ note, module, course.

**Domain**
: Top-level folder from `.agents/taxonomy.json` (e.g. `AI-Engineering`).
_Avoid:_ category, field.

**Raw source**
: Immutable file under `raw/`. LLM reads, never edits. _Avoid:_ reference note.

**Wiki page**
: LLM-maintained markdown under a topic folder or domain `_MOC.md`.
_Avoid:_ raw dump, clip.

**Index**
: `.agents/index.md` — content catalog (hidden from reading view), one row per topic. _Avoid:_ log, MOC.

**Log**
: `.agents/log.md` — append-only timeline (hidden from reading view). _Avoid:_ index.

**MOC**
: `<Domain>/_MOC.md` — map of content for one domain, ≤30 lines.
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
