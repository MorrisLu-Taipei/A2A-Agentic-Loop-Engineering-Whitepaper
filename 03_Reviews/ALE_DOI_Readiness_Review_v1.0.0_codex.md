# ALE DOI 發布準備度總審

**作者 / Reviewer**：Codex（OpenAI）  
**版本 / Version**：v1.0.0_codex  
**日期 / Date**：2026-06-21  
**目標**：判斷現行 `v2.5` 是否可作為 Zenodo DOI Working Paper 發布。

## 一、總判定

### 現況：NO-GO

現行檔案不應直接發布 DOI。不是因為 Working Paper 必須先有完整實驗，而是目前有數項會永久污染學術紀錄的 P0。

Zenodo 官方說明指出：record 發布後 metadata 可以修改，但檔案與 persistent identifier 不能直接修改；內容錯誤通常需建立新版本。因此，名稱、引用與作者揭露應在首次 Publish 前修正。

## 二、P0：發布前必修

### P0-1　更換學術名稱

**針對文件**：

- `02_Drafts/ALE_WhitePaper_v2.5.md`
- `CITATION.cff`
- `06_Publication/ZENODO_SUBMISSION.md`
- `06_Publication/ALE_Publication_Strategy_v2.md`
- `README.md`
- `RESEARCH_LOG.md`
- `06_Publication/ALE_WhitePaper_v2.5_preview.docx`

**問題**：`Agentic Loop Engineering (ALE)` 已被 arXiv:2509.06216 在同領域正式使用。

**建議**：採用：

> From Model Consensus to Executable Evidence: An Evidence-Governed Lifecycle for Agentic Software Development

並升版為 v3.0。

### P0-2　補入直接 prior art：Code-A1

**針對文件**：

- `02_Drafts/ALE_WhitePaper_v2.5.md` §1.5、§2.6、§2.7、§7、References
- `05_DueDiligence/ALE_PriorArt_RelatedWork_v2.md`
- `05_DueDiligence/NOVELTY_AND_VALUE_ASSESSMENT.md`
- `99_References/README.md`

**問題**：2026-03-16 的 `Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning` 已直接指出：

- white-box code/test self-play 會發生 self-collusion；
- 模型可能產生 trivial tests 以獲得容易的 reward；
- 其解法是將 Code LLM 與 Test LLM 目標對立化並分離。

這比目前卷宗列入的醫療、隱寫或定價 collusion 更直接。現行「test collusion 的特化與命名是我們的」已無法原樣成立。

**修正後可守的貢獻**：

1. 將 shared-context false pass 放入完整 Agentic SDLC 治理。
2. 以多類 executable evidence 作 admission/release gate。
3. 將 evidence repository、human authority、rollback 與 skill lifecycle 整合。
4. 提出可實證的 lifecycle evaluation agenda。

### P0-3　修正 `arXiv:2512.03097` 的誤讀

**針對文件**：

- `02_Drafts/ALE_WhitePaper_v2.5.md` §2.7
- `05_DueDiligence/ALE_PriorArt_RelatedWork_v2.md`
- `99_References/README.md`
- `01_Consolidation/STORY_consolidation.md`

**現行說法**：該文「證明增加 verifier agent 擋不住 collusion」。

**原文實際結果**：該文報告未防護系統的 attack success rate 可達 100%，而其 verifier agent 將成功率壓至 0%，並將 verifier 提為 defense。

**正確用法**：

> 該文支持「多 agent 共識本身不等於安全」，但不支持「verifier 必然無效」。它反而顯示：當 verifier 連接可信外部 guidelines/database 時，可以有效抵抗 consensus pressure。

這其實可強化本文真正的方向：**verifier 的價值來自外部證據，不是來自它也是另一個模型。**

### P0-4　摘要與貢獻段仍有過強直述

**針對文件**：`02_Drafts/ALE_WhitePaper_v2.5.md`

雖然後文標為研究假說，摘要仍寫：

> multi-model cross-checking reduces variance but not systematic bias

以及：

> because LLMs are highly correlated estimators

建議改為：

> We hypothesize that shared implementation context can induce correlated false passes across code- and test-generating agents. The framework therefore privileges executable evidence over model consensus at release decisions.

貢獻第 3 點也應由「論證能力邊界」改成「提出可驗證假說與實驗協定」。

### P0-5　新增 GenAI 使用揭露

**針對文件**：

- `02_Drafts/ALE_WhitePaper_v2.5.md`
- Zenodo description
- 未來 IEEE / ACM 投稿稿

卷宗明確記載 Claude 代擬、Codex 審稿、Gemini 形式化與文字嫁接。這超過純文法編修。

新增一節：

## Generative AI Use Disclosure

> Generative AI systems were used to assist with drafting, restructuring, literature discovery, experiment-protocol refinement, and independent critique. The named human author selected the research questions, supplied the field evidence, reviewed and revised the generated material, verified citations against source documents, and accepts full responsibility for the manuscript. AI systems are not listed as authors.

未來投 IEEE 時，IEEE 要求在 acknowledgments 揭露 AI 產生的文字、圖、程式及涉及章節；ACM 也禁止將 AI 列為作者，並要求對研究生命週期中的 AI 使用作相應揭露。

### P0-6　作者與 affiliation 統一

**針對文件**：

- 主稿作者列
- `AUTHOR.md`
- `CITATION.cff`
- Zenodo metadata

建議：

