import os, random
import json as _json
_T=_json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'traced.json')))
def _svg(key,color,w=None,h=None,label=None):
    o=_T[key]; vx,vy,vw,vh=o['vb']
    if w is None: w=round(h*vw/vh)
    if h is None: h=round(w*vh/vw)
    a=f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg viewBox="{vx} {vy} {vw} {vh}" width="{w}" height="{h}" {a} style="display:block;flex-shrink:0"><g transform="{o["tr"]}" fill="{color}"><path d="{o["d"]}"></path></g></svg>'
def mark(color,w,uid=None,star=True):
    return _svg('mark',color,w=w)
ROOT=os.path.join(os.path.dirname(__file__),'..','project')
IMG_CROWD='/_blob/435441db9696fc0b743851d4a3290ad2'
IMG_BEAMS='/_blob/76b8aa085f0e99619eeafcda2ce0aed4'
IMG_NIGHT='/_blob/ab42e44980fb8ccf27ed33281a8cc2e7'
DEEP='#0E1512'; FOREST='#1F3A2F'; SAGE='#8E9A93'; CREAM='#EFECE5'; PAPER='#E7E4DC'; INK='#0F0F0F'
TXT='#F1EEE6'; MUTED='#A9B2AC'; MUTED_L='#5E6661'
FONT_LINK='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&amp;display=swap">'
_uid=[0]
def uid():
    _uid[0]+=1; return f'u{_uid[0]}'
def M(color,w,star=True):
    return mark(color,w,uid(),star)
def wordmark(color,size):
    return _svg('word',color,h=round(size*0.78),label='Authentix')
def caps(text,size,color,track=0.28,weight=500,extra=''):
    text=text.replace('|','\n')
    return f'<div style="font-size: {size}px; font-weight: {weight}; letter-spacing: {track}em; text-transform: uppercase; color: {color}; line-height: 1.75; white-space: pre-line{extra}">{text}</div>'
def dash(color,w=22,h=2):
    return f'<div style="width: {w}px; height: {h}px; background: {color}"></div>'
