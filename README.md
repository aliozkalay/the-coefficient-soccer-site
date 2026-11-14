# The Coefficient

Public website source for [thecoefficiency.com](https://thecoefficiency.com), a European soccer analytics project hosted on Cloudflare Pages.

The Coefficient explains European football with public match data: competitions, a Poisson + Elo prediction model, a Match Center calendar, day and night modes, and educational analysis. It is not a betting product.

This repository holds the static site files (HTML, CSS, JavaScript, images, and self-hosted fonts) plus an optional page-builder script.

## Local preview

```bash
python3 -m http.server 8787
# open http://127.0.0.1:8787
```

To regenerate pages from the shared template:

```bash
python3 _build.py
```

## Live site

- Site: https://thecoefficiency.com
- YouTube: https://www.youtube.com/@TheCoefficient-g8c
- Portfolio: https://ali-ozkalay.pages.dev
