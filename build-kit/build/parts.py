from common import *

def hero(W,H,scale=1.0):
    s=scale
    usps=[('shield','100%|TRUSTED'),('ticket','CONCERT|TICKETS'),('globe','MY / SG|&amp; INTERNATIONAL'),('people','INTERNAL ORDERS|&amp; DISCOUNTED'),('headset','BUY FOR YOU|SERVICES')]
    items=[]
    for i,(ic,lab) in enumerate(usps):
        border='' if i==0 else f'border-left: 1px solid rgba(241,238,230,0.35);'
        items.append(f'<div style="display: flex; align-items: center; justify-content: center; gap: {round(22*s)}px; flex-grow: 1; flex-basis: 0; {border}">{icon(ic,round(44*s),TXT,1.3)}{caps(lab,round(14*s),TXT,0.16,500)}</div>')
    return f'''<div style="position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; background: {DEEP}; overflow: hidden">
{photo(IMG_CROWD,'center 60%','; opacity: 0.85')}
<div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(14,21,18,0.55) 0%, rgba(14,21,18,0.35) 45%, rgba(14,21,18,0.88) 82%, {DEEP} 100%)"></div>
<div style="position: absolute; left: {round(100*s)}px; top: {round(68*s)}px; display: flex; flex-direction: column; gap: {round(10*s)}px">{caps('MALAYSIA|SINGAPORE|AND BEYOND',round(14*s),TXT,0.22)}{dash(TXT,round(22*s),max(1,round(2*s)))}</div>
<div style="position: absolute; right: {round(100*s)}px; top: {round(68*s)}px; display: flex; flex-direction: column; gap: {round(10*s)}px; align-items: flex-end; text-align: right">{caps('CONCERTS|PEOPLE|CLOSER',round(14*s),TXT,0.22)}{dash(TXT,round(22*s),max(1,round(2*s)))}</div>
<div style="position: absolute; left: 0; right: 0; top: {round(58*s)}px; display: flex; flex-direction: column; align-items: center; gap: {round(14*s)}px">
{M(TXT,round(250*s))}
{wordmark(TXT,round(84*s))}
<div style="margin-top: {round(18*s)}px; text-align: center">{caps('MORE THAN TICKETS|REAL EXPERIENCES',round(17*s),TXT,0.42,400)}</div>
</div>
<div style="position: absolute; left: {round(40*s)}px; right: {round(40*s)}px; top: {round(H-104*s)}px; height: {round(76*s)}px; display: flex">
{''.join(items)}
</div>
</div>'''

