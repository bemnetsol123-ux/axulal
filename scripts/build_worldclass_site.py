#!/usr/bin/env python3
"""
Master Build Script for Axulal Consulting Engineers PLC
Generates index.html, assets/css/site.css, assets/js/site.js, and assets/js/data.js.
Incorporates:
- Modern Architectural Horizon Layout (Bento Grid + Telemetry HUD)
- Concise, short navigation menu names (About, Services, Projects, Gallery, Credentials, Contact)
- Dedicated Headquarters Desk in Footer with high-contrast visible logo (zero white-out)
- Procurement & Tender Intake Terminal in #contact (zero redundancy)
- 3 Initial Flagship Projects with Regional Hub Filters + Expand to all 12
- 4 Initial Construction Lifecycle Plates + Expand to all 12 + Lightbox
- Free FormSubmit.co AJAX RFP submission integration
"""

import os
import sys
import json
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
PROJECTS_DIR = ASSETS_DIR / "projects"
GALLERY_DIR = ASSETS_DIR / "gallery"
CSS_FILE = ASSETS_DIR / "css" / "site.css"
JS_FILE = ASSETS_DIR / "js" / "site.js"
DATA_FILE = ASSETS_DIR / "js" / "data.js"
INDEX_FILE = BASE_DIR / "index.html"

ASSET_VERSION = "20"
WEBP_QUALITY = 82

PROJECTS_DATA = [
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
        "chainage": "STA 0+000 - STA 27+000",
        "structures": "26 Slab/Pipe Culverts, 3 Box Culverts, 950m Retaining Walls",
        "desc": "Our largest continuous alignment: 27.0 kilometers of all-weather classified road engineered through complex catchment basins, featuring heavy rock cut benching and comprehensive community link ramps.",
        "badge": "FLAGSHIP CORRIDOR",
        "pill": "27.0 KM ALIGNMENT"
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
        "structures": "24m RC Girder Superstructure, Deep Reinforced Abutment Footings",
        "desc": "Single-span reinforced concrete deck girder bridge engineered with deep abutment footings and hydraulic scour defense over the high-discharge Awash River basin.",
        "badge": "RC BRIDGE",
        "pill": "24.0 M SPAN"
    },
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
        "desc": "15.5 km mountainous highway corridor featuring 1,200m mortared stone masonry retaining structures and heavy hydraulic box culverts engineered for intensive seasonal runoff.",
        "badge": "HIGHWAY",
        "pill": "15.5 KM"
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
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_11_berga_bridge.jpg",
        "chainage": "Bridge Station STA 1+800 (Berga River Crossing)",
        "structures": "22m RC Girder, Reinforced Concrete Abutments with Wing Walls",
        "desc": "22-meter RC girder superstructure over Berga River; site quality supervision, rebar cage tensile testing, and compressive validation.",
        "badge": "RC BRIDGE",
        "pill": "22.0 M SPAN"
    },
    {
        "id": "P-02",
        "name": "Asgori-Kotoba Gravel Road Project (Lot-1 & Lot-2)",
        "type": "road",
        "hub": "ejere",
        "length": 22.5,
        "metric": "22.5 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_2_asgori_kotoba.jpg",
        "chainage": "STA 0+000 - STA 22+500 (Dual Contract Lots)",
        "structures": "18 Pipe Culverts, 4 Box Culverts, 800m Hillside Retaining Walls",
        "desc": "Major agrarian connector featuring 18 pipe culverts, 4 multi-barrel box culverts, and heavy hillside cut benching.",
        "badge": "DUAL LOT",
        "pill": "22.5 KM"
    },
    {
        "id": "P-08",
        "name": "Ejere-Kake-Arertu Gravel Road Project",
        "type": "road",
        "hub": "ejere",
        "length": 21.5,
        "metric": "21.5 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_8_ejere_kake.jpg",
        "chainage": "STA 0+000 - STA 21+500",
        "structures": "19 Slab/Pipe Culverts, 2 Major Box Culverts, Mountain Cuts",
        "desc": "Mountainous rural highway connecting agricultural trade centers across West Shewa with comprehensive drainage catchment engineering.",
        "badge": "HIGHWAY",
        "pill": "21.5 KM"
    },
    {
        "id": "P-09",
        "name": "Olenkomi-Hamdo Gravel Road Project",
        "type": "road",
        "hub": "awash",
        "length": 11.0,
        "metric": "11.0 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_9_olenkomi_hamdo.jpg",
        "chainage": "STA 0+000 - STA 11+000",
        "structures": "11 Cross-Drainage Culverts, Sub-base Drainage Layers",
        "desc": "Highland agricultural link route with optimized alignment geometry, extensive cuts, and high-load gravel surfacing.",
        "badge": "HIGHWAY",
        "pill": "11.0 KM"
    },
    {
        "id": "P-03",
        "name": "Asgori-Kotoba Link Road Project",
        "type": "road",
        "hub": "ejere",
        "length": 8.5,
        "metric": "8.5 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_3_asgori_link.jpg",
        "chainage": "STA 0+000 - STA 8+500",
        "structures": "8 Slab Culverts, Ditch Linings, Slope Stabilizations",
        "desc": "Feeder corridor integrating local communities into the main transport artery, engineered to withstand intense seasonal rains.",
        "badge": "FEEDER",
        "pill": "8.5 KM"
    },
    {
        "id": "P-04",
        "name": "Arbu-Roge Gravel Road Project",
        "type": "road",
        "hub": "ginchi",
        "length": 10.0,
        "metric": "10.0 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_4_arbu_roge.jpg",
        "chainage": "STA 0+000 - STA 10+000",
        "structures": "10 Pipe/Slab Culverts, Subgrade Stabilization",
        "desc": "Connecting remote rural communities to municipal service hubs with durable crushed gravel sub-base courses.",
        "badge": "HIGHWAY",
        "pill": "10.0 KM"
    },
    {
        "id": "P-05",
        "name": "Asgori-Roge Gravel Road Project",
        "type": "road",
        "hub": "ejere",
        "length": 6.2,
        "metric": "6.2 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_5_asgori_roge.jpg",
        "chainage": "STA 0+000 - STA 6+200",
        "structures": "6 Pipe Culverts, Selected Granular Fill",
        "desc": "Vital regional agricultural connector built to ERA DC-2 standards with optimized longitudinal slopes and cross-fall campering.",
        "badge": "FEEDER",
        "pill": "6.2 KM"
    },
    {
        "id": "P-10",
        "name": "Hamdo-Awash Bune Gravel Road Project",
        "type": "road",
        "hub": "awash",
        "length": 14.0,
        "metric": "14.0 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_10_hamdo_awash.jpg",
        "chainage": "STA 0+000 - STA 14+000",
        "structures": "15 Drainage Culverts, River Approach Embankments",
        "desc": "Key connector traversing the Awash River plain, designed with elevated embankment fills and anti-scour protection.",
        "badge": "HIGHWAY",
        "pill": "14.0 KM"
    },
    {
        "id": "P-12",
        "name": "Holota-Kake-Berga River Gravel Road Project",
        "type": "road",
        "hub": "berga",
        "length": 9.6,
        "metric": "9.6 km",
        "standard": "6.0m Width (DC-2 Standard)",
        "speed": "50 km/h Design Speed",
        "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
        "client": "Oromiya Road Authority (ORA)",
        "img": "assets/projects/proj_12_holota_kake.jpg",
        "chainage": "STA 0+000 - STA 9+600",
        "structures": "9 Pipe/Slab Culverts, Retaining Masonry at River Approaches",
        "desc": "Scenic and technically rigorous route providing all-weather access across the Berga River catchment area.",
        "badge": "CORRIDOR",
        "pill": "9.6 KM"
    }
]

