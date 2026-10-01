from parts import *
def h2(t,c='#111'): return f'<div style="font-size: 36px; font-weight: 600; color: {c}; letter-spacing: -0.01em">{t}</div>'
def h3(t,c='#111'): return f'<div style="font-size: 24px; font-weight: 600; color: {c}">{t}</div>'
def tag(t,c=MUTED_L): return caps(t,13,c,0.24)
CARD=f'background: #F1EFEA; border-radius: 22px; box-shadow: inset 0 0 0 1px #D9D5CC'

# ---------- INSTAGRAM STRATEGY ----------
bios=[('V1 · YOUR MOCKUP (LIVE)','Concert Tickets | MY / SG &amp; Beyond|Internal Orders | Discounted | Buy For You|More Than Tickets, Real Experiences.','114','Exactly as designed — lists every service in one glance.'),
      ('V2 · TRUST-LED','Real tickets. Real fans. Real experiences.|Concerts | MY / SG &amp; Beyond|100% trusted · Buy For You service|DM or tap to order ↓','126','Use after a scam wave hits the news.'),
      ('V3 · VERIFIABLE','More than tickets.|Concert Tickets | Buy For You | Deals|MY / SG &amp; Beyond · SSM [REG NO.]|WhatsApp to order ↓','109','Shows your registration number up front.')]
bc=''.join(f'''<div style="{CARD}; padding: 26px; display: flex; flex-direction: column; gap: 14px{'; box-shadow: inset 0 0 0 2px '+FOREST if i==0 else ''}">
<div style="display: flex; justify-content: space-between">{caps(t,12,FOREST if i==0 else MUTED_L,0.22,600)}<span style="font-size: 13px; color: {MUTED_L}">{n} / 150</span></div>
<div style="font-size: 17px; line-height: 1.55; white-space: pre-line; color: #111">{b.replace('|','&#10;') if False else b.replace(' | ',' &#124; ').replace('|','&#10;')}</div>
<div style="font-size: 14px; color: {MUTED_L}; line-height: 1.5; margin-top: auto">{d}</div></div>''' for i,(t,b,n,d) in enumerate(bios))
def tile(n,tone,title,sub):
    if tone=='P':
        bg=f'background: {DEEP}'; inner=photo(IMG_BEAMS if n in (8,) else (IMG_NIGHT if n==1 else IMG_CROWD),'center')+f'<div style="position: absolute; inset: 0; background: rgba(14,21,18,0.55)"></div>'; c=TXT
    elif tone=='F': bg=f'background: {FOREST}'; inner=''; c=TXT
    else: bg=f'background: {CREAM}'; inner=''; c=FOREST
    return f'''<div style="height: 260px; {bg}; position: relative; overflow: hidden">{inner}
<div style="position: absolute; inset: 0; padding: 18px; display: flex; flex-direction: column; justify-content: space-between">
<span style="font-size: 13px; font-weight: 600; color: {c}; letter-spacing: 0.2em">{n:02d}</span>
<div style="display: flex; flex-direction: column; gap: 8px">{caps(title,15,c,0.2,600)}{dash(c,16,2)}</div>
<span style="font-size: 12px; color: {c}; opacity: 0.8">{sub}</span></div></div>'''
grid=''.join(tile(*t) for t in [(9,'C','HOW TO|ORDER','Carousel · FAQ'),(8,'P','[ARTIST]|AVAILABLE NOW','T1 Ticket Drop'),(7,'F','“REAL|REVIEW”','Customer quote'),
    (6,'P','DIFFERENT SHOWS|SAME TRUST','Tour radar'),(5,'F','WHAT|YOU PAY','Pricing table'),(4,'C','SECURED|WALL','Proof collage'),
    (3,'F','DON’T TRUST US.|VERIFY US.','T4 Trust'),(2,'C','REAL FANS|REAL SUPPORT','Brand post'),(1,'P','IT STARTS|WITH A TICKET','Brand intro')])
