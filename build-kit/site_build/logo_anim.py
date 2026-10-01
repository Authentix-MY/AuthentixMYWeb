"""Builds the animated Authentix logo (SVG + CSS + tiny JS) and a demo page."""
import json, re, os, numpy as np
HERE = os.path.dirname(__file__)
T = json.load(open(os.path.join(HERE, '..', 'build', 'traced.json')))

def parts(key):
    return [p for p in re.split(r'(?=M)', T[key]['d']) if p.strip()]

MP = parts('mark')          # 0 = A + orbit, 1 = sparkle, 2 = foot
WP = parts('word')
WORD_ORDER = [2, 8, 4, 0, 5, 6, 3, 9, 1, 7]   # A u t h e n t i(stem) i(dot) x

# ---- orbit centre-line (traced from the logo), in mark viewBox units ----
lower = [(12,488),(40,505),(95,510),(160,496),(285,461),(400,432),(540,399),(620,379),(700,354),(760,330),(800,307),(818,290)]
upper = [(790,277),(740,274),(680,281),(655,287),(540,300),(420,312),(300,328),(195,350),(150,370),(100,395),(55,428),(25,460)]
P = np.array(lower + upper, float) * 2 + np.array([662, 54])

def catmull_path(P):
    n = len(P); d = 'M%.1f %.1f' % tuple(P[0])
    for i in range(n):
        p0, p1, p2, p3 = P[(i-1) % n], P[i], P[(i+1) % n], P[(i+2) % n]
        c1 = p1 + (p2 - p0) / 6; c2 = p2 - (p3 - p1) / 6
        d += ' C%.1f %.1f %.1f %.1f %.1f %.1f' % (*c1, *c2, *p2)
    return d + 'Z'
ORBIT = catmull_path(P)

# fraction of the loop where the glint passes *behind* the A (index 15 -> 19 of the points)
seg = np.r_[0, np.cumsum(np.linalg.norm(np.diff(np.vstack([P, P[:1]]), axis=0), axis=1))]
L = seg[-1]
h0, h1 = seg[len(lower) + 3] / L, seg[len(lower) + 7] / L
HIDE = '0;1;1;0;0;1;0'
HIDE_T = '0;0.05;%.3f;%.3f;%.3f;%.3f;1' % (h0 - 0.02, h0 + 0.01, h1 - 0.01, h1 + 0.02)

MVB = ' '.join(map(str, T['mark']['vb'])); MTR = T['mark']['tr']
WVB = ' '.join(map(str, T['word']['vb'])); WTR = T['word']['tr']