def phone_profile(w, dark_status=False):
    # w = phone outer width; returns html of phone at natural height 2.05*w
    k=w/480
    def px(v): return round(v*k)
    h=px(1000)
    hl=[('ticket','Tickets'),('percent','Deals'),('globe','MY / SG'),('star','Reviews'),('headset','Help')]
    hls=''.join(f'<div style="display: flex; flex-direction: column; align-items: center; gap: {px(8)}px; width: {px(70)}px"><div style="width: {px(64)}px; height: {px(64)}px; border-radius: 50%; background: #E9E8E4; display: flex; align-items: center; justify-content: center">{icon(ic,px(28),"#1A1A1A",1.7)}</div><span style="font-size: {px(12)}px; color: #1A1A1A">{lab}</span></div>' for ic,lab in hl)
    def tile_txt(txt,bg=FOREST):
        return f'<div style="aspect-ratio: 1 / 1.25; background: {bg}; position: relative; display: flex; flex-direction: column; justify-content: center; padding: 0 {px(14)}px; gap: {px(6)}px">{caps(txt,px(11),TXT,0.2,600)}{dash(TXT,px(12),1)}</div>'
    def tile_img(src,pos='center'):
        return f'<div style="aspect-ratio: 1 / 1.25; position: relative; overflow: hidden; background: {DEEP}">{photo(src,pos)}</div>'
    grid=(tile_txt('GOOD|MUSIC|BRIGHTER|PEOPLE')+tile_img(IMG_BEAMS,'center 30%')+tile_txt('MORE|THAN|TICKETS',DEEP)
          +tile_img(IMG_NIGHT)+tile_img(IMG_CROWD,'30% center')+tile_img(IMG_BEAMS,'center 80%'))
    return f'''<div style="width: {w}px; height: {h}px; border-radius: {px(70)}px; background: #111111; padding: {px(14)}px; box-sizing: border-box; box-shadow: 0 {px(30)}px {px(60)}px rgba(0,0,0,0.25)">
<div style="width: 100%; height: 100%; border-radius: {px(58)}px; background: #FFFFFF; overflow: hidden; position: relative; color: #111111">
<div style="position: absolute; left: 50%; top: {px(12)}px; width: {px(116)}px; height: {px(34)}px; margin-left: -{px(58)}px; border-radius: {px(20)}px; background: #0A0A0A"></div>
<div style="display: flex; justify-content: space-between; align-items: center; padding: {px(18)}px {px(34)}px 0; height: {px(30)}px">
<span style="font-size: {px(16)}px; font-weight: 600">9:41</span>
<div style="display: flex; gap: {px(6)}px; align-items: flex-end"><span style="display:block;width:{px(3)}px;height:{px(6)}px;background:#111"></span><span style="display:block;width:{px(3)}px;height:{px(8)}px;background:#111"></span><span style="display:block;width:{px(3)}px;height:{px(10)}px;background:#111"></span><span style="display:block;width:{px(3)}px;height:{px(12)}px;background:#111"></span><span style="display:block;width:{px(24)}px;height:{px(12)}px;border:1.5px solid #111;border-radius:{px(3)}px;box-sizing:border-box;padding:1px"><span style="display:block;width:80%;height:100%;background:#111;border-radius:1px"></span></span></div>
</div>
<div style="display: flex; justify-content: space-between; align-items: center; padding: {px(22)}px {px(22)}px {px(10)}px">{icon('back',px(26),'#111',2)}<span style="font-size: {px(19)}px; font-weight: 600">authentix.my</span>{icon('dots',px(26),'#111',2)}</div>
<div style="display: flex; align-items: center; gap: {px(26)}px; padding: {px(8)}px {px(22)}px">
<div style="width: {px(120)}px; height: {px(120)}px; border-radius: 50%; background: {FOREST}; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{M(TXT,px(78))}</div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: {px(6)}px; flex-grow: 1; text-align: center">
<div><div style="font-size: {px(18)}px; font-weight: 700">432</div><div style="font-size: {px(13)}px">Posts</div></div>
<div><div style="font-size: {px(18)}px; font-weight: 700">12.6K</div><div style="font-size: {px(13)}px">Followers</div></div>
<div><div style="font-size: {px(18)}px; font-weight: 700">&#8203;</div><div style="font-size: {px(13)}px">Following</div></div>
</div></div>
<div style="padding: {px(10)}px {px(22)}px 0; display: flex; flex-direction: column; gap: {px(3)}px; font-size: {px(13.5)}px; line-height: 1.4">
<div style="font-weight: 700; font-size: {px(15)}px">Authentix</div>
<div style="color: #444">Concert Tickets &#160;|&#160; MY / SG &amp; Beyond</div>
<div style="color: #444">Internal Orders &#160;|&#160; Discounted &#160;|&#160; Buy For You</div>
<div>More Than Tickets, Real Experiences.</div>
</div>
<div style="display: flex; gap: {px(8)}px; padding: {px(16)}px {px(22)}px">
<button type="button" style="flex-grow: 1; height: {px(40)}px; border: 1px solid #CFCFCF; background: #FFFFFF; border-radius: {px(8)}px; font-size: {px(14)}px; font-weight: 600; color: #111">Following</button>
<button type="button" style="flex-grow: 1; height: {px(40)}px; border: 1px solid #CFCFCF; background: #FFFFFF; border-radius: {px(8)}px; font-size: {px(14)}px; font-weight: 600; color: #111">Message</button>
<button type="button" aria-label="More" style="width: {px(40)}px; height: {px(40)}px; border: 1px solid #CFCFCF; background: #FFFFFF; border-radius: {px(8)}px; display: flex; align-items: center; justify-content: center">{icon('chev',px(18),'#111',2)}</button>
</div>
<div style="display: flex; justify-content: space-between; padding: {px(2)}px {px(18)}px {px(16)}px">{hls}</div>
<div style="display: flex; justify-content: space-around; padding: {px(8)}px 0; border-top: 1px solid #EEE"><div style="border-bottom: 2px solid #111; padding-bottom: {px(8)}px">{icon('grid',px(24),'#111',1.6)}</div><div>{icon('reels',px(24),'#888',1.6)}</div><div>{icon('tagged',px(24),'#888',1.6)}</div></div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2px">{grid}</div>
</div></div>'''