plan=[('01','Day 1','It starts with a ticket','Brand intro + logo; who we are'),('02','Day 1','Real fans, real support','Values; MY / SG &amp; beyond'),('03','Day 1','Don’t trust us. Verify us.','Answer “is it real?” first. Post 1–3 together'),
      ('04','Day 3','Buy For You explained','Your hero service, 5 steps'),('05','Day 5','What you pay','Face value + fee, split clearly'),('06','Day 7','Different shows, same trust','Upcoming MY/SG tour radar'),
      ('07','Day 9','Customer review','Real quote + handle, with consent'),('08','Day 11','First ticket drop','The sell lands on a trusted profile'),('09','Day 13','How to order + FAQ','Converts drop traffic. Pin 3, 4, 9')]
pr=''.join(f'<div style="display: grid; grid-template-columns: 44px 70px 1fr 1.1fr; gap: 12px; padding: 12px 0; border-bottom: 1px solid #D9D5CC; font-size: 15px; line-height: 1.4"><span style="font-weight: 700; color: {FOREST}">{a}</span><span style="color: {MUTED_L}">{b}</span><strong>{c}</strong><span style="color: #3A403C">{d}</span></div>' for a,b,c,d in plan)
body=f'''<div style="position: absolute; inset: 0; padding: 80px 96px; box-sizing: border-box; display: flex; flex-direction: column; gap: 44px; color: #111">
<div style="display: flex; justify-content: space-between; align-items: baseline">{h2('Instagram — bio &amp; 9-grid launch')}{tag('03 · INSTAGRAM')}</div>
<div style="display: flex; flex-direction: column; gap: 16px">{h3('Bio — 3 variations')}<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px">{bc}</div></div>
<div style="display: flex; flex-direction: column; gap: 16px">
<div style="display: flex; justify-content: space-between; align-items: baseline">{h3('9-grid launch plan')}<span style="font-size: 14px; color: {MUTED_L}">Numbers = posting order · grid as it looks after post 9</span></div>
<div style="display: flex; gap: 48px; align-items: flex-start">
<div style="display: grid; grid-template-columns: repeat(3, 210px); gap: 4px; flex-shrink: 0">{grid}</div>
<div style="display: flex; flex-direction: column; flex-grow: 1">
<div style="display: grid; grid-template-columns: 44px 70px 1fr 1.1fr; gap: 12px; padding-bottom: 10px; border-bottom: 1px solid #BDB9B0">{tag('#')}{tag('WHEN')}{tag('POST')}{tag('JOB')}</div>{pr}
<div style="margin-top: 18px; font-size: 14px; color: {MUTED_L}; line-height: 1.55">Every row and column holds one photo tile, one Forest tile and one Cream tile — the same rhythm as the mockup grid, so the profile reads calm and premium.</div>
</div></div></div></div>'''
write('Instagram.dc.html',page('Authentix — Instagram bio and grid',1440,1500,PAPER,'#111',body))

# ---------- COPY KIT ----------
def tk(title,fmt,specs,cap_label,cap,tags):
    sp=''.join(f'<div><strong style="color: #111">{a}</strong> — {b}</div>' for a,b in specs)
    return f'''<div style="{CARD}; padding: 30px; display: flex; flex-direction: column; gap: 18px">
<div style="display: flex; justify-content: space-between; align-items: baseline">{h3(title)}{tag(fmt)}</div>
<div style="display: flex; flex-direction: column; gap: 7px; font-size: 15px; line-height: 1.5; color: #3A403C">{sp}</div>
<div style="background: {DEEP}; color: {TXT}; border-radius: 16px; padding: 22px; display: flex; flex-direction: column; gap: 10px">{caps(cap_label,11,SAGE,0.22,600)}<div style="font-size: 15px; line-height: 1.6; white-space: pre-line">{cap}</div><span style="font-size: 13px; color: {MUTED}">{tags}</span></div></div>'''
k1=tk('T1 · Ticket Drop','FEED 1080×1350',[('Top','B&amp;W stage photo fading to Deep Night; lockup left, drop no. right'),('Hero','dash + AVAILABLE NOW, artist in SemiBold 104, tour in spaced caps'),('Ticket','Forest body (date / city / venue) + Cream stub (“from” price)'),('Table','face value vs all-in, status in spaced caps'),('Footer','Cream CTA pill + refund rule + “not affiliated” line')],
  'CAPTION · HOOK → FACTS → PRICE → TRUST → CTA','[ARTIST] · [CITY] — available now.\n[DD MMM] · [VENUE]\nVIP / CAT 1 / CAT 2 from [RM ___] all-in. Face value shown on the post.\nOfficial e-ticket transfer · Order ID + receipt · not secured = full refund.\nDM “DROP” or WhatsApp [NUMBER].','#[Artist]KL #[Artist]SG #KpopMalaysia #SGConcerts #AuthentixMY')
