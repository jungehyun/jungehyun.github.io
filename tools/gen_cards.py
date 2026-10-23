W='/Users/jchung/Desktop/T7/website/assets/fig'
INK='#1c1917'; MUT='#78716c'; UMB='#7c4a1e'; GRN='#6b7f3a'; BLU='#5b7c99'; FRAME='#a8a29e'
F0='#faf7f3'; F1='#f3ece3'; F2='#ede3d6'; F3='#e7e2dc'; F4='#eef0e4'; TAN='#e7d3c2'; YEL='#fde68a'; YELS='#a16207'
def head(markers):
    m=''.join(f'<marker id="{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>' for i,c in markers)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" font-family="Inter, Helvetica, Arial, sans-serif" fill="{INK}"><defs>{m}<pattern id="hatch" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="#c9c2b8" stroke-width="1.2"/></pattern><pattern id="hatch2" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="#c9a27a" stroke-width="1.4"/></pattern></defs>'
HALO='paint-order="stroke" stroke="#fff" stroke-width="4" stroke-linejoin="round"'
def T(x,y,s,size=22,fill=INK,anchor='middle',w=400,halo=False):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}" {HALO if halo else ""}>{s}</text>'
def box(x,y,w,h,label,fill,stroke,fs=22):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'+T(x+w/2,y+h/2+fs*.36,label,fs,w=700)
def arrow(x1,y1,x2,y2,c=INK,mk='ah',sw=2.4,dash=''):
    d=(' stroke-dasharray="%s"'%dash) if dash else ''
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s marker-end="url(#%s)"/>'%(x1,y1,x2,y2,c,sw,d,mk)

# ================= CARD 1: model =================
m=head([('ah',INK),('ahg',GRN),('ahb',BLU),('aha',UMB)])
m+=f'<rect x="60" y="70" width="420" height="470" fill="{F0}" stroke="{FRAME}" stroke-width="1.5"/>'
for yy in (340,405,470): m+=f'<line x1="60" y1="{yy}" x2="480" y2="{yy}" stroke="#c9c2b8" stroke-width="1"/>'
m+=f'<g font-size="16" fill="{MUT}" text-anchor="end"><text x="52" y="76">0 cm</text><text x="52" y="345">15</text><text x="52" y="410">30</text><text x="52" y="475">60</text><text x="52" y="545">100</text></g>'
m+=T(200,34,'plant litter',22)+arrow(200,42,200,94,GRN,'ahg')
m+=box(120,98,160,46,'litter',F4,GRN)
m+=f'<circle cx="270" cy="200" r="28" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'+T(270,206,'decomp.',14,MUT)
m+=arrow(215,146,249,179)
m+=arrow(292,182,372,118)+T(380,112,'CO₂ (Rh)',22,anchor='start')
m+=f'<line x1="270" y1="228" x2="270" y2="246" stroke="{INK}" stroke-width="2.4"/><line x1="115" y1="246" x2="420" y2="246" stroke="{INK}" stroke-width="2.4"/>'
for x in (115,205,320,420): m+=arrow(x,246,x,262)
m+=box(72,264,86,46,'BIO',YEL,YELS)+box(162,264,86,46,'oPOM',YEL,YELS)+box(277,264,86,46,'HUM',TAN,UMB)+box(377,264,86,46,'PAS',TAN,UMB)
m+=T(160,332,'POM',16,MUT)+T(370,332,'MAOM',16,MUT)
for yy in (378,443,512): m+=T(270,yy,'same pools and flows',16,'#a8a29e')
for yy,sw in ((372,2.4),(437,2.4),(506,2.4)): m+=arrow(30,yy,82,yy,GRN,'ahg',sw)
m+=T(30,580,'root input',16,GRN,'start')
for y1,y2 in ((322,364),(384,430),(450,498),(518,568)): m+=arrow(455,y1,455,y2,BLU,'ahb')
m+=T(478,580,'transport',16,BLU,'start')
m+=f'<rect x="520" y="140" width="262" height="130" rx="8" fill="#fff" stroke="{UMB}" stroke-width="1.5"/>'+T(651,164,'mineralogy',22,UMB,w=700)
m+=f'<rect x="546" y="208" width="30" height="30" fill="{TAN}"/><rect x="546" y="186" width="30" height="22" fill="#c9a27a"/><rect x="546" y="170" width="30" height="16" fill="{UMB}"/><rect x="546" y="170" width="30" height="68" fill="none" stroke="{UMB}" stroke-width="1.2"/>'+T(561,256,'minerals',15,MUT)
m+=T(596,222,'×',22)+f'<rect x="616" y="180" width="30" height="58" fill="#d9c2a8" stroke="{UMB}" stroke-width="1.5"/>'+T(631,256,'sorption',15,MUT)
m+=T(668,222,'→',22)+f'<rect x="690" y="168" width="30" height="70" fill="{UMB}"/>'+T(705,256,'capacity',15,MUT)
m+=f'<g stroke="{UMB}" stroke-width="2.4" stroke-dasharray="8 6" fill="none" marker-end="url(#aha)"><path d="M520 200 C 440 200, 360 198, 300 200"/><path d="M520 262 C 500 290, 488 286, 466 286"/></g>'
m+=T(651,300,'MAOM formation · turnover',16,UMB)
m+=f'<g font-size="18"><text x="520" y="400" font-weight="700">calibrated on</text><text x="520" y="428">Δ¹⁴C bulk · MAOM · POM</text><text x="520" y="454">POM / MAOM fractions</text><text x="520" y="480">respiration (Rh)</text><text x="520" y="506">SOC stock (Δ¹⁴C sites)</text><text x="520" y="536" fill="{MUT}" font-size="16">global · four depths · ISRaD, SRDB</text></g>'+T(270,562,'depth not to scale',14,MUT)+'</svg>'
open(f'{W}/model_card.svg','w').write(m)

