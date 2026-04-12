(function() {
  const root = document.documentElement;
  const btn = document.getElementById('themeToggle');
  if (!btn) return;

  const stored = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const initial = stored || (prefersDark ? 'dark' : 'light');
  setTheme(initial);

  btn.addEventListener('click', () => {
    const current = root.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(current);
    localStorage.setItem('theme', current);
  });

  function setTheme(mode) {
    root.dataset.theme = mode;
    btn.textContent = mode === 'dark' ? '🌞' : '🌙';
  }
})();
