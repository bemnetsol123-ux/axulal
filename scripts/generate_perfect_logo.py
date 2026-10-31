import os, sys, math
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

# Colors from official branding
# Charcoal: Warm architectural carbon
COLOR_CHARCOAL = "#322D29"
COLOR_CHARCOAL_LIGHT = "#3E3834"
COLOR_CHARCOAL_DARK = "#24201D"

# Violet: Imperial Ethiopian Royal Violet
COLOR_VIOLET = "#4B287B"
COLOR_VIOLET_LIGHT = "#5C2F98"
COLOR_VIOLET_DARK = "#3B1F63"

# Accent & Whites
COLOR_WHITE = "#FFFFFF"
COLOR_PLATINUM = "#F1F5F9"
COLOR_TITANIUM = "#E2E8F0"

# Load Font for vector glyph extraction
font = TTFont('C:/Windows/Fonts/ETH_B_GOFA.ttf')
glyph_set = font.getGlyphSet()
cmap = font.getBestCmap()
hmtx = font['hmtx']
upm = font['head'].unitsPerEm # 2048

def get_glyph_path(ch):
    gid = cmap[ord(ch)]
    pen = SVGPathPen(glyph_set)
    glyph = glyph_set[gid]
    glyph.draw(pen)
    adv, lsb = hmtx[gid]
    return pen.getCommands(), adv, lsb

# Let's build the SVG definitions
# Canvas 800 x 720 (High Definition ViewBox)
# Center X = 400
# Emblem Top = 60, Emblem Baseline = 460 (Height = 400)
# Text Baseline = 540

