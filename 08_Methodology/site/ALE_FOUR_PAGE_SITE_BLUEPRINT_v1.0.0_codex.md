# ALE 四頁式互動網站內容藍圖

**規劃者**：Codex（OpenAI）  
**版本**：v1.0.0_codex  
**日期**：2026-06-21  
**狀態**：內容規劃稿；尚未開始 HTML 實作  
**網站核心**：從人的研究問題出發，展示 AI 如何把實驗變成工程、把工程推進為研究，並由 A2A Agent 接手執行。

---

## 1. 整站要回答的四個問題

| 頁面 | 讀者的問題 | 頁面任務 |
|---|---|---|
| 第一頁 · 故事 | 這件事怎麼開始？為什麼值得看？ | 用博士生、一天完成 dashboard、ALE 誕生與研究轉向建立情感與理解 |
| 第二頁 · 研究發表流程 | AI 到底怎麼協助完成研究與 DOI？ | 展開 00–99、G0–G6、人類／AI 分工、A2A 接手與回退機制 |
| 第三頁 · ALE 白皮書 | ALE 如何套用到其他 AI 工程工作？ | 解釋 Agentic Loop Engineering 與 A2A Data-to-Dashboard Skill Pack |
| 第四頁 · 證據與研究 | 有什麼真實成果、論文與文獻證據？ | 展示實驗網站、DOI 論文摘要、案例、限制及相關文獻 |

整站閱讀層級：

```text
故事理解
→ 流程理解
→ 方法套用
→ 證據查核
```

---

## 2. 全站共同敘事原則

### 2.1 主角

主角永遠是人類研究者。

AI 的定位：

- 加速實作
- 擴大搜尋
- 提供替代假說
- 對抗審查
- 協助形式化
- 接手重複工作

AI 不負責：

- 自動決定研究題目
- 自行宣布創新成立
- 替自己的產出完成獨立審查
- 取代原始來源
- 按下 DOI Publish
- 承擔研究責任

### 2.2 全站核心句

> 人類找到值得研究的問題；AI 放大實作、探索與驗證能力；證據與人類判斷決定什麼可以被公開主張。

### 2.3 正式命名

- 方法論：**Agentic Loop Engineering（ALE）**
- 資產：**A2A Data-to-Dashboard Skill Pack**
- 第一個案例：臺灣統一發票 Open Data 智慧分析 dashboard
- dashboard 代表性能力：
  - 回歸數據 AI 推論
  - CLI AI 分析
  - 數據落點 AI 分析

---

# 第一頁 · 從一天完成 Dashboard 到一個研究問題

## 3. 第一頁的唯一任務

讓完全不懂 ALE、A2A、SDLC 或 DOI 的人，在三至五分鐘內理解：

1. 主角是誰。
2. AI 做了什麼令人驚豔的事。
3. 人類接著提出了哪三個更深的問題。
4. 為什麼最後會走向論文研究。

本頁不詳細解釋 Gate schema、A2A JSON-RPC 或 n8n。

## 4. 第一頁戲劇結構

### Hero · AI 一天做完了

建議主標：

> **AI 用一天，完成了一個具有推理能力的專業資料網站。**

副標：

> 我是一名研究 AI 的博士生。原本只想測試今天的 AI 到底有多強，沒想到這個實驗最後發展成 Agentic Loop Engineering，以及一場 AI 輔助研究與論文發表的旅程。

視覺內容：

- 臺灣 Open Data
- dashboard 參考圖片
- 動態儀表板
- 三項 AI 分析能力
- 「1 DAY」結果

### 第一幕 · 人類提出問題

研究者正在做統一發票資料練習，找到臺灣政府 Open Data。

他不是叫 AI 隨便生一個作品，而是設定真實挑戰：

- 參考專業 dashboard 圖片
- 處理真實資料
- 建立動態網站
- 加入 AI 推理分析
- 形成可供人使用的專業分析介面

本幕關鍵句：

> 研究的第一步，不是 AI 給答案，而是人類找到值得驗證的問題。

### 第二幕 · AI 一天完成

展示完整成果：

- 資料取得與清理
- 聚合
- 互動圖表
- 回歸數據 AI 推論
- CLI AI 分析
- 數據落點 AI 分析
- 網站部署

情緒：

> AI 的能力令人驚豔。

但立即提出下一問：

> 這只是一次成功，還是可以被重複的工程能力？

### 第三幕 · 從作品到 Agentic Loop Engineering

