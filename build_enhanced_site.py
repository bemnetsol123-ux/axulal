import os
import json

def build_site():
    print("Building enhanced Axulal website...")

    # Data for the 12 projects
    projects_data = [
        {
            "id": "P-01",
            "name": "Ginchi-Danisa Gravel Road Project",
            "type": "road",
            "length": 15.5,
            "metric": "15.5 km",
            "cost": "14,660,079.54 ETB",
            "standard": "6m Width (DC-2 Standard)",
            "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_1_ginchi_danisa.jpg",
            "desc": "15.5 km of classified rural highway traversing mountainous terrain, featuring mortared stone masonry retaining walls and hydraulic box culverts."
        },
        {
            "id": "P-02",
            "name": "Asgori-Kotoba Gravel Road Project (Lot 1 & 2)",
            "type": "road",
            "length": 22.5,
            "metric": "22.5 km",
            "cost": "13,456,796.54 ETB",
            "standard": "6m Width (DC-2 Standard)",
            "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_2_asgori_kotoba.jpg",
            "desc": "Dual-lot classified road connecting agrarian market centers, with heavy cut-and-fill benching and longitudinal drainage channels."
        },
        {
            "id": "P-03",
            "name": "Awash-Horota-Tululuba Gravel Road Project",
            "type": "road",
            "length": 11.0,
            "metric": "11.0 km",
            "cost": "6,542,136.32 ETB",
            "standard": "6m Width (DC-2 Standard)",
            "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_3_awash_horota.jpg",
            "desc": "Critical transport connector with comprehensive soil stabilization, camber shaping, and selected gravel capping."
        },
        {
            "id": "P-04",
            "name": "Gallesa-Kebabereda-Keteketa Gravel Road",
            "type": "road",
            "length": 10.3,
            "metric": "10.3 km",
            "cost": "6,827,386.67 ETB",
            "standard": "6m Width (DC-2 Standard)",
            "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_4_gallesa.jpg",
            "desc": "Highland gravel alignment designed with erosion-control runoff berms and hand-dressed masonry cross-drainage structures."
        },
        {
            "id": "P-05",
            "name": "Olenkomy-Awash Gravel Road Project",
            "type": "road",
            "length": 6.5,
            "metric": "6.5 km",
            "cost": "6,631,616.00 ETB",
            "standard": "6m Width (DC-2 Standard)",
            "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_5_olenkomy_awash.jpg",
            "desc": "Heavy agricultural corridor engineered for heavy axle loads, deep sub-base compaction, and durable gravel surface course."
        },
        {
            "id": "P-06",
            "name": "Awash River Girder Bridge Project",
            "type": "bridge",
            "length": 24.0,
            "metric": "24.0 m",
            "cost": "10,126,088.28 ETB",
            "standard": "Reinforced Concrete Girder",
            "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_6_awash_bridge.jpg",
            "desc": "24-meter single-span reinforced concrete girder bridge over the Awash River with deep abutment footings and hydraulic scouring countermeasures."
        },
        {
            "id": "P-07",
            "name": "Ejere-Arertu Gravel Road Project",
            "type": "road",
            "length": 27.0,
            "metric": "27.0 km",
            "cost": "16,809,652.77 ETB",
            "standard": "6m Width (DC-2 Standard)",
            "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_7_ejere_arertu.jpg",
            "desc": "Our longest single alignment: 27.0 km of all-weather road with multi-catchment drainage culverts, rock cuts, and community access ramps."
        },
        {
            "id": "P-08",
            "name": "Ejere-Kussaye-Goli Gravel Road Project",
            "type": "road",
            "length": 9.0,
            "metric": "9.0 km",
            "cost": "11,516,832.09 ETB",
            "standard": "6m Width (DC-2 Standard)",
            "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_8_ejere_kussaye.jpg",
            "desc": "Rural link road engineered with subgrade stabilization across expansive clay soils, stone-lined ditches, and compaction QC."
        },
        {
            "id": "P-09",
            "name": "Ejere-Hidi-Ibu Gravel Road Project",
            "type": "road",
            "length": 14.0,
            "metric": "14.0 km",
            "cost": "10,057,575.13 ETB",
            "standard": "6m Width (DC-2 Standard)",
            "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_9_ejere_hidi_ibu.jpg",
            "desc": "14 km roadway connecting regional farming centers, featuring multiple concrete box culverts and roadside retaining aprons."
        },
        {
            "id": "P-10",
            "name": "Ejere-Endode Gravel Road Project",
            "type": "road",
            "length": 6.5,
            "metric": "6.5 km",
            "cost": "10,057,575.13 ETB",
            "standard": "6m Width (DC-2 Standard)",
            "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_10_ejere_endode.jpg",
            "desc": "Feeder corridor designed to DC-2 standards with optimized cut-and-fill earthworks and community water crossing facilities."
        },
        {
            "id": "P-11",
            "name": "Berga River Girder Bridge Project",
            "type": "bridge",
            "length": 22.0,
            "metric": "22.0 m",
            "cost": "8,919,374.63 ETB",
            "standard": "Reinforced Concrete Girder",
            "scope": "Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_11_berga_bridge.jpg",
            "desc": "22-meter reinforced concrete girder bridge over Berga River; site quality supervision, rebar cage testing, and concrete cube compressive validation."
        },
        {
            "id": "P-12",
            "name": "Werkakore-Bujiroo Gravel Road Project",
            "type": "road",
            "length": 6.0,
            "metric": "6.0 km",
            "cost": "5,048,618.05 ETB",
            "standard": "6m Width (DC-2 Standard)",
            "scope": "Detail Engineering Design, Tender Document, Construction Supervision and Contract Administration",
            "client": "Oromiya Road Authority (ORA)",
            "img": "assets/projects/proj_12_werkakore_bujiroo.jpg",
            "desc": "Challenging rocky terrain alignment requiring mechanical rock excavation, stone gabion protection, and final camber grading."
        }
    ]

    # Gallery Plates Data
    gallery_data = [
        {"plate": "PLATE 01", "title": "Sub-Base Compaction", "img": "assets/gallery/plate_01_compaction.jpg", "desc": "Heavy vibratory road roller compacting selected sub-base gravel on Ginchi-Danisa alignment."},
        {"plate": "PLATE 02", "title": "Bridge Pier & Abutment", "img": "assets/gallery/plate_02_bridge_pier.jpg", "desc": "Reinforced concrete pier column, abutment formwork, and falsework at Awash Bridge."},
        {"plate": "PLATE 03", "title": "Hydraulic Drainage Culvert", "img": "assets/gallery/plate_03_drainage_culvert.jpg", "desc": "Hand-dressed stone masonry headwalls and barrel construction for cross-drainage."},
        {"plate": "PLATE 04", "title": "Hillside Benching & Earthwork", "img": "assets/gallery/plate_04_hillside_cut.jpg", "desc": "Heavy crawler excavator cutting road bench through steep terrain on Asgori-Kotoba."},
        {"plate": "PLATE 05", "title": "Finished DC-2 Alignment", "img": "assets/gallery/plate_05_road_alignment.jpg", "desc": "Completed all-weather DC-2 gravel carriageway smoothly winding through rural Oromia."},
        {"plate": "PLATE 06", "title": "Substructure Foundation Excavation", "img": "assets/gallery/plate_06_foundation_works.jpg", "desc": "Deep footing excavation and dewatering for stream crossing concrete substructure."},
        {"plate": "PLATE 07", "title": "Embankment Retaining Structure", "img": "assets/gallery/plate_07_retaining_wall.jpg", "desc": "Cast reinforced concrete retaining wall stabilizing vulnerable roadway embankment toe."},
        {"plate": "PLATE 08", "title": "Reinforced Concrete Box Culvert", "img": "assets/gallery/plate_08_box_culvert.jpg", "desc": "Pre-pour formwork and reinforcement steel inspections on Ejere-Hidi-Ibu roadway."},
        {"plate": "PLATE 09", "title": "Berga Bridge Superstructure", "img": "assets/gallery/plate_09_berga_bridge_deck.jpg", "desc": "Precast reinforced concrete girder erection and deck slab rebar grid placement."},
        {"plate": "PLATE 10", "title": "Rock Cut & Grading", "img": "assets/gallery/plate_10_rock_blasting_cut.jpg", "desc": "Mechanical rock ripping, heavy excavation, and roadway grading on Werkakore-Bujiroo."},
        {"plate": "PLATE 11", "title": "Gabion Mattress Slope Defense", "img": "assets/gallery/plate_11_gabion_protection.jpg", "desc": "Heavy wire-mesh stone gabion mattresses along riverbanks preventing erosion."},
        {"plate": "PLATE 12", "title": "Final Camber Shaping & Handover", "img": "assets/gallery/plate_12_final_surface.jpg", "desc": "Motor grader fine-shaping cross-fall camber and surface smoothness prior to commissioning."}
    ]

    projects_json = json.dumps(projects_data)
    gallery_json = json.dumps(gallery_data)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Axulal Consulting Engineers PLC | Category-1 Highway and Bridge Consultants, Addis Ababa</title>
<meta name="description" content="Axulal Consulting Engineers PLC is a premier Category-1 Highway and Bridge consulting firm based in Addis Ababa, Ethiopia. Delivering expert road and bridge engineering, surveys, tender documents, and construction supervision since 2011.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,400..900&family=Source+Sans+3:ital,wght@0,300..700;1,400&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
:root {{
  --navy: #091a3e;
  --navy-dark: #050e23;
  --blue: #1c5ec2;
  --blue-light: #3a7be0;
  --blue-subtle: #edf3fc;
  --red: #d9271d;
  --red-hover: #b81e15;
  --paper: #f4f7fc;
  --card: #ffffff;
  --tr: #e7eefb;
  --ink: #111e38;
  --muted: #536280;
  --line: #c6d5eb;
  --grid: rgba(28, 94, 194, 0.05);
  --shadow-sm: 0 1px 3px rgba(9, 26, 62, 0.06), 0 1px 2px rgba(9, 26, 62, 0.04);
  --shadow-md: 0 4px 14px rgba(9, 26, 62, 0.08), 0 2px 4px rgba(9, 26, 62, 0.04);
  --shadow-lg: 0 12px 28px rgba(9, 26, 62, 0.12), 0 4px 8px rgba(9, 26, 62, 0.06);
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --max-w: 1220px;
}}

@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --navy: #0a1733;
    --navy-dark: #040a17;
    --blue: #639dfa;
    --blue-light: #89b5fc;
    --blue-subtle: #132247;
    --red: #ff5e54;
    --red-hover: #ff7b73;
    --paper: #0b1326;
    --card: #111d3d;
    --tr: #182852;
    --ink: #eaf0fc;
    --muted: #a3b4d4;
    --line: #263863;
    --grid: rgba(99, 157, 250, 0.05);
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 4px 14px rgba(0, 0, 0, 0.4);
    --shadow-lg: 0 12px 28px rgba(0, 0, 0, 0.5);
  }}
}}

:root[data-theme="dark"] {{
  --navy: #0a1733;
  --navy-dark: #040a17;
  --blue: #639dfa;
  --blue-light: #89b5fc;
  --blue-subtle: #132247;
  --red: #ff5e54;
  --red-hover: #ff7b73;
  --paper: #0b1326;
  --card: #111d3d;
  --tr: #182852;
  --ink: #eaf0fc;
  --muted: #a3b4d4;
  --line: #263863;
  --grid: rgba(99, 157, 250, 0.05);
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 14px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 12px 28px rgba(0, 0, 0, 0.5);
}}

