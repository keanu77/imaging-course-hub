# 運動醫學影像學習站

整合七個部位的影像課程、中文來源介紹與逐片教學重要性，讓醫療專業人員從同一入口開始學習。

[開始學習](https://imaging-course-hub.sportsmedicine.tw/) · [七站總覽](https://imaging-course-hub.sportsmedicine.tw/) · [吳易澄醫師](https://sportsmedicine.tw/)

**原始碼狀態：公開。歡迎瀏覽原始碼與回報問題；再利用條件請見授權說明。** 網站可瀏覽與 repo 是否公開是兩個獨立設定。

![運動醫學影像學習站桌機畫面](docs/images/desktop.png)

[手機畫面](docs/images/mobile.png) · 畫面與資料快照：2026-09-10。

## 可以參考什麼

- 資料驅動的課程與影片來源整理，維持可追溯的單元、來源及版本資訊。
- 繁體中文、手機版面與預設深色設計；使用者可切換並保存主題偏好。
- 各課程左上方可返回學習站，並透過「推薦影片／文獻」提供連結或回報修正。
- 教材與研究包分開管理；策展審閱、技術驗證與臨床能力認證不混用。

## 現有資料

以下依 2026-09-10 本機正式建置統計；資料量與影片時數不能證明臨床能力。

| 項目 | 數量 |
| --- | --- |
| 課程入口 | 7 |
| 核心影片收錄 | 134 筆／132 支不重複影片 |
| 完整影片收錄 | 251 筆 |
| 核心影片發布頻道 | 39 |

完整範圍與限制見 [DATA_AND_REVIEW](docs/DATA_AND_REVIEW.md)。零筆代表目前未提供該類資料，不表示建置失敗。

## 本機建置

需要 Python 3.11+；正式建置只使用標準函式庫。

```bash
python3 build.py
python3 test_build.py
python3 -m http.server 8940 --bind 127.0.0.1 --directory dist
```

開啟 http://127.0.0.1:8940/ 。正式建置使用已提交的資料快照，不需要相鄰七個 repo。

瀏覽器測試、資料更新及不需正式服務的驗證方式見 [開發說明](docs/DEVELOPMENT.md)。部署設定見 [DEPLOYMENT](docs/DEPLOYMENT.md)。

## 檔案入口

| 路徑 | 用途 |
| --- | --- |
| `courses.json` | 七站網址、課程介紹與本機預覽埠 |
| `video-sources.json` | 影片來源快照 |
| `channel-profiles.json` | 39 個發布頻道的中文介紹 |
| `index.template.html`、`sources.template.html` | 頁面模板 |
| `assets/` | 樣式與互動程式 |
| `build.py`、`source_pages.py` | 標準函式庫建置 |
| `prepare_sources.py` | 維護者更新快照用，依賴相鄰課程與審閱清單 |

## 提供影片、文獻或修正

從網站「推薦影片／文獻」進入表單，會自動附上課程與單元網址。可提供公開影片、DOI／PubMed／學會文獻連結或資料修正；投稿須先查核，不會自動上線。請不要提供病人個資或未獲授權的影像。

程式與介面 PR 請讀 [CONTRIBUTING](CONTRIBUTING.md)；安全問題請依 [SECURITY](SECURITY.md) 私下回報。Fork 與改作請讀 [FORKING](docs/FORKING.md)，重新設定作者、網域與投稿目的地。

## 授權與引用

本站原始碼已公開，尚未新增程式碼或教材的再利用授權。 詳見 [LICENSE](LICENSE)、[教材授權範圍](LICENSE-CONTENT.md) 與 [第三方及品牌聲明](NOTICE.md)。第三方影片、文獻與素材維持原權利人的條件，本站不代為授權。

引用專案可使用 [CITATION.cff](CITATION.cff)，並註明實際使用的 commit 或版本。引用臨床結論時，請直接引用原始文獻；專案引用不取代文獻引用。

## 使用範圍

供醫療專業人員教育使用。策展審閱確認收錄範圍、來源及課程編排，不代表對第三方影片內容的醫療背書；模型檢查或測試通過也不等於醫師逐項審閱、專業認證或獨立執業資格。使用時仍需實作訓練、合格督導與臨床判斷。

## 系列網站

| 課程 | 學習網站 | 原始碼 |
| --- | --- | --- |
| 髖關節 | [進入網站](https://hip-imaging-course.pages.dev/) | 私有，未開放 |
| 踝與足 | [進入網站](https://ankle-foot-imaging-course.pages.dev/) | 私有，未開放 |
| 肩部 | [進入網站](https://shoulder-imaging.sportsmedicine.tw/) | [GitHub](https://github.com/keanu77/shoulder-imaging-course) |
| 頸椎 | [進入網站](https://cervical-imaging-course.pages.dev/) | 私有，未開放 |
| 腰椎 | [進入網站](https://lumbar-imaging-course.pages.dev/) | 私有，未開放 |
| 腕與手 | [進入網站](https://wrist-hand-imaging-course.pages.dev/) | 私有，未開放 |
| 膝關節 | [進入網站](https://knee-imaging.sportsmedicine.tw/) | [GitHub](https://github.com/keanu77/knee-imaging-course) |
| 課程總覽 | [進入網站](https://imaging-course-hub.sportsmedicine.tw/) | [GitHub](https://github.com/keanu77/imaging-course-hub) |

[文件索引](docs/README.md) · [先前課程說明](docs/COURSE_GUIDE.md)
