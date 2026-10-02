---
topic: Making Code Changes
domain: AI-Engineering
status: researched
updated: 2026-10-02
related: ["[[../Claude-Code]]"]
tags: [claude-code, prompts, at-mentions, multimodal, flask, git-commits]
---

# Making Code Changes

> Three moves: edit a file, make a new page, paste a picture → get code. Pre-write prompts, point with @, commit each win.

## 1. Intuition

Good prompts are specific orders + limits. **@ mention** (typing @ plus file path to aim at exact file) stops guessing. Work is a loop: prompt → output → check → fix prompt.

```bash
claude
/rename landing-page-improvements
# expected output: named session ready for 5 small commits
```

> You can now: write a prompt that hits the right file first try.

## 2. How it works

### Prompt discipline

- **Write prompts offline** — draft → polish → save → paste; kills typos and missing limits.

  ```text
  Draft -> polish -> save prompts.txt -> paste
  # expected output: complete order, no live-typing errors
  ```

- **Aim with @ + limits** — `@file` pins the target; "touch nothing else" prevents sprawl; commit each milestone.

  ```bash
  git diff --stat
  # expected output: 1 file changed (proves targeting worked)
  ```

### Three moves

- **Edit + new pages** — footer links with `#` placeholders; `/terms` route + template + link swap, then "match the theme".

  ```python
  @app.route('/terms')
  def terms(): return render_template('terms.html')
  # expected output: /terms renders new page
  ```

- **Image to code** — paste a mockup with Ctrl+V, scope to the hero only; hours of hand translation become minutes.

  ```text
  Paste image + "Modify only hero in @templates/landing.html..."
  # expected output: hero matches mockup, rest untouched
  ```

- **Modal without bugs** — opens on click, closes on X + outside-click, stops video, vanilla JS only.

  ```javascript
  modal.close(); video.pause();
  // expected output: no background audio after close
  ```

### Iterate

- **Fix forward** — wrong CSS file → "merge them"; off-theme page → follow-up; AI work is iterative by nature.

  ```text
  Follow-up: "Merge these two CSS files, keep landing.css"
  # expected output: one clean CSS file
  ```

> You can now: ship a small UI task with @, limits, check, commit.

## 3. Visual

```mermaid
flowchart LR
  A[Pre-write + polish prompt] --> B[@ file aim]
  B --> C[Edit, new route, image to code, modal]
  C --> D[Browser check + git commit]
  D --> E[Follow-up if off]
```

Pictured: 4-phase web workflow (setup → links/routes → image/modal → commits), Spendly hero "Track every rupee" mockup with ₹18,240 + 34 tx cards.

## 4. Use cases

| Use case | When to use (concrete example) | When NOT to / edge case |
|---|---|---|
| Footer tweak | `@templates/base.html` + "plain links, href #, touch nothing else" | Vague "improve footer" — restyles whole page; fix: add do-not-touch line |
| New legal page | Route + template + link swap in one prompt | Forget theme — page looks alien; fix: follow-up "match website theme" |
| Designer mockup | Paste hero PNG + "hero only, exact match" | Paste without file scope — rewrites page; fix: name both HTML + CSS |
| Edge case: video keeps playing | Modal closed but audio runs | Missing stop-on-close; fix: require pause + outside-click close upfront |

## 5. AI-era leverage

- **Prompt polisher:** turn rough into exact.

  ```text
  Ask AI: "Polish this into Claude Code prompt with @ files, must-do, must-NOT-do, vanilla JS: <rough>."
  ```

- **Reviewer:** catch scope creep before commit.

  ```text
  Ask AI: "Here is git diff --stat. Did AI touch anything outside footer/terms? List extras in 3 lines."
  ```

## 6. Limits & tradeoffs

- First try rarely perfect — breaks as: expecting pixel-perfect — instead do: budget one follow-up per task.

- Placeholder URLs/data ship to prod if forgotten — breaks as: demo YouTube live — instead do: mark TODO + swap before merge.

- Big prompts burn context — breaks as: pasting whole files — instead do: @ point, let Claude read.

- Open aspects: context saving in [[05-Context-Window-Management|05 Context]]; spec-first in [[07-Spec-Driven-Plan-Mode|07 SDD + Plan]].

## 7. Related

- [[../Claude-Code|Claude Code hub]] · [[../context/Claude-Code.resources]] · [[../context/Claude-Code.build]]