:root[data-theme="light"] {{
  --navy: #091a3e;
  --navy-dark: #050e23;
  --blue: #1c5ec2;
  --blue-light: #3a7be0;
  --blue-subtle: #edf3fc;
  --red: #d9271d;
  --red-hover: #b81e15;
  --paper: #f4f7fc;
  --card: #ffffff;
  --tr: #e7eefb;
  --ink: #111e38;
  --muted: #536280;
  --line: #c6d5eb;
  --grid: rgba(28, 94, 194, 0.05);
  --shadow-sm: 0 1px 3px rgba(9, 26, 62, 0.06), 0 1px 2px rgba(9, 26, 62, 0.04);
  --shadow-md: 0 4px 14px rgba(9, 26, 62, 0.08), 0 2px 4px rgba(9, 26, 62, 0.04);
  --shadow-lg: 0 12px 28px rgba(9, 26, 62, 0.12), 0 4px 8px rgba(9, 26, 62, 0.06);
}}

*, *::before, *::after {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

html {{
  scroll-behavior: smooth;
  scroll-padding-top: 84px;
  font-size: 16px;
}}

body {{
  font-family: 'Source Sans 3', system-ui, -apple-system, sans-serif;
  color: var(--ink);
  background-color: var(--paper);
  background-image: 
    linear-gradient(var(--grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 32px 32px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}}

img {{
  max-width: 100%;
  height: auto;
  display: block;
}}

a {{
  color: inherit;
  text-decoration: none;
}}

button {{
  font: inherit;
  cursor: pointer;
  border: none;
  background: none;
}}

.wrap {{
  width: 100%;
  max-width: var(--max-w);
  margin-inline: auto;
  padding-inline: 1.5rem;
}}

/* ================= HEADER ================= */
#hd {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--navy);
  color: #ffffff;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  transition: background 0.25s ease, box-shadow 0.25s ease;
}}

#hd.sc {{
  background: var(--navy-dark);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
}}

.bar-in {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 74px;
  gap: 1rem;
}}

.brand {{
  display: inline-flex;
  align-items: center;
  gap: 0.85rem;
  font-family: 'Archivo', sans-serif;
  font-weight: 800;
  font-size: 1.05rem;
  letter-spacing: 0.02em;
  color: #ffffff;
  text-transform: uppercase;
}}

.brand img.brand-logo-img {{
  width: 38px;
  height: 38px;
  object-fit: contain;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
}}

.brand .cat-pill {{
  display: inline-block;
  font-size: 0.65rem;
  font-weight: 700;
  padding: 0.15rem 0.45rem;
  background: var(--red);
  color: #fff;
  border-radius: 3px;
  letter-spacing: 0.08em;
  vertical-align: middle;
  margin-left: 0.35rem;
}}

#nav {{
  display: flex;
  align-items: center;
  gap: 1.5rem;
}}

#nav a {{
  font-family: 'Archivo', sans-serif;
  font-size: 0.88rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: #c9d8f5;
  transition: color 0.15s ease;
  position: relative;
  padding-block: 0.25rem;
}}

#nav a:hover, #nav a.on {{
  color: #ffffff;
}}

#nav a.on::after {{
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--red);
  border-radius: 2px;
}}

.hd-actions {{
  display: flex;
  align-items: center;
  gap: 0.75rem;
}}

.theme-btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 38px;
  border-radius: var(--radius-sm);
  color: #c9d8f5;
  border: 1px solid rgba(255, 255, 255, 0.2);
  background: rgba(255, 255, 255, 0.06);
  transition: all 0.2s ease;
}}

.theme-btn:hover {{
  color: #ffffff;
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.4);
}}

.theme-btn svg {{
  width: 18px;
  height: 18px;
}}

.btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-family: 'Archivo', sans-serif;
  font-weight: 700;
  font-size: 0.88rem;
  letter-spacing: 0.03em;
  padding: 0.65rem 1.25rem;
  border-radius: var(--radius-sm);
  background: var(--red);
  color: #ffffff;
  border: 1px solid transparent;
  transition: all 0.2s ease;
  text-transform: uppercase;
}}

.btn:hover {{
  background: var(--red-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(217, 39, 29, 0.35);
}}

.btn.ghost {{
  background: transparent;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.35);
}}

.btn.ghost:hover {{
  background: rgba(255, 255, 255, 0.12);
  border-color: #ffffff;
}}

.menu-btn {{
  display: none;
  width: 42px;
  height: 42px;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-sm);
}}

.menu-btn svg {{
  width: 24px;
  height: 24px;
  stroke: currentColor;
  stroke-width: 2;
  fill: none;
}}

/* ================= HERO ================= */
.hero {{
  background: var(--navy);
  color: #ffffff;
  padding-top: 3.5rem;
  padding-bottom: 2.5rem;
  position: relative;
  overflow: hidden;
  border-bottom: 1px solid var(--line);
}}

.hero::before {{
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 65%;
  height: 100%;
  background: radial-gradient(circle at 85% 25%, rgba(28, 94, 194, 0.22), transparent 70%);
  pointer-events: none;
}}

.hero-grid {{
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 3rem;
  align-items: center;
}}

.badge-row {{
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1.25rem;
  flex-wrap: wrap;
}}

.reg-badge {{
  display: inline-flex;
  align-items: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.74rem;
  font-weight: 600;
  padding: 0.3rem 0.65rem;
  border-radius: 3px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #c9d8f5;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}}

.motto-tag {{
  display: inline-block;
  font-family: 'Archivo', sans-serif;
  font-size: 0.82rem;
  font-weight: 800;
  color: var(--red);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}}

.hero h1 {{
  font-family: 'Archivo', sans-serif;
  font-size: clamp(2.2rem, 3.8vw, 3.2rem);
  font-weight: 850;
  line-height: 1.15;
  letter-spacing: -0.02em;
  margin-bottom: 1.25rem;
  color: #ffffff;
}}

.hero-lead {{
  font-size: 1.125rem;
  line-height: 1.65;
  color: #c9d8f5;
  margin-bottom: 2rem;
  max-width: 580px;
}}

.cta-group {{
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1.75rem;
}}

.hero-links-row {{
  display: flex;
  align-items: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}}

.direct-call, .hero-map-link {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  color: #a3b8e0;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: color 0.15s ease;
}}

.direct-call:hover, .hero-map-link:hover {{
  color: #ffffff;
}}

/* Technical Showcase Box */
.hero-visual-card {{
  background: rgba(10, 23, 51, 0.82);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  overflow: hidden;
  position: relative;
}}

.visual-topbar {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.6rem 0.9rem;
  background: rgba(255, 255, 255, 0.06);
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  color: #a3b8e0;
  letter-spacing: 0.05em;
}}

.visual-tabs {{
  display: flex;
  gap: 0.35rem;
}}

.v-tab-btn {{
  padding: 0.25rem 0.65rem;
  font-family: 'Archivo', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  color: #a3b8e0;
  border-radius: 3px;
  background: transparent;
  transition: all 0.15s ease;
}}

.v-tab-btn.active {{
  background: var(--blue);
  color: #ffffff;
}}

.visual-panel {{
  display: none;
  position: relative;
}}

.visual-panel.active {{
  display: block;
}}

.hero-photo-wrap {{
  position: relative;
}}

.hero-photo-wrap img {{
  width: 100%;
  height: 290px;
  object-fit: cover;
  display: block;
}}

.photo-badge {{
  position: absolute;
  bottom: 0.75rem;
  left: 0.75rem;
  right: 0.75rem;
  background: rgba(5, 14, 35, 0.88);
  backdrop-filter: blur(5px);
  padding: 0.5rem 0.75rem;
  border-radius: var(--radius-sm);
  font-size: 0.8rem;
  color: #eaf0fc;
  border-left: 3px solid var(--red);
}}

.prof-svg-wrap {{
  padding: 1.25rem 1rem 0.75rem;
  background: #050d22;
}}

.prof-svg-wrap svg {{
  width: 100%;
  height: auto;
  display: block;
}}

.prof-svg-wrap .g {{
  fill: none;
  stroke: #2e4475;
  stroke-width: 2;
  stroke-dasharray: 4 4;
}}

.prof-svg-wrap .r {{
  fill: none;
  stroke: var(--red);
  stroke-width: 2.5;
}}

.prof-svg-wrap .b {{
  fill: none;
  stroke: var(--blue-light);
  stroke-width: 3.2;
}}

.prof-svg-wrap .t {{
  stroke: #5d75a3;
  stroke-width: 1;
  fill: none;
}}

.prof-svg-wrap text {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  fill: #8aa4d1;
  font-weight: 600;
  letter-spacing: 0.04em;
}}

/* Stats Banner */
.stats-banner {{
  margin-top: 2.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  padding-top: 1.75rem;
}}

.stats-grid {{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1.5rem;
}}

.stat-item {{
  border-left: 2px solid var(--blue-light);
  padding-left: 1rem;
}}

.stat-num {{
  display: block;
  font-family: 'Archivo', sans-serif;
  font-weight: 850;
  font-size: 1.8rem;
  line-height: 1.1;
  color: #ffffff;
  margin-bottom: 0.25rem;
}}

.stat-label {{
  font-size: 0.82rem;
  color: #a3b8e0;
  line-height: 1.35;
}}

/* ================= SECTIONS COMMON ================= */
section {{
  padding-block: 5.5rem;
}}

section.alt {{
  background: var(--card);
  border-block: 1px solid var(--line);
}}

.sec-head {{
  margin-bottom: 3.25rem;
  position: relative;
}}

.sec-tag {{
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--blue);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 0.5rem;
}}

.sec-head h2 {{
  font-family: 'Archivo', sans-serif;
  font-size: clamp(1.85rem, 3.2vw, 2.6rem);
  font-weight: 800;
  color: var(--ink);
  line-height: 1.2;
  letter-spacing: -0.02em;
}}

.sec-lead {{
  font-size: 1.125rem;
  color: var(--muted);
  max-width: 720px;
  margin-top: 0.75rem;
  line-height: 1.6;
}}

/* ================= ABOUT SECTION ================= */
.about-grid {{
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 3.5rem;
  margin-bottom: 3.5rem;
}}

.about-body p.big {{
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.5;
  margin-bottom: 1.25rem;
}}

.about-body p {{
  font-size: 1.025rem;
  color: var(--muted);
  margin-bottom: 1.25rem;
  line-height: 1.7;
}}

.vm-cards {{
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}}

.vm-box {{
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  box-shadow: var(--shadow-sm);
  position: relative;
  border-left: 4px solid var(--blue);
}}

.vm-box.mission {{
  border-left-color: var(--red);
}}

.vm-box h3 {{
  font-family: 'Archivo', sans-serif;
  font-size: 1.15rem;
  font-weight: 750;
  color: var(--ink);
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}}

.vm-box p {{
  font-size: 0.95rem;
  color: var(--muted);
  line-height: 1.6;
}}

/* Company Structure & Org Chart Box */
.org-chart-section {{
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  margin-bottom: 3.5rem;
  box-shadow: var(--shadow-sm);
}}

.org-chart-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2.5rem;
  align-items: center;
}}

.org-chart-img-wrap {{
  background: #ffffff;
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-sm);
}}

.org-chart-img-wrap img {{
  width: 100%;
  max-width: 500px;
  height: auto;
  object-fit: contain;
}}

.org-chart-text h3 {{
  font-family: 'Archivo', sans-serif;
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--ink);
  margin-bottom: 0.75rem;
}}

.org-chart-text p {{
  font-size: 0.95rem;
  color: var(--muted);
  line-height: 1.65;
  margin-bottom: 1.25rem;
}}

.dept-list {{
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}}

.dept-item {{
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.925rem;
  font-weight: 600;
  color: var(--ink);
}}

.dept-bullet {{
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--blue);
}}

/* Tech Stack & Capacity Box */
.capacity-grid {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-top: 3rem;
}}

.cap-card {{
  background: var(--tr);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  text-align: center;
}}

.cap-num {{
  font-family: 'Archivo', sans-serif;
  font-size: 2rem;
  font-weight: 850;
  color: var(--blue);
  display: block;
  line-height: 1;
  margin-bottom: 0.35rem;
}}

.cap-label {{
  font-family: 'Archivo', sans-serif;
  font-size: 0.9rem;
  font-weight: 750;
  color: var(--ink);
  margin-bottom: 0.25rem;
  display: block;
}}

