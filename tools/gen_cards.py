W='/Users/jchung/Desktop/T7/website/assets/fig'
INK='#1c1917'; MUT='#78716c'; UMB='#7c4a1e'; GRN='#6b7f3a'; BLU='#5b7c99'; FRAME='#a8a29e'
F0='#faf7f3'; F1='#f3ece3'; F2='#ede3d6'; F3='#e7e2dc'; F4='#eef0e4'; TAN='#e7d3c2'; YEL='#fde68a'; YELS='#a16207'
def head(markers):
    m=''.join(f'<marker id="{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>' for i,c in markers)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" font-family="Inter, Helvetica, Arial, sans-serif" fill="{INK}"><defs>{m}<pattern id="hatch" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="#c9c2b8" stroke-width="1.2"/></pattern></defs>'
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
m+=f'<rect x="520" y="150" width="262" height="100" rx="8" fill="#fff" stroke="{UMB}" stroke-width="1.5"/>'+T(651,186,'mineralogy',22,UMB,w=700)+T(651,212,'clay minerals · Fe/Al oxides ·',16)+T(651,232,'non-crystalline phases',16)
m+=f'<g stroke="{UMB}" stroke-width="2.4" stroke-dasharray="8 6" fill="none" marker-end="url(#aha)"><path d="M520 190 C 440 190, 360 196, 300 200"/><path d="M560 250 C 560 292, 500 286, 465 286"/></g>'
m+=T(576,308,'MAOM formation · turnover',16,UMB,'start')
m+=f'<g font-size="18"><text x="520" y="400" font-weight="700">calibrated on</text><text x="520" y="430">Δ¹⁴C bulk · MAOM · POM</text><text x="520" y="458">POM / MAOM fractions</text><text x="520" y="486">respiration (Rh)</text><text x="520" y="520" fill="{MUT}" font-size="16">global · four depths · ISRaD, SRDB</text></g>'+T(270,562,'depth not to scale',14,MUT)+'</svg>'
open(f'{W}/model_card.svg','w').write(m)

# ================= CARD 2: MRV =================
c=head([('ah',INK),('ahu',UMB)])
c+=T(140,66,'Measure',30,w=700)+T(400,66,'Model',30,w=700)+T(660,66,'Verify',30,w=700)
for x in (30,290,550): c+=f'<rect x="{x}" y="92" width="220" height="320" rx="12" fill="{F0}" stroke="{FRAME}" stroke-width="1.5"/>'
c+=arrow(254,252,288,252)+arrow(514,252,548,252)
# measure: core, handheld NIR, thermogram
c+=f'<rect x="72" y="130" width="28" height="100" fill="{TAN}" stroke="{UMB}" stroke-width="1.5"/><rect x="72" y="130" width="28" height="30" fill="#b08968"/>'
for k in range(0,101,20): c+=f'<line x1="104" y1="{130+k}" x2="113" y2="{130+k}" stroke="{MUT}" stroke-width="1.5"/>'
c+=T(90,256,'soil cores',18)
c+=f'<g transform="rotate(-20 196 166)"><rect x="166" y="148" width="52" height="36" rx="6" fill="#fff" stroke="{INK}" stroke-width="1.8"/><path d="M184 184 L180 212 L198 212 L194 184 Z" fill="#fff" stroke="{INK}" stroke-width="1.8"/><circle cx="174" cy="178" r="5" fill="none" stroke="{INK}" stroke-width="1.8"/></g>'
c+=f'<g stroke="{MUT}" stroke-width="1" stroke-dasharray="3 3"><line x1="172" y1="186" x2="186" y2="226"/><line x1="172" y1="186" x2="206" y2="226"/></g><rect x="176" y="226" width="60" height="8" fill="{TAN}"/>'
c+=T(196,256,'NIR spectra',18)
c+=f'<rect x="90" y="282" width="130" height="64" fill="#fff" stroke="{FRAME}" stroke-width="1.2"/><path d="M96 342 V288 M96 342 H214" fill="none" stroke="{MUT}" stroke-width="1.2"/><path d="M98 340 C112 340 118 298 128 298 C138 298 142 330 156 328 C172 326 180 306 192 306 C202 306 208 340 212 340" fill="none" stroke="{UMB}" stroke-width="2"/>'
c+=T(140,370,'thermal analysis',18)+T(140,398,'few samples, low cost · lab',16,MUT)
# model
c+=box(306,124,80,48,'POM',YEL,YELS,20)+box(414,124,80,48,'MAOM',TAN,UMB,20)+arrow(386,148,412,148)
c+=f'<rect x="330" y="196" width="140" height="90" fill="#fff" stroke="{FRAME}" stroke-width="1.2"/><path d="M338 280 V204 M338 280 H462" fill="none" stroke="{MUT}" stroke-width="1.2"/><line x1="340" y1="278" x2="460" y2="206" stroke="{FRAME}" stroke-dasharray="5 4"/>'
for px,py in [(.1,.86),(.2,.78),(.3,.68),(.38,.62),(.46,.52),(.52,.5),(.6,.4),(.7,.3),(.8,.22),(.9,.12),(.42,.6),(.66,.42),(.26,.74)]:
    c+=f'<circle cx="{330+px*140:.0f}" cy="{196+py*90:.0f}" r="3" fill="{UMB}"/>'