把 Agentic Engineering 放入 SDLC：

```text
需求
→ 規劃
→ 實作
→ 測試
→ 獨立驗證
→ 修正
→ 記錄
→ Skill 化
→ 下一輪
```

形成：

- Agentic Loop Engineering
- A2A 接手協定
- Data-to-Dashboard 可重複流程
- A2A Data-to-Dashboard Skill Pack

本幕關鍵句：

> 真正的突破不是 AI 做出一個 dashboard，而是下一個 Agent 也能沿著同一套方法繼續工作。

### 第四幕 · 從工程方案到研究問題

完成 Skill Pack 後，人類提出新的問題：

> 這只是一套好用的工程技巧，還是一個具有學術價值、值得公開檢驗的方法？

AI 開始協助：

- 找相關研究
- 建立概念地圖
- 比較先前方法
- 質疑新穎性
- 探尋研究價值
- 形成研究問題
- 建立論文結構

頁尾 CTA：

> 下一頁：看人類與 AI 如何把研究一路推進到 DOI。

---

# 第二頁 · 研究如何從 00 走到 DOI

## 5. 第二頁的唯一任務

把整個 ALE 論文發表卷宗說清楚：

- 00–06 是主流程
- G0–G6 是不可跳過的 Gate
- 07 是持續回饋的 Lessons
- 08 是方法論與 Agent 操作規格
- 99 是橫貫全程的證據主幹
- A2A Agent 如何讀取狀態、執行 Skill、驗證結果、通過或退回

不能把 07、08、99 誤畫成 06 之後的普通線性階段。

## 6. 第二頁主視覺

建議採雙層流程：

```text
人類研究判斷層
────────────────────────────────────────
00 Ideas → 01 Consolidation → 02 Drafts → 03 Reviews
   G0           G1              G2           G3
→ 04 Evidence → 05 Due Diligence → 06 Publication / DOI
      G4               G5                 G6

AI Agent 執行層
STATE → Router → Skill → Validate → Gate
                     ↘ Fail: route back + Lessons
                     ↘ Pass: save state + evidence hash

橫貫全程：
08 Methodology / A2A Rules
99 References / Evidence Backbone
07 Lessons Learned / Feedback Loop
```

## 7. 00–99 詳細人類／AI 分工

| 卷宗 | Skill / Gate | 人類責任 | AI / Agent 工作 | 產出與過關條件 |
|---|---|---|---|---|
| 00 Ideas | `s00 ideate.seed` / G0 | 從真實經驗提出研究現象、痛點與問題 | 拆解問題、提出開放問題、找可能研究方向 | 有明確 seed problem 與 open questions |
| 01 Consolidation | `s01 consolidate.scope` / G1 | 判斷研究範圍與值得追求的價值 | 搜尋相關研究、比較 prior art、挑戰新穎性、協助收斂定位 | positioning、候選貢獻與讓出的公共知識清楚 |
| 02 Drafts | `s02 draft.write` / G2 | 決定論證方向與可接受主張 | 建立草稿、章節、Claim–Evidence 關係與證據等級 | problem、method、framework、limitations 完整 |
| 03 Reviews | `s03 review.adversarialLoop` / G3 | 決定哪些意見採納，要求修正過度宣稱 | Producer、Reviewer、Enhancer、Verifier 分離；找漏洞並核驗 finding | finding 全部處理，造假 rejected，無未解 P0 |
| 04 Evidence | `s04 evidence.run` / G4 | 設計／核准真實實驗，確認數據可信 | 執行程式、測試、量測、整理案例與結果 | measured results 存在，核心主張有實證 |
| 05 Due Diligence | `s05 diligence.check` / G5 | 對 originality 與研究倫理負責 | 查 prior art、逐筆核驗引用、檢查 placeholder 與 novelty class | 所有引用 verified，新穎性敘述乾淨 |
| 06 Publication | `s06 publish.deposit` / G6 | 最終核可、ORCID 登入、按 Publish | 檢查 PDF／CFF／Zenodo metadata，準備 submission package | DOI、metadata 一致、human approved |
| 07 Lessons | `s07 retrospect.capture` | 判斷哪些失敗值得制度化 | 記錄 hallucination、rejected findings、錯誤模式與修正 | 回饋下一輪，不是單次 Gate |
| 08 Methodology | Agent 操作規格 | 決定治理原則、權限與公開邊界 | 讀 AGENTS、handoff、schema；依 adapter 執行 | 全程約束，不是線性階段 |
| 99 References | Evidence Repository | 閱讀原文並判斷適用性 | 找文獻、索引、交叉比對、標記核驗狀態 | 橫貫所有 Claim 與 Gate |

