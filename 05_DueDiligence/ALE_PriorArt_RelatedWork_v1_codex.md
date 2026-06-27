# `ALE_PriorArt_RelatedWork_v1.md` Codex 審閱建議

**目標文件**：`ALE_PriorArt_RelatedWork_v1.md`  
**總評**：方向正確，已開始把 ALE 從「宣稱原創」轉為「可辯護差異化」；但目前仍屬檢索筆記，尚不能作為正式 novelty due diligence。

## 一、必改項目

### 1. 不宜下「無抄襲」的絕對結論

只檢查單一 GitHub repository，不能推出整體無抄襲或無非刻意文字重合。

**建議改寫**：

> 就目前針對指定 repository 的人工比對，未發現 ALE 核心文字或結構有實質重用跡象；此結論不等同完整學術抄襲檢測。

### 2. 「概念重疊 0」不可信

兩者仍共享 agent loop、guardrail、tool use 等上位概念。差異應寫在研究問題與治理範圍，不應寫成零重疊。

### 3. 所有 2025–2026 文獻須逐筆核驗

正式納入白皮書前，記錄：

- 正確題名
- 作者
- arXiv/DOI
- 首次提交與目前版本日期
- 研究方法
- 原文實際結論
- 與 ALE 的支持、競爭或中立關係

搜尋摘要或二手文章不能取代全文核驗。

### 4. 「據我們所知」需附檢索範圍

建議在方法中記錄：

- 檢索平台
- 檢索日期
- Query
- 納入／排除條件
- 截止年份

否則「尚未見於既有文獻」不可重現。

## 二、建議的新穎性表述

> ALE 不主張發明 agent loop、SDLC、guardrail、mutation testing 或 multi-agent collusion。ALE 的候選貢獻，是把共享偏誤造成的驗證假通過特化為 Agentic SDLC 的 test-collusion failure mode，並以 mechanical evidence、model disagreement 與 human evidence review 的權責分層，組成可稽核、可回滾的治理框架。

「候選貢獻」應等 EXP-001 與系統性文獻回顧後，再升級為正式貢獻。

## 三、建議新增 Prior-Art Matrix

| 文獻 | 問題 | 驗證者是否為 AI | 是否處理共享偏誤 | 是否有 executable oracle | 是否涵蓋完整 SDLC | Skill governance |
|---|---|---:|---:|---:|---:|---:|
| Test Oracle Survey | oracle 缺失 | 否 | 部分 | 多種 | 否 | 否 |
| LLM-as-Judge Bias | 模型評審偏誤 | 是 | 是 | 否 | 否 | 否 |
| Agentic SWE Roadmap | Agent 軟體工程 | 是 | 待核 | 部分 | 部分 | 待核 |
| Multi-Agent Collusion | Agent 共謀 | 是 | 是 | 視研究而定 | 否 | 否 |
| ALE | Agentic SDLC 治理 | 是 | 是 | mechanical evidence | 是 | 是 |

空格必須以全文閱讀結果填寫，不能先假設 ALE 勝出。

## 四、名稱建議

保留 ALE 可行，但主打詞應由「Loop Engineering」轉成：

- Anti-Self-Deception Governance
- Agentic Software Assurance
- Evidence-Governed Agentic SDLC

推薦對外一句話：

> ALE is an evidence-governed Agentic SDLC framework for preventing shared-source false confidence in AI-produced software.

## 五、公開前檢查

1. 全部文獻已全文核驗。
2. 不使用「無抄襲」「全球首創」「概念重疊 0」等絕對措辭。
3. 明確區分公共財、採納整合與候選原創。
4. 文獻矩陣可重現。
5. Novelty statement 與 EXP-001 結果一致。

