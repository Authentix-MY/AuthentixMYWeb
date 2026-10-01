import sys, os, re, json, base64, shutil
sys.path.insert(0, '../build')
from common import _svg, icon, TXT, FOREST, SAGE, CREAM
from i18n import I18N
from data import DROPS, REVIEWS, FAQS, CONTACTS
import html as _h
import logo_anim as LA

OUT = 'site3'
CSS = open('base.css').read() + open('extra.css').read()
T = open('template3.html').read()

def b64(p, mime): return f'data:{mime};base64,' + base64.b64encode(open(p, 'rb').read()).decode()
def clean(svg): return svg.replace(' style="display:block;flex-shrink:0"', '')

AX_SITE_CSS = """
.hero .ax-logo{--mw:clamp(150px,22vw,230px);--ww:clamp(240px,34vw,410px);gap:14px}
.brand .ax-logo{--mw:40px}
footer .brand .ax-logo{--mw:40px}
.cta .ax-logo{--mw:96px}
.hero .hseq{opacity:0;animation:ax-hseq .9s cubic-bezier(.2,.8,.2,1) 2.7s forwards}
.hero .lead.hseq{animation-delay:2.9s}.hero .hero-ctas.hseq{animation-delay:3.05s}
@keyframes ax-hseq{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
html.ax-loading .hero,html.ax-loading .hero *{animation-play-state:paused !important}
.ax-loader{display:none}
html.ax-loading .ax-loader,html.ax-loaded .ax-loader{position:fixed;inset:0;z-index:1000;display:grid;place-items:center;background:radial-gradient(90% 70% at 50% 45%,#26302c 0%,#0E1512 70%)}
html.ax-loaded .ax-loader{animation:ax-lout .6s ease forwards;pointer-events:none}
@keyframes ax-lout{to{opacity:0;visibility:hidden}}
.ax-loader .ax-in{display:flex;flex-direction:column;align-items:center;gap:20px}
.ax-loader .ax-logo{--mw:120px}
.ax-loader i{display:block;width:120px;height:2px;border-radius:2px;background:rgba(241,238,230,.15);overflow:hidden;position:relative}
.ax-loader i:after{content:"";position:absolute;inset:0;width:40%;background:#F1EEE6;animation:ax-load 1.3s ease-in-out infinite}
@keyframes ax-load{from{transform:translateX(-100%)}to{transform:translateX(250%)}}
@media (prefers-reduced-motion:reduce){.hero .hseq{opacity:1;animation:none}}
"""
AX_HEAD = """<script>(function(){var d=document.documentElement,t0=Date.now(),show=false;d.classList.add('ax-js');
try{show=!sessionStorage.getItem('ax_seen')&&!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches);sessionStorage.setItem('ax_seen','1')}catch(e){}
function go(){if(window.__axStarted)return;window.__axStarted=true;d.classList.remove('ax-loading');if(show)d.classList.add('ax-loaded');try{document.dispatchEvent(new Event('ax:start'))}catch(e){}}
if(!show){window.__axStarted=true;return}
d.classList.add('ax-loading');
window.addEventListener('load',function(){setTimeout(go,Math.max(300,1100-(Date.now()-t0)))});setTimeout(go,2200);})();</script>"""
AX_INIT = r"""(function(){
  var A = window.AuthentixLogo; if (!A) return;
  var hero = document.querySelector(".hero .ax-logo");
  function startHero(){
    if (!hero) return;
    setTimeout(function(){ A.orbit(hero); }, 1450);
    setTimeout(function(){ hero.classList.add("ax-play-done"); A.idle(hero); }, 5200);
  }
  if (window.__axStarted) startHero(); else document.addEventListener("ax:start", startHero, { once: true });
  if (hero) A.hover(hero);
  document.querySelectorAll(".brand .ax-logo").forEach(function(el){ A.hover(el, el.closest(".brand")); });
  var cta = document.querySelector(".cta .ax-logo");
  if (cta) {
    A.hover(cta);
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { io.disconnect(); A.orbit(cta); cta.classList.add("ax-twinkle"); setTimeout(function(){ cta.classList.remove("ax-twinkle"); }, 1300); } }); }, { threshold: .6 });
      io.observe(cta);
    }
  }
})();"""

