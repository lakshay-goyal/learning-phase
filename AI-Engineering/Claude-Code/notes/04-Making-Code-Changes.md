---
topic: Making Code Changes
domain: AI-Engineering
status: researched
updated: 2026-10-02
related: ["[[../Claude-Code]]", "[[03-Slash-Commands-Sessions|Slash Commands]]"]
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

- **Plan prompts offline** — draft → polish in ChatGPT/Claude → save in file → paste into Claude Code. Kills typos + missing limits.
  ```text
  Draft -> polish -> save prompts.txt -> paste
  # expected output: complete order, no live-typing errors
  ```
- **Task 1 edit footer** — add Terms + Privacy to `@templates/base.html`, plain links, `href="#"`, touch nothing else.
  ```text
  Add two links to footer in @templates/base.html, href="#", do not modify anything else.
  # expected output: 2 links added, diff shows only footer
  ```
- **@ targeting** — `@app.py` (backend), `@templates/landing.html`, `@static/css/landing.css`. Without @ = guess + wrong file. With @ = exact + safe.
  ```bash
  git diff --stat
  # expected output: 1 file changed (proves targeting worked)
  ```
- **Commit each milestone** — 5 commits here: footer links, /terms page, /privacy page, hero redesign, youtube modal.
  ```bash
  git add . && git commit -m "landing: add terms and privacy links to footer"
  # expected output: commit created with that message
  ```
- **Task 2 new pages** — `/terms` route in app.py + `terms.html` (Acceptance, Use, Data, Liability, Changes) + fix footer `#` → `/terms`. Then follow-up: match theme.
  ```python
  @app.route('/terms')
  def terms(): return render_template('terms.html')
  # expected output: /terms renders new page
  ```
- **Task 3 picture→code** — copy image → Ctrl+V in terminal → image appears → prompt "match hero only in landing.html + landing.css, touch nothing else". Hours → minutes.
  ```text
  Paste image + "Modify only hero in @templates/landing.html..."
  # expected output: hero matches mockup, rest untouched
  ```
- **Task 4 modal** — "See how it works" opens overlay with YouTube iframe (placeholder URL ok), close on X + outside click, stop video on close, vanilla JS (plain JS, no library) only.
  ```javascript
  modal.close(); video.pause();
  // expected output: no background audio after close
  ```
- **Mistakes table** — wrong CSS name → merged files via follow-up; git typed in chat → Claude handled; bad theme → "match theme" follow-up.
  ```text
  Follow-up: "Merge these two CSS files, keep landing.css"
  # expected output: one clean CSS file
  ```

> You can now: ship a small UI task with @, limits, check, commit.

## 3. Visual

```mermaid
flowchart LR
  A[Pre-write + polish prompt] --> B[@ file aim]
  B --> C[Edit + new route + image->code + modal]
  C --> D[Browser check + git commit]
  D --> E[Follow-up if off]
```

PDF art: 4-phase web workflow (setup → links/routes → image/modal → commits), Spendly hero "Track every rupee" mockup with ₹18,240 + 34 tx cards.

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

- [[../Claude-Code|Claude Code hub]] · [[03-Slash-Commands-Sessions|03 Slash]] · [[05-Context-Window-Management|05 Context]] · [[../context/Claude-Code.resources]] · [[../context/Claude-Code.build]]
