# 08 · Methodology（本研究的生產方法論:3×AI 協助人類寫論文)

**性質**:說明「這篇論文/這個研究**是怎麼被生產出來的**」——一套**多 AI 引擎 + 人類最終權威**的學術論文生產方法論。
**雙重定位(本卷宗採「先 a 後 b」)**:
- **(a) 本卷宗的方法論說明 + GenAI 使用揭露**(服務 Codex P0-5;論文放短版指向此)。
- **(b) 第二篇論文的種子**:可抽成獨立 Design Science 投稿,**延伸**作者前作、以 ALE 專案為 worked case。
**自我引用(直系前作)**:Lu, Y.-H. (2026). *AI-Native eBook Production: Multi-IDE Orchestration as Methodology Engineering Infrastructure — A Design Science Investigation.* Zenodo. **DOI 10.5281/zenodo.20264772**。本方法論是該「Multi-IDE Orchestration」研究線在**學術論文生產**上的延伸應用。

> 一句話:**用多個獨立 AI 引擎互相對抗審查、由人類查核證據並負最終責任,來生產可稽核、可重現的學術論文**——與 ALE 框架(機械閘/模型評議/人類審證據)同構。

---

## 🤖 給 AI Agent 的入口（A2A)
若你是被指派「接手這條研究/論文生產線」的自主 agent：

1. 先讀 [`AGENTS.md`](AGENTS.md)。
2. 讀 [`CURRENT_HANDOFF.md`](CURRENT_HANDOFF.md) 恢復現況。
3. 若你是 Codex，再讀 [`CODEX_OPERATING_GUIDE.md`](CODEX_OPERATING_GUIDE.md)。
4. 需要 schema / protocol 時再載入 [`A2A_SKILLSET.md`](A2A_SKILLSET.md)。

沒有 A2A HTTP server 時採 **Local Workspace Adapter**，不得假裝呼叫成功。
- 合約/Schema/Gate 述詞:`A2A_SKILLSET.md` §2–§5｜呼叫協定(JSON-RPC):§4｜照抄的執行 trace:§6｜違反即中止的紅線:§7。
- 落地編排:`N8N_ORCHESTRATION.md`(每個 A2A method 對應一組 n8n 節點)。

---

## 0. 本目錄文件導覽

| 檔案 | 是什麼 | 給誰看 |
|---|---|---|
| `README.md`(本檔) | 方法論定位 + GenAI 使用揭露 + 角色分工 | 全部 |
| `AGENTS.md` | 自主 Agent 的通用任務、紅線、Router 與 Gate | 所有 Agent |
| `CURRENT_HANDOFF.md` | canonical 文件、Gate、open items、最近交接 | 所有接手 Agent |
| `CODEX_OPERATING_GUIDE.md` | Codex 本地工作區 adapter、檔名、寫入與交棒規則 | 下一個 Codex |
| `PROCESS_FLOWCHART.md` | **#1 文字流程圖**(ASCII + mermaid + 真實事件對照) | 想懂流程 |
| `STORY_how_to_use.md` | **#2 故事**:怎麼用這套方法寫論文(含最小 SOP) | 第一次用的人 |
| `A2A_SKILLSET.md` | **#3 A2A 技能集**:每階段+gate 做成 agent 可呼叫 skill | 下一個 AI agent |
| `N8N_ORCHESTRATION.md` | **#4 n8n 編排(教學級)**:可匯入 workflow + 逐步 lab | 實作者/學生 |
| `COURSE_SYLLABUS.md` | **上課課綱 + 該做哪些 n8n workflow** 清單(8/16 週) | 授課老師 |
| `figures/methodology_flow.svg` | 方法論流程圖(向量) | 投影片/論文 |
| `figures/n8n_topology.svg` | n8n 拓樸圖(向量) | 投影片/教學 |

---

## 1. 研究框架:Design Science(延續前作)

沿用前作的 **Design Science Investigation**(對齊 Hevner 七準則):
- **問題**:LLM 時代,單人單引擎的論文生產易有盲點(過度宣稱、誤讀文獻、漏 prior art),且不可稽核。
- **Artifact**:一套 **3×AI + 人類** 的論文生產流程(角色分工 + stage-gate + 對抗式審查)。
- **評估**:以本 ALE 專案為 **worked case**,觀察方法論是否真能攔下錯誤、提升可稽核性(見 §4 證據)。

