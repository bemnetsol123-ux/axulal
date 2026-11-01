import json
import os
from html import escape as html_escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Bump to force browsers to re-fetch CSS/JS after a change.
ASSET_VERSION = "9"

# Quality for the WebP siblings generated next to each source photo.
WEBP_QUALITY = 82

# ---------------------------------------------------------------------------
# PROJECT & GALLERY DATA
# ---------------------------------------------------------------------------
# Financial figures are intentionally excluded from all public data.

PROJECTS_DATA = [
    {
        "id": "P-01",
        "name": "Ginchi-Danisa Gravel Road Project",
        "type": "road",
        "hub": "ginchi",
        "length": 15.5,
        "metric": "15.5 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_1_ginchi_danisa.jpg",
        "chainage": "STA 0+000 - STA 15+500",
        "structures": "14 Slab Culverts, 2 Box Culverts, 1,200m Stone Retaining Walls",
        "desc": "15.5 km of classified rural highway traversing mountainous terrain, featuring mortared stone masonry retaining walls and hydraulic box culverts engineered for heavy agricultural transport."
    },
    {
        "id": "P-02",
        "name": "Asgori-Kotoba Gravel Road Project (Lot 1 & 2)",
        "type": "road",
        "hub": "asgori",
        "length": 22.5,
        "metric": "22.5 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_2_asgori_kotoba.jpg",
        "chainage": "STA 0+000 - STA 22+500 (Dual Lot)",
        "structures": "18 Pipe Culverts, 4 Multi-barrel Box Culverts, Heavy Hillside Benching",
        "desc": "Dual-lot classified road connecting agrarian market centers, with heavy cut-and-fill benching and longitudinal drainage channels mitigating highland erosion."
    },
    {
        "id": "P-03",
        "name": "Awash-Horota-Tululuba Gravel Road Project",
        "type": "road",
        "hub": "awash",
        "length": 11.0,
        "metric": "11.0 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_3_awash_horota.jpg",
        "chainage": "STA 0+000 - STA 11+000",
        "structures": "8 Cross Drainage Culverts, Subgrade Lime Stabilization",
        "desc": "Critical transport connector with comprehensive soil stabilization across expansive clay deposits, camber shaping, and selected gravel capping."
    },
    {
        "id": "P-04",
        "name": "Gallesa-Kebabereda-Keteketa Gravel Road",
        "type": "road",
        "hub": "gallesa",
        "length": 10.3,
        "metric": "10.3 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "40 km/h Mountainous Standard",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_4_gallesa.jpg",
        "chainage": "STA 0+000 - STA 10+300",
        "structures": "11 Masonry Culverts, Erosion Runoff Berms, Mountain Side Ditches",
        "desc": "Highland gravel alignment designed with erosion-control runoff berms and hand-dressed masonry cross-drainage structures."
    },
    {
        "id": "P-05",
        "name": "Olenkomy-Awash Gravel Road Project",
        "type": "road",
        "hub": "olenkomy",
        "length": 6.5,
        "metric": "6.5 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_5_olenkomy_awash.jpg",
        "chainage": "STA 0+000 - STA 6+500",
        "structures": "6 Concrete Culverts, Reinforced Scour Protection Aprons",
        "desc": "Heavy agricultural corridor engineered for heavy axle loads, deep sub-base compaction, and durable gravel surface course."
    },
    {
        "id": "P-06",
        "name": "Awash River Girder Bridge Project",
        "type": "bridge",
        "hub": "awash",
        "length": 24.0,
        "metric": "24.0 m Span",
        "standard": "Reinforced Concrete Girder Bridge",
        "speed": "AASHTO HS20-44 Loading",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_6_awash_bridge.jpg",
        "chainage": "Bridge Station STA 4+250 (Awash River Crossing)",
        "structures": "24m RC Girder Superstructure, Deep Abutment Footings, Scour Countermeasures",
        "desc": "24-meter single-span reinforced concrete girder bridge over the Awash River with deep abutment footings and hydraulic scouring countermeasures."
    },
    {
        "id": "P-07",
        "name": "Ejere-Arertu Gravel Road Project",
        "type": "road",
        "hub": "ejere",
        "length": 27.0,
        "metric": "27.0 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_7_ejere_arertu.jpg",
        "chainage": "STA 0+000 - STA 27+000 (Major Corridor)",
        "structures": "26 Hydraulic Structures, Deep Rock Cuts, Community Access Ramps",
        "desc": "Our longest single alignment: 27.0 km of all-weather road with multi-catchment drainage culverts, rock cuts, and community access ramps."
    },
    {
        "id": "P-08",
        "name": "Ejere-Kussaye-Goli Gravel Road Project",
        "type": "road",
        "hub": "ejere",
        "length": 9.0,
        "metric": "9.0 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_8_ejere_kussaye.jpg",
        "chainage": "STA 0+000 - STA 9+000",
        "structures": "9 Stone Masonry Box Culverts, Stone-Lined Trapezoidal Ditches",
        "desc": "Rural link road engineered with subgrade stabilization across expansive clay soils, stone-lined ditches, and compaction QC."
    },
    {
        "id": "P-09",
        "name": "Ejere-Hidi-Ibu Gravel Road Project",
        "type": "road",
        "hub": "ejere",
        "length": 14.0,
        "metric": "14.0 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_9_ejere_hidi_ibu.jpg",
        "chainage": "STA 0+000 - STA 14+000",
        "structures": "15 Box & Pipe Culverts, Embankment Slope Protection",
        "desc": "14 km roadway connecting regional farming centers, featuring multiple concrete box culverts and roadside retaining aprons."
    },
    {
        "id": "P-10",
        "name": "Ejere-Endode Gravel Road Project",
        "type": "road",
        "hub": "ejere",
        "length": 6.5,
        "metric": "6.5 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_10_ejere_endode.jpg",
        "chainage": "STA 0+000 - STA 6+500",
        "structures": "7 Drainage Units, Community Water Ingress Mitigation",
        "desc": "Feeder corridor designed to DC-2 standards with optimized cut-and-fill earthworks and community water crossing facilities."
    },
    {
        "id": "P-11",
        "name": "Berga River Girder Bridge Project",
        "type": "bridge",
        "hub": "berga",
        "length": 22.0,
        "metric": "22.0 m Span",
        "standard": "Reinforced Concrete Girder Bridge",
        "speed": "AASHTO HS20-44 Loading",
        "scope": "Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_11_berga_bridge.jpg",
        "chainage": "Bridge Station STA 1+800 (Berga River Crossing)",
        "structures": "22m Precast/Cast RC Deck Girder, Abutment Wingwalls, Riprap Protection",
        "desc": "22-meter reinforced concrete girder bridge over Berga River; site quality supervision, rebar cage testing, and concrete cube compressive validation."
    },
    {
        "id": "P-12",
        "name": "Werkakore-Bujiroo Gravel Road Project",
        "type": "road",
        "hub": "werkakore",
        "length": 6.0,
        "metric": "6.0 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "40 km/h Mountainous Standard",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_12_werkakore_bujiroo.jpg",
        "chainage": "STA 0+000 - STA 6+000",
        "structures": "Mechanical Rock Ripping, Stone Gabion Mattresses, Camber QC",
        "desc": "Challenging rocky terrain alignment requiring mechanical rock excavation, stone gabion protection, and final camber grading."
    }
]

# Gallery Plates Data
GALLERY_DATA = [
    {"plate": "PLATE 01", "title": "Sub-Base Compaction", "img": "assets/gallery/plate_01_compaction.jpg", "category": "compaction", "desc": "Heavy 15-ton vibratory road roller achieving 98% Modified AASHTO compaction density on selected granular sub-base along Ginchi-Danisa."},
    {"plate": "PLATE 02", "title": "Bridge Pier & Abutment", "img": "assets/gallery/plate_02_bridge_pier.jpg", "category": "structures", "desc": "Reinforced concrete pier column, abutment formwork, and heavy falsework bracing for Awash River Girder Bridge."},
    {"plate": "PLATE 03", "title": "Hydraulic Drainage Culvert", "img": "assets/gallery/plate_03_drainage_culvert.jpg", "category": "drainage", "desc": "Hand-dressed mortared stone masonry headwalls and barrel construction providing high-capacity flood runoff cross-drainage."},
    {"plate": "PLATE 04", "title": "Hillside Benching & Earthwork", "img": "assets/gallery/plate_04_hillside_cut.jpg", "category": "earthworks", "desc": "Heavy crawler excavator cutting 1:1 roadway benches through steep volcanic rock slopes on Asgori-Kotoba."},
    {"plate": "PLATE 05", "title": "Finished DC-2 Carriageway", "img": "assets/gallery/plate_05_road_alignment.jpg", "category": "surfacing", "desc": "Completed all-weather DC-2 gravel carriageway with 4% cross-fall camber smoothly winding through rural Oromia."},
    {"plate": "PLATE 06", "title": "Substructure Deep Foundation", "img": "assets/gallery/plate_06_foundation_works.jpg", "category": "structures", "desc": "Deep spread footing excavation, dewatering sump pumps, and lean concrete blinding layer for stream crossing substructure."},
    {"plate": "PLATE 07", "title": "Embankment Retaining Structure", "img": "assets/gallery/plate_07_retaining_wall.jpg", "category": "structures", "desc": "Cast-in-situ reinforced concrete retaining wall stabilizing vulnerable embankment toe against heavy seasonal river surges."},
    {"plate": "PLATE 08", "title": "Reinforced Concrete Box Culvert", "img": "assets/gallery/plate_08_box_culvert.jpg", "category": "drainage", "desc": "Pre-pour formwork, rebar spacing validation, and cover block inspection on a 2x2m reinforced concrete box culvert."},
    {"plate": "PLATE 09", "title": "Berga Bridge Superstructure", "img": "assets/gallery/plate_09_berga_bridge_deck.jpg", "category": "structures", "desc": "Reinforced concrete deck girder rebar cage placement and transverse diaphragm inspection at Berga River Bridge."},
    {"plate": "PLATE 10", "title": "Mechanical Rock Cut & Grading", "img": "assets/gallery/plate_10_rock_blasting_cut.jpg", "category": "earthworks", "desc": "Mechanical ripping, heavy rock benching, and motor grader rough-grading on steep Werkakore-Bujiroo corridor."},
    {"plate": "PLATE 11", "title": "Gabion Mattress Slope Defense", "img": "assets/gallery/plate_11_gabion_protection.jpg", "category": "drainage", "desc": "Triple-twist galvanized wire-mesh stone gabion mattresses and Reno mattresses installed to prevent riverbank scour."},
    {"plate": "PLATE 12", "title": "Final Camber Shaping & Handover", "img": "assets/gallery/plate_12_final_surface.jpg", "category": "surfacing", "desc": "Precision motor grader fine-trimming crown camber and surface smoothness ahead of official joint handover to ORA."}
]

IMG_DIMS = {
    "assets/projects/proj_10_ejere_endode.jpg": (585, 330),
    "assets/projects/proj_11_berga_bridge.jpg": (589, 784),
    "assets/projects/proj_12_werkakore_bujiroo.jpg": (687, 515),
    "assets/projects/proj_1_ginchi_danisa.jpg": (557, 584),
    "assets/projects/proj_2_asgori_kotoba.jpg": (662, 372),
    "assets/projects/proj_3_awash_horota.jpg": (571, 428),
    "assets/projects/proj_4_gallesa.jpg": (496, 882),
    "assets/projects/proj_5_olenkomy_awash.jpg": (721, 406),
    "assets/projects/proj_6_awash_bridge.jpg": (651, 488),
    "assets/projects/proj_7_ejere_arertu.jpg": (422, 750),
    "assets/projects/proj_8_ejere_kussaye.jpg": (455, 809),
    "assets/projects/proj_9_ejere_hidi_ibu.jpg": (810, 456),
    "assets/gallery/plate_01_compaction.jpg": (729, 547),
    "assets/gallery/plate_02_bridge_pier.jpg": (798, 449),
    "assets/gallery/plate_03_drainage_culvert.jpg": (607, 455),
    "assets/gallery/plate_04_hillside_cut.jpg": (663, 373),
    "assets/gallery/plate_05_road_alignment.jpg": (592, 444),
    "assets/gallery/plate_06_foundation_works.jpg": (701, 395),
    "assets/gallery/plate_07_retaining_wall.jpg": (452, 804),
    "assets/gallery/plate_08_box_culvert.jpg": (823, 463),
    "assets/gallery/plate_09_berga_bridge_deck.jpg": (590, 788),
    "assets/gallery/plate_10_rock_blasting_cut.jpg": (704, 528),
    "assets/gallery/plate_11_gabion_protection.jpg": (740, 555),
    "assets/gallery/plate_12_final_surface.jpg": (607, 455),
}

# ---------------------------------------------------------------------------
# PURE-STRING SECTIONS
# ---------------------------------------------------------------------------
# The three blocks below are plain strings: no f-string escaping is required.
# CSS and JS are emitted as cacheable external files; only HTML is inlined.

