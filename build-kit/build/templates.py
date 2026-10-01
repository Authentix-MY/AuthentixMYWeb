from parts import *
def lock(c,m=64,w=34): return f'<div style="display: flex; align-items: center; gap: 14px">{M(c,m)}{wordmark(c,w)}</div>'

# ---------- T1 Ticket Drop ----------
rows=[('VIP','[TIER]','[000]','[000]','Few left',TXT,True),('CAT 1','','[000]','[000]','Available',TXT,False),('CAT 2','','[000]','[000]','Available',TXT,False),('CAT 3','','[000]','[000]','Sold out',SAGE,False)]
tr=''
for i,(c,t,fv,ai,st,col,vip) in enumerate(rows):
    last=(i==len(rows)-1)
    name=f'<span style="display: flex; align-items: center; gap: 12px"><span style="font-size: 16px; font-weight: 600; letter-spacing: 0.2em; border: 1.5px solid {TXT}; padding: 4px 10px; border-radius: 6px">VIP</span>{t}</span>' if vip else c
    strike='; text-decoration: line-through' if st=='Sold out' else ''
    tr+=f'<div style="display: grid; grid-template-columns: 1.2fr 1fr 1fr 1fr; gap: 16px; padding: 22px 36px; font-size: 30px; font-variant-numeric: tabular-nums; align-items: center; color: {col}; {"" if last else "border-bottom: 1px solid rgba(241,238,230,0.14)"}"><span style="font-weight: 600">{name}</span><span style="opacity: 0.75">{fv}</span><span style="font-weight: 700{strike}">{ai}</span><span style="font-size: 22px; font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase">{st}</span></div>'
body=f'''<div style="position: absolute; left: 0; top: 0; width: 1080px; height: 640px; overflow: hidden">{photo(IMG_BEAMS,'center 35%')}<div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(14,21,18,0.55) 0%, rgba(14,21,18,0.25) 40%, {DEEP} 100%)"></div></div>
<div style="position: absolute; inset: 0; padding: 72px; box-sizing: border-box; display: flex; flex-direction: column; gap: 34px">
<div style="display: flex; justify-content: space-between; align-items: center">{lock(TXT)}{caps('TICKET DROP · 07',20,TXT,0.3)}</div>
<div style="display: flex; flex-direction: column; gap: 20px; margin-top: 120px">
<div style="display: flex; align-items: center; gap: 16px">{dash(TXT,40,3)}{caps('AVAILABLE NOW',24,TXT,0.34,600)}</div>
<div style="font-size: 104px; font-weight: 700; letter-spacing: -0.02em; line-height: 1">[ARTIST]</div>
{caps('[TOUR NAME] WORLD TOUR',26,TXT,0.3,500)}
</div>
<div style="display: flex; height: 170px; gap: 8px">
<div style="flex-grow: 1; border-radius: 22px; background: {FOREST}; position: relative; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; padding: 0 40px; align-items: center">
<div style="position: absolute; left: -20px; top: 65px; width: 40px; height: 40px; border-radius: 50%; background: {DEEP}"></div>
<div style="display: flex; flex-direction: column; gap: 10px">{caps('DATE',16,SAGE,0.3)}<span style="font-size: 30px; font-weight: 600; white-space: nowrap">[DD MMM]</span></div>
<div style="display: flex; flex-direction: column; gap: 10px">{caps('CITY',16,SAGE,0.3)}<span style="font-size: 30px; font-weight: 600; white-space: nowrap">[KL / SG]</span></div>
<div style="display: flex; flex-direction: column; gap: 10px">{caps('VENUE',16,SAGE,0.3)}<span style="font-size: 30px; font-weight: 600; white-space: nowrap">[VENUE]</span></div>
</div>
<div style="width: 250px; border-radius: 22px; background: {CREAM}; color: {FOREST}; position: relative; display: flex; flex-direction: column; justify-content: center; padding: 0 40px; gap: 8px">
<div style="position: absolute; right: -20px; top: 65px; width: 40px; height: 40px; border-radius: 50%; background: {DEEP}"></div>
{caps('FROM',16,FOREST,0.3)}<span style="font-size: 40px; font-weight: 700; font-variant-numeric: tabular-nums">[RM ___]</span></div>
</div>
<div style="border-radius: 22px; background: #151D19; overflow: hidden">
<div style="display: grid; grid-template-columns: 1.2fr 1fr 1fr 1fr; gap: 16px; padding: 20px 36px; border-bottom: 1px solid rgba(241,238,230,0.14)">{caps('CATEGORY',16,SAGE,0.24)}{caps('FACE VALUE',16,SAGE,0.24)}{caps('ALL-IN',16,SAGE,0.24)}{caps('STATUS',16,SAGE,0.24)}</div>
{tr}</div>
<div style="display: flex; justify-content: space-between; align-items: center; gap: 28px; margin-top: auto">
<div style="background: {CREAM}; color: {FOREST}; border-radius: 999px; padding: 22px 34px; font-size: 26px; font-weight: 600; white-space: nowrap">DM “DROP” to reserve</div>
<div style="font-size: 20px; line-height: 1.5; color: {MUTED}; text-align: right">Official e-ticket transfer · not secured = full refund.<br>Independent seller, not affiliated with the artist or organiser.</div>
</div></div>'''
write('TicketDrop.dc.html',page('Authentix — Ticket Drop post',1080,1350,DEEP,TXT,body))