k2=tk('T2 · Secured / Proof','STORY 1080×1920',[('Safe zones','keep the top 250 px and bottom 290 px free of key info'),('Headline','SECURED in SemiBold caps, order ID + time between dashes'),('Card','Cream receipt, real screenshot pasted in; solid bars over name, contact, all but last 4 of the ref'),('Watermark','diagonal “AUTHENTIX · order ID” at 8%, trust seal bottom-right'),('Rules','post within 24 h, with the customer’s OK; save to Reviews highlight')],
  'STORY TEXT','Secured ✓ [ARTIST] · CAT 1 × 2\nQueue #[000,000] → [MM:SS]\nNext drop: [DATE] — DM “BUY”','Add Link sticker → WhatsApp · Poll: “Which show next?”')
k3=tk('T3 · Buy For You','FEED 1080×1350 · PIN',[('Ground','Cream with a faint oversized A mark'),('Headline','YOU RELAX. / WE QUEUE. in spaced SemiBold caps'),('Steps','5 Forest number discs on one rail; step 5 outlined'),('Fine print','min. 2 side-by-side; organiser assigns seats')],
  'CAPTION · PAIN → PROCESS → PRICE → RISK REVERSAL → CTA','Queue opens at 10:00. You’re in a meeting. We’ve got it.\nBuy For You = we queue for your tickets on drop day and update you live.\nFee: [RM ___] per ticket on top of face value, quoted in writing first.\nPaid upfront — refunded in full if we don’t secure.\nDM “BUY” + the event name.','#BuyForYou #KpopMalaysia #ConcertSG #AuthentixMY')
k4=tk('T4 · 100% Trusted','FEED 1080×1350 · PIN',[('Top','crowd photo melting into Forest'),('Headline','DON’T TRUST US. / VERIFY US.'),('Proof grid','6 checkable facts, 2 × 3'),('Footer','“We will never…” red flags + official handles + seal')],
  'CAPTION · STAKES → INVITE TO VERIFY → SHARE','SG fans lost at least S$615,000 to concert-ticket scams in Jan–Oct 2025 (SPF).\nSo don’t take our word for it — check us: SSM [NO.], one business account, receipts, official transfers and a written refund rule.\nSave this. Send it to the friend about to pay a stranger for “CAT 1, cheap”.','#ConcertScam #KpopMalaysia #SGConcerts #AuthentixMY')
say=''.join(f'<div style="color: #111">{a}</div><div style="color: {MUTED_L}">{b}</div>' for a,b in [('“Secured”','“Guaranteed seats”'),('“Official transfer”','“100% legit!!!”'),('“All-in price”','“Cheapest in MY”'),('“Not secured = refund”','“Last 1, pay now”'),('“Real experiences”','“Backstage connections”')])
body=f'''<div style="position: absolute; inset: 0; padding: 80px 96px; box-sizing: border-box; display: flex; flex-direction: column; gap: 36px; color: #111">
<div style="display: flex; justify-content: space-between; align-items: baseline">{h2('Copy kit — layouts, captions, voice')}{tag('04 · TEMPLATES')}</div>
<div style="display: grid; grid-template-columns: 1fr 1fr 1.2fr; gap: 20px">
<div style="background: {FOREST}; color: {TXT}; border-radius: 22px; padding: 30px; display: flex; flex-direction: column; gap: 14px">{caps('VOICE',12,SAGE,0.24,600)}<div style="font-size: 26px; font-weight: 600; line-height: 1.3">Quiet. Warm. Certain.</div><p style="font-size: 16px; line-height: 1.6; color: #D5DAD6">Short lines, spaced caps, a closing dash. Talk about the night, not the hustle. Urgency comes from real stock status — never caps-lock or countdowns.</p></div>
<div style="{CARD}; padding: 30px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px 18px; font-size: 15px; line-height: 1.45; align-content: start">{caps('SAY',12,FOREST,0.24,600)}{caps('AVOID',12,MUTED_L,0.24,600)}{say}</div>
<div style="background: {DEEP}; color: {TXT}; border-radius: 22px; padding: 30px; display: flex; flex-direction: column; gap: 12px">{caps('WHATSAPP QUOTE FORMAT',12,SAGE,0.24,600)}<div style="font-size: 15px; line-height: 1.65; white-space: pre-line; font-variant-numeric: tabular-nums">AUTHENTIX · QUOTE AX-[0000]
[ARTIST] – [CITY] – [DATE]
CAT 1 × 2 (side-by-side)
Face value: [RM ___] × 2
Service fee: [RM ___] × 2
TOTAL: [RM ___]
Pay to: [BUSINESS NAME] · SSM [NO.]
Not secured = 100% refund in [X] days.
Seats assigned by organiser.</div></div>
</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 22px">{k1}{k2}{k3}{k4}</div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px">
<div style="border-top: 2px solid {FOREST}; padding-top: 14px; font-size: 15px; line-height: 1.55; color: #3A403C"><strong style="color: #111">Photos</strong> — use your own crowd shots or the supplied B&amp;W ones. No artist faces, tour art or official logos.</div>
<div style="border-top: 2px solid {FOREST}; padding-top: 14px; font-size: 15px; line-height: 1.55; color: #3A403C"><strong style="color: #111">Currency</strong> — one per post, matched to the venue city (RM for KL, S$ for SG).</div>
<div style="border-top: 2px solid {FOREST}; padding-top: 14px; font-size: 15px; line-height: 1.55; color: #3A403C"><strong style="color: #111">Placeholders</strong> — fill every [BRACKET]; don’t publish a number you can’t prove.</div>
</div></div>'''
write('CopyKit.dc.html',page('Authentix — Copy kit',1440,1900,PAPER,'#111',body))