c+=T(400,302,'modelled vs observed',16,MUT)+T(400,346,'process model,',20)+T(400,372,'field-calibrated',20)+T(400,398,'uncertainty by Monte Carlo',16,MUT)
# verify
c+=f'<line x1="585" y1="320" x2="735" y2="320" stroke="{FRAME}" stroke-width="1.5"/>'
c+=f'<line x1="585" y1="224" x2="735" y2="224" stroke="{UMB}" stroke-width="1.5" stroke-dasharray="6 4"/>'
c+=f'<rect x="606" y="250" width="38" height="70" fill="{TAN}" stroke="{UMB}" stroke-width="1.5"/><rect x="676" y="206" width="38" height="114" fill="{UMB}"/>'
c+=f'<g stroke="{INK}" stroke-width="2"><line x1="625" y1="234" x2="625" y2="266"/><line x1="619" y1="234" x2="631" y2="234"/><line x1="619" y1="266" x2="631" y2="266"/><line x1="695" y1="190" x2="695" y2="222"/><line x1="689" y1="190" x2="701" y2="190"/><line x1="689" y1="222" x2="701" y2="222"/></g>'
c+=T(625,342,'before',18,MUT)+T(695,342,'after',18,MUT)
c+=f'<line x1="586" y1="366" x2="608" y2="366" stroke="{UMB}" stroke-width="1.5" stroke-dasharray="6 4"/>'+T(614,372,'detectable change',16,UMB,'start')
c+=T(660,400,'stock change ± 95 % CI',18)
c+=T(400,470,'Low-cost, high-efficiency MRV',24,UMB,w=700)+T(400,500,'for soil-based carbon dioxide removal',24,UMB,w=700)+T(400,540,'Sejong Science Fellowship · 2024–2028',20,MUT)+'</svg>'
open(f'{W}/mrv_card.svg','w').write(c)

