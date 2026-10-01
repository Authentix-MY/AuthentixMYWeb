from parts import *
def h2(t,c='#111'): return f'<div style="font-size: 36px; font-weight: 600; color: {c}; letter-spacing: -0.01em">{t}</div>'
def tag(t,c=MUTED_L): return caps(t,13,c,0.24)
def note(n,t): return f'<div style="display: flex; gap: 14px; font-size: 16px; line-height: 1.55; color: #2A2F2C"><span style="font-weight: 700; color: {FOREST}; width: 26px; flex-shrink: 0">{n}</span><span>{t}</span></div>'

# ---------- LOGO ----------
body=f'''<div style="position: absolute; inset: 0; padding: 80px 96px; box-sizing: border-box; display: flex; flex-direction: column; gap: 44px">
<div style="display: flex; justify-content: space-between; align-items: baseline">{h2('Logo system')}{tag('02 · IDENTITY')}</div>
<div style="display: grid; grid-template-columns: 1.7fr 1fr; gap: 28px">
<div style="height: 560px; border-radius: 28px; background: {DEEP}; position: relative; overflow: hidden; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 18px">
{photo(IMG_CROWD,'center 70%','; opacity: 0.35')}
<div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 18px">{M(TXT,240)}{wordmark(TXT,80)}<div style="margin-top: 14px; text-align: center">{caps('MORE THAN TICKETS|REAL EXPERIENCES',15,TXT,0.42,400)}</div></div>
</div>
<div style="display: flex; flex-direction: column; gap: 18px; padding-top: 6px">
{tag('PRIMARY LOCKUP · STACKED',FOREST)}
<p style="font-size: 19px; line-height: 1.6; color: #2A2F2C">A bold <strong>A</strong> circled by an <strong>orbit</strong>, with a <strong>sparkle</strong> at its shoulder. The fan’s initial, the stage peak, and the moment the lights go down.</p>
{note('01','A — Authentix, and a stage peak. Slim left leg, heavy right leg, no crossbar.')}
{note('02','Orbit — MY, SG and beyond. A thin tilted ring that wraps the A below its middle.')}
{note('03','Sparkle — the “real experience”. Keep it top-right; never recolour on its own.')}
{note('04','Wordmark — custom lettering; its A carries the orbit swoosh. Always use the artwork, never retype it.')}
{note('05','Clear space = the sparkle’s height on all sides. Minimum: mark 24 px, stacked lockup 120 px wide.')}
</div>
</div>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px">
<div style="display: flex; flex-direction: column; gap: 12px"><div style="height: 200px; border-radius: 22px; background: {CREAM}; display: flex; align-items: center; justify-content: center; gap: 16px; box-shadow: 0 0 0 1px rgba(0,0,0,0.06)">{M(FOREST,62)}{wordmark(FOREST,32)}</div>{tag('HORIZONTAL · ON CREAM')}</div>
<div style="display: flex; flex-direction: column; gap: 12px"><div style="height: 200px; border-radius: 22px; background: {FOREST}; display: flex; align-items: center; justify-content: center">{M(TXT,130)}</div>{tag('MARK · ON FOREST')}</div>
<div style="display: flex; flex-direction: column; gap: 12px"><div style="height: 200px; border-radius: 22px; background: {INK}; display: flex; align-items: center; justify-content: center">{wordmark(TXT,50)}</div>{tag('WORDMARK · ON BLACK')}</div>
<div style="display: flex; flex-direction: column; gap: 12px"><div style="height: 200px; border-radius: 22px; background: {PAPER}; box-shadow: inset 0 0 0 1px #CFCBC2; display: flex; align-items: center; justify-content: center">{seal(160,FOREST)}</div>{tag('TRUST SEAL · PROOF &amp; RECEIPTS')}</div>
</div>
<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 20px; align-items: end">
<div style="display: flex; flex-direction: column; gap: 12px; align-items: flex-start"><div style="width: 150px; height: 150px; border-radius: 50%; background: {FOREST}; display: flex; align-items: center; justify-content: center">{M(TXT,96)}</div>{tag('IG PROFILE PICTURE')}</div>
<div style="display: flex; flex-direction: column; gap: 12px; align-items: flex-start"><div style="display: flex; gap: 12px; align-items: flex-end">{app_tile(96,FOREST,TXT,False)}{app_tile(48,FOREST,TXT,False)}{app_tile(24,FOREST,TXT,False,5)}</div>{tag('APP ICON / FAVICON')}</div>
<div style="grid-column: span 3; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">
<div style="border-top: 2px solid {FOREST}; padding-top: 12px; font-size: 15px; line-height: 1.5; color: #2A2F2C"><strong>Don’t</strong> add glow, gradients or outlines to the mark.</div>
<div style="border-top: 2px solid {FOREST}; padding-top: 12px; font-size: 15px; line-height: 1.5; color: #2A2F2C"><strong>Don’t</strong> thicken the orbit, move the sparkle, or rebuild the wordmark in a font.</div>
<div style="border-top: 2px solid {FOREST}; padding-top: 12px; font-size: 15px; line-height: 1.5; color: #2A2F2C"><strong>Don’t</strong> lock up with artist, promoter or venue logos — it implies partnership.</div>
</div>
</div>
</div>'''
write('Logo.dc.html',page('Authentix — Logo system',1440,1340,PAPER,'#111',body))

