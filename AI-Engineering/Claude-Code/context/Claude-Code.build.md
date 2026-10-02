---
topic: Claude Code
domain: AI-Engineering
status: researched
updated: 2026-10-02
related: []
tags: [claude-code, build]
track: Claude Code
---

# Claude Code — Build

> The ONLY build file for this whole track. Mini-projects that sharpen the ENTIRE topic — not homework, not one-subtopic drills. Pick one, ship it, prove you own the track.

## Production codebases to study (1–3, pinned — required)

| Repo | Signals (stars / users / last push / license) | Commit | Study guide (real file path, end-to-end trace) |
|---|---|---|---|
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 148921★, 25153 forks, push 2026-10-01, license null in API (see repo LICENSE) | `52c76441` | Read `README.md` → `.claude/commands/` → CLI perms/hooks wiring; run `claude --help` + `/context` |
| [anthropics/skills](https://github.com/anthropics/skills) | 179377★, 21209 forks, push 2026-09-29, license null in API (see repo) | `8a1541c4` | Read `skills/` example → `spec/` Agent Skills standard → `template/` starter; copy one SKILL.md into `.claude/skills/` |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 90950★, 11750 forks, push 2026-10-01, Other/NOASSERTION | `f46d9578` | Read `src/sqlite/` → `src/github/` → `README.md` quickstart; add sqlite server via `claude mcp add` |

Opened API listings 2026-10-02 (commit SHAs + push dates above). Licenses via API null/Other — check repo root before vendoring.

## Mini-projects (do 1 — each covers the whole track)

1. **Mini-project 1 (1–2 days):** Ship Spendly auth with spec→plan→hooks (touches 06, 07, 08, 12).
   ```bash
   git checkout -b feature/auth && /create-spec 02 register
   /plan
   # done looks like: /register + /login work, hash stored, guards redirect, hook blocks f-string SQL
   # if you see plain-text password: you skipped hash — fix: generate_password_hash + parameterized ?
   ```
   Who benefits: juniors proving SDD + job demo of safe auth.
2. **Mini-project 2 (2–3 days):** Test + review gate for one feature (touches 07, 10, 08).
   ```bash
   /test-feature 06-date-filter-profile
   /code-review-feature 06-date-filter-profile
   # done looks like: 70+ tests table + security report, f-string fixed after approval
   # if tests pass but spec fails: you tested code not spec — fix: rewrite tests from spec file
   ```
   Who benefits: teams needing trustworthy AI tests + solo devs catching injection.
3. **Mini-project 3 (3–5 days):** MCP + plugin + Railway ship (touches 11, 12, 09).
   ```bash
   claude mcp add --transport stdio sqlite -- npx -y @executeautomation/database-server $PWD/spendly.db
   /plugin install railway@railway-skills
   # done looks like: "total by category" via MCP works, public Railway URL live, Postgres noted for real data
   # if DB wipes on redeploy: SQLite ephemeral — fix: switch Postgres/MySQL before users
   ```
   Who benefits: freelancers shipping Flask demos without DevOps pain.

## Ideas, use cases & missed aspects

- AI-era scenario: incident→fix from Slack via MCP (who: on-call; task: read #incidents, patch, draft notify; fits: no dashboard hopping).
- Real use case: client demo kit — CLAUDE.md + 2 skills + 2 hooks + sqlite MCP + Railway plugin = repeatable 1-prompt deploys. Who pays: agencies with junior-heavy teams.
- Edge case track-wide: PAT committed to git + 10 MCP servers on = leak + slow. Fix order: revoke PAT first, gitignore env, keep minimal servers.
  ```bash
  claude mcp remove old-server && git rm --cached .env
  ```

## Human feedback (only human edits)

- [ ] I read the track notes + opened 1 resource + 1 repo file
- [ ] I shipped 1 mini-project above
- [ ] Flip hub + notes + this file to `human-reviewed` when done. Date: …
- [ ] I can explain this track to a fresher with one snippet per subtopic: …
- Notes: …
