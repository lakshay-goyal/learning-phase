#!/usr/bin/env python3
"""3-layer gate for learning-phase vault (v6: notes/ + context/ folders).

Single topic: <Domain>/<Slug>/ with exactly <Slug>.md + <Slug>.resources.md + <Slug>.build.md.
Track: <Domain>/<Track>/ with hub <Track>.md at root + notes/<Slug>.md per subtopic
  + context/<Track>.resources.md + context/<Track>.build.md (ONE of each per track).
No per-subtopic folders. Resources = only for going beyond the listed scope.
Build = mini-projects over the whole topic, not homework.
HARD RULE: generic filenames (readme.md, build.md, sources.md, ...) fail L1 anywhere
in wiki folders — Obsidian graph/search shows filenames, so names must be self-describing
(<Slug>.md in notes/, <Track>.* in context/). Only exception: _MOC.md domain maps.

L1 static: structure, filenames, budgets, frontmatter, mermaid, neat-graph links, index, no placeholders.
L2 scope/state: feature_list.json valid (triple + legal states + WIP<=1 + VCR), DECISIONS.md present, log format.
L3 evidence: per-subtopic receipt in evidenceDir + resource verification + pinned repo genuineness.
--probe: opt-in live URL check (warnings only, never fails offline).
Errors are WHAT + WHY + FIX with file paths.
"""
import json, re, sys
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
cfg = json.loads((ROOT / ".agents" / "config.json").read_text())
HARNESS = cfg["harness"]
VERSION = cfg["version"]
EXCLUDE = set(cfg["wikiExclude"])
BANNED = {b.lower() for b in cfg["bannedFilenames"]}
B = cfg["budgets"]
TAX = json.loads((ROOT / cfg["taxonomyFile"]).read_text())
DOMAINS = {d["id"] for d in TAX["domains"]}
errors, warnings = [], []
layer_failed = {"L1": False, "L2": False, "L3": False}

def E(layer, msg):
    errors.append(f"{layer} {msg}")
    layer_failed[layer] = True

def W(msg):
    warnings.append(msg)

def slug_of(t: Path) -> str:
    return t.relative_to(ROOT).as_posix().lower().replace("/", "-")

def expected_files(folder: Path) -> list:
    n = folder.name
    return sorted([f"{n}.md", f"{n}.resources.md", f"{n}.build.md"])

def main_of(t: Path) -> Path:
    return t / f"{t.name}.md"

def resources_of(t: Path) -> Path:
    return t / f"{t.name}.resources.md"

def build_of(t: Path) -> Path:
    return t / f"{t.name}.build.md"

def track_res(t: Path) -> Path:
    return t / "context" / f"{t.name}.resources.md"

def track_build(t: Path) -> Path:
    return t / "context" / f"{t.name}.build.md"

def notes_dir(t: Path) -> Path:
    return t / "notes"

def context_dir(t: Path) -> Path:
    return t / "context"

def topics():
    """Every folder under a domain holding its own <Folder>.md main file.
    Excludes _MOC, domain roots, and the reserved notes/ + context/ folders."""
    out = []
    for d in DOMAINS:
        if d in EXCLUDE:
            E("L1", f"config domain {d} is in wikiExclude {sorted(EXCLUDE)} — WHY taxonomy and exclude list contradict — FIX remove it from one list")
    for d in DOMAINS:
        dp = ROOT / d
        if not dp.is_dir():
            continue
        for p in dp.rglob("*.md"):
            if p.name == "_MOC.md":
                continue
            folder = p.parent
            if folder == dp:
                continue  # domain root holds only _MOC.md, never a topic main
            if folder.name in ("notes", "context"):
                continue  # reserved folders hold files, not topics
            if p.name == folder.name + ".md":
                out.append(folder)
    return sorted(set(out))

