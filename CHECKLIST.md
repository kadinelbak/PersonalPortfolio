# Portfolio Publishing Checklist

Use this before pushing a public update.

## Content

- [ ] Homepage clearly introduces Kadin El Bakkouri and the hybrid BME focus
- [ ] Project matrix links to the strongest detailed exhibits
- [ ] Each project page explains the problem, contribution, technical work, and outcome
- [ ] External links to GitHub, reports, Devpost, LinkedIn, and tools still work
- [ ] Contact information is current
- [ ] CV and resume files in `docs/assets/pdf/` are current

## Visuals

- [ ] Homepage and project-card images load from `docs/assets/img/`
- [ ] Images have useful alt text where they appear in Markdown or HTML
- [ ] Mobile layout is readable and no cards/text overlap
- [ ] Important figures are legible at normal screen widths

## Repository Hygiene

- [ ] Edit the live site in `docs/`
- [ ] Do not commit generated Python caches or one-off extraction folders
- [ ] Keep source/template experiments out of the published path unless they are intentionally maintained
- [ ] Run `git status --short` and confirm only intended files changed

## GitHub Pages

- [ ] GitHub Pages source is set to branch `main`, folder `/docs`
- [ ] Published site loads at `https://<username>.github.io/<repo-name>/`
- [ ] Navigation works from the homepage and from nested project pages
- [ ] CV and resume downloads work on the published site
