// Yum Yum Bites — header shadow, open/closed status, menu tabs, vegan filter
(() => {
  // Opening hours, 24h. Same every day for now; one entry per weekday (0 = Sunday).
  const HOURS = Array(7).fill([11, 21]);

  const header = document.querySelector('[data-header]');
  const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 40);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Open / closed, in UK time whatever the visitor's timezone
  const now = new Date(new Date().toLocaleString('en-US', { timeZone: 'Europe/London' }));
  const [open, close] = HOURS[now.getDay()];
  const h = now.getHours() + now.getMinutes() / 60;
  const isOpen = h >= open && h < close;
  const text = isOpen
    ? `Open now · until ${close}:00`
    : h < open ? `Closed · opens today at ${open}:00` : `Closed · opens tomorrow at ${HOURS[(now.getDay() + 1) % 7][0]}:00`;
  document.querySelectorAll('[data-status]').forEach(el => {
    el.textContent = text;
    el.classList.add(isOpen ? 'is-open' : 'is-closed');
  });

  // Highlight the menu tab for the section in view
  const tabBar = document.querySelector('[data-menu-tabs]');
  const tabs = [...tabBar.querySelectorAll('a')];
  const setCurrent = id => tabs.forEach(t => {
    if (t.getAttribute('href') !== '#' + id) return t.removeAttribute('aria-current');
    t.setAttribute('aria-current', 'true');
    // keep the active tab visible in the scrolling strip without moving the page
    tabBar.scrollTo({ left: t.offsetLeft - tabBar.offsetLeft - 16, behavior: 'smooth' });
  });
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) setCurrent(e.target.id); });
    }, { rootMargin: '-35% 0px -60% 0px' });
    document.querySelectorAll('.menu-sec').forEach(s => io.observe(s));
  }

  // Vegan & veggie filter: hide dishes without a plant-based mark, and sections left empty
  const menu = document.getElementById('menu');
  const filter = document.querySelector('[data-vegan-filter]');
  filter.addEventListener('change', () => {
    menu.classList.toggle('is-veg', filter.checked);
    document.querySelectorAll('.menu-sec').forEach(sec => {
      const any = !filter.checked || sec.querySelector('.dish[data-diet^="v"]');
      sec.hidden = !any;
    });
  });
})();
