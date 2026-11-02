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
        if (!projectsExpanded && index >= 5) {
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
        projectsToggleBtn.innerHTML = '<span>Showing 5 Flagship Projects &middot; Open Complete Technical Ledger (12 Projects)</span><span>&darr;</span>';
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