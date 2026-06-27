# ALE 全卷宗投稿前逐文件審閱

**作者 / Reviewer**：Codex（OpenAI）  
**版本 / Version**：v1.0.0_codex  
**日期 / Date**：2026-06-21  
**範圍**：`04_RnD/01_ALE/` 全部目錄、Markdown、CFF、程式、容器設定、HTML snapshot、DOCX preview 與 PDF 文獻庫。

## 0. 根目錄

| 文件 | 判定 | Codex 建議 |
|---|---|---|
| `README.md` | 需修 | 名稱、G4/G5/G6 狀態與主實驗敘事需隨 v3.0 更新；不要再寫既有 ALE 名稱可保留。 |
| `AUTHOR.md` | 不可隨 DOI 原樣發布 | 尚有 `[請補充]`；含街道地址與內部代擬說明。完成 bio 後另產公開版，或本次不附。 |
| `CITATION.cff` | P0 | 標題撞名；abstract 仍直述未驗假說；作者格式需統一。更名後驗證 CFF。 |
| `LICENSE` | 可用 | CC BY 4.0 適合文件；若另附程式碼，程式碼應另放 MIT/Apache-2.0，不要假設 CC BY 覆蓋程式最理想。 |
| `RESEARCH_LOG.md` | 內部可保留 | 不建議隨 DOI 上傳；更新名稱撞車、Code-A1 prior art 與本次 NO-GO 決策。 |

## 1. `00_Ideas_Inspiration`

| 文件 | 判定 | Codex 建議 |
|---|---|---|
| `README.md` | 內部有效 | 將「命名候選」更新為已確認撞名；增加 Code-A1 / shared-context false pass。 |
| `STORY_origin_einvoice.md` | 可作背景，不宜作證據 | 第四節「多找幾個 AI 救不了」過強；改為研究假說。`test collusion` 改為 early working label。 |

## 2. `01_Consolidation`

| 文件 | 判定 | Codex 建議 |
|---|---|---|
| `README.md` | G1 應重新打開 | 「撞名風險已查」的結論已被新查核推翻；既有 roadmap 使用完全相同 ALE。候選貢獻也需加入 Code-A1 後重算。 |
| `STORY_consolidation.md` | 需重寫部分敘事 | 文中稱 2512.03097 證明 verifier 擋不住，但原文結果相反；「我提供解方」也因 Code-A1 / PDD 等工作需降級。 |

## 3. `02_Drafts`

| 文件 | 判定 | Codex 建議 |
|---|---|---|
| `README.md` | 可保留 | 將 v3.0 設為 DOI 候選主稿；v2.5 改為 pre-renaming internal draft。 |
| `ALE_WhitePaper.md` | 歷史稿 | 封存，不作發布輸入。 |
| `ALE_WhitePaper_v2.1.md` | 歷史稿 | 封存，不作發布輸入。 |
| `ALE_WhitePaper_v2.3.md` | 歷史稿 | 封存；保留 Codex 審閱對照價值。 |
| `ALE_WhitePaper_v2.4.md` | 歷史稿 | 封存；仍有 placeholders。 |
| `ALE_WhitePaper_v2.5.md` | P0，不可直接 DOI | 依 `ALE_DOI_Readiness_Review_v1.0.0_codex.md` 升為 v3.0。核心問題：撞名、直接 prior art 缺漏、摘要過強、引文誤讀、GenAI 揭露缺失。 |

## 4. `03_Reviews`

| 文件群 | 判定 | Codex 建議 |
|---|---|---|
| `ALE_Review_Index_codex.md`、`ALE_WhitePaper_v2.3_codex.md` | 有效歷史審閱 | 保留。 |
| Gemini review / rewrite files | 需標示非主稿 | 保留審閱軌跡，但 `file:///` 連結不可出現在公開交付；曾有虛構 evidence 的紀錄應保留於內部。 |
| `README.md` | 需新增本次總審 | 將本次四份 v1.0.0_codex 文件加入索引，G3 因名稱與 prior art 新發現需重新開啟。 |

## 5. `04_Evidence`

### 案例文件