# ---------- T2 Proof story ----------
wm=''.join(f'<div style="font-size: 24px; font-weight: 600; white-space: nowrap; letter-spacing: 0.2em">AUTHENTIX · AX-[0000] · AUTHENTIX · AX-[0000] · AUTHENTIX · AX-[0000]</div>' for _ in range(13))
def row(k,v,bar=None,mono=False,accent=False):
    val=f'<span style="display: block; width: {bar}px; height: 32px; background: {INK}; border-radius: 4px"></span>' if bar else f'<span style="font-weight: {700 if accent else 600}; color: {FOREST if accent else INK}; font-variant-numeric: tabular-nums">{v}</span>'
    return f'<div style="display: flex; align-items: center; gap: 20px"><span style="width: 220px; color: {MUTED_L}">{k}</span>{val}</div>'
body=f'''{photo(IMG_NIGHT,'center 80%','; opacity: 0.55')}
<div style="position: absolute; inset: 0; background: linear-gradient(180deg, {DEEP} 0%, rgba(14,21,18,0.7) 40%, rgba(14,21,18,0.92) 100%)"></div>
<div style="position: absolute; inset: 0; padding: 150px 80px 290px; box-sizing: border-box; display: flex; flex-direction: column; align-items: center; gap: 44px">
{lock(TXT,54,30)}
<div style="display: flex; flex-direction: column; align-items: center; gap: 18px">
<div style="font-size: 120px; font-weight: 700; letter-spacing: 0.04em; line-height: 1">SECURED</div>
<div style="display: flex; align-items: center; gap: 16px">{dash(TXT,30,2)}{caps('ORDER AX-[0000] · [DD MMM] · [HH:MM] SGT',22,TXT,0.2)}{dash(TXT,30,2)}</div>
</div>
<div style="width: 820px; height: 800px; flex-shrink: 0; border-radius: 30px; background: {CREAM}; color: {INK}; position: relative; overflow: hidden; box-sizing: border-box; padding: 56px; display: flex; flex-direction: column; gap: 24px">
<div style="position: absolute; left: -220px; top: -120px; width: 1500px; transform: rotate(-24deg); display: flex; flex-direction: column; gap: 44px; opacity: 0.08; color: {FOREST}">{wm}</div>
<div style="display: flex; justify-content: space-between; align-items: center; position: relative"><span style="font-size: 34px; font-weight: 700">Order confirmed</span><span style="font-size: 16px; letter-spacing: 0.2em; color: {MUTED_L}; border: 1.5px dashed {MUTED_L}; padding: 6px 12px; border-radius: 8px">SCREENSHOT AREA</span></div>
<div style="display: flex; flex-direction: column; gap: 22px; position: relative; font-size: 28px">
{row('Name','',360)}{row('Email / phone','',420)}{row('Booking ref','•••• •••• [LAST 4]')}
<div style="height: 1px; background: #CFCBC2"></div>
{row('Event','[ARTIST] — [CITY]')}{row('Category','CAT 1 · × 2 · side-by-side')}{row('Queue no.','#[000,000] → secured in [MM:SS]',accent=True)}
</div>
<div style="position: absolute; right: 44px; bottom: 44px">{seal(220,FOREST)}</div>
</div>
<div style="display: flex; gap: 14px; justify-content: center">
<span style="font-size: 17px; letter-spacing: 0.12em; white-space: nowrap; text-transform: uppercase; padding: 14px 22px; border-radius: 999px; border: 1.5px solid rgba(241,238,230,0.4)">Hidden: name · contact · full ref</span>
<span style="font-size: 17px; letter-spacing: 0.12em; white-space: nowrap; text-transform: uppercase; padding: 14px 22px; border-radius: 999px; background: {CREAM}; color: {FOREST}; font-weight: 600">Shown: event · cat · queue</span>
</div>
<div style="display: flex; flex-direction: column; align-items: center; gap: 12px; margin-top: auto">
<span style="font-size: 32px; font-weight: 600">Next drop: [ARTIST] · [DATE]</span>
<span style="font-size: 24px; color: {MUTED}">DM “BUY” for our Buy For You service</span>
</div></div>'''
write('ProofStory.dc.html',page('Authentix — Secured proof story',1080,1920,DEEP,TXT,body))

