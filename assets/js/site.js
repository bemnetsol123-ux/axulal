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
});