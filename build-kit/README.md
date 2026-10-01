# Authentix website: build kit

This folder holds the **source** that generates the live website in `authentix-site/`.
It sits outside `authentix-site/`, so Netlify never publishes it. Nothing in here is visible to visitors.

> For a future Claude task: read this whole file first. The website pages are generated files;
> change the source here, rebuild, then copy only the changed outputs into `authentix-site/`.

---

## 1. How the pieces fit

| Piece | Where | What it does |
|---|---|---|
| Live website | `authentix-site/` (Netlify base directory) | Public site `/`, Chinese `/zh/`, admin `/admin/` |
| Hosting | Netlify project **authentixmy** → https://authentixmy.netlify.app | Redeploys automatically on every commit to `main` |
| Database, login, images | Supabase project ref `xyvksinppfvwhqbghryh` | Tables: enquiries, drops, reviews, faqs, settings, events, admins, heartbeat. Storage bucket `media` (public) |
| Site settings | `authentix-site/config.js` | Supabase URL + publishable key. **Edited by hand on GitHub. Never overwrite it.** |
| Keep-alive | `authentix-site/netlify/functions/keep-alive.mjs` | Daily ping so the free Supabase project doesn't pause. Needs Netlify env vars `SUPABASE_URL` and `SUPABASE_ANON_KEY` |

Drops, reviews, FAQs and the WhatsApp / Instagram / Carousell links are edited in the **admin portal** and stored in Supabase.
The copies in `site_build/data.py` are only the offline backup the site falls back on if Supabase is unreachable.

## 2. Folder map

```
build-kit/
  build/                  Brand helpers shared with the brand board
    common.py             Colours, logo SVG helper (_svg), icons
    traced.json           The traced Authentix logo (mark + wordmark paths). Do not redraw the logo, use this.
    *.py                  Brand-board generators (not needed for the website)
  site_build/
    template3.html        Public site template (EN + 中文 share one template)
    base.css, extra.css   Site styles
    i18n.py               Every English / Simplified Chinese string (key → [EN, ZH])
    data.py               Backup drops, reviews, FAQs, contact links
    logo_anim.py          Animated logo (loader, hero intro, nav/footer hover, CTA)
    admin_template.html   Admin portal (dashboard, enquiries, drops, reviews, FAQ, settings)
    build3.py             Builds the site + admin from the above
    assemble.sh           Runs the build and assembles repo/authentix-site/
    site/                 Static assets copied as-is (images, favicon, 404, thank-you)
    kit/                  Netlify + Supabase files (netlify.toml, keep-alive, SQL)
    README_repo.md        Becomes authentix-site/README.md
```

## 3. Rebuild

Needs Python 3 (standard library only) and `zip`.

1. `cd build-kit/site_build`
2. `bash assemble.sh`
3. Output appears in `site_build/repo/authentix-site/`. Copy only the files you changed into the repo's `authentix-site/`. Usually that means:
   - `index.html` and `zh/index.html` (public site)
   - `admin/index.html` (admin portal)
   - `netlify/functions/keep-alive.mjs` (only if changed)
4. **Do not copy `config.js`.** The build deliberately leaves it out.
5. Commit to `main`. Netlify redeploys in about a minute.
6. Delete `site_build/repo/`, `site_build/site3/` and the demo HTML files afterwards. They're build output and shouldn't be committed.

`logo_anim.py` can also be run on its own to produce `Authentix_Logo_Animation_Demo.html` for previewing.

## 4. Brand rules

- Colours: Forest `#1F3A2F`, Deep Night `#0E1512`, Sage `#8E9A93`, Cream `#EFECE5`, Paper `#E7E4DC`, Ink `#0F0F0F`, Text `#F1EEE6`
- Font: Montserrat (Noto Sans SC for Chinese)
- Logo: always from `build/traced.json`, never redrawn
- Tagline: "More than tickets / Real experiences"
- Chinese glossary: Internal orders = 内部票 · Buy For You = 代抢票 · Pre-order = 预订 · Drops = 开票
- Most popular service: **Internal orders**
- Every new string goes into `i18n.py` with both EN and ZH

## 5. Gotchas learned during setup

- The Supabase key is the new `sb_publishable_…` type. It's sent as `apikey` only. `Authorization: Bearer` is added only for old JWT-style keys (starting `eyJ`).
- Image uploads need the Storage bucket `media` (created by `kit/supabase/storage.sql`).
- SQL files must live in `authentix-site/supabase/` (blocked from public view by `netlify.toml`), never in the `authentix-site/` root.
- Drop posters are shown uncropped (4:5 card with a blurred backdrop). Portrait posters look best.
- Admin login: Supabase Authentication user whose email is also in the `admins` table. Public sign-ups are disabled.
- WhatsApp: +60 12-659 2025 · Instagram @authentix_my · Carousell link is set in admin Settings.
- No SSM number is shown anywhere on the site (by choice).
