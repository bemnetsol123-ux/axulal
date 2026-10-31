import os
import re
from bs4 import BeautifulSoup

def main():
    print("Reading original File 1 to extract high-resolution image assets...")
    f1_path = "Axulal Consulting Engineers PLC _ Road and Bridge Consultants, Addis Ababa 2.html"
    if not os.path.exists(f1_path):
        print(f"Error: {f1_path} not found.")
        return

    with open(f1_path, "r", encoding="utf-8", errors="ignore") as f:
        soup1 = BeautifulSoup(f.read(), "html.parser")

    imgs = [img["src"] for img in soup1.find_all("img") if img.get("src", "").startswith("data:")]
    print(f"Extracted {len(imgs)} base64 images.")

    if len(imgs) < 11:
        print("Warning: Expected 11 base64 images, found:", len(imgs))

    # Construct the master HTML
    html_parts = []
    
    html_parts.append('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Axulal Consulting Engineers PLC | Category-1 Highway and Bridge Consultants, Addis Ababa</title>
<meta name="description" content="Axulal Consulting Engineers PLC is a Category-1 Highway and Bridge consulting firm based in Addis Ababa, Ethiopia. Delivering expert road and bridge engineering, surveys, tender documents, and construction supervision since 2011.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,400..900&family=Source+Sans+3:ital,wght@0,300..700;1,400&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
:root {
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
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
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
  }
}

:root[data-theme="dark"] {
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
}

:root[data-theme="light"] {
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
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 84px;
  font-size: 16px;
}

body {
  font-family: 'Source Sans 3', system-ui, -apple-system, sans-serif;
  color: var(--ink);
  background-color: var(--paper);
  background-image: 
    linear-gradient(var(--grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 32px 32px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

a {
  color: inherit;
  text-decoration: none;
}

button {
  font: inherit;
  cursor: pointer;
  border: none;
  background: none;
}

.wrap {
  width: 100%;
  max-width: var(--max-w);
  margin-inline: auto;
  padding-inline: 1.5rem;
}

/* ================= HEADER ================= */
#hd {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--navy);
  color: #ffffff;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  transition: background 0.25s ease, box-shadow 0.25s ease;
}

#hd.sc {
  background: var(--navy-dark);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
}

.bar-in {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
  gap: 1rem;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  font-family: 'Archivo', sans-serif;
  font-weight: 800;
  font-size: 1.05rem;
  letter-spacing: 0.02em;
  color: #ffffff;
  text-transform: uppercase;
}

.brand svg {
  flex-shrink: 0;
}

.brand .cat-pill {
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
}

#nav {
  display: flex;
  align-items: center;
  gap: 1.6rem;
}

#nav a {
  font-family: 'Archivo', sans-serif;
  font-size: 0.88rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: #c9d8f5;
  transition: color 0.15s ease;
  position: relative;
  padding-block: 0.25rem;
}

#nav a:hover, #nav a.on {
  color: #ffffff;
}

#nav a.on::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--red);
  border-radius: 2px;
}

.hd-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.theme-btn {
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
}

.theme-btn:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.4);
}

.theme-btn svg {
  width: 18px;
  height: 18px;
}

.btn {
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
}

.btn:hover {
  background: var(--red-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(217, 39, 29, 0.35);
}

.btn.ghost {
  background: transparent;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.35);
}

.btn.ghost:hover {
  background: rgba(255, 255, 255, 0.12);
  border-color: #ffffff;
}

.menu-btn {
  display: none;
  width: 42px;
  height: 42px;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-sm);
}

.menu-btn svg {
  width: 24px;
  height: 24px;
  stroke: currentColor;
  stroke-width: 2;
  fill: none;
}

/* ================= HERO ================= */
.hero {
  background: var(--navy);
  color: #ffffff;
  padding-top: 3.5rem;
  padding-bottom: 2.5rem;
  position: relative;
  overflow: hidden;
  border-bottom: 1px solid var(--line);
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 60%;
  height: 100%;
  background: radial-gradient(circle at 80% 20%, rgba(28, 94, 194, 0.18), transparent 70%);
  pointer-events: none;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 3rem;
  align-items: center;
}

.badge-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1.25rem;
  flex-wrap: wrap;
}

.reg-badge {
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
}