.cap-desc {{
  font-size: 0.8rem;
  color: var(--muted);
}}

/* Software Chips Row */
.software-bar {{
  margin-top: 2rem;
  padding: 1.5rem;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}}

.software-title {{
  font-family: 'Archivo', sans-serif;
  font-size: 0.85rem;
  font-weight: 800;
  color: var(--ink);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}}

.software-chips {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}}

.sw-chip {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.3rem 0.65rem;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 4px;
  color: var(--ink);
}}

/* ================= SERVICES SECTION ================= */
.svc-nav-header {{
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1.25rem;
}}

.view-toggle {{
  display: inline-flex;
  padding: 0.25rem;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: var(--radius-sm);
  gap: 0.25rem;
}}

.view-toggle button {{
  padding: 0.4rem 0.85rem;
  font-family: 'Archivo', sans-serif;
  font-size: 0.82rem;
  font-weight: 700;
  border-radius: 3px;
  color: var(--muted);
  transition: all 0.15s ease;
}}

.view-toggle button.active {{
  background: var(--card);
  color: var(--ink);
  box-shadow: var(--shadow-sm);
}}

.svc-tabs-container {{
  display: grid;
  grid-template-columns: 330px 1fr;
  gap: 2rem;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  box-shadow: var(--shadow-sm);
}}

.svc-tablist {{
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}}

.svc-tab-btn {{
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.1rem 1.25rem;
  border-radius: var(--radius-md);
  background: var(--card);
  border: 1px solid var(--line);
  text-align: left;
  font-family: 'Archivo', sans-serif;
  font-size: 1rem;
  font-weight: 700;
  color: var(--ink);
  transition: all 0.2s ease;
}}

.svc-tab-btn svg {{
  width: 28px;
  height: 28px;
  stroke: var(--muted);
  stroke-width: 2.2;
  fill: none;
  flex-shrink: 0;
  transition: stroke 0.2s ease;
}}

.svc-tab-btn:hover {{
  border-color: var(--blue);
  color: var(--blue);
}}

.svc-tab-btn[aria-selected="true"] {{
  background: var(--navy);
  color: #ffffff;
  border-color: var(--navy);
  box-shadow: var(--shadow-md);
}}

.svc-tab-btn[aria-selected="true"] svg {{
  stroke: var(--blue-light);
}}

.svc-panel {{
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 2.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}

.svc-panel-head {{
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin-bottom: 1.25rem;
}}

.svc-panel-head svg {{
  width: 48px;
  height: 48px;
  stroke: var(--blue);
  stroke-width: 2.2;
  fill: none;
  flex-shrink: 0;
}}

.svc-panel-head h3 {{
  font-family: 'Archivo', sans-serif;
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--ink);
}}

.svc-panel-desc {{
  font-size: 1.05rem;
  color: var(--muted);
  margin-bottom: 2rem;
  line-height: 1.7;
}}

.svc-sublist {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.85rem 1.5rem;
  list-style: none;
}}

.svc-sublist li {{
  display: flex;
  align-items: center;
  gap: 0.65rem;
  font-size: 0.975rem;
  font-weight: 600;
  color: var(--ink);
}}

.svc-sublist li::before {{
  content: '✓';
  color: var(--blue);
  font-weight: 800;
}}

/* Grid View */
.svc-grid-view {{
  display: none;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}}

.svc-grid-view.active {{
  display: grid;
}}

.svc-grid-card {{
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 2rem 1.5rem;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
}}

.svc-grid-card svg {{
  width: 38px;
  height: 38px;
  stroke: var(--blue);
  stroke-width: 2.2;
  fill: none;
  margin-bottom: 1.25rem;
}}

.svc-grid-card h3 {{
  font-family: 'Archivo', sans-serif;
  font-size: 1.2rem;
  font-weight: 750;
  color: var(--ink);
  margin-bottom: 0.75rem;
}}

.svc-grid-card p {{
  font-size: 0.9rem;
  color: var(--muted);
  margin-bottom: 1.25rem;
  line-height: 1.5;
}}

.svc-grid-card ul {{
  list-style: none;
  margin-top: auto;
  border-top: 1px dashed var(--line);
  padding-top: 1rem;
}}

.svc-grid-card ul li {{
  font-size: 0.85rem;
  color: var(--ink);
  margin-bottom: 0.4rem;
}}

/* ================= HOW A PROJECT RUNS (STATIONS) ================= */
.stations-track {{
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1rem;
  position: relative;
  list-style: none;
}}

.stations-track::before {{
  content: '';
  position: absolute;
  top: 26px;
  left: 20px;
  right: 20px;
  height: 3px;
  background: var(--line);
  z-index: 1;
}}

.station-node {{
  position: relative;
  z-index: 2;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 1.25rem 1rem;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s ease, border-color 0.2s ease;
}}

.station-node:hover {{
  transform: translateY(-4px);
  border-color: var(--blue);
  box-shadow: var(--shadow-md);
}}

.sta-pin {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--blue);
  color: #fff;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
  box-shadow: 0 0 0 4px var(--card);
}}

.sta-tag {{
  display: block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--red);
  letter-spacing: 0.05em;
  margin-bottom: 0.25rem;
}}

.station-node h3 {{
  font-family: 'Archivo', sans-serif;
  font-size: 1.1rem;
  font-weight: 750;
  color: var(--ink);
  margin-bottom: 0.4rem;
}}

.station-node p {{
  font-size: 0.85rem;
  color: var(--muted);
  line-height: 1.45;
}}

/* ================= FEATURED PROJECTS ================= */
.featured-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  margin-bottom: 3.5rem;
}}

.feat-card {{
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}}

.feat-card:hover {{
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}}

.feat-img-wrap {{
  height: 260px;
  overflow: hidden;
  position: relative;
}}

.feat-img-wrap img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}}

.feat-card:hover .feat-img-wrap img {{
  transform: scale(1.03);
}}

.feat-badge {{
  position: absolute;
  top: 1rem;
  left: 1rem;
  background: var(--navy);
  color: #fff;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.35rem 0.65rem;
  border-radius: 3px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}}

.feat-info {{
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}}

.feat-info h3 {{
  font-family: 'Archivo', sans-serif;
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--ink);
  margin-bottom: 0.4rem;
}}

.feat-client {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  color: var(--blue);
  margin-bottom: 0.85rem;
}}

.feat-info p {{
  font-size: 0.95rem;
  color: var(--muted);
  line-height: 1.6;
  margin-bottom: 1.25rem;
}}

.feat-meta-row {{
  display: flex;
  gap: 1.5rem;
  margin-top: auto;
  padding-top: 1rem;
  border-top: 1px solid var(--line);
}}

.feat-stat {{
  font-family: 'Archivo', sans-serif;
}}

.feat-stat b {{
  display: block;
  font-size: 1.15rem;
  color: var(--ink);
  font-weight: 800;
}}

.feat-stat span {{
  font-size: 0.72rem;
  color: var(--muted);
  text-transform: uppercase;
}}

/* ================= PROJECT REGISTER ================= */
.register-wrap {{
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-sm);
}}

.reg-toolbar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}}

.filter-group {{
  display: flex;
  gap: 0.4rem;
  background: var(--paper);
  padding: 0.3rem;
  border-radius: var(--radius-sm);
  border: 1px solid var(--line);
}}

.filter-btn {{
  padding: 0.45rem 1rem;
  font-family: 'Archivo', sans-serif;
  font-size: 0.85rem;
  font-weight: 700;
  border-radius: 3px;
  color: var(--muted);
  transition: all 0.15s ease;
}}

.filter-btn[aria-pressed="true"] {{
  background: var(--navy);
  color: #fff;
}}

.reg-search-wrap {{
  position: relative;
  min-width: 240px;
}}

.reg-search {{
  width: 100%;
  padding: 0.5rem 1rem 0.5rem 2.2rem;
  font-size: 0.85rem;
  font-family: inherit;
  border: 1px solid var(--line);
  border-radius: var(--radius-sm);
  background: var(--paper);
  color: var(--ink);
}}

.reg-search:focus {{
  outline: none;
  border-color: var(--blue);
}}

.reg-search-icon {{
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--muted);
  pointer-events: none;
}}

.reg-summary {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--blue);
  padding-block: 0.25rem;
}}

/* Ruler */
.ruler-bar {{
  display: grid;
  grid-template-columns: 60px 80px 1.4fr 1.4fr 110px 90px;
  gap: 1rem;
  align-items: center;
  padding: 0.65rem 1rem;
  background: var(--tr);
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--muted);
  text-transform: uppercase;
}}

.ruler-scale {{
  display: flex;
  justify-content: space-between;
  padding-inline: 4px;
}}

/* Ledger Rows */
.reg-list {{
  display: flex;
  flex-direction: column;
}}

.reg-row {{
  display: grid;
  grid-template-columns: 60px 80px 1.4fr 1.4fr 110px 90px;
  gap: 1rem;
  align-items: center;
  padding: 0.75rem 1rem;
  border-bottom: 1px solid var(--line);
  font-size: 0.925rem;
  transition: background 0.15s ease;
  cursor: pointer;
}}

.reg-row:hover {{
  background: var(--paper);
}}

.reg-ref {{
  font-family: 'JetBrains Mono', monospace;
  font-weight: 600;
  color: var(--muted);
  font-size: 0.8rem;
}}

.reg-thumb-wrap {{
  width: 70px;
  height: 48px;
  border-radius: var(--radius-sm);
  overflow: hidden;
  background: #000;
}}

.reg-thumb-wrap img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
}}

.reg-title b {{
  color: var(--ink);
  font-size: 0.95rem;
  display: block;
}}

.reg-title small {{
  font-size: 0.78rem;
  color: var(--muted);
}}

.reg-bar-wrap {{
  position: relative;
  background: rgba(0, 0, 0, 0.04);
  height: 12px;
  border-radius: 6px;
  overflow: hidden;
}}

:root[data-theme="dark"] .reg-bar-wrap {{
  background: rgba(255, 255, 255, 0.08);
}}

.reg-bar-fill {{
  height: 100%;
  background: var(--blue);
  border-radius: 6px;
  transition: width 0.4s ease;
}}

.reg-bar-fill.bridge {{
  background: var(--red);
}}

.reg-cost {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--muted);
  text-align: right;
}}

.reg-value {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.88rem;
  font-weight: 700;
  text-align: right;
  color: var(--ink);
}}

.reg-footnote {{
  margin-top: 1.25rem;
  font-size: 0.82rem;
  color: var(--muted);
  font-style: italic;
}}

/* ================= GALLERY (SITE RECORDS) ================= */
.gallery-grid {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}}

.plate-card {{
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  text-align: left;
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  cursor: pointer;
  padding: 0;
}}

.plate-card:hover {{
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: var(--blue);
}}

.plate-img-wrap {{
  height: 190px;
  overflow: hidden;
  position: relative;
  background: #000;
}}

.plate-img-wrap img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}}

.plate-card:hover .plate-img-wrap img {{
  transform: scale(1.05);
}}

.plate-overlay {{
  position: absolute;
  top: 0.65rem;
  left: 0.65rem;
  background: rgba(5, 14, 35, 0.85);
  backdrop-filter: blur(4px);
  color: #fff;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.68rem;
  font-weight: 700;
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  letter-spacing: 0.05em;
}}

.plate-body {{
  padding: 1rem;
}}

.plate-body h4 {{
  font-family: 'Archivo', sans-serif;
  font-size: 0.95rem;
  font-weight: 750;
  color: var(--ink);
  line-height: 1.35;
  margin-bottom: 0.25rem;
}}

.plate-body p {{
  font-size: 0.8rem;
  color: var(--muted);
  line-height: 1.4;
}}

/* ================= CREDENTIALS ================= */
.cred-grid {{
  display: grid;
  grid-template-columns: 260px 1fr 1fr;
  gap: 3rem;
  align-items: start;
}}

.stamp-box {{
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 2rem 1.5rem;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
}}