def logo_svg(uid, show_word=True, show_tag=True, size_class='lg', loop=False):
    """Return the full animated lock-up. uid keeps ids unique when several are on one page."""
    word = ''.join('<path class="ax-l" style="--i:%d" d="%s"/>' % (k, WP[i]) for k, i in enumerate(WORD_ORDER))
    mark = f'''<svg class="ax-mark" viewBox="{MVB}" role="img" aria-label="Authentix">
  <defs>
    <clipPath id="{uid}-clip"><path transform="{MTR}" d="{MP[0]}"/></clipPath>
    <radialGradient id="{uid}-g"><stop offset="0" stop-color="#fff" stop-opacity="1"/><stop offset=".12" stop-color="#fff" stop-opacity=".85"/><stop offset=".3" stop-color="#fffbea" stop-opacity=".32"/><stop offset=".6" stop-color="#fffbea" stop-opacity=".08"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
    <radialGradient id="{uid}-gc"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".5" stop-color="#fff" stop-opacity=".45"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
    <path id="{uid}-orbit" d="{ORBIT}"/>
  </defs>
  <g class="ax-halo"><ellipse cx="1617" cy="700" rx="760" ry="420"/></g>
  <ellipse class="ax-glint ax-g-under" rx="300" ry="170" fill="url(#{uid}-g)" opacity="0">
    <animateMotion id="{uid}-m1" begin="indefinite" dur="1.9s" rotate="auto" calcMode="paced" fill="freeze"><mpath href="#{uid}-orbit"/></animateMotion>
    <animate begin="indefinite" dur="1.9s" attributeName="opacity" values="{HIDE}" keyTimes="{HIDE_T}" fill="freeze"/>
  </ellipse>
  <g transform="{MTR}">
    <path class="ax-draw" pathLength="1" d="{MP[0]}"/>
    <path class="ax-draw ax-foot-d" pathLength="1" d="{MP[2]}"/>
    <path class="ax-fill" d="{MP[0]}"/>
    <path class="ax-fill ax-foot" d="{MP[2]}"/>
  </g>
  <ellipse class="ax-glint ax-g-over" rx="300" ry="170" fill="url(#{uid}-g)" opacity="0">
    <animateMotion id="{uid}-m2" begin="indefinite" dur="1.9s" rotate="auto" calcMode="paced" fill="freeze"><mpath href="#{uid}-orbit"/></animateMotion>
    <animate begin="indefinite" dur="1.9s" attributeName="opacity" values="{HIDE}" keyTimes="{HIDE_T}" fill="freeze"/>
  </ellipse>
  <g class="ax-g-clip" clip-path="url(#{uid}-clip)">
    <ellipse class="ax-glint" rx="170" ry="70" fill="url(#{uid}-gc)" opacity="0">
      <animateMotion id="{uid}-m3" begin="indefinite" dur="1.9s" rotate="auto" calcMode="paced" fill="freeze"><mpath href="#{uid}-orbit"/></animateMotion>
      <animate begin="indefinite" dur="1.9s" attributeName="opacity" values="{HIDE}" keyTimes="{HIDE_T}" fill="freeze"/>
    </ellipse>
  </g>
  <g transform="{MTR}"><path class="ax-star" d="{MP[1]}"/></g>
</svg>'''
    w = f'<svg class="ax-word" viewBox="{WVB}" aria-hidden="true"><g transform="{WTR}">{word}</g></svg>' if show_word else ''
    tag = ('<p class="ax-tag"><span>More than tickets</span><span>Real experiences</span></p>') if show_tag else ''
    if loop:
        mark = mark.replace('begin="indefinite"', 'begin="0.3s" repeatCount="indefinite"')
    return f'<div class="ax-logo {size_class}" data-uid="{uid}">{mark}{w}{tag}</div>'