## 8. A2A Agent 如何「扛起流程」

Agent 接手時不能只收到一句 prompt。

它需要：

```text
AGENTS.md
→ CURRENT_HANDOFF.md
→ Agent-specific Operating Guide
→ Shared STATE
→ Router 判斷下一個 Skill
→ 執行 Skill
→ 驗證 Output Schema
→ Self-check
→ Gate predicate
→ Save / Route back / Human escalation
```

### A2A 執行循環

```text
1. STATE.load(research_id)
2. Router 找第一個未通過 Gate
3. 檢查 Skill preconditions
4. 指派正確角色的 Agent
5. 執行並產生結構化 output
6. 驗證 schema 與 self-check
7. Gate = pass
   → 儲存狀態、版本、evidence hash
8. Gate = fail
   → 不得前進，帶 context 回前一關
9. 高風險／發表
   → 等待 human approval
```

### 三條視覺紅線

- 生產者 ≠ 審查者
- 沒有證據，不得通過 Gate
- 發表與「已驗證」宣稱必須有人類核可

## 9. 第二頁應加入的真實案例

4.5 倍資料事件放在 G3／G4 交界的案例框：

```text
Claude Code：產生錯誤資料處理／驗證結果
→ 自己的流程看起來正確
→ Codex 以獨立 reviewer 身分重新檢查
→ 發現資料膨脹 4.5 倍
→ 修正程式與驗證方式
→ Lessons 記錄：AI 不能替自己作獨立證明
```

這個案例用來證明角色分離，不再被寫成 ALE 起源。

頁尾 CTA：

> 下一頁：把這條研究 Loop，轉成可套用於 AI 工程的 ALE 白皮書。

---

# 第三頁 · Agentic Loop Engineering 白皮書

## 10. 第三頁的唯一任務

回答：

> 如果我有另一個 AI 軟體任務，要怎麼使用 ALE？

這一頁同時作為未來 ALE 白皮書與 `A2A Data-to-Dashboard Skill Pack` 白皮書的視覺入口。

## 11. ALE 的標準 Loop

建議以八步循環呈現：

1. **Frame**：人類定義問題、價值與限制。
2. **Plan**：Agent 拆解任務、依賴、風險與完成條件。
3. **Build**：Producer Agent 實作。
4. **Test**：機械測試與可重現檢查。
5. **Challenge**：獨立 Reviewer Agent 對抗審查。
6. **Verify**：原始資料、真實執行與人類判斷。
7. **Gate**：達標才發布或進下一階段。
8. **Capitalize**：把成功流程、錯誤與判斷保存成 Skill。

接著進入下一輪。

## 12. ALE 與 SDLC 的對應

| SDLC | ALE 增強 |
|---|---|
| Requirements | Human framing + AI clarification |
| Design | 多方案生成、風險與 Gate 預先定義 |
| Development | Producer Agent 實作與版本化 |
| Testing | 機械閘、測試、不變量 |
| Review | 獨立 Reviewer，不由 Producer 自審 |
| Deployment | 人類核可、證據與 metadata |
| Maintenance | STATE、handoff、Lessons、Skill capitalization |

## 13. A2A Data-to-Dashboard Skill Pack

白皮書應說清楚它不是一個 prompt 集合，而是一組可交接資產：

- Agent Card
- Skills
- Input / Output schema
- Preconditions
- Gate predicates
- Self-check
- Failure semantics
- Shared State
- Handoff
- Evidence log
- Human approval point

Data-to-Dashboard 建議 Skill 組：

```text
data.discover
→ data.acquire
→ data.profile
→ data.clean
→ data.aggregate
→ dashboard.design
→ dashboard.build
→ ai.analysis.regression
→ ai.analysis.cli
→ ai.analysis.dataPosition
→ review.adversarial
→ verify.sourceAndRuntime
→ deploy.release
→ retrospect.capture
```

正式 Skill 名稱仍須在白皮書撰寫時逐一確認，不在網站企劃階段假定已凍結。

## 14. 第三頁互動構想

使用者選一個任務類型：

- Data-to-Dashboard
- 研究與論文
- 一般軟體功能
- 企業流程自動化

頁面顯示：

- 對應 Loop
- 人類決策點
- Agent 角色
- Gate
- 應保存的 Skill

頁尾 CTA：

