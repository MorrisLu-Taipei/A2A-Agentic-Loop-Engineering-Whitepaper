# ALE 原創性與非抄襲聲明（Originality & Non-Plagiarism Statement）

**作者 / Author**：Morris（虎智科技 TigerAI Tech Co., Ltd.）
**文件類型 / Type**：Originality Statement（發表前查核紀錄,可隨白皮書 / Zenodo 一併公開）
**版本 / Version**：v1
**查核日期 / Date of check**：2026-06-21
**對應作品**：`ALE_WhitePaper_v2.3.md`（*System Development Agentic Loop Engineering, ALE*）
**完整盡職調查**：見 `ALE_PriorArt_RelatedWork_v1.md`

> ⚠️ **更正聲明(早期版本)**:本檔所列相鄰研究中,`arXiv:2512.03097` 的正確結論是「verifier 錨定外部 guidelines 時可有效防禦共謀」(勿誤述為「無效」),且 `arXiv:2603.20281` 屬主題誤植(已於 PriorArt 移除)。正確內容以 `ALE_Originality_Statement_v2.md` / `ALE_PriorArt_RelatedWork_v2.md` 為準。

> 本聲明為公開可查的原創性紀錄。任何對 ALE 是否抄襲特定來源有疑慮者,可依本文所列之查核範圍、方法與結論逕行複驗。

---

## 1. 聲明（Statement）

虎智科技就 **System Development Agentic Loop Engineering (ALE)** 白皮書之原創性聲明如下:

> 本作品之核心構念——**測試共謀(test collusion)**、**機械閘優先於模型共識(mechanical gate over model consensus)**、**相關估計器/條件協方差論證(correlated estimators)**、**技能資產化與有限狀態機治理(skill capitalization & FSM lifecycle)**、**需求不變量防禦(spec invariants)**、以及**機械閘/模型評議/人類審證據三層驗證架構**——均為作者獨立提出與整合,**未抄襲、未改寫任何特定第三方來源**。對於與既有公共術語或文獻重疊之處(如 agent loop、guardrails、多代理人 collusion),本作品已於 Related Work 明確引用並標示界線(見 §3)。

---

## 2. 針對性查核：`github.com/agenticloops-ai/agentic-ai-engineering`

因該 repo 名稱含「agentic」「loop」字樣,與本作品標題有表面相似,特此逐項查核並記錄結論。

**查核方法**:擷取該 repo README 與目錄結構,逐一比對本作品全部核心術語與主張。

**比對結果**:

| 比較面向 | 該 repo | ALE | 是否重疊 |
|---|---|---|---|
| 體裁 | 動手教學集(tutorials) | 框架研究白皮書 | 否 |
| 授權 | MIT | （本作品擬 CC BY 4.0） | — |
| 解決的問題 | 如何**建造** agent(LLM API、tool calling、agent loop、RAG) | 如何**治理與驗證** agent 產出的軟體 | 否 |
| test collusion | 無 | 核心 | 否 |
| mechanical gate | 無 | 核心 | 否 |
| correlated estimators | 無 | 核心 | 否 |
| skill capitalization / repository | 無 | 核心 | 否 |
| anti-self-deception governance | 無 | 核心 | 否 |
| SDLC / evidence repository / FSM 技能治理 | 無 | 核心 | 否 |
| 文字重用 | 無 | — | 否 |

**結論**:**無抄襲、無實質相似、無文字重用。** 兩者為不同物種——該 repo 教「生成能力」,ALE 處理「生成之後的治理與可驗證性」。名稱中「agentic」「loop」屬該領域通用詞彙之巧合,非實質相似。

---

## 3. 與既有公共術語/文獻之界線（已於 Related Work 揭露）

本作品**不主張**下列為原創,並已就地引用:

- **「Loop Engineering / Agentic Loop」** 為 2026 既有通用術語(Data Science Dojo 2026、Kilo、MindStudio 等);本作品採納其迴圈控制實務(guardrails、circuit breaker、budget cap、termination),貢獻在其**治理與反自我欺騙驗證層**,非迴圈本身。
- **多代理人 collusion** 為既有研究議題(arXiv:2512.03097、2510.04303、2512.02682;⚠ 原列 2603.20281 為主題誤植已移除);本作品引用之,並將其**特化**為軟體驗證關卡之 *test collusion*,以**機械事實基準**為解方。注:2512.03097 之正確結論為「verifier 錨定外部基準可有效防禦」,本作品「單靠多加同質 AI 可能無效」係以相關估計器提出之**研究假說**,非引該文為證。
- **突變測試、性質導向測試、集成學習** 等基礎方法均引用原始文獻(DeMillo 1978、Claessen & Hughes 2000、Dietterich 2000 等)。

> 原則:**共享之處明確引用、原創之處清楚標界**。本作品避免兩種學術失當——「佯裝前人不存在」與「將前人成果據為己有」。

---

## 4. 原創性之佐證（時間與演進證據）

- **版本沿革**:v1.1 → v1.2 → v2.0 → v2.1 → v2.3,逐版可追溯之內部演進紀錄(repo 內保留各版檔案)。
- **實證案例**:`ALE_CaseStudy_EInvoice_v1.md`,以先於框架成文之真實專案反向印證,非事後杜撰。
- **公開時間戳(規劃中)**:擬上 arXiv `cs.SE` 與 Zenodo(DOI)以建立公開優先權。

---

## 5. 複驗指引（供第三方）

任何人欲複驗本聲明,可:
1. 取 ALE 白皮書全部核心術語清單(§2 表左欄)。
2. 對任一疑似來源之全文做關鍵詞比對。
3. 檢視本 repo 之版本沿革檔案與案例研究證據鏈。

---

*本聲明由虎智科技 TigerAI 出具,作為 ALE 發表前盡職調查之公開紀錄。— 2026-06-21*