# ================= CARD 2: MRV (hero chart) =================
c=head([('ah',INK)])
c+=f'<line x1="110" y1="440" x2="750" y2="440" stroke="{INK}" stroke-width="1.5" marker-end="url(#ah)"/><line x1="110" y1="440" x2="110" y2="80" stroke="{INK}" stroke-width="1.5" marker-end="url(#ah)"/>'
c+=f'<text x="72" y="260" font-size="20" fill="{MUT}" text-anchor="middle" transform="rotate(-90 72 260)">soil carbon stock</text>'
c+=T(160,464,'2024',18,MUT)+T(720,464,'2028',18,MUT)
# baseline, fan, model line
c+=f'<line x1="160" y1="360" x2="750" y2="360" stroke="{FRAME}" stroke-width="1" stroke-dasharray="4 4"/>'
c+=f'<path d="M160 360 C 350 330, 560 270, 720 168 L720 262 C 560 318, 350 352, 160 360 Z" fill="{TAN}" opacity=".7"/>'
c+=f'<path d="M160 360 C 350 340, 560 294, 720 210" fill="none" stroke="{UMB}" stroke-width="2.4"/>'
c+=f'<line x1="110" y1="290" x2="750" y2="290" stroke="{UMB}" stroke-width="1.5" stroke-dasharray="6 4"/>'
# cores (sampling campaigns) + connectors + points
for x,py,wh in ((152,360,18),(432,300,22),(712,206,26)):
    cx=x+8
    c+=f'<line x1="{cx}" y1="396" x2="{cx}" y2="{py+wh+4}" stroke="{FRAME}" stroke-width="1" stroke-dasharray="2 3"/>'
    c+=f'<rect x="{x}" y="396" width="16" height="44" fill="{TAN}" stroke="{UMB}" stroke-width="1.5"/><rect x="{x}" y="396" width="16" height="12" fill="#b08968"/>'
    c+=f'<line x1="{cx}" y1="{py-wh}" x2="{cx}" y2="{py+wh}" stroke="{INK}" stroke-width="2"/><line x1="{cx-6}" y1="{py-wh}" x2="{cx+6}" y2="{py-wh}" stroke="{INK}" stroke-width="2"/><line x1="{cx-6}" y1="{py+wh}" x2="{cx+6}" y2="{py+wh}" stroke="{INK}" stroke-width="2"/><circle cx="{cx}" cy="{py}" r="5" fill="{INK}"/>'
c+=T(440,490,'measured: soil cores · NIR · thermal analysis',20)
c+=T(470,192,'modelled ± Monte Carlo',18,UMB,'start')+T(118,278,'target: detectable change',18,UMB,'start')
c+=f'<path d="M742 360 H750 V210 H742" fill="none" stroke="{INK}" stroke-width="1.5"/><text x="766" y="285" font-size="20" font-weight="600" fill="{INK}" text-anchor="middle" transform="rotate(-90 766 285)">verified removal</text>'
c+=T(400,528,'Low-cost, high-efficiency MRV',22,UMB,w=700)+T(400,554,'for soil-based carbon dioxide removal',22,UMB,w=700)+T(400,586,'Sejong Science Fellowship · 2024–2028 · design concept',18,MUT)+'</svg>'
open(f'{W}/mrv_card.svg','w').write(c)