.stamp {{
  width: 150px;
  height: 150px;
  color: var(--red);
  transform: rotate(-6deg);
  margin-bottom: 1.25rem;
  transition: transform 0.3s ease;
}}

.stamp:hover {{
  transform: rotate(0deg) scale(1.03);
}}

.stamp text {{
  text-anchor: middle;
  font-family: 'Archivo', sans-serif;
  font-weight: 800;
  fill: currentColor;
}}

.stamp-caption {{
  font-family: 'Archivo', sans-serif;
  font-weight: 750;
  font-size: 0.95rem;
  color: var(--ink);
  margin-bottom: 0.25rem;
}}

.stamp-sub {{
  font-size: 0.8rem;
  color: var(--muted);
}}

.cred-col h3 {{
  font-family: 'Archivo', sans-serif;
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--ink);
  margin-bottom: 1.25rem;
  display: flex;
  align-items: center;
  gap: 0.65rem;
}}

.cred-col h3 svg {{
  width: 22px;
  height: 22px;
  stroke: var(--blue);
  fill: none;
}}

.chips-wrap {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-bottom: 1.5rem;
}}

.chip {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 0.45rem 0.85rem;
  background: var(--tr);
  border: 1px solid var(--line);
  border-radius: 4px;
  color: var(--ink);
}}

.cred-note {{
  font-size: 0.9rem;
  color: var(--muted);
  line-height: 1.6;
}}

.lic-list {{
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}}

.lic-list li {{
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  font-size: 0.925rem;
  color: var(--ink);
  line-height: 1.5;
  background: var(--card);
  padding: 0.75rem 1rem;
  border: 1px solid var(--line);
  border-radius: var(--radius-sm);
}}

.lic-check {{
  color: var(--blue);
  font-weight: 800;
  font-size: 1.1rem;
  line-height: 1;
}}

/* ================= CONTACT SECTION ================= */
.contact-section {{
  background: var(--navy);
  color: #ffffff;
  border-top: 1px solid var(--line);
}}

.contact-section .sec-tag {{
  color: var(--red);
}}

.contact-section h2 {{
  color: #ffffff;
}}

.contact-section .sec-lead {{
  color: #c9d8f5;
}}

.contact-grid {{
  display: grid;
  grid-template-columns: 1fr 1.25fr;
  gap: 3.5rem;
}}

.contact-info-card {{
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-lg);
  padding: 2.25rem;
}}

.info-item {{
  margin-bottom: 1.75rem;
}}

.info-item:last-child {{
  margin-bottom: 0;
}}

.info-lbl {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--red);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 0.4rem;
  display: block;
}}

.info-val {{
  font-size: 1.05rem;
  color: #eaf0fc;
  line-height: 1.5;
}}

.map-btn-row {{
  margin-top: 0.75rem;
}}

.map-pill-btn {{
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  padding: 0.4rem 0.8rem;
  background: var(--blue);
  color: #ffffff;
  border-radius: var(--radius-sm);
  transition: background 0.15s ease;
}}

.map-pill-btn:hover {{
  background: var(--blue-light);
}}

.contact-links-list {{
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}}

.contact-link-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.95rem;
  color: #ffffff;
  padding: 0.45rem 0.75rem;
  background: rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-sm);
  transition: background 0.15s ease;
}}

.contact-link-row:hover {{
  background: rgba(255, 255, 255, 0.12);
}}

.copy-btn {{
  font-size: 0.7rem;
  padding: 0.2rem 0.5rem;
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
  border-radius: 3px;
  text-transform: uppercase;
  transition: background 0.15s ease;
}}

.copy-btn:hover {{
  background: var(--blue);
}}

/* Contact Form */
.contact-form-card {{
  background: var(--card);
  color: var(--ink);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  box-shadow: var(--shadow-lg);
}}

.contact-form-card h3 {{
  font-family: 'Archivo', sans-serif;
  font-size: 1.4rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
}}

.contact-form-card p {{
  font-size: 0.925rem;
  color: var(--muted);
  margin-bottom: 1.75rem;
}}

.form-group {{
  margin-bottom: 1.25rem;
}}

.form-label {{
  display: block;
  font-family: 'Archivo', sans-serif;
  font-size: 0.85rem;
  font-weight: 700;
  margin-bottom: 0.4rem;
  color: var(--ink);
}}

.form-input, .form-select, .form-textarea {{
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid var(--line);
  border-radius: var(--radius-sm);
  font-family: inherit;
  font-size: 0.95rem;
  background: var(--paper);
  color: var(--ink);
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}}

.form-input:focus, .form-select:focus, .form-textarea:focus {{
  outline: none;
  border-color: var(--blue);
  box-shadow: 0 0 0 3px rgba(28, 94, 194, 0.15);
}}

.form-textarea {{
  min-height: 120px;
  resize: vertical;
}}

.form-feedback {{
  margin-top: 1rem;
  font-size: 0.875rem;
  line-height: 1.5;
  color: var(--blue);
}}

/* ================= PROJECT MODAL ================= */
dialog#projModal {{
  margin: auto;
  border: none;
  background: transparent;
  max-width: 90vw;
  max-height: 90vh;
  padding: 0;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
  border-radius: var(--radius-md);
  overflow: hidden;
}}

dialog#projModal::backdrop {{
  background: rgba(4, 10, 23, 0.88);
  backdrop-filter: blur(8px);
}}

.modal-card {{
  background: var(--card);
  color: var(--ink);
  border-radius: var(--radius-md);
  max-width: 780px;
  overflow: hidden;
  position: relative;
}}

.modal-head-img {{
  width: 100%;
  height: 320px;
  background: #000;
  position: relative;
}}

.modal-head-img img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
}}

.modal-close-btn {{
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(5, 14, 35, 0.75);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.25);
  z-index: 20;
  font-size: 1rem;
}}

.modal-close-btn:hover {{
  background: var(--red);
}}

.modal-body {{
  padding: 2rem;
}}

.modal-body h3 {{
  font-family: 'Archivo', sans-serif;
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--ink);
  margin-bottom: 0.35rem;
}}

.modal-meta-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-block: 1.5rem;
  padding: 1rem;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: var(--radius-sm);
}}

.meta-box b {{
  display: block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 1rem;
  color: var(--blue);
}}

.meta-box span {{
  font-size: 0.75rem;
  color: var(--muted);
  text-transform: uppercase;
}}

.modal-desc {{
  font-size: 0.95rem;
  color: var(--muted);
  line-height: 1.6;
  margin-bottom: 1rem;
}}

.modal-scope {{
  font-size: 0.85rem;
  color: var(--ink);
  background: var(--tr);
  padding: 0.75rem 1rem;
  border-radius: var(--radius-sm);
}}

/* ================= LIGHTBOX MODAL ================= */
dialog#lb {{
  margin: auto;
  border: none;
  background: transparent;
  max-width: 90vw;
  max-height: 90vh;
  padding: 0;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
  border-radius: var(--radius-md);
  overflow: hidden;
}}

dialog#lb::backdrop {{
  background: rgba(4, 10, 23, 0.88);
  backdrop-filter: blur(8px);
}}

.lightbox-content {{
  background: var(--navy-dark);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-md);
  position: relative;
  max-width: 940px;
}}

.lb-img-container {{
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #000;
  max-height: 70vh;
}}

.lb-img-container img {{
  max-width: 100%;
  max-height: 70vh;
  object-fit: contain;
}}

.lb-nav-btn {{
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: rgba(5, 14, 35, 0.75);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.25);
  transition: all 0.2s ease;
  z-index: 10;
  font-size: 1.5rem;
  line-height: 1;
}}

.lb-nav-btn:hover {{
  background: var(--blue);
}}

.lb-nav-btn.prev {{ left: 1rem; }}
.lb-nav-btn.next {{ right: 1rem; }}

.lb-close-btn {{
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(5, 14, 35, 0.75);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.25);
  z-index: 20;
  font-size: 1rem;
}}

.lb-close-btn:hover {{
  background: var(--red);
}}

.lb-caption-bar {{
  padding: 1.1rem 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  display: flex;
  justify-content: space-between;
  align-items: center;
}}

.lb-caption-text {{
  font-size: 0.95rem;
  color: #eaf0fc;
}}

.lb-counter {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  color: #a3b8e0;
}}

/* ================= FOOTER ================= */
footer {{
  background: var(--navy-dark);
  color: #ffffff;
  padding-block: 2.75rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}}

.ftr-in {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.5rem;
  font-size: 0.875rem;
  color: #8fa5cc;
}}

.ftr-brand {{
  display: flex;
  align-items: center;
  gap: 0.85rem;
}}

.ftr-brand img {{
  width: 28px;
  height: 28px;
  object-fit: contain;
}}

.ftr-motto {{
  font-family: 'Archivo', sans-serif;
  font-weight: 800;
  color: var(--red);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}}

.back-to-top {{
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: #c9d8f5;
  font-weight: 600;
  font-size: 0.85rem;
  transition: color 0.15s ease;
}}

.back-to-top:hover {{
  color: #ffffff;
}}

/* ================= RESPONSIVE ================= */
@media (max-width: 1024px) {{
  .hero-grid {{
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }}
  .stats-grid {{
    grid-template-columns: repeat(3, 1fr);
  }}
  .org-chart-grid {{
    grid-template-columns: 1fr;
  }}
  .capacity-grid {{
    grid-template-columns: repeat(2, 1fr);
  }}
  .svc-tabs-container {{
    grid-template-columns: 1fr;
  }}
  .stations-track {{
    grid-template-columns: repeat(3, 1fr);
  }}
  .stations-track::before {{
    display: none;
  }}
  .gallery-grid {{
    grid-template-columns: repeat(3, 1fr);
  }}
  .cred-grid {{
    grid-template-columns: 1fr;
    gap: 2rem;
  }}
  .contact-grid {{
    grid-template-columns: 1fr;
  }}
}}

@media (max-width: 768px) {{
  #nav {{
    display: none;
    position: fixed;
    top: 74px;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--navy-dark);
    flex-direction: column;
    padding: 2.5rem 2rem;
    gap: 1.75rem;
    z-index: 99;
  }}
  #nav.open {{
    display: flex;
  }}
  .menu-btn {{
    display: inline-flex;
  }}
  .about-grid {{
    grid-template-columns: 1fr;
    gap: 2rem;
  }}
  .featured-grid {{
    grid-template-columns: 1fr;
  }}
  .gallery-grid {{
    grid-template-columns: repeat(2, 1fr);
  }}
  .svc-grid-view {{
    grid-template-columns: 1fr;
  }}
  .stations-track {{
    grid-template-columns: repeat(2, 1fr);
  }}
  .stats-grid {{
    grid-template-columns: repeat(2, 1fr);
  }}
  .ruler-bar, .reg-row {{
    grid-template-columns: 50px 65px 1.2fr 1fr 70px;
  }}
  .ruler-bar > div:nth-child(5), .reg-row > div:nth-child(5) {{
    display: none;
  }}
}}

@media (max-width: 480px) {{
  .gallery-grid {{
    grid-template-columns: 1fr;
  }}
  .stations-track {{
    grid-template-columns: 1fr;
  }}
  .stats-grid {{
    grid-template-columns: 1fr;
  }}
  .capacity-grid {{
    grid-template-columns: 1fr;
  }}
  .ruler-bar, .reg-row {{
    grid-template-columns: 60px 1fr 70px;
  }}
  .ruler-bar > div:nth-child(2), .ruler-bar > div:nth-child(4), .ruler-bar > div:nth-child(5),
  .reg-row > div:nth-child(2), .reg-row > div:nth-child(4), .reg-row > div:nth-child(5) {{
    display: none;
  }}
}}
</style>
</head>
<body>