static = {
 '%%CSS%%': CSS + LA.CSS + AX_SITE_CSS,
 '%%AX_HEAD%%': AX_HEAD,
 '%%AX_LOADER%%': '<div class="ax-loader" aria-hidden="true"><div class="ax-in">' + LA.logo_svg('axl', show_word=False, show_tag=False, size_class='ldr', loop=True) + '<i></i></div></div>',
 '%%AX_NAV%%': LA.logo_svg('axn', show_word=False, show_tag=False, size_class='nv'),
 '%%AX_FOOT%%': LA.logo_svg('axf', show_word=False, show_tag=False, size_class='ft'),
 '%%AX_HERO%%': '<h2 class="sr">Authentix</h2>' + LA.logo_svg('axh', show_tag=False, size_class='hr').replace('class="ax-logo hr"', 'class="ax-logo hr ax-play"', 1),
 '%%AX_CTA%%': LA.logo_svg('axc', show_word=False, show_tag=False, size_class='ct'),
 '%%AX_JS%%': LA.JS,
 '%%AX_INIT%%': AX_INIT,
 '%%MARK_NAV%%': clean(_svg('mark', TXT, w=40)),
 '%%WORD_NAV%%': clean(_svg('word', TXT, h=22, label='Authentix')),
 '%%MARK_HERO%%': clean(_svg('mark', TXT, w=230)).replace('<svg ', '<svg style="width:clamp(150px,22vw,230px);height:auto" ', 1),
 '%%WORD_HERO%%': '<h2 class="sr">Authentix</h2>' + clean(_svg('word', TXT, h=70, label='Authentix')).replace('<svg ', '<svg style="width:clamp(240px,34vw,410px);height:auto" ', 1),
 '%%MARK_CTA%%': clean(_svg('mark', TXT, w=96)),
 '%%MARK_WM%%': clean(_svg('mark', CREAM, w=640)),
 '%%I_SHIELD%%': icon('shield', 40, TXT, 1.3), '%%I_TICKET%%': icon('ticket', 40, TXT, 1.3), '%%I_GLOBE%%': icon('globe', 40, TXT, 1.3),
 '%%I_PEOPLE%%': icon('people', 40, TXT, 1.3), '%%I_HEADSET%%': icon('headset', 40, TXT, 1.3),
 '%%I_TICKET_W%%': icon('ticket', 26, TXT, 1.6), '%%I_PERCENT_W%%': icon('percent', 26, TXT, 1.6),
 '%%I_PEOPLE_F%%': icon('people', 26, FOREST, 1.6), '%%I_HEADSET_W%%': icon('headset', 26, TXT, 1.6),
 '%%I_CHECK%%': icon('check', 28, CREAM, 2.2), '%%I_X%%': icon('x', 22, SAGE, 2.2),
 '%%I18N_JSON%%': json.dumps(I18N, ensure_ascii=False),
 '%%DROPS_JSON%%': json.dumps(DROPS, ensure_ascii=False),
 '%%REVIEWS_JSON%%': json.dumps(REVIEWS, ensure_ascii=False),
 '%%FAQS_JSON%%': json.dumps(FAQS, ensure_ascii=False),
 '%%CONTACTS_JSON%%': json.dumps(CONTACTS, ensure_ascii=False),
}
for k, v in static.items(): T = T.replace(k, v)

def prerender(html, lang):
    i = 0 if lang == 'en' else 1
    def fill(m):
        key = m.group(2)
        if key not in I18N: raise KeyError(key)
        return m.group(1) + I18N[key][i] + m.group(3)
    html = re.sub(r'(data-i18n="([\w.]+)"[^>]*>)(</)', fill, html)
    html = re.sub(r'data-i18n-ph="([\w.]+)"', lambda m: f'data-i18n-ph="{m.group(1)}" placeholder="{I18N[m.group(1)][i]}"', html)
    html = re.sub(r'data-i18n-aria="([\w.]+)"', lambda m: f'data-i18n-aria="{m.group(1)}" aria-label="{I18N[m.group(1)][i]}"', html)
    html = re.sub(r'data-i18n-content="([\w.]+)"', lambda m: f'data-i18n-content="{m.group(1)}" content="{I18N[m.group(1)][i].replace(chr(34), "&quot;")}"', html)
    return html