.motto-tag {
  display: inline-block;
  font-family: 'Archivo', sans-serif;
  font-size: 0.82rem;
  font-weight: 800;
  color: var(--red);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.hero h1 {
  font-family: 'Archivo', sans-serif;
  font-size: clamp(2.2rem, 3.8vw, 3.2rem);
  font-weight: 850;
  line-height: 1.15;
  letter-spacing: -0.02em;
  margin-bottom: 1.25rem;
  color: #ffffff;
}

.hero-lead {
  font-size: 1.125rem;
  line-height: 1.65;
  color: #c9d8f5;
  margin-bottom: 2rem;
  max-width: 580px;
}

.cta-group {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1.75rem;
}

.direct-call {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  color: #a3b8e0;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: color 0.15s ease;
}

.direct-call:hover {
  color: #ffffff;
}

/* Technical Showcase Box */
.hero-visual-card {
  background: rgba(10, 23, 51, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  overflow: hidden;
  position: relative;
}

.visual-topbar {
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
}

.visual-tabs {
  display: flex;
  gap: 0.35rem;
}

.v-tab-btn {
  padding: 0.25rem 0.65rem;
  font-family: 'Archivo', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  color: #a3b8e0;
  border-radius: 3px;
  background: transparent;
  transition: all 0.15s ease;
}

.v-tab-btn.active {
  background: var(--blue);
  color: #ffffff;
}

.visual-panel {
  display: none;
  position: relative;
}

.visual-panel.active {
  display: block;
}

.hero-photo-wrap {
  position: relative;
}

.hero-photo-wrap img {
  width: 100%;
  height: 290px;
  object-fit: cover;
  display: block;
}

.photo-badge {
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
}

.prof-svg-wrap {
  padding: 1.25rem 1rem 0.75rem;
  background: #050d22;
}

.prof-svg-wrap svg {
  width: 100%;
  height: auto;
  display: block;
}

.prof-svg-wrap .g {
  fill: none;
  stroke: #2e4475;
  stroke-width: 2;
  stroke-dasharray: 4 4;
}

.prof-svg-wrap .r {
  fill: none;
  stroke: var(--red);
  stroke-width: 2.5;
}

.prof-svg-wrap .b {
  fill: none;
  stroke: var(--blue-light);
  stroke-width: 3.2;
}

.prof-svg-wrap .t {
  stroke: #5d75a3;
  stroke-width: 1;
  fill: none;
}

.prof-svg-wrap text {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  fill: #8aa4d1;
  font-weight: 600;
  letter-spacing: 0.04em;
}

/* Stats Banner */
.stats-banner {
  margin-top: 2.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  padding-top: 1.75rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1.5rem;
}

.stat-item {
  border-left: 2px solid var(--blue-light);
  padding-left: 1rem;
}

.stat-num {
  display: block;
  font-family: 'Archivo', sans-serif;
  font-weight: 850;
  font-size: 1.8rem;
  line-height: 1.1;
  color: #ffffff;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.82rem;
  color: #a3b8e0;
  line-height: 1.35;
}

/* ================= SECTIONS COMMON ================= */
section {
  padding-block: 5.5rem;
}

section.alt {
  background: var(--card);
  border-block: 1px solid var(--line);
}

.sec-head {
  margin-bottom: 3.25rem;
  position: relative;
}

.sec-tag {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--blue);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 0.5rem;
}

.sec-head h2 {
  font-family: 'Archivo', sans-serif;
  font-size: clamp(1.85rem, 3.2vw, 2.6rem);
  font-weight: 800;
  color: var(--ink);
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.sec-lead {
  font-size: 1.125rem;
  color: var(--muted);
  max-width: 700px;
  margin-top: 0.75rem;
  line-height: 1.6;
}

/* ================= ABOUT SECTION ================= */
.about-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 3.5rem;
  margin-bottom: 3.5rem;
}

.about-body p.big {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.5;
  margin-bottom: 1.25rem;
}

.about-body p {
  font-size: 1.025rem;
  color: var(--muted);
  margin-bottom: 1.25rem;
  line-height: 1.7;
}

.vm-cards {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.vm-box {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  box-shadow: var(--shadow-sm);
  position: relative;
  border-left: 4px solid var(--blue);
}

.vm-box.mission {
  border-left-color: var(--red);
}

.vm-box h3 {
  font-family: 'Archivo', sans-serif;
  font-size: 1.15rem;
  font-weight: 750;
  color: var(--ink);
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.vm-box p {
  font-size: 0.95rem;
  color: var(--muted);
  line-height: 1.6;
}

.facts-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.75rem;
}

.fact-card {
  background: var(--tr);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.fact-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.fact-idx {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--blue);
  display: block;
  margin-bottom: 0.5rem;
}

.fact-card h3 {
  font-family: 'Archivo', sans-serif;
  font-size: 1.2rem;
  font-weight: 750;
  color: var(--ink);
  margin-bottom: 0.65rem;
}

.fact-card p {
  font-size: 0.925rem;
  color: var(--muted);
  line-height: 1.6;
}

/* ================= SERVICES SECTION ================= */
.svc-nav-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1.25rem;
}

.view-toggle {
  display: inline-flex;
  padding: 0.25rem;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: var(--radius-sm);
  gap: 0.25rem;
}

.view-toggle button {
  padding: 0.4rem 0.85rem;
  font-family: 'Archivo', sans-serif;
  font-size: 0.82rem;
  font-weight: 700;
  border-radius: 3px;
  color: var(--muted);
  transition: all 0.15s ease;
}

.view-toggle button.active {
  background: var(--card);
  color: var(--ink);
  box-shadow: var(--shadow-sm);
}

/* Tab View */
.svc-tabs-container {
  display: grid;
  grid-template-columns: 330px 1fr;
  gap: 2rem;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  box-shadow: var(--shadow-sm);
}

.svc-tablist {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

.svc-tab-btn {
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
}

.svc-tab-btn svg {
  width: 28px;
  height: 28px;
  stroke: var(--muted);
  stroke-width: 2.2;
  fill: none;
  flex-shrink: 0;
  transition: stroke 0.2s ease;
}

.svc-tab-btn:hover {
  border-color: var(--blue);
  color: var(--blue);
}

.svc-tab-btn[aria-selected="true"] {
  background: var(--navy);
  color: #ffffff;
  border-color: var(--navy);
  box-shadow: var(--shadow-md);
}

.svc-tab-btn[aria-selected="true"] svg {
  stroke: var(--blue-light);
}

.svc-panel {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 2.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.svc-panel-head {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin-bottom: 1.25rem;
}

.svc-panel-head svg {
  width: 48px;
  height: 48px;
  stroke: var(--blue);
  stroke-width: 2.2;
  fill: none;
  flex-shrink: 0;
}

.svc-panel-head h3 {
  font-family: 'Archivo', sans-serif;
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--ink);
}

.svc-panel-desc {
  font-size: 1.05rem;
  color: var(--muted);
  margin-bottom: 2rem;
  line-height: 1.7;
}

.svc-sublist {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.85rem 1.5rem;
  list-style: none;
}

.svc-sublist li {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  font-size: 0.975rem;
  font-weight: 600;
  color: var(--ink);
}

.svc-sublist li::before {
  content: '✓';
  color: var(--blue);
  font-weight: 800;
}

/* Grid View */
.svc-grid-view {
  display: none;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.svc-grid-view.active {
  display: grid;
}

.svc-grid-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 2rem 1.5rem;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
}

.svc-grid-card svg {
  width: 38px;
  height: 38px;
  stroke: var(--blue);
  stroke-width: 2.2;
  fill: none;
  margin-bottom: 1.25rem;
}

.svc-grid-card h3 {
  font-family: 'Archivo', sans-serif;
  font-size: 1.2rem;
  font-weight: 750;
  color: var(--ink);
  margin-bottom: 0.75rem;
}

.svc-grid-card p {
  font-size: 0.9rem;
  color: var(--muted);
  margin-bottom: 1.25rem;
  line-height: 1.5;
}

.svc-grid-card ul {
  list-style: none;
  margin-top: auto;
  border-top: 1px dashed var(--line);
  padding-top: 1rem;
}

.svc-grid-card ul li {
  font-size: 0.85rem;
  color: var(--ink);
  margin-bottom: 0.4rem;
}

/* ================= HOW A PROJECT RUNS (STATIONS) ================= */
.stations-track {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1rem;
  position: relative;
  list-style: none;
}

.stations-track::before {
  content: '';
  position: absolute;
  top: 26px;
  left: 20px;
  right: 20px;
  height: 3px;
  background: var(--line);
  z-index: 1;
}

.station-node {
  position: relative;
  z-index: 2;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 1.25rem 1rem;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.station-node:hover {
  transform: translateY(-4px);
  border-color: var(--blue);
  box-shadow: var(--shadow-md);
}

.sta-pin {
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
}

.sta-tag {
  display: block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--red);
  letter-spacing: 0.05em;
  margin-bottom: 0.25rem;
}

.station-node h3 {
  font-family: 'Archivo', sans-serif;
  font-size: 1.1rem;
  font-weight: 750;
  color: var(--ink);
  margin-bottom: 0.4rem;
}

.station-node p {
  font-size: 0.85rem;
  color: var(--muted);
  line-height: 1.45;
}

/* ================= FEATURED PROJECTS ================= */
.featured-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  margin-bottom: 3.5rem;
}

.feat-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.feat-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}