<!-- Header -->
<header id="hd">
  <div class="wrap bar-in">
    <a href="#top" class="brand" aria-label="Axulal Consulting Engineers PLC Home">
      <img src="assets/logo.png" alt="Axulal Official Logo" class="brand-logo-img">
      <span>Axulal Engineers<span class="cat-pill">CAT-1</span></span>
    </a>

    <nav id="nav" aria-label="Main Navigation">
      <a href="#about">About</a>
      <a href="#structure">Structure</a>
      <a href="#services">Services</a>
      <a href="#stations">Process</a>
      <a href="#projects">Projects</a>
      <a href="#records">Site Records</a>
      <a href="#credentials">Credentials</a>
      <a href="#contact">Contact</a>
    </nav>

    <div class="hd-actions">
      <!-- Theme Switcher -->
      <button class="theme-btn" id="themeToggle" aria-label="Toggle light or dark theme" title="Toggle theme">
        <svg id="themeIcon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
          <line x1="1" y1="12" x2="3" y2="12"></line>
          <line x1="21" y1="12" x2="23" y2="12"></line>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>
      </button>

      <a href="#contact" class="btn" style="padding: 0.55rem 1.1rem; font-size: 0.82rem;">Request Proposal</a>

      <button class="menu-btn" id="menuToggle" aria-expanded="false" aria-controls="nav" aria-label="Toggle Navigation Menu">
        <svg viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
    </div>
  </div>
</header>