- Creator：Yeh-Hsing Lu
- ORCID：0009-0006-5373-0586
- Affiliation 分成兩筆或使用 Zenodo 可驗證 affiliation。
- 不在公開 PDF 放公司街道地址。
- `AUTHOR.md` 尚有 `[請補充]`，不要隨 DOI 上傳。

### P0-7　正式 PDF 終檢

**針對文件**：`06_Publication/ALE_WhitePaper_v2.5_preview.docx`

目前只有 preview DOCX，正式 PDF 尚未產生。發布前檢查：

- Mermaid 全部轉為向量或高解析圖。
- 中文字型嵌入。
- 公式、表格、程式碼不溢出。
- 內部相對路徑不出現在公開稿。
- 無 `待核`、`待拍板`、`Working Draft 尚未達門檻` 等編輯字樣。
- DOI、版本與日期一致。
- PDF metadata title/author 與 Zenodo 完全一致。

## 三、P1：強烈建議發布前修

### P1-1　`Frozen Protocol v2` 與實際程式不符

**針對文件**：

- `04_Evidence/ALE_EXP-001_Protocol_v2.md`
- `04_Evidence/experiments/EXP-001/README.md`
- `runner/run_experiment.py`
- `runner/analyze_results.py`

Runner 仍包含：

- `call_model()` → `NotImplementedError`
- `inject_defect()` → `NotImplementedError`
- mutation / property gate 未實作
- token、時間與 hash 未記錄
- analyzer 仍標 `SKELETON`

因此狀態應改為：

> Protocol Frozen; Runner Scaffold Incomplete

不要寫「可執行協定」或「Docker runner 已備妥」。

### P1-2　EXP-001 設計需修正

- A 組要求注入 `PG reasoning`，但現在多數 API 不提供可公開且可重現的內部 reasoning；此變項不可依賴。
- Golden tests 不應宣稱「覆蓋率 100% 且能精準識別任何偏離規格」，這本身是不可達的 oracle 宣稱。
- FPR(D) ≤ 1% 不能預先當成「驗證」門檻。
- `temperature=0` 不保證 deterministic。
- 20 tasks × 2–4 defects × conditions × 3 runs 的統計單位與獨立性需先界定。

### P1-3　主實驗敘事不一致

**針對文件**：

- `README.md`
- `04_Evidence/README.md`
- `experiments/README.md`
- `ALE_WhitePaper_v2.5.md`

卷宗現稱 EXP-002 Skill Capitalization 是主實驗、EXP-001 是子實驗；但白皮書摘要、標題、novelty 與 related work 幾乎都以 shared false pass / test collusion 為核心。

投稿前需二選一：

1. **治理／驗證論文**：EXP-001 為主，Skill Capitalization 降為框架模組與未來工作。
2. **技能資產化論文**：EXP-002 為主，標題與摘要重寫，test collusion 降為一項 gate risk。

Codex 建議 DOI Working Paper 採第 1 條，因目前敘事與文獻主軸已在驗證治理。

### P1-4　成熟度 KPI 不宜放無來源的硬數字

**針對文件**：`ALE_WhitePaper_v2.5.md` §11。

例如：

- L1 任務完成率 ≥80%
- L3 逃逸缺陷率 ≤5%
- L4 重用率 ≥30%
- L5 production 事故率 ≤1%

即使標作初始政策，也容易被誤讀為成熟度模型的驗證門檻。Working Paper 建議改為 `organization-defined threshold`，將示例數值移到附錄。

### P1-5　`Validated` 狀態需要更審慎

**針對文件**：

- `EXP-002.../EVIDENCE_MAP_and_FSM.md`
- `SKILL_SUMMARY_abstract.md`

因完整 skill manifest、eval、security report 與可重現 artifact 不在研究卷宗，外部讀者無法驗證 `Validated`。公開稿應寫：

> Internally assessed as Validated under the proposed policy; not independently reproduced.

## 四、發布後版本策略

第一次 Zenodo 發布建議為：

- Version：3.0
- Type：Working Paper
- Title：採命名報告方案 A
- Description：明確寫 conceptual framework + preliminary field observation + evaluation agenda
- Files：正式 PDF、CITATION.cff、LICENSE；不附含 placeholder 的 AUTHOR.md

EXP-001 完成後用 Zenodo **New version** 發布 v3.1 或 v4.0，並用 version relation 保留演進。

## 五、DOI Publish 前機械檢查

```text
[ ] 標題全域一致
[ ] 作者／ORCID／affiliation 一致
[ ] References 無誤讀、無 placeholder
[ ] 加入 Code-A1 與直接競爭文獻
[ ] AI use disclosure 完成
[ ] PDF 逐頁檢查
[ ] PDF metadata 與 Zenodo metadata 一致
[ ] 原始碼／案例不洩漏機密
[ ] CFF 通過 validator
[ ] Zenodo draft 預覽後再 Publish
```

## 六、官方政策來源

- Zenodo record 發布與檔案不可直接修改：  
  https://help.zenodo.org/docs/deposit/about-records/
- Zenodo creator metadata：  
  https://help.zenodo.org/docs/deposit/describe-records/creators/
- DataCite DOI versioning：  
  https://support.datacite.org/docs/best-practices-for-datacite-members
- IEEE AI-generated content disclosure：  
  https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/
- ACM GenAI / authorship FAQ：  
  https://www.acm.org/publications/policies/frequently-asked-questions

