# 08 · 課綱 + 該做哪些 n8n Workflow（大學授課建議)

> 給 Morris 去大學教這套「3×AI + 人類 寫論文 / 治理 AI 軟體交付」方法論用。
> 配套教材:`PROCESS_FLOWCHART.md`(流程)、`A2A_SKILLSET.md`(技能)、`N8N_ORCHESTRATION.md`(實作 + 最小可匯入 workflow)、白皮書 `../02_Drafts/ALE_WhitePaper_v3.0.md`、踩坑 `../07_Lessons_Learned/`。

---

## A. 課程定位

| 項目 | 內容 |
|---|---|
| 課名(建議) | **以可執行證據治理 AI 軟體開發:Agentic 工程與 n8n 實作** |
| 對象 | 資工/資管大三~碩一;或在職專班 |
| 先備 | Python 基礎、Git、會用瀏覽器;**不需**先會 n8n(課程內教) |
| 形式 | 每週 講 1/3 + 動手 2/3;全程 Docker;**無 API key 也能上**(用 stub) |
| 學分/週數 | 可裁成 **8 週短課**或 **16 週正式課**(下方給 8 週主幹 + 加深選項) |
| 核心理念 | **生產者≠審查者 · 證據>共識 · 過關才往下 · 人類負最終責任** |

**修課後能力(CLO)**
1. 設計帶 gate 的 Agentic 流程,辨識並防止「AI 驗 AI 的自我背書」。
2. 用 n8n 做出 State→Router→Gate、對抗審查迴圈、人類核可的可稽核流程。
3. 用 stage-gate 把一個真實題目推進到**預印本 DOI**(誠實標證據等級)。
4. 做先前技術查核、引文查證、GenAI 使用揭露(學術誠信)。

---

## B. 8 週主幹課綱（每週對應一個要做的 n8n workflow)

| 週 | 主題 | 讀本 | **動手做的 n8n workflow(WF)** | Gate 概念 |
|---|---|---|---|---|
| W1 | 為什麼「AI 驗 AI」會崩:同源假通過 | 白皮書 §1、§7.1;`07` L1 | **WF-1 Hello-State**:Manual→Init State→Router→看狀態流轉 | 認識 State Object |
| W2 | stage-gate:過關才往下 | 白皮書 §4、§7.4;`PROCESS_FLOWCHART` | **WF-2 Gate-Demo**(=最小 workflow):IF gate pass/fail 回 Router | No gate, no proceed |
| W3 | 生產者≠審查者:對抗式審查 | 白皮書 §5.3、§7.2;`A2A_SKILLSET` | **WF-3 Review-Loop**:平行 HTTP 呼 producer/reviewer/enhancer | 多引擎獨立審 |
| W4 | ★ 不盲信 AI:查原始來源 | `07` L1/L4;白皮書 §7.3 | **WF-4 Verify**:finding→HTTP 抓 arXiv/PDF + Execute 跑程式比對 | 證據>共識 |
| W5 | 機械閘:突變/覆蓋/不變量 | 白皮書 §7.3、§7.7 | **WF-5 Mechanical-Gate**:Execute 跑 pytest/mutation→IF 門檻 | 機械事實定生死 |
| W6 | 人類關卡 + 安全/權限 | 白皮書 §5.6、§8、§8.7 | **WF-6 Human-Approval**:Wait/Form 核可 + 權限 stub | 高風險須人核 |
| W7 | 先前技術 / 引文查證 / 誠信 | `05_DueDiligence`;`07` L2/L3/L6 | **WF-7 PriorArt**:HTTP→arXiv API 核驗書目→產矩陣 | No verified citation, no submit |
| W8 | 發表:預印本 DOI(誠實) | `06_Publication`;`DOI_GUIDE` | **WF-8 Publish**:組 metadata + (Zenodo sandbox)取 DOI | metadata 一致 + 人核 |

> **期末 capstone**:把 WF-1~8 串成一條完整 pipeline(Hub-and-Spoke),拿學生自己的小題目跑到「預印本就緒」。

**16 週版加深**:每主題各加一週做(W*a 概念 + W*b 實作/除錯),並加:Skill Capitalization 與 FSM(白皮書 §5.5/§6)、成本工程(§9.6)、供應鏈安全(§8.5)、實驗設計 EXP-001(`04_Evidence`)、寫一篇真的投 IEEE Software 短文。

