// ─── Tab switcher ───
document.querySelectorAll(".tab").forEach((btn) =>
    btn.addEventListener("click", () => {
      // De-activate every tab & panel
      document.querySelectorAll(".tab, .tab-content").forEach((el) =>
        el.classList.remove("active")
      );
  
      // Activate clicked tab
      btn.classList.add("active");
  
      // Activate corresponding panel
      const target = btn.dataset.tab;
      document.getElementById(target).classList.add("active");
    })
  );
  
  console.log("Portfolio ready 🚀");
  