.feat-img-wrap {
  height: 240px;
  overflow: hidden;
  position: relative;
}

.feat-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.feat-card:hover .feat-img-wrap img {
  transform: scale(1.03);
}

.feat-badge {
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
}

.feat-info {
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.feat-info h3 {
  font-family: 'Archivo', sans-serif;
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--ink);
  margin-bottom: 0.4rem;
}

.feat-client {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  color: var(--blue);
  margin-bottom: 0.85rem;
}

.feat-info p {
  font-size: 0.95rem;
  color: var(--muted);
  line-height: 1.6;
  margin-bottom: 1.25rem;
}

.feat-meta-row {
  display: flex;
  gap: 1.5rem;
  margin-top: auto;
  padding-top: 1rem;
  border-top: 1px solid var(--line);
}

.feat-stat {
  font-family: 'Archivo', sans-serif;
}

.feat-stat b {
  display: block;
  font-size: 1.2rem;
  color: var(--ink);
  font-weight: 800;
}

.feat-stat span {
  font-size: 0.75rem;
  color: var(--muted);
  text-transform: uppercase;
}

/* ================= PROJECT REGISTER ================= */
.register-wrap {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-sm);
}

.reg-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.filter-group {
  display: flex;
  gap: 0.4rem;
  background: var(--paper);
  padding: 0.3rem;
  border-radius: var(--radius-sm);
  border: 1px solid var(--line);
}

.filter-btn {
  padding: 0.45rem 1rem;
  font-family: 'Archivo', sans-serif;
  font-size: 0.85rem;
  font-weight: 700;
  border-radius: 3px;
  color: var(--muted);
  transition: all 0.15s ease;
}

.filter-btn[aria-pressed="true"] {
  background: var(--navy);
  color: #fff;
}

.reg-search-wrap {
  position: relative;
  min-width: 240px;
}

.reg-search {
  width: 100%;
  padding: 0.5rem 1rem 0.5rem 2.2rem;
  font-size: 0.85rem;
  font-family: inherit;
  border: 1px solid var(--line);
  border-radius: var(--radius-sm);
  background: var(--paper);
  color: var(--ink);
}

.reg-search:focus {
  outline: none;
  border-color: var(--blue);
}

.reg-search-icon {
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--muted);
  pointer-events: none;
}

.reg-summary {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--blue);
  padding-block: 0.25rem;
}

/* Ruler */
.ruler-bar {
  display: grid;
  grid-template-columns: 80px 1.4fr 1.6fr 90px;
  gap: 1rem;
  padding: 0.65rem 1rem;
  background: var(--tr);
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--muted);
  text-transform: uppercase;
}

.ruler-scale {
  display: flex;
  justify-content: space-between;
  padding-inline: 4px;
}

/* Ledger Rows */
.reg-list {
  display: flex;
  flex-direction: column;
}

.reg-row {
  display: grid;
  grid-template-columns: 80px 1.4fr 1.6fr 90px;
  gap: 1rem;
  align-items: center;
  padding: 0.9rem 1rem;
  border-bottom: 1px solid var(--line);
  font-size: 0.925rem;
  transition: background 0.15s ease;
}

.reg-row:hover {
  background: var(--paper);
}

.reg-ref {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 600;
  color: var(--muted);
  font-size: 0.8rem;
}

.reg-title b {
  color: var(--ink);
  font-size: 0.95rem;
  display: block;
}

.reg-title small {
  font-size: 0.8rem;
  color: var(--muted);
}

.reg-bar-wrap {
  position: relative;
  background: rgba(0, 0, 0, 0.04);
  height: 12px;
  border-radius: 6px;
  overflow: hidden;
}

:root[data-theme="dark"] .reg-bar-wrap {
  background: rgba(255, 255, 255, 0.08);
}

.reg-bar-fill {
  height: 100%;
  background: var(--blue);
  border-radius: 6px;
  transition: width 0.4s ease;
}

.reg-bar-fill.bridge {
  background: var(--red);
}

.reg-value {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.88rem;
  font-weight: 700;
  text-align: right;
  color: var(--ink);
}

.reg-footnote {
  margin-top: 1.25rem;
  font-size: 0.82rem;
  color: var(--muted);
  font-style: italic;
}

/* ================= GALLERY (SITE RECORDS) ================= */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}

.plate-card {
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
}

.plate-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: var(--blue);
}

.plate-img-wrap {
  height: 180px;
  overflow: hidden;
  position: relative;
  background: #000;
}

.plate-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.plate-card:hover .plate-img-wrap img {
  transform: scale(1.05);
}

.plate-overlay {
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
}

.plate-body {
  padding: 1rem;
}

.plate-body h4 {
  font-family: 'Archivo', sans-serif;
  font-size: 0.95rem;
  font-weight: 750;
  color: var(--ink);
  line-height: 1.35;
  margin-bottom: 0.25rem;
}

.plate-body p {
  font-size: 0.8rem;
  color: var(--muted);
  line-height: 1.4;
}

/* ================= CREDENTIALS ================= */
.cred-grid {
  display: grid;
  grid-template-columns: 260px 1fr 1fr;
  gap: 3rem;
  align-items: start;
}

.stamp-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 2rem 1.5rem;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
}

.stamp {
  width: 150px;
  height: 150px;
  color: var(--red);
  transform: rotate(-6deg);
  margin-bottom: 1.25rem;
  transition: transform 0.3s ease;
}

.stamp:hover {
  transform: rotate(0deg) scale(1.03);
}

.stamp text {
  text-anchor: middle;
  font-family: 'Archivo', sans-serif;
  font-weight: 800;
  fill: currentColor;
}

.stamp-caption {
  font-family: 'Archivo', sans-serif;
  font-weight: 750;
  font-size: 0.95rem;
  color: var(--ink);
  margin-bottom: 0.25rem;
}

.stamp-sub {
  font-size: 0.8rem;
  color: var(--muted);
}

.cred-col h3 {
  font-family: 'Archivo', sans-serif;
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--ink);
  margin-bottom: 1.25rem;
  display: flex;
  align-items: center;
  gap: 0.65rem;
}

.cred-col h3 svg {
  width: 22px;
  height: 22px;
  stroke: var(--blue);
  fill: none;
}

.chips-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin-bottom: 1.5rem;
}

.chip {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 0.45rem 0.85rem;
  background: var(--tr);
  border: 1px solid var(--line);
  border-radius: 4px;
  color: var(--ink);
}

.cred-note {
  font-size: 0.9rem;
  color: var(--muted);
  line-height: 1.6;
}

.lic-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.lic-list li {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  font-size: 0.95rem;
  color: var(--ink);
  line-height: 1.5;
  background: var(--card);
  padding: 0.75rem 1rem;
  border: 1px solid var(--line);
  border-radius: var(--radius-sm);
}