<main id="top">

  <!-- ================= HERO ================= -->
  <section class="hero" style="padding-top: 3.5rem;">
    <div class="wrap">
      <div class="hero-grid">
        <div>
          <div class="badge-row">
            <span class="reg-badge">License OR/16/08/02/08/000000333</span>
            <span class="reg-badge">Federal Ministry of Construction · Cat-1</span>
            <span class="motto-tag">Conquering Possibilities!!</span>
          </div>

          <h1>Roads and bridges, engineered from first survey to final handover.</h1>

          <p class="hero-lead">
            Premier Category-1 Highway and Bridge consultants based in Addis Ababa. Since 2011, Axulal has engineered, tendered, and supervised over 128 km of vital transportation corridors and bridges connecting communities across Oromia and Ethiopia.
          </p>

          <div class="cta-group">
            <a href="#projects" class="btn">Explore Projects (12)</a>
            <a href="#contact" class="btn ghost">Request a Proposal</a>
          </div>

          <div class="hero-links-row">
            <a href="tel:+251111582107" class="direct-call">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
              Office: +251 111 582 107
            </a>

            <a href="https://maps.app.goo.gl/FPMrBogev6Ws1FoJ6" target="_blank" rel="noopener noreferrer" class="hero-map-link">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
              Katekse Bldg, Adwa Square
            </a>
          </div>
        </div>

        <!-- Technical Showcase Switcher (Elevation CAD Profile + Active Compaction Photo) -->
        <div class="hero-visual-card">
          <div class="visual-topbar">
            <span>ENGINEERING SPECIFICATION</span>
            <div class="visual-tabs">
              <button class="v-tab-btn active" id="btnShowProfile">CAD Profile</button>
              <button class="v-tab-btn" id="btnShowPhoto">Site Photo</button>
            </div>
          </div>

          <!-- Tab Panel 1: Longitudinal Road Profile CAD Drawing -->
          <div class="visual-panel active" id="panelProfile">
            <div class="prof-svg-wrap">
              <svg viewBox="0 0 1200 300" preserveAspectRatio="xMidYMax slice" role="img" aria-label="Longitudinal road profile crossing a river on a 24-metre girder bridge">
                <path class="g" d="M0 205C110 185 210 225 330 210S470 175 520 200L545 245L675 245L700 200C780 170 900 215 1010 195S1130 180 1200 185"/>
                <path class="r" d="M0 175C150 165 300 185 520 170L700 170C900 175 1050 160 1200 165"/>
                <g>
                  <path class="b" d="M520 170v10h180v-10M520 180v36M700 180v36M570 180v-10M610 180v-10M650 180v-10"/>
                </g>
                <path class="t" d="M520 170V282M700 170V282M520 262H700M520 254v16M700 254v16"/>
                <circle class="t" cx="900" cy="190" r="9"/>
                <text x="610" y="252" text-anchor="middle">24 m span girder bridge</text>
                <text x="40" y="150">Finished Road Level (Red)</text>
                <text x="40" y="240">Existing Ground (Dashed)</text>
                <text x="900" y="226" text-anchor="middle">Hydraulic Culvert</text>
                <g class="t">
                  <path d="M60 288v-8M360 288v-8M520 288v-8M700 288v-8M960 288v-8M1160 288v-8"/>
                </g>
                <text x="60" y="298" text-anchor="middle">STA 0+000</text>
                <text x="360" y="298" text-anchor="middle">STA 1+000</text>
                <text x="520" y="298" text-anchor="middle">STA 1+800</text>
                <text x="700" y="298" text-anchor="middle">STA 2+000</text>
                <text x="960" y="298" text-anchor="middle">STA 3+000</text>
                <text x="1160" y="298" text-anchor="middle">STA 4+000</text>
              </svg>
            </div>
          </div>

          <!-- Tab Panel 2: Field Site Photo -->
          <div class="visual-panel" id="panelPhoto">
            <div class="hero-photo-wrap">
              <img src="assets/gallery/plate_01_compaction.jpg" alt="Heavy vibratory road roller compacting gravel sub-base on an Axulal road project site" loading="eager">
              <div class="photo-badge">
                <b>Field Record:</b> Heavy vibratory compaction on classified gravel alignment, Oromia.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Credibility 5-Stat Banner -->
      <div class="stats-banner">
        <div class="stats-grid">
          <div class="stat-item">
            <span class="stat-num">2011</span>
            <span class="stat-label">Established in National URRAP</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">17+ Yrs</span>
            <span class="stat-label">Founding Leadership Experience</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">12</span>
            <span class="stat-label">Major Road & Bridge Projects</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">120+ M</span>
            <span class="stat-label">ETB Public Infrastructure Value</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">Cat. 1</span>
            <span class="stat-label">Ministry of Construction Grade</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= ABOUT SECTION ================= -->
  <section id="about">
    <div class="wrap">
      <div class="sec-head">
        <span class="sec-tag">Company Background</span>
        <h2>About Axulal Consulting Engineers</h2>
      </div>

      <div class="about-grid">
        <div class="about-body">
          <p class="big">
            Established in 2011 under Business License Number OR/16/08/02/08/000000333 as part of Ethiopia's national Universal Rural Roads Access Program (URRAP), Axulal has developed into a premier Category-1 Highway and Bridge consulting firm.
          </p>
          <p>
            Two senior professional engineers and one senior land surveyor—each with over fifteen years of rigorous field, structural, and materials experience—founded the firm. Our General Manager brings more than 17 years of specialized expertise in road and infrastructure development throughout Ethiopia.
          </p>
          <p>
            We manage the entire lifecycle of civil transportation works: from preliminary reconnaissance and topographic surveys through detailed structural design, tender dossiers, construction supervision, and final contract administration. Built on a debt-free capital foundation of over 558,000.00 ETB, the firm maintains strong financial stability, owning its complete fleet of field inspection vehicles, high-precision survey instruments, and cutting-edge engineering workstations.
          </p>
        </div>

        <div class="vm-cards">
          <div class="vm-box vision">
            <h3>Our Vision</h3>
            <p>To push the default standards in the country, creating innovative, green, environmentally responsive, participatory, cost-effective, and sustainable modern infrastructure solutions utilizing locally available resources.</p>
          </div>
          <div class="vm-box mission">
            <h3>Our Mission</h3>
            <p>To deliver quality consulting services exceeding client expectations while adhering to the highest standards of technical and individual excellence through continuous training, adding value, and nurturing talent.</p>
          </div>
        </div>
      </div>

      <!-- Core Values (From PDF Page 4) -->
      <div class="facts-3" style="margin-bottom: 3.5rem;">
        <div class="fact-card">
          <span class="fact-idx">CORE VALUE 01</span>
          <h3>Excellence & Resilience</h3>
          <p>We are resilient and persistent in tackling challenging terrain and setting higher performance benchmarks that help us excel in every way meaningful to our clients, communities, and partners.</p>
        </div>
        <div class="fact-card">
          <span class="fact-idx">CORE VALUE 02</span>
          <h3>Quality Assurance</h3>
          <p>Committed to continually improving our people, processes, and products. Quality conscious oversight ensures strict compliance with national design manuals and zero tolerance for defect.</p>
        </div>
        <div class="fact-card">
          <span class="fact-idx">CORE VALUE 03</span>
          <h3>Client & Community Value</h3>
          <p>We add direct value to every project through innovative solutions, ensuring full consultation and active participation of target beneficiaries—women and men, youth and elders alike.</p>
        </div>
      </div>

      <!-- Company Organizational Structure (From PDF Page 6) -->
      <div class="org-chart-section" id="structure">
        <div class="org-chart-grid">
          <div class="org-chart-text">
            <span class="sec-tag">Corporate Governance</span>
            <h3>Organization & Departmental Structure</h3>
            <p>
              Axulal Consulting Engineers PLC is led by an autonomous General Manager reporting directly to the Shareholders, supervising three dedicated operational divisions to ensure seamless quality governance across all active sites.
            </p>
            <div class="dept-list">
              <div class="dept-item">
                <span class="dept-bullet"></span>
                <span><strong>Design Department:</strong> Geometrics, structural bridge modeling, hydraulics & CAD drafting.</span>
              </div>
              <div class="dept-item">
                <span class="dept-bullet"></span>
                <span><strong>Contract Administration Department:</strong> Cost estimating, BOQ, tender dossiers & bid appraisal.</span>
              </div>
              <div class="dept-item">
                <span class="dept-bullet"></span>
                <span><strong>Administration & Finance:</strong> Logistics, human resources, accounting & statutory compliance.</span>
              </div>
            </div>
          </div>

          <div class="org-chart-img-wrap">
            <img src="assets/org_chart.png" alt="Axulal Organizational Hierarchy Chart" loading="lazy">
          </div>
        </div>

        <!-- Technical Facilities & Equipment (From PDF Page 7) -->
        <div class="capacity-grid">
          <div class="cap-card">
            <span class="cap-num">35</span>
            <span class="cap-label">Engineering Computers</span>
            <span class="cap-desc">25 Dell Workstations + 10 Field Laptops</span>
          </div>
          <div class="cap-card">
            <span class="cap-num">2</span>
            <span class="cap-label">Wide-Format Plotters</span>
            <span class="cap-desc">Dedicated engineering blueprint output</span>
          </div>
          <div class="cap-card">
            <span class="cap-num">2</span>
            <span class="cap-label">4x4 Field Vehicles</span>
            <span class="cap-desc">Dedicated site inspection & mobile survey</span>
          </div>
          <div class="cap-card">
            <span class="cap-num">100%</span>
            <span class="cap-label">Debt-Free Stability</span>
            <span class="cap-desc">Sound capital standing & zero bank loans</span>
          </div>
        </div>

        <!-- Software Suite (From PDF Page 10) -->
        <div class="software-bar">
          <span class="software-title">Engineering Software:</span>
          <div class="software-chips">
            <span class="sw-chip">AutoCAD</span>
            <span class="sw-chip">Bentley InRoads</span>
            <span class="sw-chip">Eagle Point</span>
            <span class="sw-chip">Autodesk Revit</span>
            <span class="sw-chip">Graphisoft ArchiCAD</span>
            <span class="sw-chip">CSI SAP2000</span>
            <span class="sw-chip">CSI ETABS</span>
            <span class="sw-chip">3Ds Max</span>
            <span class="sw-chip">MS Office Suite</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= SERVICES SECTION ================= -->
  <section id="services" class="alt">
    <div class="wrap">
      <div class="svc-nav-header">
        <div>
          <span class="sec-tag">Core Capabilities</span>
          <h2>What We Do</h2>
          <p class="sec-lead">Highway and bridge engineering is our specialty, backed by the comprehensive field studies, material surveys, and resident supervision required for long-term durability.</p>
        </div>
        <div class="view-toggle">
          <button id="btnTabView" class="active" title="Switch to tabbed explorer">Interactive Tabs</button>
          <button id="btnGridView" title="Switch to full grid view">Overview Grid</button>
        </div>
      </div>

      <!-- Tabbed Explorer View -->
      <div class="svc-tabs-container" id="svcTabView">
        <div class="svc-tablist" role="tablist" aria-label="Axulal Engineering Services">
          <button class="svc-tab-btn" role="tab" aria-selected="true" data-tab="0">
            <svg viewBox="0 0 44 44"><path d="M4 36h36M8 36c4-14 10-18 14-18s10 4 14 18M12 36V24M32 36V24"/></svg>
            <span>Road & Bridge Engineering</span>
          </button>
          <button class="svc-tab-btn" role="tab" aria-selected="false" data-tab="1">
            <svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="14"/><path d="M22 4v8M22 32v8M4 22h8M32 22h8"/></svg>
            <span>Studies & Surveys</span>
          </button>
          <button class="svc-tab-btn" role="tab" aria-selected="false" data-tab="2">
            <svg viewBox="0 0 44 44"><path d="M8 6h22l6 6v26H8zM14 18h16M14 25h16M14 32h10"/></svg>
            <span>Tender & Contract</span>
          </button>
          <button class="svc-tab-btn" role="tab" aria-selected="false" data-tab="3">
            <svg viewBox="0 0 44 44"><path d="M6 38l12-14 8 6 12-20M30 10h8v8"/></svg>
            <span>Supervision & Planning</span>
          </button>
        </div>

        <div class="svc-panel" id="svcPanel" role="tabpanel" aria-live="polite">
          <!-- Populated by JS -->
        </div>
      </div>

      <!-- Grid Overview View -->
      <div class="svc-grid-view" id="svcGridView">
        <div class="svc-grid-card">
          <svg viewBox="0 0 44 44"><path d="M4 36h36M8 36c4-14 10-18 14-18s10 4 14 18M12 36V24M32 36V24"/></svg>
          <h3>Road & Bridge Engineering</h3>
          <p>Our core discipline: geometric road alignments, reinforced concrete bridges, and supporting infrastructure.</p>
          <ul>
            <li>• Classified Highway Engineering</li>
            <li>• Reinforced Concrete Girder Bridges</li>
            <li>• Box & Pipe Culvert Hydraulics</li>
            <li>• Associated Building & Civil Works</li>
          </ul>
        </div>
        <div class="svc-grid-card">
          <svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="14"/><path d="M22 4v8M22 32v8M4 22h8M32 22h8"/></svg>
          <h3>Studies & Surveys</h3>
          <p>Rigorous groundwork that guarantees structural feasibility and prevents costly alignment revisions.</p>
          <ul>
            <li>• High-Precision Topographic Surveys</li>
            <li>• Soil & Geotechnical Investigations</li>
            <li>• Pre-Investment Feasibility Studies</li>
            <li>• Quarry & Material Resource Scouting</li>
          </ul>
        </div>
        <div class="svc-grid-card">
          <svg viewBox="0 0 44 44"><path d="M8 6h22l6 6v26H8zM14 18h16M14 25h16M14 32h10"/></svg>
          <h3>Tender & Contract</h3>
          <p>Transparent bidding dossiers, fair evaluations, and FIDIC/PPA contract administration.</p>
          <ul>
            <li>• Accurate BOQ & Engineer's Estimates</li>
            <li>• Standard Tender Document Preparation</li>
            <li>• Technical & Financial Bid Evaluation</li>
            <li>• Contractual Dispute & Claims Review</li>
          </ul>
        </div>
        <div class="svc-grid-card">
          <svg viewBox="0 0 44 44"><path d="M6 38l12-14 8 6 12-20M30 10h8v8"/></svg>
          <h3>Supervision & Planning</h3>
          <p>Daily on-site resident oversight, material testing, and environmental compliance.</p>
          <ul>
            <li>• Full Resident Construction Supervision</li>
            <li>• Laboratory Materials Quality Control</li>
            <li>• Environmental & Social Monitoring (ESIA)</li>
            <li>• Watershed Management & Regional Planning</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= HOW A PROJECT RUNS (STATIONS) ================= -->
  <section id="stations">
    <div class="wrap">
      <div class="sec-head">
        <span class="sec-tag">Project Lifecycle</span>
        <h2>How a Project Runs</h2>
        <p class="sec-lead">Six defined chainage milestones from preliminary field reconnaissance to final employer handover.</p>
      </div>

      <ol class="stations-track">
        <li class="station-node">
          <span class="sta-pin">1</span>
          <span class="sta-tag">STA 0+000</span>
          <h3>Study</h3>
          <p>Route reconnaissance, socio-economic community needs assessment, and technical feasibility scoping.</p>
        </li>
        <li class="station-node">
          <span class="sta-pin">2</span>
          <span class="sta-tag">STA 0+200</span>
          <h3>Survey</h3>
          <p>Detailed topographic traverse, geotechnical boreholes, soil classification, and hydrological modeling.</p>
        </li>
        <li class="station-node">
          <span class="sta-pin">3</span>
          <span class="sta-tag">STA 0+400</span>
          <h3>Design</h3>
          <p>Geometric alignment, structural bridge calculations, hydraulic structures, and complete working drawings.</p>
        </li>
        <li class="station-node">
          <span class="sta-pin">4</span>
          <span class="sta-tag">STA 0+600</span>
          <h3>Tender</h3>
          <p>Tender dossiers, bill of quantities (BOQ), confidential cost estimates, and competitive bid evaluation.</p>
        </li>
        <li class="station-node">
          <span class="sta-pin">5</span>
          <span class="sta-tag">STA 0+800</span>
          <h3>Supervision</h3>
          <p>Resident engineering, strict on-site quality control, compaction testing, and progress certification.</p>
        </li>
        <li class="station-node">
          <span class="sta-pin">6</span>
          <span class="sta-tag">STA 1+000</span>
          <h3>Handover</h3>
          <p>Defects liability monitoring, as-built documentation, final financial close-out, and official commissioning.</p>
        </li>
      </ol>
    </div>
  </section>

  <!-- ================= FEATURED PROJECTS & PROJECT REGISTER ================= -->
  <section id="projects" class="alt">
    <div class="wrap">
      <div class="sec-head">
        <span class="sec-tag">Track Record</span>
        <h2>Selected Projects & Project Register</h2>
        <p class="sec-lead">Every infrastructure project listed below was successfully designed, engineered, and supervised for the Oromiya Road Authority (ORA).</p>
      </div>

      <!-- Two Flagship Showcases -->
      <div class="featured-grid">
        <div class="feat-card">
          <div class="feat-img-wrap">
            <img src="assets/projects/proj_6_awash_bridge.jpg" alt="Awash River 24m Girder Bridge Construction" loading="lazy">
            <span class="feat-badge">Flagship Bridge · 10.13M ETB</span>
          </div>
          <div class="feat-info">
            <h3>Awash River Bridge Project</h3>
            <span class="feat-client">Client: Oromiya Road Authority (ORA) · Cost: 10,126,088.28 ETB</span>
            <p>24-meter single-span reinforced concrete girder bridge over the Awash River. Axulal provided comprehensive feasibility analysis, hydraulic sizing, structural design, tender document preparation, full site supervision, and contract administration.</p>
            <div class="feat-meta-row">
              <div class="feat-stat">
                <b>24.0 m</b>
                <span>Girder Span</span>
              </div>
              <div class="feat-stat">
                <b>Full Run</b>
                <span>Design + Supervision</span>
              </div>
              <div class="feat-stat">
                <b>Delivered</b>
                <span>Status</span>
              </div>
            </div>
          </div>
        </div>

        <div class="feat-card">
          <div class="feat-img-wrap">
            <img src="assets/projects/proj_1_ginchi_danisa.jpg" alt="Ginchi-Danisa 15.5km Gravel Road" loading="lazy">
            <span class="feat-badge">Classified Highway · 14.66M ETB</span>
          </div>
          <div class="feat-info">
            <h3>Ginchi-Danisa Gravel Road</h3>
            <span class="feat-client">Client: Oromiya Road Authority (ORA) · Cost: 14,660,079.54 ETB</span>
            <p>15.5 km of 6.0-meter wide DC-2 standard gravel highway crossing steep mountainous terrain. Included complex rock cuts, masonry drainage retaining structures, box culverts, and full supervision from initial groundbreaking through final handover.</p>
            <div class="feat-meta-row">
              <div class="feat-stat">
                <b>15.5 km</b>
                <span>Total Length</span>
              </div>
              <div class="feat-stat">
                <b>DC-2</b>
                <span>Road Class</span>
              </div>
              <div class="feat-stat">
                <b>Delivered</b>
                <span>Status</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Master Project Register Table -->
      <div class="register-wrap">
        <div class="reg-toolbar">
          <div class="filter-group" role="group" aria-label="Filter Project Register">
            <button class="filter-btn" aria-pressed="true" data-filter="all">All Projects (12)</button>
            <button class="filter-btn" aria-pressed="false" data-filter="road">Classified Roads (10)</button>
            <button class="filter-btn" aria-pressed="false" data-filter="bridge">Bridges (2)</button>
          </div>

          <div class="reg-search-wrap">
            <svg class="reg-search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
            <input type="text" id="regSearch" class="reg-search" placeholder="Search project name..." aria-label="Search project name">
          </div>

          <div id="regSummary" class="reg-summary" aria-live="polite">
            12 projects shown · 128.8 km of classified road delivered
          </div>
        </div>

        <!-- Graduated Distance Ruler -->
        <div class="ruler-bar">
          <div>Ref</div>
          <div>Site</div>
          <div>Project Name & Scope</div>
          <div class="ruler-scale">
            <span>0 km</span>
            <span>5 km</span>
            <span>10 km</span>
            <span>15 km</span>
            <span>20 km</span>
            <span>25+ km</span>
          </div>
          <div style="text-align: right;">Contract Value</div>
          <div style="text-align: right;">Metric</div>
        </div>

        <!-- Ledger Rows -->
        <div class="reg-list" id="regList">
          <!-- Populated by JS -->
        </div>

        <p class="reg-footnote">
          * Blue bars denote road alignment length in kilometres. Red bars denote girder bridge span in metres. Click any project row to view full project specifications and field photography.
        </p>
      </div>
    </div>
  </section>

  <!-- ================= SITE RECORDS & GALLERY (12 REAL PHOTOS) ================= -->
  <section id="records">
    <div class="wrap">
      <div class="sec-head">
        <span class="sec-tag">Field Documentation</span>
        <h2>Site Records & Field Evidence</h2>
        <p class="sec-lead">Select any plate to examine high-resolution field photographs of our earthworks, structural concrete, hydraulic drainage, and finished surfaces.</p>
      </div>

      <div class="gallery-grid" id="galleryGrid">
        <!-- Populated by JS or template -->
      </div>
    </div>
  </section>

  <!-- ================= CREDENTIALS ================= -->
  <section id="credentials" class="alt">
    <div class="wrap">
      <div class="sec-head">
        <span class="sec-tag">Official Authority</span>
        <h2>Credentials & Professional Licenses</h2>
        <p class="sec-lead">Certified and fully accredited to design, engineer, and supervise the highest category of highway and structural bridge infrastructure in Ethiopia.</p>
      </div>

      <div class="cred-grid">
        <!-- SVG Stamp -->
        <div class="stamp-box">
          <svg viewBox="0 0 170 170" class="stamp" role="img" aria-label="Official Category 1 Highway and Bridge Consultant Stamp">
            <circle cx="85" cy="85" r="80" fill="none" stroke="currentColor" stroke-width="4"/>
            <circle cx="85" cy="85" r="68" fill="none" stroke="currentColor" stroke-width="1.5"/>
            <text x="85" y="58" font-size="14">CATEGORY</text>
            <text x="85" y="112" font-size="62">1</text>
            <text x="85" y="134" font-size="11">HIGHWAY & BRIDGE</text>
          </svg>
          <div class="stamp-caption">Highest National Grade</div>
          <div class="stamp-sub">Ministry of Urban Development & Construction</div>
        </div>

        <!-- Standards -->
        <div class="cred-col">
          <h3>
            <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" stroke="currentColor" stroke-width="2"/></svg>
            Design Codes & Standards
          </h3>
          <p class="cred-note" style="margin-bottom: 1.25rem;">
            Every road, girder bridge, and drainage structure engineered by Axulal complies rigorously with the following national and international specifications:
          </p>
          <div class="chips-wrap">
            <span class="chip">ERA Manuals</span>
            <span class="chip">AASHTO Guidelines</span>
            <span class="chip">Bat Coda</span>
            <span class="chip">EBCS Standards</span>
            <span class="chip">Eurocodes</span>
            <span class="chip">Ethiopian Standards Code (ESCP)</span>
          </div>
          <p class="cred-note">
            From DC-1 feeder tracks up to multi-lane trunk highways, geometric parameters, pavement thicknesses, and hydraulic scour depths adhere strictly to ERA geometric design guidelines and hydrological frequency parameters.
          </p>
        </div>

        <!-- Licenses List -->
        <div class="cred-col">
          <h3>
            <svg viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="2"/></svg>
            Statutory Registrations
          </h3>
          <ul class="lic-list">
            <li>
              <span class="lic-check">✓</span>
              <span><strong>Federal Ministry of Construction:</strong> Category-1 Highway and Bridge Consultant License</span>
            </li>
            <li>
              <span class="lic-check">✓</span>
              <span><strong>Principal Trade License:</strong> Business License No. <code>OR/16/08/02/08/000000333</code></span>
            </li>
            <li>
              <span class="lic-check">✓</span>
              <span><strong>Addis Ababa Trade & Industry Bureau:</strong> Principal Registration Certificate</span>
            </li>
            <li>
              <span class="lic-check">✓</span>
              <span><strong>Ministry of Revenues:</strong> Value Added Tax (VAT) Registration No. <code>4787140032</code></span>
            </li>
            <li>
              <span class="lic-check">✓</span>
              <span><strong>Federal Tax Authority:</strong> Taxpayer Identification Number (TIN) <code>0023131810</code></span>
            </li>
            <li>
              <span class="lic-check">✓</span>
              <span><strong>Public Procurement Authority (FPPA):</strong> Registered Consultant on Suppliers List</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= CONTACT SECTION ================= -->
  <section id="contact" class="contact-section">
    <div class="wrap">
      <div class="sec-head">
        <span class="sec-tag">Initiate a Project</span>
        <h2>Start a Project With Us</h2>
        <p class="sec-lead">Tell us about your upcoming infrastructure program, survey scope, or supervision requirements. Our engineering team responds to every inquiry promptly.</p>
      </div>

      <div class="contact-grid">
        <!-- Direct Contacts -->
        <div class="contact-info-card">
          <div class="info-item">
            <span class="info-lbl">Headquarters & Office</span>
            <div class="info-val">
              Katekse Building, 3rd Floor, House No. 712/3A<br>
              Adwa Square (Near Adwa Bridge)<br>
              Yeka Sub City, Woreda 07<br>
              Addis Ababa, Ethiopia
            </div>
            <div class="map-btn-row">
              <a href="https://maps.app.goo.gl/FPMrBogev6Ws1FoJ6" target="_blank" rel="noopener noreferrer" class="map-pill-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
                View on Google Maps
              </a>
            </div>
          </div>

          <div class="info-item">
            <span class="info-lbl">Postal Address</span>
            <div class="info-val">P. O. Box 32932, Addis Ababa, Ethiopia</div>
          </div>

          <div class="info-item">
            <span class="info-lbl">Direct Telephone Lines</span>
            <div class="contact-links-list">
              <div class="contact-link-row">
                <a href="tel:+251111582107">Office: +251 111 582 107</a>
                <button class="copy-btn" onclick="copyText('+251111582107', this)">Copy</button>
              </div>
              <div class="contact-link-row">
                <a href="tel:+251911216472">Mobile: +251 911 216 472</a>
                <button class="copy-btn" onclick="copyText('+251911216472', this)">Copy</button>
              </div>
              <div class="contact-link-row">
                <a href="tel:+251930077347">Mobile: +251 930 077 347</a>
                <button class="copy-btn" onclick="copyText('+251930077347', this)">Copy</button>
              </div>
              <div class="contact-link-row">
                <span>Fax: +251 111 262 888</span>
                <button class="copy-btn" onclick="copyText('+251111262888', this)">Copy</button>
              </div>
            </div>
          </div>

          <div class="info-item">
            <span class="info-lbl">Electronic Mail</span>
            <div class="contact-link-row">
              <a href="mailto:axulalconsulting@gmail.com">axulalconsulting@gmail.com</a>
              <button class="copy-btn" onclick="copyText('axulalconsulting@gmail.com', this)">Copy</button>
            </div>
          </div>
        </div>

        <!-- Interactive RFP Form -->
        <div class="contact-form-card">
          <h3>Request a Proposal / Send an Inquiry</h3>
          <p>Complete the form below to connect directly with our chief civil engineering team.</p>

          <form id="contactForm">
            <div class="form-group">
              <label for="formName" class="form-label">Your Name / Organization *</label>
              <input type="text" id="formName" class="form-input" placeholder="e.g. Ato Bekele Tadesse / Regional Roads Authority" required>
            </div>

            <div class="form-group">
              <label for="formContact" class="form-label">Email or Phone Number *</label>
              <input type="text" id="formContact" class="form-input" placeholder="e.g. bekele@organization.gov.et or +251 9..." required>
            </div>

            <div class="form-group">
              <label for="formService" class="form-label">Service Required</label>
              <select id="formService" class="form-select">
                <option value="Road Engineering & Design">Road Engineering & Detailed Design</option>
                <option value="Bridge Engineering & Hydraulics">Bridge Engineering & Structural Design</option>
                <option value="Topographic Survey & Soil Investigation">Topographic Survey & Soil Investigation</option>
                <option value="Tender Preparation & Bid Evaluation">Tender Preparation & Bid Evaluation</option>
                <option value="Construction Supervision & Quality Control">Construction Supervision & Quality Control</option>
                <option value="Feasibility Study & Environmental Assessment">Feasibility Study & Environmental Assessment</option>
                <option value="Other Consultation">Other Engineering Consultation</option>
              </select>
            </div>

            <div class="form-group">
              <label for="formMessage" class="form-label">Project Scope / Inquiry Details *</label>
              <textarea id="formMessage" class="form-textarea" placeholder="Describe project location, estimated road length (km) or bridge span (m), and required services..." required></textarea>
            </div>

            <button type="submit" class="btn" style="width: 100%;">Send Proposal Request</button>

            <div id="formFeedback" class="form-feedback" aria-live="polite"></div>
          </form>
        </div>
      </div>
    </div>
  </section>

