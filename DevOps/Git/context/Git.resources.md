---
topic: Git
domain: DevOps
status: researched
updated: 2026-10-02
related: []
tags: [git, github-cli, gitlab-cli, gh, glab, version-control]
track: Git
---

# Git — Resources

> The ONLY resources file for this whole track. You only need it to go BEYOND the listed subtopics. If the notes + mini-projects covered what you need, close this file.

## Connected reading path

| # | Type | Title | Status | Why this one (beginner payoff in 1 line) |
|---|---|---|---|---|
| 1 | docs | [What is Git? — Pro Git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git) | OPENED 2026-10-02 | Start here: the 3-area model (desk, frame, album) in 10 min |
| 2 | docs | [Recording Changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) | OPENED 2026-10-02 | `status`/`add`/`commit`/`ignore` lifecycle with examples |
| 3 | docs | [Viewing Commit History](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History) | OPENED 2026-10-02 | `log`/`show`/`shortlog` flags you use daily |
| 4 | docs | [Git Branching — Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) | UNVERIFIED — indexed Pro Git chapter, same series as opened pages | Pointer model: branches as sliding labels + HEAD visuals |
| 5 | docs | [git-reset Manual](https://git-scm.com/docs/git-reset) | OPENED 2026-10-02 | soft/mixed/hard semantics + when each is safe |
| 6 | docs | [git-rebase Manual](https://git-scm.com/docs/git-rebase) | OPENED 2026-10-02 | Replay model, interactive verbs, recovering cleanly |
| 7 | docs | [Git Internals — Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) | OPENED 2026-10-02 | blob/tree/commit/tag + `cat-file` plumbing in one page |
| 8 | docs | [GitHub CLI Manual — gh pr create](https://cli.github.com/manual/gh_pr_create) | OPENED 2026-10-02 | Core request flags: title/body/reviewers/base/head |
| 9 | docs | [GitLab CLI (glab)](https://docs.gitlab.com/cli/) | OPENED 2026-10-02 | Install, auth, pagination, full command surface |
| 10 | docs | [git-stash Manual](https://git-scm.com/docs/git-stash) | OPENED 2026-10-02 | push/apply/pop/`stash branch` + conflict handling |
| 11 | docs | [git-push Manual](https://git-scm.com/docs/git-push) | UNVERIFIED — indexed from git-scm reference, same series as opened pages | Upstream, refspecs, `--force-with-lease` |
| 12 | docs | [Rebasing — Pro Git](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) | UNVERIFIED — indexed Pro Git chapter | Merge-vs-rebase tradeoffs, perils of rebasing shared lines |

Status ∈ `OPENED <date>` (you read it) / `UNVERIFIED — <reason>`. Dead links fail the gate — fix or remove.

## Papers

No papers — for this track the Pro Git chapters + man pages are canonical (verified across all 8 former subtopic ledgers; manuals cite each other, blogs add no new mechanism).

## Source ledger (required)

- Searched (queries): git fundamentals working tree staging; git log/reset/revert/reflog/diff manuals; git branch/merge/rebase/cherry-pick; git tag/worktree/hooks/submodules/LFS/signing; github CLI gh manual; gitlab glab CLI
- Opened (≥5): 9 above (rows 1,2,3,5,6,7,8,9,10) + git-config/gitignore/git-branch/git-merge/git-bisect/git-tag/git-worktree/gh-api/glab-mr manuals across the former subtopics (16+ total) · Skipped with reason: StackOverflow anecdotes, opinionated merge-vs-rebase blogs, video walkthroughs (docs already canonical)
- Connectedness: Pro Git chapters cite the man pages and cross-link init → recording → history → branching; reset manual cross-links revert/restore; cli.github.com manuals cross-link pr↔issue↔api; GitLab CLI docs cite the MR user docs
- Beginner starter: row #1 above — gives a working mental model + snippet in <10 min
