document.addEventListener('DOMContentLoaded', () => {
  const select = document.querySelector('select[name="package"]');
  const preview = document.getElementById('pricePreview');
  if (!select || !preview) return;

  const prices = (() => {
    try {
      return JSON.parse(select.dataset.prices || '{}');
    } catch (e) {
      return {};
    }
  })();

  const formatEuro = (value) => `€${Number(value).toFixed(2)}`;

  const update = () => {
    const val = select.value;
    if (val && prices[val]) {
      preview.textContent = formatEuro(prices[val]);
    } else {
      preview.textContent = 'Select a package';
    }
  };

  select.addEventListener('change', update);
  update();
});