GALLERY_DATA = [
    {
        "plate": "PLATE 04",
        "title": "Hillside Benching & Earthwork",
        "phase": "PHASE 1 · EXCAVATION",
        "img": "assets/gallery/plate_04_hillside_cut.jpg",
        "category": "earthworks",
        "desc": "Heavy crawler excavator cutting 1:1 roadway benches through steep volcanic rock slopes on Asgori-Kotoba alignment."
    },
    {
        "plate": "PLATE 01",
        "title": "Sub-Base Compaction",
        "phase": "PHASE 2 · COMPACTION",
        "img": "assets/gallery/plate_01_compaction.jpg",
        "category": "compaction",
        "desc": "Heavy 15-ton vibratory road roller achieving 98% Modified AASHTO compaction density on selected granular sub-base."
    },
    {
        "plate": "PLATE 03",
        "title": "Hydraulic Drainage Culvert",
        "phase": "PHASE 3 · DRAINAGE",
        "img": "assets/gallery/plate_03_drainage_culvert.jpg",
        "category": "drainage",
        "desc": "Hand-dressed mortared stone masonry headwalls and barrel construction providing high-capacity flood runoff cross-drainage."
    },
    {
        "plate": "PLATE 02",
        "title": "Bridge Pier & Abutment",
        "phase": "PHASE 4 · STRUCTURES",
        "img": "assets/gallery/plate_02_bridge_pier.jpg",
        "category": "structures",
        "desc": "Reinforced concrete pier column, abutment formwork, and heavy falsework bracing for Awash River Girder Bridge."
    },
    {
        "plate": "PLATE 06",
        "title": "Substructure Deep Foundation",
        "phase": "PHASE 5 · FOUNDATIONS",
        "img": "assets/gallery/plate_06_foundation_works.jpg",
        "category": "structures",
        "desc": "Excavation and reinforced concrete footing placement for bridge piers down to competent rock strata."
    },
    {
        "plate": "PLATE 05",
        "title": "Finished DC-2 Carriageway",
        "phase": "PHASE 6 · SURFACING",
        "img": "assets/gallery/plate_05_road_alignment.jpg",
        "category": "surfacing",
        "desc": "Completed all-weather DC-2 gravel carriageway with 4% cross-fall camber smoothly winding through rural Oromia."
    },
    {
        "plate": "PLATE 07",
        "title": "Box Culvert Formwork",
        "phase": "PHASE 7 · HYDRAULICS",
        "img": "assets/gallery/plate_07_box_culvert.jpg",
        "category": "drainage",
        "desc": "Steel reinforcement and formwork assembly for a double-barrel RC box culvert designed for 50-year storm recurrence."
    },
    {
        "plate": "PLATE 08",
        "title": "Laboratory Materials Testing",
        "phase": "PHASE 8 · MATERIALS QC",
        "img": "assets/gallery/plate_08_materials_testing.jpg",
        "category": "quality",
        "desc": "On-site field laboratory testing: sieve analysis, Atterberg limits, and concrete cube compression crush tests."
    },
    {
        "plate": "PLATE 09",
        "title": "Masonry Retaining Wall",
        "phase": "PHASE 9 · STABILIZATION",
        "img": "assets/gallery/plate_09_retaining_wall.jpg",
        "category": "structures",
        "desc": "Mortared stone masonry gravity retaining wall protecting steep roadway cut slopes from landslide failure."
    },
    {
        "plate": "PLATE 10",
        "title": "Mountain Alignment Grading",
        "phase": "PHASE 10 · EARTHWORKS",
        "img": "assets/gallery/plate_10_mountain_cut.jpg",
        "category": "earthworks",
        "desc": "Heavy motor grader shaping horizontal alignment curves and ditch profiles through high-altitude highland terrain."
    },
    {
        "plate": "PLATE 11",
        "title": "Girder Superstructure Falsework",
        "phase": "PHASE 11 · SUPERSTRUCTURE",
        "img": "assets/gallery/plate_11_bridge_deck.jpg",
        "category": "structures",
        "desc": "Heavy structural timber falsework supporting formwork and rebar placement for 22m span concrete deck girders."
    },
    {
        "plate": "PLATE 12",
        "title": "Final Corridor Handover",
        "phase": "PHASE 12 · HANDOVER",
        "img": "assets/gallery/plate_12_finished_road.jpg",
        "category": "surfacing",
        "desc": "Joint client-consultant final inspection: verifying cross-sections, drainage outfalls, and surface rideability."
    }
]