def tracks():
    """Track = topic folder with a notes/ dir holding >=1 note. Returns (track_dir, hub, [note files])."""
    found = []
    for t in topics():
        nd = notes_dir(t)
        if nd.is_dir():
            notes = sorted(nd.glob("*.md"))
            if notes:
                found.append((t, t / f"{t.name}.md", notes))
    return sorted(found, key=lambda x: x[0].as_posix())

def fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    d = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            d[k.strip()] = v.strip()
    return d

def links(text):
    return re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text)

def urls(text):
    return re.findall(r"https?://[^\s\)>\]]+", text)

def resolve(link, topic_dir):
    link = link.strip()
    if link.startswith("http") or link.startswith("#"):
        return True
    target = link.split("#")[0].split("|")[0].strip()
    if not target:
        return True
    cands = [topic_dir / target, ROOT / target, ROOT / (target + ".md"), topic_dir / (target + ".md")]
    return any(c.exists() for c in cands)

# ---------- L1 static: HARD filename rule across all wiki folders ----------
for d in DOMAINS:
    dp = ROOT / d
    if not dp.is_dir():
        continue
    for p in dp.rglob("*.md"):
        rel = p.relative_to(ROOT).as_posix()
        if p.name == "_MOC.md":
            continue  # only exception: domain maps
        if p.name.lower() in BANNED:
            E("L1", f"{rel}: banned generic filename `{p.name}` — WHY Obsidian graph/search shows filenames, so generic names are unreadable nodes — FIX rename to a self-describing name: `<Slug>.md` in notes/, `<Track>.resources.md` / `<Track>.build.md` in context/")
        # folder-name match itself is enforced per-topic below (files != expected)

# ---------- L1 static: topic/track classification (v6) ----------
# Track = hub <Track>.md + notes/<Slug>.md per subtopic + context/<Track>.resources.md + context/<Track>.build.md.
# Single topic (not in a track) = full triple in its own folder.
all_topics = topics()
tracks_found = tracks()
track_dirs = {d for d, _, _ in tracks_found}
singles = sorted([t for t in all_topics if t not in track_dirs])
tlist = singles  # every folder carrying its own resources+build triple
idx_text = (ROOT / cfg["indexFile"]).read_text() if (ROOT / cfg["indexFile"]).exists() else ""
PLACEHOLDERS = ["<Human Title>", "<Domain-Id>", "https://…", "(https://…)", "YYYY-MM-DD"]
for t in tlist:
    rel = t.relative_to(ROOT).as_posix()
    want = expected_files(t)
    files = sorted(p.name for p in t.iterdir() if p.is_file() and not p.name.startswith("."))
    if files != want:
        E("L1", f"{rel}: must contain exactly {want}, has {files} — WHY one single topic = main + resources + build, all folder-named — FIX rename/add/remove to match")
    budgets = [(main_of(t).name, "readmeMaxLines"), (resources_of(t).name, "resourcesMaxLines"), (build_of(t).name, "buildMaxLines")]
    for fname, key in budgets:
        p = t / fname
        if p.exists() and len(p.read_text().splitlines()) > B[key]:
            E("L1", f"{rel}/{fname}: {len(p.read_text().splitlines())} lines > budget {B[key]} — WHY budgets keep notes readable — FIX compress or split into a new subtopic")
    for fname in [main_of(t).name, resources_of(t).name, build_of(t).name]:
        p = t / fname
        if p.exists():
            txt = p.read_text()
            for ph in PLACEHOLDERS:
                if ph in txt:
                    E("L1", f"{rel}/{fname}: contains placeholder `{ph}` — WHY template filler is not research — FIX replace with real content")
                    break
    rd = main_of(t).read_text() if main_of(t).exists() else ""
    meta = fm(rd)
    if not meta:
        E("L1", f"{rel}: main file {main_of(t).name} missing YAML frontmatter — WHY status/domain/related drive index + graph — FIX copy template header")
        continue
    if meta.get("domain") not in DOMAINS:
        E("L1", f"{rel}: domain `{meta.get('domain')}` not in taxonomy.json — WHY nesting must be machine-checkable — FIX pick from taxonomy or add domain + MOC")
    if meta.get("status") not in ("draft", "researched", "human-reviewed"):
        E("L1", f"{rel}: bad status `{meta.get('status')}` — WHY only these 3 states exist — FIX use draft|researched|human-reviewed")
    reltd = re.findall(r'"\[\[.+?\]\]"|\'\[\[.+?\]\]\'', rd)
    if len(reltd) > B["maxRelated"]:
        E("L1", f"{rel}: {len(reltd)} related > {B['maxRelated']} — WHY neat graph beats Pati-graph — FIX keep ≤{B['maxRelated']} real links")
    wl = links(rd)
    if len(wl) > B["maxWikilinksPerReadme"]:
        E("L1", f"{rel}/{main_of(t).name}: {len(wl)} wikilinks > {B['maxWikilinksPerReadme']} — WHY every link is graph noise — FIX link hub/siblings/MOC only")
    if cfg["requireMermaidInReadme"] and "```mermaid" not in rd:
        E("L1", f"{rel}/{main_of(t).name}: missing ```mermaid block — WHY graph over paragraphs is the contract — FIX add one flow/architecture/user-flow diagram")
    for Lk in wl:
        if not resolve(Lk, t):
            W(f"{rel}: unresolved link [[{Lk}]] — check spelling or create the note")
    if cfg["requireIndexEntry"] and rel not in idx_text:
        E("L1", f"{rel}: missing row in {cfg['indexFile']} — WHY index is the navigator — FIX add one table row")
    res = resources_of(t).read_text() if resources_of(t).exists() else ""
    rows = [l for l in res.splitlines() if l.strip().startswith("|") and "http" in l]
    if len(rows) > B["resourcesMaxEntries"]:
        E("L1", f"{rel}/{resources_of(t).name}: {len(rows)} entries > max {B['resourcesMaxEntries']} — WHY most-linked-first beats link dumps — FIX keep top {B['resourcesMaxEntries']}")

