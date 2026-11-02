#!/usr/bin/env python3
"""
Master Build Script for Axulal Consulting Engineers PLC
Generates index.html, assets/css/site.css, assets/js/site.js, assets/js/data.js,
robots.txt, and sitemap.xml.

Incorporates all fixes from Axulal Website Review.md:
- Mathematically verified sums: 145.8 km of road corridors, 46.0 m bridges
- Accurate hub lengths: Ginchi 25.5 km, Awash 25.0 km + 24m, Ejere 85.7 km, Berga 9.6 km + 22m
- Robust hub filtering: filters matching cards first, then applies limit, adjusts toggle button
- Verified form submission: checks response.ok and data.success, adds honeypot anti-spam
- Professional engineering language: replaced app jargon with engineering terminology
- Defensible legal claims: Category-1 FDRE Reg #01/ORA/2011, MoUDI/MoWUD & ERA accreditation
- Accessible horizontal header logo: clear text and emblem
- Compact mobile header CTA
- Accessibility: skip link to #main-content, aria-hidden on emojis, focus-visible outline, modal focus trap & hamburger close toggle
- SEO: Canonical, Open Graph, Twitter Cards, JSON-LD Organization schema, robots.txt, sitemap.xml
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
ROBOTS_FILE = BASE_DIR / "robots.txt"
SITEMAP_FILE = BASE_DIR / "sitemap.xml"

ASSET_VERSION = "23"
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

/* High-contrast focus rings for accessibility */
:focus-visible {
  outline: 2px solid var(--brand-violet);
  outline-offset: 2px;
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
  top: -60px;
  left: 1rem;
  background: var(--brand-violet);
  color: #ffffff;
  padding: 0.65rem 1.25rem;
  z-index: 1000;
  border-radius: var(--radius-sm);
  font-weight: 700;
  font-size: 0.875rem;
  transition: top 0.2s ease;
  box-shadow: var(--shadow-lg);
}
.skip-link:focus {
  top: 1rem;
}

/* Glass Header */
.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.95);
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
  max-width: 250px;
  object-fit: contain;
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

.btn-cta-short {
  display: none;
}

/* Mobile Toggle */
.btn-mobile-toggle {
  display: none;
  background: transparent;
  border: 1.5px solid var(--border-line);
  border-radius: var(--radius-sm);
  padding: 0.45rem 0.65rem;
  font-size: 1.35rem;
  line-height: 1;
  cursor: pointer;
  color: var(--text-main);
  transition: all 0.2s ease;
}
.btn-mobile-toggle:hover {
  border-color: var(--brand-violet);
  color: var(--brand-violet);
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

/* Hero Section */
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

/* Featured Civil Works Specification Card */
.telemetry-card {
  background: rgba(15, 23, 42, 0.82);
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

/* Infrastructure Highlights Marquee */
.marquee-bar {
  margin-top: 3.5rem;
  background: rgba(11, 17, 32, 0.92);
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
  background: #ffffff;
  border: 1.5px solid var(--border-line);
  color: var(--text-muted);
  padding: 0.55rem 1.15rem;
  border-radius: var(--radius-full);
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.hub-tab.active, .hub-tab:hover {
  border-color: var(--brand-violet);
  color: var(--brand-violet);
  background: var(--brand-violet-soft);
}
.hub-tab.active {
  background: var(--brand-violet);
  color: #ffffff;
  border-color: var(--brand-violet);
  box-shadow: 0 4px 14px var(--brand-violet-glow);
}

/* Bento Projects Showcase */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
}
.bento-card {
  background: var(--bg-card);
  border: 1px solid var(--border-line);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
  display: flex;
  flex-direction: column;
  transition: transform 0.28s ease, box-shadow 0.28s ease, border-color 0.28s ease;
  position: relative;
}
.bento-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 16px 36px rgba(15, 23, 42, 0.12);
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
  height: 310px;
}
.bento-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1);
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
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
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
  padding: 1.65rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.bento-project-title {
  font-family: var(--font-heading);
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--text-main);
  line-height: 1.3;
  margin-bottom: 0.85rem;
  transition: color 0.2s ease;
}
.bento-card:hover .bento-project-title {
  color: var(--brand-violet);
}
.bento-meta-bar {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
  background: #f8fafc;
  border: 1px solid var(--border-line);
  border-radius: var(--radius-sm);
  padding: 0.65rem 0.75rem;
  margin-bottom: 1rem;
}
.bento-meta-item {
  display: flex;
  flex-direction: column;
}
.bento-meta-item .meta-label {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  margin-bottom: 0.15rem;
}
.bento-meta-item .meta-val {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--text-main);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
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
  background: var(--brand-violet-soft);
  color: var(--brand-violet);
  border: 1px solid rgba(78, 42, 132, 0.15);
  padding: 0.45rem 0.9rem;
  border-radius: var(--radius-full);
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.8125rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  transition: all 0.2s ease;
}
.btn-view-spec:hover {
  background: var(--brand-violet);
  color: #ffffff;
  border-color: var(--brand-violet);
  transform: translateX(2px);
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
  line-height: 1.6;
}

/* Executive Tender & Consultation Terminal */
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
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
.form-control:focus {
  outline: 2px solid var(--brand-violet);
  outline-offset: 1px;
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
  position: relative;
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
  background: rgba(11, 17, 32, 0.88);
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
  .brand-logo-img { height: 36px; max-width: 180px; }
  .btn-cta-full { display: none; }
  .btn-cta-short { display: inline; font-size: 0.8125rem; }
  .btn-header-cta { padding: 0.45rem 0.85rem; }
  .services-grid { grid-template-columns: 1fr; }
  .lifecycle-grid { grid-template-columns: 1fr; }
  .stat-grid { grid-template-columns: 1fr; }
  .form-row-2 { grid-template-columns: 1fr; }
  .phone-direct { display: none; }
}

/* ==========================================================================
   SCROLL REVEAL & INTERACTION ANIMATIONS
   ========================================================================== */

/* Active when JavaScript is active and prefers-reduced-motion is false */
.js-scroll-anim .reveal-init:not(.is-revealed) {
  opacity: 0;
  transform: translateY(28px);
  pointer-events: none;
}

.js-scroll-anim .reveal-init {
  transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}

/* Stagger delay utility classes */
.js-scroll-anim .reveal-delay-1 { transition-delay: 0.06s; }
.js-scroll-anim .reveal-delay-2 { transition-delay: 0.12s; }
.js-scroll-anim .reveal-delay-3 { transition-delay: 0.18s; }
.js-scroll-anim .reveal-delay-4 { transition-delay: 0.24s; }
.js-scroll-anim .reveal-delay-5 { transition-delay: 0.30s; }
.js-scroll-anim .reveal-delay-6 { transition-delay: 0.36s; }

/* Enhanced Section Header Cascade */
.js-scroll-anim .section-head.reveal-init:not(.is-revealed) .section-tag {
  opacity: 0;
  transform: translateY(12px);
}
.js-scroll-anim .section-head.reveal-init:not(.is-revealed) .section-title {
  opacity: 0;
  transform: translateY(18px);
}
.js-scroll-anim .section-head.reveal-init:not(.is-revealed) .section-desc {
  opacity: 0;
  transform: translateY(22px);
}

.js-scroll-anim .section-head.reveal-init .section-tag {
  transition: opacity 0.5s ease-out 0.04s, transform 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.04s;
}
.js-scroll-anim .section-head.reveal-init .section-title {
  transition: opacity 0.6s ease-out 0.10s, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.10s;
}
.js-scroll-anim .section-head.reveal-init .section-desc {
  transition: opacity 0.6s ease-out 0.18s, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.18s;
}

/* Subtle icon reveal pop */
.js-scroll-anim .about-bento-card.reveal-init:not(.is-revealed) .about-card-icon,
.js-scroll-anim .service-card.reveal-init:not(.is-revealed) .service-icon-box {
  transform: scale(0.85);
  opacity: 0;
}
.js-scroll-anim .about-bento-card.reveal-init .about-card-icon,
.js-scroll-anim .service-card.reveal-init .service-icon-box {
  transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) 0.15s, opacity 0.5s ease-out 0.15s;
}

/* Stat Box Pop */
.js-scroll-anim .stat-box.reveal-init:not(.is-revealed) {
  opacity: 0;
  transform: translateY(20px) scale(0.97);
}
.js-scroll-anim .stat-box.reveal-init {
  transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Scroll Progress Bar */
.scroll-progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3px;
  width: 0%;
  background: linear-gradient(90deg, var(--brand-violet) 0%, var(--brand-amber) 100%);
  transition: width 0.06s linear;
  z-index: 101;
  pointer-events: none;
}

/* Floating Back-to-Top Button */
.scroll-to-top {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: var(--brand-violet);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.25);
  box-shadow: 0 10px 25px rgba(78, 42, 132, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 99;
  opacity: 0;
  transform: translateY(16px) scale(0.85);
  pointer-events: none;
  transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1), transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), background 0.2s ease, box-shadow 0.2s ease;
}
.scroll-to-top.visible {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}
.scroll-to-top:hover {
  background: var(--brand-violet-hover);
  transform: translateY(-3px) scale(1.06);
  box-shadow: 0 14px 30px rgba(78, 42, 132, 0.45);
}
.scroll-to-top:focus-visible {
  outline: 3px solid var(--brand-amber);
  outline-offset: 3px;
}
@media (max-width: 575px) {
  .scroll-to-top {
    bottom: 1.25rem;
    right: 1.25rem;
    width: 40px;
    height: 40px;
  }
}

/* Nav Active Indicator */
.nav-links a {
  position: relative;
}
.nav-links a::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--brand-amber);
  border-radius: 2px;
  transition: width 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
.nav-links a:hover::after, .nav-links a.active::after {
  width: 100%;
}

/* Header Elevation when Scrolled */
.site-header.header-scrolled {
  background: rgba(255, 255, 255, 0.98);
  box-shadow: 0 8px 30px rgba(15, 23, 42, 0.08);
  border-bottom-color: rgba(226, 232, 240, 0.6);
}

/* Prefers Reduced Motion Accessibility Override */
@media (prefers-reduced-motion: reduce) {
  .js-scroll-anim .reveal-init:not(.is-revealed),
  .js-scroll-anim .section-head.reveal-init:not(.is-revealed) .section-tag,
  .js-scroll-anim .section-head.reveal-init:not(.is-revealed) .section-title,
  .js-scroll-anim .section-head.reveal-init:not(.is-revealed) .section-desc,
  .js-scroll-anim .stat-box.reveal-init:not(.is-revealed),
  .js-scroll-anim .about-bento-card.reveal-init:not(.is-revealed) .about-card-icon,
  .js-scroll-anim .service-card.reveal-init:not(.is-revealed) .service-icon-box {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
    pointer-events: auto !important;
  }
  .scroll-progress-bar {
    display: none !important;
  }
  .scroll-to-top {
    transition: none !important;
  }
}
"""



