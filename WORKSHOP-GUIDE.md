# Workshop Guide: Portfolio Website Templates

Welcome! This repository contains two GitHub Pages portfolio templates designed for students in different disciplines. Use this guide to set up and customize your portfolio.

---

## What's in the Box

| Item | Purpose |
|------|---------|
| `medical-template/` | Pre-built site structure for medical students, research-focused |
| `engineering-template/` | Pre-built site structure for engineering students, deployment-focused |
| `init-template.sh` or `.ps1` | Script to copy your chosen template into `docs/` folder |
| `CHECKLIST.md` | Step-by-step publishing checklist |
| `TEMPLATES.md` | Comparison of curation rules for each template |

---

## Quick Start

### Option 1: Manual (Recommended for Learning)

1. **Fork or clone this repo** to your GitHub account.
2. **Inspect both templates** in their folders to see the structure:
   - Medical: problem → question → insight → medicine connection
   - Engineering: problem → constraints → design → deployment
3. **Delete the template you don't want**:
   ```bash
   rm -rf engineering-template
   # Keep only medical-template
   ```
4. **Copy the remaining template to your site root or `docs/` folder**:
   ```bash
   cp -r medical-template/* .
   # or:
   mkdir docs && cp -r medical-template/* docs/
   ```
5. **Edit the pages** with your own content (replace placeholders).
6. **Commit and push** to GitHub.
7. **Enable GitHub Pages** in repo Settings (use `docs/` folder or root, depending on your choice).

### Option 2: Scripted (Fastest)

**Windows (PowerShell):**
```powershell
.\init-template.ps1 -template medical
```

**macOS / Linux (Bash):**
```bash
bash init-template.sh medical
```

This copies the template into `docs/`, creates `_config.yml`, and you're ready to edit.

---

## Key Rules by Template

### Medical Student Portfolio

**Goal:** "I use quantitative and design tools to better understand biological systems and translate insights into real-world health and care contexts."

**Must-have sections:**
- 4–5 curated projects (disease modeling, device, assistive tech, health ML)
- Leadership & Service (emphasize ethics, continuity, impact)
- CV and contact

**Rules:**
- Link GitHub **minimally** (one link per project under "Technical appendix")
- NO badges, language stats, or repo lists
- Emphasize the clinical problem and insight, not the code
- Hide implementation details

**Example project flow:**
1. Clinical Motivation → Why does this matter?
2. Question → What did you ask?
3. Approach (high-level)
4. Key Results → 2–3 figures
5. Connection to Medicine → Explicit, not implied
6. Artifacts → One GitHub repo link (optional)

### Engineering Student Portfolio

**Goal:** "I design and build systems that move from problem definition to real-world deployment under technical and human constraints."

**Must-have sections:**
- 3–6 projects (systems, data/ML, devices, infrastructure)
- Research (publications, posters)
- Technical Depth page (engineering details visible here)
- CV and contact

**Rules:**
- Link GitHub **prominently** (multiple repos encouraged)
- Architecture diagrams welcome
- Benchmarks and metrics are visible
- Show technical depth and tradeoffs
- Explain constraints and deployment choices

**Example project flow:**
1. Problem Definition
2. Constraints
3. System Design (with diagram)
4. Implementation
5. Results & Metrics
6. Tradeoffs
7. GitHub link

---

## Workflow for the Workshop

1. **Choose your template** (medical or engineering).
2. **Copy or run init script** to get files in place.
3. **Replace placeholder content** in all `.md` files with your work summaries.
4. **Add real assets**: figures, diagrams, and your CV (replace placeholders in `assets/`).
5. **Follow CHECKLIST.md** to clean up and publish.
6. **Test on GitHub Pages** — you now have a live portfolio!

---

## Common Edits

### Change the identity statement (home page)

Edit `index.md` (first paragraph under the `#` heading). This is the thesis of your portfolio—keep it concise.

### Add or remove projects

Edit `projects.md` to update the project list. Then add/remove files in `_projects/`.

### Update GitHub links

On each project page, add a link like:
```markdown
[Technical Appendix (GitHub)](https://github.com/yourname/your-repo)
```

### Replace images

Place figures in `assets/img/` and reference them:
```markdown
![Figure caption](../assets/img/figure.png)
```

---

## Publishing

Once you're ready:

1. **Commit changes**: `git add -A && git commit -m "Portfolio content"`
2. **Push to GitHub**: `git push`
3. **Enable Pages** in repo Settings:
   - Branch: `main`
   - Folder: `docs/` (if files are in `docs/`) or root
4. **Wait 1–2 minutes** for the site to build.
5. **Visit** `https://<yourname>.github.io/<repo-name>` to see your live portfolio!

---

## Decision Heuristic

Does your portfolio pass this test?

> "Can a reviewer say, 'I understand what this person cares about and why it matters'?"

If yes, you nailed it. If not, edit for clarity and remove projects that don't reinforce your narrative.

---

## Questions?

Refer to:
- `TEMPLATES.md` for detailed curation rules
- `CHECKLIST.md` for step-by-step publishing
- Example project pages in `_projects/` for structure inspiration

Good luck! 🎓