# ---------- L1 static: track notes (v6: notes/<Slug>.md files) ----------
track_notes = [(d, n) for d, _, notes in tracks_found for n in notes]
for track_dir, note in track_notes:
    rel = note.relative_to(ROOT).as_posix()
    rel_naked = rel[:-3] if rel.endswith(".md") else rel
    if note.name.lower() in BANNED:
        E("L1", f"{rel}: banned generic filename — WHY note names must be self-describing in graph/search — FIX rename to <Slug>.md")
        continue
    rd = note.read_text()
    for ph in PLACEHOLDERS:
        if ph in rd:
            E("L1", f"{rel}: contains placeholder `{ph}` — WHY template filler is not research — FIX replace with real content")
            break
    if len(rd.splitlines()) > B["readmeMaxLines"]:
        E("L1", f"{rel}: {len(rd.splitlines())} lines > budget {B['readmeMaxLines']} — WHY budgets keep notes readable — FIX compress or split into a new note")
    meta = fm(rd)
    if not meta:
        E("L1", f"{rel}: missing YAML frontmatter — WHY status/domain/related drive index + graph — FIX copy template header")
        continue
    if meta.get("domain") not in DOMAINS:
        E("L1", f"{rel}: domain `{meta.get('domain')}` not in taxonomy.json — WHY nesting must be machine-checkable — FIX pick from taxonomy or add domain + MOC")
    if meta.get("status") not in ("draft", "researched", "human-reviewed"):
        E("L1", f"{rel}: bad status `{meta.get('status')}` — WHY only these 3 states exist — FIX use draft|researched|human-reviewed")
    reltd = re.findall(r'"\[\[.+?\]\]"|\'\[\[.+?\]\]\'', rd)
    if len(reltd) > B["maxRelated"]:
        E("L1", f"{rel}: {len(reltd)} related > {B['maxRelated']} — WHY neat graph beats Pati-graph — FIX keep ≤{B['maxRelated']} real links")
    wl = links(rd)
    if len(wl) > B["maxWikilinksPerReadme"]:
        E("L1", f"{rel}: {len(wl)} wikilinks > {B['maxWikilinksPerReadme']} — WHY every link is graph noise — FIX link hub/siblings/MOC only")
    if cfg["requireMermaidInReadme"] and "```mermaid" not in rd:
        E("L1", f"{rel}: missing ```mermaid block — WHY graph over paragraphs is the contract — FIX add one flow/architecture/user-flow diagram")
    for Lk in wl:
        if not resolve(Lk, note.parent):
            W(f"{rel}: unresolved link [[{Lk}]] — check spelling or create the note")
    if cfg["requireIndexEntry"] and rel_naked not in idx_text:
        E("L1", f"{rel}: missing row in {cfg['indexFile']} — WHY index is the navigator — FIX add one table row")

