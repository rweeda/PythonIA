const iframe = document.getElementById("nb");
const statusEl = document.getElementById("status");
const debugEl = document.getElementById("debug");

iframe.addEventListener("load", () => {
  statusEl.textContent = "Notebook loaded (iframe). Next: make it same-origin so we can read code/output.";
  debugEl.textContent = `iframe src:\n${iframe.src}`;
});