# ================= CARD 3: soils shaped by people (full-bleed profile) =================
p=head([('ah',INK),('ahb',BLU)])
p+=T(200,40,'city · street tree',22,MUT)+T(600,40,'upland field · biochar',22,MUT)
p+='<g transform="translate(0 30)">'
p+=f'<rect x="0" y="300" width="800" height="100" fill="#d9c2a8"/><rect x="0" y="400" width="800" height="230" fill="{TAN}"/>'
p+=f'<path d="M0 400 Q100 394 200 400 T400 400 T600 400 T800 400" fill="none" stroke="#b8946f" stroke-width="1.2"/>'
p+=f'<rect x="400" y="300" width="400" height="40" fill="#cbb196"/>'
p+=f'<rect x="0" y="300" width="150" height="30" fill="#c3a98d"/><rect x="250" y="300" width="150" height="30" fill="#c3a98d"/>'
p+=f'<rect x="0" y="80" width="56" height="208" fill="{F3}"/><rect x="350" y="150" width="50" height="138" fill="{F3}"/>'
p+=f'<rect x="0" y="288" width="150" height="12" fill="{FRAME}"/><rect x="250" y="288" width="150" height="12" fill="{FRAME}"/>'
p+=f'<line x1="0" y1="300" x2="800" y2="300" stroke="{INK}" stroke-width="2.4"/>'
p+=f'<path d="M192 300 L196 190 L204 190 L208 300 Z" fill="{UMB}"/>'
p+=f'<g transform="translate(200 150) scale(1.25) translate(-200 -150)"><path d="M200 98 C230 96 262 118 262 148 C266 176 244 200 212 204 C186 206 160 198 146 180 C132 160 138 122 164 106 C176 98 190 96 200 98 Z" fill="#cdd5b8" stroke="{GRN}" stroke-width="1.6"/></g>'
p+=f'<g stroke="{UMB}" stroke-width="1.5" fill="none"><path d="M200 192 L176 140"/><path d="M200 192 L200 118"/><path d="M200 192 L226 142"/></g>'
p+=f'<g stroke="{UMB}" stroke-width="2" stroke-linecap="round" fill="none"><path d="M200 302 Q198 340 206 374"/><path d="M200 302 Q226 336 242 366"/><path d="M200 302 Q206 360 216 398"/><path d="M202 302 Q232 312 248 328"/></g>'
for i,x in enumerate(range(445,760,60)):
    h=244+(i%3)*4
    p+=f'<line x1="{x}" y1="300" x2="{x}" y2="{h}" stroke="{GRN}" stroke-width="2.4"/><path d="M{x} 280 q -18 -6 -22 -20 M{x} 270 q 18 -6 22 -20 M{x} {h+6} q 2 -12 0 -18" fill="none" stroke="{GRN}" stroke-width="2.4" stroke-linecap="round"/>'
import random; random.seed(7)
for k in range(13):
    bx=416+k*29+random.uniform(-8,8); by=random.uniform(306,334)
    p+=f'<rect x="{bx:.0f}" y="{by:.0f}" width="8" height="3" rx="1.5" fill="{INK}" opacity=".7" transform="rotate({random.uniform(-40,40):.0f} {bx:.0f} {by:.0f})"/>'
p+=f'<rect x="652" y="328" width="8" height="3" rx="1.5" fill="{INK}" opacity=".7" transform="rotate(-20 656 330)"/>'
p+=f'<g stroke="{BLU}" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#ahb)"><line x1="120" y1="312" x2="120" y2="336"/><line x1="176" y1="312" x2="176" y2="392"/><line x1="640" y1="312" x2="640" y2="420"/><line x1="700" y1="312" x2="700" y2="420"/></g>'
p+=arrow(290,290,290,230)+arrow(560,240,560,180)+arrow(590,240,590,180)+arrow(180,230,180,290)
p+=T(302,236,'CO₂',24,anchor='start',w=600)+T(602,186,'CO₂ · N₂O',24,anchor='start',w=600)
p+=T(168,252,'litter',20,anchor='end',halo=True)
p+=T(10,362,'sealed · compacted',16,MUT,'start',halo=True)+T(184,404,'water',18,BLU,'start',halo=True)
p+=T(762,378,'biochar',20,UMB,'end',halo=True)+f'<line x1="686" y1="366" x2="662" y2="336" stroke="{UMB}" stroke-width="1"/>'
p+=T(400,526,'measured: carbon forms · pollutants · water · nutrients',20,MUT,halo=True)+'</g></svg>'
open(f'{W}/people_card.svg','w').write(p)
print('cards ok')
