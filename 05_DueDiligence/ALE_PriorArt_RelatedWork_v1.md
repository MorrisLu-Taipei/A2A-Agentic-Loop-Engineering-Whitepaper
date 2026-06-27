# ALE 發表前置：抄襲查核、先前技術（Prior Art）與文獻對比

**作者 / Author**：Morris（虎智科技 TigerAI）
**文件類型 / Type**：投稿/DOI 前置盡職調查（novelty & non-plagiarism due diligence）
**版本 / Version**：v1
**日期 / Date**：2026-06-21
**對應**：`ALE_WhitePaper_v2.3.md`

> 目的:在為 ALE 申請 DOI / 投稿前,(1) 釐清是否有抄襲特定來源之虞;(2) 盤點先前技術與相鄰文獻;(3) 重新界定**可辯護的新穎性**;(4) 給出可直接套用的對比方法與引用清單。

> ⚠️ **更正聲明(本檔為早期 v1,已被 v2 取代)**:本 v1 含**兩處已更正的引用錯誤**——(a) 將 `arXiv:2512.03097` 結論**講反**(原文:verifier 錨定外部 guidelines 時可有效防禦;v1 誤述為「擋不住」);(b) 將 `arXiv:2603.20281` 誤植為共謀相關文獻(其實為演算法定價/反托拉斯經濟學,主題不符)。**正確內容請以 `ALE_PriorArt_RelatedWork_v2.md` 為準。** 下文已就地標註/更正,本檔保留作版本歷史。

---

## 1. 抄襲查核結論（針對 `github.com/agenticloops-ai/agentic-ai-engineering`）

**結論:無抄襲、無改寫之虞。**

| 比較面向 | 該 repo | ALE |
|---|---|---|
| 體裁 | 動手教學集(tutorials, MIT) | 框架研究白皮書 |
| 主題 | 如何「建造」agent(LLM API、tool calling、agent loop、RAG、guardrails) | 如何「治理與驗證」agent 產出的軟體(SDLC + 反共謀) |
| 核心術語 | agent loop、ReAct、prompt chaining、"Ralph Mode" | test collusion、mechanical gate、correlated estimators、skill capitalization、anti-self-deception |
| 概念重疊 | **0**(已逐項確認:該 README 不含我們任何核心詞) | — |
| 文字重用 | 無 | — |

> 兩者連「要解的問題」都不同:它教**生成能力**,我們處理**生成之後的治理與可驗證性**。即使名稱有「agentic」「loop」字樣,屬通用詞彙巧合,非實質相似。

---

## 2. 真正的風險:不是抄襲,是「新穎性」與「未引文獻」

### 風險 A — 名稱新穎性不足（嚴重度:中）

「**Loop Engineering / Agentic Loop**」在 2026 已是通用術語,非我們原創:

- Data Science Dojo, *Agentic Loops: From ReAct to Loop Engineering (2026 Guide)*(2026-06-09):定義 loop engineering 為「designing, specifying, and maintaining agentic loops」,並列 guardrails(iteration caps、budget limits、circuit breakers、termination criteria、human checkpoints)。
- Kilo、MindStudio 各有 "What is Loop Engineering" 專文;`agenticloops.ai` 為一品牌站。
- LangChain blog、arXiv 2509.06216 等以 "Agentic (Software) Engineering" 為題。

**影響**:
1. 我們的標題 *Agentic Loop Engineering* 處於擁擠地段,審稿人會問「與既有 loop engineering 差異?」。
2. 上述 guardrails 清單(circuit breaker、budget cap、termination)**與 ALE §7.6 高度重疊**,若不引用會顯得我們「重新發明且不知前人」。

**好消息**:無人使用「Agentic Loop Engineering = **ALE**」這個縮寫,且無人以「可治理 / 可稽核 / 可沉澱 / 技能資產化 / 反自我欺騙」界定它。我們的**差異化空間在治理與驗證,不在 loop 本身**。

### 風險 B — 「test collusion」有鄰近文獻,未引即破綻（嚴重度:高）

多代理人 collusion 是 2025–2026 活躍研究領域:

- **arXiv:2512.03097** *Many-to-One Adversarial Consensus: Exposing Multi-Agent Collusion Risks in AI-Based Healthcare* —— 展示多代理人**對抗式共識的共謀風險確實存在**;其關鍵發現是 verifier **錨定外部 guidelines** 時可將攻擊成功率降至 0%(**有效防禦**)。**正確引用方向**:此文支持 ALE「驗證須錨定**模型以外的外部基準**(對 ALE 即機械事實基準:突變/覆蓋率/性質測試/需求不變量)」之取向。〔⚠ v1 原句誤述為「加 verifier 擋不住」,與原文相反,已更正。〕
- ~~**arXiv:2603.20281**~~ —— ⚠ **已移除:該編號實為演算法定價/反托拉斯經濟學論文,與軟體驗證共謀無關(主題誤植),不列為相關前案。**
- **arXiv:2510.04303** *Audit the Whisper: Detecting Steganographic Collusion in Multi-Agent LLMs* —— 隱寫式共謀偵測。
- **arXiv:2512.02682** *Beyond Single-Agent Safety: A Taxonomy of Risks in LLM-to-LLM Interactions* —— LLM 互動風險分類。
- **arXiv:2509.06216** *Agentic Software Engineering: Foundational Pillars and a Research Roadmap* —— 最該對位的「agentic SWE」研究路線圖。