.lic-check {
  color: var(--blue);
  font-weight: 800;
  font-size: 1.1rem;
  line-height: 1;
}

/* ================= CONTACT SECTION ================= */
.contact-section {
  background: var(--navy);
  color: #ffffff;
  border-top: 1px solid var(--line);
}

.contact-section .sec-tag {
  color: var(--red);
}

.contact-section h2 {
  color: #ffffff;
}

.contact-section .sec-lead {
  color: #c9d8f5;
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1.25fr;
  gap: 3.5rem;
}

.contact-info-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-lg);
  padding: 2.25rem;
}

.info-item {
  margin-bottom: 1.75rem;
}

.info-item:last-child {
  margin-bottom: 0;
}

.info-lbl {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--red);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 0.4rem;
  display: block;
}

.info-val {
  font-size: 1.05rem;
  color: #eaf0fc;
  line-height: 1.5;
}

.contact-links-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.contact-link-row {
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
}

.contact-link-row:hover {
  background: rgba(255, 255, 255, 0.12);
}

.copy-btn {
  font-size: 0.7rem;
  padding: 0.2rem 0.5rem;
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
  border-radius: 3px;
  text-transform: uppercase;
  transition: background 0.15s ease;
}

.copy-btn:hover {
  background: var(--blue);
}

/* Contact Form */
.contact-form-card {
  background: var(--card);
  color: var(--ink);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  box-shadow: var(--shadow-lg);
}

.contact-form-card h3 {
  font-family: 'Archivo', sans-serif;
  font-size: 1.4rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
}

.contact-form-card p {
  font-size: 0.925rem;
  color: var(--muted);
  margin-bottom: 1.75rem;
}

.form-group {
  margin-bottom: 1.25rem;
}

.form-label {
  display: block;
  font-family: 'Archivo', sans-serif;
  font-size: 0.85rem;
  font-weight: 700;
  margin-bottom: 0.4rem;
  color: var(--ink);
}

.form-input, .form-select, .form-textarea {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid var(--line);
  border-radius: var(--radius-sm);
  font-family: inherit;
  font-size: 0.95rem;
  background: var(--paper);
  color: var(--ink);
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.form-input:focus, .form-select:focus, .form-textarea:focus {
  outline: none;
  border-color: var(--blue);
  box-shadow: 0 0 0 3px rgba(28, 94, 194, 0.15);
}

.form-textarea {
  min-height: 120px;
  resize: vertical;
}

.form-feedback {
  margin-top: 1rem;
  font-size: 0.875rem;
  line-height: 1.5;
  color: var(--blue);
}

/* ================= FOOTER ================= */
footer {
  background: var(--navy-dark);
  color: #ffffff;
  padding-block: 2.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.ftr-in {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.5rem;
  font-size: 0.875rem;
  color: #8fa5cc;
}

.ftr-motto {
  font-family: 'Archivo', sans-serif;
  font-weight: 800;
  color: var(--red);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.back-to-top {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: #c9d8f5;
  font-weight: 600;
  font-size: 0.85rem;
  transition: color 0.15s ease;
}

.back-to-top:hover {
  color: #ffffff;
}

/* ================= LIGHTBOX MODAL ================= */
dialog#lb {
  margin: auto;
  border: none;
  background: transparent;
  max-width: 90vw;
  max-height: 90vh;
  padding: 0;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
  border-radius: var(--radius-md);
  overflow: hidden;
}

dialog#lb::backdrop {
  background: rgba(4, 10, 23, 0.88);
  backdrop-filter: blur(8px);
}

.lightbox-content {
  background: var(--navy-dark);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-md);
  position: relative;
  max-width: 920px;
}

.lb-img-container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #000;
  max-height: 70vh;
}

.lb-img-container img {
  max-width: 100%;
  max-height: 70vh;
  object-fit: contain;
}

.lb-nav-btn {
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
}

.lb-nav-btn:hover {
  background: var(--blue);
}

.lb-nav-btn.prev { left: 1rem; }
.lb-nav-btn.next { right: 1rem; }

.lb-close-btn {
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
}

.lb-close-btn:hover {
  background: var(--red);
}

.lb-caption-bar {
  padding: 1.1rem 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.lb-caption-text {
  font-size: 0.95rem;
  color: #eaf0fc;
}

.lb-counter {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  color: #a3b8e0;
}

/* ================= RESPONSIVE ================= */
@media (max-width: 1024px) {
  .hero-grid {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
  .stats-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  .svc-tabs-container {
    grid-template-columns: 1fr;
  }
  .stations-track {
    grid-template-columns: repeat(3, 1fr);
  }
  .stations-track::before {
    display: none;
  }
  .gallery-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  .cred-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  .contact-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  #nav {
    display: none;
    position: fixed;
    top: 72px;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--navy-dark);
    flex-direction: column;
    padding: 2.5rem 2rem;
    gap: 1.75rem;
    z-index: 99;
  }
  #nav.open {
    display: flex;
  }
  .menu-btn {
    display: inline-flex;
  }
  .about-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  .facts-3 {
    grid-template-columns: 1fr;
  }
  .featured-grid {
    grid-template-columns: 1fr;
  }
  .gallery-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .svc-grid-view {
    grid-template-columns: 1fr;
  }
  .stations-track {
    grid-template-columns: repeat(2, 1fr);
  }
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .ruler-bar, .reg-row {
    grid-template-columns: 60px 1.5fr 1fr 70px;
  }
}

@media (max-width: 480px) {
  .gallery-grid {
    grid-template-columns: 1fr;
  }
  .stations-track {
    grid-template-columns: 1fr;
  }
  .stats-grid {
    grid-template-columns: 1fr;
  }
  .ruler-bar, .reg-row {
    grid-template-columns: 1fr auto;
  }
  .ruler-bar > div:nth-child(1), .ruler-bar > div:nth-child(3),
  .reg-row > div:nth-child(1), .reg-row > div:nth-child(3) {
    display: none;
  }
}
</style>
</head>
<body>

