# Progress — updated 2026-10-02

## Current state

3-layer gate live (L1 static / L2 scope+state / L3 evidence). `verify-topic` added;
generator never self-grades. `check.py` green, dead keys 0.

## In flight

Nothing. (WIP = 1: one topic at a time.)

## Blocked

Nothing.

## Next session starts

```bash
cat .agents/PROGRESS.md
python3 .agents/bin/check.py
```

## Last green baseline

`python3 .agents/bin/check.py` → [v2] 0 topics, VCR 1/1=1.00, 0 errors (2026-10-02). Dead keys: none.