def generate_svg(theme="standard"):
    charcoal = COLOR_CHARCOAL if theme != "white" else COLOR_PLATINUM
    violet = COLOR_VIOLET if theme != "white" else "#8B5CF6"
    text_color = COLOR_CHARCOAL if theme != "white" else COLOR_WHITE
    sub_color = "#64748B" if theme != "white" else "#94A3B8"

    # Precise geometric parameters (all in 800x720 canvas)
    # The emblem is based on 60-degree equilateral geometry
    # Tan(60) = sqrt(3) ~ 1.7320508
    # Sin(60) ~ 0.8660254
    # Cos(60) = 0.5
    
    # Mathematical vertices for the two interlocking structural chevrons:
    # 1. Charcoal Beam:
    # Top Apex: (384, 60)
    # Right top slope down at 60 deg to (417, 117)
    # Inner left slope down-left at 60 deg to (263, 384)
    # Top of horizontal bar at Y = 384, extends right to (455, 384)
    # Right cut slopes down-right at 60 deg to (491, 446)
    # Baseline at Y = 446, extends left to (225, 446)
    # Bottom-left rounded corner from (225, 446) curving up to (190, 396)
    # Outer left slope goes from (190, 396) up-right at 60 deg to Top Apex (384, 60)
    
    # 2. Violet Chevron:
    # Outer Top Apex: (444, 172)
    # Outer Right slope down-right at 60 deg to (602, 446)
    # Right bottom flat cut: (602, 446) to (526, 446)
    # Inner Right slope up-left at 60 deg to Inner Apex (444, 304)
    # Inner Left slope down-left at 60 deg to (362, 446)
    # Left bottom flat cut: (362, 446) to (286, 446)
    # Outer Left slope up-right at 60 deg to Outer Top Apex (444, 172)
    
    # Notice that the left leg of the Violet chevron passes over the Charcoal bottom bar (Y=384 to 446)
    # flawlessly interlocking!
    
    # Let's extract text glyphs for 'አክሱላል:AXULAL'
    # Scale for glyphs: we want text height ~ 48px
    # Font upm = 2048, so scale s = 48 / 2048 * 1.5 ~ 0.035
    s = 0.032
    # Baseline Y = 560
    
    # Build glyphs SVG group
    text_chars = ['አ', 'ክ', 'ሱ', 'ላ', 'ል', ':', 'A', 'X', 'U', 'L', 'A', 'L']
    
    # Compute total width to center it under emblem (around X = 395)
    total_w = 0
    glyph_items = []
    for ch in text_chars:
        cmd, adv, lsb = get_glyph_path(ch)
        glyph_items.append((ch, cmd, adv, lsb))
        total_w += adv * s
    
    start_x = 395 - (total_w / 2)
    
    text_svg = []
    curr_x = start_x
    for ch, cmd, adv, lsb in glyph_items:
        # Extra spacing around colon if needed
        if ch == ':':
            curr_x += 4
        text_svg.append(f'<g transform="translate({curr_x:.2f}, 560) scale({s:.5f}, {-s:.5f})"><path d="{cmd}" fill="{text_color}" /></g>')
        curr_x += adv * s
        if ch == ':':
            curr_x += 4
            
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 660" width="100%" height="100%" style="background:transparent;">
  <defs>
    <!-- Subtle gradients for high-end depth -->
    <linearGradient id="charcoalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{charcoal}" />
      <stop offset="100%" stop-color="{COLOR_CHARCOAL_DARK if theme != 'white' else '#CBD5E1'}" />
    </linearGradient>
    <linearGradient id="violetGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_VIOLET_LIGHT if theme != 'white' else '#A78BFA'}" />
      <stop offset="100%" stop-color="{violet}" />
    </linearGradient>
    <filter id="softShadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="rgba(0,0,0,0.18)" />
    </filter>
  </defs>

  <g id="axulal-emblem" filter="url(#softShadow)">
    <!-- 1. Charcoal Beam Structure (Foundation & Left Diagonal) -->
    <path d="M 384 60 
             L 417 117 
             L 263 384 
             L 455 384 
             L 491 446 
             L 225 446 
             A 35 35 0 0 1 190 396 
             Z" 
          fill="url(#charcoalGrad)" />

    <!-- 2. Violet Interlocking Chevron Structure (Superstructure & Right Truss) -->
    <path d="M 444 172 
             L 602 446 
             L 526 446 
             L 444 304 
             L 362 446 
             L 286 446 
             Z" 
          fill="url(#violetGrad)" />
  </g>

  <!-- 3. Authentic Brand Typography (Ge'ez and Latin) -->
  <g id="brand-typography">
    {''.join(text_svg)}
  </g>

  <!-- 4. Descriptor Subtitle -->
  <text x="395" y="618" 
        font-family="'Archivo', 'Segoe UI', system-ui, sans-serif" 
        font-size="16" 
        font-weight="700" 
        letter-spacing="5" 
        text-anchor="middle" 
        fill="{sub_color}">CONSULTING ENGINEERS PLC</text>

  <text x="395" y="642" 
        font-family="'JetBrains Mono', 'Segoe UI Mono', monospace" 
        font-size="11" 
        font-weight="600" 
        letter-spacing="2.5" 
        text-anchor="middle" 
        fill="{violet if theme != 'white' else '#A78BFA'}">CATEGORY-1 HIGHWAY &amp; BRIDGE CONSULTANTS</text>
</svg>'''
    return svg_content

# Generate SVG files
os.makedirs('assets', exist_ok=True)

with open('assets/logo.svg', 'w', encoding='utf-8') as f:
    f.write(generate_svg("standard"))
print("Saved assets/logo.svg")

with open('assets/logo-white.svg', 'w', encoding='utf-8') as f:
    f.write(generate_svg("white"))
print("Saved assets/logo-white.svg")

# Generate Standalone Mark SVG
mark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="markCharcoal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_CHARCOAL_LIGHT}" />
      <stop offset="100%" stop-color="{COLOR_CHARCOAL_DARK}" />
    </linearGradient>
    <linearGradient id="markViolet" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_VIOLET_LIGHT}" />
      <stop offset="100%" stop-color="{COLOR_VIOLET}" />
    </linearGradient>
  </defs>
  <g transform="translate(-140, -10) scale(0.95)">
    <path d="M 384 60 L 417 117 L 263 384 L 455 384 L 491 446 L 225 446 A 35 35 0 0 1 190 396 Z" fill="url(#markCharcoal)" />
    <path d="M 444 172 L 602 446 L 526 446 L 444 304 L 362 446 L 286 446 Z" fill="url(#markViolet)" />
  </g>
</svg>'''
with open('assets/logo-mark.svg', 'w', encoding='utf-8') as f:
    f.write(mark_svg)
print("Saved assets/logo-mark.svg")

# Generate Horizontal Lockup SVG for Navbars
h_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 140" width="100%" height="100%">
  <defs>
    <linearGradient id="hCharcoal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_CHARCOAL_LIGHT}" />
      <stop offset="100%" stop-color="{COLOR_CHARCOAL_DARK}" />
    </linearGradient>
    <linearGradient id="hViolet" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_VIOLET_LIGHT}" />
      <stop offset="100%" stop-color="{COLOR_VIOLET}" />
    </linearGradient>
  </defs>
  <!-- Emblem on left -->
  <g transform="translate(-10, -2) scale(0.26)">
    <path d="M 384 60 L 417 117 L 263 384 L 455 384 L 491 446 L 225 446 A 35 35 0 0 1 190 396 Z" fill="url(#hCharcoal)" />
    <path d="M 444 172 L 602 446 L 526 446 L 444 304 L 362 446 L 286 446 Z" fill="url(#hViolet)" />
  </g>
  <!-- Brand text -->
  <g transform="translate(160, 48)">
    <text font-family="'Archivo', 'Segoe UI', system-ui, sans-serif" font-weight="900" font-size="28" fill="{COLOR_CHARCOAL}" letter-spacing="1">አክሱላል <tspan fill="{COLOR_VIOLET}">:</tspan> AXULAL</text>
    <text y="28" font-family="'Archivo', 'Segoe UI', system-ui, sans-serif" font-weight="700" font-size="13" fill="#475569" letter-spacing="2">CONSULTING ENGINEERS PLC</text>
    <text y="50" font-family="'JetBrains Mono', monospace" font-weight="600" font-size="10" fill="{COLOR_VIOLET}" letter-spacing="1">CATEGORY-1 HIGHWAY &amp; BRIDGE CONSULTANTS</text>
  </g>