<!-- Header -->
<header id="hd">
  <div class="wrap bar-in">
    <a href="#top" class="brand" aria-label="Axulal Consulting Engineers PLC Home">
      <svg width="34" height="34" viewBox="0 0 34 34" fill="none" aria-hidden="true">
        <path d="M8 3v28M8 28h24M10 6l20 20H10z" stroke="#ffffff" stroke-width="2.4"/>
        <path d="M13 12l9 9h-9z" fill="#ff5e54"/>
      </svg>
      <span>Axulal Engineers<span class="cat-pill">CAT-1</span></span>
    </a>

    <nav id="nav" aria-label="Main Navigation">
      <a href="#about">About</a>
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
            <span class="reg-badge">Federal Ministry of Construction · Cat-1</span>
            <span class="motto-tag">Conquering Possibilities!!</span>
          </div>

          <h1>Roads and bridges, engineered from first survey to final handover.</h1>

          <p class="hero-lead">
            Category-1 Highway and Bridge consultants based in Addis Ababa. Since 2011, Axulal has studied, surveyed, designed, tendered, and supervised over 128 km of vital transportation corridors connecting communities across Oromia and Ethiopia.
          </p>

          <div class="cta-group">
            <a href="#projects" class="btn">Explore Projects</a>
            <a href="#contact" class="btn ghost">Start a Project With Us</a>
          </div>

          <a href="tel:+251111582107" class="direct-call">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
            Office: +251 111 582 107
          </a>
        </div>

        <!-- Technical Showcase Switcher (Elevation CAD Profile + Active Compaction Photo) -->
        <div class="hero-visual-card">
          <div class="visual-topbar">
            <span>TECHNICAL SPECIFICATION</span>
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
              <img src="''' + imgs[0] + ''''" alt="Heavy vibratory road roller compacting gravel sub-base on an Axulal road project site" loading="eager">
              <div class="photo-badge">
                <b>Field Record:</b> Heavy compaction on gravel alignment, Oromia rural network.
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
            <span class="stat-num">15+</span>
            <span class="stat-label">Years Leadership Experience</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">12</span>
            <span class="stat-label">Major Road & Bridge Projects</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">128+ km</span>
            <span class="stat-label">Classified Gravel Roads Delivered</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">Cat. 1</span>
            <span class="stat-label">Highest Highway & Bridge License</span>
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
            Born in 2011 inside Ethiopia's national Universal Rural Roads Access Program (URRAP), Axulal has evolved into a premier Category-1 Highway and Bridge consulting firm.
          </p>
          <p>
            Two senior professional engineers and one senior land surveyor—each with over fifteen years of rigorous field, design, and structural engineering experience—founded the firm. Together, they established a culture founded on engineering precision, honest contract stewardship, and deep respect for the communities our roads serve.
          </p>
          <p>
            We manage the entire lifecycle of civil transportation works: from preliminary reconnaissance and topographic surveys through detailed structural design, tender dossiers, construction supervision, and final contract administration. We champion the intelligent use of locally available stone and gravel resources, sustainable watershed drainage, and inclusive community engagement across Oromia and throughout Ethiopia.
          </p>
        </div>

        <div class="vm-cards">
          <div class="vm-box vision">
            <h3>Our Vision</h3>
            <p>To push past the default standard of engineering consulting in Ethiopia, establishing a new national benchmark through thoroughly investigated, resilient, and cost-effective infrastructure solutions.</p>
          </div>
          <div class="vm-box mission">
            <h3>Our Mission</h3>
            <p>To deliver quality consulting services that consistently exceed client expectations, achieved through continuous technical training, uncompromising quality control, and field-tested innovation.</p>
          </div>
        </div>
      </div>

      <!-- 3 Operational Pillars -->
      <div class="facts-3">
        <div class="fact-card">
          <span class="fact-idx">PILLAR 01</span>
          <h3>Led by Field Experience</h3>
          <p>Our principals remain active on site. Every geotechnical challenge, hydrology calculation, and structural girder design receives direct oversight from engineers with decades of hands-on Ethiopian terrain experience.</p>
        </div>
        <div class="fact-card">
          <span class="fact-idx">PILLAR 02</span>
          <h3>Tailored Multi-Disciplinary Teams</h3>
          <p>We assemble bespoke project taskforces drawing from permanent senior staff and specialized associates in geotechnical engineering, bridge hydraulics, environmental impact, and claims analysis.</p>
        </div>
        <div class="fact-card">
          <span class="fact-idx">PILLAR 03</span>
          <h3>Three Structured Departments</h3>
          <p>Structured into Engineering & Design, Operations & Contract Administration, and Quality Control & Site Supervision. Each unit operates with distinct responsibilities and stringent internal checks.</p>
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

      <!-- Two Flagship Showcases from File 1 -->
      <div class="featured-grid">
        <div class="feat-card">
          <div class="feat-img-wrap">
            <img src="''' + imgs[1] + ''''" alt="Reinforced concrete formwork and scaffolding at the Awash River bridge abutment" loading="lazy">
            <span class="feat-badge">Flagship Bridge</span>
          </div>
          <div class="feat-info">
            <h3>Awash River Bridge</h3>
            <span class="feat-client">Client: Oromiya Road Authority (ORA)</span>
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
            <img src="''' + imgs[2] + ''''" alt="Stone masonry retaining wall and drainage culvert formwork along the Ginchi-Danisa highway" loading="lazy">
            <span class="feat-badge">Classified Highway</span>
          </div>
          <div class="feat-info">
            <h3>Ginchi-Danisa Gravel Highway</h3>
            <span class="feat-client">Client: Oromiya Road Authority (ORA)</span>
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

      <!-- Master Project Register Table (Enhanced from File 2) -->
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
            12 projects · 128.8 km of classified road delivered
          </div>
        </div>

        <!-- Graduated Distance Ruler -->
        <div class="ruler-bar">
          <div>Ref</div>
          <div>Project Name & Scope</div>
          <div class="ruler-scale">
            <span>0 km</span>
            <span>5 km</span>
            <span>10 km</span>
            <span>15 km</span>
            <span>20 km</span>
            <span>25+ km</span>
          </div>
          <div style="text-align: right;">Metric</div>
        </div>

        <!-- Ledger Rows -->
        <div class="reg-list" id="regList">
          <!-- Populated by JS -->
        </div>

        <p class="reg-footnote">
          * Blue bars denote road alignment length in kilometres. Red bars denote girder bridge span in metres. All works commissioned by the Oromiya Road Authority.
        </p>
      </div>
    </div>
  </section>

  <!-- ================= SITE RECORDS & GALLERY (ALL 10 REAL PHOTOS) ================= -->
  <section id="records">
    <div class="wrap">
      <div class="sec-head">
        <span class="sec-tag">Field Documentation</span>
        <h2>Site Records & Field Evidence</h2>
        <p class="sec-lead">Select any plate to examine high-resolution field photographs of our earthworks, structural concrete, hydraulic drainage, and finished surfaces.</p>
      </div>

      <div class="gallery-grid" id="galleryGrid">
        <button class="plate-card" data-idx="0" aria-label="Open Plate 01: Sub-base Compaction">
          <div class="plate-img-wrap">
            <img src="''' + imgs[0] + ''''" alt="Heavy road roller compacting sub-base gravel on site" loading="lazy">
            <span class="plate-overlay">PLATE 01</span>
          </div>
          <div class="plate-body">
            <h4>Sub-base Compaction</h4>
            <p>Vibratory compaction of selected gravel base layer.</p>
          </div>
        </button>

        <button class="plate-card" data-idx="1" aria-label="Open Plate 02: Bridge Abutment Falsework">
          <div class="plate-img-wrap">
            <img src="''' + imgs[1] + ''''" alt="Reinforced concrete formwork and scaffolding at bridge abutment" loading="lazy">
            <span class="plate-overlay">PLATE 02</span>
          </div>
          <div class="plate-body">
            <h4>Bridge Abutment Falsework</h4>
            <p>Formwork and safety scaffolding at Awash Bridge.</p>
          </div>
        </button>

        <button class="plate-card" data-idx="2" aria-label="Open Plate 03: Hydraulic Masonry Structure">
          <div class="plate-img-wrap">
            <img src="''' + imgs[2] + ''''" alt="Stone masonry and formwork at drainage structure" loading="lazy">
            <span class="plate-overlay">PLATE 03</span>
          </div>
          <div class="plate-body">
            <h4>Hydraulic Drainage Culvert</h4>
            <p>Mortared stone masonry headwall on Ginchi-Danisa road.</p>
          </div>
        </button>

        <button class="plate-card" data-idx="3" aria-label="Open Plate 04: Hillside Road Cut">
          <div class="plate-img-wrap">
            <img src="''' + imgs[3] + ''''" alt="Excavator working on steep hillside rock and soil cut" loading="lazy">
            <span class="plate-overlay">PLATE 04</span>
          </div>
          <div class="plate-body">
            <h4>Hillside Bench Excavation</h4>
            <p>Heavy crawler excavator carving new road bench.</p>
          </div>
        </button>

        <button class="plate-card" data-idx="4" aria-label="Open Plate 05: Finished Gravel Alignment">
          <div class="plate-img-wrap">
            <img src="''' + imgs[4] + ''''" alt="Finished DC-2 gravel highway winding smoothly through Oromia hills" loading="lazy">
            <span class="plate-overlay">PLATE 05</span>
          </div>
          <div class="plate-body">
            <h4>Finished Gravel Alignment</h4>
            <p>Completed all-weather DC-2 carriageway through hills.</p>
          </div>
        </button>

        <button class="plate-card" data-idx="5" aria-label="Open Plate 06: Stone Masonry Culvert">
          <div class="plate-img-wrap">
            <img src="''' + imgs[5] + ''''" alt="Finished stone masonry box culvert beside gravel road" loading="lazy">
            <span class="plate-overlay">PLATE 06</span>
          </div>
          <div class="plate-body">
            <h4>Stone Masonry Culvert</h4>
            <p>Constructed cross-drainage culvert and catchpit.</p>
          </div>
        </button>

        <button class="plate-card" data-idx="6" aria-label="Open Plate 07: Stream Crossing Works">
          <div class="plate-img-wrap">
            <img src="''' + imgs[6] + ''''" alt="Site crew executing foundation excavation at river stream crossing" loading="lazy">
            <span class="plate-overlay">PLATE 07</span>
          </div>
          <div class="plate-body">
            <h4>Stream Crossing Foundation</h4>
            <p>Crew preparing foundation and water diversion channel.</p>
          </div>
        </button>

        <button class="plate-card" data-idx="7" aria-label="Open Plate 08: Deep Foundation Excavation">
          <div class="plate-img-wrap">
            <img src="''' + imgs[7] + ''''" alt="Yellow heavy excavator excavating deep footing for bridge pier" loading="lazy">
            <span class="plate-overlay">PLATE 08</span>
          </div>
          <div class="plate-body">
            <h4>Substructure Foundation</h4>
            <p>Excavator deepening footing to competent bedrock.</p>
          </div>
        </button>

        <button class="plate-card" data-idx="8" aria-label="Open Plate 09: Concrete Retaining Wall">
          <div class="plate-img-wrap">
            <img src="''' + imgs[8] + ''''" alt="Cast reinforced concrete drainage retaining wall alongside road" loading="lazy">
            <span class="plate-overlay">PLATE 09</span>
          </div>
          <div class="plate-body">
            <h4>Concrete Retaining Wall</h4>
            <p>Monolithic concrete wall for slope and ditch retention.</p>
          </div>
        </button>

        <button class="plate-card" data-idx="9" aria-label="Open Plate 10: Gabion Slope Protection">
          <div class="plate-img-wrap">
            <img src="''' + imgs[9] + ''''" alt="Heavy wire-mesh stone gabion wall constructed along embankment toe" loading="lazy">
            <span class="plate-overlay">PLATE 10</span>
          </div>
          <div class="plate-body">
            <h4>Gabion Slope Protection</h4>
            <p>Stone-filled wire gabions preventing bank erosion.</p>
          </div>
        </button>

        <button class="plate-card" data-idx="10" aria-label="Open Plate 11: Bridge Deck Reinforcement">
          <div class="plate-img-wrap">
            <img src="''' + imgs[10] + ''''" alt="High-tensile reinforcement steel rebar grid laid out for bridge deck casting" loading="lazy">
            <span class="plate-overlay">PLATE 11</span>
          </div>
          <div class="plate-body">
            <h4>Bridge Deck Rebar Grid</h4>
            <p>High-tensile steel reinforcement prior to concrete pour.</p>
          </div>
        </button>
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
        <!-- SVG Stamp from File 2 -->
        <div class="stamp-box">
          <svg viewBox="0 0 170 170" class="stamp" role="img" aria-label="Official Category 1 Highway and Bridge Consultant Stamp">
            <circle cx="85" cy="85" r="80" fill="none" stroke="currentColor" stroke-width="4"/>
            <circle cx="85" cy="85" r="68" fill="none" stroke="currentColor" stroke-width="1.5"/>
            <text x="85" y="58" font-size="14">CATEGORY</text>
            <text x="85" y="112" font-size="62">1</text>
            <text x="85" y="134" font-size="11">HIGHWAY & BRIDGE</text>
          </svg>
          <div class="stamp-caption">Highest National Grade</div>
          <div class="stamp-sub">Federal Ministry of Construction</div>
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
            <span class="chip">EBCS Standards</span>
            <span class="chip">Eurocodes</span>
            <span class="chip">Ethiopian Standards Code</span>
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
              <span><strong>Addis Ababa Trade & Industry Bureau:</strong> Principal Commercial Trade License</span>
            </li>
            <li>
              <span class="lic-check">✓</span>
              <span><strong>City Administration of Addis Ababa:</strong> Business Registration Certificate</span>
            </li>
            <li>
              <span class="lic-check">✓</span>
              <span><strong>Ministry of Revenues:</strong> Value Added Tax (VAT) Registration</span>
            </li>
            <li>
              <span class="lic-check">✓</span>
              <span><strong>Federal Tax Authority:</strong> Taxpayer Identification Number (TIN)</span>
            </li>
            <li>
              <span class="lic-check">✓</span>
              <span><strong>Public Procurement Authority (FPPA):</strong> Registered Consultants List</span>
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
              Katekse Building, 3rd Floor<br>
              Adwa Square (near Adwa Bridge)<br>
              Yeka Sub City, Woreda 07<br>
              Addis Ababa, Ethiopia
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
    <div style="display: flex; align-items: center; gap: 0.75rem;">
      <svg width="24" height="24" viewBox="0 0 34 34" fill="none" aria-hidden="true">
        <path d="M8 3v28M8 28h24M10 6l20 20H10z" stroke="#ffffff" stroke-width="2.4"/>
        <path d="M13 12l9 9h-9z" fill="#ff5e54"/>
      </svg>
      <span>© 2026 Axulal Consulting Engineers PLC. All rights reserved.</span>
    </div>

    <div class="ftr-motto">Conquering Possibilities!!</div>

    <a href="#top" class="back-to-top">
      Back to Top
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 15l-6-6-6 6"/></svg>
    </a>
  </div>
