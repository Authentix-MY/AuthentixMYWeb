# Authentix website + admin

| Path | What it is |
|---|---|
| `/` | Website (English) |
| `/zh/` | Website (简体中文) |
| `/admin/` | Admin: dashboard, enquiries, drops, reviews, settings |
| `config.js` | The ONLY file you edit at go-live (Supabase URL + anon key) |
| `data/*.json` | Backup copy of drops, reviews, FAQ and contact links, shown if the database is unreachable (download fresh copies from Admin → Settings) |
| `supabase/schema.sql` | Run once in Supabase → SQL Editor (change the admin email first) |
| `supabase/seed.sql` | Loads the current drops, reviews, FAQ and contact links |
| `netlify/functions/keep-alive.mjs` | Daily ping so the free database never pauses |

## Go-live checklist
1. Supabase: create a project (Singapore region) → SQL Editor → paste `schema.sql` (edit the admin email) → Run → paste `seed.sql` → Run (loads your drops, reviews, FAQ and contact links).
2. Supabase → Authentication → Users → Add user (your admin email + a strong password).
3. Supabase → Project Settings → API: copy the Project URL and the `anon` public key into `config.js`.
4. GitHub: create a private repo and upload this whole folder.
5. Netlify: Add new site → Import from GitHub → pick the repo (publish directory `.`; no build command).
6. Netlify → Site configuration → Environment variables: add `SUPABASE_URL` and `SUPABASE_ANON_KEY` (same values) → redeploy.
7. Netlify → Forms: enable form detection, then add an email notification for the `quote` form.
8. Test: submit a quote on the live site → it appears in `/admin/` and in your inbox.

Without steps 1–3 the site still works: drops/reviews come from the backup copy and enquiries arrive by Netlify email.