CSS = r'''
.ax-logo{--ax-c:#F1EEE6;display:flex;flex-direction:column;align-items:center;gap:.9em;color:var(--ax-c);user-select:none}
.ax-mark{display:block;overflow:visible;width:var(--mw,260px)}
.ax-word{display:block;width:var(--ww,300px);overflow:visible}
.ax-fill{fill:var(--ax-c)}
.ax-l{fill:var(--ax-c);transform-box:fill-box;transform-origin:50% 100%}
.ax-star{fill:var(--ax-c);transform-box:fill-box;transform-origin:50% 50%;filter:drop-shadow(0 0 0 rgba(255,255,255,0))}
.ax-draw{fill:none;stroke:var(--ax-c);stroke-width:1.4px;vector-effect:non-scaling-stroke;stroke-dasharray:1 1;stroke-dashoffset:1;opacity:0}
.ax-halo ellipse{fill:rgba(241,238,230,.07);filter:blur(60px);opacity:0}
.ax-g-clip{display:none}
.ax-on-light .ax-tag span{background:none;color:var(--ax-c)}
.ax-on-light .ax-g-clip{display:inline}.ax-on-light .ax-g-under,.ax-on-light .ax-g-over{display:none}
.ax-logo .ax-tag{margin:.4em 0 0;display:flex;flex-direction:column;align-items:center;gap:.55em;font:500 var(--ts,15px)/1 Montserrat,"Helvetica Neue",Arial,sans-serif;letter-spacing:.42em;text-transform:uppercase;padding-left:.42em}
.ax-tag span{background:linear-gradient(100deg,var(--ax-c) 0%,var(--ax-c) 38%,#cfe7ff 46%,#ffe1f2 50%,#fff3cf 54%,var(--ax-c) 62%,var(--ax-c) 100%);background-size:300% 100%;background-position:100% 0;-webkit-background-clip:text;background-clip:text;color:transparent}

/* ---------- intro (add .ax-play) ---------- */
.ax-play .ax-draw{animation:ax-draw 1.5s cubic-bezier(.6,0,.3,1) .15s forwards,ax-fade .5s ease 1.5s forwards}
.ax-play .ax-foot-d{animation-delay:.55s,1.5s}
.ax-play .ax-fill{opacity:0;animation:ax-in .7s ease 1.1s forwards}
.ax-play .ax-foot{animation-delay:1.25s}
.ax-play .ax-halo ellipse{animation:ax-halo 2.4s ease 1.2s forwards}
.ax-play .ax-star{transform:scale(0) rotate(-120deg);animation:ax-pop .9s cubic-bezier(.2,1.6,.4,1) 2s forwards,ax-flash 1.1s ease 2.15s}
.ax-play .ax-l{opacity:0;transform:translateY(55%);animation:ax-rise .7s cubic-bezier(.2,.8,.2,1) calc(2.25s + var(--i)*.06s) forwards}
.ax-play .ax-tag span{opacity:0;filter:blur(8px);letter-spacing:.9em;animation:ax-tag 1.1s cubic-bezier(.2,.8,.2,1) 2.9s forwards,ax-holo 2.4s ease 3.6s}
.ax-play .ax-tag span+span{animation-delay:3.15s,3.85s}
@keyframes ax-draw{0%{opacity:1;stroke-dashoffset:1}100%{opacity:1;stroke-dashoffset:0}}
@keyframes ax-fade{to{opacity:0}}
@keyframes ax-in{to{opacity:1}}
@keyframes ax-halo{0%{opacity:0}40%{opacity:1}100%{opacity:.55}}
.ax-play-done .ax-halo ellipse{opacity:.55}
@keyframes ax-pop{to{transform:scale(1) rotate(0)}}
@keyframes ax-flash{0%,100%{filter:drop-shadow(0 0 0 rgba(255,255,255,0))}35%{filter:drop-shadow(0 0 60px rgba(255,255,255,.95))}}
@keyframes ax-rise{to{opacity:1;transform:none}}
@keyframes ax-tag{to{opacity:1;filter:blur(0);letter-spacing:.42em}}
@keyframes ax-holo{from{background-position:100% 0}to{background-position:0 0}}

/* ---------- idle moments (classes toggled by JS) ---------- */
.ax-twinkle .ax-star{animation:ax-twk 1.2s ease-in-out}
@keyframes ax-twk{0%{transform:scale(1) rotate(0)}30%{transform:scale(.7) rotate(25deg)}60%{transform:scale(1.18) rotate(90deg);filter:drop-shadow(0 0 45px rgba(255,255,255,.85))}100%{transform:scale(1) rotate(90deg)}}
.ax-shine .ax-halo ellipse{animation:ax-breathe 2.6s ease}
@keyframes ax-breathe{0%,100%{opacity:.55}50%{opacity:1}}
.ax-holo-run .ax-tag span{animation:ax-holo 2.4s ease}

@media (prefers-reduced-motion:reduce){
  .ax-logo *{animation:none !important;transition:none !important}
  .ax-play .ax-fill,.ax-play .ax-l,.ax-play .ax-tag span{opacity:1 !important;transform:none !important;filter:none !important;letter-spacing:.42em}
  .ax-play .ax-star{transform:none !important}
  .ax-glint{display:none}
}
'''