CSS = r"""
    /* CSS Reset & Adaptive Design Tokens */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    /* Authoritative: `hidden` must beat component display rules (cards, grids). */
    [hidden] {
      display: none !important;
    }

    /* <picture> is a source-selection wrapper only: keep it out of layout. */
    picture {
      display: contents;
    }

    :root {
      /* Authentic Brand Identity */
      --brand-carbon: #181513;
      --brand-charcoal: #2b2622;
      --brand-charcoal-light: #3d3632;
      --brand-violet: #4a2882;
      --brand-violet-hover: #3d1f6d;
      --brand-violet-light: #6d39be;
      --brand-violet-subtle: #f5f0fa;
      --brand-violet-glow: rgba(74, 40, 130, 0.16);

      /* Engineering Functional Accents */
      --accent-amber: #d97706;
      --accent-amber-light: #fbbf24;
      --accent-amber-subtle: #fef3c7;
      --accent-blue: #1d4ed8;
      --accent-blue-subtle: #eff6ff;
      --accent-emerald: #059669;

      /* Surfaces, Inks & Borders */
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --bg-card-subtle: #f1f5f9;
      --bg-card-hover: #ffffff;
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-subtle: #64748b;
      --border-line: #e2e8f0;
      --border-focus: #4a2882;

      /* Elevation Shadows */
      --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.06), 0 1px 2px rgba(15, 23, 42, 0.04);
      --shadow-md: 0 4px 10px -1px rgba(15, 23, 42, 0.08), 0 2px 4px -2px rgba(15, 23, 42, 0.04);
      --shadow-lg: 0 14px 24px -4px rgba(15, 23, 42, 0.09), 0 6px 10px -4px rgba(15, 23, 42, 0.05);
      --shadow-xl: 0 24px 38px -6px rgba(15, 23, 42, 0.12), 0 10px 15px -5px rgba(15, 23, 42, 0.06);

      /* Layout Geometry */
      --radius-xs: 4px;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-xl: 24px;
      --max-w: 1280px;
      --header-h: 74px;
    }

    [data-theme="dark"] {
      --brand-carbon: #0a0c10;
      --brand-charcoal: #12151c;
      --brand-charcoal-light: #1c212b;
      --brand-violet: #7c4dff;
      --brand-violet-hover: #9068ff;
      --brand-violet-light: #a788ff;
      --brand-violet-subtle: rgba(124, 77, 255, 0.12);
      --brand-violet-glow: rgba(124, 77, 255, 0.25);

      --bg-page: #0b0f17;
      --bg-card: #131823;
      --bg-card-subtle: #19202e;
      --bg-card-hover: #1f2737;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-subtle: #64748b;
      --border-line: #222c3d;
      --border-focus: #7c4dff;

      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.4);
      --shadow-md: 0 4px 10px -1px rgba(0, 0, 0, 0.5);
      --shadow-lg: 0 14px 24px -4px rgba(0, 0, 0, 0.6);
      --shadow-xl: 0 24px 38px -6px rgba(0, 0, 0, 0.7);
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
      -webkit-text-size-adjust: 100%;
      overflow-x: hidden;
      overflow-x: clip;
      max-width: 100%;
      width: 100%;
    }

    body {
      font-family: 'Source Sans 3', system-ui, -apple-system, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      overflow-x: hidden;
      overflow-x: clip;
      max-width: 100%;
      width: 100%;
      position: relative;
      transition: background-color 0.25s ease, color 0.25s ease;
    }

    /* Prevent horizontal page drift across all device viewports */
    header, main, section, footer, .container, .hero-section {
      max-width: 100%;
      box-sizing: border-box;
    }

    /* Architectural Background Grids */
    .blueprint-bg {
      background-image: 
        radial-gradient(circle at 100% 0%, var(--brand-violet-subtle) 0%, transparent 40%),
        radial-gradient(circle at 0% 100%, rgba(217, 119, 6, 0.04) 0%, transparent 35%),
        linear-gradient(var(--border-line) 1px, transparent 1px),
        linear-gradient(90deg, var(--border-line) 1px, transparent 1px);
      background-size: 100% 100%, 100% 100%, 48px 48px, 48px 48px;
      background-position: 0 0, 0 0, -1px -1px, -1px -1px;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
      font-family: 'Archivo', sans-serif;
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: -0.02em;
      line-height: 1.15;
    }

    .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    img {
      max-width: 100%;
      height: auto;
      display: block;
    }

    /* Prevent iOS auto-zoom on inputs */
    button, input, textarea, select {
      font-family: inherit;
      font-size: 1rem;
    }

    .container {
      width: 100%;
      max-width: var(--max-w);
      margin-left: auto;
      margin-right: auto;
      padding-left: 1.5rem;
      padding-right: 1.5rem;
    }

    @media (max-width: 640px) {
      .container {
        padding-left: 1rem;
        padding-right: 1rem;
      }
    }

    /* Top Credentials Status Bar */
    .top-bar {
      background-color: var(--brand-carbon);
      color: #cbd5e1;
      font-size: 0.8125rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
      z-index: 101;
    }

    .top-bar .container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 0.45rem;
      padding-bottom: 0.45rem;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .top-badge-group {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      flex-wrap: wrap;
    }

    .cert-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: rgba(217, 119, 6, 0.2);
      color: #fbbf24;
      padding: 0.15rem 0.55rem;
      border-radius: var(--radius-xs);
      font-weight: 700;
      font-size: 0.75rem;
      border: 1px solid rgba(251, 191, 36, 0.3);
      letter-spacing: 0.5px;
      white-space: nowrap;
    }

    .top-contact-links {
      display: flex;
      align-items: center;
      gap: 1.15rem;
      font-size: 0.8125rem;
      flex-wrap: wrap;
    }

    .top-contact-links a:hover {
      color: #ffffff;
      text-decoration: underline;
    }

    /* Main Navigation Header (Persistent Sticky on Mobile & Desktop) */
    header#site-header {
      position: sticky;
      top: 0;
      z-index: 998;
      background: rgba(248, 250, 252, 0.96);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-line);
      height: var(--header-h);
      transition: background 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }

    header#site-header.header-scrolled {
      background: rgba(248, 250, 252, 0.98);
      box-shadow: 0 4px 20px rgba(15, 23, 42, 0.08);
    }

    [data-theme="dark"] header#site-header {
      background: rgba(11, 15, 23, 0.96);
    }

    [data-theme="dark"] header#site-header.header-scrolled {
      background: rgba(11, 15, 23, 0.98);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }

    /* Floating Return-to-Top Action Button */
    .floating-back-to-top {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: var(--brand-violet);
      color: #ffffff;
      border: 2px solid rgba(255, 255, 255, 0.25);
      box-shadow: 0 4px 18px rgba(74, 40, 130, 0.45), 0 2px 6px rgba(0, 0, 0, 0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 990;
      opacity: 0;
      visibility: hidden;
      transform: translateY(20px) scale(0.9);
      transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1), transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), background 0.2s ease, visibility 0.3s;
      touch-action: manipulation;
    }

    .floating-back-to-top.visible {
      opacity: 1;
      visibility: visible;
      transform: translateY(0) scale(1);
    }

    .floating-back-to-top:hover {
      background: var(--brand-violet-hover);
      transform: translateY(-3px) scale(1.05);
      box-shadow: 0 8px 26px rgba(74, 40, 130, 0.6);
    }

    .floating-back-to-top:active {
      transform: translateY(0) scale(0.95);
    }

    @media (max-width: 768px) {
      .floating-back-to-top {
        bottom: 1.25rem;
        right: 1.25rem;
        width: 44px;
        height: 44px;
      }
    }

    header#site-header .container {
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .brand-logo-wrap {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      flex-shrink: 0;
    }

    .brand-logo-img {
      height: 52px;
      width: auto;
      object-fit: contain;
      border-radius: var(--radius-xs);
      transition: height 0.2s ease;
    }

    [data-theme="dark"] .brand-logo-img {
      background: #ffffff;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
    }

    .nav-menu {
      display: flex;
      align-items: center;
      gap: 0.35rem;
      list-style: none;
    }

    .nav-link {
      font-size: 0.9375rem;
      font-weight: 600;
      color: var(--text-muted);
      padding: 0.5rem 0.75rem;
      border-radius: var(--radius-sm);
      transition: all 0.2s ease;
      white-space: nowrap;
    }

    .nav-link:hover, .nav-link.active {
      color: var(--brand-violet);
      background-color: var(--brand-violet-subtle);
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      font-family: 'Archivo', sans-serif;
      font-weight: 700;
      font-size: 0.9375rem;
      padding: 0.65rem 1.25rem;
      min-height: 44px;
      border-radius: var(--radius-sm);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      text-decoration: none;
      white-space: nowrap;
      touch-action: manipulation;
    }

    .btn-primary {
      background-color: var(--brand-violet);
      color: #ffffff;
      box-shadow: 0 4px 14px var(--brand-violet-glow);
    }

    .btn-primary:hover {
      background-color: var(--brand-violet-hover);
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(74, 40, 130, 0.28);
    }

    .btn-secondary {
      background-color: var(--bg-card);
      color: var(--text-main);
      border-color: var(--border-line);
      box-shadow: var(--shadow-sm);
    }

    .btn-secondary:hover {
      background-color: var(--bg-card-subtle);
      border-color: var(--brand-violet);
      color: var(--brand-violet);
    }

    .theme-toggle-btn {
      background: transparent;
      border: 1px solid var(--border-line);
      color: var(--text-muted);
      width: 44px;
      height: 44px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
      flex-shrink: 0;
      touch-action: manipulation;
    }

    .theme-toggle-btn:hover {
      background-color: var(--bg-card-subtle);
      color: var(--text-main);
    }

    .mobile-menu-btn {
      display: none;
      background: transparent;
      border: 1px solid var(--border-line);
      color: var(--text-main);
      width: 44px;
      height: 44px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 1.35rem;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      touch-action: manipulation;
    }

    /* Hero Section */
    .hero-section {
      position: relative;
      padding-top: 4rem;
      padding-bottom: 5rem;
      overflow: hidden;
      border-bottom: 1px solid var(--border-line);
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 3.5rem;
      align-items: center;
    }

    .hero-pretitle {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--brand-violet-subtle);
      color: var(--brand-violet);
      font-weight: 700;
      font-size: 0.8125rem;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      border: 1px solid rgba(74, 40, 130, 0.2);
      margin-bottom: 1.25rem;
      text-transform: uppercase;
      letter-spacing: 0.75px;
      max-width: 100%;
      flex-wrap: wrap;
      line-height: 1.4;
    }

    .hero-title {
      font-size: clamp(2.1rem, 4.2vw, 3.65rem);
      font-weight: 900;
      line-height: 1.1;
      margin-bottom: 1.25rem;
      color: var(--text-main);
    }

    .hero-title span.violet {
      color: var(--brand-violet);
      position: relative;
    }

    .hero-subtitle {
      font-size: 1.125rem;
      color: var(--text-muted);
      line-height: 1.65;
      margin-bottom: 2rem;
      max-width: 620px;
    }

    .hero-cta-group {
      display: flex;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
      margin-bottom: 2.5rem;
    }

    .hero-stats-band {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
      padding-top: 1.75rem;
      border-top: 1px solid var(--border-line);
    }

    .hero-stat-item {
      display: flex;
      flex-direction: column;
    }

    .stat-val {
      font-family: 'Archivo', sans-serif;
      font-size: 1.85rem;
      font-weight: 900;
      color: var(--text-main);
      line-height: 1.1;
      display: flex;
      align-items: baseline;
      gap: 2px;
    }

    .stat-val .unit {
      font-size: 1.1rem;
      color: var(--brand-violet);
    }

    .stat-lbl {
      font-size: 0.8125rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-top: 0.25rem;
    }

    /* Hero Featured Infrastructure Carousel */
    .hero-carousel-card {
      position: relative;
      border-radius: var(--radius-xl);
      background: #0f172a;
      border: 1px solid var(--border-line);
      box-shadow: var(--shadow-xl);
      overflow: hidden;
      height: 400px;
      user-select: none;
      touch-action: pan-y;
    }

    .hero-slides-wrap {
      position: relative;
      width: 100%;
      height: 100%;
    }

    .hero-slide {
      position: absolute;
      inset: 0;
      display: block;
      width: 100%;
      height: 100%;
      padding: 0;
      border: 0;
      background: none;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.85s;
      cursor: pointer;
    }

    .hero-slide:focus-visible {
      outline: 3px solid var(--accent);
      outline-offset: -3px;
    }

    .hero-slide.active {
      opacity: 1;
      visibility: visible;
      z-index: 1;
    }

    .hero-slide-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transform: scale(1);
      transition: transform 6s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .hero-slide.active .hero-slide-img {
      transform: scale(1.05);
    }

    .hero-overlay-tag {
      position: absolute;
      top: 1.25rem;
      left: 1.25rem;
      background: rgba(24, 21, 19, 0.88);
      backdrop-filter: blur(8px);
      color: #ffffff;
      padding: 0.4rem 0.85rem;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      border: 1px solid rgba(255, 255, 255, 0.18);
      z-index: 4;
    }

    .hero-nav-arrow {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(15, 23, 42, 0.78);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.22);
      color: #ffffff;
      font-size: 1.5rem;
      line-height: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 5;
      opacity: 0;
      transition: opacity 0.25s ease, background 0.2s ease, transform 0.2s ease;
      padding-bottom: 2px;
    }

    .hero-carousel-card:hover .hero-nav-arrow {
      opacity: 1;
    }

    .hero-nav-arrow.prev {
      left: 0.85rem;
    }

    .hero-nav-arrow.next {
      right: 0.85rem;
    }

    .hero-nav-arrow:hover {
      background: var(--brand-violet);
      border-color: var(--brand-violet);
      transform: translateY(-50%) scale(1.1);
    }

    .hero-carousel-pagination {
      position: absolute;
      bottom: 0.85rem;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: 0.45rem;
      z-index: 5;
      background: rgba(15, 23, 42, 0.7);
      backdrop-filter: blur(6px);
      padding: 0.35rem 0.65rem;
      border-radius: var(--radius-full);
      border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .carousel-pill {
      width: 8px;
      height: 6px;
      padding: 0;
      border: 0;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.45);
      cursor: pointer;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .carousel-pill:focus-visible {
      outline: 2px solid var(--accent-amber);
      outline-offset: 3px;
    }

    .carousel-pill.active {
      width: 24px;
      background: var(--accent-amber);
      box-shadow: 0 0 8px rgba(217, 119, 6, 0.7);
    }

    .hero-badge-float {
      position: absolute;
      bottom: 2.75rem;
      right: 1.25rem;
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      padding: 0.875rem 1.15rem;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-xl);
      display: flex;
      align-items: center;
      gap: 0.75rem;
      max-width: 295px;
      cursor: pointer;
      z-index: 5;
      transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    }

    .hero-badge-float:hover {
      transform: translateY(-3px);
      border-color: var(--brand-violet);
      box-shadow: 0 14px 30px rgba(0, 0, 0, 0.22);
    }

    .badge-arrow-cue {
      font-size: 0.85rem;
      color: var(--brand-violet);
      margin-left: auto;
      transition: transform 0.2s ease;
    }

    .hero-badge-float:hover .badge-arrow-cue {
      transform: translateX(3px);
    }

    .float-icon {
      width: 42px;
      height: 42px;
      border-radius: var(--radius-sm);
      background: var(--brand-violet-subtle);
      color: var(--brand-violet);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      flex-shrink: 0;
    }

    /* Section Headers */
    .section-wrap {
      padding-top: 5rem;
      padding-bottom: 5rem;
    }

    .section-wrap.alt {
      background-color: var(--bg-card-subtle);
      border-top: 1px solid var(--border-line);
      border-bottom: 1px solid var(--border-line);
    }

    .section-head {
      text-align: center;
      max-width: 760px;
      margin-left: auto;
      margin-right: auto;
      margin-bottom: 3.5rem;
    }

    .section-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8125rem;
      font-weight: 700;
      color: var(--brand-violet);
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 0.75rem;
      display: block;
    }

    .section-title {
      font-size: clamp(1.85rem, 3.2vw, 2.75rem);
      font-weight: 800;
      line-height: 1.15;
      margin-bottom: 1rem;
    }

    .section-desc {
      font-size: 1.0625rem;
      color: var(--text-muted);
      line-height: 1.6;
    }

    /* About Section & Org Chart */
    .about-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3.5rem;
      align-items: center;
    }

    .about-narrative h3 {
      font-size: 1.75rem;
      margin-bottom: 1rem;
    }

    .about-narrative p {
      color: var(--text-muted);
      font-size: 1.05rem;
      margin-bottom: 1.25rem;
      line-height: 1.7;
    }

    .about-pillars {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
      margin-top: 1.75rem;
    }

    .pillar-card {
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      box-shadow: var(--shadow-sm);
    }

    .pillar-card .pillar-title {
      font-weight: 800;
      font-size: 1rem;
      margin-bottom: 0.35rem;
      color: var(--brand-violet);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .pillar-card p {
      font-size: 0.875rem;
      color: var(--text-muted);
      margin: 0;
      line-height: 1.5;
    }

    .org-chart-box {
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      box-shadow: var(--shadow-md);
      text-align: center;
      position: relative;
    }

    .org-chart-box-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .org-chart-box-header h4 {
      font-size: 1.15rem;
      margin: 0;
      text-align: left;
      font-weight: 800;
      color: var(--text-main);
    }

    .org-chart-badge {
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--brand-violet);
      background: var(--brand-violet-subtle);
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-full);
      border: 1px solid rgba(74, 40, 130, 0.2);
      font-family: var(--font-mono);
    }

    .org-chart-wrapper {
      position: relative;
      overflow: hidden;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-line);
      background: #ffffff;
      cursor: zoom-in;
      box-shadow: inset 0 0 0 1px rgba(0,0,0,0.03);
    }

    .org-chart-thumb {
      width: 100%;
      height: auto;
      aspect-ratio: 1200 / 660;
      object-fit: contain;
      display: block;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .org-chart-wrapper:hover .org-chart-thumb {
      transform: scale(1.015);
    }

    .org-chart-overlay-badge {
      position: absolute;
      bottom: 0.85rem;
      right: 0.85rem;
      background: rgba(24, 21, 19, 0.85);
      color: #ffffff;
      backdrop-filter: blur(6px);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.35rem 0.75rem;
      border-radius: var(--radius-full);
      display: flex;
      align-items: center;
      gap: 0.4rem;
      pointer-events: none;
      transition: opacity 0.2s ease;
    }

    .org-caption {
      margin-top: 1rem;
      font-size: 0.875rem;
      font-weight: 600;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.75rem;
    }

    /* Services Grid */
    .services-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.75rem;
    }

    .service-card {
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-lg);
      padding: 2rem;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }

    .service-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: var(--brand-violet);
      opacity: 0;
      transition: opacity 0.25s ease;
    }

    .service-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-lg);
      border-color: var(--brand-violet);
    }

    .service-card:hover::before {
      opacity: 1;
    }

    .service-icon-wrap {
      width: 54px;
      height: 54px;
      border-radius: var(--radius-md);
      background: var(--brand-violet-subtle);
      color: var(--brand-violet);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 1.5rem;
      font-size: 1.6rem;
    }

    .service-title {
      font-size: 1.35rem;
      font-weight: 800;
      margin-bottom: 0.85rem;
    }

    .service-body {
      color: var(--text-muted);
      font-size: 0.95rem;
      line-height: 1.6;
      margin-bottom: 1.5rem;
      flex-grow: 1;
    }

    .service-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      border-top: 1px solid var(--border-line);
      padding-top: 1rem;
    }

    .stag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.2rem 0.5rem;
      border-radius: var(--radius-xs);
      background: var(--bg-card-subtle);
      color: var(--text-muted);
    }

    /* Projects Directory */
    .projects-toolbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 2rem;
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      padding: 0.875rem 1.25rem;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
    }

    .filter-pills {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .filter-btn {
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-muted);
      font-size: 0.875rem;
      font-weight: 700;
      padding: 0.45rem 0.95rem;
      min-height: 40px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s ease;
      touch-action: manipulation;
      white-space: nowrap;
    }

    .filter-btn:hover {
      background: var(--bg-card-subtle);
      color: var(--text-main);
    }

    .filter-btn.active {
      background: var(--brand-violet);
      color: #ffffff;
      box-shadow: 0 2px 8px var(--brand-violet-glow);
    }

    .search-input-wrap {
      position: relative;
      min-width: 260px;
    }

    .search-input {
      width: 100%;
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-sm);
      padding: 0.55rem 0.75rem 0.55rem 2.25rem;
      font-size: 0.9375rem;
      color: var(--text-main);
      outline: none;
      min-height: 42px;
      transition: border-color 0.2s ease;
    }

    .search-input:focus {
      border-color: var(--brand-violet);
      background: var(--bg-card);
    }

    .search-icon {
      position: absolute;
      left: 0.75rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-subtle);
      font-size: 0.875rem;
      pointer-events: none;
    }

    .projects-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.75rem;
    }

    .projects-empty {
      grid-column: 1 / -1;
      text-align: center;
      padding: 3rem 1.5rem;
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-lg);
      color: var(--text-muted);
    }

    .projects-empty strong {
      display: block;
      color: var(--text-main);
      font-size: 1.125rem;
      margin-bottom: 0.35rem;
    }

    .project-card {
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      flex-direction: column;
      cursor: pointer;
      touch-action: manipulation;
    }

    .project-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-lg);
      border-color: var(--brand-violet);
    }

    .project-img-wrap {
      position: relative;
      height: 220px;
      overflow: hidden;
      background: #0f172a;
    }

    .project-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }

    .project-card:hover .project-img {
      transform: scale(1.05);
    }

    .project-badge {
      position: absolute;
      top: 0.875rem;
      left: 0.875rem;
      background: rgba(24, 21, 19, 0.85);
      backdrop-filter: blur(8px);
      color: #ffffff;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-xs);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
    }

    .project-type-badge {
      position: absolute;
      top: 0.875rem;
      right: 0.875rem;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-xs);
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .type-road {
      background: rgba(74, 40, 130, 0.9);
      color: #ffffff;
    }

    .type-bridge {
      background: rgba(217, 119, 6, 0.9);
      color: #ffffff;
    }

    .project-card-body {
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    .project-name {
      font-size: 1.25rem;
      font-weight: 800;
      line-height: 1.25;
      margin-bottom: 0.75rem;
    }

    .project-meta-list {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.6rem;
      margin-bottom: 1.25rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--border-line);
    }

    .pm-item {
      display: flex;
      flex-direction: column;
    }

    .pm-label {
      font-size: 0.75rem;
      color: var(--text-subtle);
      font-weight: 600;
      text-transform: uppercase;
    }

    .pm-val {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.875rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .project-desc-short {
      font-size: 0.9rem;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 1.25rem;
      flex-grow: 1;
    }

    .project-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 0.75rem;
      border-top: 1px solid var(--border-line);
    }

    .view-spec-btn {
      font-family: 'Archivo', sans-serif;
      font-size: 0.8125rem;
      font-weight: 700;
      color: var(--brand-violet);
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
      background: none;
      border: 0;
      padding: 0.25rem 0;
      margin: 0;
      cursor: pointer;
      text-decoration: underline;
      text-decoration-color: transparent;
      text-underline-offset: 3px;
      transition: color 0.2s ease, text-decoration-color 0.2s ease;
    }

    .view-spec-btn:hover {
      color: var(--brand-violet-hover);
      text-decoration-color: currentColor;
    }

    .project-client {
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    /* Field Photographic Plates Gallery (High Contrast & Accessible) */
    .gallery-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
    }

    .gallery-card {
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      height: auto;
      cursor: pointer;
      transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
      position: relative;
    }

    .gallery-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-lg);
      border-color: var(--brand-violet);
    }

    .gallery-open {
      display: block;
      width: 100%;
      padding: 0;
      margin: 0;
      border: 0;
      background: none;
      cursor: zoom-in;
      font: inherit;
      color: inherit;
      text-align: left;
    }

    .gallery-open:focus-visible {
      outline: 3px solid var(--brand-violet);
      outline-offset: 2px;
    }

    .gallery-img-wrap {
      display: block;
      position: relative;
      height: 220px;
      width: 100%;
      flex-shrink: 0;
      overflow: hidden;
      background: #0f172a;
    }

    .gallery-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.4s ease;
    }

    .gallery-card:hover .gallery-img {
      transform: scale(1.06);
    }

    .gallery-plate-pill {
      position: absolute;
      top: 0.75rem;
      left: 0.75rem;
      background: var(--accent-amber);
      color: #ffffff;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-sm);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.45);
      z-index: 2;
    }

    .gallery-zoom-pill {
      position: absolute;
      bottom: 0.75rem;
      right: 0.75rem;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(6px);
      color: #ffffff;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-full);
      border: 1px solid rgba(255, 255, 255, 0.25);
      opacity: 0.9;
      transition: opacity 0.2s ease, background 0.2s ease;
      z-index: 2;
    }

    .gallery-card:hover .gallery-zoom-pill {
      opacity: 1;
      background: var(--brand-violet);
      border-color: var(--brand-violet);
    }

    .gallery-card-body {
      padding: 1.15rem 1.25rem;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
      background: var(--bg-card);
      border-top: 1px solid var(--border-line);
    }

    .gallery-card-title {
      font-family: var(--font-heading);
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 0.4rem;
      line-height: 1.3;
    }

    .gallery-card-desc {
      font-size: 0.8125rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin: 0;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    /* Credentials & Standards */
    .cred-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
    }

    .cred-card {
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      box-shadow: var(--shadow-sm);
      text-align: center;
    }

    .cred-icon {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: var(--brand-violet-subtle);
      color: var(--brand-violet);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      margin-bottom: 1rem;
    }

    .cred-title {
      font-size: 1.15rem;
      font-weight: 800;
      margin-bottom: 0.5rem;
    }

    .cred-desc {
      font-size: 0.875rem;
      color: var(--text-muted);
      line-height: 1.5;
    }

    /* Contact Section */
    .contact-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3.5rem;
    }

    .contact-info-card {
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-xl);
      padding: 2.5rem;
      box-shadow: var(--shadow-md);
    }

    .contact-detail-row {
      display: flex;
      gap: 1.25rem;
      margin-bottom: 1.75rem;
      align-items: flex-start;
    }

    .ci-icon {
      width: 44px;
      height: 44px;
      border-radius: var(--radius-sm);
      background: var(--brand-violet-subtle);
      color: var(--brand-violet);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      flex-shrink: 0;
    }

    .ci-text h4 {
      font-size: 1rem;
      font-weight: 800;
      margin-bottom: 0.25rem;
    }

    .ci-text p, .ci-text a {
      color: var(--text-muted);
      font-size: 0.9375rem;
      line-height: 1.5;
    }

    .rfp-form-card {
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-xl);
      padding: 2.5rem;
      box-shadow: var(--shadow-lg);
    }

    .form-row-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
    }

    .form-control {
      width: 100%;
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-sm);
      padding: 0.75rem 1rem;
      font-size: 1rem;
      color: var(--text-main);
      outline: none;
      min-height: 46px;
      transition: all 0.2s ease;
    }

    .form-control:focus {
      border-color: var(--brand-violet);
      background: var(--bg-card);
      box-shadow: 0 0 0 3px var(--brand-violet-subtle);
    }

    .form-group {
      margin-bottom: 1.15rem;
    }

    .form-label {
      display: block;
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.35rem;
    }

    .form-note {
      font-size: 0.85rem;
      line-height: 1.55;
      color: var(--text-subtle);
      margin-bottom: 1.4rem;
    }

    /* Spam trap: hidden from sighted users but never display:none, so bots still fill it. */
    .form-honeypot {
      position: absolute;
      left: -9999px;
      width: 1px;
      height: 1px;
      overflow: hidden;
    }

    .form-status {
      margin-top: 1.1rem;
      font-size: 0.92rem;
      line-height: 1.55;
      padding: 0.8rem 1rem;
      border-radius: var(--radius-sm);
      border: 1px solid transparent;
    }

    .form-status:empty {
      display: none;
    }

    .form-status.is-pending,
    .form-status.is-info {
      background: var(--brand-violet-subtle);
      border-color: rgba(74, 40, 130, 0.25);
      color: var(--brand-violet-hover);
    }

    .form-status.is-success {
      background: #ecfdf5;
      border-color: #a7f3d0;
      color: #065f46;
    }

    .form-status.is-error {
      background: #fef2f2;
      border-color: #fecaca;
      color: #991b1b;
    }

    [data-theme="dark"] .form-status.is-success {
      background: rgba(16, 185, 129, 0.14);
      border-color: rgba(16, 185, 129, 0.4);
      color: #6ee7b7;
    }

    [data-theme="dark"] .form-status.is-error {
      background: rgba(239, 68, 68, 0.14);
      border-color: rgba(239, 68, 68, 0.4);
      color: #fca5a5;
    }

    [data-theme="dark"] .form-status.is-pending,
    [data-theme="dark"] .form-status.is-info {
      color: var(--brand-violet-light);
      border-color: rgba(124, 77, 255, 0.4);
    }

    .form-fallback {
      margin-top: 0.9rem;
      font-size: 0.82rem;
      line-height: 1.5;
      color: var(--text-subtle);
      text-align: center;
    }

    .form-fallback a {
      color: var(--brand-violet);
      font-weight: 700;
      text-decoration: none;
    }

    .form-fallback a:hover,
    .form-fallback a:focus-visible {
      text-decoration: underline;
    }

    .btn:disabled,
    .btn[aria-disabled="true"] {
      opacity: 0.6;
      cursor: not-allowed;
    }

    /* Simple Modern Footer */
    footer#site-footer {
      background: #141210;
      color: #94a3b8;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 3.25rem;
      padding-bottom: 2.25rem;
    }

    .footer-simple-wrap {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 2rem;
      padding-bottom: 2.25rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }

    .footer-brand-block {
      max-width: 400px;
    }

    .footer-logo {
      height: 48px;
      width: auto;
      max-width: 240px;
      object-fit: contain;
      background: #ffffff;
      padding: 4px 8px;
      border-radius: var(--radius-sm);
      margin-bottom: 0.85rem;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
      display: inline-block;
    }

    .footer-tagline {
      font-size: 0.875rem;
      color: #94a3b8;
      line-height: 1.5;
      margin-bottom: 0.5rem;
    }

    .footer-reg-badge {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: #64748b;
      font-weight: 600;
    }

    .footer-simple-nav {
      list-style: none;
      display: flex;
      align-items: center;
      gap: 1.5rem;
      flex-wrap: wrap;
    }

    .footer-simple-nav a {
      color: #cbd5e1;
      font-size: 0.9375rem;
      font-weight: 600;
      text-decoration: none;
      transition: color 0.2s ease;
    }

    .footer-simple-nav a:hover {
      color: var(--accent-amber);
    }

    .footer-contact-pill {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 0.65rem 1.15rem;
      border-radius: var(--radius-full);
      font-family: var(--font-mono);
      font-size: 0.8125rem;
      color: #e2e8f0;
      flex-wrap: wrap;
    }

    .footer-contact-pill a {
      color: inherit;
      text-decoration: none;
      transition: color 0.2s ease;
    }

    .footer-contact-pill a:hover {
      color: var(--accent-amber);
    }

    .footer-bottom {
      padding-top: 1.75rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.8125rem;
      color: #64748b;
    }

    .back-to-top-btn {
      color: #94a3b8;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.8125rem;
      transition: color 0.2s ease;
    }

    .back-to-top-btn:hover {
      color: var(--accent-amber);
    }

    /* Modal / Lightbox Popups */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(10, 14, 23, 0.85);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.25rem;
      opacity: 0;
      transition: opacity 0.25s ease;
    }

    .modal-backdrop.open {
      display: flex;
      opacity: 1;
    }

    .modal-window {
      background: var(--bg-card);
      border: 1px solid var(--border-line);
      border-radius: var(--radius-xl);
      max-width: 840px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: var(--shadow-xl);
      position: relative;
    }

    .modal-close-btn {
      position: absolute;
      top: 1rem;
      right: 1rem;
      background: rgba(15, 23, 42, 0.85);
      color: #ffffff;
      border: none;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.35rem;
      z-index: 10;
      transition: background 0.2s ease;
      touch-action: manipulation;
    }

    .modal-close-btn:hover {
      background: #000000;
    }

    /* Lightbox specific */
    .lightbox-img-box {
      max-width: 1000px;
      width: 100%;
      text-align: center;
    }

    .lightbox-img {
      max-height: 75vh;
      width: auto;
      max-width: 100%;
      margin: 0 auto;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-xl);
    }

    .lightbox-caption {
      margin-top: 1.25rem;
      color: #ffffff;
      font-size: 1.05rem;
      font-weight: 600;
      line-height: 1.5;
      background: rgba(15, 23, 42, 0.94);
      backdrop-filter: blur(10px);
      padding: 0.85rem 1.5rem;
      border-radius: var(--radius-md);
      border: 1px solid rgba(255, 255, 255, 0.18);
      display: inline-block;
      max-width: 90%;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
      text-align: left;
    }

    /* Responsive Rules */
    @media (max-width: 1180px) {
      .hero-grid {
        gap: 2.5rem;
      }
      .services-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .projects-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .gallery-grid {
        grid-template-columns: repeat(3, 1fr);
      }
      .footer-simple-wrap {
        flex-direction: column;
        align-items: flex-start;
        gap: 1.5rem;
      }
    }

    @media (max-width: 991px) {
      .hero-grid {
        grid-template-columns: 1fr;
        gap: 2.5rem;
      }
      .hero-img-main {
        height: 320px;
      }
      .about-grid {
        grid-template-columns: 1fr;
        gap: 2.5rem;
      }
      .contact-layout {
        grid-template-columns: 1fr;
        gap: 2.5rem;
      }
      .cred-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (max-width: 768px) {
      :root {
        --header-h: 68px;
      }

      .top-bar {
        max-width: 100%;
        overflow: hidden;
      }

      .top-bar .top-contact-links {
        display: none;
      }

      .top-bar .container {
        justify-content: center;
        text-align: center;
        padding-top: 0.35rem;
        padding-bottom: 0.35rem;
      }

      .top-badge-group {
        justify-content: center;
        text-align: center;
        font-size: 0.75rem;
        max-width: 100%;
      }

      .cert-pill {
        font-size: 0.7rem;
        padding: 0.15rem 0.45rem;
        max-width: 100%;
      }

      .brand-logo-img {
        height: 44px;
      }

      .nav-menu {
        display: none;
      }

      .mobile-menu-btn {
        display: inline-flex;
      }

      .header-rfp-btn {
        display: none;
      }

      .section-wrap {
        padding-top: 3.5rem;
        padding-bottom: 3.5rem;
      }

      .section-head {
        margin-bottom: 2.5rem;
      }

      .hero-section {
        padding-top: 2.5rem;
        padding-bottom: 3.5rem;
      }

      .hero-title {
        font-size: 2.15rem;
      }

      .hero-subtitle {
        font-size: 1rem;
      }

      .hero-cta-group {
        flex-direction: column;
        align-items: stretch;
        gap: 0.75rem;
      }

      .hero-pretitle {
        font-size: 0.725rem;
        letter-spacing: 0.35px;
        padding: 0.35rem 0.65rem;
        border-radius: var(--radius-sm);
        display: inline-block;
        max-width: 100%;
        line-height: 1.4;
      }

      .hero-cta-group .btn {
        width: 100%;
        white-space: normal;
        text-align: center;
      }

      .hero-stats-band {
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
      }

      .stat-val {
        font-size: 1.55rem;
      }

      .hero-carousel-card {
        height: 280px;
      }

      .hero-overlay-tag {
        left: 0.75rem;
        top: 0.75rem;
        max-width: calc(100% - 1.5rem);
        white-space: normal;
        font-size: 0.7rem;
        padding: 0.25rem 0.65rem;
      }

      .hero-badge-float {
        left: 0.75rem;
        right: 0.75rem;
        max-width: none;
        bottom: 2.25rem;
        padding: 0.55rem 0.75rem;
      }

      .services-grid {
        grid-template-columns: 1fr;
        gap: 1.25rem;
      }

      .service-card {
        padding: 1.5rem;
      }

      .projects-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
      }

      .projects-toolbar {
        padding: 0.75rem;
        flex-direction: column;
        align-items: stretch;
        max-width: 100%;
        overflow: hidden;
      }

      .filter-pills {
        display: flex;
        width: 100%;
        max-width: 100%;
        min-width: 0;
        overflow-x: auto;
        flex-wrap: nowrap;
        padding-bottom: 0.5rem;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
      }

      .filter-pills::-webkit-scrollbar {
        display: none;
      }

      .search-input-wrap {
        width: 100%;
        min-width: 0;
      }

      .gallery-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
      }

      .gallery-card {
        height: auto;
      }

      .gallery-img-wrap {
        height: 180px;
        flex-shrink: 0;
      }

      .gallery-card-body {
        padding: 0.95rem 1rem;
      }

      .gallery-card-title {
        font-size: 0.95rem;
        margin-bottom: 0.25rem;
      }

      .gallery-card-desc {
        font-size: 0.8rem;
        -webkit-line-clamp: 3;
      }

      .lightbox-img {
        max-height: 55vh;
      }

      .lightbox-caption {
        font-size: 0.875rem;
        padding: 0.65rem 1rem;
        margin-top: 0.75rem;
        max-width: 95%;
      }

      .cred-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
      }

      .type-select-grid {
        grid-template-columns: 1fr;
      }

      .contact-info-card, .rfp-form-card {
        padding: 1.5rem;
      }

      .form-row-2 {
        grid-template-columns: 1fr;
        gap: 0;
      }

      .footer-contact-pill {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.5rem;
        border-radius: var(--radius-md);
        width: 100%;
      }

      .about-pillars {
        grid-template-columns: 1fr;
      }

      .modal-backdrop {
        padding: 0.75rem;
      }

      .modal-window {
        border-radius: var(--radius-lg);
      }
    }

    @media (max-width: 600px) {
      .gallery-grid {
        grid-template-columns: 1fr;
        gap: 1.25rem;
      }

      .gallery-card {
        height: auto;
      }

      .gallery-img-wrap {
        height: 230px;
        flex-shrink: 0;
      }

      .gallery-card-body {
        padding: 1.15rem 1.25rem;
      }

      .gallery-card-title {
        font-size: 1.05rem;
        margin-bottom: 0.35rem;
      }

      .gallery-card-desc {
        font-size: 0.825rem;
        -webkit-line-clamp: 4;
      }
    }

    @media (max-width: 400px) {
      .hero-title {
        font-size: 1.85rem;
      }
      .hero-stats-band {
        grid-template-columns: 1fr;
      }
    }

    /* ================= PRELOADER & LOADING CASCADE ================= */
    .blueprint-curtain {
      position: fixed;
      inset: 0;
      z-index: 999999;
      background: #141210;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      transition: transform 0.75s cubic-bezier(0.77, 0, 0.175, 1), opacity 0.5s ease;
      will-change: transform, opacity;
      overflow: hidden;
    }

    .blueprint-curtain.loaded {
      transform: translateY(-100%);
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      display: none !important;
    }

    .curtain-grid-overlay {
      position: absolute;
      inset: 0;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.035) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.035) 1px, transparent 1px);
      background-size: 40px 40px;
      pointer-events: none;
    }

    .curtain-content {
      position: relative;
      z-index: 2;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      padding: 2rem;
      max-width: 460px;
      width: 90%;
    }

    .curtain-logo-wrap {
      position: relative;
      width: 92px;
      height: 92px;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .curtain-logo {
      width: 90px;
      height: 90px;
      object-fit: contain;
      background: #ffffff;
      padding: 6px;
      border-radius: 14px;
      filter: drop-shadow(0 0 18px rgba(77, 46, 126, 0.7));
      animation: logoPulse 1.8s ease-in-out infinite alternate;
    }

    .curtain-pulse-ring {
      position: absolute;
      inset: -6px;
      border-radius: 50%;
      border: 1.5px dashed rgba(217, 119, 6, 0.45);
      animation: rotateCurtainRing 10s linear infinite;
    }

    @keyframes rotateCurtainRing {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    @keyframes logoPulse {
      0% { transform: scale(0.95); filter: drop-shadow(0 0 10px rgba(77, 46, 126, 0.4)); }
      100% { transform: scale(1.05); filter: drop-shadow(0 0 24px rgba(77, 46, 126, 0.85)); }
    }

    .curtain-brand-title {
      font-family: var(--font-heading);
      font-size: 1.15rem;
      font-weight: 900;
      color: #FFFFFF;
      letter-spacing: 2px;
      margin-bottom: 0.35rem;
    }

    .curtain-brand-sub {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--accent-amber);
      letter-spacing: 1.5px;
      margin-bottom: 1.75rem;
    }

    .curtain-progress-track {
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 9999px;
      overflow: hidden;
      position: relative;
      box-shadow: inset 0 1px 2px rgba(0,0,0,0.5);
    }

    .curtain-progress-bar {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #4D2E7E, #D97706, #FBBF24);
      border-radius: 9999px;
      box-shadow: 0 0 10px rgba(217, 119, 6, 0.7);
      transition: width 0.12s ease-out;
    }

    .curtain-status {
      margin-top: 0.85rem;
      width: 100%;
      display: flex;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 0.6875rem;
      font-weight: 700;
      color: #94A3B8;
    }

    /* Staggered Hero Entrance Cascade */
    .fade-cascade {
      opacity: 0;
      transform: translateY(22px);
      transition: opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1), transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform;
    }

    body.page-ready .fade-cascade {
      opacity: 1;
      transform: translateY(0);
    }

    body.page-ready .fade-delay-1 { transition-delay: 0.08s; }
    body.page-ready .fade-delay-2 { transition-delay: 0.18s; }
    body.page-ready .fade-delay-3 { transition-delay: 0.28s; }
    body.page-ready .fade-delay-4 { transition-delay: 0.38s; }
    body.page-ready .fade-delay-5 { transition-delay: 0.48s; }

    /* In-View Scroll Reveal */
    .scroll-reveal {
      opacity: 0;
      transform: translateY(28px);
      transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform;
    }

    .scroll-reveal.revealed {
      opacity: 1;
      transform: translateY(0);
    }
"""

