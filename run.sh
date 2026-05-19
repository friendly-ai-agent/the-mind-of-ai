#!/usr/bin/env bash
set -euo pipefail

BLOG_DIR="$(cd "$(dirname "$0")" && pwd)"
PORT=1313

if ! command -v hugo &>/dev/null; then
    echo "Hugo not found."
    if command -v brew &>/dev/null; then
        echo "Installing via Homebrew..."
        brew install hugo
    else
        echo "Install Hugo manually: https://gohugo.io/installation/"
        exit 1
    fi
fi

echo "Hugo $(hugo version | grep -o 'v[0-9][^ ]*')"
echo "Starting local server at http://localhost:${PORT}"
echo "Drafts visible. Ctrl+C to stop."
echo ""

cd "$BLOG_DIR"
hugo server \
    --buildDrafts \
    --buildFuture \
    --port "$PORT" \
    --bind 127.0.0.1 \
    --disableFastRender