JS = r'''
(function(){
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  function orbit(el){ el.querySelectorAll("animateMotion,animate").forEach(function(m){ try { m.beginElement(); } catch(e){} }); }
  function pulse(el, cls, ms){ el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); setTimeout(function(){ el.classList.remove(cls); }, ms); }
  function play(el){
    el.classList.remove("ax-play"); void el.offsetWidth; el.classList.add("ax-play");
    clearTimeout(el._t1); clearTimeout(el._t2);
    if (reduce) return;
    el._t1 = setTimeout(function(){ orbit(el); }, 1450);           // glint flies round the ring
    el._t2 = setTimeout(function(){ el.classList.add("ax-play-done"); }, 3700);
  }
  function idle(el){
    if (reduce || el._idle) return;
    var n = 0;
    el._idle = setInterval(function(){
      n++;
      if (document.hidden) return;
      if (n % 2) pulse(el, "ax-twinkle", 1300); else orbit(el);
      if (n % 4 === 0) pulse(el, "ax-shine", 2700);
    }, 3600);
  }
  function hover(el, target){
    var last = 0;
    (target || el).addEventListener("pointerenter", function(){
      if (reduce || Date.now() - last < 2000) return; last = Date.now();
      orbit(el); pulse(el, "ax-twinkle", 1300); pulse(el, "ax-holo-run", 2500);
    });
  }
  window.AuthentixLogo = { play: play, idle: idle, hover: hover, orbit: orbit };
  document.querySelectorAll(".ax-logo[data-autoplay]").forEach(function(el){
    var start = function(){ play(el); setTimeout(function(){ idle(el); }, 5200); hover(el); };
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { io.disconnect(); start(); } }); }, { threshold: .4 });
      io.observe(el);
    } else start();
  });
})();
'''