| 文件 | 判定 | Codex 建議 |
|---|---|---|
| `ALE_CaseStudy_EInvoice_v1.md` | 歷史稿，不公開 | 過度使用實證、證實、Cov→1。 |
| `_v1_codex.md` | 有效審閱 | 保留。 |
| `_v1_gemini.md` | 不作 evidence source | 曾含虛構日誌；只能留作失敗審閱案例。 |
| `ALE_CaseStudy_EInvoice_v2.md` | 可作 preliminary case | DOI 稿只引用 v2；仍須明確寫 post-hoc、analogue、不可推論 AI-to-AI。 |

### EXP-001 協定與 scaffold

| 文件 | 判定 | Codex 建議 |
|---|---|---|
| `ALE_EXP-001_Protocol_v1.md`、`_codex.md`、`_gemini.md` | 歷史／審閱 | 保留。 |
| `ALE_EXP-001_Protocol_v2.md` | 協定可凍結，但 runner 未完成 | 狀態改為 `Frozen Protocol; Incomplete Runner`。修正 PG reasoning、golden oracle、determinism 與統計單位。 |
| `experiments/EXP-001/README.md` | 說明完整但狀態過強 | 「過此實驗 = G4 過關」與 EXP-002 主實驗說法衝突；改為完成 C1/C2/C5/C6 的驗證關卡。 |
| `.env.example` | 可用 | 保留通用端點；價格與模型 snapshot 另記 evidence。 |
| `Dockerfile` | 可建 scaffold | Protocol 寫 Python 3.10 與 pinned minor versions，Dockerfile 實際是 Python 3.11 + wildcard major；須一致並產 lockfile。 |
| `docker-compose.yml` | 尚不可完成實驗 | 預設 A/C/D/E，但 runner 未實作 API、缺陷注入與 D gate。 |
| prompts | 需修 | 不依賴 PG hidden reasoning；保留可公開的 rationale artifact 才能作變項。 |
| `run_experiment.py` | 未完成 | 兩個 `NotImplementedError`；未實作 mutation/property/token/time/hash。 |
| `analyze_results.py` | skeleton | 只算分組 FPR；未作 paired analysis、CI、effect size 或 task clustering。 |
| T01 spec / defects / reference / golden | 可作最小任務 | Golden test 可抓 D1–D3，但目前不是「100% oracle」；INV-1 在 T01 無 national-total fixture，D gate 尚未實作。 |
| `RESULTS_TEMPLATE.md` | 可保留 | 未有數據，發布稿不得暗示已執行。 |

### EXP-002

| 文件 | 判定 | Codex 建議 |
|---|---|---|
| `README.md` | 設計研究構想 | `Loop 0 proven` 改為 `retrospectively documented`；未有可重現 skill artifact，不能稱 proven。 |
| `BASELINE_einvoice.md` | baseline 不足 | 沒有工時，只有 proxy，無法計算可靠降幅；Loop 1 不應和 proxy baseline 做百分比效果宣稱。 |
| `EVIDENCE_MAP_and_FSM.md` | 內部自評 | `Validated` 改為 `internally assessed as Validated`。 |
| `SKILL_SUMMARY_abstract.md` | 保密策略合理 | 但若完全不公開 manifest / eval，學術可重現性很弱；至少公開 synthetic schema 或 redacted exemplar。 |
| `METRICS_SCHEMA.md` | 可用初稿 | `reuse_rate = 組裝步驟/總步驟` 需要可重現的步驟分類規則。`rework_loc` 不適合跨語言／低碼 workflow 單獨比較。 |
| `RESULTS_TEMPLATE.md` | 可保留 | Loop 1/2 空白，不能支撐 DOI 摘要中的技能降本暗示。 |

## 6. `05_DueDiligence`

| 文件 | 判定 | Codex 建議 |
|---|---|---|
| Originality v1 系列 | 歷史稿 | 不公開。 |
| `ALE_Originality_Statement_v2.md` | 仍需修 | 仍寫核心構念均為作者獨立原創；Code-A1 與既有 ALE 出現後需重寫。避免自行發布「不存在惡意剽竊」式法律語氣。 |
| PriorArt v1 系列 | 歷史稿 | 保留。 |
| `ALE_PriorArt_RelatedWork_v2.md` | P0 | 檢索不充分且矩陣有誤讀；加入 Code-A1、PDD、Agentic Verification、Agentic Agile-V、Agentic SDLC reviews。 |
| `NOVELTY_AND_VALUE_ASSESSMENT.md` | 需重評 | C-A 已不能稱作者特化命名；C-B 與 PDD/formal verification 接近；C-C/C-D 可能仍有整合價值，但須擴大檢索。 |
| `README.md` | G5 應改為未過 | 不是只有非 arXiv 待核，現在還有直接 prior art 缺漏與錯誤解讀。 |

