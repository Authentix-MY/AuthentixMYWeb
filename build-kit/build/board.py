from parts import *
W=1440; H=1440; TOP=618
dots=''.join(f'<div style="width: 40px; height: 40px; border-radius: 50%; background: {c}; box-shadow: 0 0 0 1px rgba(0,0,0,0.06)"></div>' for c in [FOREST,SAGE,CREAM,INK])
body=f'''{hero(W,TOP,1.0)}
<div style="position: absolute; left: 0; top: {TOP}px; width: {W}px; height: {H-TOP}px; background: {PAPER}"></div>
<div style="position: absolute; left: 42px; top: 634px">{phone_profile(478)}</div>
<div style="position: absolute; left: 556px; top: 643px; display: flex; gap: 13px">{app_tile(180,FOREST,TXT)}{app_tile(180,CREAM,FOREST)}{app_tile(180,INK,TXT)}</div>
<div style="position: absolute; left: 1172px; top: 643px; display: flex; flex-direction: column; gap: 10px">{dots}</div>
<div style="position: absolute; left: 1250px; top: 668px; display: flex; flex-direction: column; gap: 10px">{caps('SAME|MUSIC|BIGGER|STORIES',13,'#2A2F2C',0.28)}{dash('#2A2F2C',20,1)}</div>
<div style="position: absolute; left: 556px; top: 852px">{ticket(560,PAPER)}</div>
<div style="position: absolute; left: 548px; top: 1083px; display: flex; gap: 16px">
<div style="box-shadow: 0 16px 30px rgba(0,0,0,0.18); border-radius: 12px; overflow: hidden">{post_trust(280)}</div>
<div style="box-shadow: 0 16px 30px rgba(0,0,0,0.12); border-radius: 12px; overflow: hidden">{post_real(280)}</div>
<div style="box-shadow: 0 16px 30px rgba(0,0,0,0.18); border-radius: 12px; overflow: hidden">{post_ticket(280)}</div>
</div>
<div style="position: absolute; left: 1433px; top: 676px; width: 14px; height: 170px; background: #151515; transform: rotate(36.5deg); transform-origin: top center; border-radius: 2px"></div>
<div style="position: absolute; left: 1318px; top: 806px; width: 28px; height: 28px; border-radius: 50%; border: 6px solid #8B8F8C; box-sizing: border-box"></div>
<div style="position: absolute; left: 1229px; top: 826px; transform: rotate(12deg); transform-origin: 50% 0%">{lanyard_card(205)}</div>'''
write('Board.dc.html',page('Authentix — Brand board',W,H,PAPER,'#111',body))

# Hero banner asset 1920x1080
write('Hero.dc.html',page('Authentix — Hero banner',1920,1080,DEEP,TXT,hero(1920,1080,1.6)))
print('ok')