> 下一頁：查看真實案例、研究摘要、DOI 與相關文獻。

---

# 第四頁 · 實驗案例、DOI 論文與研究證據

## 15. 第四頁的唯一任務

讓讀者自行判斷：

- 系統是否真的存在？
- 方法是否實際使用過？
- 論文主張是什麼？
- 哪些證據已完成？
- 哪些限制仍公開保留？
- 它與哪些研究相關？

## 16. 第一區 · 實驗案例網站

展示：

- 實際 dashboard 網站連結／截圖
- 臺灣 Open Data 來源
- 完成時間：一天
- 技術與功能摘要
- 三項 AI 分析能力
- Data-to-Dashboard 流程
- 4.5 倍錯誤發現與修正紀錄

重要區分：

- 「一天完成」描述第一版端到端成果。
- 後續治理、修正、Skill 化與研究不是全部在同一天完成。

## 17. 第二區 · DOI 論文摘要

用非學術讀者也能看懂的五格摘要：

1. **研究問題**：如何治理可重複的 Agentic Software Development？
2. **方法**：機械閘、人類核可、證據主幹、獨立審查、Skill 資產化。
3. **案例**：Data-to-Dashboard 與論文生產流程。
4. **發現**：AI 能大幅加速，但同源驗證與自我審查會產生 false confidence。
5. **限制**：第二案例與部分量化實驗仍待完成；預印本與正式論文狀態需清楚區分。

提供：

- DOI
- PDF
- Citation
- CITATION.cff
- License
- GenAI 使用揭露

## 18. 第三區 · Claim–Evidence 狀態

建議用狀態卡：

- `validated`
- `preliminary`
- `conceptual`
- `blocked`

不能只展示成果，必須展示限制。

例如：

| 主張 | 狀態 | 證據 |
|---|---|---|
| AI 一天完成第一版 dashboard | case evidence | 網站、commit／log、輸出 |
| 獨立 reviewer 發現 4.5 倍錯誤 | case evidence | 修正紀錄、review finding |
| ALE 可降低 false pass | preliminary / pending experiment | EXP-001 |
| 可跨專案泛化 | blocked / second case pending | 第二案例 |

## 19. 第四區 · 相關文獻

不要只列 bibliography；依研究問題分群：

- Agentic Software Engineering
- LLM-based coding agents
- Multi-agent review／debate
- Software supply-chain evidence
- Human-in-the-loop governance
- Design Science Research
- Reproducibility and executable evidence
- Skill／memory capitalization

每篇顯示：

- 文獻解決什麼問題
- 與 ALE 相同之處
- 與 ALE 不同之處
- ALE 是否引用、讓出或延伸該概念
- 原始 PDF／DOI／arXiv 連結
- verified 狀態

## 20. 第四頁結尾

建議結尾：

> 這項研究不是在證明 AI 可以取代研究者，而是在探索：當 AI 開始承擔更多工程與研究工作，人類如何仍能保有問題意識、證據標準與最終責任。

---

## 21. 四頁導覽名稱

建議中文：

1. `故事起點`
2. `研究到 DOI`
3. `ALE 如何運作`
4. `案例與證據`

建議英文：

1. `Origin Story`
2. `Research to DOI`
3. `How ALE Works`
4. `Cases & Evidence`

避免使用：

- 首頁
- 方法
- 更多
- 其他

因為無法讓第一次來的讀者預測內容。

---

## 22. 實作順序

內容核准後，不應四頁同時開工。

建議：

1. 凍結第一頁中文故事。
2. 凍結第二頁 00–99 與 A2A 流程。
3. 定義第三頁 ALE 白皮書目錄與 Skill Pack 邊界。
4. 整理第四頁網站、DOI、PDF、文獻與 Claim–Evidence 資料。
5. 建立共用網站 shell 與四頁導覽。
6. 實作第一頁。
7. 實作第二頁。
8. 實作第三、第四頁。
9. 完成英文版。
10. 驗證桌機、手機、連結與內容一致性。

---

## 23. 仍待 Morris 確認

1. 「發表前抓回三個錯」是否公開三項完整內容？
2. 正式論文是否仍等待第二案例，先走預印本 DOI？
3. 第一個 dashboard 的公開網站路徑／網址。
4. CLI AI 分析的正式中文／英文名稱及實際操作形式。
5. 「數據落點 AI 分析」的精確定義與英文名稱。
6. 四頁網站最終是四個 HTML，還是一個 HTML 的四個 route？