</main>

<!-- Footer -->
<footer>
  <div class="wrap ftr-in">
    <div class="ftr-brand">
      <img src="assets/logo.png" alt="Axulal Logo">
      <span>© 2026 Axulal Consulting Engineers PLC. Category-1 Highway & Bridge Consultants.</span>
    </div>

    <div class="ftr-motto">Conquering Possibilities!!</div>

    <a href="#top" class="back-to-top">
      Back to Top
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 15l-6-6-6 6"/></svg>
    </a>
  </div>
</footer>

<!-- Project Detail Modal -->
<dialog id="projModal" aria-label="Project Detail View">
  <div class="modal-card">
    <button class="modal-close-btn" id="modalClose" aria-label="Close project preview">✕</button>
    <div class="modal-head-img">
      <img id="modalImg" src="" alt="">
    </div>
    <div class="modal-body">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.25rem; flex-wrap: wrap; gap: 0.5rem;">
        <h3 id="modalTitle"></h3>
        <span id="modalRef" style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: var(--blue);"></span>
      </div>
      <div id="modalClient" style="font-size: 0.85rem; color: var(--blue); margin-bottom: 0.75rem;"></div>
      <p id="modalDesc" class="modal-desc"></p>
      
      <div class="modal-meta-grid">
        <div class="meta-box">
          <b id="modalCost"></b>
          <span>Project Cost (ETB)</span>
        </div>
        <div class="meta-box">
          <b id="modalMetric"></b>
          <span>Length / Span</span>
        </div>
        <div class="meta-box">
          <b id="modalStandard"></b>
          <span>Standard</span>
        </div>
      </div>

      <div class="modal-scope">
        <strong>Services Rendered:</strong> <span id="modalScope"></span>
      </div>
    </div>
  </div>
</dialog>

<!-- Lightbox Modal Dialog -->
<dialog id="lb" aria-label="Field Photo Viewer">
  <div class="lightbox-content">
    <button class="lb-close-btn" id="lbClose" aria-label="Close photo preview">✕</button>
    <button class="lb-nav-btn prev" id="lbPrev" aria-label="Previous photo">‹</button>
    <button class="lb-nav-btn next" id="lbNext" aria-label="Next photo">›</button>

    <div class="lb-img-container">
      <img id="lbImg" src="" alt="">
    </div>

    <div class="lb-caption-bar">
      <div id="lbCaption" class="lb-caption-text"></div>
      <div id="lbCounter" class="lb-counter"></div>
    </div>
  </div>
</dialog>

<!-- Client JavaScript -->
<script>
const PROJECTS = {projects_json};
const GALLERY = {gallery_json};

// Render Gallery Grid
const galleryGrid = document.getElementById("galleryGrid");
GALLERY.forEach((g, idx) => {{
  const btn = document.createElement("button");
  btn.className = "plate-card";
  btn.setAttribute("data-idx", idx);
  btn.setAttribute("aria-label", "Open " + g.plate + ": " + g.title);
  btn.innerHTML = `
    <div class="plate-img-wrap">
      <img src="${{g.img}}" alt="${{g.title}}" loading="lazy">
      <span class="plate-overlay">${{g.plate}}</span>
    </div>
    <div class="plate-body">
      <h4>${{g.title}}</h4>
      <p>${{g.desc}}</p>
    </div>
  `;
  btn.onclick = () => openLightbox(idx);
  galleryGrid.appendChild(btn);
}});

// Render Project Register
const regList = document.getElementById("regList");
const regSummary = document.getElementById("regSummary");
const regSearch = document.getElementById("regSearch");
let currentFilter = "all";

function renderProjects() {{
  const query = regSearch.value.trim().toLowerCase();
  regList.innerHTML = "";
  let totalKm = 0;
  let count = 0;

  PROJECTS.forEach((p, idx) => {{
    const isBridge = p.type === "bridge";
    const matchesFilter = currentFilter === "all" || p.type === currentFilter;
    const matchesSearch = p.name.toLowerCase().includes(query) || p.scope.toLowerCase().includes(query) || p.cost.toLowerCase().includes(query);

    if (matchesFilter && matchesSearch) {{
      count++;
      if (!isBridge) totalKm += p.length;

      const row = document.createElement("div");
      row.className = "reg-row";
      row.onclick = () => openProjectModal(idx);
      const pct = Math.min(100, (p.length / 27.0) * 100);

      row.innerHTML = `
        <div class="reg-ref">${{p.id}}</div>
        <div class="reg-thumb-wrap">
          <img src="${{p.img}}" alt="${{p.name}}" loading="lazy">
        </div>
        <div class="reg-title">
          <b>${{p.name}}</b>
          <small>${{p.scope}}</small>
        </div>
        <div class="reg-bar-wrap">
          <div class="reg-bar-fill${{isBridge ? ' bridge' : ''}}" style="width: ${{pct}}%;"></div>
        </div>
        <div class="reg-cost">${{p.cost}}</div>
        <div class="reg-value">${{p.metric}}</div>
      `;
      regList.appendChild(row);
    }}
  }});

  regSummary.textContent = `${{count}} projects shown · ${{totalKm.toFixed(1)}} km of classified road delivered`;
}}

renderProjects();

