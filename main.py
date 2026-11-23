"""News Image 22 Nov 2026 — MakeFun bounty news-image-20261122.

Regenerates entry.png deterministically from the STORIES data below.
No network, no randomness, no timestamps in the PNG: two runs
produce byte-identical output. Run:  python3 main.py
Output: entry.png next to this file, and /output/entry.png if writable.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1024, 1024

TITLE = "Sunday 22 November 2026: COP31 collapses with no deal, Iran hits Bahrain site and 2 tankers in Hormuz, Mexico captures 'El Chapo Isidro' — and 41 more stories"

# (number, region, headline, detail)
STORIES = [
    (1, "CLIMATE", "COP31 collapses with no deal", "Antalya: ~200 nations, EU + ~130 reject draft with no fossil fuels; longest summit, 2 days overtime."),
    (2, "MIDEAST", "Iran hits Bahrain site; 2 tankers hit in Hormuz", "Bahrain: 2 wounded at Sitra industrial site; tankers hit Sat; 25 shipping incidents in a week."),
    (3, "AMERICAS", "Mexico captures 'El Chapo Isidro'", "Sinaloa: 11 killed incl. 4 soldiers; $5m bounty; FBI Top 10; flown to Mexico City 05:20."),
    (4, "MIDEAST", "Trump dares Iran to break US port blockade", "Seeks permanent deal on nuclear programme; decision may wait until 2027."),
    (5, "MIDEAST", "Houthis say they hit Saudi refinery", "Rabigh: Saudi intercepts missiles; Gulf states condemn Bahrain attack."),
    (6, "MIDEAST", "Gaza strikes continue despite truce", "3 soup-kitchen workers killed; truce toll since Oct 2025 now 1,671."),
    (7, "MIDEAST", "Settlers torch 12 vehicles in 4 West Bank villages", "Israel opens inquiry after overnight attacks near Ramallah."),
    (8, "MIDEAST", "Basra power station fire kills 4", "Iraq: 35 injured at Hartha plant north of Basra."),
    (9, "MIDEAST", "Iran begins rationing electricity", "Tehran: power rationing as Gulf conflict strains grid."),
    (10, "MIDEAST", "Eisenkot calls settler attacks 'terrorism'", "Israeli opposition leader condemns West Bank attacks."),
    (11, "EUROPE", "Russian drone hits Dymer flats; 14 missing", "Near Kyiv: 5-storey block partly collapses; 2 killed, 4 wounded."),
    (12, "EUROPE", "Russian warship hit at Benghazi, Libya", "Suspected Ukrainian sea drones strike docked vessel; 2nd ship targeted."),
    (13, "EUROPE", "Sparta II burns in Gulf of Finland", "Sanctioned Russian cargo ship still burning a day after drone strike; crew evacuated."),
    (14, "EUROPE", "2 Russian missiles + drone fall in Poland", "NATO calls it a 'grave violation'; no injuries; jets scrambled."),
    (15, "EUROPE", "Shenzhen summit fallout: no Ukraine breakthrough", "Trump, Xi, Putin: nuclear declaration, but no arms limits, no timeline."),
    (16, "EUROPE", "Spain: snap election 29 Nov; PP ahead of PSOE", "Banking levy extended to 2027 to raise ~EUR 1.4bn for housing."),
    (17, "EUROPE", "UK and EU seek closer post-Brexit ties", "London: new cooperation deal pursued after Brexit."),
    (18, "EUROPE", "Thousands protest in Istanbul over media takeover", "Turkey: crowds rally against press crackdown."),
    (19, "EUROPE", "Denmark expels Russian defence attache", "Copenhagen restricts visas after alleged assassination plot thwarted."),
    (20, "EUROPE", "Russia revives pre-2022 NATO demands", "Moscow seeks rollback of NATO forces in Ukraine security talks."),
    (21, "AMERICAS", "Democrats win 258 House seats", "Largest US House majority since 1992."),
    (22, "AMERICAS", "FBI probes suspected hack of crime database", "National Crime Information Center breach under investigation."),
    (23, "AMERICAS", "Seattle airport immigration arrests draw outcry", "ICE arrests at Seattle airport spark protests."),
    (24, "AMERICAS", "Peru quake 6.7 hits Junin Andes", "15 injured, no deaths; adobe buildings cracked in Sacred Valley."),
    (25, "AMERICAS", "Brazil storm kills 3 in Tupancireta", "Gusts 114 km/h; thousands of buildings damaged in Rio Grande do Sul."),
    (26, "AMERICAS", "Bolsonaro stable in intensive care", "Brasilia: ex-president, 27-year sentence, acute abdominal obstruction."),
    (27, "AMERICAS", "Argentina approves $50bn LNG project", "Buenos Aires: major energy export deal green-lit."),
    (28, "AMERICAS", "Haiti strikes prison deal with El Salvador", "New prisons planned amid gang violence and state crisis."),
    (29, "ASIA-PAC", "Indonesia candy factory fire: 3 dead, 36 missing", "Banten, west of Jakarta: rescuers search ruins in Cikande."),
    (30, "ASIA-PAC", "Manipur toxic alcohol: 11 dead, 180+ in hospital", "India: contaminated local liquor; chief minister orders inquiry."),
    (31, "ASIA-PAC", "S Korea minister resigns over AI exam chaos", "College entrance exam rules changed days before test to stop AI cheating."),
    (32, "ASIA-PAC", "China-Japan ties worsen over Taiwan, minerals", "Beijing curbs critical-mineral exports after Takaichi remarks."),
    (33, "ASIA-PAC", "Mongolia faces snap presidential vote", "Ulaanbaatar: outgoing leader calls for constitutional reform."),
    (34, "ASIA-PAC", "Hong Kong holds Election Committee vote", "City votes for committee that picks its leader."),
    (35, "ASIA-PAC", "Garment strikes and clashes in Bangladesh", "Gazipur: workers protest, clashes reported."),
    (36, "ASIA-PAC", "EU-Indonesia trade deal after ~10 years", "Tariffs scrapped on up to 98.5% of goods."),
    (37, "AFRICA", "Nigeria boat capsizes: 24 dead", "Wooden boat carrying funeral mourners sinks in southern Nigeria."),
    (38, "AFRICA", "Drones hit Khartoum homes + UN building", "Sudan: ~1,630 civilian drone deaths Jan-Oct 2026, UN data."),
    (39, "AFRICA", "ICJ genocide ruling: reactions continue", "Ruling 19 Nov: Myanmar guilty on Rohingya; rights groups urge sanctions."),
    (40, "AFRICA", "S Africa mourns Mlambo-Ngcuka, 71", "First female deputy president; led UN Women 2013-2021."),
    (41, "MARKETS", "Stocks fall as AI sell-off deepens", "S&P 500 -3.7%, Nikkei -5.06%; worst week since Apr 2025."),
    (42, "SCIENCE", "BepiColombo enters orbit around Mercury", "ESA-JAXA probe arrives after 8-year, 6bn-mile journey."),
    (43, "SPORT", "Liverpool thrash Man Utd 4-0 at Anfield", "Yoro red 8'; Szoboszlai, Wirtz, Ngumoha, Munoz score."),
    (44, "SPORT", "Verstappen wins Las Vegas GP; Alcaraz wins ATP Finals", "F1: Verstappen from pole; tennis: Alcaraz beats Zverev 6-2, 7-6."),
]

REGION_COLORS = {
    "CLIMATE": (0, 120, 90),
    "MIDEAST": (178, 34, 34),
    "EUROPE": (30, 80, 180),
    "AMERICAS": (0, 130, 110),
    "ASIA-PAC": (200, 110, 0),
    "AFRICA": (120, 60, 160),
    "MARKETS": (90, 90, 90),
    "SCIENCE": (0, 110, 160),
    "SPORT": (170, 30, 110),
}
REGION_LABELS = [
    ("CLIMATE", "Climate"), ("MIDEAST", "Middle East"), ("EUROPE", "Europe"),
    ("AMERICAS", "Americas"), ("ASIA-PAC", "Asia-Pacific"), ("AFRICA", "Africa & Justice"),
    ("MARKETS", "Markets"), ("SCIENCE", "Science"), ("SPORT", "Sport"),
]

def font(name, size):
    path = "/usr/share/fonts/truetype/dejavu/%s" % name
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def build():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    fb = lambda s: font("DejaVuSans-Bold.ttf", s)
    fr = lambda s: font("DejaVuSans.ttf", s)
    # Header
    d.rectangle([0, 0, W, 108], fill=(11, 31, 58))
    d.rectangle([0, 108, W, 114], fill=(255, 196, 0))
    d.text((24, 18), "SUNDAY  22  NOVEMBER  2026", font=fb(34), fill=(255, 255, 255))
    d.text((24, 66), "WORLD IN ONE PICTURE  •  44 STORIES  •  9 REGIONS  •  DATE-CHECKED", font=fb(16), fill=(255, 196, 0))
    d.text((848, 16), "44", font=fb(48), fill=(255, 196, 0))
    d.text((908, 30), "STORIES", font=fb(18), fill=(255, 255, 255))
    d.text((848, 70), "BBC • Reuters • AP", font=fr(12), fill=(200, 210, 225))
    # Leads
    y = 122
    d.text((24, y), "THE 3 LEADS", font=fb(14), fill=(11, 31, 58))
    d.text((560, y), "SCHEMATIC PANELS — NOT PHOTOS", font=fr(11), fill=(120, 120, 120))
    y += 22
    lead_h = 56
    for i, s in enumerate(STORIES[:3]):
        _, region, head, detail = s
        col = REGION_COLORS[region]
        d.rounded_rectangle([24, y, 1000, y + lead_h], radius=8, fill=(245, 247, 250), outline=col, width=2)
        d.ellipse([36, y + 10, 72, y + 46], fill=col)
        d.text((54, y + 15), str(i + 1), font=fb(20), fill=(255, 255, 255), anchor="mm")
        d.text((84, y + 6), head, font=fb(18), fill=(11, 31, 58))
        for j, line in enumerate(wrap(d, detail, fr(12), 880)):
            d.text((84, y + 30 + j * 14), line, font=fr(12), fill=(40, 40, 40))
        y += lead_h + 6
    # Timeline strip
    d.rounded_rectangle([24, y, 1000, y + 40], radius=8, fill=(11, 31, 58))
    d.text((36, y + 5), "HOW THE DAY UNFOLDED", font=fb(12), fill=(255, 196, 0))
    steps = ["EARLY: COP31 stalls", "MORNING: Tankers hit", "MIDDAY: Chapo confirmed", "AFTERNOON: Dymer, 14 missing", "EVENING: COP31 collapses"]
    x = 36
    for si, st in enumerate(steps):
        d.text((x, y + 21), st, font=fr(11), fill=(255, 255, 255))
        x += d.textlength(st, font=fr(11)) + 20
        if si < len(steps) - 1:
            d.text((x - 13, y + 21), "›", font=fb(12), fill=(255, 196, 0))
    y += 48
    # Region legend
    x = 24
    d.text((x, y), "REGIONS:", font=fb(12), fill=(11, 31, 58))
    x += 72
    for key, label in REGION_LABELS:
        col = REGION_COLORS[key]
        d.ellipse([x, y + 2, x + 11, y + 13], fill=col)
        d.text((x + 15, y), label, font=fr(12), fill=(30, 30, 30))
        x += 15 + d.textlength(label, font=fr(12)) + 18
    y += 20
    # Two-column list, stories 4-44
    rest = STORIES[3:]
    cols = [rest[:21], rest[21:]]
    col_x = [24, 522]
    col_w = 478
    row_h = 26
    for ci, col_items in enumerate(cols):
        cx = col_x[ci]
        cy = y
        for (num, region, head, detail) in col_items:
            col = REGION_COLORS[region]
            # number badge
            d.ellipse([cx, cy + 1, cx + 21, cy + 21], fill=col)
            d.text((cx + 11, cy + 11), str(num), font=fb(10), fill=(255, 255, 255), anchor="mm")
            head_lines = wrap(d, head, fb(11), col_w - 30)
            det_lines = wrap(d, detail, fr(10), col_w - 30)
            yy = cy
            for ln in head_lines[:1]:
                d.text((cx + 28, yy), ln, font=fb(11), fill=(15, 15, 15))
                yy += 13
            for ln in det_lines[:1]:
                d.text((cx + 28, yy), ln, font=fr(10), fill=(70, 70, 70))
                yy += 12
            cy += row_h
    # Footer
    d.rectangle([0, 992, W, H], fill=(11, 31, 58))
    d.text((24, 1000), "Sources: BBC, Reuters, Al Jazeera, AP, AFP, Euronews, One Turn (22 Nov 2026 edition)  •  All 44 dated 22 Nov 2026; ICJ item = reactions on 22 Nov to 19 Nov ruling.", font=fr(11), fill=(220, 225, 235))
    return img

def main():
    img = build()
    assert img.size == (1024, 1024)
    dst_local = os.path.join(HERE, "entry.png")
    img.save(dst_local, format="PNG")
    print("wrote %s (%d bytes)" % (dst_local, os.path.getsize(dst_local)))
    try:
        os.makedirs("/output", exist_ok=True)
        dst = "/output/entry.png"
        img.save(dst, format="PNG")
        print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
    except OSError as e:
        print("skip /output: %s" % e)

if __name__ == "__main__":
    main()
