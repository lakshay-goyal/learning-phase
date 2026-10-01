---
topic: Git
domain: DevOps
status: researched
updated: 2026-10-02
related: []
tags: [git, github-cli, gitlab-cli, gh, glab, version-control]
track: Git
---

# Git — Build

> The ONLY build file for this whole track. Mini-projects that sharpen the ENTIRE topic — not homework, not one-subtopic drills. Pick one, ship it, prove you own the track.

## Production codebases to study (1–3, pinned — required)

| Repo | Signals (stars / users / last push / license) | Commit | Study guide (real file path, end-to-end trace) |
|---|---|---|---|
| [git/git](https://github.com/git/git) | 63.5k★, 28.5k forks, push 2026-10-01, GPLv2 | `a0189536` | Read `Documentation/gittutorial.adoc` → `builtin/log.c` → `builtin/merge.c` → `builtin/stash.c`; trace one save → branch → merge → undo inside the clone itself |
| [cli/cli](https://github.com/cli/cli) | 46.5k★, 9.1k forks, push 2026-10-01, MIT | `fc4b137c` | Read `pkg/cmd/pr/create/create.go` → `pkg/cmd/pr/merge/merge.go` → `pkg/cmd/api/api.go`; run `gh pr list --json number,title --jq length` |
| [gitlab-org/cli](https://gitlab.com/gitlab-org/cli) | push 2026-10-01, MIT, used by GitLab self-managed fleets | `5a38b396` | Read `commands/mr/mr.go` → `commands/mr/create/mr_create.go` → `commands/api/api.go`; run `glab mr list --help` + `glab api --help` |

Opened git/git + cli/cli listings 2026-10-02 (tests in `t/`, CI via `.github/`). glab inspected via API 2026-10-02 (GitLab canonical host, not cloned — marked honestly).

## Mini-projects (do 1 — each covers the whole track)

_Beginner rule: each project = what you ship in 1 line + exact steps with commands + what done looks like + 1 common mistake + fix + who benefits. Each touches ≥3 subtopics._

1. **Mini-project 1 (1–2 days):** Ship a versioned feature on a scratch repo — init → branch → saves → conflicted merge → tag (touches 01, 03, 04, 06).
   ```bash
   mkdir ship && cd ship && git init -b main && git commit -q --allow-empty -m init
   git switch -c feature && echo v1 > app.txt && git add -A && git commit -m "add app"
   git switch main && echo v2 > app.txt && git add -A && git commit -m "main moves too"
   git merge feature   # conflicts: fix app.txt, delete markers, git add, git commit
   git diff --check && git tag -a v0.1.0 -m "first" && git log --graph --oneline -5
   # done looks like: clean `diff --check`, visible merge knot, tag listed by `git tag`
   # if you see leftover `<<<<<` markers: you committed the conflict — fix: edit, `git add`, `git commit --amend`
   ```
   Who benefits: anyone who must land features without fear (juniors, freelancers, agent supervisors).
2. **Mini-project 2 (2–3 days):** Break it, rescue it, prove it — one drill per undo layer + a bisect hunt (touches 02, 05).
   ```bash
   echo bad >> app.txt && git restore app.txt                    # desk layer
   git commit -qam wip && git reset --soft HEAD~1                # private-save layer
   git commit -qam wip && git revert HEAD --no-edit && git log --oneline -2  # shared-save layer
   git stash push -m "safety" && git stash pop                   # park layer
   git reflog -5 && git bisect start && git bisect bad HEAD && git bisect good v0.1.0 && git bisect reset
   # done looks like: each layer undone the right way, reflog lists every move, bisect exits cleanly
   # if `reset --hard` scares you here: good — practice it ONLY on this throwaway repo
   ```
   Who benefits: on-call devs + anyone supervising AI agents (recovery speed is the skill).
3. **Mini-project 3 (3–5 days):** Terminal-only collaboration on one forge — repo → request → review loop → merge → release (touches 03, 07 or 08).
   ```bash
   gh repo create demo --private --source=. --push   # or: glab repo create demo
   git switch -c feat && echo x > f.txt && git add -A && git commit -m "feat" && git push -u origin feat
   gh pr create --title "Feat" --body "why + tests" && gh pr checks   # or: glab mr create --fill
   gh pr checkout 1 && gh pr diff && gh pr review --approve       # reviewer loop
   gh pr merge --squash --delete-branch && gh release create v0.1.0 --generate-notes
   # done looks like: merged request + release page with generated notes exists on the forge
   # if commands 403: `gh auth status` → `gh auth refresh` (missing token scope)
   ```
   Who benefits: teams drowning in review queues; developers who want the browser only for giant diffs.

## Ideas, use cases & missed aspects

- AI-era scenario: agent farm on worktrees (`worktree add` per task) + `pre-commit` guardrails + signed tags for agent-assisted releases — parallel agents, human merges.
  ```bash
  git worktree add ../agent-a feature-a && git worktree list
  ```
- Real use case: client onboarding kit — config doc + `.gitignore` templates + daily 5-command checklist + undo runbook + terminal review loop. Who pays: teams with juniors + billing code touched by agents.
- Edge case track-wide: committed a secret (`.env`) and pushed — every clone holds a copy forever. Fix order matters: rotate the secret FIRST, then `git rm --cached .env` + `.gitignore` + rewrite/push. Rewriting without rotating is theater.
  ```bash
  git rm --cached .env && echo ".env" >> .gitignore && git commit -m "stop tracking secrets"
  ```

## Human feedback (only human edits)

- [ ] I read the track notes + opened 1 resource + 1 repo file
- [ ] I shipped 1 mini-project above
- [ ] Flip hub + notes + this file to `human-reviewed` when done. Date: …
- [ ] I can explain this track to a fresher with one snippet per subtopic: …
- Notes: …