# ---------- T3 Buy For You ----------
steps=[('01','Tell us the show','Event, date, category and quantity — DM or WhatsApp.'),
       ('02','Get a written, all-in quote','Face value + service fee, itemised. No surprises later.'),
       ('03','Pay &amp; get your Order ID','Full payment to our registered business account only.'),
       ('04','Drop day: we queue for you','Live updates in your chat while we’re in the queue.'),
       ('05','Secured → official e-ticket','Not secured? Full refund within [X] working days.')]
st=''
for n,t,d in steps:
    circ=f'background: {FOREST}; color: {TXT}' if n!='05' else f'background: {CREAM}; color: {FOREST}; box-shadow: inset 0 0 0 2px {FOREST}'
    st+=f'<div style="display: flex; gap: 30px; align-items: flex-start; padding: 14px 0; position: relative"><div style="width: 72px; height: 72px; flex-shrink: 0; border-radius: 50%; {circ}; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 600; letter-spacing: 0.06em">{n}</div><div style="display: flex; flex-direction: column; gap: 6px; padding-top: 4px"><span style="font-size: 33px; font-weight: 600">{t}</span><span style="font-size: 25px; color: {MUTED_L}; line-height: 1.4">{d}</span></div></div>'
body=f'''<div style="position: absolute; right: -170px; top: 150px; opacity: 0.06">{M(FOREST,760,False)}</div>
<div style="position: absolute; inset: 0; padding: 72px; box-sizing: border-box; display: flex; flex-direction: column; gap: 36px; color: {FOREST}">
<div style="display: flex; justify-content: space-between; align-items: center">{lock(FOREST)}<div style="display: flex; align-items: center; gap: 12px">{icon('headset',30,FOREST,1.6)}{caps('BUY FOR YOU',20,FOREST,0.3,600)}</div></div>
<div style="display: flex; flex-direction: column; gap: 22px">
{caps('YOU RELAX.|WE QUEUE.',64,FOREST,0.16,600)}
{dash(FOREST,60,4)}
<div style="font-size: 28px; color: #2A2F2C; line-height: 1.4">Drop-day help for shows that sell out in minutes. MY, SG &amp; beyond.</div>
</div>
<div style="display: flex; flex-direction: column; position: relative">
<div style="position: absolute; left: 35px; top: 40px; bottom: 40px; width: 2px; background: #CFCBC2"></div>{st}</div>
<div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 32px; margin-top: auto; border-top: 1px solid #CFCBC2; padding-top: 26px">
<div style="font-size: 21px; color: {MUTED_L}; line-height: 1.5; max-width: 560px">Min. 2 tickets side-by-side. Seats are assigned by the organiser — preferred zone noted, not guaranteed.</div>
<div style="background: {FOREST}; color: {TXT}; border-radius: 999px; padding: 22px 32px; font-size: 26px; font-weight: 600; white-space: nowrap">DM “BUY” + event</div>
</div></div>'''
write('HelpToBuy.dc.html',page('Authentix — Buy For You explainer',1080,1350,CREAM,FOREST,body))

