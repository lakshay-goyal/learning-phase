---
topic: Git
domain: DevOps
status: researched
updated: 2026-10-02
related: []
tags: [git, github-cli, gitlab-cli, gh, glab, version-control]
track: Git
---

# Git

> Full terminal track: save work, branch safely, combine + undo anything, and drive GitHub/GitLab from the shell. Finish it and you can ship a feature end-to-end: branch → save → review → merge → release.

```mermaid
flowchart LR
  A[01 Fundamentals] --> B[02 Commits & History]
  B --> C[03 Branches & Remotes]
  C --> D[04 Merge & Rebase]
  D --> E[05 Undo & Recovery]
  E --> F[06 Tags Worktrees Internals]
  F --> G[07 GitHub CLI]
  G --> H[08 GitLab CLI & Automation]
  style A fill:#ecfdf5,stroke:#059669
  style G fill:#eff6ff,stroke:#2563eb
  style H fill:#fff7ed,stroke:#ea580c
```

## How to use this track

1. Go in order `01 → 08`, 15–30 min per subtopic. Each one assumes the previous.
2. Each subtopic is main note (learn with snippets) → `resources` (go deeper) → `build` (prove it with 1 task).
3. Rule of the track: **Git owns history, hosting owns collaboration, CLI drives hosting.** After each subtopic you can do one new real thing (see the table).

## Subtopics

| # | Note | Covers (plain words + payoff) |
|---|---|---|
| 01 | [[notes/01-Fundamentals|Fundamentals]] | Save + inspect work — you can start/join a project and make clean saves |
| 02 | [[notes/02-Commits-History|Commits & History]] | Read + fix history — you can compare saves and undo the right way |
| 03 | [[notes/03-Branches-Remotes|Branches & Remotes]] | Parallel lines + syncing — you can branch and sync without losing work |
| 04 | [[notes/04-Merge-Rebase|Merge & Rebase]] | Combining work — you can land features and resolve conflicts |
| 05 | [[notes/05-Undo-Recovery|Undo & Recovery]] | Mistakes + rescue — you can recover anything, park work, find culprits |
| 06 | [[notes/06-Tags-Worktrees-Internals|Tags, Worktrees & Internals]] | Releases + parallel desks + how Git stores it all — you can version and multitask |
| 07 | [[notes/07-GitHub-CLI|GitHub CLI]] | `gh` reviews/tasks/releases/scripting — you can run GitHub from the terminal |
| 08 | [[notes/08-GitLab-CLI-Automation|GitLab CLI & Automation]] | `glab` + automating both sites — you can work both platforms with one map |

## Related

- [[DevOps|DevOps MOC]] · [[context/Git.resources]] · [[context/Git.build]]
