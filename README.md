# 運動醫學影像學習站

整合肩、腕手、髖、膝、踝足、頸椎、腰椎七站，附課程介紹、部位篩選、學習方式與吳易澄醫師的個人網站／Facebook／Instagram／LINE 入口。

## 預覽與建置

- 正式連結版：`python3 build.py` → `dist/`；入口連往已驗證可達的公開課程。
- 本機設計版：`python3 build.py --preview` → `preview/`；入口連往本機 8931–8937 的新設計。**不可將 preview/ 當正式輸出發布。**
- 預覽伺服器：`python3 -m http.server 8940 --bind 127.0.0.1`。
- 本機設計主頁：<http://127.0.0.1:8940/preview/>。
- 正式網址導覽版本：<http://127.0.0.1:8940/dist/>。
- 瀏覽器驗證：`node verify.cjs`（Playwright 路徑見檔案首行，可依環境調整）。

無 npm 套件、外部字型、追蹤碼或分析服務。關閉 JavaScript 仍能看到全部七站、介紹、追蹤入口及完整影片來源。JavaScript 提供部位篩選、來源搜尋及可保存的深淺主題。

## 影片來源與重要性

- `sources.html`：七站主要影片共 134 筆收錄、132 支不重複影片、39 個發布頻道；可切換完整 251 筆收錄。
- 每筆列出原片名稱、發布來源、講者與資格資料連結、上傳日期、原課程收錄理由、使用範圍、課程與原片入口；缺少講者或資格連結的 7 筆主要收錄保留待補查標示。
- 主要影片依目前 syllabus 的 `learning_tier=core` 定義，不代表證據等級或臨床背書。`source-profiles.json` 補充八組來源的教學用途與官方網站。
- `python3 prepare_sources.py` 從七站目前 syllabus 整理資料，並與 `../imaging-course-review-2026-09-09/video-inventory.json` 逐筆核對；輸出 `video-sources.json` 後，再分別建置正式連結版與本機版。
- 影片 metadata 沿用 2026-09-09 的核對快照；整理日期為 2026-09-10。本次不會重新查詢影片，也不更新原課程的策展或醫療審閱狀態。
- `core-video-sources.csv` 與 `all-video-sources.csv` 可從來源頁下載，以 UTF-8 BOM 輸出供試算表開啟。
- 本機來源頁：<http://127.0.0.1:8940/preview/sources.html>；驗證：`node verify-sources.cjs`。

課程資料以 `courses.json` 維護。`previewPort` 只在 build 的 --preview 模式使用；正式輸出不含 localhost 入口。發布前應由實際設定的主網域補 canonical／社群預覽，並另行確認索引策略；目前保留 noindex；GitHub 為 keanu77/imaging-course-hub（private），正式輸出部署至 imaging-course-hub.pages.dev。

## 品牌與來源

- 配色及身份參考：<https://sportsmedicine.tw/>，2026-09-09 公開首頁。
- 追蹤連結使用該頁的實際 href：Facebook EthanWuMD、Instagram ethan77wu、LINE @521cvffb。
- 七站介紹由各站目前課程範圍整理，不包含尚未發布的髖／踝足新增工作坊，也不宣稱所有教材均已核准。
- 五站自訂網域當次 DNS 無法解析，採用已通過匿名 GET 的 Pages 網址；完整來源檢查見 `../imaging-design-audit-2026-09-09/course-link-check.json`。

## 驗證

`docs/validation.json`、`docs/screens/`：320/390/820/1440、深淺模式、分類、實際 href、主題保存、鍵盤跳過導覽、快速分類焦點、無 JS 導览、正式／本機兩種輸出隔離。

本輪七站多模型報告：`../imaging-design-audit-2026-09-09/PASS2.md`。

2026-09-10 更新：`docs/UPDATE-2026-09-10.md`、`docs/sources-validation.json` 與 `docs/sources-screens/`。主頁及七站已移除裝飾性的粗頂邊與圓角框，保留操作元件與使用須知的必要分隔。前一日多模型報告不代表本次新增來源頁另做過多模型審查。


## 發布維護（2026-09-10）

- 工作位置：`/Users/ethanstudio/Documents/Vobe coding/imaging-course-hub`；其餘七站與審閱資料位於同一層。
- Cloudflare Pages 使用 Git integration、`main` 分支、`python3 build.py && python3 test_build.py`、輸出 `dist/`。建置只需 Python 標準函式庫；不會讀取相鄰課程 repo。
- `channel-profiles.json` 為 39 個發布頻道的中文背景、重要性、學習時機與參考連結；來源頁已全數呈現。背景和教學用途分開，不以頻道知名度代替證據等級。
- `prepare_sources.py` 是維護者在本機更新資料時使用；更新後將資料快照與程式一起提交。
- `version.json` 記錄部署 commit SHA；上線後須核對 GitHub、Pages 與實際內容一致。
