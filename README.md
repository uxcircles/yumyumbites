# Yum Yum Bites 甲奔 — 網站改版提案

純靜態網站（HTML / CSS / JS），不需要建置步驟，任何靜態主機都能直接部署。

> **概念設計展示**：這是由 [UX CIRCLES](https://ux-circles.com/web) 設計的改版提案，並非 Yum Yum Bites 官方網站。
> 頁面頂端有「Concept」標示列，設為 `noindex`，`robots.txt` 也禁止收錄，避免和官方網站搶搜尋結果。
> 如果店家正式採用：刪掉 `.concept-bar`、`<meta name="robots" content="noindex, nofollow">`，`robots.txt` 改回 `Allow: /`，並把 canonical / og 網址改成 `https://yumyumbites.co.uk/`。

## 檔案結構

```
index.html               由 _build/build.py 產生，不要直接改菜單區塊
_build/menu.py           菜單資料（品項、中文名、價格、素食標記）
_build/index.template.html  頁面模板
_build/build.py          產生 index.html：python3 _build/build.py
styles.css / main.js     樣式；互動（營業狀態、菜單分頁、純素篩選、地圖延遲載入）
assets/map.js            地圖配色（MapLibre + OpenFreeMap，顏色在檔案開頭的 C）
assets/vendor/maplibre/  MapLibre GL JS 4.7.1（BSD 授權）
assets/img/              照片（WebP，兩種尺寸）、logo、og.jpg
assets/menus/            原本的菜單 PDF
_redirects, vercel.json  舊網址 /menu、/reviews 轉址
```

## 本機預覽

```bash
python3 -m http.server 5180
```

## 日常更新

| 要改什麼 | 改哪裡 |
|---|---|
| 菜色／價格 | `_build/menu.py`，然後跑 `python3 _build/build.py` |
| 營業時間 | `main.js` 的 `HOURS`，以及模板裡的 JSON-LD、首頁和 Visit 區的文字 |
| 改了 CSS／JS | 把 `styles.css?v=1`、`main.js?v=1` 的版本號 +1 |

## 內部筆記

原網站檢視結果、待店家確認事項和 pitch 資料放在本機的 `.private/`（已被 `.gitignore` 排除，不會進 git）。

第一次 clone 後啟用 git hooks：

```
git config core.hooksPath .githooks
```

之後每次 commit / push 會擋下 `.private/` 的檔案和 `.private/blocklist.txt` 裡的敏感字詞，並列出 `.private/NOTES.md` 裡未完成的待辦。隨時查看：`sh .githooks/remind.sh`
