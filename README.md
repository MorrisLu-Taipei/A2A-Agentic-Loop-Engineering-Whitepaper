<!--
  ============================================================================
  FOR AI AGENTS / A2A
  Continue from:
    1. 08_Methodology/AGENTS.md
    2. 08_Methodology/CURRENT_HANDOFF.md
    3. Codex only: 08_Methodology/CODEX_OPERATING_GUIDE.md

  Hard rules:
  - producer != reviewer
  - verify AI output against primary evidence
  - no gate, no proceed
  - only a human may approve publication or a "validated" claim
  - never expose secrets, tokens, or proprietary skill internals
  ============================================================================
-->

# Agentic Loop Engineering（ALE）

> 從「AI 一天做出一個具分析能力的 Dashboard」，走向一套可治理、可驗證、可重複、能累積技能資產的 Agentic Software Engineering 方法。

**研究主持人**：Yeh-Hsing Lu（Morris）  
**研究單位**：Tiger AI Tech Co., Ltd., Taiwan  
**ORCID**：[`0009-0006-5373-0586`](https://orcid.org/0009-0006-5373-0586)  
**目前狀態**：Working Paper；受控實驗尚未完成；Zenodo DOI 尚未發布  
**最後更新**：2026-06-22（Codex）

---

## 這項研究在解決什麼問題？

AI 已經能快速產生可執行的程式，但「做得出來」不等於「可以放心交付」。

當 AI 開始負責需求、設計、開發、測試、部署與維運，真正困難的問題變成：

> 當寫程式的是 AI、驗證程式的也是 AI，我們要如何避免它們一起犯錯、一起通過，最後互相背書？

ALE 的回答不是「再多加一個 AI」，而是建立一條有責任分工與證據關卡的工程循環：

1. **完整生命週期迴圈**：從問題定義、需求、設計、開發、驗證、資安、部署到回饋。
2. **可執行證據治理**：能機械驗證的項目，以測試、不變量、掃描與真實執行結果裁決。
3. **人類保留最終權限**：AI 提案與執行，人類審查證據、承擔決策責任。
4. **技能資產化**：把每次專案中可重用、可測試、可治理的能力沉澱成 Skill。

一句話版本：

> **ALE 是把 Agentic AI 從「一次性寫程式」提升成「有證據、有關卡、可回滾、會累積能力的軟體工程循環」。**

---

## 研究是怎麼開始的？

Morris 是研究 AI 的博士生。他想驗證一件很實際的事：

> AI 到底可以多快完成一個專業、動態，而且具有 AI 推理分析能力的資料網站？

他當時正在研究臺灣統一發票資料，找到政府開放資料後，將參考 Dashboard 圖片與需求交給 AI。AI 在一天內完成第一版系統，包含：

- 回歸數據 AI 推論
- CLI AI 分析
- 數據落點 AI 分析

這次成果令人驚豔，但也帶出下一個問題：如果 AI 能做一次，能不能把整個過程工程化，讓 Agent 一輪一輪可靠地重做？

於是，單次 Dashboard 實驗逐漸發展成 **Agentic Loop Engineering**。

開發期間也出現過關鍵失敗：Claude Code 產生的資料處理錯誤造成約 **4.5 倍資料膨脹**，後來由獨立的 Codex 審查發現並修正。這個事件不是受控實驗結果，而是一項回溯式田野觀察；它促成 ALE 的核心治理原則：

> **生產者不能同時是唯一審查者；模型共識不能取代外部證據。**

完成工程框架後，研究又進入下一層：使用同一套 ALE 流程，讓 Claude、Codex、Gemini 與人類作者協作研究、審稿、查證並準備 DOI。換句話說，這份研究卷宗本身也是 ALE 的自我應用案例。

---

## ALE 的研究定位

### 對外工程名稱

**Agentic Loop Engineering（ALE）**

### 學術定位

ALE 被定位為一套 **evidence-governed agentic software engineering framework**，重點不是宣稱發明 agent loop、SDLC、mutation testing 或「Agentic Loop Engineering」這個詞，而是提出並實作以下整合：

- Agentic SDLC 的階段、產物、權限與 Gate
- Producer / Reviewer 分離
- Mechanical Evidence / Model Review / Human Decision 三層驗證
- Evidence、Policy、Project 與 Skill Repository
- Skill 的版本、驗證、升級、退役與重用生命週期

> **學術命名提醒**：arXiv:2509.06216 已在 2025 年使用 `Agentic Loop Engineering (ALE)` 一詞。本研究可以把 ALE 作為 TigerAI 的公開框架名稱，但不可宣稱首創該名詞。正式論文應引用先前用語，並把貢獻放在「可執行證據治理、完整生命週期整合與技能資產化」。

---

## 目前有什麼證據？

| 主張 | 現有證據 | 目前等級 |
|---|---|---|
| AI 可快速完成具分析能力的 Dashboard | 電子發票開放資料案例與公開 Demo | 田野觀察 |
| 同源資料或共同脈絡可能造成 false pass | 4.5× 膨脹事件的回溯紀錄 | 初步觀察 |
| 外部不變量可提供較獨立的檢查基準 | 修復後 `vv_crosscheck.py` 實跑 PASS，比例 17.3% | 初步工程證據 |
| Mechanical gate 優於單純多模型審查 | EXP-001 協定已建立，runner 尚未完成 | 待驗證假說 |
| Skill Repository 可降低後續專案成本 | EXP-002 只有 Loop 0，缺第二案例 | 待驗證假說 |

重要限制：

- 修復前的 4.5× 資料快照與真實 FAIL log 未保留。
- 現存 17.3% PASS 證明的是「修復後資料符合上界」，不能反推當時 Gate 已實際攔下錯誤。
- EXP-001 / EXP-002 尚未完成，因此目前沒有核心主張可標示為 `[validated]`。
- DOI 只能證明文件被永久識別與公開保存，**不等於通過同行評審**。

---

## 研究卷宗怎麼讀？

如果你第一次進來，建議依序閱讀：

1. [`00_Ideas_Inspiration/STORY_origin_einvoice.md`](00_Ideas_Inspiration/STORY_origin_einvoice.md) — 研究起點
2. [`01_Consolidation/STORY_consolidation.md`](01_Consolidation/STORY_consolidation.md) — 如何收斂成研究問題
3. [`02_Drafts/ALE_WhitePaper_v3.2_EN.md`](02_Drafts/ALE_WhitePaper_v3.2_EN.md) — 現行英文工作稿(v3.2)
4. [`04_Evidence/ALE_CaseStudy_EInvoice_v2.md`](04_Evidence/ALE_CaseStudy_EInvoice_v2.md) — 電子發票案例與證據限制
5. [`08_Methodology/README.md`](08_Methodology/README.md) — 人類與多 AI 如何協作
6. [`03_Reviews/ALE_WhitePaper_v3.1_DOI_Review_v1.0.0_codex.md`](03_Reviews/ALE_WhitePaper_v3.1_DOI_Review_v1.0.0_codex.md) — 最新 DOI 前審

### 給 AI Agent

不要從這份人類導讀直接開始執行。請依序閱讀：

1. [`08_Methodology/AGENTS.md`](08_Methodology/AGENTS.md)
2. [`08_Methodology/CURRENT_HANDOFF.md`](08_Methodology/CURRENT_HANDOFF.md)
3. Codex 再讀 [`08_Methodology/CODEX_OPERATING_GUIDE.md`](08_Methodology/CODEX_OPERATING_GUIDE.md)
4. 需要 A2A schema / JSON-RPC 時才讀 [`08_Methodology/A2A_SKILLSET.md`](08_Methodology/A2A_SKILLSET.md)

沒有真實 A2A 或 n8n runtime 時，必須清楚標示使用本地 workspace adapter，不能假裝遠端 Agent 已執行。

---

## Stage-Gate 研究流程

```text
00 Ideas
   └─G0→ 01 Consolidation
          └─G1→ 02 Drafts
                 └─G2→ 03 Reviews
                        └─G3→ 04 Evidence
                               └─G4→ 05 Due Diligence
                                      └─G5→ 06 Publication
                                             └─G6→ Publish

07 Lessons Learned  ↺ 回饋所有階段
08 Methodology      ─ 橫向規範人類／AI／A2A 工作方式
99 References       ─ 橫向提供文獻與一手來源
```

| 目錄 | 用途 | 現況 |
|---|---|---|
| [`00_Ideas_Inspiration/`](00_Ideas_Inspiration/) | 起源、靈感、開放問題 | 持續累積 |
| [`01_Consolidation/`](01_Consolidation/) | 收斂研究問題、定位與新穎性 | 已建立 |
| [`02_Drafts/`](02_Drafts/) | 作者主稿與版本演進 | v3.2 working paper |
| [`03_Reviews/`](03_Reviews/) | Codex、Gemini 與外部獨立審閱 | DOI 前審進行中 |
| [`04_Evidence/`](04_Evidence/) | 案例、EXP-001、EXP-002 與執行證據 | G4 未通過 |
| [`05_DueDiligence/`](05_DueDiligence/) | prior art、原創性與引文盡調 | 尚需完整核驗 |
| [`06_Publication/`](06_Publication/) | PDF、DOI、venue 與 metadata | 尚未發布 DOI |
| [`07_Lessons_Learned/`](07_Lessons_Learned/) | 錯誤、修正與可重用教訓 | 持續回饋 |
| [`08_Methodology/`](08_Methodology/) | Agent 工作規則與 A2A 方法 | 已建立 |
| [`99_References/`](99_References/) | 一手文獻與核驗索引 | 持續補全 |

### Gate 鐵則

```text
No converged research question, no drafting.
No self-consistent draft, no independent review.
No resolved review, no evidence claim.
No measured evidence, no validated claim.
No verified references and metadata, no DOI release.
No human approval, no publication.
```

---

## 人類與 AI 如何分工？

| 角色 | 主要責任 | 不可取代的人類責任 |
|---|---|---|
| Morris | 找題目、定研究價值、提供田野事實、做最終決策 | 作者責任、證據真實性、發表核可 |
| Claude | 操作化、整合、程式與文件生產 | 不可自行宣稱驗證完成 |
| Codex | 獨立對抗審查、找矛盾、查 prior art、檢查證據 | 不可替作者按下 Publish |
| Gemini | 形式化、結構化、文字與分析補強 | 產出仍須查一手來源 |
| Mechanical Gate | 執行測試、不變量、掃描與門檻判定 | 只能裁決可機械化條件 |

核心不是「三個 AI 投票」，而是：

> **AI 分工產生與挑戰；機械證據處理可測事實；人類對研究判斷與公開主張負責。**

---

## 白皮書與 DOI 狀態

### 現行候選

- 英文來源：[`02_Drafts/ALE_WhitePaper_v3.2_EN.md`](02_Drafts/ALE_WhitePaper_v3.2_EN.md)
- 英文 PDF：[`06_Publication/ALE_WhitePaper_v3.2_EN.pdf`](06_Publication/ALE_WhitePaper_v3.2_EN.pdf)
- 引用資料：[`CITATION.cff`](CITATION.cff)
- Zenodo 作業：[`06_Publication/ZENODO_SUBMISSION.md`](06_Publication/ZENODO_SUBMISSION.md)

### 目前判定

**v3.2(2026-06-22)已修正 Codex v3.1 前審的 6 個 P0;DOI 仍待最後人工關卡。**

| # | Codex v3.1 P0 | v3.2 處理 |
|---|---|---|
| 1 | 命名與「internal codename / unrelated」矛盾 | ✅ 採 Agentic Loop Engineering(ALE)為對外框架名、**不宣稱首創此名詞**;移除矛盾敘事 |
| 2 | 版本/metadata 不一致 | ✅ 內文、`CITATION.cff`、`ZENODO_SUBMISSION`、PDF metadata 全統一 v3.2 |
| 3 | §7.7 測試無法觸發去重缺陷 | ✅ 改「去重蛻變關係 + 獨立外部上界」兩條有效 property,標為 post-fix 回歸防護 |
| 4 | 4.5× 過度宣稱「Gate 當時攔截」 | ✅ 改寫為**回溯式田野觀察**;C1/C2/C6 降級 |
| 5 | 「引文全核驗」與「待核」衝突 | ✅ 揭露改為「核心引文已核、其餘標待核」 |
| 6 | 安全/閘絕對語句 | ✅ 軟化(「管線不能被改」「定生死」) |

**v3.2 後續修正(2026-06-22)**:✅ 文獻 #14(MCP)/#22(Data Science Dojo)已核驗官方出處(移除「待核」);✅ §9.7 Claim–Evidence Matrix PDF 表格排版修復(原顯示成 markdown 管線文字);✅ 清除 Zenodo 指南殘留 v3.0 文字。

**目前 Zenodo GO 狀態**:✅ **可建 Draft**、✅ **可「Get a DOI now」預留 DOI**;❌ **先不要 Publish**、❌ 不要視為正式發布完成。**最終 GO 前唯一人工關卡**:作者逐頁閱讀核可(視需要再補系統性文獻回顧)。現行稿:`02_Drafts/ALE_WhitePaper_v3.2_EN.md` / `06_Publication/ALE_WhitePaper_v3.2_EN.pdf`(v3.0/v3.1 保留為演進證據)。

完整審查見:

[`03_Reviews/ALE_WhitePaper_v3.1_DOI_Review_v1.0.0_codex.md`](03_Reviews/ALE_WhitePaper_v3.1_DOI_Review_v1.0.0_codex.md)

---

## 授權與引用

- 文件授權：[`LICENSE`](LICENSE)（CC BY 4.0）
- 引用格式：[`CITATION.cff`](CITATION.cff)
- 作者資料：[`AUTHOR.md`](AUTHOR.md)

在 DOI 正式發布前，請把本卷宗視為持續修訂中的研究工作，不要把 Working Paper 的設計主張描述為已經驗證的實證結論。

---

*TigerAI · Agentic Loop Engineering research dossier*  
*README rewritten by Codex, version 2.0.0_codex, 2026-06-22.*
