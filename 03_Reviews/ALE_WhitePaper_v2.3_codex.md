# `ALE_WhitePaper_v2.3.md` Codex 審閱建議

**目標文件**：`ALE_WhitePaper_v2.3.md`  
**審閱範圍**：研究定位、主張強度、相關研究、實證設計、工程可操作性  
**總評**：框架完整度高；目前主要缺口是直接實證與正式引文，而不是概念數量。

## 一、必改項目（P0）

### 1. 版本沿革中的「無懈可擊」

**位置**：版本沿革與結論版本摘要。

**風險**：不可證偽且語氣超過 Working Draft 可承受的證據強度，會讓審稿人轉而尋找反例。

**建議改寫**：

> ALE v2.3：強化統計論證、需求源頭防禦與 AI 特有威脅模型。

### 2. 「LLM 對自身輸出的自我審查近乎無效」

**位置**：§5.3。

**風險**：目前引用與實驗不足以支持接近全稱命題；不同模型、任務、提示與工具回饋會改變結果。

**建議改寫**：

> 生產者與審查者應維持角色、上下文與證據來源的適度獨立。當審查者與生產者共享模型、實作脈絡或錯誤來源時，自我審查可能受到共同偏誤限制。

### 3. Test Collusion 的學術定位

**位置**：§1.2、§1.3、§1.5、§7.1。

**風險**：若描述為完全新發現，會與 test oracle problem、common-mode failure、test-suite overfitting、LLM self-preference 及 multi-agent collusion 文獻正面碰撞。

**建議定義**：

> Test collusion 是 Agentic SDLC 中，生產者與驗證者因共享實作脈絡、規格轉譯、訓練偏誤或資料來源，而形成的 correlated false-pass failure mode。

**可辯護的新穎性**：

1. 將相關失效特化到 PG Agent 與 V&V Agent 的軟體驗證關係。
2. 將 mechanical evidence 設為不可被模型共識覆寫的 release gate。
3. 整合為 Agentic SDLC 的治理架構，而不是只描述單一測試技術。

### 4. 補齊正式引用

**位置**：§2.6、§7.2、References 12–13。

**必補類型**：

- Test oracle problem survey
- Metamorphic testing 與 oracle problem
- LLM-as-a-Judge self-preference / position / verbosity bias
- SWE-bench 與 SWE-bench Verified
- Agentic SWE roadmap
- Multi-agent collusion / verifier insufficiency
- Prompt injection 與 agent hijacking
- Software supply-chain provenance（如 SLSA、in-toto）

**禁止狀態**：正式公開版不得保留「待補」引用。

## 二、重要改進（P1）

### 5. 把「框架、規範、假說」分層

目前部分段落把設計主張寫成已驗證結論。建議在每個核心命題加標籤：

| 類型 | 示例 |
|---|---|
| Design Principle | No evidence, no release |
| Engineering Specification | State Object、RBAC、append-only evidence |
| Research Hypothesis | 多模型評議無法有效降低共享偏誤 |
| Preliminary Evidence | 電子發票單案例 |
| Validated Finding | 待 EXP-001 或後續研究產生 |

### 6. 修正 §7.2 的統計表述

**風險**：直接寫「LLM 之間是高度相關估計器」仍需實際測量；條件協方差趨近 1 也不應作為一般性事實。

**建議**：

- 將其寫為待驗假說。
- 定義錯誤向量與相關性的可觀測方式。
- 在 EXP-001 中量測不同測試生成條件的 error correlation。
- 避免把「不同模型」與「統計獨立」畫上等號。

### 7. Mechanical Gate 不等於 Ground Truth

**位置**：摘要、§7.3、§7.4。

**風險**：coverage、mutation score 與 property tests 是強證據，但不自動等於需求真實性或完整 correctness oracle。

**建議用語**：

> Mechanical gates provide executable, reproducible evidence that is less dependent on model opinion; they do not by themselves guarantee specification correctness.

中文：

> 機械閘提供可執行、可重現且較不依賴模型意見的證據，但不單獨保證需求與系統的完整正確性。

### 8. Skill Curator 的固定閾值應標為初始政策

**位置**：§9.2.1。

`τ = 0.85` 目前沒有資料支持。建議標示為：

> 初始政策值，須以人工標註的 duplicate/merge 資料集校準，並依技能類型分層設定。

另外，AST 不適用於 Prompt、n8n workflow、Policy 等所有 Skill 類型；需定義 artifact-specific similarity strategy。

### 9. 成熟度模型需要驗收條件

**位置**：§11。

每一級至少補：

- Entry criteria
- Required artifacts
- Mandatory gates
- Evidence retention
- Human authority
- 可量測 KPI

否則 L0–L5 容易成為描述性分級，難以用於企業診斷與驗收。

## 三、建議新增（P2）

### 10. 新增 Claim–Evidence Matrix

建議在 §10 前加入：

| Claim ID | 主張 | 現有證據 | 證據等級 | 下一步 |
|---|---|---|---|---|
| C1 | Test collusion 存在 | EInvoice 單案例 | Preliminary | EXP-001 |
| C2 | Mechanical gate 優於 model review | 單一案例方向性證據 | Preliminary | Controlled ablation |
| C3 | Skill reuse 降低成本 | 尚無 | Hypothesis | 跨專案追蹤 |
| C4 | Evidence Repository 提升可稽核性 | 架構主張 | Design | Auditor study |

### 11. 將工程規格拆出

白皮書同時承擔研究論文、架構規範與產品藍圖，篇幅與論證焦點容易失控。建議後續拆成：

- ALE White Paper：問題、理論、框架、證據。
- ALE Technical Specification：State Schema、RBAC、Gate Policy、JSON-RPC。
- ALE Evaluation Protocol：實驗、指標、資料與統計方法。

## 四、建議的 v2.4 進入條件

不要因新增文句就建立 v2.4。建議至少完成：

1. Prior art 文獻逐筆核驗。
2. References 不再有 placeholder。
3. 案例措辭與證據強度對齊。
4. EXP-001 protocol 凍結或已有 pilot 結果。
5. Claim–Evidence Matrix 完成。