</footer>

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
// --- Project Database ---
const PROJECTS = [
  ["Ginchi-Danisa Gravel Road", 15.5, "road", "Design + supervision"],
  ["Asgori-Kotoba Gravel Road, Lots 1 and 2", 22.5, "road", "Design + supervision"],
  ["Awash-Horota-Tululuba Gravel Road", 11.0, "road", "Design + supervision"],
  ["Gallesa-Kebabereda-Keteketa Gravel Road", 10.3, "road", "Design + supervision"],
  ["Olenkomy-Awash Gravel Road", 6.5, "road", "Design + supervision"],
  ["Awash Bridge, 24 m girder", 24.0, "bridge", "Design + supervision"],
  ["Ejere-Arertu Gravel Road", 27.0, "road", "Design + supervision"],
  ["Ejere-Kussaye-Goli Gravel Road", 9.0, "road", "Design + supervision"],
  ["Ejere-Hidi-Ibu Gravel Road", 14.0, "road", "Design + supervision"],
  ["Ejere-Endode Gravel Road", 6.5, "road", "Design + supervision"],
  ["Berga Bridge, 22 m girder", 22.0, "bridge", "Supervision only"],
  ["Werkakore-Bujiroo Gravel Road", 6.0, "road", "Design + supervision"]
];