---

## C. 該做哪些 n8n Workflow(建議清單,由淺到深)

> 全部可從 `N8N_ORCHESTRATION.md` 的「最小可匯入 workflow」長出來;**先 stub 跑通,再換真端點**。

**Tier 0 · 骨架(W1–W2)**
- **WF-1 Hello-State** — Manual Trigger → Code(Init State)→ Code(Router)→ 看 `state`。學:狀態驅動。
- **WF-2 Gate-Demo** — 加 IF gate(open_findings==0?)→ pass/fail 兩條線回 Router。學:stage-gate。

**Tier 1 · 核心價值(W3–W5)**
- **WF-3 Review-Loop** — 平行 HTTP Request 呼 producer/reviewer/enhancer(三個 MODEL_* )→ Merge。學:生產者≠審查者。
- **WF-4 Verify** — Switch(finding 類型)→ HTTP 抓 arXiv/PDF 或 Execute Command 跑程式 → 標 verified/rejected。學:**證據>共識**(整套靈魂)。
- **WF-5 Mechanical-Gate** — Execute Command 在容器跑 `pytest --cov` / `mutmut` → 解析輸出 → IF(coverage≥85% & mutation≥0.75)。學:機械閘。

**Tier 2 · 治理與發表(W6–W8)**
- **WF-6 Human-Approval** — Wait(Form/Webhook)→ 人按核可才繼續;否則凍結。學:human-in-the-loop。
- **WF-7 PriorArt-Verify** — HTTP → `export.arxiv.org/api/query` 核驗每筆書目(編號↔題名↔日期)→ 產對比矩陣。學:引文查證(直接對應我們踩過的誤讀/撞名坑)。
- **WF-8 Publish-Preprint** — Set 組 Zenodo metadata + (sandbox.zenodo.org)建 draft → 回填 DOI。學:誠實發表。

**Tier 3 · 整合(capstone)**
- **WF-9 Full-Pipeline** — 用主 Router 把 WF-2~8 當子流程串起來(Execute Sub-workflow 節點),單一 State Object 貫穿、斷點續傳。
- **WF-10 Kaizen-Dashboard**(選) — 收集各節點 execution 的延遲/重試/gate 失敗率 → 寫 Postgres → 簡單儀表板。學:元迴圈(白皮書 §9.5)。

> 教學小抄:**每個 WF 都先給 stub 版(零金鑰可跑)**,作業是「把某個 stub 換成真的」——降低門檻又有成就感。

---

## D. 課堂必教的三個真實踩坑(我們親身)
1. schedule trigger 不能被 CLI execute → smoke 用 manual-trigger 變體。
2. healthcheck 用 `127.0.0.1`(不要 localhost,IPv6 假性 unhealthy)。
3. 匯入憑證/工作流 JSON 必帶顯式 `id`。
> 外加學術面三坑:誤讀文獻(讀原文!)、撞名(讀正文非摘要)、AI 造假證據(查證)。

---

## E. 評量設計

| 項目 | 佔比 | 說明 |
|---|---|---|
| 週實作(WF-1~8) | 40% | 每週交可跑的 workflow(stub 即可) |
| 期中:Review-Loop + Verify | 20% | 能展示「對抗審查 + 查原始來源」 |
| 期末 capstone | 30% | 自選題目跑到「預印本就緒」+ 誠實的證據等級標註 |
| 學術誠信 | 10% | GenAI 使用揭露、引文查證、prior-art 矩陣 |

**capstone rubric**:State 流轉正確 25% · Gate 邏輯 25% · 對抗審查含查證 25% · 誠實邊界(stub/人核/證據等級) 25%。

---

## F. 一句話教學定位
> 這門課不教「怎麼叫 AI 寫東西」,教**「怎麼讓多個 AI 互相把關、人類查證,做出敢具名、可稽核、不會自信地出錯的成果」**——用 n8n 把這套紀律變成跑得動、看得見、留得下痕跡的流程。

---
*配套圖:`figures/methodology_flow.svg`(方法論流程)、`figures/n8n_topology.svg`(n8n 拓樸)。可匯入 workflow:見 `N8N_ORCHESTRATION.md` §4。*
