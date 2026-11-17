/* gm.js — the three behaviours the design language needs. No dependencies.
   1. reveal: .gm-reveal rises and fades in once, staggered inside [data-gm-stagger]
   2. count-up: [data-gm-count="118"] counts from 0 when it scrolls into view
   3. nav: .gm-nav gets .is-scrolled (hairline + faint shadow) after 8px */
(function () {
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  document.querySelectorAll("[data-gm-stagger]").forEach(function (group) {
    var step = parseFloat(group.getAttribute("data-gm-stagger")) || 0.08;
    group.querySelectorAll(".gm-reveal").forEach(function (el, i) {
      el.style.setProperty("--gm-delay", (i * step).toFixed(2) + "s");
    });
  });

  function countUp(el) {
    var raw = el.getAttribute("data-gm-count");
    var target = parseFloat(raw);
    if (isNaN(target)) return;
    var decimals = (raw.split(".")[1] || "").length;
    var prefix = el.getAttribute("data-gm-prefix") || "";
    var suffix = el.getAttribute("data-gm-suffix") || "";
    // numbers follow the page language: 1,100 on an English page, 1.100 on a German one
    var locale = el.getAttribute("data-gm-locale") || document.documentElement.lang || "en";
    var fmt = function (v) {
      var opts = { minimumFractionDigits: decimals, maximumFractionDigits: decimals }, text;
      try { text = v.toLocaleString(locale, opts); } catch (e) { text = v.toLocaleString("en", opts); }
      return prefix + text + suffix;
    };
    if (reduce) { el.textContent = fmt(target); return; }
    var start = null, dur = 1200;
    function tick(t) {
      if (start === null) start = t;
      var p = Math.min((t - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(target * eased);
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  if (!("IntersectionObserver" in window)) {
    document.querySelectorAll(".gm-reveal").forEach(function (el) { el.classList.add("is-in"); });
    document.querySelectorAll("[data-gm-count]").forEach(countUp);
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        if (e.target.classList.contains("gm-reveal")) e.target.classList.add("is-in");
        if (e.target.hasAttribute("data-gm-count")) countUp(e.target);
        io.unobserve(e.target);
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -8% 0px" });
    document.querySelectorAll(".gm-reveal, [data-gm-count]").forEach(function (el) { io.observe(el); });
  }

  var nav = document.querySelector(".gm-nav");
  if (nav) {
    var onScroll = function () { nav.classList.toggle("is-scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  document.querySelectorAll(".gm-toggle").forEach(function (t) {
    t.addEventListener("click", function () { t.classList.toggle("is-on"); });
  });
  document.querySelectorAll("[data-gm-rail-next]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var rail = document.querySelector(btn.getAttribute("data-gm-rail-next"));
      if (rail) rail.scrollBy({ left: rail.clientWidth * 0.8, behavior: reduce ? "auto" : "smooth" });
    });
  });
})();
