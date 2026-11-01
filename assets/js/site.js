
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

    // 3. Project Grid — Progressive Disclosure & Dynamic Filtering
    const projectsContainer = document.getElementById("projectsContainer");
    const projectSearch = document.getElementById("projectSearch");
    const projectsEmpty = document.getElementById("projectsEmpty");
    const filterButtons = Array.from(document.querySelectorAll("#projectFilterGroup .filter-btn"));
    const projectCards = Array.from(projectsContainer.querySelectorAll(".project-card"));
    const projectsShowMoreWrap = document.getElementById("projectsShowMoreWrap");
    const projectsToggleBtn = document.getElementById("projectsToggleBtn");

    const INITIAL_PROJECTS_LIMIT = 3;
    let currentFilter = "all";
    let searchQuery = "";
    let projectsExpanded = false;

    function applyProjectFilters() {
      const q = searchQuery.trim().toLowerCase();
      const isDefaultShowcase = (currentFilter === "all" && !q);
      let matchedCount = 0;
      let visibleCount = 0;

      projectCards.forEach(card => {
        let matchesFilter = true;
        if (currentFilter === "road") matchesFilter = card.dataset.type === "road";
        else if (currentFilter === "bridge") matchesFilter = card.dataset.type === "bridge";
        else if (currentFilter === "ejere") matchesFilter = card.dataset.hub === "ejere";

        const matchesSearch = !q || (card.dataset.search || "").includes(q);
        const matches = matchesFilter && matchesSearch;

        if (matches) {
          matchedCount += 1;
          if (isDefaultShowcase && !projectsExpanded && matchedCount > INITIAL_PROJECTS_LIMIT) {
            card.hidden = true;
          } else {
            card.hidden = false;
            visibleCount += 1;
          }
        } else {
          card.hidden = true;
        }
      });

      if (projectsEmpty) projectsEmpty.hidden = visibleCount !== 0;
      projectsContainer.dataset.visibleCount = String(visibleCount);

      if (projectsShowMoreWrap && projectsToggleBtn) {
        if (!isDefaultShowcase) {
          projectsShowMoreWrap.hidden = true;
        } else {
          projectsShowMoreWrap.hidden = false;
          projectsToggleBtn.setAttribute("aria-expanded", projectsExpanded ? "true" : "false");
          if (projectsExpanded) {
            projectsToggleBtn.innerHTML = '<span class="btn-expand-label">Showing All ' + projectCards.length + ' Projects &middot; Show Less</span><span class="btn-expand-arrow" aria-hidden="true">&uarr;</span>';
          } else {
            projectsToggleBtn.innerHTML = '<span class="btn-expand-label">Showing <strong class="shown-count">' + INITIAL_PROJECTS_LIMIT + '</strong> of ' + projectCards.length + ' Projects &middot; Show All Projects</span><span class="btn-expand-arrow" aria-hidden="true">&darr;</span>';
          }
        }
      }
    }

    if (projectsToggleBtn) {
      projectsToggleBtn.addEventListener("click", () => {
        projectsExpanded = !projectsExpanded;
        applyProjectFilters();
        if (!projectsExpanded) {
          const sec = document.getElementById("projects");
          if (sec) {
            const top = sec.getBoundingClientRect().top + window.pageYOffset - 90;
            window.scrollTo({ top, behavior: "smooth" });
          }
        }
      });
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

    // 4. Field Photographic Plates — Progressive Disclosure & Lightbox
    const galleryContainer = document.getElementById("galleryContainer");
    const galleryShowMoreWrap = document.getElementById("galleryShowMoreWrap");
    const galleryToggleBtn = document.getElementById("galleryToggleBtn");
    const galleryCards = Array.from(galleryContainer.querySelectorAll(".gallery-card"));

    const INITIAL_PLATES_LIMIT = 4;
    let galleryExpanded = false;

    function updateGalleryVisibility() {
      galleryCards.forEach((card, idx) => {
        card.hidden = !galleryExpanded && idx >= INITIAL_PLATES_LIMIT;
      });

      if (galleryShowMoreWrap && galleryToggleBtn) {
        galleryToggleBtn.setAttribute("aria-expanded", galleryExpanded ? "true" : "false");
        if (galleryExpanded) {
          galleryToggleBtn.innerHTML = '<span class="btn-expand-label">Showing All ' + galleryCards.length + ' Field Plates &middot; Show Less</span><span class="btn-expand-arrow" aria-hidden="true">&uarr;</span>';
        } else {
          galleryToggleBtn.innerHTML = '<span class="btn-expand-label">Showing <strong class="shown-count">' + INITIAL_PLATES_LIMIT + '</strong> of ' + galleryCards.length + ' Field Plates &middot; Show All Field Plates</span><span class="btn-expand-arrow" aria-hidden="true">&darr;</span>';
        }
      }
    }

    if (galleryToggleBtn) {
      galleryToggleBtn.addEventListener("click", () => {
        galleryExpanded = !galleryExpanded;
        updateGalleryVisibility();
        if (!galleryExpanded) {
          const sec = document.getElementById("gallery");
          if (sec) {
            const top = sec.getBoundingClientRect().top + window.pageYOffset - 90;
            window.scrollTo({ top, behavior: "smooth" });
          }
        }
      });
    }

    updateGalleryVisibility();

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

    // Return to Top Handler, Scroll-Direction Header Color Change, and Active Section Scrollspy
    const backToTopBtn = document.getElementById("backToTopBtn");
    const siteHeader = document.getElementById("site-header");
    const navLinks = Array.from(document.querySelectorAll(".nav-menu .nav-link"));
    const mobileLinks = Array.from(document.querySelectorAll("#mobileDrawer a[href^='#']"));

    // Section IDs to track for scrollspy
    const sectionIds = ["about", "services", "projects", "gallery", "credentials", "contact"];
    const sectionElements = sectionIds
      .map(id => document.getElementById(id))
      .filter(el => el !== null);

    let lastScrollY = window.scrollY || 0;
    let scrollTicking = false;

    function handleScrollUpdates() {
      const scrollY = window.scrollY || document.documentElement.scrollTop;
      const isDown = scrollY > lastScrollY;
      const isScrolled = scrollY > 20;

      // 1. Dynamic Menu Bar Color Change (Scrolled Down vs Scrolled Up)
      if (siteHeader) {
        if (isScrolled) {
          siteHeader.classList.add("header-scrolled");
          if (isDown) {
            siteHeader.classList.add("scroll-down");
            siteHeader.classList.remove("scroll-up");
          } else {
            siteHeader.classList.add("scroll-up");
            siteHeader.classList.remove("scroll-down");
          }
        } else {
          siteHeader.classList.remove("header-scrolled", "scroll-down", "scroll-up");
        }
      }

      // 2. Floating Return-to-Top Button
      if (backToTopBtn) {
        if (scrollY > 280) {
          backToTopBtn.classList.add("visible");
        } else {
          backToTopBtn.classList.remove("visible");
        }
      }

      // 3. Dynamic Section Scrollspy (Color Change on Menu Items as User Scrolls Down/Up)
      let currentSectionId = "";
      const headerOffset = 140; // compensation for sticky header height

      for (let i = 0; i < sectionElements.length; i++) {
        const sec = sectionElements[i];
        const top = sec.offsetTop - headerOffset;
        const bottom = top + sec.offsetHeight;

        if (scrollY >= top && scrollY < bottom) {
          currentSectionId = sec.id;
          break;
        }
      }

      // Edge case: top of page
      if (!currentSectionId && scrollY < 300) {
        currentSectionId = "";
      } else if (!currentSectionId && (window.innerHeight + scrollY) >= document.documentElement.scrollHeight - 60) {
        currentSectionId = "contact";
      }

      // Update active nav link colors
      navLinks.forEach(link => {
        const href = link.getAttribute("href") || "";
        const targetId = href.replace(/^#/, "");
        if (targetId && targetId === currentSectionId) {
          link.classList.add("active");
        } else {
          link.classList.remove("active");
        }
      });

      // Update mobile drawer links active state
      mobileLinks.forEach(link => {
        const href = link.getAttribute("href") || "";
        const targetId = href.replace(/^#/, "");
        if (targetId && targetId === currentSectionId) {
          link.classList.add("active");
          link.style.color = "var(--brand-violet)";
        } else {
          link.classList.remove("active");
          link.style.color = "";
        }
      });

      lastScrollY = Math.max(0, scrollY);
      scrollTicking = false;
    }

    window.addEventListener("scroll", () => {
      if (!scrollTicking) {
        requestAnimationFrame(handleScrollUpdates);
        scrollTicking = true;
      }
    }, { passive: true });

    // Initial check on load
    handleScrollUpdates();

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
