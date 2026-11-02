# Axulal Consulting Engineers PLC — Official Website

> **Category-1 Highway & Bridge Engineering Consultants · Addis Ababa, Ethiopia**  
> Established 2011 · Registered under FDRE Licensure #01/ORA/2011 with the Ministry of Urban Development & Infrastructure (MoUDI/MoWUD) and Ethiopian Roads Administration (ERA).

---

## 🏗️ Corporate Overview

**Axulal Consulting Engineers PLC (አክሱላል ኮንሰልቲንግ ኢንጂነርስ ኃላ/የተ/የግ/ማህበር)** is a premier Category-1 Ethiopian engineering consultancy. Founded in 2011, the firm specializes in highway geometric alignment design, reinforced concrete bridge structural engineering, hydrological catchment modeling, and resident construction supervision.

### Key Delivered Metrics
- **145.8 km** of delivered all-weather classified road corridors across highland, rolling, and mountainous terrains.
- **46.0 m** of reinforced concrete girder river crossings (Awash River 24.0 m and Berga River 22.0 m).
- **100+** hydraulic cross-drainage box culverts, slab structures, and mortared stone retaining walls.
- **15 Years** of uninterrupted public and commercial infrastructure delivery.

---

## 💻 Architecture & Technical Stack

The website is engineered as a high-performance, accessible, and lightweight static application:

- **Semantic HTML5**: Native semantic markup with full accessibility (WCAG AA), screen-reader friendly emoji handling (`aria-hidden="true"`), skip link navigation, and modal focus management with focus trapping.
- **Modern Responsive Design**: Custom CSS with architectural Bento grids, CSS Grid/Flexbox layouts, fluid typography (`clamp()`), and zero external framework overhead.
- **Typography**: Google Fonts pairing — *Archivo* for authoritative architectural headings, *Source Sans 3* for legibility, and *JetBrains Mono* for technical telemetry and chainage specs.
- **Image Pipeline**: Optimized next-gen WebP assets with progressive JPG/PNG fallbacks and responsive `<picture>` tags.
- **Client-Side Interactivity**: Vanilla JavaScript ES5/ES6 for regional hub filtering, dynamic card expansion, high-resolution photographic lightboxes, and accessible dialogs.
- **Tender Intake**: AJAX form submission via FormSubmit.co with honeypot anti-spam protection and server response validation.
- **SEO & Social**: Open Graph meta tags, Twitter Card tags, canonical link, JSON-LD `EngineeringService` structured data, `robots.txt`, and XML `sitemap.xml`.

---

## 📁 Repository Structure

```text
.
├── index.html                       # Production live website
├── favicon.ico                      # Root browser icon
├── robots.txt                       # Search engine crawler instructions
├── sitemap.xml                      # Canonical XML sitemap
├── assets/
│   ├── css/
│   │   └── site.css                 # Master compiled stylesheet
│   ├── js/
│   │   ├── site.js                  # Core client-side interactions & modals
│   │   └── data.js                  # Machine-readable project & gallery datasets
│   ├── logo-horizontal.png / .webp  # High-legibility horizontal header lockup
│   ├── logo.png / .webp             # Authentic bilingual brand mark (emblem + Ge'ez)
│   ├── favicon.png / .svg           # Scalable browser icons
│   ├── org_chart.png / .svg / .webp # Institutional governance charts
│   ├── projects/                    # 12 classified road & bridge project images
│   └── gallery/                     # 12 resident supervision field plates
├── scripts/
│   └── build_worldclass_site.py     # Master deterministic site compiler
├── .gitignore
└── README.md
```

---

## 🚀 Building & Running Locally

### Run Locally
No web server installation is required. Open `index.html` in any browser or launch Python's built-in server:

```bash
python -m http.server 8000
```
Then visit `http://localhost:8000`.

### Master Rebuild
To regenerate `index.html`, `site.css`, `site.js`, `data.js`, `robots.txt`, and `sitemap.xml`:

```bash
python scripts/build_worldclass_site.py
```

---

## 🏛️ Corporate Headquarters Desk

- **Physical Location**: Adwa Square, Katekse Building, Third floor, House No: 712/A, Woreda: 07, Sub-city: Yeka, Addis Ababa, Ethiopia
- **Telephone**: +251 111 582107
- **Technical Director Direct**: +251 93 007 7347
- **FAX**: +251 111 262888
- **Postal Box**: P.O. Box 26061/1000, Addis Ababa, Ethiopia
- **Tender Inquiries**: tenders@axulalengineers.com
- **Direct Mail**: info@axulalengineers.com
- **Statutory Licensure**: Category-1 Highway & Bridge Consultants · FDRE Reg #01/ORA/2011

---

© 2011 – 2026 **Axulal Consulting Engineers PLC (አክሱላል ኮንሰልቲንግ ኢንጂነርስ ኃላ/የተ/የግ/ማህበር)**. All rights reserved.