# ---------- STRATEGY ----------
ins=[('S$615k','Scams define the category','At least S$615,000 lost across 722 concert-ticket scam cases in SG, Jan–Oct 2025. KL Coldplay fans were turned away at the gate with fake tickets.','SPF advisory, Dec 2025'),
     ('“Official only”','Default advice: don’t buy resale','Police and promoters tell fans to buy from authorised sellers. A third party starts with a trust deficit — evidence closes it, claims don’t.','SPF · promoter advisories'),
     ('Rules shifting','ID checks &amp; anti-scalping talk','Malaysia is studying anti-scalping laws and ID-matched entry. Name-bound tickets favour Buy For You over pure resale.','KPDN via Malay Mail, Jul 2025'),
     ('DM-first','The sale happens in chat','Discovery on IG / TikTok, closing on WhatsApp. The identity has to work as a 110 px profile picture and inside a chat bubble.','Channel behaviour')]
ic=''.join(f'<div style="{CARD}; padding: 28px; display: flex; flex-direction: column; gap: 12px"><div style="font-size: 36px; font-weight: 700; color: {FOREST}">{a}</div><div style="font-size: 18px; font-weight: 600">{b}</div><p style="font-size: 15px; line-height: 1.55; color: #3A403C">{c}</p><div style="margin-top: auto">{caps(d,11,MUTED_L,0.2)}</div></div>' for a,b,c,d in ins)
rank=''.join(f'<div style="border-top: 2px solid {FOREST if i<2 else "#BDB9B0"}; padding-top: 12px; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 13px; font-weight: 700; color: {FOREST}">0{i+1}</span><span style="font-size: 17px; font-weight: 600">{a}</span><span style="font-size: 14px; color: {MUTED_L}">{b}</span></div>' for i,(a,b) in enumerate([('Is it real?','Proof of legitimacy'),('What if it fails?','Refund rule in writing'),('How fast?','Reply + queue speed'),('What’s the real price?','Face value vs fee'),('Where will I sit?','Category / zone')]))
explored=''.join(f'<div style="border: 1px dashed #BDB9B0; border-radius: 16px; padding: 18px 20px; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 12px; letter-spacing: 0.2em; color: {MUTED_L}">{a}</span><span style="font-size: 17px; font-weight: 600; color: #3A403C">{b}</span><span style="font-size: 14px; color: {MUTED_L}; line-height: 1.5">{c}</span></div>' for a,b,c in [('EXPLORED · A','Cyber Neon VIP','Scroll-stopping, but reads like every scam reseller.'),('EXPLORED · B','Verified Premium','Trustworthy, but cold for a fan brand.'),('EXPLORED · C','Concert Glow','Emotional, but relies on photos you don’t own.')])
claims=''.join(f'<div style="font-weight: 600; color: {TXT}">{a}</div><div style="color: #C9D0CB">{b}</div>' for a,b in [('“100% Trusted”','Back it with the six checkable facts (T4): SSM no., one account, receipts, official transfer, refund rule, reviews.'),('“Internal Orders”','Advertise only allocations you can document. Explain the source in the DM, not on posters.'),('“Discounted”','Show face value next to your price. Below-face offers are the #1 scam bait — say why yours exist.'),('Organiser T&amp;Cs','Many events void resold or name-mismatched tickets. Check per event; lead with Buy For You where tickets are name-bound.')])
body=f'''<div style="position: absolute; left: 0; top: 0; right: 0; height: 560px; overflow: hidden; background: {DEEP}">{photo(IMG_CROWD,'center 60%','; opacity: 0.55')}<div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(14,21,18,0.4), {DEEP})"></div></div>
<div style="position: absolute; inset: 0; padding: 80px 96px; box-sizing: border-box; display: flex; flex-direction: column; gap: 64px; color: #111">
<div style="display: flex; justify-content: space-between; align-items: center; color: {TXT}"><div style="display: flex; align-items: center; gap: 14px">{M(TXT,56)}{wordmark(TXT,30)}</div>{caps('BRAND STRATEGY · MY / SG &amp; BEYOND · SEP 2026',13,TXT,0.24)}</div>
<div style="display: flex; flex-direction: column; gap: 24px; max-width: 1000px; color: {TXT}">
{caps('00 · THE ONE-LINE STRATEGY',13,SAGE,0.26,600)}
<div style="font-size: 60px; font-weight: 600; line-height: 1.1; letter-spacing: -0.01em">In a market full of scams, fans don’t buy the hype. They buy the proof — and the night.</div>
<p style="font-size: 20px; line-height: 1.6; color: #C9D0CB; max-width: 880px">Authentix pairs a quiet, premium look (forest, cream, black-and-white crowds) with checkable proof in every post. More than tickets, real experiences.</p>
</div>
<div style="display: flex; flex-direction: column; gap: 26px">
{h2('01 · Market dynamics')}
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px">{ic}</div>
<div style="display: flex; gap: 20px"><div style="width: 190px; flex-shrink: 0; padding-top: 14px">{tag('WHAT FANS WEIGH, IN ORDER')}</div><div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 14px; flex-grow: 1">{rank}</div></div>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 36px">
<div style="display: flex; flex-direction: column; gap: 22px">
{h2('02 · Direction: Forest &amp; Cream')}
<p style="font-size: 17px; line-height: 1.6; color: #3A403C">Your mockup is the chosen direction. It beats the three explored routes because calm reads as safe, and B&amp;W crowds keep the focus on fans instead of artists you don’t represent.</p>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px">{explored}</div>
<div style="display: flex; flex-direction: column; gap: 12px; font-size: 16px; line-height: 1.5; color: #3A403C">
<div><strong style="color: #111">Quiet confidence</strong> — forest, cream and black. No neon; scammers shout, we don’t.</div>
<div><strong style="color: #111">Real crowds</strong> — black-and-white fan photography, never artist faces or tour art.</div>
<div><strong style="color: #111">Spaced statements</strong> — short caps lines closed by a dash: “Different shows, same trust.”</div>
</div></div>
<div style="background: {FOREST}; border-radius: 24px; padding: 34px; display: flex; flex-direction: column; gap: 18px">
<div style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 22px; font-weight: 600; color: {TXT}">Claims you must be able to back</span>{caps('NOT LEGAL ADVICE',11,SAGE,0.22)}</div>
<div style="display: grid; grid-template-columns: 1fr 1.7fr; gap: 14px 22px; font-size: 15px; line-height: 1.5">{claims}</div>
</div></div></div>'''
write('Main.dc.html',page('Authentix — Strategy',1440,2040,PAPER,'#111',body))

