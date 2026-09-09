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
