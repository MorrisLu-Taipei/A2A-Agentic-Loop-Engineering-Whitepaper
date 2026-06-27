# ALE White Paper v3.1 DOI 發布前審查

**審查者**：Codex（OpenAI）  
**文件版本**：v1.0.0_codex  
**審查日期**：2026-06-22  
**主要目標**：`06_Publication/ALE_WhitePaper_v3.1_EN.pdf`  
**同步比對**：

- `02_Drafts/ALE_WhitePaper_v3.1_EN.md`
- `02_Drafts/ALE_WhitePaper_v3.1.md`
- `04_Evidence/ALE_CaseStudy_EInvoice_v2.md`
- `CITATION.cff`
- `06_Publication/ZENODO_SUBMISSION.md`
- 根目錄 `README.md`

---

## 一、結論

### DOI 判定：NO-GO

v3.1 已具備可辨識的研究主軸，也比早期版本誠實許多；但目前仍不適合直接鑄造 Zenodo DOI。

原因不是「沒有做完所有實驗就不能發 Working Paper」。Working Paper 可以公開未完成研究，前提是版本、證據、引文與主張彼此一致。v3.1 的主要問題是：

1. **品牌名稱與學術定位自相矛盾**。
2. **版本與 metadata 不一致**。
3. **核心技術範例不能驗證它宣稱要驗證的缺陷**。
4. **4.5× 事件的現存證據不足以支持「Gate 當時攔截」的寫法**。
5. **文獻核驗狀態與 GenAI Disclosure 的聲明衝突**。
6. **PDF 呈現仍是內部草稿，不像可長期引用的正式研究物件**。

建議不要修補 v3.1 PDF；應以來源稿建立 **v3.2**，完成 P0 後重新輸出 PDF。

---

## 二、值得保留的部分

v3.1 並不是全部重來。以下研究資產值得保留：

- 「從模型共識轉向可執行證據」是清楚且有價值的主軸。
- 已主動把多數強主張降級為 `[research hypothesis]`、`[design principle]`、`[preliminary evidence]`。
- `producer != reviewer`、機械證據、模型評議、人類審證的三層結構具工程溝通力。
- Skill Capitalization 把單次交付轉成可治理資產，具有白皮書與產品方法論價值。
- 對成本、垃圾進垃圾出、LLM 版本漂移與人工瓶頸已有誠實限制說明。
- GenAI 使用揭露清楚指出人類作者負最終責任，方向正確。

問題主要在於：這些好內容被過長摘要、過多支線、版本矛盾與不可靠範例拖累。

---

## 三、P0：發布前必須修正

### P0-1｜ALE 命名必須改成「承接既有概念、提出特定框架」

#### 現況

PDF 同時出現：

- `(internal codename) ALE`
- `unrelated to "Agentic Loop Engineering"`
- `we therefore retire that name`

但目前作者決策是：**Agentic Loop Engineering 為 ALE 對外正式名稱**。

此外，arXiv:2509.06216 已在 2025 年提出並使用 `Agentic Loop Engineering (ALE)`。因此不能把相同名稱寫成 TigerAI 首創，也不能再寫成「unrelated」。

#### 建議定位

把名稱分成兩層：

- **公開框架名**：TigerAI Agentic Loop Engineering（ALE）
- **學術論文題名**：使用描述性題名，不把 ALE 名稱本身當作原創貢獻

建議首次定義：

> We operationalize Agentic Loop Engineering (ALE) as an evidence-governed, full-lifecycle framework for agentic software delivery. The term has appeared in prior Agentic Software Engineering literature; our contribution is not the term itself, but the integration of executable gates, human evidence review, rollback, and skill capitalization.

這樣既保留品牌，也不會跟 prior art 打架。

---

### P0-2｜v3.0 / v3.1 與出版 metadata 尚未同步

目前可見的不一致：

- PDF 封面寫 v3.1，但 Claim–Evidence Matrix 與結尾仍寫 v3.0。
- `CITATION.cff` 仍是 `version: "3.0"`。
- `CITATION.cff` 仍使用早期 `test collusion` 與較強的 bias 直述。
- `ZENODO_SUBMISSION.md` 仍殘留 v3.0 與 v2.5 上傳指示。
- PDF metadata 沒有 Title、Author、Subject、Keywords。
- Root / Drafts / Publication / Handoff 對 canonical version 的記錄不同。

#### 修正原則

以 v3.2 為單一發布版本，以下欄位必須完全一致：