# ---------- PROMPTS ----------
P=[('01 · LOGO','Foil logo on forest card','Launch post, deck cover','Premium brand identity mockup: a minimalist monogram logo — a bold geometric letter “A” without crossbar, encircled by a thin tilted orbit ring that passes in front of the letter, with a small four-point sparkle at the upper right — cream foil stamped on a thick matte deep forest-green (#1F3A2F) card, cream wordmark “Authentix” in a clean geometric sans below, soft directional studio light, subtle paper texture, 30° angle on dark stone, quiet luxury, photorealistic','--ar 4:5 --style raw --s 200'),
   ('02 · IG PROFILE','Phone mockup on cream set','Link-in-bio hero, pitch','Photorealistic smartphone mockup lying on a warm cream (#E7E4DC) paper surface, screen showing a light-mode Instagram profile with a deep forest-green circular avatar containing an “A” monogram with orbit ring and sparkle, beside it three rounded app-icon tiles in forest green, cream and black, soft daylight shadows, minimal editorial brand presentation, no other brand logos','--ar 4:5 --style raw --s 150'),
   ('03 · STORY / POST','B&amp;W crowd post in hand','Reels cover, ads','A hand holding a smartphone in a dark concert arena, black-and-white crowd with raised hands and hazy stage beams behind, the screen shows a dark photo post with widely letter-spaced cream capital text “DIFFERENT SHOWS SAME TRUST” and a short dash, subtle forest-green tint, 35mm film grain, cinematic, no performer faces, no artist logos','--ar 9:16 --style raw --s 150'),
   ('04 · TICKET','Branded ticket voucher','Ticket drop posts, gifts','Luxury concert ticket voucher: dark ticket with a faded black-and-white crowd photo background, left semicircle notch, perforated stub on the right with a vertical barcode and small spaced caps “LIVE MUSIC REAL PEOPLE”, cream “A” monogram with orbit ring and sparkle next to the wordmark “Authentix”, lying on warm cream paper with soft shadow, product photography, ultra-detailed','--ar 3:2 --style raw --s 250'),
   ('05 · LANYARD','VIP lanyard pass flat-lay','VIP / priority posts','Top-down flat lay on a warm cream surface: a deep forest-green rounded VIP lanyard card with a black strap and silver clip, cream “A” monogram with orbit and sparkle and the word “Authentix”, small spaced caps “CREATING MORE LIVE MOMENTS” in the corner, beside a black app-icon tile and a folded ticket, soft natural light, minimal premium branding, sharp focus','--ar 4:5 --style raw --s 200')]