JS = r"""
    // Embedded Data (Prices Completely Removed)

    // 1. Theme Management (Light / Dark)
    const themeToggle = document.getElementById("themeToggle");
    const themeIcon = document.getElementById("themeIcon");

    function initTheme() {
      const savedTheme = localStorage.getItem("axulal-theme") || "light";
      document.documentElement.setAttribute("data-theme", savedTheme);
      themeIcon.textContent = savedTheme === "dark" ? "☀️" : "🌙";
    }

    themeToggle.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("axulal-theme", next);
      themeIcon.textContent = next === "dark" ? "☀️" : "🌙";
    });

    initTheme();

    // 2. Mobile Menu Drawer
    const mobileMenuBtn = document.getElementById("mobileMenuBtn");
    const mobileDrawer = document.getElementById("mobileDrawer");

    function setMobileMenu(open) {
      mobileDrawer.style.display = open ? "block" : "none";
      mobileMenuBtn.setAttribute("aria-expanded", open ? "true" : "false");
      mobileMenuBtn.setAttribute("aria-label", open ? "Close mobile menu" : "Open mobile menu");
      mobileMenuBtn.textContent = open ? "✕" : "☰";
      if (open) {
        lockScroll();
      } else {
        unlockScrollIfIdle();
      }
    }

    function closeMobileMenu() {
      setMobileMenu(false);
    }

    mobileMenuBtn.setAttribute("aria-expanded", "false");
    mobileMenuBtn.addEventListener("click", () => {
      setMobileMenu(mobileDrawer.style.display !== "block");
    });

    // 3. Project Grid — markup is server-rendered; JS only filters it
    const projectsContainer = document.getElementById("projectsContainer");
    const projectSearch = document.getElementById("projectSearch");
    const projectsEmpty = document.getElementById("projectsEmpty");
    const filterButtons = Array.from(document.querySelectorAll("#projectFilterGroup .filter-btn"));
    const projectCards = Array.from(projectsContainer.querySelectorAll(".project-card"));

    let currentFilter = "all";
    let searchQuery = "";

    function applyProjectFilters() {
      const q = searchQuery.trim().toLowerCase();
      let visible = 0;

      projectCards.forEach(card => {
        let matchesFilter = true;
        if (currentFilter === "road") matchesFilter = card.dataset.type === "road";
        else if (currentFilter === "bridge") matchesFilter = card.dataset.type === "bridge";
        else if (currentFilter === "ejere") matchesFilter = card.dataset.hub === "ejere";

        const matchesSearch = !q || (card.dataset.search || "").includes(q);
        const show = matchesFilter && matchesSearch;

        card.hidden = !show;
        if (show) visible += 1;
      });

      if (projectsEmpty) projectsEmpty.hidden = visible !== 0;
      projectsContainer.dataset.visibleCount = String(visible);
    }

    // Filter Button Clicks
    filterButtons.forEach(btn => {
      btn.setAttribute("aria-pressed", btn.classList.contains("active") ? "true" : "false");
      btn.addEventListener("click", () => {
        filterButtons.forEach(b => {
          b.classList.remove("active");
          b.setAttribute("aria-pressed", "false");
        });
        btn.classList.add("active");
        btn.setAttribute("aria-pressed", "true");
        currentFilter = btn.dataset.filter || "all";
        applyProjectFilters();
      });
    });

    // Search Input
    if (projectSearch) {
      projectSearch.addEventListener("input", (e) => {
        searchQuery = e.target.value;
        applyProjectFilters();
      });
      projectSearch.addEventListener("search", (e) => {
        searchQuery = e.target.value;
        applyProjectFilters();
      });
    }

    applyProjectFilters();

    // Card activation — one delegated handler, keyboard-safe (the CTA is a real button)
    projectsContainer.addEventListener("click", (event) => {
      const card = event.target.closest(".project-card");
      if (!card || !projectsContainer.contains(card)) return;
      openProjectModal(card.id);
    });

    // 4. Field Plates — markup is server-rendered; the plate button opens the lightbox
    const galleryContainer = document.getElementById("galleryContainer");

    galleryContainer.addEventListener("click", (event) => {
      const card = event.target.closest(".gallery-card");
      if (!card || !galleryContainer.contains(card)) return;
      const data = card.dataset;
      const caption = data.plate + ": " + data.title + " — " + data.desc;
      openLightbox(data.img, caption);
    });

    // 5. Project Modal Handler (No Price Fields)
    const projectModal = document.getElementById("projectModal");
    const modalContent = document.getElementById("modalContent");
    const lightboxModal = document.getElementById("lightboxModal");
    const lightboxImg = document.getElementById("lightboxImg");
    const lightboxCaption = document.getElementById("lightboxCaption");

    let lastFocusedElement = null;

    function rememberFocus() {
      const active = document.activeElement;
      lastFocusedElement = active && active !== document.body ? active : null;
    }

    function restoreFocus() {
      if (lastFocusedElement && document.contains(lastFocusedElement)) {
        lastFocusedElement.focus({ preventScroll: true });
      }
      lastFocusedElement = null;
    }

    function lockScroll() {
      document.body.style.overflow = "hidden";
    }

    function unlockScrollIfIdle() {
      const anyModalOpen =
        projectModal.classList.contains("open") || lightboxModal.classList.contains("open");
      if (!anyModalOpen) document.body.style.overflow = "";
    }

    function focusInto(container) {
      const target =
        container.querySelector("[data-autofocus]") ||
        container.querySelector(
          "button:not([disabled]), [href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex='-1'])"
        );
      if (target) target.focus({ preventScroll: true });
    }

    // Keeps Tab / Shift+Tab cycling inside the open dialog.
    function trapFocus(container, event) {
      if (event.key !== "Tab") return;
      const focusable = container.querySelectorAll(
        "button:not([disabled]), [href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex='-1'])"
      );
      if (!focusable.length) return;
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }

    function openProjectModal(id) {
      const p = PROJECTS.find(item => item.id === id);
      if (!p) return;

      rememberFocus();
      modalContent.innerHTML = `
        <div style="position:relative; height:280px; overflow:hidden; background:#0f172a;">
          const webpImg = p.img.replace(/\.(jpg|jpeg|png)$/i, '.webp');
          <picture>
            <source type="image/webp" srcset="${webpImg}">
            <img src="${p.img}" alt="${p.name}" style="width:100%; height:100%; object-fit:cover;" loading="eager" decoding="async">
          </picture>
          <div style="position:absolute; bottom:0; left:0; right:0; background:linear-gradient(to top, rgba(15,23,42,0.95), transparent); padding:1.5rem; color:#ffffff;">
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.8125rem; color:#fbbf24; font-weight:700; margin-bottom:0.25rem;">
              ${p.id} · ${p.type === 'bridge' ? 'BRIDGE INFRASTRUCTURE' : 'HIGHWAY ALIGNMENT'}
            </div>
            <h2 id="modalTitle" style="font-size:clamp(1.35rem, 3vw, 1.85rem); color:#ffffff; line-height:1.2;">${p.name}</h2>
          </div>
        </div>

        <div style="padding:1.5rem;">
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(140px, 1fr)); gap:1rem; background:var(--bg-card-subtle); padding:1.25rem; border-radius:var(--radius-md); margin-bottom:1.5rem; border:1px solid var(--border-line);">
            <div>
              <div style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; font-weight:700;">Metric Scope</div>
              <div style="font-family:'JetBrains Mono', monospace; font-size:1.15rem; font-weight:800; color:var(--brand-violet);">${p.metric}</div>
            </div>
            <div>
              <div style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; font-weight:700;">Design Speed / Loading</div>
              <div style="font-family:'JetBrains Mono', monospace; font-size:1.05rem; font-weight:800;">${p.speed}</div>
            </div>
            <div>
              <div style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase; font-weight:700;">Client Authority</div>
              <div style="font-size:0.95rem; font-weight:800;">${p.client}</div>
            </div>
          </div>

          <h4 style="font-size:1.15rem; margin-bottom:0.65rem;">Technical Parameters &amp; Cross Section</h4>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:0.75rem; margin-bottom:1.5rem; font-size:0.925rem;">
            <div><strong>Chainage Extents:</strong> <span class="font-mono">${p.chainage}</span></div>
            <div><strong>Geometric Standard:</strong> ${p.standard}</div>
            <div><strong>Design Speed / Loading:</strong> ${p.speed}</div>
            <div><strong>Hydraulic &amp; Earthwork Assets:</strong> ${p.structures}</div>
          </div>

          <h4 style="font-size:1.15rem; margin-bottom:0.65rem;">Consulting Engineering Scope</h4>
          <p style="color:var(--text-muted); font-size:0.925rem; line-height:1.6; margin-bottom:1.5rem; background:var(--bg-card-subtle); padding:1rem; border-radius:var(--radius-sm); border-left:4px solid var(--brand-violet);">
            ${p.scope}
          </p>

          <h4 style="font-size:1.15rem; margin-bottom:0.65rem;">Field Engineering Overview</h4>
          <p style="color:var(--text-muted); font-size:0.95rem; line-height:1.6; margin-bottom:2rem;">
            ${p.desc}
          </p>

          <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--border-line); padding-top:1.25rem; flex-wrap:wrap; gap:0.75rem;">
            <button class="btn btn-secondary" type="button" data-close-modal="project">Close Overview</button>
            <a href="#contact" class="btn btn-primary" data-close-modal="project">Request Tender Dossier</a>
          </div>
        </div>
      `;

      projectModal.classList.add("open");
      projectModal.setAttribute("aria-hidden", "false");
      lockScroll();
      focusInto(projectModal);
    }

    function closeProjectModal() {
      if (!projectModal.classList.contains("open")) return;
      projectModal.classList.remove("open");
      projectModal.setAttribute("aria-hidden", "true");
      unlockScrollIfIdle();
      restoreFocus();
    }

    // 6. Lightbox Handler
    function openLightbox(src, caption) {
      rememberFocus();
      const webpSrc = src.replace(/\.(jpg|jpeg|png)$/i, '.webp');
      lightboxImg.src = webpSrc;
      lightboxImg.onerror = () => { lightboxImg.src = src; };
      lightboxImg.alt = caption || "Field photography plate";
      lightboxCaption.textContent = caption || "";
      lightboxModal.classList.add("open");
      lightboxModal.setAttribute("aria-hidden", "false");
      lockScroll();
      focusInto(lightboxModal);
    }

    function closeLightbox() {
      if (!lightboxModal.classList.contains("open")) return;
      lightboxModal.classList.remove("open");
      lightboxModal.setAttribute("aria-hidden", "true");
      unlockScrollIfIdle();
      restoreFocus();
    }

    // Backdrop dismissal: only a click on the backdrop itself closes the dialog.
    [projectModal, lightboxModal].forEach((backdrop) => {
      backdrop.addEventListener("click", (event) => {
        if (event.target !== backdrop) return;
        if (backdrop === projectModal) {
          closeProjectModal();
        } else {
          closeLightbox();
        }
      });
    });

    // Return to Top Handler & Persistent Header Elevation
    const backToTopBtn = document.getElementById("backToTopBtn");
    const siteHeader = document.getElementById("site-header");

    window.addEventListener("scroll", () => {
      const scrollY = window.scrollY || document.documentElement.scrollTop;
      
      if (backToTopBtn) {
        if (scrollY > 280) {
          backToTopBtn.classList.add("visible");
        } else {
          backToTopBtn.classList.remove("visible");
        }
      }

      if (siteHeader) {
        if (scrollY > 15) {
          siteHeader.classList.add("header-scrolled");
        } else {
          siteHeader.classList.remove("header-scrolled");
        }
      }
    }, { passive: true });

    if (backToTopBtn) {
      backToTopBtn.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
      });
    }

    // Keyboard: Escape closes the topmost layer, Tab stays inside open dialogs
    window.addEventListener("keydown", (e) => {
      const projectOpen = projectModal.classList.contains("open");
      const lightboxOpen = lightboxModal.classList.contains("open");

      if (e.key === "Escape") {
        if (projectOpen) closeProjectModal();
        else if (lightboxOpen) closeLightbox();
        else closeMobileMenu();
        return;
      }

      if (projectOpen) {
        trapFocus(projectModal, e);
      } else if (lightboxOpen) {
        trapFocus(lightboxModal, e);
      }
    });

    // Delegated close/navigation hooks (keeps the markup free of inline handlers)
    document.addEventListener("click", (event) => {
      const closer = event.target.closest("[data-close-modal]");
      if (closer) {
        if (closer.dataset.closeModal === "lightbox") {
          closeLightbox();
        } else {
          closeProjectModal();
        }
        return;
      }

      if (event.target.closest("[data-close-drawer]")) {
        closeMobileMenu();
      }
    });

    // 8. Form Submission Feedback
    // Point RFP_ENDPOINT at a form backend (Formspree, Web3Forms, Basin, or any
    // endpoint that accepts a JSON POST). While it is empty the form stays fully
    // usable: it opens a prefilled mail draft to the tender desk instead.
    const RFP_ENDPOINT = "";
    const RFP_MAILBOX = "tenders@axulalengineers.com";
    const RFP_SUBJECT = "Request for proposal \u2014 highway / bridge consultancy";

    function setFormStatus(message, state) {
      const status = document.getElementById("rfpStatus");
      if (!status) return;
      status.className = state ? "form-status is-" + state : "form-status";
      status.textContent = message || "";
    }

    function buildMailtoDraft(form) {
      const data = new FormData(form);
      const lines = [
        "Request for proposal \u2014 Axulal Consulting Engineers PLC",
        "",
        "Full name: " + (data.get("name") || ""),
        "Organization / authority: " + (data.get("org") || ""),
        "Email: " + (data.get("email") || ""),
        "Phone: " + (data.get("phone") || ""),
        "Project domain: " + (data.get("category") || ""),
        "",
        "Scope description & location:",
        (data.get("message") || ""),
        "",
        "(Sent from axulalengineers.com)",
      ];
      return (
        "mailto:" + RFP_MAILBOX +
        "?subject=" + encodeURIComponent(RFP_SUBJECT) +
        "&body=" + encodeURIComponent(lines.join("\n"))
      );
    }

    async function handleFormSubmit(e) {
      e.preventDefault();
      const form = e.target;

      // Bots fill the honeypot; humans never see it. Pretend it worked.
      const trap = form.querySelector("[name='_gotcha']");
      if (trap && trap.value) {
        setFormStatus("Thank you. Your inquiry has been received.", "success");
        form.reset();
        return;
      }

      if (!RFP_ENDPOINT) {
        const draft = buildMailtoDraft(form);
        setFormStatus(
          "Your email app is opening with the request prefilled. If nothing happens, write to " +
            RFP_MAILBOX + " directly.",
          "info"
        );
        window.location.href = draft;
        return;
      }

      const submitBtn = form.querySelector("button[type='submit']");
      const originalLabel = submitBtn ? submitBtn.textContent : "";
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = "Sending\u2026";
      }
      setFormStatus("Sending your inquiry to the tender desk\u2026", "pending");

      try {
        const payload = Object.fromEntries(new FormData(form).entries());
        delete payload["_gotcha"];
        const response = await fetch(RFP_ENDPOINT, {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify(payload),
        });
        if (!response.ok) throw new Error("HTTP " + response.status);
        setFormStatus(
          "Thank you, " + (payload.name || "colleague") +
            ". Your inquiry is with the tender desk and a senior highway/bridge director will respond within one working day.",
          "success"
        );
        form.reset();
      } catch (error) {
        setFormStatus(
          "That did not send. Please email " + RFP_MAILBOX + " or call +251 911 406830 and we will pick it up directly.",
          "error"
        );
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = originalLabel;
        }
      }
    }

    // 7. Architectural Blueprint Preloader Sequence (Fail-Safe & Fast)
    function dismissPreloader() {
      const curtain = document.getElementById("blueprintCurtain");
      if (curtain && !curtain.classList.contains("loaded")) {
        curtain.classList.add("loaded");
        setTimeout(() => { curtain.style.display = "none"; }, 400);
      }
      document.body.classList.add("page-ready");
      if (typeof animateCounters === "function") animateCounters();
      if (typeof initScrollReveals === "function") initScrollReveals();
    }

    (function initPreloader() {
      const curtain = document.getElementById("blueprintCurtain");
      const bar = document.getElementById("curtainProgressBar");
      const pct = document.getElementById("curtainPercent");
      const status = document.getElementById("curtainStatusText");
      if (!curtain) {
        dismissPreloader();
        return;
      }

      let progress = 0;
      const stages = [
        { p: 30, msg: "INITIALIZING AXULAL ROAD & BRIDGE ASSETS..." },
        { p: 70, msg: "LOADING INFRASTRUCTURE BLUEPRINTS..." },
        { p: 100, msg: "ENGINEERING DISCIPLINE CERTIFIED · 100%" }
      ];

      // Fast, slick cadence: complete in ~60ms
      const timer = setInterval(() => {
        progress += 35;
        if (progress > 100) progress = 100;

        if (bar) bar.style.width = progress + "%";
        if (pct) pct.textContent = progress + "%";

        for (let s of stages) {
          if (progress <= s.p) {
            if (status) status.textContent = s.msg;
            break;
          }
        }

        if (progress >= 100) {
          clearInterval(timer);
          setTimeout(dismissPreloader, 40);
        }
      }, 16);

      // Immediate fail-safe timeout
      setTimeout(dismissPreloader, 250);
    })();

    // Window load & DOMContentLoaded safeguards
    window.addEventListener("load", () => { dismissPreloader(); });
    document.addEventListener("DOMContentLoaded", () => { setTimeout(dismissPreloader, 50); });

    // Animated Metric Numbers
    function animateCounters() {
      const counters = document.querySelectorAll('.counter');
      counters.forEach(counter => {
        const target = parseFloat(counter.getAttribute('data-target'));
        const isDecimal = target % 1 !== 0;
        const duration = 1500;
        const startTime = performance.now();

        function updateNumber(now) {
          const elapsed = now - startTime;
          const progress = Math.min(elapsed / duration, 1);
          // Ease-out exponential curve
          const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
          const current = ease * target;
          counter.textContent = isDecimal ? current.toFixed(1) : Math.floor(current);
          if (progress < 1) {
            requestAnimationFrame(updateNumber);
          } else {
            counter.textContent = isDecimal ? target.toFixed(1) : target;
          }
        }
        requestAnimationFrame(updateNumber);
      });
    }

    // In-View Scroll Reveal Observer
    function initScrollReveals() {
      const reveals = document.querySelectorAll(".scroll-reveal");
      if (!("IntersectionObserver" in window)) {
        reveals.forEach(el => el.classList.add("revealed"));
        return;
      }
      const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add("revealed");
            obs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1 });
      reveals.forEach(el => observer.observe(el));
    }

    // 8. Featured Infrastructure Hero Carousel
    // Slide metadata lives on the static markup (data-*), so there is exactly
    // one source of truth and the carousel works before JS finishes loading.
    function readHeroSlides() {
      return Array.from(document.querySelectorAll('.hero-slide')).map(function (el) {
        return {
          el: el,
          id: el.getAttribute('data-project') || '',
          tag: el.getAttribute('data-tag') || '',
          icon: el.getAttribute('data-icon') || '',
          title: el.getAttribute('data-title') || '',
          sub: el.getAttribute('data-sub') || ''
        };
      });
    }

    const HERO_SLIDES = readHeroSlides();

    let currentHeroIndex = 0;
    let heroTimer = null;
    let heroIsPaused = false;

    function updateHeroCarousel(index) {
      if (!HERO_SLIDES.length) return;
      currentHeroIndex = (index + HERO_SLIDES.length) % HERO_SLIDES.length;
      const data = HERO_SLIDES[currentHeroIndex];

      // Update slide images
      const slides = document.querySelectorAll('.hero-slide');
      slides.forEach((s, idx) => {
        const isActive = idx === currentHeroIndex;
        s.classList.toggle('active', isActive);
        s.tabIndex = isActive ? 0 : -1;
      });

      // Update indicators
      const pills = document.querySelectorAll('.carousel-pill');
      pills.forEach((p, idx) => {
        const isActive = idx === currentHeroIndex;
        p.classList.toggle('active', isActive);
        if (isActive) {
          p.setAttribute('aria-current', 'true');
        } else {
          p.removeAttribute('aria-current');
        }
      });

      // Update tag & floating badge
      const tag = document.getElementById('heroCarouselTag');
      const icon = document.getElementById('heroBadgeIcon');
      const title = document.getElementById('heroBadgeTitle');
      const sub = document.getElementById('heroBadgeSub');

      if (tag) tag.textContent = data.tag;
      if (icon) icon.textContent = data.icon;
      if (title) title.textContent = data.title;
      if (sub) sub.textContent = data.sub;
    }

    function nextHeroSlide(e) {
      if (e) e.stopPropagation();
      updateHeroCarousel(currentHeroIndex + 1);
    }

    function prevHeroSlide(e) {
      if (e) e.stopPropagation();
      updateHeroCarousel(currentHeroIndex - 1);
    }

    function gotoHeroSlide(idx) {
      updateHeroCarousel(idx);
    }

    function pauseHeroCarousel() {
      heroIsPaused = true;
      if (heroTimer) clearInterval(heroTimer);
    }

    function resumeHeroCarousel() {
      heroIsPaused = false;
      startHeroAutoplay();
    }

    function startHeroAutoplay() {
      if (heroTimer) clearInterval(heroTimer);
      if (!HERO_SLIDES.length) return;
      if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      heroTimer = setInterval(() => {
        if (!heroIsPaused) {
          updateHeroCarousel(currentHeroIndex + 1);
        }
      }, 4800);
    }

    // Accepts "P-06", "proj-06", "6" or a slide element and returns "P-06".
    function normalizeProjectId(value) {
      const raw = String(value == null ? '' : value).trim();
      if (/^P-\d+$/.test(raw)) return raw;
      const digits = raw.match(/(\d+)/);
      if (!digits) return '';
      return 'P-' + digits[1].padStart(2, '0');
    }

    function openCurrentHeroProject(source) {
      let raw = '';
      if (source && typeof source === 'object' && source.getAttribute) {
        raw = source.getAttribute('data-project') || '';
      } else if (typeof source === 'number' && HERO_SLIDES[source]) {
        raw = HERO_SLIDES[source].id;
      } else if (typeof source === 'string') {
        raw = source;
      } else if (HERO_SLIDES[currentHeroIndex]) {
        raw = HERO_SLIDES[currentHeroIndex].id;
      }

      const id = normalizeProjectId(raw);
      if (!id) return;
      if (typeof openProjectModal === 'function') {
        openProjectModal(id);
      }
    }

    // Touch Swipe Support for Hero Carousel
    (function initHeroSwipe() {
      const card = document.getElementById('heroCarousel');
      if (!card) return;
      let startX = 0;
      let startY = 0;

      card.addEventListener('touchstart', (e) => {
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
        pauseHeroCarousel();
      }, { passive: true });

      card.addEventListener('touchend', (e) => {
        const diffX = e.changedTouches[0].clientX - startX;
        const diffY = e.changedTouches[0].clientY - startY;
        if (Math.abs(diffX) > 40 && Math.abs(diffX) > Math.abs(diffY)) {
          if (diffX < 0) nextHeroSlide();
          else prevHeroSlide();
        }
        resumeHeroCarousel();
      }, { passive: true });
    })();

    // Hero interaction: slide dossiers, pagination pills, arrows and badge (CSP friendly)
    (function initHeroDelegates() {
      const card = document.getElementById('heroCarousel');
      if (!card) return;

      card.addEventListener('mouseenter', pauseHeroCarousel);
      card.addEventListener('mouseleave', resumeHeroCarousel);

      card.addEventListener('click', (e) => {
        const arrow = e.target.closest('[data-hero]');
        if (arrow) {
          if (arrow.dataset.hero === 'next') nextHeroSlide(e);
          else prevHeroSlide(e);
          return;
        }

        const pill = e.target.closest('.carousel-pill');
        if (pill) {
          gotoHeroSlide(Number(pill.dataset.index));
          return;
        }

        const slide = e.target.closest('.hero-slide');
        if (slide) {
          openCurrentHeroProject(slide.dataset.project || slide);
          return;
        }

        if (e.target.closest('#heroCarouselBadge')) {
          openCurrentHeroProject();
        }
      });
    })();

    // 9. Wire the enquiry form without inline handlers (CSP friendly).
    (function initRfpForm() {
      const form = document.getElementById("rfpForm");
      if (!form) return;
      if (RFP_ENDPOINT) form.setAttribute("action", RFP_ENDPOINT);
      form.addEventListener("submit", handleFormSubmit);
      form.addEventListener("input", () => {
        const status = document.getElementById("rfpStatus");
        if (status && status.classList.contains("is-error")) setFormStatus("", "");
      });
    })();

    startHeroAutoplay();
"""