def app_tile(size,bg,fg,shadow=True,radius=None):
    r=radius if radius is not None else round(size*0.16)
    sh=f'box-shadow: 0 {round(size*0.04)}px {round(size*0.1)}px rgba(0,0,0,0.12);' if shadow else ''
    return f'<div style="width: {size}px; height: {size}px; border-radius: {r}px; background: {bg}; display: flex; align-items: center; justify-content: center; {sh} flex-shrink: 0">{M(fg,round(size*0.62))}</div>'

def ticket(w, board_bg):
    k=w/1400
    def px(v): return round(v*k)
    h=px(520); stub=px(300); main=w-stub-px(8)
    notch=px(44)
    return f'''<div style="width: {w}px; height: {h}px; position: relative; display: flex; gap: {px(8)}px; filter: drop-shadow(0 {px(18)}px {px(30)}px rgba(0,0,0,0.25))">
<div style="width: {main}px; height: {h}px; position: relative; overflow: hidden; border-radius: {px(22)}px; background: {DEEP}">
{photo(IMG_CROWD,'center 55%','; opacity: 0.6')}
<div style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(14,21,18,0.85) 0%, rgba(14,21,18,0.35) 100%)"></div>
<div style="position: absolute; left: -{notch//2}px; top: {h//2-notch//2}px; width: {notch}px; height: {notch}px; border-radius: 50%; background: {board_bg}"></div>
<div style="position: absolute; left: {px(90)}px; top: 0; bottom: 0; display: flex; align-items: center; gap: {px(34)}px">
{M(TXT,px(170))}
<div style="display: flex; flex-direction: column; gap: {px(22)}px">{wordmark(TXT,px(92))}{caps('CONCERT TICKETS|MY / SG &amp; BEYOND',px(20),TXT,0.3,500)}</div>
</div>
</div>
<div style="width: {stub}px; height: {h}px; position: relative; overflow: hidden; border-radius: {px(22)}px; background: #151A17; display: flex; align-items: center; justify-content: space-between; padding: 0 {px(46)}px 0 {px(56)}px; box-sizing: border-box">
<div style="position: absolute; right: -{notch//2}px; top: {h//2-notch//2}px; width: {notch}px; height: {notch}px; border-radius: 50%; background: {board_bg}"></div>
<div style="display: flex; flex-direction: column; gap: {px(16)}px">{caps('LIVE|MUSIC|REAL|PEOPLE',px(20),TXT,0.26,500)}{dash(TXT,px(24),max(1,px(3)))}</div>
{vbarcode(px(44),px(360),TXT)}
</div>
</div>'''