def page(title,w,h,bg,color,body,lang='en'):
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT_LINK}
<style>
body{{margin:0;font-family:Montserrat,'Helvetica Neue',Arial,sans-serif;background:{bg};color:{color}}}
p{{margin:0}}
button{{font-family:Montserrat,'Helvetica Neue',Arial,sans-serif}}
</style>
</helmet>
<div style="width: {w}px; height: {h}px; box-sizing: border-box; background: {bg}; color: {color}; position: relative; overflow: hidden; font-family: Montserrat, 'Helvetica Neue', Arial, sans-serif">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{}};
  }}
}}
</script>
</body>
</html>
'''
def write(name,html):
    open(os.path.join(ROOT,name),'w').write(html)

# ---------- icons (24 viewBox, stroke) ----------
def ico(paths,size,color,sw=1.5,extra=''):
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" aria-hidden="true" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" style="display:block;flex-shrink:0{extra}">{paths}</svg>'
I={
 'shield':'<path d="M12 3L19 6V11C19 15.5 16 19 12 21C8 19 5 15.5 5 11V6Z"></path><path d="M8.8 12L11 14.2L15.4 9.8"></path>',
 'ticket':'<g transform="rotate(-22 12 12)"><path d="M3 7.5H21V10.5A1.5 1.5 0 0 0 21 13.5V16.5H3V13.5A1.5 1.5 0 0 0 3 10.5Z"></path><path d="M15 8.5V15.5" stroke-dasharray="1.2 1.8"></path></g>',
 'globe':'<circle cx="12" cy="12" r="9"></circle><path d="M3 12H21"></path><ellipse cx="12" cy="12" rx="4" ry="9"></ellipse><path d="M4.5 7.5H19.5M4.5 16.5H19.5"></path>',
 'people':'<circle cx="9" cy="8" r="3.2"></circle><path d="M3.5 19.5C3.5 16.2 6 13.8 9 13.8S14.5 16.2 14.5 19.5"></path><circle cx="16.5" cy="9" r="2.6"></circle><path d="M15.8 13.7C18.6 13.9 20.5 16.2 20.5 19.2"></path>',
 'headset':'<path d="M4 14V12A8 8 0 0 1 20 12V14"></path><rect x="3" y="13" width="4" height="6" rx="1.5"></rect><rect x="17" y="13" width="4" height="6" rx="1.5"></rect><path d="M20 19C20 20.5 18.5 21.5 16 21.5H13.5"></path>',
 'percent':'<path d="M6 18L18 6"></path><circle cx="7" cy="7" r="2.2"></circle><circle cx="17" cy="17" r="2.2"></circle>',
 'star':'<path d="M12 3.5L14.6 9.1L20.6 9.7L16.1 13.7L17.4 19.7L12 16.6L6.6 19.7L7.9 13.7L3.4 9.7L9.4 9.1Z" fill="currentColor"></path>',
 'grid':'<rect x="4" y="4" width="16" height="16" rx="1"></rect><path d="M9.3 4V20M14.7 4V20M4 9.3H20M4 14.7H20"></path>',
 'reels':'<rect x="4" y="4" width="16" height="16" rx="3"></rect><path d="M10.5 9.5L14.5 12L10.5 14.5Z"></path>',
 'tagged':'<rect x="4" y="4" width="16" height="16" rx="2"></rect><circle cx="12" cy="10" r="2.5"></circle><path d="M7.5 17C8.3 15.2 10 14.2 12 14.2S15.7 15.2 16.5 17"></path>',
 'back':'<path d="M15 5L8 12L15 19"></path>',
 'dots':'<circle cx="5" cy="12" r="0.9" fill="currentColor"></circle><circle cx="12" cy="12" r="0.9" fill="currentColor"></circle><circle cx="19" cy="12" r="0.9" fill="currentColor"></circle>',
 'chev':'<path d="M7 10L12 15L17 10"></path>',
 'check':'<path d="M5 12.5L9.5 17L19 7.5"></path>',
 'x':'<path d="M6 6L18 18M18 6L6 18"></path>',
 'bolt':'<path d="M13 2L4 14H11L10 22L19 10H12Z"></path>',
}
def icon(name,size,color,sw=1.5):
    p=I[name]
    if name=='star':
        return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" aria-hidden="true" style="display:block;flex-shrink:0"><path d="M12 3.5L14.6 9.1L20.6 9.7L16.1 13.7L17.4 19.7L12 16.6L6.6 19.7L7.9 13.7L3.4 9.7L9.4 9.1Z" fill="{color}"></path></svg>'
    return ico(p,size,color,sw)

def photo(src,pos='center',extra=''):
    return f'<img src="{src}" alt="" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: cover; object-position: {pos}{extra}">'

def barcode(w,h,color,seed=3):
    r=random.Random(seed); x=0; rects=[]
    while x<w:
        bw=r.choice([1,1,2,2,3,4]); 
        rects.append(f'<rect x="{x}" y="0" width="{bw}" height="{h}" fill="{color}"></rect>'); x+=bw+r.choice([1,2,2,3])
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" aria-hidden="true" style="display:block">{"".join(rects)}</svg>'

def seal(size,color,text='AUTHENTIX · 100% TRUSTED · MY / SG &amp; BEYOND ·'):
    u=uid()
    inner=mark(color,200,u+'s')
    return (f'<svg viewBox="0 0 200 200" width="{size}" height="{size}" aria-hidden="true" style="display:block">'
      f'<defs><path id="arc{u}" d="M28,100 a72,72 0 1,1 144,0 a72,72 0 1,1 -144,0"></path></defs>'
      f'<circle cx="100" cy="100" r="94" fill="none" stroke="{color}" stroke-width="2"></circle>'
      f'<circle cx="100" cy="100" r="56" fill="none" stroke="{color}" stroke-width="1"></circle>'
      f'<text font-family="Montserrat, sans-serif" font-size="12.5" font-weight="600" fill="{color}"><textPath href="#arc{u}" textLength="444" lengthAdjust="spacing">{text}</textPath></text>'
      f'<g transform="translate(58 71.6) scale(0.42)">{inner}</g></svg>')

def vbarcode(w,h,color,seed=5):
    r=random.Random(seed); y=0; rects=[]
    while y<h:
        bh=r.choice([1,1,2,2,3,4]); rects.append(f'<rect x="0" y="{y}" width="{w}" height="{bh}" fill="{color}"></rect>'); y+=bh+r.choice([1,2,2,3])
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" aria-hidden="true" style="display:block;flex-shrink:0">{"".join(rects)}</svg>'