**影響**:這些文獻證明「多代理人 collusion」已是公認議題,且 2512.03097 指出「**verifier 須錨定外部基準**才有效」(⚠ 非「verifier 不足」)。ALE 若不引用,會被質疑「無視同領域成果」;若引用得當,反而**借力**——把 ALE 定位為該議題在 **SDLC 驗證關卡**的特化解(以機械事實基準為外部錨)。

---

## 3. 重新界定「可辯護的新穎性」（Defensible Novelty）

把貢獻收斂到**別人沒有、且我們能守住**的三點;明確讓出已是公共財的部分:

| 主張 | 是否新穎 | 處置 |
|---|---|---|
| Agent 跑 loop / plan-act-observe | ❌ 公共財(loop engineering) | 引用,不主張原創 |
| guardrails:budget / circuit breaker / termination | ❌ 公共財 | §7.6 引用 DS Dojo 等,定位為「採納既有實務」 |
| 多代理人 collusion 存在 | ❌ 已有文獻 | 引用 2512.03097 等 |
| 「verifier **錨定外部基準**可有效防禦 collusion」(2512.03097, healthcare) | ⚠️ 已有 | 〔⚠ v1 原列為「verifier 不足以擋 collusion」係**講反原文**,已更正〕正確:該文 verifier 接外部指南即壓制共謀;我們的「單靠多加同質 AI 可能無效」是以 correlated estimators / Cov→1 提出之**研究假說**(非引該文為證) |
| **把 collusion 特化到 PG↔V&V「從實作生成測試」的關係(= test collusion)** | ✅ 我們的 | 主張之一 |
| **以機械閘(突變/覆蓋/性質/需求不變量)取代「再加 AI」作為定生死基準** | ✅ 我們的 | 主張之二(核心) |
| **Skill Capitalization + FSM 生命週期治理 + 去退化演算法** | ✅ 我們的 | 主張之三 |
| **三層:機械閘定生死 / 模型評議找分歧 / 人類審證據** | ✅ 我們的整合 | 統合性貢獻 |

> 一句話定位:**「別人問『agent 怎麼跑得好』;我們問『當驗證 agent 的也是 agent 時,如何不自我欺騙』——並用機械事實、而非更多 AI,來回答。」**

### 名稱選項(待 Founder 決策)
- **選項 1(建議):保留 ALE,但副標突顯差異**,並在 §1.5 Novelty + §2 Related Work **明寫**「loop engineering 已是既有術語,本文貢獻在其**治理與反自我欺騙驗證**層」。主打詞改以「**Anti-Self-Deception Governance**」為記憶點(這詞無人用)。
- **選項 2:換主名**,如「*Verifiable Agentic SDLC (VA-SDLC)*」或「*Anti-Self-Deception Software Factory*」,把「loop」降為內文用語,徹底避開擁擠地段。
- **選項 3:保留 ALE 全稱但重新展開縮寫**,強調 *System Development* 前綴與既有 loop engineering 區隔。

---

## 4. 「怎麼對比參考與文獻研究」——可操作方法（SOP）

### 步驟 1：先前技術檢索（prior-art search）
對每個核心主張各跑一輪檢索,關鍵詞配對:
- `"agentic" + ("software engineering" | "SDLC")`
- `"loop engineering" | "agent loop"`
- `LLM "collusion" | "self-preference" | "LLM-as-judge"`
- `"mutation testing" + LLM | agent`
- `multi-agent verification | verifier agent`
記錄:出處、年份、定義原文、與我方主張的關係(支持/中立/競爭)。

### 步驟 2：建對比矩陣（differentiation matrix）
每篇相鄰工作一列,欄位:`解什麼問題 / 方法 / 是否處理「驗證者也是 AI」/ 是否用機械事實基準 / 是否談 skill 資產化`。一眼看出 ALE 的空位。

### 步驟 3：把對比寫成 Related Work（見 §5 可直接貼)
原則:**先承認共享(讓出公共財)→ 再標出我們補的洞**。避免「假裝前人不存在」與「把前人說成錯的」兩種審稿地雷。

### 步驟 4：引用紀律
- 凡與既有術語/實務重疊處(loop、guardrail、collusion),**就地引用**。
- 「支持我方」與「我方原創」分開講;不把支持證據冒充原創。
- 投稿前核對每條引文的確切出版資訊(arXiv 編號、年份、版本)。