| 欄位 | Source MD | PDF | CFF | Zenodo |
|---|---:|---:|---:|---:|
| Title | ✓ | ✓ | ✓ | ✓ |
| Author | ✓ | ✓ | ✓ | ✓ |
| ORCID | ✓ | ✓ | ✓ | ✓ |
| Version | ✓ | ✓ | ✓ | ✓ |
| Date | ✓ | ✓ | ✓ | ✓ |
| Abstract | ✓ | — | ✓ | ✓ |
| Keywords | ✓ | ✓ | ✓ | ✓ |
| License | ✓ | — | ✓ | ✓ |

PDF 重新輸出後，至少以 `pdfinfo` 與 `pdftotext` 做機械終檢。

---

### P0-3｜§7.7 的 Hypothesis 範例是無效測試

英文稿範例設定：

```python
NATIONAL_TOTAL_LIMIT = 1_000_000
max_size = 100
count <= 5_000
```

因此輸入總和最多為：

```text
100 × 5,000 = 500,000
```

測試資料不可能突破 1,000,000，上界 assertion 幾乎必定通過。此外：

- 測試沒有刻意建立重複 business key。
- `calculate_channel_invoice_count()` 沒有依 ID 去重，但 property 也沒有要求「加入重複資料後聚合值不變」。
- 這段不能證明它能抓到 pagination dedup defect。

#### 應改成的核心 property

```python
def aggregate_unique(records):
    unique = {r["id"]: r for r in records}
    return sum(r["count"] for r in unique.values())

@given(records=invoice_records())
def test_duplicate_invariance(records):
    duplicated = records + records[: max(1, len(records) // 2)]
    assert aggregate_unique(duplicated) == aggregate_unique(records)
```

再另設一條使用**獨立資料來源**計算的 national upper bound。兩條 property 不應混成一條：

1. 去重蛻變關係：重複輸入不應改變唯一鍵聚合結果。
2. 外部上界不變量：通路總量不得高於全國總量。

修正後必須實際執行，附上 fail-before / pass-after 測試結果；若無法重建舊缺陷，只能把它標示為 regression test，不可冒充歷史攔截證據。

---

### P0-4｜4.5× 事件的敘事超過現有證據

`ALE_CaseStudy_EInvoice_v2.md` 已誠實記載：

- 修復前資料快照未保留。
- 沒有真實 FAIL log。
- 現有輸出是修復後 PASS / exit 0 / 17.3%。
- 先前 AI 產生的 FAIL log 是虛構內容，已隔離。

因此下列寫法不夠精確：

- `the e-invoice upper-bound caught it`
- `mechanical gate ... actual run PASS ... see case study` 與「當時攔截」並列
- 把 17.3% PASS 當成 4.5× 缺陷曾被 Gate 捕捉的證據

#### 建議改寫

> During dashboard development, an independent Codex review identified a pagination-related duplication defect that had inflated an aggregate by approximately 4.5×. The pre-fix dataset and a contemporaneous failing gate log were not preserved; the incident is therefore reported as a retrospective field observation, not controlled evidence. A post-fix invariant check currently passes at 17.3% of the independently derived national upper bound, demonstrating the present safeguard but not proving that the gate intercepted the original defect.

Claim–Evidence Matrix 的 C1、C2、C6 應同步降級：

- C1：retrospective field observation
- C2：hypothesis，尚無 controlled comparison
- C6：post-fix safeguard demonstrated；historical interception unverified

---

### P0-5｜「所有引文已核驗」與正文狀態衝突

正文仍寫：

- `not yet exhaustively full-text verified`
- `Anthropic ... to verify`
- `Data Science Dojo ... non-arXiv`
- 多篇引用只有標題或 `et al.`，沒有完整作者、venue、年份、DOI

但 GenAI Disclosure 又宣稱人類作者已：

> verified citations against source documents

這兩句不能同時成立。

#### 修正方式

二選一：

1. 完成逐篇全文核驗、補完整 bibliography 與檢索日誌，再保留原揭露。
2. 把揭露改為「作者已核驗本文所依賴的核心引文；其餘探索性文獻仍待完整核驗」，並在 DOI 前完成全部 P0 引文。

正式 DOI 版不應保留 `to verify`、`etc.` 或不完整 reference。

---

### P0-6｜安全主張過度絕對

下列句子不宜原樣公開：

> an agent can be fooled; the pipeline cannot be changed

