# jungehyun.github.io

Personal website of Junge Hyun. Plain HTML + CSS, no build step.

- `index.html`, `style.css` — the page
- `assets/photo.jpg` — portrait (480 px square), `assets/CV_JungeHyun.pdf` — CV (web version, no phone number)
- `content_draft.md` — working notes for the text (not served)

Preview locally: `python3 -m http.server 8791` in this folder, then open http://localhost:8791/.

Deploy: push to the GitHub repository `jungehyun/jungehyun.github.io` (branch `main`); GitHub Pages serves it at https://jungehyun.github.io within a few minutes. In the repository settings, Pages → Source should be "Deploy from a branch", branch `main`, folder `/ (root)`.
