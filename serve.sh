#!/bin/sh
# Serve the built site at http://localhost:8000
# Run from repo root: ./serve.sh
cd "$(dirname "$0")/docs" && python3 -m http.server 8000