if __name__ == '__main__':
    hero = logo_svg('h1').replace('class="ax-logo lg"', 'class="ax-logo lg" data-autoplay')
    pre = logo_svg('p1', show_word=False, show_tag=False, size_class='pre')
    nav = logo_svg('n1', show_tag=False, size_class='nav').replace('class="ax-logo nav"', 'class="ax-logo nav ax-play-static"')
    light = logo_svg('l1', size_class='lt').replace('class="ax-logo lt"', 'class="ax-logo lt ax-on-light" data-autoplay')
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Authentix · Logo animation demo</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box}}html,body{{margin:0}}
body{{background:#0E1512;color:#F1EEE6;font-family:Montserrat,"Helvetica Neue",Arial,sans-serif}}
{CSS}
.stage{{position:relative;min-height:100vh;display:grid;place-items:center;overflow:hidden;
  background:radial-gradient(120% 90% at 50% 38%,#4a5550 0%,#2c3532 38%,#141b18 75%,#0b100e 100%)}}
.stage:before{{content:"";position:absolute;inset:-20%;background:conic-gradient(from 200deg at 50% -10%,transparent 0 40%,rgba(255,255,255,.06) 47%,transparent 54% 100%);animation:sweep 14s ease-in-out infinite alternate;pointer-events:none}}
@keyframes sweep{{from{{transform:rotate(-8deg)}}to{{transform:rotate(8deg)}}}}
.lg{{--mw:min(400px,72vw);--ww:min(400px,72vw);--ts:clamp(11px,1.7vw,17px)}}
.lg .ax-word{{margin-top:-.2em}}
.bar{{position:absolute;left:50%;bottom:22px;transform:translateX(-50%);display:flex;gap:10px;z-index:5}}
.btn{{min-height:44px;padding:0 18px;white-space:nowrap;border-radius:999px;border:0;background:#EFECE5;color:#1F3A2F;font:600 14px Montserrat,sans-serif;cursor:pointer}}
.btn.ghost{{background:rgba(241,238,230,.08);color:#F1EEE6;box-shadow:inset 0 0 0 1px rgba(241,238,230,.3)}}
section.more{{padding:72px 20px 120px;max-width:1080px;margin:0 auto}}
section.more h2{{font-size:13px;letter-spacing:.3em;text-transform:uppercase;color:#A9B2AC;font-weight:600;margin:0 0 22px}}
.grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}}
.card{{border-radius:24px;padding:28px;min-height:300px;display:flex;flex-direction:column;justify-content:space-between;background:#16201c;box-shadow:inset 0 0 0 1px rgba(241,238,230,.08)}}
.card .lbl{{font-size:13px;font-weight:600}}.card p{{margin:6px 0 0;font-size:13px;color:#A9B2AC;line-height:1.5}}
.card .demo{{flex:1;display:grid;place-items:center;padding:18px 0}}
.pre{{--mw:120px}}
.loader{{display:flex;flex-direction:column;align-items:center;gap:18px}}
.loader i{{display:block;width:120px;height:2px;border-radius:2px;background:rgba(241,238,230,.15);overflow:hidden;position:relative}}
.loader i:after{{content:"";position:absolute;inset:0;width:40%;background:#F1EEE6;animation:load 1.4s ease-in-out infinite}}
@keyframes load{{from{{transform:translateX(-100%)}}to{{transform:translateX(250%)}}}}
.nav{{flex-direction:row;gap:10px;--mw:46px;--ww:104px}}
.navbar{{width:100%;display:flex;align-items:center;justify-content:space-between;padding:14px 18px;border-radius:16px;background:rgba(14,21,18,.9);box-shadow:0 0 0 1px rgba(241,238,230,.08)}}
.navbar small{{color:#A9B2AC;font-size:12px;white-space:nowrap}}
.card.cream{{background:#EFECE5;color:#1F3A2F}}.card.cream p{{color:#5E6661}}
.lt{{--ax-c:#1F3A2F;--mw:160px;--ww:160px;--ts:9px}}
.lt .ax-halo{{display:none}}
@media (max-width:860px){{.grid{{grid-template-columns:1fr}}}}
@media (max-width:420px){{.btn{{padding:0 14px;font-size:13px}}.bar{{gap:6px}}}}
</style></head><body>
<header class="stage" id="hero">{hero}
  <div class="bar"><button class="btn" id="replay" type="button">Replay intro</button><button class="btn ghost" id="orbit" type="button">Orbit glint</button><button class="btn ghost" id="twk" type="button">Twinkle</button></div>
</header>
<section class="more">
  <h2>Where it lives on the website</h2>
  <div class="grid">
    <div class="card"><div><div class="lbl">1 · Page loader</div><p>Shows for a split second while the site loads, ring keeps orbiting.</p></div><div class="demo"><div class="loader">{pre}<i></i></div></div></div>
    <div class="card"><div><div class="lbl">2 · Navigation bar</div><p>Static at rest. Hover it: the glint orbits and the star twinkles.</p></div><div class="demo"><div class="navbar">{nav}<small>Drops · FAQ</small></div></div></div>
    <div class="card cream"><div><div class="lbl">3 · On cream (footer / posters)</div><p>Same motion in brand forest green on light backgrounds.</p></div><div class="demo">{light}</div></div>
  </div>
</section>
<script>{JS}</script>
<script>
(function(){{
  var h = document.querySelector("#hero .ax-logo"), A = window.AuthentixLogo;
  document.getElementById("replay").onclick = function(){{ A.play(h); }};
  document.getElementById("orbit").onclick = function(){{ A.orbit(h); }};
  document.getElementById("twk").onclick = function(){{ h.classList.remove("ax-twinkle"); void h.offsetWidth; h.classList.add("ax-twinkle"); setTimeout(function(){{ h.classList.remove("ax-twinkle"); }}, 1300); }};
  var p = document.querySelector(".pre"); A.orbit(p); setInterval(function(){{ A.orbit(p); }}, 2100);
  setInterval(function(){{ p.classList.remove("ax-twinkle"); void p.offsetWidth; p.classList.add("ax-twinkle"); }}, 4200);
  var n = document.querySelector(".nav"); A.hover(n);
}})();
</script>
</body></html>'''
    out = os.path.join(HERE, 'Authentix_Logo_Animation_Demo.html')
    open(out, 'w').write(html)
    print('wrote', out, len(html))
