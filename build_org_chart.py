import os
import subprocess
import sys

def get_svg_content():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1300 860" width="100%" height="100%" style="background-color: #FFFFFF; font-family: 'Archivo', 'Segoe UI', system-ui, -apple-system, sans-serif;">
  <defs>
    <!-- Card and Header Gradients -->
    <linearGradient id="carbonGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#282320" />
      <stop offset="100%" stop-color="#141210" />
    </linearGradient>

    <linearGradient id="violetGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#5B2E98" />
      <stop offset="50%" stop-color="#4A2882" />
      <stop offset="100%" stop-color="#381D66" />
    </linearGradient>

    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>

    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#F8FAFC" />
    </linearGradient>

    <!-- Refined Drop Shadows -->
    <filter id="softCardShadow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="rgba(15,23,42,0.07)" />
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="rgba(15,23,42,0.04)" />
    </filter>

    <filter id="violetGlow" x="-15%" y="-15%" width="130%" height="135%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="rgba(74,40,130,0.28)" />
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="rgba(74,40,130,0.15)" />
    </filter>
  </defs>

  <!-- Architectural Canvas Grid Pattern -->
  <g stroke="#E2E8F0" stroke-width="0.8" opacity="0.65">
    <line x1="60" y1="0" x2="60" y2="860" stroke-dasharray="3 3" />
    <line x1="247" y1="0" x2="247" y2="860" stroke-dasharray="3 3" />
    <line x1="650" y1="0" x2="650" y2="860" stroke-dasharray="3 3" />
    <line x1="1053" y1="0" x2="1053" y2="860" stroke-dasharray="3 3" />
    <line x1="1240" y1="0" x2="1240" y2="860" stroke-dasharray="3 3" />
    <line x1="0" y1="90" x2="1300" y2="90" stroke-dasharray="3 3" />
    <line x1="0" y1="230" x2="1300" y2="230" stroke-dasharray="3 3" />
    <line x1="0" y1="340" x2="1300" y2="340" stroke-dasharray="3 3" />
    <line x1="0" y1="650" x2="1300" y2="650" stroke-dasharray="3 3" />
  </g>

  <!-- ================= TOP HEADER BANNER ================= -->
  <g transform="translate(60, 28)">
    <!-- Axulal Interlocking Chevron Monogram Emblem -->
    <g transform="translate(0, 4) scale(0.12)">
      <path d="M 384 60 L 417 117 L 263 384 L 455 384 L 491 446 L 225 446 A 35 35 0 0 1 190 396 Z" fill="#000000" />
      <path d="M 444 172 L 602 446 L 526 446 L 444 304 L 362 446 L 286 446 Z" fill="#4D2E7E" />
    </g>

    <g transform="translate(85, 14)">
      <text font-size="11" font-weight="800" fill="#D97706" letter-spacing="2.5" font-family="'JetBrains Mono', monospace">AXULAL CONSULTING ENGINEERS PLC</text>
      <text y="24" font-size="21" font-weight="900" fill="#0F172A" letter-spacing="-0.5">Corporate Governance &amp; Operational Hierarchy</text>
    </g>

    <!-- Certification Badges on Top Right -->
    <g transform="translate(1180, 16)" text-anchor="end">
      <rect x="-240" y="-3" width="240" height="28" rx="6" fill="#F5F0FA" stroke="rgba(74,40,130,0.25)" stroke-width="1.2" />
      <circle cx="-225" cy="11" r="4" fill="#4A2882" />
      <text x="-10" y="15" font-size="10.5" font-weight="800" fill="#4A2882" font-family="'JetBrains Mono', monospace" letter-spacing="0.5">CATEGORY-1 ROAD &amp; BRIDGE</text>
      <text x="0" y="38" font-size="9.5" font-weight="600" fill="#64748B" font-family="'JetBrains Mono', monospace">MoWUD &amp; ERA ACCREDITED GOVERNANCE</text>
    </g>
  </g>

  <!-- ================= STRUCTURAL PIPELINE CONNECTORS ================= -->
  <!-- Arterial Hierarchy Bus Lines -->
  <g stroke="#4A2882" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <!-- Shareholders to General Manager -->
    <path d="M 650 152 L 650 188" />

    <!-- General Manager to Distribution Bar -->
    <path d="M 650 274 L 650 324" />

    <!-- Horizontal Distribution Bar across 3 Operational Departments -->
    <path d="M 247 324 L 1053 324" />

    <!-- Drops to the 3 Department cards -->
    <path d="M 247 324 L 247 358" />
    <path d="M 650 324 L 650 358" />
    <path d="M 1053 324 L 1053 358" />
  </g>

  <!-- Lower Convergence Bus: 3 Departments converge down to Projects Base -->
  <g stroke="#94A3B8" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <!-- Drops from bottom of 3 departments (y=628 to y=662) -->
    <path d="M 247 628 L 247 662" />
    <path d="M 650 628 L 650 662" />
    <path d="M 1053 628 L 1053 662" />

    <!-- Horizontal Convergence Bar -->
    <path d="M 247 662 L 1053 662" />

    <!-- Final Drop into Projects Base -->
    <path d="M 650 662 L 650 696" />
  </g>

  <!-- Side Advisory Branch: GM to Internal Audit & QA (Dashed line) -->
  <path d="M 410 231 L 280 231" stroke="#64748B" stroke-width="2" stroke-dasharray="5 4" fill="none" />

  <!-- Connector Node Hubs (Dots with white inner ring) -->
  <g fill="#4A2882">
    <circle cx="650" cy="188" r="4.5" />
    <circle cx="650" cy="324" r="5.5" fill="#D97706" />
    <circle cx="247" cy="324" r="4.5" />
    <circle cx="1053" cy="324" r="4.5" />
    <circle cx="247" cy="358" r="4" />
    <circle cx="650" cy="358" r="4" />
    <circle cx="1053" cy="358" r="4" />
    
    <!-- Lower convergence nodes -->
    <circle cx="247" cy="662" r="4" fill="#64748B" />
    <circle cx="650" cy="662" r="5" fill="#64748B" />
    <circle cx="1053" cy="662" r="4" fill="#64748B" />
    <circle cx="650" cy="696" r="4.5" fill="#24201D" />
  </g>


  <!-- ================= LEVEL 1: SHAREHOLDERS ================= -->
  <g transform="translate(450, 92)" filter="url(#softCardShadow)">
    <rect width="400" height="60" rx="10" fill="url(#carbonGrad)" stroke="#3D3632" stroke-width="1.5" />
    
    <!-- Icon Container: Pediment / Governance Temple Vector Icon -->
    <rect x="14" y="12" width="36" height="36" rx="8" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.12)" />
    <g transform="translate(22, 19)" stroke="#F59E0B" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M 2 8 L 10 2 L 18 8 Z" fill="rgba(245,158,11,0.2)" />
      <line x1="1" y1="8" x2="19" y2="8" />
      <line x1="4" y1="8" x2="4" y2="18" />
      <line x1="8" y1="8" x2="8" y2="18" />
      <line x1="12" y1="8" x2="12" y2="18" />
      <line x1="16" y1="8" x2="16" y2="18" />
      <line x1="1" y1="18" x2="19" y2="18" />
    </g>

    <g transform="translate(62, 26)">
      <text font-size="15" font-weight="900" fill="#FFFFFF" letter-spacing="1.2">SHAREHOLDERS</text>
      <text y="17" font-size="10.5" font-weight="700" fill="#FBBF24" letter-spacing="0.5">OWNERSHIP &amp; STRATEGIC GOVERNANCE</text>
    </g>

    <!-- Authority Badge -->
    <rect x="290" y="18" width="96" height="24" rx="5" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.1)" />
    <text x="338" y="34" font-size="9" font-weight="800" fill="#E2E8F0" text-anchor="middle" font-family="'JetBrains Mono', monospace">SUPREME DESK</text>
  </g>


  <!-- ================= ADVISORY WING: INTERNAL AUDIT & QA ================= -->
  <g transform="translate(60, 199)" filter="url(#softCardShadow)">
    <rect width="220" height="64" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" stroke-dasharray="4 3" />
    
    <!-- Shield / Audit Icon -->
    <rect x="12" y="14" width="36" height="36" rx="6" fill="#EFF6FF" stroke="#BFDBFE" />
    <g transform="translate(20, 22)" stroke="#2563EB" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M 10 2 L 18 5 V 11 C 18 16 10 20 10 20 C 10 20 2 16 2 11 V 5 Z" fill="rgba(37,99,235,0.1)" />
      <polyline points="6 11 9 14 14 8" />
    </g>

    <g transform="translate(58, 26)">
      <text font-size="11.5" font-weight="900" fill="#0F172A">INTERNAL AUDIT &amp; QA</text>
      <text y="15" font-size="9.5" font-weight="700" fill="#64748B">Independent Oversight</text>
      <text y="27" font-size="8.5" font-weight="600" fill="#94A3B8" font-family="'JetBrains Mono', monospace">ISO/QMS &amp; Statutory Desk</text>
    </g>
  </g>


  <!-- ================= LEVEL 2: GENERAL MANAGER ================= -->
  <g transform="translate(410, 188)" filter="url(#violetGlow)">
    <rect width="480" height="86" rx="12" fill="url(#violetGrad)" stroke="#8B5CF6" stroke-width="2" />
    
    <!-- Executive Star-Shield Vector Icon -->
    <rect x="18" y="17" width="52" height="52" rx="10" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.2)" />
    <g transform="translate(28, 26)" stroke="#FFFFFF" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="16" cy="12" r="6" fill="rgba(255,255,255,0.2)" />
      <path d="M 6 30 C 6 24 10 20 16 20 C 22 20 26 24 26 30" />
      <path d="M 23 15 L 29 17 L 27 23" stroke="#FBBF24" />
    </g>

    <g transform="translate(86, 36)">
      <text font-size="18" font-weight="900" fill="#FFFFFF" letter-spacing="1">GENERAL MANAGER</text>
      <text y="21" font-size="11" font-weight="600" fill="#F1F5F9" letter-spacing="0.3">EXECUTIVE LEADERSHIP &amp; STATUTORY REPRESENTATIVE</text>
      <text y="36" font-size="9.5" font-weight="600" fill="#DDD6FE" font-family="'JetBrains Mono', monospace">Senior Highway &amp; Structural Engineer</text>
    </g>

    <!-- Experience Badge -->
    <rect x="368" y="16" width="96" height="26" rx="6" fill="rgba(0,0,0,0.3)" stroke="rgba(251,191,36,0.5)" stroke-width="1.2" />
    <text x="416" y="33" font-size="10.5" font-weight="900" fill="#FBBF24" text-anchor="middle" font-family="'JetBrains Mono', monospace">17+ YRS EXP</text>
  </g>


  <!-- ================= LEVEL 3: THREE STRATEGIC OPERATIONAL DEPARTMENTS ================= -->

  <!-- 1. DESIGN DEPARTMENT (Violet Brand Theme) -->
  <g transform="translate(60, 358)" filter="url(#softCardShadow)">
    <rect width="374" height="270" rx="12" fill="url(#cardGrad)" stroke="#CBD5E1" stroke-width="1.5" />
    
    <!-- Header Block -->
    <rect width="374" height="66" rx="12" fill="#F5F0FA" />
    <rect x="0" y="52" width="374" height="14" fill="#F5F0FA" />
    <line x1="0" y1="66" x2="374" y2="66" stroke="#DDD6FE" stroke-width="1.5" />

    <!-- Drafting Compass & Ruler Vector Icon -->
    <rect x="18" y="15" width="36" height="36" rx="8" fill="#FFFFFF" stroke="rgba(74,40,130,0.25)" stroke-width="1.2" />
    <g transform="translate(24, 21)" stroke="#4A2882" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="5" r="3" />
      <path d="M 6 20 L 10 7 L 14 7 L 18 20" />
      <line x1="8" y1="14" x2="16" y2="14" />
      <line x1="4" y1="20" x2="20" y2="20" stroke-width="1.5" />
    </g>

    <g transform="translate(66, 32)">
      <text font-size="14.5" font-weight="900" fill="#4A2882" letter-spacing="0.5">DESIGN DEPARTMENT</text>
      <text y="19" font-size="10.5" font-weight="700" fill="#6D39BE" letter-spacing="0.4">ENGINEERING, GEOMETRICS &amp; MODELING</text>
    </g>

    <!-- 5 Technical Competencies -->
    <g transform="translate(20, 88)" font-size="11.5" font-family="'Archivo', sans-serif">
      <!-- Bullet 1 -->
      <circle cx="7" cy="8" r="3.5" fill="#4A2882" />
      <text x="20" y="12" font-weight="700" fill="#1E293B">Highway Route Geometric Alignment</text>
      <text x="20" y="24" font-size="9.5" font-weight="500" fill="#64748B">Terrain modeling, profile grades &amp; super-elevation</text>

      <!-- Bullet 2 -->
      <circle cx="7" cy="44" r="3.5" fill="#4A2882" />
      <text x="20" y="48" font-weight="700" fill="#1E293B">Structural Bridge &amp; Hydraulic Culverts</text>
      <text x="20" y="60" font-size="9.5" font-weight="500" fill="#64748B">RC box culverts, multi-span decks &amp; abutments</text>

      <!-- Bullet 3 -->
      <circle cx="7" cy="80" r="3.5" fill="#4A2882" />
      <text x="20" y="84" font-weight="700" fill="#1E293B">Hydrology &amp; Catchment Runoff Sizing</text>
      <text x="20" y="96" font-size="9.5" font-weight="500" fill="#64748B">50-yr flood frequency &amp; drainage discharge modeling</text>

      <!-- Bullet 4 -->
      <circle cx="7" cy="116" r="3.5" fill="#4A2882" />
      <text x="20" y="120" font-weight="700" fill="#1E293B">Geotechnical Soil CBR &amp; Quarry Surveys</text>
      <text x="20" y="132" font-size="9.5" font-weight="500" fill="#64748B">Subgrade strength, borrow pits &amp; pavement layers</text>

      <!-- Bullet 5 -->
      <circle cx="7" cy="152" r="3.5" fill="#4A2882" />
      <text x="20" y="156" font-weight="700" fill="#1E293B">Civil 3D Modeling &amp; CAD Detailing</text>
      <text x="20" y="168" font-size="9.5" font-weight="500" fill="#64748B">High-precision corridor cross-sections &amp; tender plans</text>
    </g>
  </g>


  <!-- 2. CONTRACT ADMINISTRATION DEPARTMENT (Amber Theme) -->
  <g transform="translate(463, 358)" filter="url(#softCardShadow)">
    <rect width="374" height="270" rx="12" fill="url(#cardGrad)" stroke="#CBD5E1" stroke-width="1.5" />
    
    <!-- Header Block -->
    <rect width="374" height="66" rx="12" fill="#FFFBEB" />
    <rect x="0" y="52" width="374" height="14" fill="#FFFBEB" />
    <line x1="0" y1="66" x2="374" y2="66" stroke="#FDE68A" stroke-width="1.5" />

    <!-- Contract Clipboard Vector Icon -->
    <rect x="18" y="15" width="36" height="36" rx="8" fill="#FFFFFF" stroke="rgba(217,119,6,0.3)" stroke-width="1.2" />
    <g transform="translate(25, 21)" stroke="#D97706" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <rect x="3" y="5" width="16" height="18" rx="2" />
      <path d="M 8 5 V 2 H 14 V 5" />
      <line x1="7" y1="10" x2="15" y2="10" />
      <line x1="7" y1="14" x2="15" y2="14" />
      <line x1="7" y1="18" x2="11" y2="18" />
    </g>

    <g transform="translate(66, 32)">
      <text font-size="14.5" font-weight="900" fill="#D97706" letter-spacing="0.5">CONTRACT ADMINISTRATION</text>
      <text y="19" font-size="10.5" font-weight="700" fill="#B45309" letter-spacing="0.4">TENDERS, BOQ, PROCUREMENT &amp; CLAIMS</text>
    </g>

    <!-- 5 Technical Competencies -->
    <g transform="translate(20, 88)" font-size="11.5" font-family="'Archivo', sans-serif">
      <!-- Bullet 1 -->
      <circle cx="7" cy="8" r="3.5" fill="#D97706" />
      <text x="20" y="12" font-weight="700" fill="#1E293B">Standard Bidding Documents (SBD/PPA)</text>
      <text x="20" y="24" font-size="9.5" font-weight="500" fill="#64748B">FIDIC conditions, MoWUD clauses &amp; special specs</text>

      <!-- Bullet 2 -->
      <circle cx="7" cy="44" r="3.5" fill="#D97706" />
      <text x="20" y="48" font-weight="700" fill="#1E293B">Detailed Quantity Take-Off &amp; BoQ</text>
      <text x="20" y="60" font-size="9.5" font-weight="500" fill="#64748B">Earthwork mass-haul, structural volumes &amp; unit rates</text>

      <!-- Bullet 3 -->
      <circle cx="7" cy="80" r="3.5" fill="#D97706" />
      <text x="20" y="84" font-weight="700" fill="#1E293B">Tender Evaluation &amp; Bid Dossiers</text>
      <text x="20" y="96" font-size="9.5" font-weight="500" fill="#64748B">Technical appraisals, financial scoring &amp; award reports</text>

      <!-- Bullet 4 -->
      <circle cx="7" cy="116" r="3.5" fill="#D97706" />
      <text x="20" y="120" font-weight="700" fill="#1E293B">IPC Measurement &amp; Payment Audits</text>
      <text x="20" y="132" font-size="9.5" font-weight="500" fill="#64748B">Monthly interim certificate verification &amp; retention</text>

      <!-- Bullet 5 -->
      <circle cx="7" cy="152" r="3.5" fill="#D97706" />
      <text x="20" y="156" font-weight="700" fill="#1E293B">Variation Orders &amp; Claims Governance</text>
      <text x="20" y="168" font-size="9.5" font-weight="500" fill="#64748B">Scope changes, time extension reviews &amp; handovers</text>
    </g>
  </g>


  <!-- 3. ADMINISTRATION & FINANCE DEPARTMENT (Precision Blue Theme) -->
  <g transform="translate(866, 358)" filter="url(#softCardShadow)">
    <rect width="374" height="270" rx="12" fill="url(#cardGrad)" stroke="#CBD5E1" stroke-width="1.5" />
    
    <!-- Header Block -->
    <rect width="374" height="66" rx="12" fill="#EFF6FF" />
    <rect x="0" y="52" width="374" height="14" fill="#EFF6FF" />
    <line x1="0" y1="66" x2="374" y2="66" stroke="#BFDBFE" stroke-width="1.5" />

    <!-- Briefcase / Corporate Icon -->
    <rect x="18" y="15" width="36" height="36" rx="8" fill="#FFFFFF" stroke="rgba(29,78,216,0.3)" stroke-width="1.2" />
    <g transform="translate(25, 21)" stroke="#1D4ED8" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <rect x="2" y="6" width="20" height="16" rx="2" />
      <path d="M 8 6 V 3 H 16 V 6" />
      <line x1="2" y1="12" x2="22" y2="12" />
      <circle cx="12" cy="12" r="1.5" fill="#1D4ED8" />
    </g>

    <g transform="translate(66, 32)">
      <text font-size="14.5" font-weight="900" fill="#1D4ED8" letter-spacing="0.5">ADMINISTRATION &amp; FINANCE</text>
      <text y="19" font-size="10.5" font-weight="700" fill="#1E40AF" letter-spacing="0.4">LOGISTICS, HR &amp; STATUTORY GOVERNANCE</text>
    </g>

    <!-- 5 Technical Competencies -->
    <g transform="translate(20, 88)" font-size="11.5" font-family="'Archivo', sans-serif">
      <!-- Bullet 1 -->
      <circle cx="7" cy="8" r="3.5" fill="#1D4ED8" />
      <text x="20" y="12" font-weight="700" fill="#1E293B">Corporate Accounting, Payroll &amp; Tax</text>
      <text x="20" y="24" font-size="9.5" font-weight="500" fill="#64748B">Statutory ERCA audits, project ledgers &amp; cash flows</text>

      <!-- Bullet 2 -->
      <circle cx="7" cy="44" r="3.5" fill="#1D4ED8" />
      <text x="20" y="48" font-weight="700" fill="#1E293B">Human Resources &amp; Capacity Development</text>
      <text x="20" y="60" font-size="9.5" font-weight="500" fill="#64748B">Professional onboarding, continuing education &amp; staff welfare</text>

      <!-- Bullet 3 -->
      <circle cx="7" cy="80" r="3.5" fill="#1D4ED8" />
      <text x="20" y="84" font-weight="700" fill="#1E293B">4x4 Fleet Operations &amp; Site Logistics</text>
      <text x="20" y="96" font-size="9.5" font-weight="500" fill="#64748B">Heavy-duty Toyota Hilux fleet &amp; field fuel replenishment</text>

      <!-- Bullet 4 -->
      <circle cx="7" cy="116" r="3.5" fill="#1D4ED8" />
      <text x="20" y="120" font-weight="700" fill="#1E293B">IT Workstations, Plotters &amp; Software</text>
      <text x="20" y="132" font-size="9.5" font-weight="500" fill="#64748B">HP DesignJet wide plotters, Autodesk Civil 3D &amp; backups</text>

      <!-- Bullet 5 -->
      <circle cx="7" cy="152" r="3.5" fill="#1D4ED8" />
      <text x="20" y="156" font-weight="700" fill="#1E293B">Statutory Licensing &amp; Legal Records</text>
      <text x="20" y="168" font-size="9.5" font-weight="500" fill="#64748B">Professional indemnity insurance, commercial registry &amp; archives</text>
    </g>
  </g>


  <!-- ================= LEVEL 4: BEDROCK / PROJECTS & RESIDENT SUPERVISION ================= -->
  <g transform="translate(60, 696)" filter="url(#softCardShadow)">
    <rect width="1180" height="114" rx="12" fill="url(#carbonGrad)" stroke="#3D3632" stroke-width="1.5" />
    
    <!-- Hardhat / Civil Construction Site Vector Icon -->
    <rect x="22" y="24" width="66" height="66" rx="10" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.12)" />
    <g transform="translate(35, 36)" stroke="#F59E0B" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M 4 24 C 4 14 12 8 20 8 C 28 8 36 14 36 24" fill="rgba(245,158,11,0.15)" />
      <line x1="2" y1="24" x2="38" y2="24" stroke-width="3" />
      <path d="M 12 8 V 3 H 28 V 8" />
      <circle cx="20" cy="16" r="2.5" fill="#F59E0B" />
    </g>

    <g transform="translate(104, 38)">
      <div style="display:flex; align-items:center; gap:8px;">
        <text font-size="17" font-weight="900" fill="#FFFFFF" letter-spacing="1">PROJECTS &amp; RESIDENT SITE OFFICES</text>
      </div>
      <text y="24" font-size="11" font-weight="600" fill="#CBD5E1" letter-spacing="0.4">FULL-TIME RESIDENT SUPERVISION • IN-SITU MATERIALS QUALITY TESTING • WORKMANSHIP QA</text>
      <text y="42" font-size="9.5" font-weight="700" fill="#FBBF24" font-family="'JetBrains Mono', monospace">DEPLOYED ACROSS ACTIVE HIGHWAY &amp; URBAN ROAD CORRIDORS NATIONWIDE</text>
    </g>

    <!-- 4 Specialized Resident Crew Roster Badges -->
    <g transform="translate(680, 22)" font-family="'JetBrains Mono', monospace" font-size="10.5">
      <!-- Badge 1 -->
      <rect x="0" y="0" width="235" height="30" rx="5" fill="rgba(255,255,255,0.07)" stroke="rgba(255,255,255,0.12)" />
      <circle cx="14" cy="15" r="3.5" fill="#38BDF8" />
      <text x="26" y="19" font-weight="700" fill="#F8FAFC">Resident Highway Engineers (PE)</text>

      <!-- Badge 2 -->
      <rect x="250" y="0" width="235" height="30" rx="5" fill="rgba(255,255,255,0.07)" stroke="rgba(255,255,255,0.12)" />
      <circle cx="264" cy="15" r="3.5" fill="#FBBF24" />
      <text x="276" y="19" font-weight="700" fill="#F8FAFC">Senior Materials &amp; Soil Technicians</text>

      <!-- Badge 3 -->
      <rect x="0" y="38" width="235" height="30" rx="5" fill="rgba(255,255,255,0.07)" stroke="rgba(255,255,255,0.12)" />
      <circle cx="14" cy="53" r="3.5" fill="#A78BFA" />
      <text x="26" y="57" font-weight="700" fill="#F8FAFC">Total Station Survey &amp; GPS Crews</text>

      <!-- Badge 4 -->
      <rect x="250" y="38" width="235" height="30" rx="5" fill="rgba(255,255,255,0.07)" stroke="rgba(255,255,255,0.12)" />
      <circle cx="264" cy="53" r="3.5" fill="#34D399" />
      <text x="276" y="57" font-weight="700" fill="#F8FAFC">Inspectors of Works, HSE &amp; Envir.</text>
    </g>
  </g>

  <!-- Diagram Bottom Margin Footnote -->
  <g transform="translate(60, 836)" font-size="9" font-weight="600" fill="#94A3B8" font-family="'JetBrains Mono', monospace">
    <text>AXULAL CONSULTING ENGINEERS PLC • ADDIS ABABA, ETHIOPIA • CATEGORY-1 HIGHWAY CONSULTANT</text>
    <text x="1180" text-anchor="end">QUALITY MANAGEMENT SYSTEM COMPLIANT • ERA &amp; FIDIC STANDARDS</text>
  </g>