HTML = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Axulal Consulting Engineers PLC | Category-1 Highway &amp; Bridge Consultants, Addis Ababa</title>
  <meta name="description" content="Axulal Consulting Engineers PLC (አክሱላል) is Ethiopia's premier Category-1 Highway and Bridge consulting firm based in Addis Ababa. Delivering feasibility, detailed design, tender documentation, and construction supervision since 2011.">
  <meta name="keywords" content="Axulal Consulting Engineers PLC, Category 1 Highway Consultant, Bridge Engineers Addis Ababa, Ethiopia Road Construction, ORA road projects, civil engineering consultancy, structural engineering Ethiopia">
  <link rel="icon" type="image/png" href="assets/favicon.png?v=__V__">
  <link rel="shortcut icon" href="favicon.ico?v=__V__">
  <link rel="apple-touch-icon" href="assets/favicon.png?v=__V__">

  <!-- Google Fonts: Archivo (Geometric Structural Sans), Source Sans 3 (Clean Body), JetBrains Mono (CAD Coordinates & Specs) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800;900&family=Source+Sans+3:ital,wght@0,300;0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="assets/css/site.css?v=__V__">
</head>
<body>
  <!-- Architectural Blueprint Curtain Preloader -->
  <div id="blueprintCurtain" class="blueprint-curtain" aria-hidden="true">
    <div class="curtain-grid-overlay"></div>
    <div class="curtain-content">
      <div class="curtain-logo-wrap">
        <img src="assets/logo-mark.png?v=__V__" alt="Axulal Monogram" class="curtain-logo">
        <div class="curtain-pulse-ring"></div>
      </div>
      <div class="curtain-brand-title">AXULAL CONSULTING ENGINEERS</div>
      <div class="curtain-brand-sub">CATEGORY-1 HIGHWAY &amp; BRIDGE CONSULTANTS</div>
      <div class="curtain-progress-track">
        <div id="curtainProgressBar" class="curtain-progress-bar"></div>
      </div>
      <div class="curtain-status">
        <span id="curtainStatusText">INITIALIZING CAD &amp; GEOMETRIC ASSETS...</span>
        <span id="curtainPercent">0%</span>
      </div>
    </div>
  </div>



  <!-- Top Certification Ribbon -->
  <div class="top-bar">
    <div class="container">
      <div class="top-badge-group">
        <span class="cert-pill">✓ CATEGORY-1 HIGHWAY &amp; BRIDGE</span>
        <span>FDRE Reg #01/ORA/2011 · Addis Ababa</span>
      </div>
      <div class="top-contact-links font-mono">
        <a href="tel:+251911406830">📞 +251 911 406830</a>
        <a href="mailto:info@axulalengineers.com">✉️ info@axulalengineers.com</a>
      </div>
    </div>
  </div>

  <!-- Main Sticky Navigation -->
  <header id="site-header">
    <div class="container">
      <a href="#home" class="brand-logo-wrap" aria-label="Axulal Consulting Engineers Home">
        <!-- SVG Vector Logo -->
        <picture><source type="image/webp" srcset="assets/logo.webp?v=__V__"><img src="assets/logo.png?v=__V__" alt="Axulal Consulting Engineers PLC Logo" class="brand-logo-img" width="1014" height="313"></picture>
      </a>

      <!-- Desktop Nav -->
      <nav aria-label="Main Navigation">
        <ul class="nav-menu">
          <li><a href="#about" class="nav-link">About</a></li>
          <li><a href="#services" class="nav-link">Services</a></li>
          <li><a href="#projects" class="nav-link">Projects</a></li>
          <li><a href="#gallery" class="nav-link">Field Plates</a></li>
          <li><a href="#credentials" class="nav-link">Credentials</a></li>
          <li><a href="#contact" class="nav-link">Contact</a></li>
        </ul>
      </nav>

      <div class="nav-actions">
        <!-- Theme Toggle -->
        <button id="themeToggle" class="theme-toggle-btn" aria-label="Toggle Dark / Light Theme" title="Toggle Theme">
          <span id="themeIcon">🌙</span>
        </button>

        <a href="#contact" class="btn btn-primary header-rfp-btn">Request RFP</a>

        <button id="mobileMenuBtn" class="mobile-menu-btn" aria-label="Open mobile menu">
          ☰
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer Menu (Accessible & Touch-Optimized) -->
  <div id="mobileDrawer" style="display:none; position:fixed; top:calc(var(--header-h) + 31px); left:0; right:0; bottom:0; background:var(--bg-card); z-index:99; padding:1.75rem; overflow-y:auto; border-bottom:1px solid var(--border-line); box-shadow:var(--shadow-xl);">
    <ul style="list-style:none; display:flex; flex-direction:column; gap:1.15rem; font-size:1.15rem; font-weight:700;">
      <li><a href="#about" data-close-drawer style="display:block; padding:0.4rem 0;">About Axulal</a></li>
      <li><a href="#services" data-close-drawer style="display:block; padding:0.4rem 0;">Engineering Services</a></li>
      <li><a href="#projects" data-close-drawer style="display:block; padding:0.4rem 0;">Projects</a></li>
      <li><a href="#gallery" data-close-drawer style="display:block; padding:0.4rem 0;">Construction Plates</a></li>
      <li><a href="#credentials" data-close-drawer style="display:block; padding:0.4rem 0;">Registration &amp; QA</a></li>
      <li><a href="#contact" data-close-drawer style="display:block; padding:0.4rem 0;">Contact &amp; Tender Desk</a></li>
    </ul>
    <div style="margin-top:2rem; padding-top:1.5rem; border-top:1px solid var(--border-line);">
      <a href="#contact" class="btn btn-primary" style="width:100%; text-align:center;" data-close-drawer>Submit RFP Inquiry →</a>
    </div>
  </div>

  <main id="home">
    <!-- Hero Section -->
    <section class="hero-section blueprint-bg">
      <div class="container">
        <div class="hero-grid">
          <div>
            <div class="hero-pretitle fade-cascade fade-delay-1">
              <span>★</span> Category-1 Highway &amp; Bridge Consultants · Addis Ababa
            </div>
            <h1 class="hero-title fade-cascade fade-delay-2">
              Engineering Ethiopia’s Arteries of <span class="violet">Growth &amp; Resilience.</span>
            </h1>
            <p class="hero-subtitle fade-cascade fade-delay-3">
              Since 2011, <strong>Axulal Consulting Engineers PLC (አክሱላል)</strong> has delivered premier feasibility studies, precision geometric road design, reinforced concrete bridge engineering, tender preparation, and resident construction supervision across Ethiopia.
            </p>
            <div class="hero-cta-group fade-cascade fade-delay-4">
              <a href="#projects" class="btn btn-primary">Explore Completed Projects ↓</a>
              <a href="#contact" class="btn btn-secondary">Request Technical Proposal 📋</a>
            </div>

            <!-- Key Metric Counters -->
            <div class="hero-stats-band fade-cascade fade-delay-5">
              <div class="hero-stat-item">
                <div class="stat-val"><span class="counter" data-target="145.3">145.3</span><span class="unit">km</span></div>
                <div class="stat-lbl">Classified Roads Designed</div>
              </div>
              <div class="hero-stat-item">
                <div class="stat-val"><span class="counter" data-target="46.0">46.0</span><span class="unit">m</span></div>
                <div class="stat-lbl">RC Girder Bridges Spanned</div>
              </div>
              <div class="hero-stat-item">
                <div class="stat-val"><span class="counter" data-target="12">12</span><span class="unit">+</span></div>
                <div class="stat-lbl">Handed-Over Contracts</div>
              </div>
              <div class="hero-stat-item">
                <div class="stat-val"><span class="counter" data-target="15">15</span><span class="unit">Yrs</span></div>
                <div class="stat-lbl">Excellence Since 2011</div>
              </div>
            </div>
          </div>

          <!-- Hero Featured Infrastructure Carousel -->
          <div>
            <div class="hero-carousel-card fade-cascade fade-delay-3" id="heroCarousel">
              <!-- Slides Track (Crossfade) -->
              <div class="hero-slides-wrap" id="heroSlidesWrap">__HERO_SLIDES__</div>

              <!-- Top Infrastructure Tag -->
              <div class="hero-overlay-tag" id="heroCarouselTag">__HERO_TAG__</div>

              <!-- Floating Interactive Project Dossier Badge -->
              <button type="button" class="hero-badge-float" id="heroCarouselBadge">
                <span class="float-icon" id="heroBadgeIcon">__HERO_ICON__</span>
                <span>
                  <span id="heroBadgeTitle" style="display:block; font-weight:800; font-size:0.95rem;">__HERO_TITLE__</span>
                  <span id="heroBadgeSub" style="display:block; font-size:0.75rem; color:var(--text-muted);">__HERO_SUB__</span>
                </span>
                <span class="badge-arrow-cue" aria-hidden="true">➔</span>
              </button>

              <!-- Navigation Controls (Prev / Next) -->
              <button class="hero-nav-arrow prev" type="button" data-hero="prev" aria-label="Previous Featured Project">‹</button>
              <button class="hero-nav-arrow next" type="button" data-hero="next" aria-label="Next Featured Project">›</button>

              <!-- Progress Pagination Indicators -->
              <div class="hero-carousel-pagination" id="heroCarouselPagination">__HERO_PILLS__</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section & Org Chart -->
    <section id="about" class="section-wrap scroll-reveal">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">COMPANY PROFILE &amp; LEADERSHIP</span>
          <h2 class="section-title">Built on Rigorous Engineering Discipline</h2>
          <p class="section-desc">
            Headquartered in Addis Ababa, Axulal Consulting Engineers PLC brings together senior Ethiopian highway designers, structural bridge specialists, hydrologists, and geotechnical materials experts.
          </p>
        </div>

        <div class="about-grid">
          <div class="about-narrative">
            <h3>Pioneering Sustainable Infrastructure Across Oromia and Beyond</h3>
            <p>
              Established in 2011 under the Commercial Code of Ethiopia, Axulal Consulting Engineers PLC is fully registered as a <strong>Category-1 Highway and Bridge Consulting Firm</strong> with the Ministry of Urban Development and Construction and certified by regional authorities including the Oromiya Road Authority (ORA).
            </p>
            <p>
              Our multidisciplinary team has successfully planned, designed, and supervised over 145 kilometers of critical all-weather rural road corridors, multi-span reinforced concrete river bridges, and hydraulic catchment networks, transforming economic connectivity for hundreds of thousands of citizens.
            </p>

            <div class="about-pillars">
              <div class="pillar-card">
                <div class="pillar-title">🛡️ Quality Assurance</div>
                <p>Strict conformity with ERA Standards, AASHTO guidelines, and rigorous compressive cube and nuclear compaction testing.</p>
              </div>
              <div class="pillar-card">
                <div class="pillar-title">⛰️ Terrain Mastery</div>
                <p>Proven track record resolving complex mountain benching, black cotton soil stabilization, and heavy flood hydrology.</p>
              </div>
              <div class="pillar-card">
                <div class="pillar-title">📋 Contract Rigor</div>
                <p>Impartial FIDIC and MoWUD contract administration, dispute-free project handovers, and transparent BoQ auditing.</p>
              </div>
              <div class="pillar-card">
                <div class="pillar-title">🤝 Client Partnership</div>
                <p>Trusted partner to regional road authorities, municipal councils, and international development initiatives.</p>
              </div>
            </div>
          </div>

          <!-- Organizational Chart Viewer -->
          <div class="org-chart-box">
            <div class="org-chart-box-header">
              <h4>Corporate Governance Hierarchy</h4>
              <span class="org-chart-badge">CATEGORY-1 CERTIFIED</span>
            </div>
            <div class="org-chart-wrapper" role="button" tabindex="0"
                 data-lightbox-src="assets/org_chart.svg"
                 data-lightbox-caption="Axulal Consulting Engineers PLC — Corporate Governance &amp; Operational Hierarchy">
              <picture>
                <source srcset="assets/org_chart.svg" type="image/svg+xml">
                <img src="assets/org_chart.png" alt="Axulal Corporate Governance &amp; Operational Hierarchy" class="org-chart-thumb" id="orgChartThumb" width="2400" height="1320" loading="lazy" decoding="async">
              </picture>
              <div class="org-chart-overlay-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
                <span>Click to Inspect Full Vector Diagram</span>
              </div>
            </div>
            <div class="org-caption">
              <span>Four-tier institutional structure from Shareholders to Resident Site Offices</span>
              <div style="display:flex; gap:0.5rem; align-items:center;">
                <button class="btn btn-secondary" style="padding:0.35rem 0.75rem; font-size:0.75rem;"
                        data-lightbox-src="assets/org_chart.svg"
                        data-lightbox-caption="Axulal Consulting Engineers PLC — Corporate Governance &amp; Operational Hierarchy">🔍 Zoom In</button>
                <a href="assets/org_chart.png" target="_blank" download="Axulal_Corporate_Governance_Hierarchy_HD.png" class="btn btn-secondary" style="padding:0.35rem 0.75rem; font-size:0.75rem; text-decoration:none;">📥 HD PNG</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="section-wrap alt scroll-reveal">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">COMPREHENSIVE COMPETENCIES</span>
          <h2 class="section-title">End-to-End Civil Engineering Solutions</h2>
          <p class="section-desc">
            From initial reconnaissance and topographic GPS surveying to final defect-liability certification, we provide complete lifecycle engineering.
          </p>
        </div>

        <div class="services-grid">
          <!-- Service 1 -->
          <div class="service-card">
            <div class="service-icon-wrap">🛣️</div>
            <h3 class="service-title">Highway &amp; Route Alignment Design</h3>
            <p class="service-body">
              Geometric alignment design for DC-1 to DC-6 standards using modern digital terrain modeling (Civil 3D). Optimization of cut-and-fill mass haul diagrams, horizontal and vertical curvature, sight distances, and cross-fall cambers tailored to Ethiopian highlands.
            </p>
            <div class="service-tags">
              <span class="stag">ERA Standards</span>
              <span class="stag">DC-2 6m Width</span>
              <span class="stag">Mass-Haul Balance</span>
            </div>
          </div>

          <!-- Service 2 -->
          <div class="service-card">
            <div class="service-icon-wrap">🌉</div>
            <h3 class="service-title">Bridge &amp; Structural Engineering</h3>
            <p class="service-body">
              Comprehensive structural analysis and detailing for reinforced concrete girder bridges, pier columns, abutments, and wingwalls. Designed to AASHTO HS20-44 live loads with deep scour countermeasures and elastomeric expansion bearings.
            </p>
            <div class="service-tags">
              <span class="stag">RC Girder Decks</span>
              <span class="stag">AASHTO HS20-44</span>
              <span class="stag">Deep Abutments</span>
            </div>
          </div>

          <!-- Service 3 -->
          <div class="service-card">
            <div class="service-icon-wrap">💧</div>
            <h3 class="service-title">Hydrology &amp; Hydraulic Modeling</h3>
            <p class="service-body">
              Catchment rainfall run-off modeling, peak discharge calculations, and hydraulic sizing of cross-drainage structures: reinforced single/twin concrete box culverts, hand-dressed mortared stone headwalls, and stone gabion mattress riverbank protections.
            </p>
            <div class="service-tags">
              <span class="stag">50-Yr Return Flood</span>
              <span class="stag">Box Culverts</span>
              <span class="stag">Gabion Mattresses</span>
            </div>
          </div>

          <!-- Service 4 -->
          <div class="service-card">
            <div class="service-icon-wrap">🔬</div>
            <h3 class="service-title">Geotechnical &amp; Materials Testing</h3>
            <p class="service-body">
              Dynamic Cone Penetrometer (DCP) investigations, California Bearing Ratio (CBR) soil testing, Atterberg limit determinations, and borrow pit quarry suitability studies. Specialized solutions for expansive black cotton soils and gravel capping.
            </p>
            <div class="service-tags">
              <span class="stag">CBR Validation</span>
              <span class="stag">Expansive Soil Fixes</span>
              <span class="stag">Quarry Assessment</span>
            </div>
          </div>

          <!-- Service 5 -->
          <div class="service-card">
            <div class="service-icon-wrap">📑</div>
            <h3 class="service-title">Tender Documents &amp; BoQ Drafting</h3>
            <p class="service-body">
              Authoring comprehensive Standard Bidding Documents (SBD) compliant with PPA and FIDIC guidelines. Detailed technical specifications, accurate take-off itemized Bill of Quantities (BoQ), cost estimation, and contractor bid evaluations.
            </p>
            <div class="service-tags">
              <span class="stag">PPA Guidelines</span>
              <span class="stag">FIDIC Conditions</span>
              <span class="stag">Detailed BoQ</span>
            </div>
          </div>

          <!-- Service 6 -->
          <div class="service-card">
            <div class="service-icon-wrap">👷‍♂️</div>
            <h3 class="service-title">Construction Supervision &amp; QA</h3>
            <p class="service-body">
              Full-time resident engineer inspection teams enforcing day-to-day contract compliance. On-site concrete cube compressive crushing tests, nuclear gauge compaction verification, interim payment certificate (IPC) audits, and dispute management.
            </p>
            <div class="service-tags">
              <span class="stag">Resident Supervision</span>
              <span class="stag">Cube Crushing QC</span>
              <span class="stag">IPC Auditing</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section-wrap scroll-reveal">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">VERIFIED INFRASTRUCTURE PORTFOLIO</span>
          <h2 class="section-title">Landmark Road &amp; Bridge Projects</h2>
          <p class="section-desc">
            Explore our completed highway corridors and bridge crossings delivered for the Oromiya Road Authority (ORA) spanning over 145 km of critical regional transport infrastructure.
          </p>
        </div>

        <!-- Toolbar with Responsive Touch-Scrolling Filters -->
        <div class="projects-toolbar">
          <div class="filter-pills" id="projectFilterGroup">
            <button class="filter-btn active" data-filter="all">All Projects</button>
            <button class="filter-btn" data-filter="road">Highways &amp; Roads</button>
            <button class="filter-btn" data-filter="bridge">Bridges</button>
            <button class="filter-btn" data-filter="ejere">Ejere Sector</button>
          </div>

          <div class="search-input-wrap">
            <span class="search-icon" aria-hidden="true">🔍</span>
            <input type="text" id="projectSearch" class="search-input"
                   placeholder="Search project, route or standard..."
                   aria-label="Search projects by name, route or design standard">
          </div>
        </div>

        <!-- Grid of Projects — static, crawlable markup; JS only filters it -->
        <div class="projects-grid" id="projectsContainer">
          __PROJECT_CARDS__
          <p class="projects-empty" id="projectsEmpty" hidden>
            <strong>No projects match that filter.</strong>
            Try a shorter search term or select “All Projects”.
          </p>
        </div>
      </div>
    </section>

    <!-- Field Photographic Plates Gallery (12 Plates) -->
    <section id="gallery" class="section-wrap alt scroll-reveal">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">ENGINEERING DOCUMENTARY</span>
          <h2 class="section-title">Construction Photographic Plates</h2>
          <p class="section-desc">
            Direct high-resolution photographic evidence of resident engineering supervision: subgrade compaction, falsework, retaining structures, and asphalt/gravel handovers.
          </p>
        </div>

        <div class="gallery-grid" id="galleryContainer">
          __GALLERY_CARDS__
        </div>
      </div>
    </section>

    <!-- Credentials & Governance -->
    <section id="credentials" class="section-wrap alt scroll-reveal">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">REGULATORY COMPLIANCE</span>
          <h2 class="section-title">Accreditations &amp; Engineering Standards</h2>
          <p class="section-desc">
            We adhere strictly to national statutory codes, international design criteria, and environmental safeguard policies.
          </p>
        </div>

        <div class="cred-grid">
          <div class="cred-card">
            <div class="cred-icon">📜</div>
            <h4 class="cred-title">Category-1 License</h4>
            <p class="cred-desc">Certified Highway and Bridge Consultant registered with the Federal Ministry of Urban Development &amp; Construction.</p>
          </div>
          <div class="cred-card">
            <div class="cred-icon">📐</div>
            <h4 class="cred-title">ERA Manuals 2024</h4>
            <p class="cred-desc">Full compliance with Ethiopian Roads Administration geometric, drainage, pavement, and bridge design standards.</p>
          </div>
          <div class="cred-card">
            <div class="cred-icon">⚖️</div>
            <h4 class="cred-title">FIDIC / PPA Contracts</h4>
            <p class="cred-desc">Mastery of FIDIC Red Book and standard Ethiopian procurement conditions for transparent contract governance.</p>
          </div>
          <div class="cred-card">
            <div class="cred-icon">🌿</div>
            <h4 class="cred-title">Environmental ESIA</h4>
            <p class="cred-desc">Rigorous environmental and social impact assessments ensuring watershed protection and community sustainability.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact & RFP Portal -->
    <section id="contact" class="section-wrap scroll-reveal">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">TENDER DESK &amp; HEADQUARTERS</span>
          <h2 class="section-title">Initiate a Project Partnership</h2>
          <p class="section-desc">
            Contact our Addis Ababa central office to submit an RFP, discuss a road or bridge tender, or schedule a technical consultation.
          </p>
        </div>

        <div class="contact-layout">
          <!-- Office Contacts -->
          <div class="contact-info-card">
            <h3 style="font-size:1.6rem; margin-bottom:1.5rem;">Addis Ababa Central Desk</h3>
            
            <div class="contact-detail-row">
              <div class="ci-icon">🏢</div>
              <div class="ci-text">
                <h4>Head Office Location</h4>
                <p><strong>Addis International Bank Bldg (Balderas Branch)</strong></p>
                <p>Yeka Sub-City, Addis Ababa, Ethiopia</p>
                <p style="font-size:0.8125rem; color:var(--text-subtle); margin-top:0.25rem;">
                  Coordinates: 9.0231° N, 38.7811° E (Balderas Area)
                </p>
                <div style="margin-top:0.65rem;">
                  <a href="https://maps.app.goo.gl/yg9Xyg8iLbp4tbS18" target="_blank" rel="noopener noreferrer" class="btn btn-secondary" style="padding:0.4rem 0.85rem; font-size:0.8125rem; display:inline-flex; align-items:center; gap:0.4rem; text-decoration:none;">
                    <span>📍</span> Open in Google Maps ↗
                  </a>
                </div>
              </div>
            </div>

            <div class="contact-detail-row">
              <div class="ci-icon">📞</div>
              <div class="ci-text">
                <h4>Telephone &amp; Direct Desk</h4>
                <p><a href="tel:+251911406830">+251 911 406830</a> (Technical Director)</p>
                <p><a href="tel:+251116670000">+251 11 667 0000</a> (Headquarters Desk)</p>
              </div>
            </div>

            <div class="contact-detail-row">
              <div class="ci-icon">✉️</div>
              <div class="ci-text">
                <h4>Official Email Channels</h4>
                <p><a href="mailto:info@axulalengineers.com">info@axulalengineers.com</a></p>
                <p><a href="mailto:tenders@axulalengineers.com">tenders@axulalengineers.com</a></p>
              </div>
            </div>

            <div class="contact-detail-row" style="margin-bottom:1.25rem;">
              <div class="ci-icon">⏱️</div>
              <div class="ci-text">
                <h4>Working Hours</h4>
                <p>Monday - Friday: 8:30 AM - 5:30 PM (EAT)</p>
                <p>Saturday: 8:30 AM - 12:30 PM</p>
              </div>
            </div>

            <!-- Interactive Google Map Embed Card -->
            <div style="border-radius:var(--radius-md); overflow:hidden; border:1px solid var(--border-line); height:210px; position:relative; background:var(--bg-card-subtle); box-shadow:var(--shadow-sm); margin-top:1.5rem;">
              <iframe 
                src="https://maps.google.com/maps?q=9.0231243,38.7811344&amp;hl=en&amp;z=16&amp;output=embed" 
                width="100%" 
                height="100%" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade"
                title="Axulal Head Office Google Map Location - Addis International Bank Balderas">
              </iframe>
              <a href="https://maps.app.goo.gl/yg9Xyg8iLbp4tbS18" target="_blank" rel="noopener noreferrer" style="position:absolute; bottom:0.65rem; right:0.65rem; background:rgba(15,23,42,0.88); backdrop-filter:blur(6px); color:#ffffff; font-size:0.75rem; font-weight:700; padding:0.35rem 0.75rem; border-radius:var(--radius-full); text-decoration:none; display:inline-flex; align-items:center; gap:0.35rem; border:1px solid rgba(255,255,255,0.22); box-shadow:0 2px 8px rgba(0,0,0,0.35);">
                <span>📍 View on Google Maps ↗</span>
              </a>
            </div>
          </div>

          <!-- RFP Form -->
          <div class="rfp-form-card">
            <h3 style="font-size:1.6rem; margin-bottom:0.75rem;">Request a Consultation / RFP</h3>
            <p class="form-note">
              Tell us the corridor, terrain and required milestones. The tender desk replies within one working day.
              Fields marked * are required.
            </p>
            <form id="rfpForm" method="post">
              <div class="form-row-2 form-group">
                <div>
                  <label class="form-label" for="rfpName">Full Name *</label>
                  <input type="text" id="rfpName" name="name" class="form-control" placeholder="Ato / W/ro / Eng." autocomplete="name" required>
                </div>
                <div>
                  <label class="form-label" for="rfpOrg">Organization / Authority *</label>
                  <input type="text" id="rfpOrg" name="org" class="form-control" placeholder="e.g. ORA, ERA, Municipality" autocomplete="organization" required>
                </div>
              </div>

              <div class="form-row-2 form-group">
                <div>
                  <label class="form-label" for="rfpEmail">Email Address *</label>
                  <input type="email" id="rfpEmail" name="email" class="form-control" placeholder="name@domain.gov.et" autocomplete="email" required>
                </div>
                <div>
                  <label class="form-label" for="rfpPhone">Phone Number *</label>
                  <input type="tel" id="rfpPhone" name="phone" class="form-control" placeholder="+251 9..." autocomplete="tel" required>
                </div>
              </div>

              <div class="form-group">
                <label class="form-label" for="rfpCategory">Project Domain</label>
                <select id="rfpCategory" name="category" class="form-control">
                  <option value="highway">Highways &amp; Rural Road Corridor (DC-1 to DC-4)</option>
                  <option value="bridge">Reinforced Concrete Girder River Bridge</option>
                  <option value="drainage">Hydraulic Catchment &amp; Culvert System</option>
                  <option value="supervision">Resident Construction Supervision &amp; Audit</option>
                  <option value="other">General Engineering Advisory</option>
                </select>
              </div>

              <div class="form-group">
                <label class="form-label" for="rfpMessage">Scope Description &amp; Location *</label>
                <textarea id="rfpMessage" name="message" class="form-control" rows="4" placeholder="Specify approximate route length, geographic region, terrain, and required design milestones..." required></textarea>
              </div>

              <!-- Spam trap: real users never see or reach this field. -->
              <div class="form-honeypot" aria-hidden="true">
                <label for="rfpWebsite">Website</label>
                <input type="text" id="rfpWebsite" name="_gotcha" tabindex="-1" autocomplete="off">
              </div>

              <button type="submit" class="btn btn-primary" style="width:100%;">
                Submit Inquiry to Engineering Desk →
              </button>

              <p id="rfpStatus" class="form-status" role="status" aria-live="polite"></p>

              <p class="form-fallback">
                Prefer email? Send your scope to
                <a href="mailto:tenders@axulalengineers.com?subject=Request%20for%20proposal%20%E2%80%94%20highway%20%2F%20bridge%20consultancy">tenders@axulalengineers.com</a>
                or call <a href="tel:+251911406830">+251 911 406830</a>.
              </p>
            </form>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Simplified Modern Footer -->
    <!-- Floating Back to Top Button -->
  <button id="backToTopBtn" class="floating-back-to-top" aria-label="Return to top of page" title="Return to top">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M18 15l-6-6-6 6"/>
    </svg>
  </button>

  <footer id="site-footer">
    <div class="container">
      <div class="footer-simple-wrap">
        <!-- Brand Identity -->
        <div class="footer-brand-block">
          <picture><source type="image/webp" srcset="assets/logo.webp?v=__V__"><img src="assets/logo.png?v=__V__" alt="Axulal Consulting Engineers PLC" class="footer-logo"></picture>
          <p class="footer-tagline">
            Category-1 Highway &amp; Bridge Consulting Engineers · Addis Ababa, Ethiopia
          </p>
          <div class="footer-reg-badge">
            FDRE Reg #01/ORA/2011 · MoWUD &amp; ERA Accredited
          </div>
        </div>

        <!-- Clean Navigation Links -->
        <ul class="footer-simple-nav">
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#gallery">Gallery</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>

        <!-- Direct Contact Info -->
        <div class="footer-contact-pill">
          <span>📞 <a href="tel:+251911406830">+251 911 406830</a></span>
          <span>✉️ <a href="mailto:info@axulalengineers.com">info@axulalengineers.com</a></span>
          <span>📍 <a href="https://maps.app.goo.gl/yg9Xyg8iLbp4tbS18" target="_blank" rel="noopener noreferrer">Balderas, Addis Ababa ↗</a></span>
        </div>
      </div>

      <!-- Footer Bottom -->
      <div class="footer-bottom">
        <div>
          © 2011 – 2026 <strong>Axulal Consulting Engineers PLC (አክሱላል)</strong>. All rights reserved.
        </div>
        <div>
          <a href="#home" class="back-to-top-btn">Back to Top ↑</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Project Detail Modal -->
  <div id="projectModal" class="modal-backdrop" role="dialog" aria-modal="true" aria-labelledby="modalTitle" aria-hidden="true">
    <div class="modal-window">
      <button class="modal-close-btn" type="button" data-close-modal="project" aria-label="Close project overview">✕</button>
      <div id="modalContent">
        <!-- Injected via JavaScript -->
      </div>
    </div>
  </div>

  <!-- Fullscreen Photographic Lightbox -->
  <div id="lightboxModal" class="modal-backdrop" role="dialog" aria-modal="true" aria-label="Enlarged field photograph" aria-hidden="true">
    <button class="modal-close-btn" type="button" data-close-modal="lightbox" aria-label="Close enlarged photograph">✕</button>
    <div class="lightbox-img-box">
      <img id="lightboxImg" src="" alt="Enlarged view" class="lightbox-img">
      <div id="lightboxCaption" class="lightbox-caption"></div>
    </div>
  </div>

  <!-- JavaScript Application -->
  <script defer src="assets/js/data.js?v=__V__"></script>
  <script defer src="assets/js/site.js?v=__V__"></script>
