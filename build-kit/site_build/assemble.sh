set -e
python3 build3.py
rm -rf repo && mkdir repo && cp -r site3 repo/authentix-site && cp -r kit/* repo/authentix-site/
cp README_repo.md repo/authentix-site/README.md
# Never ship the blank config.js: the live one on GitHub holds the real Supabase URL + key.
rm -f repo/authentix-site/config.js
(cd repo && rm -f ../Authentix_Website_Netlify.zip && zip -rq ../Authentix_Website_Netlify.zip authentix-site)