</svg>'''

def main():
    svg_data = get_svg_content()
    
    # 1. Save SVG
    with open('assets/org_chart.svg', 'w', encoding='utf-8') as f:
        f.write(svg_data)
    print("Saved assets/org_chart.svg")

    # 2. Render High-Resolution PNG using Chrome headless
    # Wrap in an HTML wrapper for perfect crisp viewport rendering
    html_wrapper = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&amp;family=JetBrains+Mono:wght@500;700;800&amp;display=swap" rel="stylesheet">
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ background: #FFFFFF; width: 1300px; height: 860px; overflow: hidden; }}
  </style>
</head>
<body>
  {svg_data}
</body>
</html>'''

    html_path = os.path.abspath('org_chart_render.html')
    png_path = os.path.abspath('assets/org_chart.png')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_wrapper)

    chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    if os.path.exists(chrome_exe):
        print("Rendering high-resolution 2600x1720 PNG via Google Chrome headless...")
        cmd = [
            chrome_exe,
            '--headless=new',
            '--disable-gpu',
            '--force-device-scale-factor=2',
            '--window-size=1300,860',
            f'--screenshot={png_path}',
            f'file:///{html_path.replace(os.sep, "/")}'
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print("Chrome result returncode:", result.returncode)
        if result.stderr:
            print("Chrome stderr:", result.stderr)
        if os.path.exists(png_path):
            from PIL import Image
            img = Image.open(png_path)
            print(f"assets/org_chart.png generated! Dimensions: {img.size}, Size: {os.path.getsize(png_path):,} bytes")
    
    # Clean up temp file
    if os.path.exists(html_path):
        os.remove(html_path)

if __name__ == '__main__':
    main()
