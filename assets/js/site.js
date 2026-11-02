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