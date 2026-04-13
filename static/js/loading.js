document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll("form");
  forms.forEach((form) => {
    form.addEventListener("submit", () => {
      const submitBtn =
        form.querySelector("[type='submit']:not([disabled])") ||
        form.querySelector("button");
      if (!submitBtn) return;
      submitBtn.classList.add("is-loading");
      submitBtn.setAttribute("disabled", "disabled");
    });
  });
});