def lanyard_card(w):
    k=w/560
    def px(v): return round(v*k)
    h=px(800)
    return f'''<div style="width: {w}px; height: {h}px; border-radius: {px(40)}px; background: linear-gradient(160deg, #26473A 0%, {FOREST} 55%, #183026 100%); position: relative; box-shadow: 0 {px(30)}px {px(60)}px rgba(0,0,0,0.3); display: flex; flex-direction: column; align-items: center">
<div style="margin-top: {px(40)}px; width: {px(120)}px; height: {px(22)}px; border-radius: {px(11)}px; background: {PAPER}; box-shadow: inset 0 {px(3)}px {px(6)}px rgba(0,0,0,0.3)"></div>
<div style="margin-top: {px(150)}px">{M(TXT,px(220))}</div>
<div style="margin-top: {px(28)}px">{wordmark(TXT,px(64))}</div>
<div style="position: absolute; left: {px(56)}px; bottom: {px(70)}px; display: flex; flex-direction: column; gap: {px(10)}px">{caps('CREATING|MORE LIVE|MOMENTS',px(16),TXT,0.26,500)}</div>
</div>'''

def post_trust(w):
    k=w/1080
    def px(v): return round(v*k)
    return f'''<div style="width: {w}px; height: {px(1350)}px; position: relative; overflow: hidden; background: {DEEP}">
{photo(IMG_BEAMS,'center 40%')}
<div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(14,21,18,0.7) 0%, rgba(14,21,18,0.1) 45%, rgba(14,21,18,0.5) 100%)"></div>
<div style="position: absolute; left: {px(96)}px; top: {px(120)}px; display: flex; flex-direction: column; gap: {px(34)}px">{caps('DIFFERENT|SHOWS|SAME TRUST',px(58),TXT,0.26,600)}{dash(TXT,px(60),px(4))}</div>
</div>'''

def post_real(w):
    k=w/1080
    def px(v): return round(v*k)
    return f'''<div style="width: {w}px; height: {px(1350)}px; position: relative; overflow: hidden; background: {CREAM}">
<div style="position: absolute; right: -{px(140)}px; top: {px(260)}px; opacity: 0.07">{M(FOREST,px(900),False)}</div>
<div style="position: absolute; left: {px(96)}px; top: {px(110)}px; display: flex; flex-direction: column; gap: {px(10)}px">{M(FOREST,px(110))}{wordmark(FOREST,px(46))}</div>
<div style="position: absolute; left: {px(96)}px; top: {px(760)}px; display: flex; flex-direction: column; gap: {px(34)}px">{caps('REAL FANS|REAL SUPPORT|REAL EXPERIENCES',px(46),FOREST,0.24,500)}{dash(FOREST,px(60),px(4))}</div>
<div style="position: absolute; left: {px(96)}px; right: {px(96)}px; bottom: {px(96)}px; display: flex; gap: {px(40)}px">{caps('MALAYSIA',px(24),FOREST,0.3,500)}{caps('SINGAPORE',px(24),FOREST,0.3,500)}{caps('AND BEYOND',px(24),FOREST,0.3,500)}</div>
</div>'''

def post_ticket(w):
    k=w/1080
    def px(v): return round(v*k)
    return f'''<div style="width: {w}px; height: {px(1350)}px; position: relative; overflow: hidden; background: {DEEP}">
{photo(IMG_NIGHT,'center 70%')}
<div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(14,21,18,0.85) 0%, rgba(14,21,18,0.2) 55%, rgba(14,21,18,0.75) 100%)"></div>
<div style="position: absolute; left: {px(96)}px; top: {px(120)}px; display: flex; flex-direction: column; gap: {px(34)}px">{caps('IT|STARTS|WITH|A TICKET',px(58),TXT,0.26,600)}{dash(TXT,px(60),px(4))}</div>
<div style="position: absolute; left: 0; right: 0; bottom: {px(96)}px; display: flex; justify-content: center; align-items: center; gap: {px(16)}px">{M(TXT,px(74))}{wordmark(TXT,px(40))}</div>
</div>'''
