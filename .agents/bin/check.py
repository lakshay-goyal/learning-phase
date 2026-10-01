#!/usr/bin/env python3
"""3-layer gate for learning-phase vault. Every config.json key is consumed here.

L1 static: structure, budgets, frontmatter, mermaid, neat-graph links, index, no placeholders.
L2 scope/state: feature_list.json valid (triple + legal states + WIP<=1 + VCR), DECISIONS.md present, log format.
L3 evidence: per-topic receipt in evidenceDir + resource verification columns + pinned repo genuineness.
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
TOPIC_FILES = cfg["topicFiles"]
B = cfg["budgets"]
TAX = json.loads((ROOT / cfg["taxonomyFile"]).read_text())
DOMAINS = {d["id"] for d in TAX["domains"]}
errors, warnings = [], []
layer_failed = {"L1": False, "L2": False, "L3": False}

def E(layer, msg):
    errors.append(f"{layer} {msg}")
    layer_failed[layer] = True

def W(msg):
    warnings.append(f"WARN {msg}")

def slug_of(t: Path) -> str:
    return t.relative_to(ROOT).as_posix().lower().replace("/", "-")

def topics():
    out = []
    for d in DOMAINS:
        if d in EXCLUDE:
            E("L1", f"config domain {d} is in wikiExclude {sorted(EXCLUDE)} — WHY taxonomy and exclude list contradict — FIX remove it from one list")
    for d in DOMAINS:
        dp = ROOT / d
        if not dp.is_dir():
            continue
        for p in dp.rglob("README.md"):
            t = p.parent
            if (t / "resources.md").exists() and t != dp:
                out.append(t)
    return sorted(set(out))

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
    target = link.split("#")[0]
    cands = [topic_dir / target, ROOT / target, ROOT / (target + ".md"), topic_dir / (target + ".md")]
    return any(c.exists() for c in cands)

# ---------- L1 static ----------
tlist = topics()
idx_text = (ROOT / cfg["indexFile"]).read_text() if (ROOT / cfg["indexFile"]).exists() else ""
PLACEHOLDERS = ["<Human Title>", "<Domain-Id>", "https://…", "(https://…)", "YYYY-MM-DD"]
for t in tlist:
    rel = t.relative_to(ROOT).as_posix()
    files = sorted(p.name for p in t.iterdir() if p.is_file() and not p.name.startswith("."))
    if files != sorted(TOPIC_FILES):
        E("L1", f"{rel}: must contain exactly {TOPIC_FILES}, has {files} — WHY extra files create hop hell — FIX keep README/resources/build only")
    for fname, key in [("README.md", "readmeMaxLines"), ("resources.md", "resourcesMaxLines"), ("build.md", "buildMaxLines")]:
        p = t / fname
        if p.exists() and len(p.read_text().splitlines()) > B[key]:
            E("L1", f"{rel}/{fname}: {len(p.read_text().splitlines())} lines > budget {B[key]} — WHY conciseness is the contract — FIX compress, move detail to the correct file")
    for fname in TOPIC_FILES:
        p = t / fname
        if p.exists():
            txt = p.read_text()
            for ph in PLACEHOLDERS:
                if ph in txt:
                    E("L1", f"{rel}/{fname}: contains placeholder `{ph}` — WHY template filler is not research — FIX replace with real content")
                    break
    rd = (t / "README.md").read_text() if (t / "README.md").exists() else ""
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
        E("L1", f"{rel}: {len(reltd)} related > {B['maxRelated']} — WHY neat graph beats Pati-graph — FIX keep ≤4 real links")
    wl = links(rd)
    if len(wl) > B["maxWikilinksPerReadme"]:
        E("L1", f"{rel}/README.md: {len(wl)} wikilinks > {B['maxWikilinksPerReadme']} — WHY every link is graph noise — FIX link MOC/index/siblings/≤4 related only")
    if cfg["requireMermaidInReadme"] and "```mermaid" not in rd:
        E("L1", f"{rel}/README.md: missing ```mermaid block — WHY graph over paragraphs is the contract — FIX add one flow/architecture/user-flow diagram")
    for Lk in wl:
        if not resolve(Lk, t):
            W(f"{rel}: unresolved link [[{Lk}]] — check spelling or create the note")
    if cfg["requireIndexEntry"] and rel not in idx_text:
        E("L1", f"{rel}: missing row in {cfg['indexFile']} — WHY index is the navigator — FIX add one table row")

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
        E("L2", f"WIP={active} > 1 — WHY one topic at a time prevents under-finish — FIX finish or block extras")
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
if cfg["requireEvidenceReceipt"] and not layer_failed["L1"]:
    for t in tlist:
        rel = t.relative_to(ROOT).as_posix()
        slug = slug_of(t)
        rp = evdir / f"{slug}.json"
        if not rp.exists():
            E("L3", f"{rel}: missing receipt {cfg['evidenceDir']}/{slug}.json — WHY done needs executable evidence — FIX run learn-topic Finish step to write it")
            continue
        try:
            r = json.loads(rp.read_text())
            if not all(k in r for k in ("slug", "checks", "result")):
                E("L3", f"{rel}: receipt lacks slug|checks|result — WHY receipts must be replayable — FIX rewrite receipt with commands + exit codes")
            elif r.get("result") != "pass":
                W(f"{rel}: receipt result `{r.get('result')}` — last gate did not pass")
        except Exception as ex:
            E("L3", f"{rel}: receipt unreadable: {ex} — FIX rewrite valid JSON")
if cfg["requireResourceVerification"]:
    for t in tlist:
        rel = t.relative_to(ROOT).as_posix()
        res = (t / "resources.md").read_text() if (t / "resources.md").exists() else ""
        rows = [l for l in res.splitlines() if l.strip().startswith("|") and "http" in l]
        if len(rows) < cfg["minResourceEntries"]:
            E("L3", f"{rel}/resources.md: {len(rows)} linked entries < min {cfg['minResourceEntries']} — WHY depth needs breadth first — FIX research docs→papers→blogs→repos, min 5 opened")
        if "OPENED" not in res and "UNVERIFIED" not in res:
            E("L3", f"{rel}/resources.md: no OPENED/UNVERIFIED verification labels — WHY every link needs a trust label — FIX mark each entry OPENED <date> or UNVERIFIED + reason")
        bld = (t / "build.md").read_text() if (t / "build.md").exists() else ""
        repos = [l for l in bld.splitlines() if "github.com" in l or "gitlab.com" in l]
        if not repos:
            E("L3", f"{rel}/build.md: no pinned OSS repo — WHY production code beats tutorial hell — FIX add 1–3 repos with commit + study path")
        elif not re.search(r"\b[0-9a-f]{7,40}\b", bld):
            E("L3", f"{rel}/build.md: no pinned commit hash — WHY unpinned repos drift — FIX pin short SHA + last-push date")
if not revdir.is_dir():
    W(f"{cfg['reviewsDir']} missing — verifier has nowhere to write; create it")

# ---------- opt-in live probe ----------
if "--probe" in sys.argv:
    from urllib.error import URLError
    for t in tlist:
        rel = t.relative_to(ROOT).as_posix()
        for u in urls(((t / "resources.md").read_text() if (t / "resources.md").exists() else "")):
            try:
                req = Request(u, headers={"User-Agent": "vault-probe"}, method="HEAD")
                code = urlopen(req, timeout=8).status
                if code >= 400:
                    W(f"{rel}: {u} -> HTTP {code}")
            except Exception as ex:
                W(f"{rel}: {u} unreachable ({type(ex).__name__}) — re-check or mark UNVERIFIED")

print(f"[{HARNESS} v{VERSION}] topics: {len(tlist)} VCR: {vcr_str} errors: {len(errors)} warnings: {len(warnings)}")
for e in errors:
    print("ERROR " + e)
for w in warnings:
    print("WARN " + w)
sys.exit(1 if errors else 0)