沒有任何 pipeline 可以合理宣稱「不能被改變」。Prompt injection、供應鏈攻擊、憑證濫用、CI 設定竄改與管理者權限都可能改變 pipeline。

建議改成：

> Individual agents may be compromised; therefore routing, policy, evidence retention, and release authority should be constrained by controls outside the producing agent's authority.

同理：

> Mechanical gates decide pass/fail.

應限縮為：

> Mechanical gates decide machine-checkable conditions; humans retain authority over ambiguous requirements, risk acceptance, and release decisions.

---

## 四、P1：內容與學術表達建議

### P1-1｜先決定它是白皮書、技術規格，還是研究論文

v3.1 同時塞入：

- 研究動機與 RQ
- related work
- 完整架構規格
- 安全威脅模型
- maturity model
- 實驗計畫
- 案例
- AI 使用揭露

結果是每一項都有提到，但核心論證沒有足夠篇幅展開。

建議拆成三個可互相引用的研究物件：

1. **ALE White Paper**：8–12 頁，講問題、故事、框架、價值、限制。
2. **ALE Technical Specification**：Agent、artifact、gate、policy、state、skill lifecycle。
3. **ALE Evaluation Protocol**：EXP-001 / EXP-002、資料、假說、指標、統計方法。

DOI 第一版可先發布 White Paper + Evaluation Protocol，不要假裝已是完整實證論文。

---

### P1-2｜摘要太長，研究問題太多

目前摘要同時處理：

- SDLC
- multi-agent
- skill capitalization
- shared-context false pass
- estimator bias
- mechanical gate
- human review
- n8n
- JSON-RPC
- data sovereignty
- prompt injection
- healthcare

讀者讀完仍不容易說出「這篇只做了哪一件事」。

建議摘要只保留：

1. 問題：agentic delivery 缺乏可信 release evidence。
2. 方法：ALE 的 full-lifecycle + evidence gate + human authority。
3. 初步材料：一項 retrospective field observation。
4. 限制：controlled experiments pending。
5. 貢獻：framework / specification / evaluation agenda。

RQ 建議從五題縮成三題：

- RQ1：共享脈絡何時造成 false pass？
- RQ2：外部證據 Gate 相對模型審查能攔下多少缺陷、成本多少？
- RQ3：治理與 Skill Capitalization 是否改善跨專案交付與稽核？

---

### P1-3｜把「人的研究洞察」放回開場

目前論文一開始像一般 Agentic SWE 框架，缺少這項研究真正有辨識度的起點：

1. 人類博士生提出研究問題。
2. AI 一天完成具 AI 分析能力的電子發票 Dashboard。
3. 成功引發「如何重複」的工程問題。
4. 4.5× 失敗引發「如何可信」的治理問題。
5. 同一套流程再被用來研究與發表 ALE。

建議 Introduction 前加入 200–300 字 `Origin and Design Trigger`。它不是行銷故事，而是 Design Science 的 problem relevance 與 artifact genesis。

---

### P1-4｜把「證據」分成三種，不要混用

建議全文固定使用：

| 類型 | 意義 | 可用語氣 |
|---|---|---|
| Retrospective field observation | 事後紀錄，證據鏈可能不完整 | motivated / observed / informed |
| Executed engineering evidence | 有程式、輸出、hash、環境 | demonstrated in the reference implementation |
| Controlled empirical result | 有 protocol、比較組與統計 | supported / validated |

目前 4.5× 事件、17.3% PASS、EXP-001 設計常被放在同一層，容易讓讀者誤認為已完成受控實驗。

---

### P1-5｜圖比更多文字重要

正式 PDF 至少需要四張可閱讀的向量圖：

1. ALE 全生命週期與 feedback loop
2. 三層驗證與權限邊界
3. Stage / Artifact / Gate / Evidence 對照
4. Skill lifecycle 與跨專案 capitalization loop

目前 Markdown Mermaid 沒有出現在 PDF，讀者只看到密集文字。這讓最重要的系統關係幾乎無法快速理解。

---

### P1-6｜章節編號與 PDF 排版需要重建

目前可見：

- 章節從 5 直接到 5.6、8.5、9.7、13.6。
- Claim–Evidence Matrix 在 PDF 中被排成一長串文字。
- 程式碼行遭截斷。
- 目錄出現在標題頁之前。
- PDF metadata 缺 Title / Author。
- 文末寫 v3.0，封面寫 v3.1。
- 字元與破折號在部分輸出中有編碼風險。

