# Publishing Checklist

## Before Publishing (for both templates)

### 1. Folder & File Cleanup

- [ ] Delete the template you don't want (or use `init-template` script)
- [ ] Rename the template folder to root (copy contents up to `index.md`, `_projects/`, `assets/`) or move into `docs/`
- [ ] Verify folder structure is clean (no extra template folders in final site)

### 2. GitHub Account Setup

- [ ] Confirm GitHub is linked on `contact.md`
- [ ] (Medical): Limit to 1–2 repos visible (under "Technical appendix"); hide others
- [ ] (Engineering): Ensure prominent repos have clear READMEs and architecture diagrams

### 3. Content Review

- [ ] Replace placeholder text in all `.md` files with your work summaries
- [ ] Replace placeholder images in `assets/img/`
- [ ] Replace placeholder `assets/pdf/CV.pdf` with your CV
- [ ] Verify all links are correct and relative paths work
- [ ] Read through the site and check for typos

### 4. Curation (Medical)

- [ ] Confirm each project answers: problem, question, insight, connection to medicine
- [ ] No volunteer hours, clinical logs, or raw notebooks visible
- [ ] Leadership & Service highlights ethics, continuity, and impact (not volunteer hours)

### 5. Curation (Engineering)

- [ ] Confirm each project has a clear problem definition and constraints
- [ ] Benchmarks and metrics are presented responsibly
- [ ] Architecture diagrams are clear and professional
- [ ] GitHub repos link is working

### 6. Enable GitHub Pages

- [ ] Push to your repo on GitHub
- [ ] Go to **Settings** > **Pages**
- [ ] Choose **Branch**: `main` and **Folder**: `docs/` (if files are in `docs/`) or just `main` (if files are at root)
- [ ] Wait 1–2 minutes for the site to build
- [ ] Verify the site is live at `https://<username>.github.io/<repo-name>`

### 7. Test

- [ ] Click through all links
- [ ] Verify images and PDFs load
- [ ] Test on mobile (resize browser window)

---

## Quick Start Commands (Optional)

If using the `init-template` script to copy a template into `docs/`:

### Windows PowerShell

```powershell
.\init-template.ps1 -template medical
# or
.\init-template.ps1 -template engineering
```

### macOS / Linux

```bash
bash init-template.sh medical
# or
bash init-template.sh engineering
```

This will copy the template files into `docs/`, create a minimal `_config.yml`, and you can then commit and enable Pages.