# track hubs + folders
for track_dir, hub, notes in tracks_found:
    rel = track_dir.relative_to(ROOT).as_posix()
    if not hub.exists():
        E("L1", f"{rel}: track has {len(notes)} note(s) but no hub {hub.name} — WHY the hub is the navigator — FIX create {hub.name} with links to each note")
        continue
    htxt = hub.read_text()
    if len(htxt.splitlines()) > B["hubMaxLines"]:
        E("L1", f"{rel}/{hub.name}: {len(htxt.splitlines())} lines > budget {B['hubMaxLines']} — WHY hub is a map not a dump — FIX link notes, move detail down")
    if fm(htxt) is None:
        E("L1", f"{rel}/{hub.name}: missing YAML frontmatter — WHY hub must be searchable — FIX copy hub template header")
    if cfg.get("requireMermaidInHub") and "```mermaid" not in htxt:
        E("L1", f"{rel}/{hub.name}: missing ```mermaid block — WHY track needs one visual map — FIX add track diagram")
    for ph in PLACEHOLDERS:
        if ph in htxt:
            E("L1", f"{rel}/{hub.name}: contains placeholder `{ph}` — FIX replace with real content")
            break
    for n in notes:
        if n.stem not in htxt and n.relative_to(ROOT).as_posix() not in htxt:
            E("L1", f"{rel}/{hub.name}: does not link note {n.stem} — WHY hub is the single navigator — FIX add a row/link per note")
    for Lk in links(htxt):
        if not resolve(Lk, track_dir):
            W(f"{rel}/{hub.name}: unresolved link [[{Lk}]] — check spelling or create the note")
    if cfg["requireIndexEntry"] and rel not in idx_text:
        E("L1", f"{rel}: hub track missing row in {cfg['indexFile']} — WHY index must list the track — FIX add one track row")
    # v6 folders: root holds only the hub; retired per-subtopic folders fail; context/ holds exactly the two track files
    for p in track_dir.iterdir():
        if p.is_file() and not p.name.startswith(".") and p.suffix == ".md" and p.name != hub.name:
            E("L1", f"{rel}/{p.name}: stray file in track root — WHY v6 track root holds only the hub; notes go in notes/, resources+build in context/ — FIX move it and delete")
    for child in sorted(track_dir.iterdir()):
        if child.is_dir() and child.name not in ("notes", "context") and any(child.rglob("*.md")):
            E("L1", f"{rel}/{child.name}: retired per-subtopic folder — WHY v6 keeps all notes directly in notes/ (one folder per note made no sense) — FIX move its note into notes/ and delete the folder")
    want_ctx = sorted([track_res(track_dir).name, track_build(track_dir).name])
    have_ctx = sorted(p.name for p in context_dir(track_dir).iterdir() if p.is_file() and not p.name.startswith(".")) if context_dir(track_dir).is_dir() else []
    if have_ctx != want_ctx:
        E("L1", f"{rel}/context: must contain exactly {want_ctx}, has {have_ctx} — WHY one resources + one build per track, track-named — FIX rename/add/remove to match")
    else:
        for fp, key in [(track_res(track_dir), "resourcesMaxLines"), (track_build(track_dir), "buildMaxLines")]:
            ftxt = fp.read_text()
            if len(ftxt.splitlines()) > B[key]:
                E("L1", f"{rel}/context/{fp.name}: {len(ftxt.splitlines())} lines > budget {B[key]} — WHY budgets keep files readable — FIX keep only the most-connected resources / highest-value mini-projects")
            for ph in PLACEHOLDERS:
                if ph in ftxt:
                    E("L1", f"{rel}/context/{fp.name}: contains placeholder `{ph}` — FIX replace with real content")
                    break

