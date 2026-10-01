from parts import *
# App icons 512
for name,bg,fg in [('IconGreen',FOREST,TXT),('IconCream',CREAM,FOREST),('IconBlack',INK,TXT)]:
    write(f'{name}.dc.html',page(f'Authentix — App icon {name[4:].lower()}',512,512,bg,fg,
      f'<div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center">{M(fg,320)}</div>'))
# PFP (circle crop safe) 1080
write('ProfilePic.dc.html',page('Authentix — Profile picture',1080,1080,FOREST,TXT,
  f'<div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center">{M(TXT,640)}</div>'))
# Ticket
write('Ticket.dc.html',page('Authentix — Ticket',1480,600,PAPER,TXT,f'<div style="position: absolute; left: 40px; top: 40px">{ticket(1400,PAPER)}</div>'))
# Lanyard
lan=f'''<div style="position: absolute; left: 385px; top: 0; width: 30px; height: 150px; background: #151515"></div>
<div style="position: absolute; left: 375px; top: 140px; width: 50px; height: 50px; border-radius: 50%; border: 10px solid #8B8F8C; box-sizing: border-box"></div>
<div style="position: absolute; left: 120px; top: 180px">{lanyard_card(560)}</div>'''
write('Lanyard.dc.html',page('Authentix — VIP lanyard pass',800,1040,PAPER,TXT,lan))
# Posts
write('PostTrust.dc.html',page('Authentix — Post: Different shows, same trust',1080,1350,DEEP,TXT,post_trust(1080)))
write('PostReal.dc.html',page('Authentix — Post: Real fans',1080,1350,CREAM,FOREST,post_real(1080)))
write('PostTicket.dc.html',page('Authentix — Post: It starts with a ticket',1080,1350,DEEP,TXT,post_ticket(1080)))
# Profile phone
write('Profile.dc.html',page('Authentix — Instagram profile mockup',560,1080,PAPER,'#111',f'<div style="position: absolute; left: 40px; top: 40px">{phone_profile(480)}</div>'))
# Highlight covers: 5 story covers shown + 1080x1920 spec
hl=[('ticket','Tickets'),('percent','Deals'),('globe','MY / SG'),('star','Reviews'),('headset','Help')]
covers=''.join(f'''<div style="display: flex; flex-direction: column; align-items: center; gap: 18px">
<div style="width: 180px; height: 320px; border-radius: 18px; background: {FOREST}; display: flex; align-items: center; justify-content: center; position: relative">
<div style="width: 150px; height: 150px; border-radius: 50%; background: #E9E8E4; display: flex; align-items: center; justify-content: center">{icon(ic,70,'#1A1A1A',1.5)}</div></div>
<div style="width: 110px; height: 110px; border-radius: 50%; background: #E9E8E4; box-shadow: 0 0 0 2px {PAPER}, 0 0 0 4px #C9C6BE; display: flex; align-items: center; justify-content: center">{icon(ic,48,'#1A1A1A',1.6)}</div>
<span style="font-size: 18px; font-weight: 500; color: #1A1A1A">{lab}</span></div>''' for ic,lab in hl)
body=f'''<div style="position: absolute; inset: 0; padding: 64px 72px; box-sizing: border-box; display: flex; flex-direction: column; gap: 40px">
<div style="display: flex; justify-content: space-between; align-items: baseline"><div style="font-size: 30px; font-weight: 600; color: #111">Story highlight covers</div>{caps('EXPORT 1080 × 1920 · ICON IN CENTRE CIRCLE',14,MUTED_L,0.2)}</div>
<div style="display: flex; justify-content: space-between">{covers}</div>
<div style="font-size: 17px; color: {MUTED_L}; line-height: 1.6">Cover = Forest story frame with a light-grey disc and a dark line icon, so the ring reads as soft grey on the profile (as in the mockup). Top row: full story cover. Bottom: how it crops on the profile.</div>
</div>'''
write('Highlights.dc.html',page('Authentix — Highlight covers',1320,760,PAPER,'#111',body))
print('assets ok')
