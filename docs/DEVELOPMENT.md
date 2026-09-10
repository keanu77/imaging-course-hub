# 開發與驗證

## 基本建置

依 README 安裝 Python／uv。程式建置與讀取資料快照不需要 API 憑證；只有重新查詢外部來源或部署才需要相應工具與權限。

## 瀏覽器測試

需要 Node.js 及 Playwright，可安裝在 repo 的暫存目錄：

```bash
npm install --prefix .tmp/browser-tools --no-package-lock playwright@1.62.1
.tmp/browser-tools/node_modules/.bin/playwright install chromium
```

先依 README 啟動本機網站，再於另一終端執行：

```bash
export PLAYWRIGHT_MODULE="$PWD/.tmp/browser-tools/node_modules/playwright"
python3 build.py --preview
# 在另一終端從 repo 根目錄啟動：python3 -m http.server 8940 --bind 127.0.0.1
BASE_URL=http://127.0.0.1:8940/ node verify.cjs
BASE_URL=http://127.0.0.1:8940/ node verify-sources.cjs
```

一般課程的 `test-course-ui.cjs` 目前使用已安裝的 Google Chrome；膝部及主頁使用 Playwright Chromium。測試阻擋／取代外部影片時，只驗網站互動，不代表真實串流通過。

## 資料維護

`python3 prepare_sources.py` 需要相鄰七站及 `imaging-course-review-2026-09-09/video-inventory.json`；這是維護者更新快照的流程，單獨 clone 不保證能執行。一般使用者直接建置已提交的 video-sources.json 即可。欲更新來源時，先準備完整維護工作區並核對影片配置，再提交更新的快照；不得把整理日期寫成新的查證日期。

## 文件更新

README 的數量是具日期的建置快照。調整課程後，從 dist/course.json（主頁為來源快照）重算，並同步資料範圍文件。新增畫面需從實際瀏覽器擷取，不用模擬設計稿代替正式畫面。
