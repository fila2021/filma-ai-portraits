document.addEventListener("DOMContentLoaded", function () {
  const root = document.documentElement;
  const toggle = document.getElementById("themeToggle");
  const storageKey = "askuala-theme";

  const applyTheme = (theme) => {
    root.setAttribute("data-theme", theme);
    if (toggle) {
      toggle.textContent = theme === "dark" ? "☼" : "☾";
      toggle.setAttribute(
        "aria-label",
        theme === "dark" ? "Switch to light mode" : "Switch to dark mode"
      );
    }
  };

  const savedTheme = localStorage.getItem(storageKey);

  // Default every new visitor to dark mode and persist that choice unless they toggle.
  const initialTheme = savedTheme || "dark";
  if (!savedTheme) {
    localStorage.setItem(storageKey, "dark");
  }
  applyTheme(initialTheme);

  if (toggle) {
    toggle.addEventListener("click", function () {
      const currentTheme = root.getAttribute("data-theme") || "dark";
      const nextTheme = currentTheme === "dark" ? "light" : "dark";
      localStorage.setItem(storageKey, nextTheme);
      applyTheme(nextTheme);
    });
  }
});
