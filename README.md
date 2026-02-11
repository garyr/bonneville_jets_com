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

Open `docs/index.html` in a browser, or serve the `docs` folder:

```bash
python3 -m http.server 8000 --directory docs
```

Then visit **http://localhost:8000**.

### Mobile preview (no deploy needed)

1. From the repo root, run:
   ```bash
   ./serve.sh
   ```
   (Or: `python3 build.py` then `python3 -m http.server 8000 --directory docs`.)

2. In **Chrome**: open http://localhost:8000, press **F12** to open DevTools, then **Ctrl+Shift+M** (Mac: **Cmd+Shift+M**) to toggle the **device toolbar** and pick a phone (e.g. iPhone 12) or set a custom width.

3. Reload after changing CSS or running `build.py`; no need to restart the server.

## Content

- Edit **Markdown** in `content/` and run `build.py` to regenerate HTML.
- **DIRECTIONS.MD** is the source of truth for content, structure, and design guidance.
- Assets (CSS, JS, images) live in `assets/` and are copied into `docs/assets/` on build.

## Hosting elsewhere

The built site in `docs/` is plain HTML/CSS/JS with relative paths. Upload the contents of `docs/` to any static host (e.g. GoDaddy) and it will work.
