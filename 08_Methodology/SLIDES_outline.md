---
title: "以可執行證據治理 AI 軟體開發：Agentic 工程與 n8n 實作"
subtitle: "從模型共識到可執行證據 · 3×AI + 人類的論文/交付生產線"
author: "Yeh-Hsing Lu (Morris) · Tiger AI Tech"
date: "2026"
---

# 投影片大綱（每張 `##` = 一張投影片;可直接轉 PDF/Beamer)

## 1. 開場:一張對不上的發票
- 真實案例:電子發票儀表板,金額膨脹 **4.5 倍**
- 驗證(儀表板 vs DB)兩邊都 PASS → 因為**同源、一起錯、互相背書**
- 提問:這是 bug,還是結構性問題?

## 2. 核心風險:當「驗證 AI 的也是 AI」
- AI 寫碼 + AI 寫測試 → 收斂到「全綠燈、卻沒驗到規格」
- 名稱:shared-context false pass(早期叫 test collusion)
- ⚠ 多找幾個 AI 互檢**未必**救得了(假說,待實驗)

## 3. 解法主張:從模型共識 → 可執行證據
- 機械閘(突變/覆蓋/性質/不變量/真實執行)= 不問模型意見的事實
- 模型評議只「找分歧」;人類「審證據」不審共識
- 外部實證:arXiv:2512.03097 — 共識不安全,但**接外部指南的 verifier 有效**

## 4. 方法論三鐵則
- 生產者 ≠ 審查者
- 證據 > 共識(AI 產出一律查原始來源)
- 過關才往下 · 人類負最終責任

## 5. Stage-Gate 流水線(00→08)
- 00 Ideas → 01 Consolidation → 02 Draft → 03 Review → 04 Evidence → 05 DueDiligence → 06 Publication → 07 Lessons(↺)→ 08 Methodology
- 每關一個 gate:No evidence, no release
- (圖)`figures/methodology_flow.svg`

## 6. 角色:3×AI + 人類
- 人類(Founder):洞察 / 證據 / 決策 / 負責
- Claude:操作化 / 整合 / 查核
- Codex:對抗式審查
- Gemini:形式化 / 潤稿

## 7. 真實案例:這套方法當場抓到 3 個錯
- 撞名(別人已用 Agentic Loop Engineering)
- 漏 prior art(Code-A1 已提 self-collusion)
- 誤讀文獻(把 2512.03097 講反)
- → 全靠「對抗審查 + 讀原文」抓出

## 8. n8n 為什麼適合
- stage-gate 視覺化 · 斷點續傳 · 天然稽核 · 組合不重造
- (圖)`figures/n8n_topology.svg`

## 9. Lab 開始:WF-1 Hello-State
- State Object → Router → 看 next_skill
- 匯入 `n8n_workflows/WF-1_Hello-State.json`

## 10. WF-2 Gate-Demo
- IF gate:open_findings==0 → pass / 否則回 Router
- 練習:改成 1,看走哪條線

## 11. WF-3 Review-Loop(生產者≠審查者)
- 平行 reviewer + enhancer → Merge+Verify
- 作業:把 stub 換成真 HTTP(不同模型!)

## 12. WF-4 Verify(★ 靈魂)
- 不盲信 AI:真打 arXiv 核驗書目
- 對不上 → 不准引用

## 13. WF-5 Mechanical-Gate
- 覆蓋率≥85% + 突變≥75% 雙門檻
- 真實版:Execute Command 跑 pytest/mutmut

## 14. WF-6 Human-Approval
- Wait 節點:發表前人類必核可

## 15. WF-7 PriorArt-Verify
- 真打 arXiv 批次核驗 → 對比矩陣
- 對應「撞名/漏 prior-art」教訓

## 16. WF-8 Publish-Preprint
- metadata 一致性 →(sandbox)DOI
- ⚠ 用 ORCID 登入 Zenodo 再 deposit(否則不進你的學術紀錄)

## 17. 三個 n8n 真實踩坑
- schedule trigger 不能 CLI execute
- healthcheck 用 127.0.0.1
- 憑證/工作流 JSON 帶顯式 id

## 18. Capstone
- 把 WF-2~8 串成 Full-Pipeline,跑自己的小題目到「預印本就緒」
- rubric:State 流轉 / Gate 邏輯 / 對抗審查含查證 / 誠實邊界

## 19. 學術誠信
- GenAI 使用揭露(AI 不列作者)
- 引文查證 · prior-art 矩陣 · 證據等級標註(不過度宣稱)

## 20. 收束
- n8n 不是來「自動生論文」
- 是把**「多 AI 對抗 + 人類查證 + 過關才往下」**變成看得見、跑得動、留得下痕跡的紀律
- = ALE 白皮書 §7/§9 的可執行版
