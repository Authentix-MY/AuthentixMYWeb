DROPS = [
 {"id":"bigbang-sg-2026","artist":"BIGBANG","tour_en":"2026–2027 World Tour XX:COSMOS","tour_zh":"2026–2027 世界巡回演唱会 XX:COSMOS",
  "city":"SG","venue_en":"Singapore National Stadium","venue_zh":"新加坡国家体育场",
  "date_label_en":"Sat 17 Oct 2026 · 7pm","date_label_zh":"2026年10月17日（周六）· 晚上7点","event_date":"2026-10-17",
  "status":"preorder","note_en":"All categories except VIP Ultimate","note_zh":"除 VIP Ultimate 外所有票区","image_url":"beams","published":True},
 {"id":"tba-kl-1","artist":"[ARTIST]","tour_en":"[TOUR NAME]","tour_zh":"[巡演名称]","city":"KL","venue_en":"[VENUE]","venue_zh":"[场馆]",
  "date_label_en":"[DD MMM 2026]","date_label_zh":"[2026年X月X日]","event_date":None,"status":"soon",
  "note_en":"Get notified when sales open","note_zh":"开票时第一时间通知你","image_url":"crowd","published":True},
 {"id":"tba-sg-1","artist":"[ARTIST]","tour_en":"[TOUR NAME]","tour_zh":"[巡演名称]","city":"SG","venue_en":"[VENUE]","venue_zh":"[场馆]",
  "date_label_en":"[DD MMM 2026]","date_label_zh":"[2026年X月X日]","event_date":None,"status":"soon",
  "note_en":"Get notified when sales open","note_zh":"开票时第一时间通知你","image_url":"night","published":True},
]
REVIEWS = [
 {"id":"r1","handle":"aria.abjalil","text":"Totally legit — got the e-ticket for sure. I was kinda nervous at first, but the seller walked me through everything. Luckily I managed to snag the ticket, even if it was a bit last minute.","tags":["Great communication","Knows their stuff"],"event":"HIGHLIGHT Live, Malaysia","source":"Carousell","screenshot_url":"review-1.jpg","visible":True,"sort_order":1},
 {"id":"r2","handle":"westasiesta","text":"Trusted seller! Replied to my queries about the tickets very quickly, and was able to deal in person. Trustworthy, even secured me a poster! Polite and helpful seller. Thank you, I had a great time!","tags":["Value for money","Great communication"],"event":"MONSTA X, Malaysia","source":"Carousell","screenshot_url":"review-2.jpg","visible":True,"sort_order":2},
 {"id":"r3","handle":"hoodawon","text":"Nice service from the seller! Fast replies and very trustworthy. It was a last-minute purchase, and thankfully they managed to get the best seats for me and my sister.","tags":["Value for money","Great communication"],"event":"MONSTA X, Malaysia","source":"Carousell","screenshot_url":"review-4.jpg","visible":True,"sort_order":3},
 {"id":"r4","handle":"bluelikeocean","text":"Seller was so patient and was willing to wait for me to make payment. Great seller to deal with and even gave me a good price for my seat. Hope to deal with you again. Thank you!","tags":["Great communication","Above and beyond"],"event":"MONSTA X, Malaysia","source":"Carousell","screenshot_url":"review-5.jpg","visible":True,"sort_order":4},
 {"id":"r5","handle":"kimja999","text":"Not regret buying this from this seller. Really trustworthy!","tags":["Great communication","Unique listings"],"event":"MONSTA X, Malaysia","source":"Carousell","screenshot_url":"review-3.jpg","visible":True,"sort_order":5},
]

from i18n import I18N as _I
FAQS = [{"id": f"faq-{i}", "q_en": _I[f"q{i}"][0], "q_zh": _I[f"q{i}"][1], "a_en": _I[f"a{i}"][0], "a_zh": _I[f"a{i}"][1], "visible": True, "sort_order": i} for i in range(1, 7)]
CONTACTS = {
  "whatsapp_number": "+60 12-659 2025",
  "whatsapp_link": "https://wa.me/message/254MFSUP73ZGN1",
  "whatsapp_on": True,
  "instagram_url": "https://www.instagram.com/authentix_my",
  "instagram_handle": "authentix_my",
  "instagram_on": True,
  "carousell_url": "http://carousell.app.link/lHrZAsmCeKb",
  "carousell_on": True,
}