REV_FILES = [r['screenshot_url'] for r in REVIEWS]

def page(lang, mode):
    s = T.replace('%%HTMLLANG%%', 'en' if lang == 'en' else 'zh-Hans').replace('%%INITLANG%%', lang)
    if mode == 'demo':
        img = lambda f: b64(f'site/assets/img/{f}', 'image/jpeg')
        s = (s.replace('%%IMG_CROWD%%', img('crowd-hands.jpg')).replace('%%IMG_BEAMS%%', img('stage-beams.jpg')).replace('%%IMG_NIGHT%%', img('festival-night.jpg'))
              .replace('%%IMG_QR%%', b64('site/assets/img/ig-qr.png', 'image/png'))
              .replace('%%FAVICON%%', b64('site/assets/favicon.png', 'image/png')).replace('%%TOUCH%%', b64('site/assets/favicon.png', 'image/png'))
              .replace('%%OG%%', 'assets/og-image.jpg').replace('%%HREFLANG%%', '')
              .replace('%%SHOT_BASE%%', '').replace('%%INLINE_SHOTS%%', '[' + ','.join('"' + b64(f'site/assets/img/reviews/{f}', 'image/jpeg') + '"' for f in REV_FILES) + ']'))
    else:
        s = (s.replace('%%IMG_CROWD%%', '/assets/img/crowd-hands.jpg').replace('%%IMG_BEAMS%%', '/assets/img/stage-beams.jpg').replace('%%IMG_NIGHT%%', '/assets/img/festival-night.jpg')
              .replace('%%IMG_QR%%', '/assets/img/ig-qr.png').replace('%%FAVICON%%', '/assets/favicon.png').replace('%%TOUCH%%', '/apple-touch-icon.png')
              .replace('%%OG%%', '/assets/og-image.jpg')
              .replace('%%HREFLANG%%', '<link rel="alternate" hreflang="en" href="/">\n<link rel="alternate" hreflang="zh-Hans" href="/zh/">\n<link rel="alternate" hreflang="x-default" href="/">')
              .replace('%%SHOT_BASE%%', '/assets/img/reviews/').replace('%%INLINE_SHOTS%%', '[]'))
    k = 'en' if lang == 'en' else 'zh'
    s = s.replace('%%FAQ_HTML%%', ''.join(f'<details data-q="{f["id"]}"><summary><span>{_h.escape(f["q_"+k])}</span><span class="pm" aria-hidden="true">+</span></summary><p>{_h.escape(f["a_"+k])}</p></details>' for f in FAQS if f["visible"]))
    s = s.replace('%%CONFIG_SCRIPT%%', '' if mode == 'demo' else '<script src="/config.js"></script>\n')
    s = prerender(s, lang)
    left = re.findall(r'%%\w+%%', s)
    assert not left, left
    return s