CSS = r"""
:root {
  --brand-violet: #4e2a84;
  --brand-violet-dark: #371d60;
  --brand-violet-soft: #f4effa;
  --brand-violet-glow: rgba(78, 42, 132, 0.35);
  --accent-amber: #e67e22;
  --accent-amber-soft: #fef5ec;
  --accent-emerald: #10b981;
  --text-main: #0f172a;
  --text-muted: #475569;
  --text-subtle: #64748b;
  --bg-page: #f8fafc;
  --bg-card: #ffffff;
  --bg-dark: #0b1120;
  --border-line: #e2e8f0;
  --border-dark: rgba(255, 255, 255, 0.12);
  --font-heading: 'Archivo', sans-serif;
  --font-body: 'Source Sans 3', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-full: 9999px;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
  --shadow-lg: 0 12px 32px rgba(15,23,42,0.12);
  --shadow-xl: 0 20px 48px rgba(15,23,42,0.18);
  --header-h: 72px;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: var(--header-h);
}

body {
  font-family: var(--font-body);
  background: var(--bg-page);
  color: var(--text-main);
  line-height: 1.6;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
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

.container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--brand-violet);
  color: white;
  padding: 8px;
  z-index: 1000;
  transition: top 0.2s ease;
}
.skip-link:focus {
  top: 0;
}

/* Glass Header */
.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.94);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-line);
  transition: all 0.25s ease;
}
.header-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: var(--header-h);
}
.brand-logo-img {
  height: 44px;
  width: auto;
  display: block;
}
.nav-links {
  display: flex;
  gap: 1.75rem;
  list-style: none;
}
.nav-links a {
  font-family: var(--font-heading);
  font-size: 0.9375rem;
  font-weight: 700;
  color: var(--text-muted);
  transition: color 0.2s ease;
  position: relative;
}
.nav-links a:hover, .nav-links a.active {
  color: var(--brand-violet);
}
.header-cta-group {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}
.phone-direct {
  font-family: var(--font-mono);
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--brand-violet);
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
}
.btn-primary {
  background: var(--brand-violet);
  color: #ffffff;
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.9375rem;
  padding: 0.65rem 1.35rem;
  border-radius: var(--radius-full);
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  box-shadow: 0 4px 14px var(--brand-violet-glow);
  transition: all 0.25s ease;
  border: none;
  cursor: pointer;
}
.btn-primary:hover {
  background: var(--brand-violet-dark);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px var(--brand-violet-glow);
  color: #ffffff;
}

/* Mobile Toggle */
.btn-mobile-toggle {
  display: none;
  background: transparent;
  border: 1.5px solid var(--border-line);
  border-radius: var(--radius-sm);
  padding: 0.45rem 0.65rem;
  font-size: 1.25rem;
  cursor: pointer;
  color: var(--text-main);
}

/* Mobile Drawer */
#mobileDrawer {
  display: none;
  position: fixed;
  top: var(--header-h);
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--bg-card);
  z-index: 99;
  padding: 1.75rem;
  overflow-y: auto;
  border-bottom: 1px solid var(--border-line);
  box-shadow: var(--shadow-xl);
}
#mobileDrawer ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 1.15rem;
  font-size: 1.15rem;
  font-weight: 700;
  font-family: var(--font-heading);
}
#mobileDrawer a {
  display: block;
  padding: 0.4rem 0;
  color: var(--text-main);
}
#mobileDrawer a:hover {
  color: var(--brand-violet);
}

/* Hero Section (Architectural Viewport) */
.hero-viewport {
  position: relative;
  background: var(--bg-dark);
  color: #ffffff;
  padding: 5rem 0 3.5rem;
  overflow: hidden;
}
.hero-viewport::before {
  content: '';
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(circle at 80% 20%, rgba(78, 42, 132, 0.45) 0%, transparent 60%),
    radial-gradient(circle at 10% 80%, rgba(230, 126, 34, 0.18) 0%, transparent 50%);
  pointer-events: none;
}
.hero-grid-overlay {
  position: absolute;
  inset: 0;
  background-size: 40px 40px;
  background-image: linear-gradient(to right, rgba(255, 255, 255, 0.035) 1px, transparent 1px),
                    linear-gradient(to bottom, rgba(255, 255, 255, 0.035) 1px, transparent 1px);
  opacity: 0.75;
  pointer-events: none;
}
.hero-layout {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 3.5rem;
  align-items: center;
}
.hero-badge-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-full);
  padding: 0.35rem 0.9rem;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--accent-amber);
  letter-spacing: 0.5px;
  margin-bottom: 1.25rem;
}
.hero-title {
  font-family: var(--font-heading);
  font-size: clamp(2.2rem, 4vw, 3.4rem);
  font-weight: 900;
  line-height: 1.12;
  letter-spacing: -0.5px;
  margin-bottom: 1.25rem;
}
.hero-title .highlight {
  background: linear-gradient(135deg, #ffffff 40%, #c4b5fd 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero-desc {
  font-size: 1.125rem;
  color: #94a3b8;
  line-height: 1.7;
  margin-bottom: 2rem;
  max-width: 580px;
}
.hero-btn-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
.btn-secondary-glass {
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.25);
  color: #ffffff;
  padding: 0.65rem 1.35rem;
  border-radius: var(--radius-full);
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.9375rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.25s ease;
}
.btn-secondary-glass:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
  color: #ffffff;
}

/* Telemetry HUD Glass Card */
.telemetry-card {
  background: rgba(15, 23, 42, 0.78);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border-dark);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  box-shadow: var(--shadow-xl);
  position: relative;
}
.telemetry-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255,255,255,0.1);
  padding-bottom: 0.85rem;
  margin-bottom: 1.15rem;
}
.telemetry-tag {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  color: var(--accent-amber);
  font-weight: 700;
  letter-spacing: 0.5px;
}
.telemetry-live-dot {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.72rem;
  color: var(--accent-emerald);
  font-weight: 600;
  font-family: var(--font-mono);
}
.telemetry-live-dot::before {
  content: '';
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent-emerald);
  box-shadow: 0 0 8px var(--accent-emerald);
  animation: pulseDot 2s infinite;
}
@keyframes pulseDot {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}
.telemetry-img-wrap {
  border-radius: var(--radius-md);
  overflow: hidden;
  height: 200px;
  position: relative;
  margin-bottom: 1.15rem;
  background: #000;
}
.telemetry-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.telemetry-title {
  font-family: var(--font-heading);
  font-size: 1.25rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
  color: #ffffff;
}
.telemetry-spec-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.65rem;
  margin-top: 1rem;
}
.spec-item {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-sm);
  padding: 0.65rem 0.85rem;
}
.spec-label {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: #94a3b8;
  text-transform: uppercase;
  display: block;
  margin-bottom: 0.2rem;
}
.spec-value {
  font-family: var(--font-mono);
  font-size: 0.875rem;
  font-weight: 700;
  color: #ffffff;
}

/* Live Telemetry Marquee */
.marquee-bar {
  margin-top: 3.5rem;
  background: rgba(11, 17, 32, 0.9);
  backdrop-filter: blur(8px);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding: 0.75rem 0;
  overflow: hidden;
  white-space: nowrap;
  position: relative;
}
.marquee-track {
  display: inline-flex;
  gap: 2.5rem;
  animation: marqueeScroll 26s linear infinite;
}
@keyframes marqueeScroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.marquee-item {
  font-family: var(--font-mono);
  font-size: 0.8125rem;
  font-weight: 600;
  color: #cbd5e1;
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  letter-spacing: 0.5px;
}
.marquee-item::after {
  content: '◆';
  color: var(--accent-amber);
  font-size: 0.65rem;
}

/* 4-Stat Key Proof Band */
.stat-band {
  background: var(--bg-card);
  border-bottom: 1px solid var(--border-line);
  padding: 2.5rem 0;
}
.stat-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}
.stat-box {
  text-align: center;
  padding: 1.25rem 1rem;
  border-right: 1px solid var(--border-line);
}
.stat-box:last-child {
  border-right: none;
}
.stat-number {
  font-family: var(--font-heading);
  font-size: 2.5rem;
  font-weight: 900;
  color: var(--brand-violet);
  line-height: 1;
  margin-bottom: 0.4rem;
}
.stat-unit {
  color: var(--accent-amber);
  font-size: 1.75rem;
}
.stat-label {
  font-size: 0.9375rem;
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 0.2rem;
}
.stat-sub {
  font-size: 0.8125rem;
  color: var(--text-muted);
}

/* Section Structure */
.section-wrap {
  padding: 5rem 0;
}
.section-wrap.alt {
  background: #ffffff;
  border-top: 1px solid var(--border-line);
  border-bottom: 1px solid var(--border-line);
}
.section-head {
  margin-bottom: 3rem;
  text-align: center;
  max-width: 760px;
  margin-left: auto;
  margin-right: auto;
}
.section-tag {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 800;
  color: var(--brand-violet);
  background: var(--brand-violet-soft);
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-full);
  display: inline-block;
  margin-bottom: 0.85rem;
  letter-spacing: 0.75px;
}
.section-title {
  font-family: var(--font-heading);
  font-size: clamp(1.85rem, 3vw, 2.5rem);
  font-weight: 800;
  color: var(--text-main);
  line-height: 1.2;
  margin-bottom: 0.85rem;
}
.section-desc {
  font-size: 1.05rem;
  color: var(--text-muted);
}

/* About Bento Grid */
.about-bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
}
.about-bento-card {
  background: var(--bg-card);
  border: 1px solid var(--border-line);
  border-radius: var(--radius-lg);
  padding: 2.25rem 2rem;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  transition: transform 0.28s ease, box-shadow 0.28s ease;
}
.about-bento-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--brand-violet);
}
.about-card-icon {
  font-size: 2.25rem;
  margin-bottom: 1.25rem;
  display: inline-block;
}
.about-card-title {
  font-family: var(--font-heading);
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--text-main);
  margin-bottom: 0.75rem;
}
.about-card-text {
  font-size: 0.9375rem;
  color: var(--text-muted);
  line-height: 1.65;
  margin-bottom: 1.25rem;
}
.about-card-highlight {
  font-family: var(--font-mono);
  font-size: 0.8125rem;
  font-weight: 700;
  color: var(--brand-violet);
  margin-top: auto;
  padding-top: 0.85rem;
  border-top: 1px solid var(--border-line);
}

/* Services Grid */
.services-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}
.service-card {
  background: var(--bg-page);
  border: 1px solid var(--border-line);
  border-radius: var(--radius-lg);
  padding: 2rem 1.75rem;
  display: flex;
  flex-direction: column;
  transition: transform 0.28s ease, box-shadow 0.28s ease;
}
.service-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--brand-violet);
}
.service-icon-box {
  font-size: 2rem;
  margin-bottom: 1.15rem;
}
.service-title {
  font-family: var(--font-heading);
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--text-main);
  margin-bottom: 0.65rem;
  line-height: 1.3;
}
.service-text {
  font-size: 0.9rem;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 1.25rem;
}
.service-list {
  list-style: none;
  font-size: 0.8125rem;
  color: var(--text-main);
  margin-top: auto;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
.service-list li::before {
  content: '✓ ';
  color: var(--brand-violet);
  font-weight: 800;
}

/* Regional Hub Filter Tabs */
.hub-tabs-wrap {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}
.hub-tab {
  background: var(--bg-card);
  border: 1.5px solid var(--border-line);
  color: var(--text-muted);
  padding: 0.6rem 1.25rem;
  border-radius: var(--radius-full);
  font-family: var(--font-heading);
  font-size: 0.875rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
}
.hub-tab.active, .hub-tab:hover {
  border-color: var(--brand-violet);
  color: var(--brand-violet);
  background: var(--brand-violet-soft);
}

/* Bento Projects Showcase */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}
.bento-card {
  background: var(--bg-card);
  border: 1px solid var(--border-line);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  transition: transform 0.28s ease, box-shadow 0.28s ease, border-color 0.28s ease;
  position: relative;
}
.bento-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-xl);
  border-color: var(--brand-violet);
}
.bento-card.bento-hero {
  grid-column: span 2;
}
.bento-card[data-hidden-project="true"] {
  display: none;
}
.bento-img-wrap {
  position: relative;
  height: 240px;
  overflow: hidden;
  background: #0b1120;
}
.bento-hero .bento-img-wrap {
  height: 300px;
}
.bento-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.4s ease;
}
.bento-card:hover .bento-img {
  transform: scale(1.06);
}
.bento-badge-group {
  position: absolute;
  top: 1rem;
  left: 1rem;
  display: flex;
  gap: 0.5rem;
  z-index: 2;
}
.bento-pill {
  background: rgba(15, 23, 42, 0.88);
  backdrop-filter: blur(6px);
  color: #ffffff;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.25rem 0.65rem;
  border-radius: var(--radius-sm);
  border: 1px solid rgba(255, 255, 255, 0.2);
}
.bento-pill.pill-amber {
  background: var(--accent-amber);
  border-color: var(--accent-amber);
}
.bento-card-body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.bento-project-title {
  font-family: var(--font-heading);
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--text-main);
  line-height: 1.25;
  margin-bottom: 0.65rem;
}
.bento-meta-bar {
  display: flex;
  gap: 1.25rem;
  flex-wrap: wrap;
  font-family: var(--font-mono);
  font-size: 0.8125rem;
  color: var(--text-muted);
  margin-bottom: 0.85rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--border-line);
}
.bento-meta-item strong {
  color: var(--text-main);
}
.bento-desc {
  font-size: 0.9375rem;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 1.25rem;
  flex-grow: 1;
}
.bento-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--border-line);
  padding-top: 1rem;
  margin-top: auto;
}
.bento-client {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--text-subtle);
}
.btn-view-spec {
  background: none;
  border: 0;
  color: var(--brand-violet);
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.875rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0;
}
.btn-view-spec:hover {
  color: var(--brand-violet-dark);
  text-decoration: underline;
}

/* Lifecycle Strip (Field Plates) */
.lifecycle-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}
.lifecycle-card {
  background: #0b1120;
  border: 1px solid var(--border-line);
  border-radius: var(--radius-lg);
  overflow: hidden;
  position: relative;
  cursor: pointer;
  box-shadow: var(--shadow-sm);
  transition: transform 0.28s ease, box-shadow 0.28s ease, border-color 0.28s ease;
}
.lifecycle-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-xl);
  border-color: var(--brand-violet);
}
.lifecycle-card[data-hidden-gallery="true"] {
  display: none;
}
.lifecycle-img-wrap {
  height: 230px;
  position: relative;
  overflow: hidden;
}
.lifecycle-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.4s ease;
}
.lifecycle-card:hover .lifecycle-img {
  transform: scale(1.08);
}
.lifecycle-phase-tag {
  position: absolute;
  top: 0.85rem;
  left: 0.85rem;
  background: var(--accent-amber);
  color: #ffffff;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 800;
  padding: 0.25rem 0.65rem;
  border-radius: var(--radius-sm);
  z-index: 2;
  box-shadow: 0 2px 8px rgba(0,0,0,0.4);
}
.lifecycle-caption-bar {
  position: absolute;
  inset: auto 0 0 0;
  padding: 2.5rem 1rem 0.85rem;
  background: linear-gradient(to top, rgba(11, 17, 32, 0.95) 0%, rgba(11, 17, 32, 0.7) 60%, transparent 100%);
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 0.5rem;
  z-index: 2;
}
.lifecycle-title {
  color: #ffffff;
  font-family: var(--font-heading);
  font-size: 0.9375rem;
  font-weight: 700;
  line-height: 1.3;
  text-shadow: 0 1px 4px rgba(0,0,0,0.8);
}
.lifecycle-inspect-pill {
  background: rgba(255, 255, 255, 0.18);
  backdrop-filter: blur(8px);
  color: #ffffff;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.25rem 0.65rem;
  border-radius: var(--radius-full);
  border: 1px solid rgba(255, 255, 255, 0.3);
  flex-shrink: 0;
  transition: all 0.2s ease;
}
.lifecycle-card:hover .lifecycle-inspect-pill {
  background: var(--brand-violet);
  border-color: var(--brand-violet);
}

/* Expand / Collapse Button */
.show-all-wrap {
  text-align: center;
  margin-top: 2.5rem;
}
.btn-show-all {
  background: var(--bg-card);
  border: 1.5px solid var(--border-line);
  border-radius: var(--radius-full);
  padding: 0.85rem 2.25rem;
  font-family: var(--font-heading);
  font-size: 0.9375rem;
  font-weight: 700;
  color: var(--text-main);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  box-shadow: var(--shadow-sm);
  transition: all 0.25s ease;
}
.btn-show-all:hover {
  border-color: var(--brand-violet);
  color: var(--brand-violet);
  background: var(--brand-violet-soft);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

/* Credentials Grid */
.credentials-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
}
.credential-badge-card {
  background: var(--bg-card);
  border: 1px solid var(--border-line);
  border-radius: var(--radius-lg);
  padding: 2.25rem 2rem;
  box-shadow: var(--shadow-sm);
  text-align: center;
}
.credential-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}
.credential-title {
  font-family: var(--font-heading);
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--text-main);
  margin-bottom: 0.5rem;
}
.credential-meta {
  font-family: var(--font-mono);
  font-size: 0.8125rem;
  color: var(--accent-amber);
  font-weight: 700;
  margin-bottom: 0.75rem;
}
.credential-desc {
  font-size: 0.9rem;
  color: var(--text-muted);
}

/* Executive Tender Terminal */
.terminal-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2.5rem;
}
.terminal-card {
  background: var(--bg-card);
  border: 1px solid var(--border-line);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  box-shadow: var(--shadow-sm);
}
.terminal-card h3 {
  font-family: var(--font-heading);
  font-size: 1.5rem;
  font-weight: 800;
  margin-bottom: 1.25rem;
  color: var(--text-main);
}
.hq-info-row {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.25rem;
}
.hq-icon {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-md);
  background: var(--brand-violet-soft);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  flex-shrink: 0;
}
.hq-text h4 {
  font-family: var(--font-heading);
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 0.2rem;
  color: var(--text-main);
}
.hq-text p {
  font-size: 0.9375rem;
  color: var(--text-muted);
  line-height: 1.5;
}
.tender-notice {
  font-size: 0.875rem;
  color: var(--brand-violet);
  background: var(--brand-violet-soft);
  padding: 0.75rem 1rem;
  border-radius: var(--radius-md);
  margin-top: 1rem;
  font-weight: 600;
}
.map-frame-wrap {
  height: 220px;
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid var(--border-line);
  margin-top: 1.25rem;
}

/* Form Inputs */
.form-group {
  margin-bottom: 1.25rem;
}
.form-label {
  display: block;
  font-family: var(--font-heading);
  font-size: 0.875rem;
  font-weight: 700;
  margin-bottom: 0.35rem;
}
.form-control {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1.5px solid var(--border-line);
  border-radius: var(--radius-md);
  font-family: var(--font-body);
  font-size: 0.9375rem;
  transition: border-color 0.2s ease;
}
.form-control:focus {
  outline: none;
  border-color: var(--brand-violet);
  box-shadow: 0 0 0 3px var(--brand-violet-soft);
}
.form-row-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}
.form-status-alert {
  padding: 0.75rem 1rem;
  border-radius: var(--radius-md);
  font-size: 0.875rem;
  font-weight: 600;
  margin-top: 1rem;
  display: none;
}
.form-status-alert.success {
  display: block;
  background: #dcfce7;
  color: #166534;
  border: 1px solid #bbf7d0;
}
.form-status-alert.error {
  display: block;
  background: #fee2e2;
  color: #991b1b;
  border: 1px solid #fecaca;
}

/* Architectural Headquarters Desk Footer */
footer#site-footer {
  background: #0b1120;
  color: #94a3b8;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 3.5rem;
  padding-bottom: 2rem;
}

.footer-hq-container {
  display: grid;
  grid-template-columns: 340px 1fr;
  gap: 3rem;
  padding-bottom: 2.75rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  align-items: center;
}

.footer-brand-side {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.footer-logo {
  height: 54px;
  width: auto;
  max-width: 270px;
  object-fit: contain;
  background: #ffffff;
  padding: 6px 14px;
  border-radius: var(--radius-sm);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.45);
  display: inline-block;
}

.footer-reg-pill {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  font-size: 0.8125rem;
  color: #94a3b8;
  line-height: 1.4;
}

.footer-reg-pill .reg-title {
  font-weight: 700;
  color: #e2e8f0;
}

.footer-reg-pill .reg-code {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--accent-amber);
  font-weight: 700;
}

.footer-hq-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-lg);
  padding: 1.75rem 2rem;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}

.footer-hq-title {
  font-family: var(--font-heading);
  font-size: 1.15rem;
  font-weight: 800;
  color: #ffffff;
  margin-bottom: 1.25rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  letter-spacing: -0.2px;
}

.footer-hq-title::before {
  content: '';
  display: inline-block;
  width: 4px;
  height: 18px;
  background: var(--brand-violet);
  border-radius: 2px;
}

.footer-hq-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
}

.footer-hq-item {
  display: flex;
  gap: 0.85rem;
  font-size: 0.875rem;
  line-height: 1.55;
}

.footer-hq-item .fhq-icon {
  font-size: 1.25rem;
  flex-shrink: 0;
  line-height: 1.2;
}

.footer-hq-item strong {
  display: block;
  color: #ffffff;
  font-family: var(--font-heading);
  font-size: 0.875rem;
  margin-bottom: 0.3rem;
}

.footer-hq-item p {
  color: #94a3b8;
  margin: 0;
}

.footer-hq-item a {
  color: #cbd5e1;
  text-decoration: none;
  transition: color 0.2s ease;
}

.footer-hq-item a:hover {
  color: #ffffff;
  text-decoration: underline;
}

.footer-bottom {
  padding-top: 1.75rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #64748b;
  font-size: 0.875rem;
}

.back-to-top-btn {
  color: #cbd5e1;
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.875rem;
  text-decoration: none;
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-sm);
  border: 1px solid rgba(255, 255, 255, 0.15);
  transition: all 0.2s ease;
}

.back-to-top-btn:hover {
  background: var(--brand-violet);
  color: #ffffff;
  border-color: var(--brand-violet);
}

/* Modals */
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
  border-radius: var(--radius-lg);
  max-width: 780px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-xl);
  position: relative;
  padding: 2.25rem;
}
.modal-close-btn {
  position: absolute;
  top: 1.25rem;
  right: 1.25rem;
  background: var(--bg-page);
  border: 1px solid var(--border-line);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  font-size: 1.25rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-main);
  transition: all 0.2s ease;
}
.modal-close-btn:hover {
  background: var(--brand-violet);
  color: #ffffff;
}
.modal-spec-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  margin: 1.5rem 0;
  background: var(--bg-page);
  padding: 1.25rem;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-line);
}
.modal-spec-cell {
  font-size: 0.875rem;
}
.modal-spec-cell strong {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--brand-violet);
  text-transform: uppercase;
}

/* Lightbox */
.lightbox-window {
  max-width: 900px;
  background: transparent;
  border: none;
  box-shadow: none;
  padding: 0;
  text-align: center;
}
.lightbox-img {
  max-width: 100%;
  max-height: 75vh;
  object-fit: contain;
  border-radius: var(--radius-md);
  margin: 0 auto;
  box-shadow: 0 10px 40px rgba(0,0,0,0.6);
}
.lightbox-caption {
  color: #ffffff;
  margin-top: 1rem;
  font-size: 1rem;
  line-height: 1.5;
  background: rgba(11, 17, 32, 0.85);
  padding: 1rem 1.5rem;
  border-radius: var(--radius-md);
  border: 1px solid rgba(255,255,255,0.1);
}

/* Responsive */
@media (max-width: 991px) {
  .hero-layout { grid-template-columns: 1fr; gap: 2.5rem; }
  .about-bento-grid { grid-template-columns: 1fr; }
  .services-grid { grid-template-columns: repeat(2, 1fr); }
  .bento-grid { grid-template-columns: 1fr; }
  .bento-card.bento-hero { grid-column: auto; }
  .lifecycle-grid { grid-template-columns: repeat(2, 1fr); }
  .stat-grid { grid-template-columns: repeat(2, 1fr); }
  .stat-box { border-right: none; border-bottom: 1px solid var(--border-line); }
  .credentials-grid { grid-template-columns: 1fr; }
  .terminal-grid { grid-template-columns: 1fr; }
  .footer-hq-container { grid-template-columns: 1fr; gap: 2rem; }
  .footer-hq-grid { grid-template-columns: 1fr; gap: 1.25rem; }
  .footer-bottom { flex-direction: column; gap: 1rem; text-align: center; }
  .nav-links { display: none; }
  .btn-mobile-toggle { display: block; }
}

@media (max-width: 575px) {
  .services-grid { grid-template-columns: 1fr; }
  .lifecycle-grid { grid-template-columns: 1fr; }
  .stat-grid { grid-template-columns: 1fr; }
  .form-row-2 { grid-template-columns: 1fr; }
  .phone-direct { display: none; }
}
"""



