#!/usr/bin/env bash
# Build and serve the site locally. Use with Chrome DevTools device mode for mobile preview.
set -e
cd "$(dirname "$0")"
python3 build.py
echo ""
echo "Serving at http://127.0.0.1:8000"
echo "Mobile preview: Chrome → F12 (DevTools) → Ctrl+Shift+M (device toolbar) → pick a device or set width."
echo ""
python3 -m http.server 8000 --directory docs