</body>
</html>"""

# ---------------------------------------------------------------------------
# RENDERING HELPERS
# ---------------------------------------------------------------------------

# Curated hero features. Each entry points at a real PROJECTS_DATA record so the
# slide copy, metric and image can never drift from the project dossier.
HERO_FEATURE = [
    {
        "id": "P-06",
        "title": "Awash River Bridge",
        "tag": "FEATURED INFRASTRUCTURE · AWASH BRIDGE",
        "icon": "🌉",
        "tail": "RC Girder · ORA Contract · West Shewa",
    },
    {
        "id": "P-11",
        "title": "Berga River Bridge",
        "tag": "FEATURED INFRASTRUCTURE · BERGA BRIDGE",
        "icon": "🌉",
        "tail": "RC Girder Deck · Heavy Falsework",
    },
    {
        "id": "P-01",
        "title": "Ginchi – Danisa Corridor",
        "tag": "FEATURED INFRASTRUCTURE · GINCHI HIGHWAY",
        "icon": "🛣️",
        "tail": "DC-2 Granular Alignment · ORA",
    },
    {
        "id": "P-10",
        "title": "Ejere – Endode Alignment",
        "tag": "FEATURED INFRASTRUCTURE · EJERE SECTOR",
        "icon": "🛣️",
        "tail": "Mountainous Benching & Drainage",
    },
]


def _project_by_id(project_id):
    for p in PROJECTS_DATA:
        if p["id"] == project_id:
            return p
    raise KeyError("HERO_FEATURE references unknown project id %r" % project_id)


def render_hero_slides(features=None):
    """Hero slides as real buttons with data-* metadata read by site.js."""
    features = HERO_FEATURE if features is None else features
    out = []
    for index, feature in enumerate(features):
        p = _project_by_id(feature["id"])
        img = p["img"]
        first = index == 0
        out.append(
            """
                <button type="button" class="hero-slide%(active)s" data-index="%(index)d"
                        data-project="%(id)s" data-tag="%(tag)s" data-icon="%(icon)s"
                        data-title="%(title)s" data-sub="%(sub)s"
                        aria-label="Open dossier: %(aria)s">
                  %(picture)s
                </button>""" % {
                "active": " active" if first else "",
                "index": index,
                "id": p["id"],
                "tag": feature["tag"],
                "icon": feature["icon"],
                "title": feature["title"],
                "sub": "%s · %s" % (p["metric"], feature["tail"]),
                "aria": _esc(p["name"]),
                "picture": _picture(
                    img,
                    _esc(p["name"]),
                    img_class="hero-slide-img",
                    loading="eager" if first else "lazy",
                    fetchpriority="high" if first else None,
                ),
            }
        )
    return "".join(out)


def render_hero_pills(features=None):
    """Pagination pills as real buttons so the carousel is keyboard reachable."""
    features = HERO_FEATURE if features is None else features
    out = []
    for index, feature in enumerate(features):
        p = _project_by_id(feature["id"])
        out.append(
            """
                <button type="button" class="carousel-pill%(active)s" data-index="%(index)d"
                        aria-label="Show featured project %(n)d of %(total)d: %(name)s"%(current)s></button>""" % {
                "active": " active" if index == 0 else "",
                "index": index,
                "n": index + 1,
                "total": len(features),
                "name": p["name"],
                "current": ' aria-current="true"' if index == 0 else "",
            }
        )
    return "".join(out)


def _photo_sources():
    """Every source photo the page references, de-duplicated and in order."""
    seen = set()
    ordered = []
    for item in list(PROJECTS_DATA) + list(GALLERY_DATA):
        src = item.get("img")
        if src and src not in seen:
            seen.add(src)
            ordered.append(src)
    return ordered


def _webp_variant(src, thumbnail=False):
    """WebP sibling of a photo (or thumbnail), or None when not generated."""
    if not src:
        return None
    stem, ext = os.path.splitext(src)
    if ext.lower() not in (".jpg", ".jpeg", ".png"):
        return None
    if thumbnail:
        thumb_candidate = stem + "_thumb.webp"
        if os.path.exists(os.path.join(ROOT, thumb_candidate)):
            return thumb_candidate
    candidate = stem + ".webp"
    return candidate if os.path.exists(os.path.join(ROOT, candidate)) else None


def ensure_webp(quality=WEBP_QUALITY):
    """Generate WebP siblings and thumbnails so <picture> can serve smaller payloads.

    Non-fatal by design: without Pillow the build simply ships JPEG only.
    """
    try:
        from PIL import Image
    except ImportError:
        print("  webp: skipped (Pillow not installed) - JPEG fallback only")
        return 0

    generated = fresh = failed = 0
    for src in _photo_sources():
        source = os.path.join(ROOT, src)
        stem = os.path.splitext(source)[0]
        target = stem + ".webp"
        thumb_target = stem + "_thumb.webp"
        rel_target = os.path.splitext(src)[0] + ".webp"

        if not os.path.exists(source):
            failed += 1
            print("  webp: missing source %s" % src)
            continue

        try:
            with Image.open(source) as image:
                w, h = image.size

                # 1. High-Resolution WebP
                if not (os.path.exists(target) and os.path.getmtime(target) >= os.path.getmtime(source)):
                    image.convert("RGB").save(target, "WEBP", quality=quality, method=6)
                    generated += 1
                else:
                    fresh += 1

                # 2. Optimized Card Thumbnail WebP (max 480px width)
                if not (os.path.exists(thumb_target) and os.path.getmtime(thumb_target) >= os.path.getmtime(source)):
                    target_w = 480
                    if w > target_w:
                        ratio = target_w / w
                        thumb = image.resize((target_w, int(h * ratio)), Image.Resampling.LANCZOS)
                    else:
                        thumb = image
                    thumb.convert("RGB").save(thumb_target, "WEBP", quality=78, method=6)
                    generated += 1
                else:
                    fresh += 1
        except Exception as exc:
            failed += 1
            print("  webp: failed for %s (%s)" % (rel_target, exc))

    print(
        "  webp: %d generated, %d up to date, %d failed"
        % (generated, fresh, failed)
    )
    return generated


def _picture(src, alt, img_class="", loading="lazy", fetchpriority=None, thumbnail=False):
    """<picture> with a WebP source and the original JPEG as the fallback."""
    w, h = IMG_DIMS.get(src, (0, 0))
    bits = []
    if img_class:
        bits.append('class="%s"' % img_class)
    bits.append('src="%s"' % src)
    bits.append('alt="%s"' % alt)
    if w and h:
        bits.append('width="%d" height="%d"' % (w, h))
        bits.append('style="aspect-ratio:%d/%d"' % (w, h))
    bits.append('loading="%s"' % loading)
    bits.append('decoding="async"')
    if fetchpriority:
        bits.append('fetchpriority="%s"' % fetchpriority)

    webp = _webp_variant(src, thumbnail=thumbnail)
    source = (
        '<source type="image/webp" srcset="%s">' % webp if webp else ""
    )
    return (
        "<picture>%s<img %s></picture>" % (source, " ".join(bits))
    )


def _esc(value):
    """HTML-escape text for element content and quoted attribute values."""
    return html_escape(str(value), quote=True)


def _dims_attrs(img, style=True):
    """width/height attributes (optionally an aspect-ratio guard) from IMG_DIMS."""
    w, h = IMG_DIMS.get(img, (0, 0))
    if not w or not h:
        return ""
    bits = ' width="%d" height="%d"' % (w, h)
    if style:
        bits += ' style="aspect-ratio:%d/%d"' % (w, h)
    return bits


def render_project_cards(projects):
    """Static, crawlable project cards. JS only toggles `hidden` on this markup."""
    out = []
    for p in projects:
        is_bridge = p["type"] == "bridge"
        search_blob = " ".join(
            str(p.get(key, ""))
            for key in ("id", "name", "standard", "desc", "metric", "chainage", "structures", "scope")
        ).lower()
        out.append(
            """
          <article class="project-card" id="%(id)s" data-type="%(type)s"
                   data-hub="%(hub)s" data-search="%(search)s">
            <div class="project-img-wrap">
              %(picture)s
              <span class="project-badge">%(id)s</span>
              <span class="project-type-badge %(type_class)s">%(type_label)s</span>
            </div>
            <div class="project-card-body">
              <h3 class="project-name">%(name)s</h3>
              <div class="project-meta-list">
                <div class="pm-item">
                  <span class="pm-label">%(metric_label)s</span>
                  <span class="pm-val">%(metric)s</span>
                </div>
                <div class="pm-item">
                  <span class="pm-label">Design Standard</span>
                  <span class="pm-val">%(standard_label)s</span>
                </div>
                <div class="pm-item" style="grid-column: 1 / -1;">
                  <span class="pm-label">Chainage Extents</span>
                  <span class="pm-val">%(chainage)s</span>
                </div>
              </div>
              <p class="project-desc-short">%(desc)s</p>
              <div class="project-footer">
                <span class="project-client">Client: ORA</span>
                <button type="button" class="view-spec-btn" aria-haspopup="dialog">
                  View Blueprint &amp; Specs &rarr;
                </button>
              </div>
            </div>
          </article>""" % {
                "id": _esc(p["id"]),
                "type": _esc(p["type"]),
                "hub": _esc(p.get("hub", "")),
                "search": _esc(search_blob),
                "picture": _picture(
                    p["img"], _esc(p["name"]), img_class="project-img", thumbnail=True
                ),
                "name": _esc(p["name"]),
                "metric": _esc(p["metric"]),
                "chainage": _esc(p["chainage"]),
                "desc": _esc(p["desc"]),
                "type_class": "type-bridge" if is_bridge else "type-road",
                "type_label": "RC Bridge" if is_bridge else "Highway",
                "metric_label": "Span Length" if is_bridge else "Route Length",
                "standard_label": "RC Girder" if is_bridge else "DC-2 Standard",
            }
        )
    return "".join(out)


def render_gallery_cards(gallery):
    """Static field plates. The whole plate is opened from its data-* attributes."""
    out = []
    for g in gallery:
        out.append(
            """
          <figure class="gallery-card" data-category="%(cat)s" data-img="%(img)s"
                  data-plate="%(plate)s" data-title="%(title)s" data-desc="%(desc)s">
            <button type="button" class="gallery-open" aria-haspopup="dialog"
                    aria-label="Open plate %(plate)s: %(title)s">
              <span class="gallery-img-wrap">
                %(picture)s                <span class="gallery-plate-pill">%(plate)s</span>
                <span class="gallery-zoom-pill">&#128269; Zoom</span>
              </span>
            </button>
            <div class="gallery-card-body">
              <h4 class="gallery-card-title">%(title)s</h4>
              <p class="gallery-card-desc">%(desc)s</p>
            </div>
          </figure>""" % {
                "cat": _esc(g["category"]),
                "img": _esc(g["img"]),
                "plate": _esc(g["plate"]),
                "title": _esc(g["title"]),
                "desc": _esc(g["desc"]),
                "dims": _dims_attrs(g["img"]),
                "picture": _picture(g["img"], _esc(g["title"]), img_class="gallery-img", thumbnail=True),
            }
        )
    return "".join(out)


def build():
    print("Building Axulal Consulting Engineers PLC website...")
    ensure_webp()

    projects_json = json.dumps(PROJECTS_DATA, ensure_ascii=False, indent=2)
    gallery_json = json.dumps(GALLERY_DATA, ensure_ascii=False, indent=2)

    data_js = (
        "/* Axulal project & gallery data. Generated by scripts/build_worldclass_site.py. */\n"
        "window.PROJECTS = " + projects_json + ";\n"
        "window.GALLERY = " + gallery_json + ";\n"
    )

    hero_first = HERO_FEATURE[0]
    hero_first_project = _project_by_id(hero_first["id"])

    html = (
        HTML.replace("__HERO_SLIDES__", render_hero_slides())
        .replace("__HERO_PILLS__", render_hero_pills())
        .replace("__HERO_TAG__", hero_first["tag"])
        .replace("__HERO_ICON__", hero_first["icon"])
        .replace("__HERO_TITLE__", hero_first["title"])
        .replace(
            "__HERO_SUB__",
            "%s · %s" % (hero_first_project["metric"], hero_first["tail"]),
        )
        .replace("__PROJECT_CARDS__", render_project_cards(PROJECTS_DATA))
        .replace("__GALLERY_CARDS__", render_gallery_cards(GALLERY_DATA))
        .replace("__V__", ASSET_VERSION)
    )

    outputs = [
        ("index.html", html),
        (os.path.join("assets", "css", "site.css"), CSS),
        (os.path.join("assets", "js", "site.js"), JS),
        (os.path.join("assets", "js", "data.js"), data_js),
    ]
    for rel, content in outputs:
        full = os.path.join(ROOT, rel)
        parent = os.path.dirname(full)
        if parent and not os.path.isdir(parent):
            os.makedirs(parent, exist_ok=True)
        with open(full, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content if content.endswith("\n") else content + "\n")
        print("  wrote", rel.replace(os.sep, "/"))


if __name__ == "__main__":
    build()