// --- Render Project Register ---
const regList = document.getElementById("regList");
const regSummary = document.getElementById("regSummary");
const regSearch = document.getElementById("regSearch");
let currentFilter = "all";

function renderProjects() {
  const query = regSearch.value.trim().toLowerCase();
  regList.innerHTML = "";
  let totalKm = 0;
  let count = 0;

  PROJECTS.forEach((p, idx) => {
    const isBridge = p[2] === "bridge";
    const matchesFilter = currentFilter === "all" || p[2] === currentFilter;
    const matchesSearch = p[0].toLowerCase().includes(query) || p[3].toLowerCase().includes(query);

    if (matchesFilter && matchesSearch) {
      count++;
      if (!isBridge) totalKm += p[1];

      const row = document.createElement("div");
      row.className = "reg-row";
      const ref = "P-" + String(idx + 1).padStart(2, "0");
      const pct = Math.min(100, (p[1] / 27.0) * 100);

      row.innerHTML = `
        <div class="reg-ref">${ref}</div>
        <div class="reg-title">
          <b>${p[0]}</b>
          <small>${p[3]} · Oromiya Road Authority</small>
        </div>
        <div class="reg-bar-wrap">
          <div class="reg-bar-fill${isBridge ? ' bridge' : ''}" style="width: ${pct}%;"></div>
        </div>
        <div class="reg-value">${p[1]} ${isBridge ? 'm' : 'km'}</div>
      `;
      regList.appendChild(row);
    }
  });

  regSummary.textContent = `${count} projects shown · ${totalKm.toFixed(1)} km of classified road`;
}

renderProjects();

// Filter buttons
document.querySelectorAll(".filter-btn").forEach(btn => {
  btn.onclick = () => {
    document.querySelectorAll(".filter-btn").forEach(b => b.setAttribute("aria-pressed", "false"));
    btn.setAttribute("aria-pressed", "true");
    currentFilter = btn.dataset.filter;
    renderProjects();
  };
});

regSearch.oninput = () => renderProjects();

// --- Services Tab System ---
const SERVICES = [
  {
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
  },
  {
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
  },
  {
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
  },
  {
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
  }
];

const svcTabBtns = document.querySelectorAll(".svc-tab-btn");
const svcPanel = document.getElementById("svcPanel");

function setServiceTab(idx) {
  svcTabBtns.forEach((btn, i) => btn.setAttribute("aria-selected", i === idx));
  const s = SERVICES[idx];
  svcPanel.innerHTML = `
    <div class="svc-panel-head">
      <svg viewBox="0 0 44 44"><path d="${s.svg}"/></svg>
      <h3>${s.title}</h3>
    </div>
    <p class="svc-panel-desc">${s.lead}</p>
    <ul class="svc-sublist">
      ${s.items.map(it => `<li>${it}</li>`).join("")}
    </ul>
  `;
}

svcTabBtns.forEach((btn, i) => {
  btn.onclick = () => setServiceTab(i);
});
setServiceTab(0);

// View switcher (Tabs vs Grid)
const btnTabView = document.getElementById("btnTabView");
const btnGridView = document.getElementById("btnGridView");
const svcTabView = document.getElementById("svcTabView");
const svcGridView = document.getElementById("svcGridView");

btnTabView.onclick = () => {
  btnTabView.classList.add("active");
  btnGridView.classList.remove("active");
  svcTabView.style.display = "grid";
  svcGridView.classList.remove("active");
};

btnGridView.onclick = () => {
  btnGridView.classList.add("active");
  btnTabView.classList.remove("active");
  svcTabView.style.display = "none";
  svcGridView.classList.add("active");
};

// --- Hero Visual Showcase Switcher ---
const btnShowProfile = document.getElementById("btnShowProfile");
const btnShowPhoto = document.getElementById("btnShowPhoto");
const panelProfile = document.getElementById("panelProfile");
const panelPhoto = document.getElementById("panelPhoto");

btnShowProfile.onclick = () => {
  btnShowProfile.classList.add("active");
  btnShowPhoto.classList.remove("active");
  panelProfile.classList.add("active");
  panelPhoto.classList.remove("active");
};

btnShowPhoto.onclick = () => {
  btnShowPhoto.classList.add("active");
  btnShowProfile.classList.remove("active");
  panelPhoto.classList.add("active");
  panelProfile.classList.remove("active");
};

// --- Light / Dark Theme Switcher ---
const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");

function updateThemeIcon(isDark) {
  if (isDark) {
    themeIcon.innerHTML = `<path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" fill="currentColor"/>`;
  } else {
    themeIcon.innerHTML = `<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>`;
  }
}

// Initialize theme from storage or system
const savedTheme = localStorage.getItem("axulal-theme");
const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
const initialDark = savedTheme ? savedTheme === "dark" : systemPrefersDark;

if (savedTheme) {
  document.documentElement.setAttribute("data-theme", savedTheme);
}
updateThemeIcon(initialDark);