# ---------- L2 scope/state ----------
flp = ROOT / cfg["featureListPath"]
try:
    fl = json.loads(flp.read_text())
    feats = fl.get("features", [])
    legal = {"not-started", "in-progress", "blocked", "done"}
    active = 0
    for f in feats:
        if not all(k in f for k in ("id", "behavior", "verification", "state")):
            E("L2", f"feature_list.json entry {f.get('id', '?')}: missing id|behavior|verification|state triple — WHY scope must be machine-readable — FIX complete the triple")
        if f.get("state") not in legal:
            E("L2", f"feature {f.get('id')}: illegal state `{f.get('state')}` — WHY states drive WIP/VCR — FIX use {sorted(legal)}")
        if f.get("state") == "in-progress":
            active += 1
        if f.get("state") == "done" and not f.get("evidence"):
            E("L2", f"feature {f.get('id')}: state done without evidence — WHY done needs proof — FIX record check output or revert state")
    if active > 1:
        E("L2", f"WIP={active} > 1 — WHY one track at a time prevents under-finish — FIX finish or block extras")
    passing = sum(1 for f in feats if f.get("state") == "done")
    activated = sum(1 for f in feats if f.get("state") in ("in-progress", "blocked", "done"))
    vcr = (passing / activated) if activated else 1.0
    vcr_str = f"{passing}/{activated}={vcr:.2f}"
except Exception as ex:
    E("L2", f"cannot read {cfg['featureListPath']}: {ex} — WHY scope is the system of record — FIX restore valid JSON")
    vcr_str = "n/a"
if not (ROOT / cfg["decisionsFile"]).exists():
    E("L2", f"{cfg['decisionsFile']} missing — WHY why-not-what must persist — FIX recreate with date/reason/rejected-alternative")
logp = ROOT / cfg["logFile"]
if not logp.exists():
    E("L2", f"{cfg['logFile']} missing — WHY timeline is append-only memory — FIX recreate log.md")
elif not re.search(r"^## \[\d{4}-\d{2}-\d{2}\] (research|update|lint|review-human) \|", logp.read_text(), re.M):
    E("L2", f"{cfg['logFile']}: no well-formed `## [YYYY-MM-DD] verb | ...` entries — WHY grep-able history matters — FIX use the four verbs")

# ---------- L3 evidence ----------
evdir = ROOT / cfg["evidenceDir"]
revdir = ROOT / cfg["reviewsDir"]
def check_receipt(rel: str, slug: str):
    rp = evdir / f"{slug}.json"
    if not rp.exists():
        E("L3", f"{rel}: missing receipt {cfg['evidenceDir']}/{slug}.json — WHY done needs executable evidence — FIX run learn-topic Finish step to write it")
        return
    try:
        r = json.loads(rp.read_text())
        if not all(k in r for k in ("slug", "checks", "result")):
            E("L3", f"{rel}: receipt lacks slug|checks|result — WHY receipts must be replayable — FIX rewrite receipt with commands + exit codes")
        elif r.get("result") != "pass":
            W(f"{rel}: receipt result `{r.get('result')}` — last gate did not pass")
    except Exception as ex:
        E("L3", f"{rel}: receipt unreadable: {ex} — FIX rewrite valid JSON")

