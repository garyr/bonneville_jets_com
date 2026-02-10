# Bonneville Jets

Official site for the annual Bonneville Jets AMA RC turbine jet event on the Bonneville Salt Flats.

## Build

From the repo root:

```bash
python3 build.py
```

Output is written to **`docs/`** for GitHub Pages. No extra dependencies (Python 3 stdlib only).

## Deploy (GitHub Pages)

1. Push the repo to GitHub.
2. In the repo **Settings → Pages**, set **Source** to "Deploy from a branch" and choose branch `main`, folder **`/docs`**.
3. Save; the site will be available at `https://<username>.github.io/<repo>/`.

## Local preview

Open `docs/index.html` in a browser, or serve the `docs` folder (e.g. `python3 -m http.server 8000 --directory docs` then visit http://localhost:8000).

## Content

- Edit **Markdown** in `content/` and run `build.py` to regenerate HTML.
- **DIRECTIONS.MD** is the source of truth for content, structure, and design guidance.
- Assets (CSS, JS, images) live in `assets/` and are copied into `docs/assets/` on build.

## Hosting elsewhere

The built site in `docs/` is plain HTML/CSS/JS with relative paths. Upload the contents of `docs/` to any static host (e.g. GoDaddy) and it will work.
