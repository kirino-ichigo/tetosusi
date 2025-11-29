// ナビメニュー
let nav = document.querySelector("#navArea");
let btn = document.querySelector(".toggle-btn");
let mask = document.querySelector("#mask");

btn.onclick = () => {
  nav.classList.toggle("open");
};

mask.onclick = () => {
  nav.classList.toggle("open");
};

// ▼ スクロールしたら toggle-btn の線を非表示
const toggleBtn = document.querySelector(".toggle-btn");
const headerEl = document.querySelector("header");

window.addEventListener("scroll", () => {
  const headerHeight = headerEl.offsetHeight;

  if (window.scrollY > headerHeight) {
    toggleBtn.classList.add("hide-lines");
  } else {
    toggleBtn.classList.remove("hide-lines");
  }
});


// ▼▼ ローディング（純JS版） ▼▼
window.addEventListener("load", () => {
  const splash = document.getElementById("splash");
  const splashLogo = document.getElementById("splash_logo");

  // ロゴをフェードアウト
  setTimeout(() => {
    splashLogo.style.opacity = "0";
    splashLogo.style.transition = "opacity 0.6s";
  }, 1200);

  // 背景全体をフェードアウト
  setTimeout(() => {
    splash.style.opacity = "0";
    splash.style.transition = "opacity 0.8s";
    splash.style.pointerEvents = "none"; // 見えない後に操作を邪魔しないように
  }, 1500);

  // 完全に非表示にする（CSS的に消す）
  setTimeout(() => {
    splash.style.display = "none";
  }, 2300);
});