JS = r"""
document.addEventListener('DOMContentLoaded', function() {
  // 1. Mobile Drawer Toggle
  var mobileToggleBtn = document.getElementById('btnMobileToggle');
  var mobileDrawer = document.getElementById('mobileDrawer');
  if (mobileToggleBtn && mobileDrawer) {
    mobileToggleBtn.addEventListener('click', function() {
      var isOpen = mobileDrawer.style.display === 'block';
      mobileDrawer.style.display = isOpen ? 'none' : 'block';
      mobileToggleBtn.setAttribute('aria-expanded', !isOpen);
    });

    document.querySelectorAll('[data-close-drawer]').forEach(function(link) {
      link.addEventListener('click', function() {
        mobileDrawer.style.display = 'none';
        mobileToggleBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // 2. Regional Hub Filter Tabs for Projects
  var hubTabs = document.querySelectorAll('.hub-tab');
  var projectCards = document.querySelectorAll('.bento-card');
  var projectsExpanded = false;
  var currentHub = 'all';

  function applyProjectFilters() {
    projectCards.forEach(function(card, index) {
      var cardHub = card.getAttribute('data-hub');
      var hubMatch = (currentHub === 'all' || cardHub === currentHub);
      
      if (!hubMatch) {
        card.style.display = 'none';
      } else {
        if (!projectsExpanded && index >= 3) {
          card.style.display = 'none';
        } else {
          card.style.display = 'flex';
        }
      }
    });
  }

  hubTabs.forEach(function(tab) {
    tab.addEventListener('click', function() {
      hubTabs.forEach(function(t) { t.classList.remove('active'); });
      tab.classList.add('active');
      currentHub = tab.getAttribute('data-hub');
      applyProjectFilters();
    });
  });

  // 3. Projects Expand / Collapse Toggle (Showing 3 initially)
  var projectsToggleBtn = document.getElementById('projectsToggleBtn');
  if (projectsToggleBtn) {
    projectsToggleBtn.addEventListener('click', function() {
      projectsExpanded = !projectsExpanded;
      if (projectsExpanded) {
        projectsToggleBtn.innerHTML = '<span>Showing All 12 Projects &middot; Show Less</span><span>&uarr;</span>';
      } else {
        projectsToggleBtn.innerHTML = '<span>Showing 3 Flagship Projects &middot; Open Complete Technical Ledger (12 Projects)</span><span>&darr;</span>';
      }
      applyProjectFilters();
    });
  }

  // 4. Gallery Expand / Collapse Toggle (Showing 4 initially)
  var galleryToggleBtn = document.getElementById('galleryToggleBtn');
  var galleryCards = document.querySelectorAll('.lifecycle-card');
  var galleryExpanded = false;

  if (galleryToggleBtn) {
    galleryToggleBtn.addEventListener('click', function() {
      galleryExpanded = !galleryExpanded;
      galleryCards.forEach(function(card, index) {
        if (index >= 4) {
          card.style.display = galleryExpanded ? 'block' : 'none';
        }
      });
      if (galleryExpanded) {
        galleryToggleBtn.innerHTML = '<span>Showing All 12 Lifecycle Plates &middot; Show Less</span><span>&uarr;</span>';
      } else {
        galleryToggleBtn.innerHTML = '<span>Showing 4 Initial Lifecycle Plates &middot; Open Complete Photographic Archive (12 Plates)</span><span>&darr;</span>';
      }
    });
  }

  // 5. Project Technical Specification Modal
  var projectModal = document.getElementById('projectModal');
  var modalCloseBtn = document.getElementById('modalCloseBtn');
  var modalTitle = document.getElementById('modalTitle');
  var modalImg = document.getElementById('modalImg');
  var modalDesc = document.getElementById('modalDesc');
  var modalChainage = document.getElementById('modalChainage');
  var modalStandard = document.getElementById('modalStandard');
  var modalStructures = document.getElementById('modalStructures');
  var modalClient = document.getElementById('modalClient');

  function openProjectModal(projectId) {
    if (!window.AXULAL_PROJECTS) return;
    var proj = window.AXULAL_PROJECTS.find(function(p) { return p.id === projectId; });
    if (!proj) return;

    if (modalTitle) modalTitle.textContent = proj.name + ' (' + proj.id + ')';
    if (modalImg) {
      modalImg.src = proj.img.replace('.jpg', '.webp');
      modalImg.alt = proj.name;
    }
    if (modalDesc) modalDesc.textContent = proj.desc;
    if (modalChainage) modalChainage.textContent = proj.chainage;
    if (modalStandard) modalStandard.textContent = proj.standard + ' · ' + proj.speed;
    if (modalStructures) modalStructures.textContent = proj.structures;
    if (modalClient) modalClient.textContent = proj.client;

    if (projectModal) {
      projectModal.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  document.querySelectorAll('.btn-view-spec').forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      var id = btn.getAttribute('data-project-id');
      openProjectModal(id);
    });
  });

  if (modalCloseBtn && projectModal) {
    modalCloseBtn.addEventListener('click', function() {
      projectModal.classList.remove('open');
      document.body.style.overflow = '';
    });
    projectModal.addEventListener('click', function(e) {
      if (e.target === projectModal) {
        projectModal.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  }

  // 6. Gallery Lightbox Modal
  var galleryModal = document.getElementById('galleryModal');
  var lightboxCloseBtn = document.getElementById('lightboxCloseBtn');
  var lightboxImg = document.getElementById('lightboxImg');
  var lightboxCaption = document.getElementById('lightboxCaption');

  document.querySelectorAll('.lifecycle-card').forEach(function(card) {
    card.addEventListener('click', function() {
      var img = card.querySelector('.lifecycle-img');
      var title = card.querySelector('.lifecycle-title');
      var phase = card.querySelector('.lifecycle-phase-tag');
      var desc = card.getAttribute('data-desc');

      if (lightboxImg && img) {
        lightboxImg.src = img.src;
        lightboxImg.alt = img.alt;
      }
      if (lightboxCaption && title) {
        var phaseText = phase ? phase.textContent : '';
        lightboxCaption.innerHTML = '<strong>' + (phaseText ? phaseText + ' &middot; ' : '') + title.textContent + '</strong><br>' + (desc || '');
      }
      if (galleryModal) {
        galleryModal.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  if (lightboxCloseBtn && galleryModal) {
    lightboxCloseBtn.addEventListener('click', function() {
      galleryModal.classList.remove('open');
      document.body.style.overflow = '';
    });
    galleryModal.addEventListener('click', function(e) {
      if (e.target === galleryModal) {
        galleryModal.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  }

  // Global ESC Key closes open modals
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      if (projectModal && projectModal.classList.contains('open')) {
        projectModal.classList.remove('open');
        document.body.style.overflow = '';
      }
      if (galleryModal && galleryModal.classList.contains('open')) {
        galleryModal.classList.remove('open');
        document.body.style.overflow = '';
      }
    }
  });

  // 7. Free FormSubmit.co AJAX Endpoint Integration
  var rfpForm = document.getElementById('rfpForm');
  var formAlert = document.getElementById('formStatusAlert');
  var submitBtn = document.getElementById('rfpSubmitBtn');

  if (rfpForm) {
    rfpForm.addEventListener('submit', function(e) {
      e.preventDefault();
      if (!submitBtn) return;

      var originalBtnHtml = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<span>Submitting RFP Inquiry...</span>';
      if (formAlert) {
        formAlert.className = 'form-status-alert';
        formAlert.style.display = 'none';
      }

      var formData = new FormData(rfpForm);

      fetch('https://formsubmit.co/ajax/tenders@axulalengineers.com', {
        method: 'POST',
        headers: {
          'Accept': 'application/json'
        },
        body: formData
      })
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnHtml;
        if (formAlert) {
          formAlert.textContent = '✓ Thank you! Your RFP inquiry has been transmitted to our engineering desk. A Principal Engineer will reply within 24–48 hours.';
          formAlert.className = 'form-status-alert success';
        }
        rfpForm.reset();
      })
      .catch(function(error) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnHtml;
        if (formAlert) {
          formAlert.textContent = '⚠ Network submission issue. Please email your RFP directly to tenders@axulalengineers.com or call +251 111 582107.';
          formAlert.className = 'form-status-alert error';
        }
      });
    });
  }
});
"""



HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Axulal Consulting Engineers PLC | Category-1 Highway &amp; Bridge Engineering Consultants</title>
  <meta name="description" content="Axulal Consulting Engineers PLC — Category-1 Highway and Bridge consulting engineers in Addis Ababa, Ethiopia (FDRE Reg #01/ORA/2011). Over 145 km of delivered arterial infrastructure since 2011.">
  <meta name="theme-color" content="#0b1120">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="assets/css/site.css?v=__V__">
  <link rel="icon" type="image/png" href="assets/logo.png?v=__V__">
</head>
<body>
  <a href="#projects" class="skip-link">Skip to Projects</a>

  <!-- Header -->
  <header class="site-header">
    <div class="container header-wrap">
      <a href="#home">
        <picture>
          <source type="image/webp" srcset="assets/logo.webp?v=__V__">
          <img src="assets/logo.png?v=__V__" alt="Axulal Consulting Engineers PLC Logo" class="brand-logo-img" width="1014" height="313">
        </picture>
      </a>

      <!-- Desktop Nav -->
      <nav aria-label="Main Navigation">
        <ul class="nav-links">
          <li><a href="#about">About</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#gallery">Gallery</a></li>
          <li><a href="#credentials">Credentials</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>

      <div class="header-cta-group">
        <a href="tel:+251111582107" class="phone-direct">
          <span>📞</span> +251 111 582107
        </a>
        <a href="#contact" class="btn-primary">
          <span>Request RFP</span>
          <span>&rarr;</span>
        </a>
        <button class="btn-mobile-toggle" id="btnMobileToggle" aria-label="Toggle Navigation" aria-expanded="false">
          ☰
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer Menu -->
  <div id="mobileDrawer">
    <ul>
      <li><a href="#about" data-close-drawer>About</a></li>
      <li><a href="#services" data-close-drawer>Services</a></li>
      <li><a href="#projects" data-close-drawer>Projects</a></li>
      <li><a href="#gallery" data-close-drawer>Gallery</a></li>
      <li><a href="#credentials" data-close-drawer>Credentials</a></li>
      <li><a href="#contact" data-close-drawer>Contact</a></li>
    </ul>
    <div style="margin-top:2rem; padding-top:1.5rem; border-top:1px solid var(--border-line);">
      <a href="#contact" class="btn-primary" style="width:100%; justify-content:center;" data-close-drawer>Submit RFP Inquiry &rarr;</a>
    </div>
  </div>

  <main>
    <!-- Hero Section -->
    <section class="hero-viewport" id="home">
      <div class="hero-grid-overlay"></div>
      <div class="container hero-layout">
        
        <!-- Left Hero Column -->
        <div>
          <div class="hero-badge-pill">
            <span>🏛️</span>
            <span>CATEGORY-1 HIGHWAY &amp; BRIDGE CONSULTANTS</span>
          </div>
          <h1 class="hero-title">
            Engineering Ethiopia’s <br>
            <span class="highlight">Arterial Highways &amp; Critical Bridges</span>
          </h1>
          <p class="hero-desc">
            Delivering precision engineering design, hydrological modeling, and resident construction supervision across over 145 km of classified transport infrastructure since 2011.
          </p>
          <div class="hero-btn-row">
            <a href="#projects" class="btn-primary">
              <span>Explore Corridors</span>
              <span>&darr;</span>
            </a>
            <a href="#credentials" class="btn-secondary-glass">
              <span>📄 Capability Profile</span>
            </a>
          </div>
        </div>

        <!-- Right Telemetry Glass Card (Featured Project HUD) -->
        <div>
          <div class="telemetry-card">
            <div class="telemetry-header">
              <span class="telemetry-tag">FEATURED INFRASTRUCTURE · AWASH BRIDGE</span>
              <span class="telemetry-live-dot">VERIFIED SPEC</span>
            </div>

            <div class="telemetry-img-wrap">
              <picture>
                <source type="image/webp" srcset="assets/projects/proj_6_awash_bridge.webp?v=__V__">
                <img src="assets/projects/proj_6_awash_bridge.jpg?v=__V__" alt="Awash River Girder Bridge" class="telemetry-img" width="1280" height="720">
              </picture>
            </div>

            <h3 class="telemetry-title">Awash River Girder Bridge (P-06)</h3>
            <p style="font-size:0.875rem; color:#94a3b8;">
              Single-span reinforced concrete deck girder bridge engineered with deep abutment footings and hydraulic scour defense.
            </p>

            <div class="telemetry-spec-grid">
              <div class="spec-item">
                <span class="spec-label">Span Length</span>
                <span class="spec-value">24.0 m Clear Span</span>
              </div>
              <div class="spec-item">
                <span class="spec-label">Design Loading</span>
                <span class="spec-value">AASHTO HS20-44</span>
              </div>
              <div class="spec-item">
                <span class="spec-label">Authority Client</span>
                <span class="spec-value">ORA (Oromiya)</span>
              </div>
              <div class="spec-item">
                <span class="spec-label">Station Extent</span>
                <span class="spec-value">STA 4+250 Crossing</span>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- Live Telemetry Marquee Ticker -->
      <div class="marquee-bar">
        <div class="marquee-track">
          <span class="marquee-item">145.3 KM DELIVERED ALL-WEATHER HIGHWAYS</span>
          <span class="marquee-item">46.0 M REINFORCED CONCRETE RIVER BRIDGES</span>
          <span class="marquee-item">STA 0+000 – STA 27+000 EJERE-ARERTU CORRIDOR</span>
          <span class="marquee-item">100+ CROSS-DRAINAGE HYDRAULIC BOX &amp; PIPE CULVERTS</span>
          <span class="marquee-item">CATEGORY-1 FDRE REG #01/ORA/2011 ACCREDITATION</span>
          <span class="marquee-item">98% MODIFIED AASHTO SUB-BASE COMPACTION QC</span>
          <span class="marquee-item">145.3 KM DELIVERED ALL-WEATHER HIGHWAYS</span>
          <span class="marquee-item">46.0 M REINFORCED CONCRETE RIVER BRIDGES</span>
          <span class="marquee-item">STA 0+000 – STA 27+000 EJERE-ARERTU CORRIDOR</span>
          <span class="marquee-item">100+ CROSS-DRAINAGE HYDRAULIC BOX &amp; PIPE CULVERTS</span>
          <span class="marquee-item">CATEGORY-1 FDRE REG #01/ORA/2011 ACCREDITATION</span>
          <span class="marquee-item">98% MODIFIED AASHTO SUB-BASE COMPACTION QC</span>
        </div>
      </div>
    </section>

    <!-- 4-Stat Metric Proof Band -->
    <section class="stat-band">
      <div class="container">
        <div class="stat-grid">
          <div class="stat-box">
            <div class="stat-number">145.3 <span class="stat-unit">km</span></div>
            <div class="stat-label">Classified Highway Delivered</div>
            <div class="stat-sub">Highland, mountainous &amp; rolling alignments</div>
          </div>
          <div class="stat-box">
            <div class="stat-number">46.0 <span class="stat-unit">m</span></div>
            <div class="stat-label">RC River Bridge Spans</div>
            <div class="stat-sub">Awash (24m) &amp; Berga (22m) Crossings</div>
          </div>
          <div class="stat-box">
            <div class="stat-number">100<span class="stat-unit">+</span></div>
            <div class="stat-label">Hydraulic Drainage Units</div>
            <div class="stat-sub">Box culverts, stone aprons &amp; retaining walls</div>
          </div>
          <div class="stat-box">
            <div class="stat-number">Cat-1</div>
            <div class="stat-label">Highest Statutory License</div>
            <div class="stat-sub">Ministry of Urban Development &amp; ERA</div>
          </div>
        </div>
      </div>
    </section>

    <!-- About Axulal Section -->
    <section class="section-wrap" id="about">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">ABOUT AXULAL</span>
          <h2 class="section-title">Institutional Engineering Excellence</h2>
          <p class="section-desc">
            Established in 2011 in Addis Ababa, Axulal Consulting Engineers PLC has earned a distinguished reputation as a premier Category-1 consultancy for critical road, highway, and bridge infrastructure.
          </p>
        </div>

        <div class="about-bento-grid">
          <div class="about-bento-card">
            <span class="about-card-icon">🏛️</span>
            <h3 class="about-card-title">15 Years of National Impact</h3>
            <p class="about-card-text">
              Fully licensed as a Category-1 Highway and Bridge Consultant under FDRE Registration #01/ORA/2011. Partnering with the Oromiya Road Authority (ORA) and national transport authorities since 2011 with zero contractual defaults.
            </p>
            <div class="about-card-highlight">FDRE Reg #01/ORA/2011 · MoWUD &amp; ERA Accredited</div>
          </div>

          <div class="about-bento-card">
            <span class="about-card-icon">📐</span>
            <h3 class="about-card-title">Technical Directorate</h3>
            <p class="about-card-text">
              Led by senior highway and structural engineers with decades of specialized field expertise in complex Ethiopian topography, volcanic soils, high-discharge hydrological basins, and modern CAD geometric design.
            </p>
            <div class="about-card-highlight">Multi-Discipline Highway &amp; Bridge Specialists</div>
          </div>

          <div class="about-bento-card">
            <span class="about-card-icon">🔬</span>
            <h3 class="about-card-title">Rigorous Quality Assurance</h3>
            <p class="about-card-text">
              Strict compliance with AASHTO, ERA, and Ethiopian building codes. Dedicated field testing protocols including 98% Modified AASHTO compaction control, concrete cube compressive testing, and rebar tensile validation.
            </p>
            <div class="about-card-highlight">100% Quality Acceptance on Delivered Arteries</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Disciplines & Services -->
    <section class="section-wrap alt" id="services">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">CORE DISCIPLINES</span>
          <h2 class="section-title">Comprehensive Engineering Services</h2>
          <p class="section-desc">
            From initial terrain reconnaissance and hydrological modeling to detailed CAD blueprinting and resident site supervision.
          </p>
        </div>

        <div class="services-grid">
          <div class="service-card">
            <div class="service-icon-box">🛣️</div>
            <h3 class="service-title">Highway &amp; Route Design</h3>
            <p class="service-text">
              Comprehensive geometric alignment, earthwork balancing, terrain profile modeling, and pavement structure design across DC-1 to DC-4 classifications.
            </p>
            <ul class="service-list">
              <li>Geometric CAD Alignments</li>
              <li>Cut/Fill Mass Haul Optimization</li>
              <li>Pavement Thickness Design</li>
            </ul>
          </div>

          <div class="service-card">
            <div class="service-icon-box">🌉</div>
            <h3 class="service-title">Bridge &amp; Structural Engineering</h3>
            <p class="service-text">
              Detailed structural engineering for reinforced concrete girder bridges, pier columns, deep foundation footings, and AASHTO HS20-44 live load calculations.
            </p>
            <ul class="service-list">
              <li>Single &amp; Multi-Span RC Girders</li>
              <li>Abutment Scour Defense</li>
              <li>Substructure Foundation Analysis</li>
            </ul>
          </div>

          <div class="service-card">
            <div class="service-icon-box">💧</div>
            <h3 class="service-title">Hydrology &amp; Drainage</h3>
            <p class="service-text">
              Catchment basin modeling, runoff hydrographs, and hydraulic dimensioning for multi-barrel RC box culverts, slab culverts, and stone masonry ditch linings.
            </p>
            <ul class="service-list">
              <li>50-Year Flood Hydrographs</li>
              <li>Multi-Barrel Box Culverts</li>
              <li>Erosion Protection Aprons</li>
            </ul>
          </div>

          <div class="service-card">
            <div class="service-icon-box">📋</div>
            <h3 class="service-title">Resident Site Supervision</h3>
            <p class="service-text">
              Full-time resident engineers providing on-site quality control, laboratory testing verification, contractor compliance audits, and contract administration.
            </p>
            <ul class="service-list">
              <li>Daily Materials QA/QC Testing</li>
              <li>Interim Payment Certificates (IPC)</li>
              <li>Final Milestone Handover Audits</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Flagship Bento Projects Showcase -->
    <section class="section-wrap" id="projects">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">ENGINEERING PORTFOLIO</span>
          <h2 class="section-title">Regional Infrastructure Showcase</h2>
          <p class="section-desc">
            Structured bento showcase highlighting high-capacity highway alignments and reinforced concrete river crossings delivered for the Oromiya Road Authority.
          </p>
        </div>

        <!-- Regional Hub Filter Tabs -->
        <div class="hub-tabs-wrap">
          <button class="hub-tab active" data-hub="all">All Corridors (12)</button>
          <button class="hub-tab" data-hub="ginchi">Ginchi Corridor (15.5km)</button>
          <button class="hub-tab" data-hub="awash">Awash River Basin (35km)</button>
          <button class="hub-tab" data-hub="ejere">Ejere Regional Sector (56.5km)</button>
          <button class="hub-tab" data-hub="berga">Berga River Crossing (22m)</button>
        </div>

        <!-- Bento Grid -->
        <div class="bento-grid" id="projectsGrid">
          __PROJECT_CARDS__
        </div>

        <!-- Expansion Trigger -->
        <div class="show-all-wrap">
          <button id="projectsToggleBtn" class="btn-show-all">
            <span>Showing 3 Flagship Projects &middot; Open Complete Technical Ledger (12 Projects)</span>
            <span>&darr;</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Construction Supervision Lifecycle (Field Plates) -->
    <section class="section-wrap alt" id="gallery">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">RESIDENT SUPERVISION EVIDENCE</span>
          <h2 class="section-title">Construction Lifecycle Documentation</h2>
          <p class="section-desc">
            Chronological photographic evidence of engineering supervision: from mechanical rock ripping and compaction QC to final camber handover.
          </p>
        </div>

        <div class="lifecycle-grid" id="galleryGrid">
          __GALLERY_CARDS__
        </div>

        <div class="show-all-wrap">
          <button id="galleryToggleBtn" class="btn-show-all">
            <span>Showing 4 Initial Lifecycle Plates &middot; Open Complete Photographic Archive (12 Plates)</span>
            <span>&darr;</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Credentials & Accreditation Section -->
    <section class="section-wrap" id="credentials">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">ACCREDITATION &amp; QA</span>
          <h2 class="section-title">Statutory Licensure &amp; Standards</h2>
          <p class="section-desc">
            Formally certified and licensed to execute high-stakes federal, regional, and municipal infrastructure assignments across the Federal Democratic Republic of Ethiopia.
          </p>
        </div>

        <div class="credentials-grid">
          <div class="credential-badge-card">
            <div class="credential-icon">📜</div>
            <h3 class="credential-title">Category-1 Licensure</h3>
            <div class="credential-meta">FDRE REG #01/ORA/2011</div>
            <p class="credential-desc">
              Highest statutory consulting license for highway, structural, and hydraulic infrastructure, legally authorizing unlimited contract value and technical jurisdiction.
            </p>
          </div>

          <div class="credential-badge-card">
            <div class="credential-icon">🏛️</div>
            <h3 class="credential-title">Ministry Accredited</h3>
            <div class="credential-meta">MoWUD &amp; ERA COMPLIANT</div>
            <p class="credential-desc">
              Officially registered with the Ministry of Urban Development and Ethiopian Roads Authority, maintaining strict compliance with national engineering codes.
            </p>
          </div>

          <div class="credential-badge-card">
            <div class="credential-icon">🏆</div>
            <h3 class="credential-title">Flawless Delivery Record</h3>
            <div class="credential-meta">15 YEARS · 100% TIMELY COMPLETION</div>
            <p class="credential-desc">
              Over 145.3 km of classified roads and 46.0 m of RC bridges delivered with zero contractual defaults, zero liquidated damages, and 100% client satisfaction.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Procurement & Tender Intake Terminal (NO Redundancy with Headquarters Desk) -->
    <section class="section-wrap alt" id="contact">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">PROCUREMENT &amp; TENDER INTAKE</span>
          <h2 class="section-title">Initiate a Project Partnership</h2>
          <p class="section-desc">
            Connect directly with our engineering directorate to submit an RFP, discuss an upcoming road/bridge tender, or schedule a technical advisory consultation.
          </p>
        </div>

        <div class="terminal-grid">
          
          <!-- Left Tender Submission & Advisory Intake Card -->
          <div class="terminal-card">
            <h3>Tender Submission Desk &amp; Advisory Intake</h3>
            
            <div class="hq-info-row">
              <div class="hq-icon">📋</div>
              <div class="hq-text">
                <h4>Direct Procurement Routing</h4>
                <p>All RFP submissions, project specifications, and tender terms of reference (TOR) are reviewed directly by our Principal Highway and Bridge Engineers within 24–48 business hours.</p>
              </div>
            </div>

            <div class="hq-info-row">
              <div class="hq-icon">📞</div>
              <div class="hq-text">
                <h4>Procurement Hotlines &amp; Direct Mail</h4>
                <p>Tender Submissions: <a href="mailto:tenders@axulalengineers.com"><strong>tenders@axulalengineers.com</strong></a><br>
                Technical Director Direct: <a href="tel:+251930077347"><strong>+251 93 007 7347</strong></a><br>
                Office Landline: <a href="tel:+251111582107">+251 111 582107</a> &middot; FAX: +251 111 262888</p>
              </div>
            </div>

            <!-- Interactive Google Map Frame -->
            <div class="map-frame-wrap">
              <iframe 
                src="https://maps.google.com/maps?q=Katekse+Building,+Adwa+Square,+Addis+Ababa,+Ethiopia&amp;hl=en&amp;z=16&amp;output=embed" 
                width="100%" 
                height="100%" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade"
                title="Axulal Head Office Google Map Location - Adwa Square, Katekse Building, Third floor">
              </iframe>
            </div>

            <p class="tender-notice">
              📍 Official corporate registration, postal address, and physical office details are located in the Headquarters Desk below.
            </p>
          </div>

          <!-- Right RFP Consultation Terminal -->
          <div class="terminal-card">
            <h3>Request an RFP Consultation</h3>
            <p style="font-size:0.9375rem; color:var(--text-muted); margin-bottom:1.5rem;">
              Submit your corridor requirements and milestones. Our senior highway and bridge engineering directors reply within one working day.
            </p>

            <form id="rfpForm">
              <input type="hidden" name="_subject" value="New Engineering RFP Submission - Axulal Web Portal">
              <input type="hidden" name="_captcha" value="false">

              <div class="form-row-2 form-group">
                <div>
                  <label class="form-label" for="rfpName">Full Name *</label>
                  <input type="text" id="rfpName" name="name" class="form-control" placeholder="Ato / W/ro / Eng." required>
                </div>
                <div>
                  <label class="form-label" for="rfpOrg">Organization / Authority *</label>
                  <input type="text" id="rfpOrg" name="organization" class="form-control" placeholder="e.g. ORA, ERA, Municipality" required>
                </div>
              </div>

              <div class="form-row-2 form-group">
                <div>
                  <label class="form-label" for="rfpEmail">Email Address *</label>
                  <input type="email" id="rfpEmail" name="email" class="form-control" placeholder="name@domain.gov.et" required>
                </div>
                <div>
                  <label class="form-label" for="rfpPhone">Phone Number *</label>
                  <input type="tel" id="rfpPhone" name="phone" class="form-control" placeholder="+251 9..." required>
                </div>
              </div>

              <div class="form-group">
                <label class="form-label" for="rfpDiscipline">Project Discipline</label>
                <select id="rfpDiscipline" name="discipline" class="form-control">
                  <option value="Highways &amp; Rural Road Corridor (DC-1 to DC-4)">Highways &amp; Rural Road Corridor (DC-1 to DC-4)</option>
                  <option value="Reinforced Concrete Girder River Bridge">Reinforced Concrete Girder River Bridge</option>
                  <option value="Hydraulic Catchment &amp; Culvert System">Hydraulic Catchment &amp; Culvert System</option>
                  <option value="Resident Construction Supervision &amp; Contract Administration">Resident Construction Supervision &amp; Contract Administration</option>
                </select>
              </div>

              <div class="form-group">
                <label class="form-label" for="rfpScope">Scope Description &amp; Location *</label>
                <textarea id="rfpScope" name="scope" class="form-control" rows="4" placeholder="Specify approximate route chainage, geographic region, terrain, and required design milestones..." required></textarea>
              </div>

              <button type="submit" id="rfpSubmitBtn" class="btn-primary" style="width:100%; justify-content:center; padding:0.85rem;">
                <span>Submit Inquiry to Engineering Desk &rarr;</span>
              </button>

              <div id="formStatusAlert" class="form-status-alert"></div>
            </form>
          </div>

        </div>
      </div>
    </section>
  </main>

  <!-- Architectural Headquarters Desk Footer -->
  <footer id="site-footer">
    <div class="container">
      <div class="footer-hq-container">
        <!-- Brand Block: Vivid colorful Logo on high-contrast crisp white badge (no white-out) -->
        <div class="footer-brand-side">
          <picture>
            <source type="image/webp" srcset="assets/logo.webp?v=__V__">
            <img src="assets/logo.png?v=__V__" alt="Axulal Consulting Engineers PLC Logo" class="footer-logo" width="1014" height="313">
          </picture>
          <div class="footer-reg-pill">
            <span class="reg-title">Category-1 Highway &amp; Bridge Consultants</span>
            <span class="reg-code">FDRE Reg #01/ORA/2011 · Ministry of Urban Development</span>
          </div>
        </div>

        <!-- Headquarters Desk (Sole Focus of Footer) -->
        <div class="footer-hq-card">
          <h4 class="footer-hq-title">Headquarters Desk</h4>
          <div class="footer-hq-grid">
            <div class="footer-hq-item">
              <span class="fhq-icon" aria-hidden="true">📍</span>
              <div>
                <strong>Location</strong>
                <p>Adwa Square, Katekse Building, Third floor<br>
                House No: 712/A · Woreda: 07, Sub-city: Yeka<br>
                Addis Ababa, Ethiopia</p>
              </div>
            </div>

            <div class="footer-hq-item">
              <span class="fhq-icon" aria-hidden="true">📞</span>
              <div>
                <strong>Telephone &amp; FAX</strong>
                <p>Tel: <a href="tel:+251111582107"><strong>+251 111 582107</strong></a><br>
                Mob: <a href="tel:+251930077347">+251 93 007 7347</a><br>
                FAX: +251 111 262888</p>
              </div>
            </div>

            <div class="footer-hq-item">
              <span class="fhq-icon" aria-hidden="true">📮</span>
              <div>
                <strong>Postal &amp; Direct Mail</strong>
                <p>P.O. Box: <strong>26061/1000</strong>, Addis Ababa<br>
                Tender Desk: <a href="mailto:tenders@axulalengineers.com">tenders@axulalengineers.com</a><br>
                Direct: <a href="mailto:info@axulalengineers.com">info@axulalengineers.com</a></p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer Bottom -->
      <div class="footer-bottom">
        <div>
          © 2011 – 2026 <strong>Axulal Consulting Engineers PLC (አክሱላል ኮንሰልቲንግ ኢንጂነርስ ኃላ/የተ/የግ/ማህበር)</strong>. All rights reserved.
        </div>
        <div>
          <a href="#home" class="back-to-top-btn">Back to Top ↑</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Project Technical Specification Modal -->
  <div class="modal-backdrop" id="projectModal" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
    <div class="modal-window">
      <button class="modal-close-btn" id="modalCloseBtn" aria-label="Close Project Modal">&times;</button>
      <h3 id="modalTitle" style="font-family:var(--font-heading); font-size:1.5rem; margin-bottom:1rem; color:var(--text-main);">Project Blueprint Specifications</h3>
      
      <div style="border-radius:var(--radius-md); overflow:hidden; max-height:300px; margin-bottom:1.25rem; background:#0b1120;">
        <img id="modalImg" src="" alt="Project Blueprint" style="width:100%; height:100%; object-fit:cover;">
      </div>

      <p id="modalDesc" style="color:var(--text-muted); font-size:0.95rem; line-height:1.6; margin-bottom:1rem;"></p>

      <div class="modal-spec-grid">
        <div class="modal-spec-cell">
          <strong>Route Chainage</strong>
          <span id="modalChainage">STA 0+000</span>
        </div>
        <div class="modal-spec-cell">
          <strong>Road Standard</strong>
          <span id="modalStandard">DC-2</span>
        </div>
        <div class="modal-spec-cell">
          <strong>Hydraulic Structures</strong>
          <span id="modalStructures">Drainage Culverts</span>
        </div>
        <div class="modal-spec-cell">
          <strong>Client Authority</strong>
          <span id="modalClient">ORA</span>
        </div>
      </div>

      <div style="text-align:right; margin-top:1.5rem;">
        <a href="#contact" class="btn-primary" onclick="document.getElementById('projectModal').classList.remove('open'); document.body.style.overflow='';" style="padding:0.6rem 1.25rem;">
          Inquire About This Corridor &rarr;
        </a>
      </div>
    </div>
  </div>

  <!-- Gallery Lightbox Modal -->
  <div class="modal-backdrop" id="galleryModal" role="dialog" aria-modal="true" aria-label="Photo Lightbox">
    <div class="modal-window lightbox-window">
      <button class="modal-close-btn" id="lightboxCloseBtn" aria-label="Close Lightbox" style="top:-15px; right:-15px; background:#ffffff;">&times;</button>
      <img id="lightboxImg" class="lightbox-img" src="" alt="Field Plate Preview">
      <div id="lightboxCaption" class="lightbox-caption"></div>
    </div>
  </div>

  <script src="assets/js/data.js?v=__V__"></script>
  <script src="assets/js/site.js?v=__V__"></script>