# ---------- T4 Trust ----------
facts=[('Registered business','SSM [REG NO.] — the name matches our bank account.'),('One payment account','Business account only. Never a personal or third-party one.'),
       ('Receipt + Order ID','Every order itemised: face value and fee, in writing.'),('Official e-tickets','Transferred via the organiser’s platform — never a screenshot.'),
       ('Full refund rule','Not secured or invalid at entry = refund in [X] days.'),('Public track record','[N] secured orders in our Reviews highlight.')]
fc=''.join(f'<div style="background: rgba(241,238,230,0.06); border: 1px solid rgba(241,238,230,0.16); border-radius: 22px; padding: 22px 26px; display: flex; gap: 18px; align-items: flex-start">{icon("check",36,TXT,2.2)}<div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 27px; font-weight: 600">{t}</span><span style="font-size: 22px; color: {MUTED}; line-height: 1.4">{d}</span></div></div>' for t,d in facts)
nev=''.join(f'<div style="display: flex; gap: 12px">{icon("x",26,SAGE,2.2)}<span>{t}</span></div>' for t in ['Rush you to pay in 5 minutes','Ask for gift cards, crypto or OTPs','DM you first from a new account'])
body=f'''<div style="position: absolute; left: 0; top: 0; right: 0; height: 520px; overflow: hidden">{photo(IMG_CROWD,'center 60%','; opacity: 0.7')}<div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(31,58,47,0.45) 0%, {FOREST} 100%)"></div></div>
<div style="position: absolute; inset: 0; padding: 72px; box-sizing: border-box; display: flex; flex-direction: column; gap: 30px">
<div style="display: flex; justify-content: space-between; align-items: center">{lock(TXT)}<div style="display: flex; align-items: center; gap: 12px">{icon('shield',30,TXT,1.6)}{caps('100% TRUSTED',20,TXT,0.3,600)}</div></div>
<div style="display: flex; flex-direction: column; gap: 18px; margin-top: 40px">
{caps('DON’T TRUST US.|VERIFY US.',58,TXT,0.12,600)}{dash(TXT,60,4)}
<div style="font-size: 26px; color: {MUTED}; line-height: 1.4">Six things you can check yourself, before you pay.</div></div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px">{fc}</div>
<div style="display: flex; flex-direction: column; gap: 14px; border-top: 1px solid rgba(241,238,230,0.18); padding-top: 22px">{caps('WE WILL NEVER',18,SAGE,0.3,600)}<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; font-size: 22px; line-height: 1.4; color: {TXT}">{nev}</div></div>
<div style="display: flex; justify-content: space-between; align-items: center; gap: 24px; margin-top: auto">
<span style="font-size: 21px; color: {MUTED}; line-height: 1.5">Our only accounts: <strong style="color: {TXT}">@authentix.my</strong> · WhatsApp <strong style="color: {TXT}">[+60 / +65 NUMBER]</strong>. Anyone else using our name — report to us.</span>{seal(140,TXT)}
</div></div>'''
write('ScamProof.dc.html',page('Authentix — Trust guarantee',1080,1350,FOREST,TXT,body))
print('templates ok')
