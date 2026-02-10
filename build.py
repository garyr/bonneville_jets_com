#!/usr/bin/env python3
"""
Build Bonneville Jets static site: Markdown + template -> HTML.
Output goes to docs/ for GitHub Pages. Run from repo root.
"""
import re
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "content"
TEMPLATE_DIR = ROOT / "templates"
ASSETS_DIR = ROOT / "assets"
OUT_DIR = ROOT / "docs"

PAGES = [
    ("index.md", "index.html"),
    ("when-and-where.md", "when-and-where.html"),
    ("faq.md", "faq.html"),
    ("media.md", "media.html"),
    ("contact.md", "contact.html"),
]


def parse_frontmatter(text):
    """Extract optional YAML frontmatter and body. Returns (dict, body)."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return {}, text
    fm, body = match.groups()
    data = {}
    for line in fm.strip().split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip().lower()] = v.strip()
    return data, body.strip()


def render_md(md_text):
    """Convert Markdown to HTML. Headers, bold, links, paragraphs; raw HTML passed through."""
    out = []
    lines = md_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        # Consecutive lines starting with < (or blank between them) -> raw HTML block
        if line.strip().startswith("<"):
            raw = []
            while i < len(lines):
                s = lines[i].strip()
                if s and not s.startswith("<"):
                    break
                raw.append(lines[i])
                i += 1
            out.append("\n".join(raw))
            continue
        if line.strip() == "":
            i += 1
            continue
        m = re.match(r"^(#{1,3})\s+(.+)$", line)
        if m:
            n = len(m.group(1))
            out.append(f"<h{n}>{inline_md(m.group(2))}</h{n}>")
        else:
            out.append(f"<p>{inline_md(line)}</p>")
        i += 1
    return "\n".join(out)


def inline_md(s):
    """Process inline markdown: **bold**, [text](url)."""
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def load_template():
    path = TEMPLATE_DIR / "base.html"
    return path.read_text(encoding="utf-8")


def build_page(template, md_path, out_path):
    full_md = (CONTENT_DIR / md_path).read_text(encoding="utf-8")
    meta, body = parse_frontmatter(full_md)
    title = meta.get("title", "Page")
    description = meta.get("description", "Bonneville Jets — annual AMA RC turbine jet event.")
    content_html = render_md(body)
    html = template.replace("{{ title }}", title)
    html = html.replace("{{ description }}", description)
    html = html.replace("{{ content }}", content_html)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    print(f"  {md_path} -> {out_path.relative_to(ROOT)}")


def copy_assets():
    """Copy assets/ into docs/assets/."""
    out_assets = OUT_DIR / "assets"
    out_assets.mkdir(parents=True, exist_ok=True)
    for path in ASSETS_DIR.rglob("*"):
        if path.is_file():
            rel = path.relative_to(ASSETS_DIR)
            dest = out_assets / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(path.read_bytes())
            print(f"  assets/{rel} -> docs/assets/{rel}")


def main():
    print("Building Bonneville Jets site -> docs/")
    template = load_template()
    for md_name, html_name in PAGES:
        build_page(template, md_name, OUT_DIR / html_name)
    copy_assets()
    print("Done.")


if __name__ == "__main__":
    main()