def check_resources_file(rel: str, fname: str, text: str):
    rows = [l for l in text.splitlines() if l.strip().startswith("|") and "http" in l]
    if len(rows) < cfg["minResourceEntries"]:
        E("L3", f"{rel}/{fname}: {len(rows)} linked entries < min {cfg['minResourceEntries']} — WHY depth needs breadth first — FIX research docs→papers→blogs→repos, min 5 opened")
    if len(rows) > B["resourcesMaxEntries"]:
        E("L3", f"{rel}/{fname}: {len(rows)} entries > max {B['resourcesMaxEntries']} — WHY most-linked-first beats link dumps — FIX keep top {B['resourcesMaxEntries']}")
    if "OPENED" not in text and "UNVERIFIED" not in text:
        E("L3", f"{rel}/{fname}: no OPENED/UNVERIFIED verification labels — WHY every link needs a trust label — FIX mark each entry OPENED <date> or UNVERIFIED + reason")

def check_build_file(rel: str, fname: str, text: str):
    repos = [l for l in text.splitlines() if "github.com" in l or "gitlab.com" in l]
    if not repos:
        E("L3", f"{rel}/{fname}: no pinned OSS repo — WHY production code beats tutorial hell — FIX add 1–3 repos with commit + study path")
    elif not re.search(r"\b[0-9a-f]{7,40}\b", text):
        E("L3", f"{rel}/{fname}: no pinned commit hash — WHY unpinned repos drift — FIX pin short SHA + last-push date")

if cfg["requireEvidenceReceipt"] and not layer_failed["L1"]:
    for t in tlist:
        check_receipt(t.relative_to(ROOT).as_posix(), slug_of(t))
    for track_dir, _, _ in tracks_found:
        check_receipt(track_dir.relative_to(ROOT).as_posix(), slug_of(track_dir))
if cfg["requireResourceVerification"]:
    for t in tlist:
        rel = t.relative_to(ROOT).as_posix()
        if resources_of(t).exists():
            check_resources_file(rel, resources_of(t).name, resources_of(t).read_text())
        if build_of(t).exists():
            check_build_file(rel, build_of(t).name, build_of(t).read_text())
    for track_dir, _, _ in tracks_found:
        rel = track_dir.relative_to(ROOT).as_posix()
        if track_res(track_dir).exists():
            check_resources_file(rel, f"context/{track_res(track_dir).name}", track_res(track_dir).read_text())
        else:
            E("L3", f"{rel}: missing context/{track_res(track_dir).name} — WHY one beyond-scope reading path per track — FIX create it from the track-resources template")
        if track_build(track_dir).exists():
            check_build_file(rel, f"context/{track_build(track_dir).name}", track_build(track_dir).read_text())
        else:
            E("L3", f"{rel}: missing context/{track_build(track_dir).name} — WHY one mini-project file per track — FIX create it from the track-build template")
if not revdir.is_dir():
    W(f"{cfg['reviewsDir']} missing — verifier has nowhere to write; create it")

# ---------- opt-in live probe ----------
if "--probe" in sys.argv:
    from urllib.error import URLError
    probe_targets = [(t.relative_to(ROOT).as_posix(), resources_of(t)) for t in tlist]
    probe_targets += [(d.relative_to(ROOT).as_posix(), track_res(d)) for d, _, _ in tracks_found]
    for rel, fp in probe_targets:
        for u in urls((fp.read_text() if fp.exists() else "")):
            try:
                req = Request(u, headers={"User-Agent": "vault-probe"}, method="HEAD")
                code = urlopen(req, timeout=8).status
                if code >= 400:
                    W(f"{rel}: {u} -> HTTP {code}")
            except Exception as ex:
                W(f"{rel}: {u} unreachable ({type(ex).__name__}) — re-check or mark UNVERIFIED")

print(f"[{HARNESS} v{VERSION}] notes: {len(track_notes) + len(tlist)} tracks: {len(tracks_found)} singles: {len(tlist)} VCR: {vcr_str} errors: {len(errors)} warnings: {len(warnings)}")
for e in errors:
    print("ERROR " + e)
for w in warnings:
    print("WARN " + w)
sys.exit(1 if errors else 0)