### 步驟 5：DOI / 預印本流程
- 先上預印本(arXiv / Zenodo 取 DOI)建立**時間戳優先權**;Zenodo 可立即發 DOI 給白皮書。
- 釋出時附 `LICENSE`(建議 CC BY 4.0 給文件)、`CITATION.cff`、版本號;與既有 GitHub 系列(顧問方法論)一致命名。
- 保留 v2.0/v2.1/v2.3 沿革作為**原創性與演進證據**。

---

## 5. 可直接貼進白皮書的 Related Work 增補（草稿）

> 置於 §2.6 之後,新增 §2.7。

### 2.7 Loop Engineering、Agentic SWE 與多代理人共謀（與本文之區別）

近期實務社群將「**loop engineering**」界定為設計與維護 agent 的 plan–act–observe 迴圈,並以 guardrails(iteration cap、budget limit、circuit breaker、termination、human checkpoint)控制其行為 [Data Science Dojo 2026; Kilo 2026; MindStudio 2026]。學術側,[arXiv 2509.06216] 提出 agentic software engineering 的基礎支柱與研究路線。ALE **採納**上述迴圈控制實務(見 §7.6),但其貢獻**不在迴圈本身**,而在迴圈**產出之治理與可驗證性**——尤其是當驗證階段亦由 agent 執行時的可信度問題。

在多代理人安全方面,既有研究顯示 LLM 之間可發生共謀:adversarial consensus 之共謀風險存在、且 verifier 錨定外部 guidelines 時可有效防禦 [arXiv 2512.03097]、可經隱寫通道進行 [arXiv 2510.04303],並已被納入 LLM-to-LLM 風險分類 [arXiv 2512.02682]。值得注意的是,[arXiv 2512.03097] 指出**將 verifier 錨定到外部 guidelines 可有效防禦共謀**——這正支持本文 §7.2「驗證須錨定模型以外的機械事實基準」之取向(⚠ v1 原句曾誤述為「加 verifier 不足以阻止共謀」,與原文相反,已更正)。本文「為何單靠多加同質 AI 可能無效」是以**相關估計器**提出的**研究假說**,非援引此文為證。本文的區別在於:(1) 我們將共謀**特化**到軟體驗證關卡中「PG agent 產碼、V&V agent 由實作生成測試」的關係,命名為 **test collusion**;(2) 我們以**統計論證**(相關估計器、條件協方差趨近 1)解釋「為何加 AI 無效」;(3) 我們提出的解方**不是再加一個 agent,而是不問模型意見的機械事實基準**(突變測試、覆蓋率、性質測試、需求不變量),並輔以技能資產化治理。據我們所知,將「test collusion + 機械閘優先」整合進完整 Agentic SDLC 的框架,尚未見於既有文獻。

---

## 6. 待補引用（References 增補，投稿前核對確切資訊）

- Data Science Dojo (2026). *Agentic Loops: From ReAct to Loop Engineering (2026 Guide).* (blog, 2026-06-09)
- arXiv:2509.06216. *Agentic Software Engineering: Foundational Pillars and a Research Roadmap.*
- arXiv:2512.03097. *Many-to-One Adversarial Consensus: Exposing Multi-Agent Collusion Risks in AI-Based Healthcare.* 〔正確結論:verifier 錨定外部 guidelines 可有效防禦;勿誤述為「無效」。〕
- ~~arXiv:2603.20281~~ 〔已移除:主題誤植,非共謀相關文獻。〕
- arXiv:2510.04303. *Audit the Whisper: Detecting Steganographic Collusion in Multi-Agent LLMs.*
- arXiv:2512.02682. *Beyond Single-Agent Safety: A Taxonomy of Risks in LLM-to-LLM Interactions.*
- （另補）LLM-as-judge self-preference / position / verbosity bias 之代表作（支援 §7.2）。

---

## 7. 行動清單（投 DOI 前）

1. **名稱決策**(§3 三選項)——Founder 拍板。
2. 把 §5 的 **§2.7 Related Work** 併入白皮書,出 **v2.4**(保留 v2.3)。
3. §7.6 guardrails 段落**就地引用** loop engineering 來源,聲明採納既有實務。
4. §7.2 加註:引 arXiv:2512.03097——其「verifier 錨定外部基準可防禦」之發現,支持 ALE「驗證錨定模型以外的機械基準」取向(⚠ 勿誤述為「加 verifier 無效」)。
5. 核對所有 arXiv 編號與年份(本檔部分日期係抓取時推得,**投稿前務必逐筆驗證**)。
6. 上 Zenodo 取 DOI + 附 `CITATION.cff` / `LICENSE(CC BY 4.0)`。

---

*— End of Prior-Art & Related-Work Due Diligence v1 —*