// Filter buttons
document.querySelectorAll(".filter-btn").forEach(btn => {{
  btn.onclick = () => {{
    document.querySelectorAll(".filter-btn").forEach(b => b.setAttribute("aria-pressed", "false"));
    btn.setAttribute("aria-pressed", "true");
    currentFilter = btn.dataset.filter;
    renderProjects();
  }};
}});

regSearch.oninput = () => renderProjects();

// Project Modal
const projModal = document.getElementById("projModal");
const modalImg = document.getElementById("modalImg");
const modalTitle = document.getElementById("modalTitle");
const modalRef = document.getElementById("modalRef");
const modalClient = document.getElementById("modalClient");
const modalDesc = document.getElementById("modalDesc");
const modalCost = document.getElementById("modalCost");
const modalMetric = document.getElementById("modalMetric");
const modalStandard = document.getElementById("modalStandard");
const modalScope = document.getElementById("modalScope");
const modalClose = document.getElementById("modalClose");

function openProjectModal(idx) {{
  const p = PROJECTS[idx];
  modalImg.src = p.img;
  modalImg.alt = p.name;
  modalTitle.textContent = p.name;
  modalRef.textContent = p.id;
  modalClient.textContent = "Client: " + p.client;
  modalDesc.textContent = p.desc;
  modalCost.textContent = p.cost;
  modalMetric.textContent = p.metric;
  modalStandard.textContent = p.standard;
  modalScope.textContent = p.scope;
  projModal.showModal();
}}

modalClose.onclick = () => projModal.close();
projModal.onclick = e => {{
  if (e.target === projModal) projModal.close();
}};

// Services Tab System
const SERVICES = [
  {{
    title: "Road & Bridge Engineering",
    svg: "M4 36h36M8 36c4-14 10-18 14-18s10 4 14 18M12 36V24M32 36V24",
    lead: "Our core competence: design of classified roads, single- and multi-span girder bridges, and auxiliary structures designed for lifelong durability under heavy axle loads.",
    items: [
      "Geometric Road Design (DC-1 to DC-8 Standards)",
      "Reinforced Concrete Girder Bridges",
      "Hydraulic Drainage & Structural Culverts",
      "Pavement Analysis & Overlay Design",
      "Associated Administrative & Civil Buildings",
      "Slope Protection & Gabion Retaining Walls"
    ]
  }},
  {{
    title: "Studies & Surveys",
    svg: "M22 8a14 14 0 1 0 0 28 14 14 0 0 0 0-28zM22 2v8M22 34v8M2 22h8M34 22h8",
    lead: "Fieldwork and ground investigations that guarantee accuracy before ground is broken. We eliminate downstream contractor variation through exhaustive site characterization.",
    items: [
      "High-Precision Topographic & GPS Surveys",
      "Geotechnical Boring & Subsoil Profiling",
      "CBR, Atterberg Limits & Proctor Testing",
      "Catchment Hydrology & Scour Modeling",
      "Quarry & Construction Materials Surveys",
      "Pre-Investment Socio-Economic Feasibility"
    ]
  }},
  {{
    title: "Tender & Contract Administration",
    svg: "M8 6h22l6 6v26H8zM14 18h16M14 25h16M14 32h10",
    lead: "Defensible procurement packages, transparent evaluations, and firm FIDIC/PPA contract administration to keep projects within budget and free of avoidable dispute.",
    items: [
      "Bills of Quantities (BOQ) Preparation",
      "Confidential Engineer's Cost Estimates",
      "Standard PPA / ERA / FIDIC Tender Dossiers",
      "Technical & Financial Bid Evaluation",
      "Contract Drafting & Negotiation Support",
      "Contractor Claims Appraisal & Dispute Review"
    ]
  }},
  {{
    title: "Supervision & Regional Planning",
    svg: "M6 38l12-14 8 6 12-20M30 10h8v8",
    lead: "On-site quality enforcement that ensures the contractor builds to exact design tolerances, alongside planning that integrates roads with the wider regional landscape.",
    items: [
      "Full-Time Resident Site Supervision",
      "Field Compaction & In-Situ Density Testing",
      "Concrete Compressive Strength Cube Crushing",
      "Interim Payment Certificate (IPC) Auditing",
      "Environmental & Social Impact (ESIA) Monitoring",
      "Watershed Conservation & Corridor Planning"
    ]
  }}
];

const svcTabBtns = document.querySelectorAll(".svc-tab-btn");
const svcPanel = document.getElementById("svcPanel");

function setServiceTab(idx) {{
  svcTabBtns.forEach((btn, i) => btn.setAttribute("aria-selected", i === idx));
  const s = SERVICES[idx];
  svcPanel.innerHTML = `
    <div class="svc-panel-head">
      <svg viewBox="0 0 44 44"><path d="${{s.svg}}"/></svg>
      <h3>${{s.title}}</h3>
    </div>
    <p class="svc-panel-desc">${{s.lead}}</p>
    <ul class="svc-sublist">
      ${{s.items.map(it => `<li>${{it}}</li>`).join("")}}
    </ul>
  `;
}}

svcTabBtns.forEach((btn, i) => {{
  btn.onclick = () => setServiceTab(i);
}});
setServiceTab(0);

// View switcher (Tabs vs Grid)
const btnTabView = document.getElementById("btnTabView");
const btnGridView = document.getElementById("btnGridView");
const svcTabView = document.getElementById("svcTabView");
const svcGridView = document.getElementById("svcGridView");

btnTabView.onclick = () => {{
  btnTabView.classList.add("active");
  btnGridView.classList.remove("active");
  svcTabView.style.display = "grid";
  svcGridView.classList.remove("active");
}};

btnGridView.onclick = () => {{
  btnGridView.classList.add("active");
  btnTabView.classList.remove("active");
  svcTabView.style.display = "none";
  svcGridView.classList.add("active");
}};

// Hero Visual Showcase Switcher
const btnShowProfile = document.getElementById("btnShowProfile");
const btnShowPhoto = document.getElementById("btnShowPhoto");
const panelProfile = document.getElementById("panelProfile");
const panelPhoto = document.getElementById("panelPhoto");

btnShowProfile.onclick = () => {{
  btnShowProfile.classList.add("active");
  btnShowPhoto.classList.remove("active");
  panelProfile.classList.add("active");
  panelPhoto.classList.remove("active");
}};

btnShowPhoto.onclick = () => {{
  btnShowPhoto.classList.add("active");
  btnShowProfile.classList.remove("active");
  panelPhoto.classList.add("active");
  panelProfile.classList.remove("active");
}};

// Light / Dark Theme Switcher
const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");

function updateThemeIcon(isDark) {{
  if (isDark) {{
    themeIcon.innerHTML = `<path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" fill="currentColor"/>`;
  }} else {{
    themeIcon.innerHTML = `<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>`;
  }}
}}

const savedTheme = localStorage.getItem("axulal-theme");
const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
const initialDark = savedTheme ? savedTheme === "dark" : systemPrefersDark;

if (savedTheme) {{
  document.documentElement.setAttribute("data-theme", savedTheme);
}}
updateThemeIcon(initialDark);

themeToggle.onclick = () => {{
  const current = document.documentElement.getAttribute("data-theme");
  const isDarkNow = current === "dark" || (!current && systemPrefersDark);
  const nextTheme = isDarkNow ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", nextTheme);
  localStorage.setItem("axulal-theme", nextTheme);
  updateThemeIcon(nextTheme === "dark");
}};

// Mobile Navigation Menu
const menuToggle = document.getElementById("menuToggle");
const nav = document.getElementById("nav");

function toggleMenu(open) {{
  const isOpen = typeof open === "boolean" ? open : !nav.classList.contains("open");
  nav.classList.toggle("open", isOpen);
  menuToggle.setAttribute("aria-expanded", String(isOpen));
}}

menuToggle.onclick = () => toggleMenu();
nav.querySelectorAll("a").forEach(a => {{
  a.onclick = () => toggleMenu(false);
}});
document.addEventListener("keydown", e => {{
  if (e.key === "Escape") {{
    toggleMenu(false);
    if (projModal.open) projModal.close();
    if (lb.open) lb.close();
  }}
}});

// Header Scroll Effect & ScrollSpy
const hd = document.getElementById("hd");
window.addEventListener("scroll", () => {{
  hd.classList.toggle("sc", window.scrollY > 10);
}}, {{ passive: true }});

if ("IntersectionObserver" in window) {{
  const navLinks = nav.querySelectorAll("a");
  const observer = new IntersectionObserver(entries => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        const id = entry.target.id;
        navLinks.forEach(link => {{
          link.classList.toggle("on", link.getAttribute("href") === "#" + id);
        }});
      }}
    }});
  }}, {{ rootMargin: "-35% 0px -45% 0px" }});

  ["about", "structure", "services", "stations", "projects", "records", "credentials", "contact"].forEach(id => {{
    const el = document.getElementById(id);
    if (el) observer.observe(el);
  }});
}}

// Lightbox Dialog
const lb = document.getElementById("lb");
const lbImg = document.getElementById("lbImg");
const lbCaption = document.getElementById("lbCaption");
const lbCounter = document.getElementById("lbCounter");
const lbClose = document.getElementById("lbClose");
const lbPrev = document.getElementById("lbPrev");
const lbNext = document.getElementById("lbNext");
let currentPlateIdx = 0;

function openLightbox(idx) {{
  currentPlateIdx = idx;
  const item = GALLERY[idx];
  lbImg.src = item.img;
  lbImg.alt = item.title;
  lbCaption.textContent = item.plate + ": " + item.title + " — " + item.desc;
  lbCounter.textContent = (idx + 1) + " / " + GALLERY.length;
  lb.showModal();
}}

lbClose.onclick = () => lb.close();
lb.onclick = e => {{
  if (e.target === lb) lb.close();
}};

lbPrev.onclick = () => {{
  const prevIdx = (currentPlateIdx - 1 + GALLERY.length) % GALLERY.length;
  openLightbox(prevIdx);
}};

lbNext.onclick = () => {{
  const nextIdx = (currentPlateIdx + 1) % GALLERY.length;
  openLightbox(nextIdx);
}};

document.addEventListener("keydown", e => {{
  if (!lb.open) return;
  if (e.key === "ArrowLeft") lbPrev.click();
  if (e.key === "ArrowRight") lbNext.click();
}});

// Copy to Clipboard Utility
function copyText(text, btnEl) {{
  navigator.clipboard.writeText(text).then(() => {{
    const original = btnEl.textContent;
    btnEl.textContent = "Copied!";
    btnEl.style.background = "#1c5ec2";
    setTimeout(() => {{
      btnEl.textContent = original;
      btnEl.style.background = "";
    }}, 2000);
  }}).catch(() => {{
    prompt("Copy to clipboard:", text);
  }});
}}

// Contact Form Submission
const contactForm = document.getElementById("contactForm");
const formFeedback = document.getElementById("formFeedback");

contactForm.onsubmit = e => {{
  e.preventDefault();
  const name = document.getElementById("formName").value.trim();
  const contact = document.getElementById("formContact").value.trim();
  const service = document.getElementById("formService").value;
  const message = document.getElementById("formMessage").value.trim();

  const body = `Name/Organization: ${{name}}
Contact Details: ${{contact}}
Service Required: ${{service}}

Project Description:
${{message}}`;

  formFeedback.textContent = "Preparing dispatch to axulalconsulting@gmail.com...";
  
  const mailtoUrl = `mailto:axulalconsulting@gmail.com?subject=${{encodeURIComponent("Proposal Request: " + service + " - " + name)}}&body=${{encodeURIComponent(body)}}`;
  
  setTimeout(() => {{
    window.location.href = mailtoUrl;
    formFeedback.textContent = "Email client opened! If your email app did not launch automatically, please email us directly at axulalconsulting@gmail.com.";
  }}, 400);
}};
</script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    with open("Axulal Consulting Engineers PLC _ Master.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Website created successfully with all PDF pictures and project data!")

if __name__ == "__main__":
    build_site()
