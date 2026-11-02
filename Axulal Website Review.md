# Axulal Website Review

Review of the Axulal Consulting Engineers PLC website (Axulal.zip), 2 November 2026. Code read in full, tested in a headless browser on desktop (1366px) and mobile (390px), and checked against the project data and git history.

## Summary

The site is well built overall, but the project filter is broken, the numbers disagree with each other, and some of the claims could cause trouble.

## What it is

A single-page static site with no framework or build step at runtime: `index.html` (65 KB), one stylesheet, `site.js` and `data.js`. It uses Archivo, Source Sans 3 and JetBrains Mono from Google Fonts, with a violet brand colour and an amber accent.

Sections, in order:

- Header with the phone number and a “Request RFP” button
- Hero with a featured Awash Bridge card and a scrolling stats ticker
- Four-number stat band
- About (three cards)
- Services (four cards)
- Projects (12 projects, filterable, with spec modals)
- Gallery (12 photo plates with a lightbox)
- Credentials
- Contact (RFP form, Google Map and a footer “Headquarters Desk”)

What works well: the code is clean, there are no console errors from the site itself (the only error was Google Fonts failing to load in the test sandbox), there is no horizontal scroll on desktop or mobile, images use WebP with JPG fallback and thumbnails, images are lazy-loaded, there is a skip link and a mobile drawer, and modals close with Escape. No project prices appear anywhere, which matches the decision not to disclose them.

## Bugs to fix first

### 1. The project filter hides projects

The code checks each card’s position among all 12 cards, not among the filtered ones, so most cards vanish unless “Show All” is open. Confirmed in the browser:

| Tab | Cards that exist | Cards shown |
| --- | --- | --- |
| Ginchi | 2 | 1 |
| Awash | 3 | 1 |
| Ejere | 5 | 2 |
| Berga | 2 | 1 |

Fix: filter by hub first, then apply the “first N” limit to the filtered list.

### 2. The form always shows “Thank you” after sending

The `.then()` handler never checks whether FormSubmit actually accepted the message, so a failed send looks like a success. FormSubmit also needs a one-time email confirmation for `tenders@axulalengineers.com` before it delivers anything. The form has `_captcha=false` and no honeypot, so spam will arrive, and the email address is visible in the JavaScript. Test it with a real send before launch.

### 3. The numbers don’t agree with each other

- Road lengths in `data.js` add up to 145.8 km, but the site says 145.3 km.
- The tab labels don’t match the project data: Ejere says 56.5 km but the data gives 85.7 km; Ginchi says 15.5 km (data: 25.5 km); Awash says 35 km (data: 25 km of road plus a 24 m bridge).
- The form intro promises a reply “within one working day”, while the success message and the Contact section say 24–48 hours.

Some placeholder numbers were already noted as needing correction, so this is probably that list. Take these figures from the company profile and keep them in one place.

## Content and legal risk

Claims to check with Axulal before launch:

- “Zero contractual defaults, zero liquidated damages, 100% client satisfaction, 100% timely completion, 100% quality acceptance” can’t be proven, and if a client disagrees it could hurt the company.
- “Unlimited contract value and technical jurisdiction” and “Highest statutory license” should match the licence document wording exactly.
- “Arterial Highways”, “classified highways” and “Critical Bridges” overstate what the data shows. Almost every project is a 6 m DC-2 gravel road, plus two bridges of 24 m and 22 m. “Rural road corridors and river bridges” would be accurate and still strong.
- The accreditation lines don’t agree: “MoWUD & ERA” in some places, “MoWUD & ORA” in the README, and “FDRE Reg #01/ORA/2011” is an unusual way to write a registration.
- Some copy describes work that isn’t in the project data (50-year flood hydrographs, pavement thickness design, “Interim Payment Certificates”). Keep these only if they are in the company profile.

## Design and usability

- **Logo:** In the header it is only about 140 px wide, so the small bilingual text under it can’t be read. A cleaner horizontal lockup would help.
- **Mobile header:** “Request RFP” wraps onto two lines and takes up too much of the bar. The mobile page is also very long (about 16,700 px).
- **“Capability Profile” button:** It just jumps to Credentials. If the company profile PDF exists, link it so people can download it; tender officers look for this.
- **Language:** There is no Amharic version, although the footer carries the Amharic company name. Amharic is worth adding for regional clients.
- **Wording:** Phrases like “Telemetry”, “Terminal” and “Verified Spec” read like an app, not a consultancy. Plainer words would feel more trustworthy.

## Accessibility and SEO

- **Modals:** They have `role="dialog"` but no focus trap and no focus return when closed, and the hamburger button never changes to a close icon.
- **Focus outline:** `.form-control:focus` removes the outline and relies on a faint violet shadow that may be hard to see.
- **Emoji icons:** Most aren’t marked `aria-hidden`, so screen readers read them out.
- **Skip link:** It says “Skip to Projects” and should go to the main content.
- **Lightbox:** It loads the card’s image, which may be the 480 px thumbnail.
- **Missing for search:** No canonical URL, Open Graph or Twitter tags, structured data (`Organization` / `LocalBusiness`), `robots.txt` or sitemap. The favicon link points at `logo.png`, not the favicon files.

## Repo and project hygiene

- **README is out of date.** It describes a preloader, a 4-slide carousel, a light/dark theme toggle, a “Master” HTML mirror and root-level build scripts. None of those are in the code, and the scripts live in `scripts/`.
- **Duplicated content.** It lives in three places: static HTML, `data.js` (which also holds an unused gallery list) and the Python build script. This is why the numbers drift apart.
- **Working-tree leftovers.** The zip includes the `.git` folder, `__pycache__` and two PSD files (2.8 MB), and 15 modified files are not committed.
- **Cache-busting.** It is a hand-edited `?v=21`. That works, but it’s easy to forget.
- **Fonts and images.** Three Google font families with many weights are the main performance cost, and the project modal loads full-size WebP.

## Suggested next steps

1. Fix the filter and the form, and make the figures consistent.
2. Reword the unprovable claims.
3. Fix the mobile header and the logo size.
4. Add SEO tags and a downloadable company profile.
5. Refresh the README.