JS = r"""
document.addEventListener('DOMContentLoaded', function() {
  var lastFocusedElement = null;

  function trapFocus(modalElement) {
    var focusableEls = modalElement.querySelectorAll('a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])');
    if (!focusableEls.length) return;
    var firstEl = focusableEls[0];
    var lastEl = focusableEls[focusableEls.length - 1];

    modalElement.onkeydown = function(e) {
      if (e.key === 'Tab') {
        if (e.shiftKey) {
          if (document.activeElement === firstEl) {
            e.preventDefault();
            lastEl.focus();
          }
        } else {
          if (document.activeElement === lastEl) {
            e.preventDefault();
            firstEl.focus();
          }
        }
      }
    };
  }

  function closeModal(modalElement) {
    modalElement.classList.remove('open');
    document.body.style.overflow = '';
    modalElement.onkeydown = null;
    if (lastFocusedElement) {
      lastFocusedElement.focus();
      lastFocusedElement = null;
    }
  }

  // 1. Mobile Drawer Toggle with Accessible State
  var mobileToggleBtn = document.getElementById('btnMobileToggle');
  var mobileDrawer = document.getElementById('mobileDrawer');
  if (mobileToggleBtn && mobileDrawer) {
    mobileToggleBtn.addEventListener('click', function() {
      var isOpen = mobileDrawer.style.display === 'block';
      mobileDrawer.style.display = isOpen ? 'none' : 'block';
      mobileToggleBtn.setAttribute('aria-expanded', !isOpen);
      mobileToggleBtn.innerHTML = isOpen ? '&#9776;' : '&times;';
    });

    document.querySelectorAll('[data-close-drawer]').forEach(function(link) {
      link.addEventListener('click', function() {
        mobileDrawer.style.display = 'none';
        mobileToggleBtn.setAttribute('aria-expanded', 'false');
        mobileToggleBtn.innerHTML = '&#9776;';
      });
    });
  }

  // 2. Regional Hub Filter Tabs (FIX: Filter matching cards first, then apply limit)
  var hubTabs = document.querySelectorAll('.hub-tab');
  var projectCards = document.querySelectorAll('.bento-card');
  var projectsToggleBtn = document.getElementById('projectsToggleBtn');
  var projectsExpanded = false;
  var currentHub = 'all';

  function applyProjectFilters() {
    var matchingCards = [];
    projectCards.forEach(function(card) {
      var cardHub = card.getAttribute('data-hub');
      var hubMatch = (currentHub === 'all' || cardHub === currentHub);
      if (hubMatch) {
        matchingCards.push(card);
      } else {
        card.style.display = 'none';
      }
    });

    matchingCards.forEach(function(card, idx) {
      if (!projectsExpanded && idx >= 5) {
        card.style.display = 'none';
      } else {
        card.style.display = 'flex';
        card.classList.add('is-revealed');
      }
    });

    if (projectsToggleBtn) {
      if (matchingCards.length <= 5) {
        projectsToggleBtn.style.display = 'none';
      } else {
        projectsToggleBtn.style.display = 'inline-flex';
        if (projectsExpanded) {
          projectsToggleBtn.innerHTML = '<span>Showing All ' + matchingCards.length + ' Projects &middot; Show Less</span><span>&uarr;</span>';
        } else {
          projectsToggleBtn.innerHTML = '<span>Showing 5 of ' + matchingCards.length + ' Projects &middot; Open Complete Technical Ledger</span><span>&darr;</span>';
        }
      }
    }
  }

  hubTabs.forEach(function(tab) {
    tab.addEventListener('click', function() {
      hubTabs.forEach(function(t) { t.classList.remove('active'); });
      tab.classList.add('active');
      currentHub = tab.getAttribute('data-hub');
      applyProjectFilters();
    });
  });

  if (projectsToggleBtn) {
    projectsToggleBtn.addEventListener('click', function() {
      projectsExpanded = !projectsExpanded;
      applyProjectFilters();
    });
  }

  // 3. Gallery Expand / Collapse Toggle (Showing 4 initially)
  var galleryToggleBtn = document.getElementById('galleryToggleBtn');
  var galleryCards = document.querySelectorAll('.lifecycle-card');
  var galleryExpanded = false;

  if (galleryToggleBtn) {
    galleryToggleBtn.addEventListener('click', function() {
      galleryExpanded = !galleryExpanded;
      galleryCards.forEach(function(card, index) {
        if (index >= 4) {
          card.style.display = galleryExpanded ? 'block' : 'none';
          if (galleryExpanded) {
            card.classList.add('is-revealed');
          }
        }
      });
      if (galleryExpanded) {
        galleryToggleBtn.innerHTML = '<span>Showing All 12 Lifecycle Plates &middot; Show Less</span><span>&uarr;</span>';
      } else {
        galleryToggleBtn.innerHTML = '<span>Showing 4 Initial Lifecycle Plates &middot; Open Complete Photographic Archive (12 Plates)</span><span>&darr;</span>';
      }
    });
  }

  // 4. Project Technical Specification Modal
  var projectModal = document.getElementById('projectModal');
  var modalCloseBtn = document.getElementById('modalCloseBtn');
  var modalTitle = document.getElementById('modalTitle');
  var modalImg = document.getElementById('modalImg');
  var modalDesc = document.getElementById('modalDesc');
  var modalChainage = document.getElementById('modalChainage');
  var modalStandard = document.getElementById('modalStandard');
  var modalStructures = document.getElementById('modalStructures');
  var modalClient = document.getElementById('modalClient');

  function openProjectModal(projectId, triggerBtn) {
    if (!window.AXULAL_PROJECTS) return;
    var proj = window.AXULAL_PROJECTS.find(function(p) { return p.id === projectId; });
    if (!proj) return;

    lastFocusedElement = triggerBtn;

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
      trapFocus(projectModal);
    }
  }

  document.querySelectorAll('.btn-view-spec').forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      var id = btn.getAttribute('data-project-id');
      openProjectModal(id, btn);
    });
  });

  if (modalCloseBtn && projectModal) {
    modalCloseBtn.addEventListener('click', function() {
      closeModal(projectModal);
    });
    projectModal.addEventListener('click', function(e) {
      if (e.target === projectModal) {
        closeModal(projectModal);
      }
    });
  }

  // 5. Gallery Lightbox Modal
  var galleryModal = document.getElementById('galleryModal');
  var lightboxCloseBtn = document.getElementById('lightboxCloseBtn');
  var lightboxImg = document.getElementById('lightboxImg');
  var lightboxCaption = document.getElementById('lightboxCaption');

  document.querySelectorAll('.lifecycle-card').forEach(function(card) {
    card.addEventListener('click', function() {
      lastFocusedElement = card;
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
        trapFocus(galleryModal);
      }
    });
  });

  if (lightboxCloseBtn && galleryModal) {
    lightboxCloseBtn.addEventListener('click', function() {
      closeModal(galleryModal);
    });
    galleryModal.addEventListener('click', function(e) {
      if (e.target === galleryModal) {
        closeModal(galleryModal);
      }
    });
  }

  // Global ESC Key closes open modals
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      if (projectModal && projectModal.classList.contains('open')) {
        closeModal(projectModal);
      }
      if (galleryModal && galleryModal.classList.contains('open')) {
        closeModal(galleryModal);
      }
    }
  });

  // 6. Free FormSubmit.co AJAX Endpoint with Response Verification
  var rfpForm = document.getElementById('rfpForm');
  var formAlert = document.getElementById('formStatusAlert');
  var submitBtn = document.getElementById('rfpSubmitBtn');

  if (rfpForm) {
    rfpForm.addEventListener('submit', function(e) {
      e.preventDefault();
      if (!submitBtn) return;

      var originalBtnHtml = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<span>Transmitting RFP Inquiry...</span>';
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
        if (!response.ok) {
          throw new Error('Server returned HTTP ' + response.status);
        }
        return response.json();
      })
      .then(function(data) {
        if (data && (data.success === false || data.success === 'false')) {
          throw new Error(data.message || 'Submission was not accepted');
        }
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnHtml;
        if (formAlert) {
          formAlert.textContent = '✓ Thank you! Your RFP inquiry has been transmitted to our engineering directorate. A senior engineer will review your scope and reply within 24–48 hours.';
          formAlert.className = 'form-status-alert success';
        }
        rfpForm.reset();
      })
      .catch(function(error) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnHtml;
        if (formAlert) {
          formAlert.textContent = '⚠ Submission note: Please email your terms of reference directly to tenders@axulalengineers.com or call our office at +251 111 582107.';
          formAlert.className = 'form-status-alert error';
        }
      });
    });
  }

  // =========================================================================
  // 7. Scroll-Driven Section Animations & Telemetry
  // =========================================================================
  var prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Scroll Progress Bar & Floating Back to Top Controls
  var progressBar = document.getElementById('scrollProgressBar');
  var btnScrollToTop = document.getElementById('btnScrollToTop');
  var siteHeader = document.querySelector('.site-header');

  if (btnScrollToTop) {
    btnScrollToTop.addEventListener('click', function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Optimized Scroll Handler (Progress, Header Scrolled & Back-to-Top)
  var scrollTicking = false;
  function handleScrollTelemetry() {
    var winScroll = document.documentElement.scrollTop || document.body.scrollTop;
    var docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;

    // 1. Progress Bar
    if (progressBar && docHeight > 0) {
      var pct = Math.min(Math.max((winScroll / docHeight) * 100, 0), 100);
      progressBar.style.width = pct + '%';
    }

    // 2. Header Scrolled Elevation
    if (siteHeader) {
      if (winScroll > 30) {
        siteHeader.classList.add('header-scrolled');
      } else {
        siteHeader.classList.remove('header-scrolled');
      }
    }

    // 3. Floating Back to Top Button
    if (btnScrollToTop) {
      if (winScroll > 450) {
        btnScrollToTop.classList.add('visible');
      } else {
        btnScrollToTop.classList.remove('visible');
      }
    }

    scrollTicking = false;
  }

  window.addEventListener('scroll', function() {
    if (!scrollTicking) {
      window.requestAnimationFrame(handleScrollTelemetry);
      scrollTicking = true;
    }
  }, { passive: true });

  handleScrollTelemetry();

  // Scrollspy: Synchronize Active Nav Links
  var trackedSections = document.querySelectorAll('section[id]');
  var allNavLinks = document.querySelectorAll('.nav-links a, #mobileDrawer a');
  if (trackedSections.length && allNavLinks.length && 'IntersectionObserver' in window) {
    var scrollSpyObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var id = entry.target.getAttribute('id');
          if (id) {
            allNavLinks.forEach(function(link) {
              var href = link.getAttribute('href');
              if (href === '#' + id) {
                link.classList.add('active');
              } else {
                link.classList.remove('active');
              }
            });
          }
        }
      });
    }, {
      rootMargin: '-20% 0px -65% 0px'
    });

    trackedSections.forEach(function(sec) {
      scrollSpyObserver.observe(sec);
    });
  }

  // Scroll-Reveal Animations (IntersectionObserver)
  if (!prefersReducedMotion && 'IntersectionObserver' in window) {
    document.documentElement.classList.add('js-scroll-anim');

    var revealTargets = document.querySelectorAll(
      '.section-head, .stat-box, .about-bento-card, .service-card, .hub-tabs-wrap, .bento-card, .lifecycle-card, .credential-badge-card, .terminal-card'
    );

    revealTargets.forEach(function(el) {
      el.classList.add('reveal-init');
    });

    // Apply staggered delays to sibling grids
    var staggerContainers = document.querySelectorAll(
      '.stat-grid, .about-bento-grid, .services-grid, .credentials-grid, .terminal-grid'
    );
    staggerContainers.forEach(function(container) {
      var items = container.querySelectorAll('.reveal-init');
      items.forEach(function(item, idx) {
        item.classList.add('reveal-delay-' + ((idx % 6) + 1));
      });
    });

    var revealObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    revealTargets.forEach(function(el) {
      revealObserver.observe(el);
    });

    // Metric Proof Counters Animation
    var statBand = document.querySelector('.stat-band');
    if (statBand) {
      var counterRan = false;
      var counterObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting && !counterRan) {
            counterRan = true;
            observer.unobserve(entry.target);

            var statNumbers = statBand.querySelectorAll('.stat-number[data-target]');
            statNumbers.forEach(function(numEl) {
              var targetVal = parseFloat(numEl.getAttribute('data-target'));
              var decimals = parseInt(numEl.getAttribute('data-decimals') || '0', 10);
              var unitSpan = numEl.querySelector('.stat-unit');
              var duration = 1500;
              var startTimestamp = null;

              function easeOutQuart(x) {
                return 1 - Math.pow(1 - x, 4);
              }

              function step(timestamp) {
                if (!startTimestamp) startTimestamp = timestamp;
                var progress = Math.min((timestamp - startTimestamp) / duration, 1);
                var currentVal = easeOutQuart(progress) * targetVal;
                var displayStr = decimals > 0 ? currentVal.toFixed(decimals) : Math.floor(currentVal).toString();

                if (unitSpan && numEl.childNodes[0]) {
                  numEl.childNodes[0].nodeValue = displayStr + (decimals > 0 ? ' ' : '');
                } else if (!unitSpan) {
                  numEl.textContent = displayStr;
                }

                if (progress < 1) {
                  window.requestAnimationFrame(step);
                } else {
                  var finalStr = decimals > 0 ? targetVal.toFixed(decimals) : targetVal.toString();
                  if (unitSpan && numEl.childNodes[0]) {
                    numEl.childNodes[0].nodeValue = finalStr + (decimals > 0 ? ' ' : '');
                  } else if (!unitSpan) {
                    numEl.textContent = finalStr;
                  }
                }
              }

              window.requestAnimationFrame(step);
            });
          }
        });
      }, {
        threshold: 0.2
      });

      counterObserver.observe(statBand);
    }
  }
});
"""



HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Axulal Consulting Engineers PLC | Category-1 Highway &amp; Bridge Consultants</title>
  <meta name="description" content="Axulal Consulting Engineers PLC — Category-1 Highway and Bridge consulting engineers in Addis Ababa, Ethiopia (FDRE Reg #01/ORA/2011). Over 145.8 km of classified road corridors and 46.0 m of reinforced concrete river crossings delivered since 2011.">
  <link rel="canonical" href="https://axulalengineers.com/">
  <meta name="theme-color" content="#0b1120">

  <!-- Open Graph / Social Meta -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://axulalengineers.com/">
  <meta property="og:title" content="Axulal Consulting Engineers PLC | Category-1 Highway &amp; Bridge Consultants">
  <meta property="og:description" content="Category-1 Highway &amp; Bridge engineering consultancy in Addis Ababa, Ethiopia. Delivering over 145.8 km of classified road corridors and 46.0 m of reinforced concrete river crossings since 2011.">
  <meta property="og:image" content="https://axulalengineers.com/assets/logo.png">

  <!-- Twitter Meta -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://axulalengineers.com/">
  <meta name="twitter:title" content="Axulal Consulting Engineers PLC | Category-1 Highway &amp; Bridge Consultants">
  <meta name="twitter:description" content="Category-1 Highway &amp; Bridge engineering consultancy in Addis Ababa, Ethiopia. Delivering over 145.8 km of classified road corridors and 46.0 m of reinforced concrete river crossings since 2011.">
  <meta name="twitter:image" content="https://axulalengineers.com/assets/logo.png">

  <!-- Favicons -->
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
  <link rel="icon" type="image/png" href="assets/favicon.png">

  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "EngineeringService",
    "name": "Axulal Consulting Engineers PLC",
    "alternateName": "አክሱላል ኮንሰልቲንግ ኢንጂነርስ ኃላ/የተ/የግ/ማህበር",
    "url": "https://axulalengineers.com",
    "logo": "https://axulalengineers.com/assets/logo.png",
    "image": "https://axulalengineers.com/assets/projects/proj_6_awash_bridge.jpg",
    "foundingDate": "2011",
    "description": "Category-1 Highway and Bridge consulting engineers in Addis Ababa, Ethiopia (FDRE Reg #01/ORA/2011). Specializing in road geometric design, RC bridges, and resident construction supervision.",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Adwa Square, Katekse Building, 3rd Floor, House No: 712/A, Woreda: 07",
      "addressLocality": "Yeka Sub-city, Addis Ababa",
      "postalCode": "26061/1000",
      "addressCountry": "ET"
    },
    "telephone": "+251111582107",
    "email": "tenders@axulalengineers.com",
    "areaServed": "Ethiopia"
  }
  </script>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="assets/css/site.css?v=__V__">
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- Header -->
  <header class="site-header">
    <div class="container header-wrap">
      <a href="#home" aria-label="Axulal Consulting Engineers PLC Home">
        <picture>
          <source type="image/webp" srcset="assets/logo-horizontal.webp?v=__V__">
          <img src="assets/logo-horizontal.png?v=__V__" alt="Axulal Consulting Engineers PLC - አክሱላል" class="brand-logo-img" width="650" height="140">
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
          <span aria-hidden="true">📞</span> +251 111 582107
        </a>
        <a href="#contact" class="btn-primary btn-header-cta">
          <span class="btn-cta-full">Request RFP &rarr;</span>
          <span class="btn-cta-short">RFP &rarr;</span>
        </a>
        <button class="btn-mobile-toggle" id="btnMobileToggle" aria-label="Toggle Navigation" aria-expanded="false">
          &#9776;
        </button>
      </div>
    </div>
    <!-- Scroll Reading Progress Bar -->
    <div id="scrollProgressBar" class="scroll-progress-bar" aria-hidden="true"></div>
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

  <main id="main-content">
    <!-- Hero Section -->
    <section class="hero-viewport" id="home">
      <div class="hero-grid-overlay"></div>
      <div class="container hero-layout">
        
        <!-- Left Hero Column -->
        <div>
          <div class="hero-badge-pill">
            <span aria-hidden="true">🏛️</span>
            <span>CATEGORY-1 HIGHWAY &amp; BRIDGE CONSULTANTS</span>
          </div>
          <h1 class="hero-title">
            Engineering Ethiopia’s <br>
            <span class="highlight">Road Corridors &amp; River Bridges</span>
          </h1>
          <p class="hero-desc">
            Delivering precision geometric design, hydrological catchment modeling, and resident construction supervision across over 145.8 km of classified road infrastructure since 2011.
          </p>
          <div class="hero-btn-row">
            <a href="#projects" class="btn-primary">
              <span>Explore Projects</span>
              <span>&darr;</span>
            </a>
            <a href="#credentials" class="btn-secondary-glass">
              <span>📄 Corporate Profile</span>
            </a>
          </div>
        </div>

        <!-- Right Featured Civil Works Specification Card -->
        <div>
          <div class="telemetry-card">
            <div class="telemetry-header">
              <span class="telemetry-tag">FEATURED CIVIL WORKS &middot; AWASH BRIDGE</span>
              <span class="telemetry-live-dot">TECHNICAL SPEC</span>
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

      <!-- Infrastructure Highlights Marquee -->
      <div class="marquee-bar">
        <div class="marquee-track">
          <span class="marquee-item">145.8 KM DELIVERED ALL-WEATHER ROAD CORRIDORS</span>
          <span class="marquee-item">46.0 M REINFORCED CONCRETE RIVER BRIDGES</span>
          <span class="marquee-item">STA 0+000 – STA 27+000 EJERE-ARERTU CORRIDOR</span>
          <span class="marquee-item">100+ CROSS-DRAINAGE HYDRAULIC BOX &amp; PIPE CULVERTS</span>
          <span class="marquee-item">CATEGORY-1 FDRE REG #01/ORA/2011 ACCREDITATION</span>
          <span class="marquee-item">98% MODIFIED AASHTO SUB-BASE COMPACTION QC</span>
          <span class="marquee-item">145.8 KM DELIVERED ALL-WEATHER ROAD CORRIDORS</span>
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
            <div class="stat-number" data-target="145.8" data-decimals="1">145.8 <span class="stat-unit">km</span></div>
            <div class="stat-label">Classified Roads Delivered</div>
            <div class="stat-sub">Highland, mountainous &amp; rolling alignments</div>
          </div>
          <div class="stat-box">
            <div class="stat-number" data-target="46.0" data-decimals="1">46.0 <span class="stat-unit">m</span></div>
            <div class="stat-label">RC River Bridge Spans</div>
            <div class="stat-sub">Awash (24m) &amp; Berga (22m) Crossings</div>
          </div>
          <div class="stat-box">
            <div class="stat-number" data-target="100" data-decimals="0">100<span class="stat-unit">+</span></div>
            <div class="stat-label">Hydraulic Drainage Units</div>
            <div class="stat-sub">Box culverts, stone aprons &amp; retaining walls</div>
          </div>
          <div class="stat-box">
            <div class="stat-number">Cat-1</div>
            <div class="stat-label">Ministry Licensure</div>
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
            Established in 2011 in Addis Ababa, Axulal Consulting Engineers PLC (አክሱላል) is a Category-1 civil engineering consultancy specializing in road corridor design, structural bridges, and resident construction supervision.
          </p>
        </div>

        <div class="about-bento-grid">
          <div class="about-bento-card">
            <span class="about-card-icon" aria-hidden="true">🏛️</span>
            <h3 class="about-card-title">15-Year Proven Track Record</h3>
            <p class="about-card-text">
              Registered under FDRE Licensure #01/ORA/2011 with accreditation from the Ministry of Urban Development and Infrastructure (MoUDI) and the Ethiopian Roads Administration (ERA). Partnering with the Oromiya Road Authority (ORA) since 2011.
            </p>
            <div class="about-card-highlight">FDRE Reg #01/ORA/2011 &middot; MoUDI &amp; ERA Accredited</div>
          </div>

          <div class="about-bento-card">
            <span class="about-card-icon" aria-hidden="true">📐</span>
            <h3 class="about-card-title">Specialized Engineering Directorate</h3>
            <p class="about-card-text">
              Led by senior highway and structural engineers with extensive field experience across Ethiopian mountainous topography, expansive volcanic soils, seasonal flood basins, and modern CAD route geometry.
            </p>
            <div class="about-card-highlight">Senior Highway &amp; Bridge Engineers</div>
          </div>

          <div class="about-bento-card">
            <span class="about-card-icon" aria-hidden="true">🔬</span>
            <h3 class="about-card-title">Rigorous Field Quality Control</h3>
            <p class="about-card-text">
              Strict adherence to AASHTO, ERA, and Ethiopian road design manuals. Systematic quality testing including 98% Modified AASHTO sub-base compaction control, concrete cube compressive testing, and rebar validation.
            </p>
            <div class="about-card-highlight">Authority Acceptance on All 145.8 km Delivered</div>
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
            From initial route reconnaissance and hydrological catchment modeling to detailed CAD blueprinting and full-time resident site supervision.
          </p>
        </div>

        <div class="services-grid">
          <div class="service-card">
            <div class="service-icon-box" aria-hidden="true">🛣️</div>
            <h3 class="service-title">Road Feasibility &amp; Geometric Design</h3>
            <p class="service-text">
              Complete horizontal and vertical alignment optimization, earthwork cut/fill mass haul balancing, cross-fall cambering, and pavement layering across DC-1 to DC-4 road classes.
            </p>
            <ul class="service-list">
              <li>Geometric Alignment &amp; Profile CAD</li>
              <li>Earthwork Mass Haul Balancing</li>
              <li>Granular Sub-Base Optimization</li>
            </ul>
          </div>

          <div class="service-card">
            <div class="service-icon-box" aria-hidden="true">🌉</div>
            <h3 class="service-title">Bridge &amp; Structural Engineering</h3>
            <p class="service-text">
              Detailed structural engineering for reinforced concrete girder bridges, pier columns, deep foundation footings, and AASHTO HS20-44 live load calculations over high-discharge river basins.
            </p>
            <ul class="service-list">
              <li>Single &amp; Multi-Span RC Girders</li>
              <li>Abutment Scour Defense Systems</li>
              <li>Substructure Foundation Analysis</li>
            </ul>
          </div>

          <div class="service-card">
            <div class="service-icon-box" aria-hidden="true">💧</div>
            <h3 class="service-title">Hydrology &amp; Drainage Modeling</h3>
            <p class="service-text">
              Catchment basin runoff calculations and hydraulic dimensioning for multi-barrel RC box culverts, pipe culverts, mortared stone masonry headwalls, and erosion protection aprons.
            </p>
            <ul class="service-list">
              <li>Catchment Runoff Modeling</li>
              <li>Multi-Barrel Box Culverts</li>
              <li>Erosion Protection Aprons</li>
            </ul>
          </div>

          <div class="service-card">
            <div class="service-icon-box" aria-hidden="true">📋</div>
            <h3 class="service-title">Resident Supervision &amp; Oversight</h3>
            <p class="service-text">
              Full-time resident engineers providing on-site quality assurance, field testing verification, contractor compliance audits, measurement validation, and handover inspections.
            </p>
            <ul class="service-list">
              <li>Daily Materials QA/QC Testing</li>
              <li>Interim Payment Measurement Checks</li>
              <li>Authority Handover Audits</li>
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
            Structured bento showcase highlighting high-capacity road alignments and reinforced concrete river crossings delivered for the Oromiya Road Authority.
          </p>
        </div>

        <!-- Regional Hub Filter Tabs with Mathematically Verified Lengths -->
        <div class="hub-tabs-wrap">
          <button class="hub-tab active" data-hub="all">All Corridors (12)</button>
          <button class="hub-tab" data-hub="ginchi">Ginchi Hub (25.5 km)</button>
          <button class="hub-tab" data-hub="awash">Awash Basin (25.0 km + 24m Bridge)</button>
          <button class="hub-tab" data-hub="ejere">Ejere Sector (85.7 km)</button>
          <button class="hub-tab" data-hub="berga">Berga Sector (9.6 km + 22m Bridge)</button>
        </div>

        <!-- Bento Grid -->
        <div class="bento-grid" id="projectsGrid">
          __PROJECT_CARDS__
        </div>

        <!-- Expansion Trigger -->
        <div class="show-all-wrap">
          <button id="projectsToggleBtn" class="btn-show-all">
            <span>Showing 5 Flagship Projects &middot; Open Complete Technical Ledger (12 Projects)</span>
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
          <span class="section-tag">ACCREDITATION &amp; STANDARDS</span>
          <h2 class="section-title">Statutory Licensure &amp; Standards</h2>
          <p class="section-desc">
            Formally certified and licensed to execute highway, structural, and hydraulic civil engineering assignments across the Federal Democratic Republic of Ethiopia.
          </p>
        </div>

        <div class="credentials-grid">
          <div class="credential-badge-card">
            <div class="credential-icon" aria-hidden="true">📜</div>
            <h3 class="credential-title">Category-1 Licensure</h3>
            <div class="credential-meta">FDRE REG #01/ORA/2011</div>
            <p class="credential-desc">
              Category-1 consulting engineering license for highway, structural, and hydraulic infrastructure, authorizing major public and commercial transport projects.
            </p>
          </div>

          <div class="credential-badge-card">
            <div class="credential-icon" aria-hidden="true">🏛️</div>
            <h3 class="credential-title">Ministry Accredited</h3>
            <div class="credential-meta">MoUDI &amp; ERA ACCREDITED</div>
            <p class="credential-desc">
              Officially registered with the Ministry of Urban Development &amp; Infrastructure (MoUDI/MoWUD) and maintaining continuous compliance with ERA engineering manuals.
            </p>
          </div>

          <div class="credential-badge-card">
            <div class="credential-icon" aria-hidden="true">🏆</div>
            <h3 class="credential-title">15-Year Track Record</h3>
            <div class="credential-meta">OVER 145.8 KM DELIVERED</div>
            <p class="credential-desc">
              Over 145.8 km of classified road corridors and 46.0 m of RC bridges delivered in full compliance with authority design specifications and handover standards.
            </p>
          </div>
        </div>

        <div style="text-align:center; margin-top:2.5rem;">
          <button onclick="window.print()" class="btn-secondary-glass" style="color:var(--text-main); border-color:var(--border-line);">
            <span>🖨️ Print / Save Corporate Summary</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Tender & Project Inquiries Section -->
    <section class="section-wrap alt" id="contact">
      <div class="container">
        <div class="section-head">
          <span class="section-tag">TENDER &amp; PROJECT INQUIRIES</span>
          <h2 class="section-title">Initiate a Project Partnership</h2>
          <p class="section-desc">
            Connect directly with our engineering directorate to submit an RFP, discuss an upcoming road or bridge tender, or schedule a technical consultation.
          </p>
        </div>

        <div class="terminal-grid">
          
          <!-- Left Tender Submission Desk & Consultations Card -->
          <div class="terminal-card">
            <h3>Tender Submission Desk &amp; Consultations</h3>
            
            <div class="hq-info-row">
              <div class="hq-icon" aria-hidden="true">📋</div>
              <div class="hq-text">
                <h4>Engineering Proposal Review</h4>
                <p>All RFP submissions, project specifications, and tender terms of reference are reviewed directly by our Principal Highway and Bridge Engineers within 24–48 hours.</p>
              </div>
            </div>

            <div class="hq-info-row">
              <div class="hq-icon" aria-hidden="true">📞</div>
              <div class="hq-text">
                <h4>Direct Contact Lines &amp; Tender Desk</h4>
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
              📍 Corporate headquarters, statutory registration, and postal address are detailed in the Headquarters Desk below.
            </p>
          </div>

          <!-- Right RFP Consultation Form with Anti-Spam & Verified Feedback -->
          <div class="terminal-card">
            <h3>Request an RFP Consultation</h3>
            <p style="font-size:0.9375rem; color:var(--text-muted); margin-bottom:1.5rem;">
              Submit your project scope and corridor extent. Our senior highway and bridge directors reply within 24–48 hours.
            </p>

            <form id="rfpForm">
              <!-- FormSubmit Anti-Spam & Direct Routing -->
              <input type="hidden" name="_subject" value="New Engineering Inquiry - Axulal Web Portal">
              <input type="hidden" name="_captcha" value="false">
              <!-- Honeypot field (hidden from real users, catches bots) -->
              <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">

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
                  <option value="Road Corridor Geometric Design (DC-1 to DC-4)">Road Corridor Geometric Design (DC-1 to DC-4)</option>
                  <option value="Reinforced Concrete Girder River Bridge">Reinforced Concrete Girder River Bridge</option>
                  <option value="Hydraulic Catchment &amp; Drainage Culverts">Hydraulic Catchment &amp; Drainage Culverts</option>
                  <option value="Resident Construction Supervision &amp; QA">Resident Construction Supervision &amp; QA</option>
                </select>
              </div>

              <div class="form-group">
                <label class="form-label" for="rfpScope">Scope Description &amp; Location *</label>
                <textarea id="rfpScope" name="scope" class="form-control" rows="4" placeholder="Specify approximate route chainage, geographic region, terrain, and required design milestones..." required></textarea>
              </div>

              <button type="submit" id="rfpSubmitBtn" class="btn-primary" style="width:100%; justify-content:center; padding:0.85rem;">
                <span>Submit RFP Inquiry &rarr;</span>
              </button>

              <div id="formStatusAlert" class="form-status-alert" role="status" aria-live="polite"></div>
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
            <img src="assets/logo.png?v=__V__" alt="Axulal Consulting Engineers PLC Logo" class="footer-logo" width="800" height="660">
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

  <!-- Floating Back to Top Button -->
  <button id="btnScrollToTop" class="scroll-to-top" aria-label="Scroll to top of page" title="Return to top">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 15l-6-6-6 6"/></svg>
  </button>

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
    logo_files = [
        ASSETS_DIR / "logo.png",
        ASSETS_DIR / "logo-horizontal.png",
        ASSETS_DIR / "logo-mark.png"
    ]
    for lf in logo_files:
        if lf.exists():
            sources.append(lf)

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
        # Balanced bento layout: hero card on row 1 (idx 0), row 3 (idx 5), row 5 (idx 11)
        is_hero = (idx in [0, 5, 11])
        is_hidden = (idx >= 5)
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
              <div class="bento-meta-item">
                <span class="meta-label">Chainage</span>
                <span class="meta-val">{p['chainage']}</span>
              </div>
              <div class="bento-meta-item">
                <span class="meta-label">Standard</span>
                <span class="meta-val">{p['standard']}</span>
              </div>
              <div class="bento-meta-item">
                <span class="meta-label">Structures</span>
                <span class="meta-val">{p['structures']}</span>
              </div>
            </div>
            <p class="bento-desc">
              {p['desc']}
            </p>
            <div class="bento-card-footer">
              <span class="bento-client">Client: {p['client']}</span>
              <button class="btn-view-spec" data-project-id="{p['id']}">
                <span>View Blueprint &amp; Specs</span>
                <span>&rarr;</span>
              </button>
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

    # 6. Write robots.txt
    robots_content = """User-agent: *
Allow: /

Sitemap: https://axulalengineers.com/sitemap.xml
"""
    with open(ROBOTS_FILE, "w", encoding="utf-8") as f:
        f.write(robots_content.strip() + "\n")
    print("  wrote robots.txt")

    # 7. Write sitemap.xml
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://axulalengineers.com/</loc>
    <lastmod>2026-11-02</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
"""
    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(sitemap_content.strip() + "\n")
    print("  wrote sitemap.xml")

    print(f"Master build complete! Version: {ASSET_VERSION}")

if __name__ == "__main__":
    build()
