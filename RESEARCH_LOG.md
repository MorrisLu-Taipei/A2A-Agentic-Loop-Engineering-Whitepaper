# ALE 研究進度：Milestone-Gate 儀表板 + Research Log

> 本檔是 ALE 研究的**時間/進度視圖**(結構分類見 `README.md`)。上半:現在在哪一關;下半:做了什麼的日誌。
> 一句話:**跑 loop → 出結論(過 G4)→ 才發表(G6)。預印本 DOI 可在 G4 前先走以鎖優先權。**

---

## 一、Milestone / Gate 儀表板（現在式)

**目前位置:G3 已過,卡在 G4(等第二案 Loop 1);預印本子路徑進行中。**

| Gate | 里程碑 | 狀態 | 卡點 / 解鎖條件 |
|---|---|---|---|
| **G0** 點子值得投入 | 失效模式種子(發票案) | ✅ | — |
| **G1** 主題收斂 | 定位/新穎性/RQ | 🟥 **重開** | 撞名(2509.06216)+ Code-A1 翻案 → v3.0 改名、降級新穎性 |
| **G2** 草稿自洽 | 白皮書 **v3.0** | ✅ | v3.0(更名+3 事實修正) |
| **G3** 審閱收斂 | Codex/Gemini + **第二輪 Codex DOI 審** | 🟥 **重開→已修** | 3 個 P0(撞名/prior-art/誤讀)已修進 v3.0 |
| **G4** 實證 | **EXP-002 主實驗** | ⛔ **未過(阻塞)** | Loop 0 已形式化;**Loop 1 第二案資料:目前無,待補** |
| **G5** 盡職調查 | prior-art / originality / 價值 | 🟥 **重開** | 補 Code-A1/2509.06216、檢索須窮盡化、新穎性重算 |
| **G6** 發表 | venue/DOI | 🟡 預印本子路徑 | 標題已定(方案 B);剩 PDF 轉檔 + (建議)補 prior-art;正式 full paper 須先過 G4 |

### 預印本 DOI 子路徑(G4 前可走)
- [x] LICENSE(CC BY 4.0)備妥
- [x] CITATION.cff 備妥(ORCID、最終標題待補)
- [x] Zenodo 上傳清單 `06_Publication/ZENODO_SUBMISSION.md`
- [x] **DOCX 預覽**產出(`06_Publication/ALE_WhitePaper_v2.5_preview.docx`;機密終檢 ✅ 無洩漏、無真 placeholder)
- [ ] 白皮書 v2.5 轉**正式 PDF**(待:① 標題拍板 ② mermaid 轉圖 ③ CJK 字型)
- [x] **ORCID**:0009-0006-5373-0586(已填入 CITATION.cff)。⚠ 上 Zenodo 時**用 ORCID 登入**,作品才會自動進 ORCID 紀錄(前兩筆未連動,需手動補)
- [x] **標題已拍板(2026-06-21,方案 B)**:*Governing Agentic Software Development with Executable Evidence: Mechanical Gates, Human Review, and Skill Capitalization*(內部代號 ALE 保留)
- [ ] 上 Zenodo 取 DOI → 回填 CITATION.cff

### 解鎖 G4 的唯一條件
> **一份結構不同於發票的資料(Loop 1)** → Agent + n8n 組裝 → 量 lead time/rework/reuse/defect。沒有它,G4 不過、正式論文不發。
>
> **🟥 阻塞紀錄(2026-06-21):目前「沒有第二案資料」。待補。** 量測框架、baseline、結果模板皆已備好(`04_Evidence/experiments/EXP-002.../`),資料一到即可直接跑、直接出降本數字。在資料到位前,G4 維持阻塞,**只走預印本子路徑**(Zenodo/arXiv),不投正式期刊/研討會。

---

## 二、Research Log（歷史軸,新到舊)

### 2026-06-21 (三) · 第二輪 Codex DOI 前審 → v3.0 大修 + 07/08 建立
- **Codex DOI 前審 = NO-GO**,3 個 P0 經**作者讀原文查證屬實**:① 名稱撞 arXiv:2509.06216 §5.2 的 "Agentic Loop Engineering (ALE)";② 漏 **Code-A1 [2603.15611]** 直接 prior art(self-collusion);③ **誤讀 2512.03097**(實為「外部證據 verifier 有效」)。
- **白皮書 v3.0**:更名《From Model Consensus to Executable Evidence》(ALE 降為內部代號);全卷宗修正誤讀;test collusion → shared-context false pass;新穎性降為「整合」;加 GenAI Use Disclosure;KPI→organization-defined。
- **新增 07_Lessons_Learned**(7 則 + meta:錯誤靠對抗式審查+讀原文抓出)、**08_Methodology**(3×AI 寫論文方法論,Design Science,self-cite 20264772)。
- **下載 Code-A1 PDF** 入 99_References(共 12 篇)。
- **G1/G3/G5 重開**;G4 仍卡第二案資料。誠實:這輪是「方法論抓到人類+主力 AI 的錯」的活案例。