建議：

- 重編連續章節。
- 使用 Pandoc filter 或 LaTeX 原生表格處理寬表。
- 程式碼改成短行或移到 Appendix。
- 封面 → 摘要 → 目錄 → 正文。
- 產出後用 `pdftotext` 搜尋 Unicode replacement character（`U+FFFD`）、舊版本號、`to verify`、`internal codename`。

---

## 五、建議的 v3.2 學術包裝

### 建議主標題

> **From Model Consensus to Executable Evidence: A Governed Lifecycle for Agentic Software Engineering**

### 建議副標

> **The TigerAI Agentic Loop Engineering (ALE) Framework**

這個組合的好處：

- 主標題說清楚真正貢獻。
- 副標保留 ALE 品牌。
- 不把既有 `Agentic Loop Engineering` 名詞包裝成首創。
- 後續可把 Technical Specification 與 Evaluation Protocol 掛在同一 ALE 系列下。

### 建議一句話定位

> ALE is a full-lifecycle agentic software engineering framework in which producing agents cannot approve their own work, machine-checkable release conditions are decided by executable evidence, and humans retain authority over ambiguous and high-risk decisions.

### 建議貢獻縮成三項

1. **Lifecycle governance**：把 Agent、Artifact、Gate、Evidence、Rollback 串成完整 SDLC。
2. **Evidence separation**：生產、審查、機械證據與人類決策分權。
3. **Capability capitalization**：把通過驗證的專案經驗沉澱成有生命週期的 Skill。

---

## 六、建議發布包

首次 Zenodo DOI 不需要上傳整個研究卷宗。建議只放：

- `ALE_WhitePaper_v3.2_EN.pdf`
- `ALE_Evaluation_Protocol_v1.0.pdf`（若已整理完成）
- `CITATION.cff`
- `LICENSE`
- 一頁 `README_PUBLIC.md`

不要上傳：

- `AUTHOR.md` 的內部資訊
- `CURRENT_HANDOFF.md`
- Agent 操作規則
- `_QUARANTINE_DO_NOT_PUBLISH/`
- 未完成 runner 或會被誤認為已完成實驗的空殼
- 專有 Skill 清單、資料契約、token、內部路徑

Zenodo 正式發布後，metadata 可修改，但檔案與 persistent identifier 原則上是固定的；重大修改應建立新版本。因此先在 draft 預覽與機械檢查完成後再 Publish。

---

## 七、v3.2 GO Gate

以下全部完成才建議發布：

- [ ] ALE 公開名稱與 prior-art 定位一致
- [ ] 來源稿、PDF、CFF、Zenodo metadata 全部是 v3.2
- [ ] §7.7 測試能真實 fail-before / pass-after，或誠實標為 post-fix regression safeguard
- [ ] 4.5× 案例不再宣稱有未保存的即時攔截證據
- [ ] Claim–Evidence Matrix 與案例證據等級一致
- [ ] 所有 References 完整且逐篇核驗
- [ ] Disclosure 不再聲稱超過實際完成程度
- [ ] 移除安全與驗證的絕對語句
- [ ] PDF 圖、表、程式碼、章節與 metadata 通過檢查
- [ ] `pdftotext` 無 replacement character、舊版本號、placeholder、`to verify`
- [ ] 人類作者逐頁閱讀並核准

---

## 八、Codex 的直接建議

這篇真正有價值的地方不是「發明 ALE 三個字」，也不是現在就證明多模型一定會共同失敗。

真正值得發表的是：

> **一位人類研究者如何把 AI 的驚人開發速度，轉化成一套不盲信 AI、要求外部證據、能持續累積工程能力的方法。**

把論文寫回這條主線，會比目前「把所有 Agentic SWE 概念一次塞滿」更有辨識度，也更可信。

---

## 參考的一手來源

- Hassan et al., *Agentic Software Engineering: Foundational Pillars and a Research Roadmap*, arXiv:2509.06216：  
  https://arxiv.org/abs/2509.06216
- Zenodo, *About records*：  
  https://help.zenodo.org/docs/deposit/about-records/
- Zenodo, *Manage versions*：  
  https://help.zenodo.org/docs/deposit/manage-versions/
- Zenodo, *Reserve a DOI*：  
  https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/

---

*本審查不修改或覆寫 v3.1 PDF；建議以 v3.2 新版本修訂，保留 v3.1 作為研究演進證據。*
