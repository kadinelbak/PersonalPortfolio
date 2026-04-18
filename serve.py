#!/usr/bin/env python3
"""
Simple HTTP server to preview the markdown portfolio on localhost:5000
This converts markdown to HTML on-the-fly for preview purposes.
"""

import os
import re
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse
import markdown
from markdown.extensions.toc import TocExtension

REPO_ROOT = Path(__file__).resolve().parent
DEFAULT_TEMPLATE_ROOT = REPO_ROOT / "engineering-template"
LEGACY_PREFIXES = ("medical", "engineering")

class MarkdownHTTPHandler(SimpleHTTPRequestHandler):
    def _render_liquid_relative_urls(self, content):
        # GitHub Pages resolves these Liquid tags at build time; local preview must do it explicitly.
        return re.sub(
            r"\{\{\s*['\"](?P<path>/[^'\"]*)['\"]\s*\|\s*relative_url\s*\}\}",
            lambda match: match.group("path"),
            content,
        )

    def _resolve_file_path(self, path):
        normalized_path = path if path in ("/", "/index.html") else path.rstrip("/")

        if normalized_path in ("", "/", "/index.html"):
            return DEFAULT_TEMPLATE_ROOT / "index.md"

        pretty_pages = {
            "/leadership": DEFAULT_TEMPLATE_ROOT / "leadership.md",
            "/projects": DEFAULT_TEMPLATE_ROOT / "projects.md",
            "/research": DEFAULT_TEMPLATE_ROOT / "research.md",
            "/engineering": DEFAULT_TEMPLATE_ROOT / "engineering.md",
            "/contact": DEFAULT_TEMPLATE_ROOT / "contact.md",
            "/cv": DEFAULT_TEMPLATE_ROOT / "cv.md",
        }

        if normalized_path in pretty_pages:
            return pretty_pages[normalized_path]

        if normalized_path.startswith("/projects/"):
            project_name = normalized_path.removeprefix("/projects/").strip("/")
            return DEFAULT_TEMPLATE_ROOT / "_projects" / f"{project_name}.md"

        if path.startswith("/assets/"):
            root_asset_path = REPO_ROOT / path.lstrip("/")
            if root_asset_path.exists():
                return root_asset_path

            template_asset_path = DEFAULT_TEMPLATE_ROOT / path.lstrip("/")
            if template_asset_path.exists():
                return template_asset_path

            return root_asset_path

        return DEFAULT_TEMPLATE_ROOT / path.lstrip("/")

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parsed.query

        for prefix in LEGACY_PREFIXES:
            legacy_prefix = f"/{prefix}"
            if path == legacy_prefix or path.startswith(f"{legacy_prefix}/"):
                stripped_path = path[len(legacy_prefix):] or "/"
                redirect_target = stripped_path
                if query:
                    redirect_target = f"{redirect_target}?{query}"
                self.send_response(302)
                self.send_header("Location", redirect_target)
                self.end_headers()
                return

        file_path = self._resolve_file_path(path)

        # Serve markdown as HTML
        if file_path.suffix == ".md":
            if file_path.exists() and file_path.is_file():
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Strip YAML frontmatter
                    if content.startswith("---"):
                        parts = content.split("---", 2)
                        if len(parts) >= 3:
                            content = parts[2].strip()

                    content = self._render_liquid_relative_urls(content)

                    # Convert markdown to HTML
                    md = markdown.Markdown(extensions=["extra", "codehilite", TocExtension()])
                    html_content = md.convert(content)

                    nav_links = {
                        "About": "/",
                        "Projects": "/#matrix",
                        "Contact": "/#contact",
                    }

                    css_href = "/assets/css/site.css"
                    nav_items_html = "\n                ".join(
                        f'<a href="{href}">{label}</a>' for label, href in nav_links.items()
                    )
                    brand_href = "/"
                    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <base href="/">
    <title>Portfolio Preview</title>
    <link rel="stylesheet" href="{css_href}">
</head>
<body>
    <header class="site-header">
        <div class="site-header__inner">
            <a href="{brand_href}" class="brand">Portfolio</a>
            <nav class="nav-links">
                {nav_items_html}
            </nav>
        </div>
    </header>
    <main class="page">
        <div class="page__eyebrow">Hybrid BME Portfolio</div>
        <article class="content-card">
            {html_content}
        </article>
    </main>
    <script>
        const currentPath = window.location.pathname;
        document.querySelectorAll('.nav-links a').forEach((link) => {{
            if (currentPath.endsWith(link.getAttribute('href').split('/').pop())) {{
                link.classList.add('active');
            }}
        }});
    </script>
    <script>
        (function () {{
            const filterGroups = document.querySelectorAll('[data-bento-filters]');
            if (!filterGroups.length) return;
            const cards = document.querySelectorAll('[data-bento-card]');
            filterGroups.forEach((group) => {{
                const buttons = group.querySelectorAll('button[data-filter]');
                const applyFilter = (filter) => {{
                    cards.forEach((card) => {{
                        const categories = (card.dataset.category || '').split(/\s+/).filter(Boolean);
                        const matches = filter === 'all' || categories.includes(filter);
                        card.hidden = !matches;
                    }});
                    buttons.forEach((button) => {{
                        const active = button.dataset.filter === filter;
                        button.classList.toggle('active', active);
                        button.setAttribute('aria-pressed', active ? 'true' : 'false');
                    }});
                }};
                buttons.forEach((button) => {{
                    button.addEventListener('click', () => applyFilter(button.dataset.filter));
                }});
                applyFilter('all');
            }});
        }})();
    </script>
    <script>
        (function () {{
            const reveals = document.querySelectorAll('.reveal');
            const observer = new IntersectionObserver((entries) => {{
                entries.forEach((entry) => {{
                    if (entry.isIntersecting) {{
                        entry.target.classList.add('is-visible');
                    }}
                }});
            }}, {{ threshold: 0.15 }});
            reveals.forEach((el) => observer.observe(el));
        }})();
    </script>
    <script>
        window.MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']]
            }},
            options: {{
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
            }}
        }};
    </script>
    <script id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</body>
</html>"""

                    self.send_response(200)
                    self.send_header("Content-type", "text/html; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(html.encode("utf-8"))
                except Exception as e:
                    self.send_error(500, str(e))
            else:
                self.send_error(404)
        else:
            # Serve other files (images, pdfs, etc.)
            if file_path.exists():
                self.directory = str(file_path.parent)
                self.path = f"/{file_path.name}"
            elif path.startswith("/assets/"):
                self.directory = str(REPO_ROOT)
                self.path = path
            else:
                self.directory = str(DEFAULT_TEMPLATE_ROOT)
                self.path = path
            super().do_GET()

if __name__ == "__main__":
    os.chdir(REPO_ROOT)

    print("=" * 60)
    print("Portfolio Preview Server")
    print("=" * 60)
    print("Starting server on http://localhost:5000")
    print("Portfolio: http://localhost:5000/")
    print("Legacy routes redirect to /")
    print("Press Ctrl+C to stop")
    print("=" * 60)

    server_address = ("", 5000)
    httpd = HTTPServer(server_address, MarkdownHTTPHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