### 2026-06-21 (續) · 機密化 + 創新性/價值評估 + G4 可執行部分備齊 + 預印本預覽
- **機密把關**:依指示將 Data2Dashboard skill set 全面**抽象化**(刪含細節的 Manifest,改 `SKILL_SUMMARY_abstract.md`;全卷宗 grep 零殘留技能名/路徑/契約);記憶亦更新機密鐵則。
- **創新性 × 研究價值評估卡**:`05_DueDiligence/NOVELTY_AND_VALUE_ASSESSMENT.md`——誠實結論:**新穎性=候選(特化+整合);研究價值之「有效性」=0 數據,待 G4**;prior-art 未窮盡。
- **G4 可執行部分備齊(等資料即可跑)**:EXP-002 量測 schema(`metrics/METRICS_SCHEMA.md`)、from-scratch baseline(`loop0/BASELINE_einvoice.md`)、結果模板(`results/RESULTS_TEMPLATE.md`);EXP-001 結果模板。
- **預印本預覽**:v3.0 → DOCX(機密終檢通過)。正式 PDF 待 mermaid 轉圖 + 字型嵌入。
- **仍卡**:G4 唯一硬輸入 = **第二案資料**;G6 預印本剩 PDF 轉檔 +(建議)補 prior-art(標題已定方案 B、ORCID 已具備)。

### 2026-06-21 · 研究卷宗成形 + Loop 0 形式化 + 預印本素材
- **卷宗結構化**:把研究卷宗改造成 ALE 式 **stage-gate 流水線**(00 Ideas → 06 Publication + 99 References),每目錄一份 README + Gate-Review Checklist。
- **外部研究與盡職調查**:查核 `agenticloops` repo(未發現實質重用);盤點 prior-art。下載並 API 核驗 10 篇 arXiv + in-toto 入 `99_References`。⚠ 此階段我**誤讀** arXiv:2512.03097(把結論講反),於 v3.0 由 Codex 審查 + 讀原文糾正(見 `07_Lessons_Learned` L1)。
- **多方審閱與校準**:Codex(降過度宣稱、補引文、設計實驗)→ 白皮書 v2.4;Gemini(統計形式化、Python 不變量、文獻、措辭)→ v2.5。**Gemini 案例研究的虛構日誌經查核攔截、未採用**,改放真實 `vv_crosscheck.py` 輸出。
- **實驗設計修正(重要)**:原誤把實驗窄化為「去重 test collusion」;更正為主實驗 **EXP-002 · Skill Capitalization Loop**(真實案例→SDLC→可重用可驗證 Skill→重用降本),EXP-001(test collusion)降為其「可驗證關卡」子實驗。
- **Loop 0 形式化**:把電子發票案萃取出的 **TigerAI 專有交付 skill set(商業機密,僅摘要)**對映成 **ALE 證據 + FSM 判定 = Validated**(未達 Certified,因需 ≥3 案)。細節不入卷宗。
- **作者資料**:建 `AUTHOR.md`(含「自我盤點找研究主題」方法);填入學經歷/證照(PMP、n8n L1、MCP)。
- **緣起故事**:`00_Ideas_Inspiration/STORY_origin_einvoice.md`、`01_Consolidation/STORY_consolidation.md`。
- **決策**:第二案尚未到位 → **先走預印本 DOI 子路徑**;備妥 LICENSE / CITATION.cff / Zenodo 清單。

### (此前)白皮書理論演進
- v1.1 產線骨架 → v1.2 可驗證(機械閘/反共謀/三層驗證)→ v2.0 可治理可稽核可沉澱 → v2.1 RQ/Evaluation/Maturity/權限/供應鏈/產線威脅 → v2.3 統計論證/需求不變量/AI 威脅。
- 實證來源:電子發票開放資料儀表板(`06_Product/04_EInvoiceDashboard`),其 LESSONS #3「同源假通過」為 test collusion 的真實起點。

---

## 三、待辦看板（下一步)
- 🟥 **阻塞(待補)**:Loop 1 第二案資料 —— **目前沒有資料**(2026-06-21 記)。這是 G4 的唯一硬卡關;資料到位前正式論文不發。
- ▶️ **可立即做**:白皮書 v2.5 轉 PDF → 上 Zenodo 取預印本 DOI(鎖優先權)。
- ▶️ **可立即做**:ORCID 申請、名稱拍板、非 arXiv 引文核驗(推進 G5)。
- 🔜 Loop 1 到位後:跑組裝 → 量降本 → 回寫 v2.6 → 升 §9.7 Matrix → 過 G4 → 投 IEEE Software / 規劃 AIware・FORGE 2027。
- 🔜 **(未來)related work 補引**:`book-to-skill`(MIT;書/文件→agent skill,遵 Agent Skills 標準)當 §2.7 skill-packaging 相關工作引用,並評估「Agent Skills 標準」當我方 skill 格式。**走查證流程**(讀原始 repo/標準、不憑印象)。詳見記憶 reference-book-to-skill。尚未動工。

---
*維護:每有進展就在「二、Research Log」加一條日期條目,並同步「一、儀表板」的 gate 狀態。*
