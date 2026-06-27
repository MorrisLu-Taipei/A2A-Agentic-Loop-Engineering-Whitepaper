# ALE 學術命名與標題查核

**作者 / Reviewer**：Codex（OpenAI）  
**版本 / Version**：v1.0.0_codex  
**日期 / Date**：2026-06-21  
**目標文件**：

- `02_Drafts/ALE_WhitePaper_v2.5.md`
- `CITATION.cff`
- `06_Publication/ZENODO_SUBMISSION.md`
- `06_Publication/ALE_Publication_Strategy_v2.md`
- `README.md`
- `RESEARCH_LOG.md`
- `06_Publication/ALE_WhitePaper_v2.5_preview.docx`

## 一、命名查核結論

### 1. `Agentic Loop Engineering (ALE)` 已被同領域文獻使用

`Agentic Software Engineering: Foundational Pillars and a Research Roadmap`（arXiv:2509.06216）已明確將 **Agentic Loop Engineering (ALE)** 定義為 Structured Agentic Software Engineering 的六項工程活動之一，用來治理 agents 如何探索、迭代與收斂。

這不是單純的縮寫碰撞，而是：

- 同一研究領域：Agentic Software Engineering。
- 相同完整詞：Agentic Loop Engineering。
- 相同縮寫：ALE。
- 相近內涵：可觀測、可重現、可治理的 agent execution loop。

因此，`System Development` 前綴不足以消除學術歧義。若沿用，搜尋、引用與審稿都會先遇到「是否沿用或改寫既有 ALE」的問題。

### 2. `System Development Agentic Loop Engineering` 英文不自然

學術與工程慣用語是 `software development`、`systems development` 或 `software engineering`。`System Development Agentic Loop Engineering` 的修飾關係不清楚，像把數個名詞硬串在一起。

### 3. 不建議再創造另一個縮寫

目前最有利的做法不是立即造出 EGASD、VA-SDLC 等新縮寫，而是使用一個清楚、可搜尋、直接陳述貢獻的學術標題。框架成熟並經同行引用後，再決定是否需要品牌化名稱。

## 二、Codex 最推薦的 DOI 標題

### 推薦方案 A（學術最穩）

> **From Model Consensus to Executable Evidence: An Evidence-Governed Lifecycle for Agentic Software Development**

中文：

> **從模型共識到可執行證據：Agentic 軟體開發的證據治理生命週期**

理由：

- 不與既有 ALE 撞名。
- 直接凸顯本文最強的差異：model consensus → executable evidence。
- `lifecycle` 能涵蓋 SDLC、治理、回滾、監控與技能沉澱。
- 不宣稱已證明某個新自然定律。

### 推薦方案 B（工程治理導向）

> **Governing Agentic Software Development with Executable Evidence: Mechanical Gates, Human Review, and Skill Capitalization**

優點：三項設計元件一眼可見。  
缺點：標題較長。

### 推薦方案 C（保留歷史名稱但降為副題）

> **From Model Consensus to Executable Evidence: The TigerAI ALE Framework for Agentic Software Development**

此方案只適合 ALE 已是公司既有品牌、必須保留時使用。內文必須明確寫：

> TigerAI ALE is unrelated to the previously published use of “Agentic Loop Engineering (ALE)” in arXiv:2509.06216.

Codex 不推薦此方案作學術首選，因為仍會形成引用歧義。

## 三、現象命名建議

### `test collusion` 不適合再當作主要原創詞

原因：

1. `test collusion` 長期已用於教育測驗舞弊研究。
2. 2026-03 的 `Code-A1` 已直接使用 **self-collusion** 描述單一模型或共享目標下的 code/test generation 問題。
3. 目前電子發票案例是 shared-source false pass analogue，不是兩個 agent 有策略性合謀。

建議主要使用中性操作型名稱：

> **shared-context false pass**

或：

> **implementation-conditioned false pass**

內文可保留：

> We initially referred to this failure mode as “test collusion”; in this paper we use the more descriptive term “shared-context false pass” to avoid implying intentional coordination.

中文：

> 本研究早期將此失效模式稱為「測試共謀」；正式稿改用「共享脈絡假通過」，避免暗示 agent 具有主觀合謀意圖。

## 四、建議的引用名稱

### DOI / Zenodo

> Lu, Y.-H. (2026). *From Model Consensus to Executable Evidence: An Evidence-Governed Lifecycle for Agentic Software Development* (Version 3.0) [Working paper]. Zenodo. DOI

### 作者名稱

學術 metadata 統一使用：

> **Yeh-Hsing Lu**

`Morris` 可放在作者介紹或括號中，但不應讓主稿使用 `Morris`、CFF 使用 `Yeh-Hsing (Morris)`、Zenodo 又使用另一種形式。

## 五、名稱變更的版本策略

因為主標題與核心術語變更屬重大變更，建議：

- 將下一版定為 **v3.0**，不要叫 v2.6。
- v2.5 保留為內部歷史稿。
- v3.0 在 Version Lineage 說明：
  - 避免與 arXiv:2509.06216 的既有 ALE 術語混淆。
  - 納入 Code-A1 等直接 prior art。
  - 將 test collusion 校準為 shared-context false pass。

## 六、網路查核的主要來源

- Agentic Software Engineering roadmap / 既有 Agentic Loop Engineering (ALE)：  
  https://arxiv.org/html/2509.06216v2
- Code-A1 / code-test self-collusion：  
  https://arxiv.org/html/2603.15611v1
- Agentic Software Development Lifecycle 的既有使用：  
  https://arxiv.org/abs/2604.26275
- Zenodo DOI 與 record 規則：  
  https://help.zenodo.org/docs/deposit/about-records/
- DataCite 版本 DOI 建議：  
  https://support.datacite.org/docs/best-practices-for-datacite-members