# ================= CARD 3: soils shaped by people (cross-section) =================
p=head([('ah',INK),('ahb',BLU)])
p+=f'<rect x="0" y="310" width="800" height="110" fill="{F1}"/><rect x="0" y="420" width="800" height="120" fill="{F0}"/>'
p+=f'<path d="M0 420 Q100 414 200 420 T400 420 T600 420 T800 420" fill="none" stroke="#b8ad9f" stroke-width="1.5"/>'
p+=f'<rect x="400" y="310" width="400" height="46" fill="{F2}"/>'
p+=f'<rect x="0" y="310" width="150" height="35" fill="url(#hatch)"/><rect x="250" y="310" width="150" height="35" fill="url(#hatch)"/>'
p+=f'<line x1="0" y1="310" x2="800" y2="310" stroke="{MUT}" stroke-width="2"/>'
p+=f'<line x1="400" y1="250" x2="400" y2="540" stroke="#c9c2b8" stroke-width="1" stroke-dasharray="4 4"/>'
p+=f'<rect x="0" y="298" width="150" height="12" fill="{F3}" stroke="{FRAME}" stroke-width="1.2"/><rect x="250" y="298" width="150" height="12" fill="{F3}" stroke="{FRAME}" stroke-width="1.2"/>'
p+=f'<rect x="10" y="170" width="38" height="128" fill="none" stroke="#d6d3d1" stroke-width="1.5"/><rect x="340" y="190" width="48" height="108" fill="none" stroke="#d6d3d1" stroke-width="1.5"/>'
p+=f'<path d="M194 310 L197 205 L203 205 L206 310 Z" fill="{UMB}"/><path d="M200 98 C230 96 262 118 262 148 C266 176 244 200 212 204 C186 206 160 198 146 180 C132 160 138 122 164 106 C176 98 190 96 200 98 Z" fill="{F4}" stroke="{GRN}" stroke-width="1.5"/><g stroke="{UMB}" stroke-width="1.2" fill="none"><path d="M200 205 L176 150"/><path d="M200 205 L200 128"/><path d="M200 205 L226 152"/></g>'
p+=f'<g stroke="{UMB}" stroke-width="1.5" stroke-linecap="round" fill="none"><path d="M200 312 Q180 340 160 372"/><path d="M200 312 Q222 338 240 368"/><path d="M200 312 Q196 360 190 400"/><path d="M202 312 Q232 318 252 342"/></g>'
for i,x in enumerate(range(445,760,60)):
    h=268+(i%3)*4
    p+=f'<line x1="{x}" y1="310" x2="{x}" y2="{h}" stroke="{GRN}" stroke-width="1.8"/><path d="M{x} 292 q -16 -6 -20 -18 M{x} 284 q 16 -6 20 -18 M{x} {h+4} q 2 -10 0 -16" fill="none" stroke="{GRN}" stroke-width="1.8" stroke-linecap="round"/>'
import random; random.seed(4)
n=0
while n<16:
    bx=random.uniform(410,790); by=random.uniform(316,352)
    if bx>655 and by>336: continue
    n+=1; p+=f'<rect x="{bx:.0f}" y="{by:.0f}" width="7" height="3" rx="1.5" fill="{INK}" opacity=".7" transform="rotate({random.uniform(-40,40):.0f} {bx:.0f} {by:.0f})"/>'
# water
p+=f'<g stroke="{BLU}" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#ahb)"><line x1="75" y1="312" x2="75" y2="340"/><line x1="80" y1="304" x2="30" y2="304"/><line x1="560" y1="318" x2="560" y2="410"/><line x1="660" y1="318" x2="660" y2="410"/></g>'
# gases & inputs
p+=arrow(272,296,272,240)+arrow(470,296,470,240)+arrow(580,296,580,240)+arrow(170,232,170,296)+arrow(770,232,770,296)
p+=T(284,240,'CO₂',24,anchor='start',w=600)+T(482,240,'CO₂',24,anchor='start',w=600)+T(592,240,'N₂O',24,anchor='start',w=600)
p+=T(160,226,'litter · mulch',20,anchor='end')+T(760,226,'fertiliser',20,anchor='end')
p+=T(14,392,'sealed · compacted',20,MUT,'start',halo=True)+T(762,378,'biochar',20,UMB,'end',halo=True)+f'<line x1="686" y1="372" x2="666" y2="352" stroke="{UMB}" stroke-width="1"/>'
p+=T(560,440,'water',20,BLU,'start',halo=True)+T(258,372,'roots',20,MUT,'start',halo=True)
p+=T(200,578,'urban green space',22,MUT)+T(600,578,'cropland · biochar',22,MUT)+'</svg>'
open(f'{W}/people_card.svg','w').write(p)
print('cards ok')