## 7. `06_Publication`

| 文件 | 判定 | Codex 建議 |
|---|---|---|
| `README.md` | 需更新 | 預印本 checklist 中 CFF/License 其實已備，但名稱未過；新增 GenAI disclosure 與 PDF metadata check。 |
| Publication Strategy v1 系列 | 歷史稿 | 保留。 |
| `ALE_Publication_Strategy_v2.md` | 需修 | 仍指向 `v2.4_gemini` 且檔尾標 v1_gemini；命名建議已失效。 |
| `DOI_GUIDE.md` | 大致可用 | 修正「預印本 DOI 不衝突」為「通常可接受，但每個 venue 必須查 prior-publication policy」。 |
| `ZENODO_SUBMISSION.md` | P0 | title、version、描述、CFF 待更名；不要附 AUTHOR.md；加入 AI disclosure。 |
| `IEEE_Software.md` | 投稿前重查 | 官方頁 snapshot 難以直接證實所有二手 IF/Q2 數字；移除不必要 IF 宣稱或用官方 JCR。 |
| `AIware_FORGE_conferences.md` | 基本可用 | AIware 是 conference，不應與 workshop 混稱；2027 日期必須屆時重查。 |
| `Journals_JSS_IST_EMSE_ASE.md` | 僅供內部 | IF/APC 多為二手來源，不可當正式投稿決策最終依據。 |
| `_raw_snapshots/*.html` | 有保存價值 | 是 2026-06-21 快照，不代表未來規則；標記 source URL + retrieval date + hash。 |
| `ALE_WhitePaper_v2.5_preview.docx` | 預覽而非發布品 | 標題與內容即將大改；不要轉 PDF 後直接上傳。 |

## 8. `99_References`

| 文件群 | 判定 | Codex 建議 |
|---|---|---|
| 10 篇 arXiv PDF | 檔案有效 | 書目存在不等於文中解讀正確。 |
| `2512.03097` | 被誤讀 | 原文 verifier 將 attack success rate 壓至 0；重寫所有引用。 |
| `2603.20281` | 相關性弱 | 主題是定價演算法 collusion 與異質性，不可直接支持 code/test verification。 |
| `2306.05685` | 可支持 judge bias，但有限 | 原文也提出偏誤可被緩解；不能推出所有 model panel 都無效。 |
| `2509.06216` | P0 命名衝突來源 | 不只是 related work，也已定義 Agentic Loop Engineering (ALE)。 |
| in-toto PDF | 可用 | 正確支持供應鏈 provenance。 |
| `README.md` | P0 | 加入 Code-A1；將 2512.03097 關係描述修正；新增全文閱讀狀態欄。 |

### 建議新增的直接文獻

1. Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning  
   https://arxiv.org/html/2603.15611v1
2. Agentic AI Software Engineers: Programming with Trust  
   https://arxiv.org/html/2502.13767v3
3. Governing Generated Software Through Invariants and Continuous Evidence  
   https://arxiv.org/html/2605.12981v3
4. Agentic Verification of Software Systems  
   https://arxiv.org/html/2511.17330v3
5. Bias in the Loop: Auditing LLM-as-a-Judge for Software Engineering  
   https://arxiv.org/html/2604.16790v1
6. Systematic Literature Review of Agentic AI across the SDLC  
   https://arxiv.org/abs/2605.15245

## 9. 發布候選檔案最小集合

首次 DOI 不需要把整個研究卷宗全部上傳。建議只上傳：

1. `v3.0` 正式 PDF。
2. 更新後 `CITATION.cff`。
3. `LICENSE`。
4. 可選：一份短版 `AI_USE_DISCLOSURE.md` 或放入 PDF。

不要上傳：

- 歷史草稿與 AI rewrite。
- 含 placeholder 的 AUTHOR。
- 內部研究日誌。
- 商業機密 skill 資料。
- 未完成 runner 與空白結果模板，除非明確標為 incomplete research artifact。

