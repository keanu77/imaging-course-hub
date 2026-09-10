# 2026-09-10 主頁原始碼公開

- 使用者已自行將 keanu77/imaging-course-hub 設為 PUBLIC，已透過 GitHub 核對。
- 現況為主頁、肩部、膝部公開，其餘五部位維持私有。README 系列入口與部署文件已同步。
- 本次只同步狀態與連結，沒有新增程式碼或教材授權；以下歷史紀錄的可見性以本段為準。

# 2026-09-10 首頁文字精簡

- 依使用者要求，移除首頁「醫師專業教育」及「適合醫師、住院醫師與在合格督導下學習的醫療專業人員」；英文影像分類保留，移除多餘分隔符。
- 頁尾教育使用須知、來源及課程資料維持原樣。

# 2026-09-10 Repo 文件整備

- 原始碼可見性：PRIVATE；依使用者指示，只公開肩部與膝部，其餘維持私有。
- 現行入口：https://imaging-course-hub.sportsmedicine.tw/；系列首頁：https://imaging-course-hub.sportsmedicine.tw/。
- README、引用、貢獻、安全回報、資料範圍、開發、部署與改作說明已整理。歷史說明見 docs/COURSE_GUIDE.md；其他日期報告維持歷史用途。
- 本次不新增教材、不刷新醫療審閱、不更動搜尋索引。資料以 course 原始檔 SHA 比對確認。
- 最終驗證與部署摘要見 docs/REPOSITORY_READINESS.md。

以下保留之前交接；其中網址、可見性與未發布狀態可能已過期，以本段和現行文件為準。

# 2026-09-10 學習站正式網域

- 主頁正式網址：https://imaging-course-hub.sportsmedicine.tw/。課程返回按鈕與主頁 canonical 同步更新。
- 延續預設深色與既有教材審閱狀態。發布及驗證紀錄見工作區 HANDOFF 與 hub-domain-*.json。

# 2026-09-10 預設深色與返回主頁

- 首次造訪預設深色；即使系統偏好淺色、無儲存權限或無 JavaScript 亦然。原有深淺切換與有效偏好繼續保留。
- 七個課程網站左上方新增「← 學習站首頁」，連到 https://imaging-course-hub.pages.dev/；檢核表與已發布進階頁同步提供。
- 檢核表採深色螢幕顯示、白底列印。膝部純靜態單元講義維持無 JS、固定深色，主頁外連延續新分頁規則。
- 教材、策展批准與醫療審閱狀態未改。八站實際品質檢查及瀏覽器驗證均通過，證據為 ../imaging-design-audit-2026-09-09/dark-default-checks-final.json 與 dark-default-browser-0.json；舊失敗報告保留。
- 最終部署 SHA 與狀態見工作區 ../.claude/HANDOFF.md。

# 2026-09-10 首頁影片來源精簡

- 首頁「主要影片從哪裡來？」改為約 275 字中文，分學會與專家兩段，介紹 AMSSM、ESSR、SSR、Carlo Martinoli、Christoph Agten，附官方／講者連結。
- 移除兩個 CSV 下載入口及建置輸出；舊的 dist/preview 下載檔會於建置時清除。39 個中文頻道說明、134 筆核心與 251 筆完整收錄保留線上查閱。
- 重新核對 AMSSM 教育頁、ESSR e-learning、SSR 官網、熱那亞大學 Martinoli 資料與 Agten 個人簡介；各人的教學特色依已收錄影片整理，不是排名或臨床背書。
- 正式網址：https://imaging-course-hub.pages.dev/；GitHub keanu77/imaging-course-hub，main 推送由 Cloudflare 自動部署。工作區最終部署狀態見 ../.claude/HANDOFF.md。
- 本次未更動七站教材、影片選片、策展或醫療審閱狀態。

以下為歷史記錄。

# 2026-09-10 搬移與發布進行中

工作路徑：`/Users/ethanstudio/Documents/Vobe coding/imaging-course-hub`。使用者已要求推送 GitHub 與部署 Cloudflare；正在核對實際上線 commit。以下為歷史工作記錄。髖／踝足進階研究包仍保留 draft，不視為新增策展批准。

# 2026-09-10：主頁更名、移除裝飾框與影片來源

- 使用者指定標題「運動醫學影像學習站」，主頁 title、H1 與頁尾已同步。
- 主頁 route panel 與 course cards，以及七站 CourseGuide、ConsoleHeader、AdvancedEntry 與章節標題移除裝飾外框／粗頂邊；保留細分隔線及功能元件。
- 新增主要影片來源導覽與 sources.html：134 筆核心收錄、132 支不重複影片、39 個發布頻道；完整模式為 251 筆收錄、244 支影片。
- 每筆列原始標題、發布頻道、講者／資格連結、日期、原課程收錄理由與使用範圍；7 筆核心收錄的講者或資格欄位缺漏明示待補查。重要性來自原課程選片理由，來源概述以教學用途描述，不構成臨床背書。
- 八組來源概述附官方網站：AMSSM、ESSR、SSR、SMUG／The Ultrasound Site、Christoph Agten、LearnNeuroradiology、ISMRM／ISMRT、Sonosite 等設備商教育。2026-09-10 查閱公開來源；具體網址存於 source-profiles.json。
- 影片 metadata 為 2026-09-09 快照；本次不是全片重看、真實串流複核或新一輪醫療簽核。近十年界線及經典理由沿用該次核對。
- prepare_sources.py 與當前七站 syllabus 的所有影片／單元／核心標記逐筆核對；84 個 course 檔案 SHA-256 與設計起始版本相同，七站 git diff --check 通過。
- 驗證通過：七站 168 組版面與 49 項操作；主頁響應式／深淺模式／分類／無 JS；來源頁 7 站核心數量、core/all、搜尋、空結果、發布者篩選與鍵盤焦點、8 組視窗／主題、對應課程 URL、CSV、無 JS 完整清單。詳見 sources-validation.json 和 ../imaging-design-audit-2026-09-09/design-validation.json。
- 來源頁測試的第一次失敗是 selector 選入其他部位隱藏連結；已限定膝站資料列並確認 46 個膝站單元 href，修正後全數通過。
- 尚未 commit、push 或部署；主頁尚無正式網域。imaging-course-hub.zip 僅打包 dist，排除本機預覽入口。

預覽：http://127.0.0.1:8940/preview/
來源：http://127.0.0.1:8940/preview/sources.html
