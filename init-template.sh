#!/bin/bash

# init-template.sh
# Usage: bash init-template.sh
DOCS_DIR="docs"
TEMPLATE_DIR="engineering-template"

if [ ! -d "$TEMPLATE_DIR" ]; then
    echo "Error: $TEMPLATE_DIR/ folder not found."
    exit 1
fi

# Remove old docs folder if it exists
if [ -d "$DOCS_DIR" ]; then
    rm -rf "$DOCS_DIR"
fi

# Copy template into docs
cp -r "$TEMPLATE_DIR" "$DOCS_DIR"

# Create a minimal _config.yml
cat > "$DOCS_DIR/_config.yml" << 'EOF'
# GitHub Pages Configuration
theme: jekyll-theme-minimal
title: Portfolio
description: My portfolio website

# Optional: add nav if Jekyll supports it
# navigation:
#   - title: Home
#     url: /index.html
EOF

echo "✓ Copied $TEMPLATE_DIR to $DOCS_DIR/"
echo "✓ Created $DOCS_DIR/_config.yml"
echo ""
echo "Next steps:"
echo "  1. Update content in $DOCS_DIR/"
echo "  2. git add -A && git commit -m 'Initialize portfolio'"
echo "  3. git push"
echo "  4. Enable GitHub Pages from repo Settings (branch: main, folder: docs/)"