themeToggle.onclick = () => {
  const current = document.documentElement.getAttribute("data-theme");
  const isDarkNow = current === "dark" || (!current && systemPrefersDark);
  const nextTheme = isDarkNow ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", nextTheme);
  localStorage.setItem("axulal-theme", nextTheme);
  updateThemeIcon(nextTheme === "dark");
};

// --- Mobile Navigation Menu ---
const menuToggle = document.getElementById("menuToggle");
const nav = document.getElementById("nav");

function toggleMenu(open) {
  const isOpen = typeof open === "boolean" ? open : !nav.classList.contains("open");
  nav.classList.toggle("open", isOpen);
  menuToggle.setAttribute("aria-expanded", String(isOpen));
}

menuToggle.onclick = () => toggleMenu();
nav.querySelectorAll("a").forEach(a => {
  a.onclick = () => toggleMenu(false);
});
document.addEventListener("keydown", e => {
  if (e.key === "Escape") toggleMenu(false);
});

// --- Header Scroll Effect & ScrollSpy ---
const hd = document.getElementById("hd");
window.addEventListener("scroll", () => {
  hd.classList.toggle("sc", window.scrollY > 10);
}, { passive: true });

if ("IntersectionObserver" in window) {
  const navLinks = nav.querySelectorAll("a");
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navLinks.forEach(link => {
          link.classList.toggle("on", link.getAttribute("href") === "#" + id);
        });
      }
    });
  }, { rootMargin: "-35% 0px -45% 0px" });

  ["about", "services", "stations", "projects", "records", "credentials", "contact"].forEach(id => {
    const el = document.getElementById(id);
    if (el) observer.observe(el);
  });
}

// --- Lightbox Dialog for All 10 Plates ---
const PLATES = [
  { title: "Plate 01: Sub-base Compaction", desc: "Heavy vibratory road roller compacting gravel sub-base on an active project site." },
  { title: "Plate 02: Bridge Abutment Falsework", desc: "Reinforced concrete formwork and scaffolding at the Awash River bridge abutment." },
  { title: "Plate 03: Hydraulic Drainage Structure", desc: "Stone masonry wingwalls and formwork at drainage structure on the Ginchi-Danisa road." },
  { title: "Plate 04: Hillside Road Cut", desc: "Heavy excavator carving through rock and clay hillside bench along alignment." },
  { title: "Plate 05: Finished Gravel Alignment", desc: "Completed DC-2 gravel carriageway smoothly winding through Ethiopian rural terrain." },
  { title: "Plate 06: Stone Masonry Culvert", desc: "Hand-dressed stone masonry culvert headwall and roadside runoff ditch." },
  { title: "Plate 07: Stream Crossing Works", desc: "Site engineers and construction crew executing foundation prep at river stream crossing." },
  { title: "Plate 08: Deep Foundation Excavation", desc: "Hydraulic crawler excavator establishing bridge pier footing down to sound stratum." },
  { title: "Plate 09: Concrete Retaining Wall", desc: "Cast-in-place reinforced concrete retaining wall for slope stabilization." },
  { title: "Plate 10: Gabion Embankment Protection", desc: "Wire mesh stone gabion mattresses stabilizing vulnerable hillside fill." },
  { title: "Plate 11: Bridge Deck Reinforcement", desc: "High-tensile reinforcement steel rebar grid laid out for bridge deck concrete pour." }
];

const lb = document.getElementById("lb");
const lbImg = document.getElementById("lbImg");
const lbCaption = document.getElementById("lbCaption");
const lbCounter = document.getElementById("lbCounter");
const lbClose = document.getElementById("lbClose");
const lbPrev = document.getElementById("lbPrev");
const lbNext = document.getElementById("lbNext");
let currentPlateIdx = 0;

const plateButtons = document.querySelectorAll(".plate-card");

function openLightbox(idx) {
  currentPlateIdx = idx;
  const btn = plateButtons[idx];
  const img = btn.querySelector("img");
  lbImg.src = img.src;
  lbImg.alt = img.alt;
  lbCaption.textContent = PLATES[idx].title + " — " + PLATES[idx].desc;
  lbCounter.textContent = (idx + 1) + " / " + plateButtons.length;
  lb.showModal();
}

plateButtons.forEach((btn, idx) => {
  btn.onclick = () => openLightbox(idx);
});

lbClose.onclick = () => lb.close();
lb.onclick = e => {
  if (e.target === lb) lb.close();
};

lbPrev.onclick = () => {
  const prevIdx = (currentPlateIdx - 1 + plateButtons.length) % plateButtons.length;
  openLightbox(prevIdx);
};

lbNext.onclick = () => {
  const nextIdx = (currentPlateIdx + 1) % plateButtons.length;
  openLightbox(nextIdx);
};

document.addEventListener("keydown", e => {
  if (!lb.open) return;
  if (e.key === "ArrowLeft") lbPrev.click();
  if (e.key === "ArrowRight") lbNext.click();
});

// --- Copy to Clipboard Utility ---
function copyText(text, btnEl) {
  navigator.clipboard.writeText(text).then(() => {
    const original = btnEl.textContent;
    btnEl.textContent = "Copied!";
    btnEl.style.background = "#1c5ec2";
    setTimeout(() => {
      btnEl.textContent = original;
      btnEl.style.background = "";
    }, 2000);
  }).catch(() => {
    prompt("Copy to clipboard:", text);
  });
}

// --- Contact Form Submission ---
const contactForm = document.getElementById("contactForm");
const formFeedback = document.getElementById("formFeedback");

contactForm.onsubmit = e => {
  e.preventDefault();
  const name = document.getElementById("formName").value.trim();
  const contact = document.getElementById("formContact").value.trim();
  const service = document.getElementById("formService").value;
  const message = document.getElementById("formMessage").value.trim();

  const body = `Name/Organization: ${name}
Contact Details: ${contact}
Service Required: ${service}

Project Description:
${message}`;

  formFeedback.textContent = "Preparing dispatch to axulalconsulting@gmail.com...";
  
  const mailtoUrl = `mailto:axulalconsulting@gmail.com?subject=${encodeURIComponent("Proposal Request: " + service + " - " + name)}&body=${encodeURIComponent(body)}`;
  
  setTimeout(() => {
    window.location.href = mailtoUrl;
    formFeedback.textContent = "Email client opened! If your email app did not launch automatically, please email us directly at axulalconsulting@gmail.com.";
  }, 400);
};
</script>
</body>
</html>
''')

    full_html = "".join(html_parts)

    print("Writing index.html...")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(full_html)

    print("Writing Axulal Consulting Engineers PLC _ Master.html...")
    with open("Axulal Consulting Engineers PLC _ Master.html", "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Success! Master website created ({len(full_html):,} bytes).")

if __name__ == "__main__":
    main()