pc=''.join(f'<div style="display: grid; grid-template-columns: 280px 1fr; gap: 32px; {CARD}; padding: 28px 32px"><div style="display: flex; flex-direction: column; gap: 10px">{caps(a,13,FOREST,0.22,600)}<span style="font-size: 21px; font-weight: 600; line-height: 1.3">{b}</span><span style="font-size: 14px; color: {MUTED_L}">{c}</span></div><div style="font-size: 15px; line-height: 1.7; color: #1A1F1C">{d} <span style="color: {FOREST}; font-weight: 600">{e}</span></div></div>' for a,b,c,d,e in P)
body=f'''<div style="position: absolute; inset: 0; padding: 80px 96px; box-sizing: border-box; display: flex; flex-direction: column; gap: 32px; color: #111">
<div style="display: flex; justify-content: space-between; align-items: baseline">{h2('Mockup prompts — Midjourney / DALL·E')}{tag('05 · PROMPTS')}</div>
<div style="display: flex; flex-direction: column; gap: 16px">{pc}</div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px">
<div style="border-top: 2px solid {FOREST}; padding-top: 14px; font-size: 15px; line-height: 1.55; color: #3A403C"><strong style="color: #111">DALL·E / ChatGPT</strong> — delete everything after “--” and add “Aspect ratio 4:5. Any text must read exactly: Authentix.”</div>
<div style="border-top: 2px solid {FOREST}; padding-top: 14px; font-size: 15px; line-height: 1.55; color: #3A403C"><strong style="color: #111">Keep the logo exact</strong> — export the App icon artboard as PNG and attach it as an image reference, or composite the real logo afterwards.</div>
<div style="border-top: 2px solid {FOREST}; padding-top: 14px; font-size: 15px; line-height: 1.55; color: #3A403C"><strong style="color: #111">Label it</strong> — AI scenes are mood only, never “proof”. Proof posts use real, redacted confirmations.</div>
</div></div>'''
write('Prompts.dc.html',page('Authentix — AI image prompts',1440,1500,PAPER,'#111',body))
print('content ok')
