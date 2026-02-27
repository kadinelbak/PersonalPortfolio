#!/usr/bin/env python3
"""
Simple HTTP server to preview the markdown portfolio on localhost:5000
This converts markdown to HTML on-the-fly for preview purposes.
"""

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse
import markdown
from markdown.extensions.toc import TocExtension

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = {
    "medical": REPO_ROOT / "medical-template",
    "engineering": REPO_ROOT / "engineering-template",
}

class MarkdownHTTPHandler(SimpleHTTPRequestHandler):
    def _resolve_template(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path == "/":
            return "medical", "/medical/"
        for key in ("medical", "engineering"):
            prefix = f"/{key}/"
            if path.startswith(prefix):
                return key, prefix
        return "medical", "/medical/"

    def do_GET(self):
        template_key, base_prefix = self._resolve_template()
        template_root = TEMPLATES[template_key]
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/":
            self.send_response(302)
            self.send_header("Location", "/medical/")
            self.end_headers()
            return

        if path == base_prefix:
            path = f"{base_prefix}index.md"

        if path.startswith("/assets/"):
            file_path = REPO_ROOT / path.lstrip("/")
        elif path.startswith(base_prefix):
            relative_path = path[len(base_prefix):]
            file_path = template_root / relative_path
        else:
            relative_path = path.lstrip("/")
            file_path = template_root / relative_path

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

                    # Convert markdown to HTML
                    md = markdown.Markdown(extensions=["extra", "codehilite", TocExtension()])
                    html_content = md.convert(content)

                    other_key = "engineering" if template_key == "medical" else "medical"
                    other_label = "Engineering" if other_key == "engineering" else "Medical"
                    other_href = f"/{other_key}/"

                    nav_links = {
                        "Gallery": f"{base_prefix}index.md#gallery",
                        "Exhibits": f"{base_prefix}index.md#exhibits",
                        "Research": f"{base_prefix}index.md#research",
                        "Leadership": f"{base_prefix}index.md#leadership",
                        "Contact": f"{base_prefix}index.md#contact",
                    }

                    if template_key == "engineering":
                        nav_links = {
                            "Gallery": f"{base_prefix}index.md#gallery",
                            "Exhibits": f"{base_prefix}index.md#exhibits",
                            "Research": f"{base_prefix}index.md#research",
                            "Technical": f"{base_prefix}index.md#technical",
                            "Leadership": f"{base_prefix}index.md#leadership",
                            "Contact": f"{base_prefix}index.md#contact",
                        }

                    css_href = f"{base_prefix}assets/css/site.css"
                    nav_items_html = "\n                ".join(
                        f'<a href="{href}">{label}</a>' for label, href in nav_links.items()
                    )
                    view_toggle_html = """
            <div class="view-toggle" data-view-toggle>
                <button type="button" data-view="wall">Gallery Wall</button>
                <button type="button" data-view="immersive">Immersive</button>
                <button type="button" data-view="grid">Grid Plan</button>
            </div>
                    """
                    brand_href = f"{base_prefix}index.md"
                    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <base href="{base_prefix}">
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
            {view_toggle_html}
        </div>
    </header>
    <main class="page">
        <div class="page__eyebrow">Museum Exhibit — {template_key.title()} Portfolio</div>
        <article class="content-card">
            {html_content}
        </article>
    </main>
    <a class="template-switch" href="{other_href}">Switch to {other_label}</a>
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
            const root = document.body;
            const buttons = document.querySelectorAll('[data-view-toggle] button');
            const storageKey = 'portfolio-view';
            const applyView = (view) => {{
                root.classList.remove('view-wall', 'view-immersive', 'view-grid');
                root.classList.add(`view-${{view}}`);
                buttons.forEach((btn) => btn.classList.toggle('active', btn.dataset.view === view));
            }};
            const saved = localStorage.getItem(storageKey) || 'wall';
            applyView(saved);
            buttons.forEach((btn) => {{
                btn.addEventListener('click', () => {{
                    localStorage.setItem(storageKey, btn.dataset.view);
                    applyView(btn.dataset.view);
                }});
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

            const mapLinks = document.querySelectorAll('.gallery-map a');
            const sections = Array.from(mapLinks)
                .map((link) => document.querySelector(link.getAttribute('href')))
                .filter(Boolean);
            const mapObserver = new IntersectionObserver((entries) => {{
                entries.forEach((entry) => {{
                    if (entry.isIntersecting) {{
                        mapLinks.forEach((link) => link.classList.remove('active'));
                        const active = document.querySelector(`.gallery-map a[href="#${{entry.target.id}}"]`);
                        if (active) active.classList.add('active');
                    }}
                }});
            }}, {{ threshold: 0.35 }});
            sections.forEach((section) => mapObserver.observe(section));
        }})();
    </script>
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
            if path.startswith("/assets/"):
                self.directory = str(REPO_ROOT)
                self.path = path
            else:
                self.directory = str(template_root)
                self.path = "/" + relative_path
            super().do_GET()

if __name__ == "__main__":
    os.chdir(REPO_ROOT)

    print("=" * 60)
    print("Portfolio Preview Server")
    print("=" * 60)
    print("Starting server on http://localhost:5000")
    print("Medical: http://localhost:5000/medical/")
    print("Engineering: http://localhost:5000/engineering/")
    print("Press Ctrl+C to stop")
    print("=" * 60)

    server_address = ("", 5000)
    httpd = HTTPServer(server_address, MarkdownHTTPHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
