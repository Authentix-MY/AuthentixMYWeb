def mark(color, w, uid, star=True):
    cy=118
    ring=(f"M6 {cy} A94 25 0 1 0 194 {cy} A94 25 0 1 0 6 {cy} Z "
          f"M12 {cy-3} A88 18.5 0 1 0 188 {cy-3} A88 18.5 0 1 0 12 {cy-3} Z")
    A="M86 26 Q100 10 115 26 L170 172 L137 172 L100.5 66 L72 172 L46 172 Z"
    rot=f"rotate(-19 100 {cy})"
    st=(f'<path d="M168 22 Q170 37 185 39 Q170 41 168 56 Q166 41 151 39 Q166 37 168 22 Z" fill="{color}"></path>' if star else '')
    h=round(w*0.9)
    return (f'<svg viewBox="0 0 200 180" width="{w}" height="{h}" aria-hidden="true" style="display:block">'
      f'<defs><clipPath id="cf{uid}"><rect x="-20" y="{cy}" width="240" height="80"></rect></clipPath>'
      f'<clipPath id="cb{uid}"><rect x="-20" y="{cy}" width="240" height="80"></rect><rect x="78" y="60" width="140" height="{cy-60}"></rect></clipPath>'
      f'<mask id="mk{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="200" height="180"><rect x="0" y="0" width="200" height="180" fill="#fff"></rect>'
      f'<g transform="{rot}"><path d="{ring}" fill-rule="evenodd" fill="#000" stroke="#000" stroke-width="9" clip-path="url(#cf{uid})"></path></g></mask></defs>'
      f'<g transform="{rot}"><path d="{ring}" fill-rule="evenodd" fill="{color}" clip-path="url(#cb{uid})"></path></g>'
      f'<path d="{A}" fill="{color}" mask="url(#mk{uid})"></path>'
      f'<g transform="{rot}"><path d="{ring}" fill-rule="evenodd" fill="{color}" clip-path="url(#cf{uid})"></path></g>'
      f'{st}</svg>')