</svg>'''
with open('assets/logo-horizontal.svg', 'w', encoding='utf-8') as f:
    f.write(h_svg)
print("Saved assets/logo-horizontal.svg")

# Also generate high-resolution PNG using PIL
def generate_high_res_png():
    # Render at 1600 x 1320
    W, H = 1600, 1320
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Scale from 800x660 to 1600x1320 (2x)
    s = 2.0
    
    # Charcoal polygon:
    # M 384 60 L 417 117 L 263 384 L 455 384 L 491 446 L 225 446 A 35 35 0 0 1 190 396 Z
    pts_charcoal = [
        (384*s, 60*s),
        (417*s, 117*s),
        (263*s, 384*s),
        (455*s, 384*s),
        (491*s, 446*s),
        (225*s, 446*s),
        (190*s, 396*s)
    ]
    draw.polygon(pts_charcoal, fill=(50, 45, 41, 255))
    
    # Violet polygon:
    # M 444 172 L 602 446 L 526 446 L 444 304 L 362 446 L 286 446 Z
    # Outer triangle:
    draw.polygon([(444*s, 172*s), (602*s, 446*s), (286*s, 446*s)], fill=(75, 40, 123, 255))
    # Cut out inner triangle:
    draw.polygon([(444*s, 304*s), (526*s, 446*s), (362*s, 446*s)], fill=(0, 0, 0, 0))
    
    # Text rendering with PIL using the authentic ETH_B_GOFA.ttf font
    font_main = ImageFont.truetype('C:/Windows/Fonts/ETH_B_GOFA.ttf', int(48 * s))
    text = "አክሱላል:AXULAL"
    bbox = font_main.getbbox(text)
    tw = bbox[2] - bbox[0]
    tx = (W - tw) / 2
    ty = int(505 * s)
    draw.text((tx, ty), text, font=font_main, fill=(50, 45, 41, 255))
    
    # Subtitle
    font_sub = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', int(17 * s))
    sub1 = "CONSULTING ENGINEERS PLC"
    bbox1 = font_sub.getbbox(sub1)
    draw.text(((W - (bbox1[2]-bbox1[0]))/2, int(600 * s)), sub1, font=font_sub, fill=(100, 116, 139, 255))
    
    img.save('assets/logo.png', 'PNG')
    print("Saved assets/logo.png (1600x1320 high resolution)")

generate_high_res_png()
