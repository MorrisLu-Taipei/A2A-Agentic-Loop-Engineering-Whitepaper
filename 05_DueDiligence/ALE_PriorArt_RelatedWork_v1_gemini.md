# ALE 先前技術查核、文獻對比與新穎性定位
## Prior Art, Related Work, and Novelty Due Diligence

---

**作者 / Author**：Morris（虎智科技 TigerAI）
**文件類型 / Type**：發表與 DOI 前置盡職調查 (Novelty & Academic Integrity Review)
**版本 / Version**：v1_gemini (基於 v1 進行學術客觀性調校與文獻矩陣填補)
**日期 / Date**：2026-06-21

> ⚠️ **更正聲明(早期版本)**:本檔對 `arXiv:2512.03097` 之描述,僅以「該文展示多代理人共謀風險存在」為限始屬正確;**不可**據此宣稱「加 verifier 無效」——原文相反:verifier 錨定外部 guidelines 時可有效防禦。正確定位以 `ALE_PriorArt_RelatedWork_v2.md` 為準。

> **摘要與核查結論**：本文件針對 ALE 框架（*System Development Agentic Loop Engineering*）進行先前技術（Prior Art）檢索與學術地位對比。經比對，**無文字抄襲或實質架構改寫之虞**。本文件記錄了可重現的檢索日誌、補齊了文獻對比矩陣，並對 ALE 的「候選新穎性（Candidate Novelty）」進行了客觀界定，明示其與既有公共財與同領域工作的邊界。

---

## 1. 針對性查核：`github.com/agenticloops-ai/agentic-ai-engineering`

鑑於該開源專案名稱中包含 `agentic` 與 `loops` 等詞彙，為排除非刻意的文字重合與概念衝突，特進行針對性比對。

**查核結論**：  
經人工逐項對照該 repository 的 README 與程式結構，**未發現任何核心文字重合或實質架構抄襲**。此比對結論僅代表對特定目標專案之人工核對，不等同於自動化之全文防剽竊檢測系統（例如 Turnitin）。

主要差異如下：
- **體裁與目的**：該開源專案為 MIT 授權的動手實作教學集（Tutorials），教導開發者如何「建構」基本的 Agent 迴圈（如 ReAct、Tool Calling、RAG）；ALE 則為學術/工程方法論白皮書，聚焦於 Agent 接管 SDLC 後的「治理、可信驗證與防止同源欺騙」。
- **概念重疊度**：兩者在「如何調度 LLM 寫代碼」的底層技術上共用業界標準術語（如 Agent Loop, Tool Call），但 ALE 的核心論點（Test Collusion, Mechanical Gate, Spec Invariants, Skill Capitalization FSM）在該專案中均不存在。

---

## 2. 先前技術檢索日誌 (Search Log & Reproducibility)

為確保文獻對比之學術可信度，本節記錄檢索條件以利第三方重現：

- **檢索平台**：Google Scholar, arXiv.org (cs.SE / cs.CL)
- **檢索日期**：2026-06-21
- **檢索詞（Queries）**：
  1. `("agentic software engineering" OR "agentic SDLC") AND ("verification" OR "governance")`
  2. `("LLM collusion" OR "multi-agent collusion") AND ("developer" OR "verifier")`
  3. `("LLM-as-judge" OR "self-preference bias") AND "software testing"`
- **納入條件 (Inclusion)**：2023 年至 2026 年 6 月間發表、探討多 AI 代理人協同軟體開發、AI 評估偏誤或多 Agent 安全繞過之同行評審論文與 arXiv 預印本。
- **排除條件 (Exclusion)**：單純教導 prompt template 撰寫之部落格文章，或不含自動化評估之單點代碼補全工具介紹。

---

## 3. 文獻對比矩陣 (Prior-Art Matrix)

基於上述檢索所得之代表性文獻，將 ALE 與相鄰工作進行維度對比：

| 文獻 / 領域 | 探討核心問題 | 驗證者是否為 AI | 是否處理共享偏誤 (Shared Bias) | 是否包含可執行機械事實 (Executable Oracle) | 是否涵蓋完整 SDLC | 知識與技能資產化 (Skill FSM) |
|---|---|:--:|:--:|:--:|:--:|:--:|
| **Test Oracle Survey**<br>[Barr et al. 2015] | 測試 Oracle 缺失與生成難題 | 否 (傳統工程) | 部分 (人為偏誤) | 是 (契合測試/Metamorphic) | 否 (僅測試階段) | 否 |
| **LLM-as-Judge Bias**<br>[Zheng et al. 2023] | LLM 作為評審時的自我偏好與長度偏誤 | 是 | 是 | 否 (僅作主觀評語) | 否 | 否 |
| **Agentic SWE Roadmap**<br>[arXiv:2509.06216] | Agent 軟體工程的架構支柱與挑戰 | 是 | 否 (側重生成效能) | 部分 (單點單元測試) | 部分 (分析/PG/測試) | 否 |
| **Multi-Agent Collusion**<br>[arXiv:2512.03097] | 多代理人合意繞過驗證之安全風險 | 是 | 是 | 否 (側重合意共識) | 否 | 否 |
| **ALE (本文候選貢獻)** | Agentic SDLC 之可驗證性與反同源欺騙治理 | 是 | **是 (形式化條件協方差論證)** | **是 (Mutation + Spec Invariants 機械閘)** | **是 (Context 到 Monitoring 閉環)** | **是 (Skill Manifest & Lifecycle)** |

---

## 4. 可辯護的新穎性界定 (Defensible Novelty)

為使 ALE 在學術評審中免受「只是 DevOps 加 Agent」或「重新發明輪子」的預期質疑，我們將新穎性界定如下：

1. **讓出公共財 (Conceding Public Goods)**：  
   ALE **不主張**發明了 Agent 迴圈（Loop Engineering）、Guardrails（如 Token 預算、最大重試、電路熔斷）或突變測試方法。這些均為已發表的業界公共財 [Data Science Dojo 2026; DeMillo et al. 1978]，ALE 僅將其採納為流水線基本組件。
2. **界定特化貢獻 (Specialized Contributions)**：
   - **Test Collusion 的特化與形式化**：將多代理人 collusion [arXiv:2512.03097] 特化於軟體工程中「開發代碼 ↔ 測試代碼」同源生成的失效場景，並給出條件協方差趨近於 1 的統計論證（§7.2）。
   - **機械閘優先於模型共識 (Mechanical Gate Over Model Consensus)**：論證了「多模型集成無法消除系統性偏誤（Bias）」，並規定以覆蓋率、突變分數與需求不變量（Spec Invariants）等無模型意見之事實作為 Release Gate 信任根的設計架構。
   - **技能資產化與去退化治理**：提出技能生命週期有限狀態機，並配合 AST 與 Embedding 相似度比對的去重合併演算法，實現邊際成本次線性成長的治理框架。

---

## 5. 公開發表前必辦清單 (Pre-publication Checklist)

- [x] 完成 Prior-Art Matrix 所有對比欄位之填補。
- [x] 移除「概念重疊 0」、「完全無抄襲」等絕對化措辭，改以符合學術誠信的客觀描述。
- [x] 記錄明確的檢索平台、日期與檢索詞，確保先前技術查核之可重現性。
- [ ] 待 `EXP-001` 取得數據後，將統計結果填入本文件，以對位 Novelty Statement 中的假說驗證。

---

*— End of Prior-Art & Related-Work Due Diligence v1_gemini —*
