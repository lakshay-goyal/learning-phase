#!/usr/bin/env python3
"""Static gate for learning-phase vault. Every config.json key is consumed here."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
cfg = json.loads((ROOT / ".agents" / "config.json").read_text())
HARNESS = cfg["harness"]  # identity, shown in output
VERSION = cfg["version"]
EXCLUDE = set(cfg["wikiExclude"])
TAX = json.loads((ROOT / cfg["taxonomyFile"]).read_text())

DOMAINS = {d["id"] for d in TAX["domains"]}
TOPIC_FILES = cfg["topicFiles"]
B = cfg["budgets"]
errors, warnings = [], []

def topics():
    out = []
    for d in DOMAINS:
        if d in EXCLUDE:
            errors.append(f"domain {d} is in wikiExclude")
            continue
    for d in DOMAINS:
        dp = ROOT / d
        if not dp.is_dir():
            continue
        for sub in dp.iterdir():
            if sub.is_dir() and (sub / "README.md").exists():
                out.append(sub)
            elif sub.name == "_MOC.md":
                continue
    # nested one deeper e.g. AI-Engineering/RAG/X
    for d in DOMAINS:
        for p in (ROOT / d).rglob("README.md"):
            t = p.parent
            if t not in out and t != ROOT / d and (t / "resources.md").exists():
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

def resolve(link, topic_dir):
    link = link.strip()
    if link.startswith("http") or link.startswith("#"):
        return True
    target = link.split("#")[0]
    cands = [topic_dir / target, ROOT / target,
             ROOT / (target + ".md"), topic_dir / (target + ".md")]
    return any(c.exists() for c in cands)

tlist = topics()
idx_text = (ROOT / cfg["indexFile"]).read_text() if (ROOT / cfg["indexFile"]).exists() else ""
for t in tlist:
    rel = t.relative_to(ROOT).as_posix()
    files = sorted(p.name for p in t.iterdir() if p.is_file() and not p.name.startswith("."))
    if files != sorted(TOPIC_FILES):
        errors.append(f"{rel}: must contain exactly {TOPIC_FILES}, has {files}")
    for fname, key in [("README.md", "readmeMaxLines"), ("resources.md", "resourcesMaxLines"), ("build.md", "buildMaxLines")]:
        p = t / fname
        if p.exists() and len(p.read_text().splitlines()) > B[key]:
            errors.append(f"{rel}/{fname}: over budget {B[key]} lines")
    rd = (t / "README.md").read_text() if (t / "README.md").exists() else ""
    meta = fm(rd)
    if not meta:
        errors.append(f"{rel}: missing frontmatter")
        continue
    if meta.get("domain") not in DOMAINS:
        errors.append(f"{rel}: domain {meta.get('domain')} not in taxonomy.json")
    if meta.get("status") not in ("draft", "researched", "human-reviewed"):
        errors.append(f"{rel}: bad status {meta.get('status')}")
    reltd = re.findall(r'"\[\[.+?\]\]"|\'\[\[.+?\]\]\'', rd)
    if len(reltd) > B["maxRelated"]:
        errors.append(f"{rel}: related > {B['maxRelated']}")
    wl = links(rd)
    if len(wl) > B["maxWikilinksPerReadme"]:
        errors.append(f"{rel}/README.md: {len(wl)} wikilinks > {B['maxWikilinksPerReadme']} (neat-graph rule)")
    if cfg["requireMermaidInReadme"] and "```mermaid" not in rd:
        errors.append(f"{rel}/README.md: missing ```mermaid diagram")
    for L in wl:
        if not resolve(L, t):
            warnings.append(f"{rel}: unresolved link [[{L}]]")
    if cfg["requireIndexEntry"] and rel not in idx_text:
        errors.append(f"{rel}: missing row in {cfg['indexFile']}")

if not (ROOT / cfg["logFile"]).exists():
    errors.append("log.md missing")
print(f"[{HARNESS} v{VERSION}] topics: {len(tlist)}  errors: {len(errors)}  warnings: {len(warnings)}")
for e in errors:
    print("ERROR " + e)
for w in warnings:
    print("WARN " + w)
if "--fix-index" in sys.argv:
    print("(fix-index: only adds missing rows; run learn-topic for content)")
sys.exit(1 if errors else 0)