</body>
</html>
"""



def _webp_variant(src):
    p = Path(src)
    return str(p.with_suffix(".webp")).replace("\\", "/")

def ensure_webp(quality=WEBP_QUALITY):
    generated = 0
    up_to_date = 0
    failed = 0

    sources = []
    if PROJECTS_DIR.exists():
        sources.extend(PROJECTS_DIR.glob("*.jpg"))
        sources.extend(PROJECTS_DIR.glob("*.png"))
    if GALLERY_DIR.exists():
        sources.extend(GALLERY_DIR.glob("*.jpg"))
        sources.extend(GALLERY_DIR.glob("*.png"))
    logo_file = ASSETS_DIR / "logo.png"
    if logo_file.exists():
        sources.append(logo_file)

    for src in sources:
        dst = src.with_suffix(".webp")
        if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
            up_to_date += 1
            continue
        try:
            with Image.open(src) as im:
                im.save(dst, "WEBP", quality=quality, method=6)
            generated += 1
        except Exception as e:
            print(f"  warn: failed webp for {src}: {e}")
            failed += 1

    print(f"  webp: {generated} generated, {up_to_date} up to date, {failed} failed")

def render_project_cards(projects):
    cards = []
    for idx, p in enumerate(projects):
        is_hero = (idx == 0)
        is_hidden = (idx >= 3)
        hero_class = "bento-hero" if is_hero else ""
        hidden_attr = 'data-hidden-project="true"' if is_hidden else ''
        
        webp_src = _webp_variant(p["img"])
        png_src = p["img"].replace("\\", "/")

        card_html = f"""        <article class="bento-card {hero_class}" data-hub="{p['hub']}" {hidden_attr}>
          <div class="bento-img-wrap">
            <picture>
              <source type="image/webp" srcset="{webp_src}?v=__V__">
              <img src="{png_src}?v=__V__" alt="{p['name']}" class="bento-img" loading="lazy" width="800" height="500">
            </picture>
            <div class="bento-badge-group">
              <span class="bento-pill pill-amber">{p['badge']}</span>
              <span class="bento-pill">{p['pill']}</span>
            </div>
          </div>
          <div class="bento-card-body">
            <h3 class="bento-project-title">{p['name']} ({p['id']})</h3>
            <div class="bento-meta-bar">
              <div class="bento-meta-item">Chainage: <strong>{p['chainage']}</strong></div>
              <div class="bento-meta-item">Standard: <strong>{p['standard']}</strong></div>
              <div class="bento-meta-item">Structures: <strong>{p['structures']}</strong></div>
            </div>
            <p class="bento-desc">
              {p['desc']}
            </p>
            <div class="bento-card-footer">
              <span class="bento-client">Client: {p['client']}</span>
              <button class="btn-view-spec" data-project-id="{p['id']}">View Blueprint &amp; Specs &rarr;</button>
            </div>
          </div>
        </article>"""
        cards.append(card_html)
    return "\n".join(cards)

def render_gallery_cards(gallery):
    cards = []
    for idx, g in enumerate(gallery):
        is_hidden = (idx >= 4)
        hidden_attr = 'data-hidden-gallery="true"' if is_hidden else ''
        webp_src = _webp_variant(g["img"])
        png_src = g["img"].replace("\\", "/")

        card_html = f"""        <figure class="lifecycle-card" data-desc="{g['desc']}" {hidden_attr}>
          <div class="lifecycle-img-wrap">
            <picture>
              <source type="image/webp" srcset="{webp_src}?v=__V__">
              <img src="{png_src}?v=__V__" alt="{g['title']}" class="lifecycle-img" loading="lazy" width="600" height="400">
            </picture>
            <span class="lifecycle-phase-tag">{g['phase']}</span>
            <div class="lifecycle-caption-bar">
              <span class="lifecycle-title">{g['title']}</span>
              <span class="lifecycle-inspect-pill">🔍 Inspect</span>
            </div>
          </div>
        </figure>"""
        cards.append(card_html)
    return "\n".join(cards)

def build():
    print("Building Axulal Consulting Engineers PLC website...")
    ensure_webp()

    # 1. Render components
    project_cards_html = render_project_cards(PROJECTS_DATA)
    gallery_cards_html = render_gallery_cards(GALLERY_DATA)

    # 2. Render HTML
    html = HTML_TEMPLATE
    html = html.replace("__PROJECT_CARDS__", project_cards_html)
    html = html.replace("__GALLERY_CARDS__", gallery_cards_html)
    html = html.replace("__V__", ASSET_VERSION)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print("  wrote index.html")

    # 3. Write CSS
    CSS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CSS_FILE, "w", encoding="utf-8") as f:
        f.write(CSS.strip())
    print("  wrote assets/css/site.css")

    # 4. Write JS
    JS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(JS_FILE, "w", encoding="utf-8") as f:
        f.write(JS.strip())
    print("  wrote assets/js/site.js")

    # 5. Write Data JS
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    data_content = f"window.AXULAL_PROJECTS = {json.dumps(PROJECTS_DATA, indent=2)};\n"
    data_content += f"window.AXULAL_GALLERY = {json.dumps(GALLERY_DATA, indent=2)};\n"
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(data_content)
    print("  wrote assets/js/data.js")

    print(f"Master build complete! Version: {ASSET_VERSION}")

if __name__ == "__main__":
    build()