# ---------- PALETTE ----------
sw=[('Forest',FOREST,'31 58 47','25%','App icon, PFP, lanyard, feature tiles',TXT),
    ('Deep Night',DEEP,'14 21 18','35%','Hero bands, photo overlays, dark posts',TXT),
    ('Sage',SAGE,'142 154 147','5%','Dividers, secondary icons on dark only',INK),
    ('Cream',CREAM,'239 236 229','20%','Type on dark, light posts, app tile',FOREST),
    ('Paper',PAPER,'231 228 220','10%','Board and print backgrounds',FOREST),
    ('Ink',INK,'15 15 15','5%','Black tile, barcodes, phone',TXT)]
cards=''.join(f'''<div style="display: flex; flex-direction: column; gap: 12px">
<div style="height: 200px; border-radius: 20px; background: {hx}; box-shadow: inset 0 0 0 1px rgba(0,0,0,0.08); display: flex; align-items: flex-end; padding: 18px; box-sizing: border-box"><span style="font-size: 30px; font-weight: 700; color: {fg}">{pct}</span></div>
<div style="font-size: 19px; font-weight: 600">{n}</div>
<div style="font-size: 14px; color: {MUTED_L}; line-height: 1.6; font-variant-numeric: tabular-nums">{hx}<br>RGB {rgb}</div>
<div style="font-size: 14px; color: #2A2F2C; line-height: 1.5">{use}</div></div>''' for n,hx,rgb,pct,use,fg in sw)
bar=''.join(f'<div style="width: {pct}; background: {hx}"></div>' for n,hx,rgb,pct,use,fg in [sw[1],sw[0],sw[3],sw[4],sw[2],sw[5]])
pairs=[('Cream on Deep Night',TXT,DEEP,'16.0'),('Cream on Forest',TXT,FOREST,'10.6'),('Forest on Cream',FOREST,CREAM,'10.4'),('Sage on Deep Night',SAGE,DEEP,'6.3'),('Grey text on Paper',MUTED_L,PAPER,'4.7')]
pr=''.join(f'<div style="background: {bg}; border-radius: 12px; padding: 14px 16px; display: flex; justify-content: space-between; align-items: center; box-shadow: inset 0 0 0 1px rgba(0,0,0,0.06)"><span style="color: {fg}; font-weight: 600; font-size: 15px">{n}</span><span style="color: {fg}; font-size: 14px; font-variant-numeric: tabular-nums">{r} : 1</span></div>' for n,fg,bg,r in pairs)
body=f'''<div style="position: absolute; inset: 0; padding: 80px 96px; box-sizing: border-box; display: flex; flex-direction: column; gap: 40px">
<div style="display: flex; justify-content: space-between; align-items: baseline">{h2('Colour, type &amp; photography')}{tag('02 · IDENTITY')}</div>
<div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 16px">{cards}</div>
<div style="display: flex; height: 22px; border-radius: 6px; overflow: hidden">{bar}</div>
<div style="display: grid; grid-template-columns: 1.1fr 1fr; gap: 28px">
<div style="background: {DEEP}; border-radius: 24px; padding: 36px 40px; color: {TXT}; display: flex; flex-direction: column; gap: 20px">
{caps('TYPOGRAPHY · MONTSERRAT',13,SAGE,0.24)}
<div style="display: flex; align-items: flex-end; gap: 24px">{wordmark(TXT,64)}<span style="font-size: 14px; color: {MUTED}">Wordmark is artwork · Montserrat SemiBold 600 for headlines</span></div>
<div style="display: flex; flex-direction: column; gap: 8px">{caps('DIFFERENT SHOWS|SAME TRUST',26,TXT,0.26,600)}<span style="font-size: 14px; color: {MUTED}">SemiBold caps, +26% tracking · post statements (58 px on 1080)</span></div>
<div style="display: flex; flex-direction: column; gap: 8px">{caps('MALAYSIA · SINGAPORE · AND BEYOND',15,TXT,0.3,500)}<span style="font-size: 14px; color: {MUTED}">Medium caps, +28–42% tracking · labels, taglines</span></div>
<div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 20px; font-weight: 400; line-height: 1.5">Concert Tickets | MY / SG &amp; Beyond. More than tickets, real experiences.</span><span style="font-size: 14px; color: {MUTED}">Regular 400 · captions, prices, body (tabular figures for prices)</span></div>
<div style="display: flex; gap: 10px; align-items: center">{dash(TXT,22,2)}<span style="font-size: 14px; color: {MUTED}">The short dash closes every caps statement.</span></div>
</div>
<div style="display: flex; flex-direction: column; gap: 20px">
<div style="display: flex; flex-direction: column; gap: 10px">{caps('TESTED CONTRAST (WCAG)',13,MUTED_L,0.24)}{pr}<div style="font-size: 14px; color: {MUTED_L}; line-height: 1.5">Sage on Paper is 2.3 : 1 — decorative only, never text.</div></div>
<div style="display: grid; grid-template-columns: 150px 1fr; gap: 20px; align-items: center">
<div style="width: 150px; height: 150px; border-radius: 16px; overflow: hidden; position: relative; background: {DEEP}">{photo(IMG_BEAMS)}</div>
<div style="display: flex; flex-direction: column; gap: 8px">{caps('PHOTOGRAPHY',13,MUTED_L,0.24)}<div style="font-size: 15px; line-height: 1.55; color: #2A2F2C">Black-and-white crowds, hands and stage light with a faint green tint. No artist faces or tour art. Keep the top third dark for type.</div></div>
</div>
</div>
</div>
</div>'''
write('Palette.dc.html',page('Authentix — Colour and type',1440,1240,PAPER,'#111',body))
print('identity ok')