if __name__ == '__main__':
    shutil.rmtree(OUT, ignore_errors=True)
    shutil.copytree('site', OUT, ignore=shutil.ignore_patterns('_test.html', 'index.html'))
    os.makedirs(f'{OUT}/zh', exist_ok=True); os.makedirs(f'{OUT}/data', exist_ok=True)
    open(f'{OUT}/index.html', 'w').write(page('en', 'prod'))
    open(f'{OUT}/zh/index.html', 'w').write(page('zh', 'prod'))
    json.dump(DROPS, open(f'{OUT}/data/drops.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(REVIEWS, open(f'{OUT}/data/reviews.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(FAQS, open(f'{OUT}/data/faqs.json', 'w'), ensure_ascii=False, indent=1)
    json.dump([{"key": "contacts", "value": CONTACTS}], open(f'{OUT}/data/settings.json', 'w'), ensure_ascii=False, indent=1)
    open('Authentix_Website_Demo.html', 'w').write(page('en', 'demo'))
    print('built', os.path.getsize(f'{OUT}/index.html'), os.path.getsize(f'{OUT}/zh/index.html'), os.path.getsize('Authentix_Website_Demo.html'))

# ---------------- ADMIN ----------------
def admin(mode):
    A = open('admin_template.html').read()
    ico = lambda p: f'<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
    A = (A.replace('%%MARK_NAV%%', clean(_svg('mark', TXT, w=34))).replace('%%WORD_NAV%%', clean(_svg('word', TXT, h=18, label='Authentix')))
          .replace('%%MARK_DARK%%', clean(_svg('mark', FOREST, w=40)))
          .replace('%%I_GRID%%', ico('<rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/>'))
          .replace('%%I_INBOX%%', ico('<path d="M3 13l2.5-8h13L21 13v6H3z"/><path d="M3 13h5l1.5 2.5h5L16 13h5"/>'))
          .replace('%%I_TICKET%%', ico('<path d="M3 7.5H21V10.5A1.5 1.5 0 0 0 21 13.5V16.5H3V13.5A1.5 1.5 0 0 0 3 10.5Z"/><path d="M15 8.5V15.5" stroke-dasharray="1.2 1.8"/>'))
          .replace('%%I_STAR%%', ico('<path d="M12 3.5L14.6 9.1L20.6 9.7L16.1 13.7L17.4 19.7L12 16.6L6.6 19.7L7.9 13.7L3.4 9.7L9.4 9.1Z"/>'))
          .replace('%%I_GEAR%%', ico('<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>'))
          .replace('%%DROPS_JSON%%', json.dumps(DROPS, ensure_ascii=False)).replace('%%REVIEWS_JSON%%', json.dumps(REVIEWS, ensure_ascii=False))
          .replace('%%FAQS_JSON%%', json.dumps(FAQS, ensure_ascii=False)).replace('%%CONTACTS_JSON%%', json.dumps(CONTACTS, ensure_ascii=False))
          .replace('%%I_HELP%%', ico('<circle cx="12" cy="12" r="9"/><path d="M9.5 9.2a2.6 2.6 0 0 1 5 .9c0 1.7-2.5 2.3-2.5 3.9"/><circle cx="12" cy="17" r=".6" fill="currentColor"/>')))
    if mode == 'demo':
        img = lambda f: b64(f'site/assets/img/{f}', 'image/jpeg')
        bundled = {'crowd': img('crowd-hands.jpg'), 'beams': img('stage-beams.jpg'), 'night': img('festival-night.jpg'),
                   'shots': {f: b64(f'site/assets/img/reviews/{f}', 'image/jpeg') for f in REV_FILES}}
        A = A.replace('%%FAVICON%%', b64('site/assets/favicon.png', 'image/png'))
    else:
        bundled = {'crowd': '/assets/img/crowd-hands.jpg', 'beams': '/assets/img/stage-beams.jpg', 'night': '/assets/img/festival-night.jpg',
                   'shots': {f: f'/assets/img/reviews/{f}' for f in REV_FILES}}
        A = A.replace('%%FAVICON%%', '/assets/favicon.png')
    A = A.replace('%%BUILD_DEMO%%', 'true' if mode == 'demo' else 'false')
    A = A.replace('%%BUNDLED_JSON%%', json.dumps(bundled)).replace('%%CONFIG_SCRIPT%%', '' if mode == 'demo' else '<script src="/config.js"></script>\n')
    assert not re.findall(r'%%\w+%%', A), re.findall(r'%%\w+%%', A)
    return A

if __name__ == '__main__':
    os.makedirs(f'{OUT}/admin', exist_ok=True)
    open(f'{OUT}/admin/index.html', 'w').write(admin('prod'))
    open('Authentix_Admin_Demo.html', 'w').write(admin('demo'))
    print('admin built', os.path.getsize('Authentix_Admin_Demo.html'))