承前作四特性,本方法論聚焦其中兩項並落地到論文:**多引擎對抗式審查(multi-engine adversarial review)** 與 **可重現衍生(Git + 宣告式流程 + DOI)**。

---

## 2. 角色分工(3×AI + 人類)

| 角色 | 引擎 | 職責 | 對應 ALE |
|---|---|---|---|
| **Founder / 作者** | 人類(Morris) | 定研究問題、供田野證據、最終決策、**負全責** | Human authority |
| **操作化 + 整合 + 查核** | Claude | 把洞見寫成文件、整合各方、**查核 AI 產出**、維護版本與結構 | Orchestrator + 生產 |
| **對抗式審查** | Codex | 預設為獨立 Reviewer + 原始來源查證；使用者要求時可實作修改，但該修改仍需另一實例獨立審查 | **Reviewer / Local Workspace Adapter** |
| **形式化 + 潤稿** | Gemini | 統計形式化、補程式範例、文獻補齊、措辭校準 | 補強 |

> 鐵則(= ALE §5.3 / §7):**生產者 ≠ 審查者**;審查發現的問題以**讀原文/真實執行**裁決,不以「哪個 AI 講得漂亮」。

---

## 3. 流程(= 本卷宗的 stage-gate)

```text
人類洞見 → Claude 操作化(00→02) → Codex/Gemini 審查(03) →
證據實驗(04) → 盡職調查(05) → 發表(06) → 回顧/教訓(07) ↺
```
每關有 gate(No evidence, no release 等);審閱(03)與文獻(99)、教訓(07)橫貫回饋。**這份方法論(08)就是對「上面這條線怎麼運作」的反身描述。**

---

## 4. 證據:方法論「真的有效」的 worked case

本 ALE 專案中,**獨立對抗式審查(Codex)+ 讀原文查核**實際攔下了**人類+主力 AI 一起犯的三個錯**(見 `07_Lessons_Learned`):
1. **誤讀** arXiv:2512.03097(把結論講反)→ 讀 PDF 原文糾正。
2. **撞名**:漏看 arXiv:2509.06216 已定義 ALE → 改名。
3. **漏 prior art**:arXiv:2603.15611(Code-A1)已提 self-collusion → 補引、降級宣稱。

> 這是方法論價值的**直接證據**:單一 AI(含主力)會自信地錯;**多引擎對抗 + 人類查核**才擋得住。對應 ALE 的核心主張——**證據優於共識**。

也記錄**失敗模式**:Gemini 曾產**虛構稽核日誌**(`07` L4)→ 證明「AI 產出必須查核」是方法論的必要關卡,不是裝飾。

---

## 5. Generative AI Use Disclosure（可直接放進論文)

> **Generative AI Use Disclosure.** Generative AI systems were used to assist with drafting, restructuring, literature discovery, statistical formalization, experiment-protocol design, and independent adversarial critique. Specifically: Claude (operationalization, integration, verification, version control), Codex (independent adversarial review, prior-art and consistency checking, experiment design), and Gemini (formalization, code examples, copy-editing). The named human author (Yeh-Hsing Lu) selected the research questions, supplied the field evidence, reviewed and revised all generated material, **verified citations against source documents**, and accepts full responsibility for the manuscript. AI systems are **not** listed as authors. This disclosure aligns with IEEE/ACM policies on AI-generated content.

中文摘要:本研究在起草、重構、文獻檢索、形式化、實驗設計與**獨立對抗式審查**上使用生成式 AI(Claude / Codex / Gemini 分工如 §2);**研究問題、田野證據、引文查核與最終責任由人類作者承擔,AI 不列為作者。**

---

## 6. 抽成第二篇論文時的 to-do(定位 b)
- 標題候選:*Three-Engine Adversarial Authorship: A Design-Science Method for AI-Assisted Academic Writing*(延伸 20264772)。
- 以 ALE 專案為案例,量化:對抗審查攔錯率、人類查核工時、可重現性。
- 對齊 Hevner 七準則;self-cite 20264772 + 本卷宗。
- 走自己的 stage-gate(這次方法論可遞迴套用於方法論論文本身)。

---
*本檔同時是 GenAI 使用揭露來源(論文放短版指向此)與第二篇論文種子。前作:DOI 10.5281/zenodo.20264772。*
