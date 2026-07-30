# Kadin El Bakkouri Portfolio

This repository contains the source for Kadin El Bakkouri's biomedical engineering portfolio, published with GitHub Pages from the `docs/` folder.

The portfolio focuses on:

- biomedical device design
- computational modeling and clinical data workflows
- research infrastructure
- leadership and assistive technology project delivery

## Source of Truth

Edit the live site in `docs/`.

Key files:

- `docs/index.md` - homepage and project matrix
- `docs/projects.md` - grouped project overview
- `docs/research.md` - research highlights
- `docs/_projects/` - detailed project pages
- `docs/assets/css/site.css` - site styling
- `docs/assets/img/` - images used by the published site
- `docs/assets/pdf/` - downloadable CV and resume files

## Local Preview

The included preview server renders the Markdown site locally:

```powershell
python serve.py
```

Then open:

```text
http://localhost:5000/PersonalPortfolio/
```

## Publishing

In GitHub Pages settings, publish from:

- branch: `main`
- folder: `/docs`

After changes, click through the site and confirm images, project pages, CV, and resume downloads load correctly.
