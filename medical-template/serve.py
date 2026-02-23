#!/usr/bin/env python3
"""
Simple HTTP server to preview the markdown portfolio on localhost:5000
This converts markdown to HTML on-the-fly for preview purposes.
"""

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import markdown
from markdown.extensions.toc import TocExtension

class MarkdownHTTPHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Default to index.md for root path
        if self.path == '/':
            self.path = '/index.md'
        
        # Serve markdown as HTML
        if self.path.endswith('.md'):
            file_path = Path(self.directory) / self.path.lstrip('/')
            
            if file_path.exists() and file_path.is_file():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Strip YAML frontmatter
                    if content.startswith('---'):
                        parts = content.split('---', 2)
                        if len(parts) >= 3:
                            content = parts[2].strip()
                    
                    # Convert markdown to HTML
                    md = markdown.Markdown(extensions=['extra', 'codehilite', TocExtension()])
                    html_content = md.convert(content)
                    
                    # Wrap in basic HTML template
                    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Portfolio Preview</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #fafbfc;
        }}
        nav {{
            background: #fff;
            border-bottom: 1px solid #eaecef;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}
        .nav-container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            align-items: center;
            height: 60px;
        }}
        .nav-brand {{
            font-weight: 600;
            font-size: 16px;
            margin-right: 40px;
            color: #333;
            text-decoration: none;
        }}
        .nav-links {{
            display: flex;
            gap: 30px;
            flex: 1;
        }}
        .nav-links a {{
            color: #666;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            transition: color 0.2s;
        }}
        .nav-links a:hover {{
            color: #0366d6;
        }}
        .nav-links a.active {{
            color: #0366d6;
            border-bottom: 2px solid #0366d6;
            padding-bottom: 2px;
        }}
        .content {{
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        a {{
            color: #0366d6;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        h1, h2, h3 {{
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }}
        h1 {{
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
            margin-top: 0;
        }}
        h2 {{
            margin-top: 32px;
        }}
        code {{
            background: #f6f8fa;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            border-left: 3px solid #0366d6;
        }}
        pre code {{
            background: none;
            padding: 0;
            border-radius: 0;
        }}
        .breadcrumb {{
            font-size: 13px;
            color: #666;
            margin-bottom: 20px;
        }}
        .breadcrumb a {{
            color: #0366d6;
        }}
        ul, ol {{
            margin: 16px 0;
            padding-left: 24px;
        }}
        li {{
            margin: 8px 0;
        }}
        blockquote {{
            border-left: 4px solid #eaecef;
            padding-left: 16px;
            margin: 16px 0;
            color: #666;
        }}
    </style>
</head>
<body>
    <nav>
        <div class="nav-container">
            <a href="/" class="nav-brand">Portfolio</a>
            <div class="nav-links">
                <a href="/">About</a>
                <a href="/projects.md">Projects</a>
                <a href="/leadership.md">Leadership</a>
                <a href="/cv.md">CV</a>
                <a href="/contact.md">Contact</a>
            </div>
        </div>
    </nav>
    <div class="content">
        {html_content}
    </div>
</body>
</html>"""
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(html.encode('utf-8'))
                except Exception as e:
                    self.send_error(500, str(e))
            else:
                self.send_error(404)
        else:
            # Serve other files normally
            super().do_GET()

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    
    print("=" * 60)
    print("Portfolio Preview Server")
    print("=" * 60)
    print("Starting server on http://localhost:5000")
    print("Press Ctrl+C to stop")
    print("=" * 60)
    
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, MarkdownHTTPHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
