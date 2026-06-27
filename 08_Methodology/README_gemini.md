# 08 · Methodology（本研究的生產方法論 — Gemini 修訂版）

本檔案為 `08_Methodology` 的 **Gemini 修訂版導讀**。其主要目的在於整合新發表的 `_gemini.md` 檔案，特別是補齊了 A2A Agent 運行所需的 JSON-RPC 格式與 Schema 深度規格檔案 **`A2A_SKILLSET_gemini.md`**，並明定 **Gemini 編輯代理人** 的工作職責與驗證規範。

---

## 🤖 給 AI Agent 的入口（A2A 入門指引）

若您是被指派「接手這條研究與論文生產線」的自主/協同 AI Agent：

1.  **首要任務**：閱讀 [AGENTS.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/08_Methodology/AGENTS.md) 了解主執行迴圈、全域紅線與執行流程。
2.  **深入資料結構**：載入 **[A2A_SKILLSET_gemini.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/08_Methodology/A2A_SKILLSET_gemini.md)**，這是本方法論的**深度規格書**，包含完整的 State Object JSON Schema、各 Skill 的 I/O 驗證合約，以及專屬於 **Gemini 編輯代理人** 的形式化、代碼生成與文獻核檢操作細則。
3.  **流程編排落地**：參考 [N8N_ORCHESTRATION.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/08_Methodology/N8N_ORCHESTRATION.md) 進行節點對應與環境變數設定。

---

## 📂 目錄文件導覽（更新版）

| 檔案 | 類型與用途 | 適用對象 |
|---|---|---|
| [README.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/08_Methodology/README.md) | 原始方法論說明（歷史存檔） | 全員 |
| **[README_gemini.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/08_Methodology/README_gemini.md)** | **本導讀檔**：整合 `_gemini` 資產與 A2A 入口導航 | 全員 |
| [AGENTS.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/08_Methodology/AGENTS.md) | 自主 / A2A Agent 運作主手冊 | 執行期 Agent |
| **[A2A_SKILLSET_gemini.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/08_Methodology/A2A_SKILLSET_gemini.md)** | **新技能規格書**：完整 JSON Schemas、錯誤碼與 Gemini 操作細則 | 執行期 Agent (尤其是 Gemini) |
| [PROCESS_FLOWCHART.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/08_Methodology/PROCESS_FLOWCHART.md) | 生產線文字流程圖與真實事件比對 | 架構師 / 設計者 |
| [STORY_how_to_use.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/08_Methodology/STORY_how_to_use.md) | 多 Agent 論文協同寫作實戰故事（SOP 範例） | 新加入的協作者 |
| [N8N_ORCHESTRATION.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/08_Methodology/N8N_ORCHESTRATION.md) | n8n 工作流編排與除錯 Lab 指南 | 系統部署與運作人員 |
| [COURSE_SYLLABUS.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/08_Methodology/COURSE_SYLLABUS.md) | 學術方法論 8/16 週教學課綱與評分標準 | 授課教師 |

---

## ✍️ Gemini 編輯代理人 (Editor Agent) 核心職責摘要
在 `3×AI + 人類` 的協同寫作管線中，Gemini 主要執行以下任務（詳細判定合約見 `A2A_SKILLSET_gemini.md §3`）：
1.  **數學與統計形式化校對**：驗證草稿中條件協方差、偏誤與變異的統計論證合理性。
2.  **不變量性質測試代碼生成**：針對系統紅線，自動產出基於 `Hypothesis` 測試庫之 Python 代碼。
3.  **文獻真實性核檢 (學術防線)**：核查 `99_References` 內的真實 PDF 檔案，校正對 `arXiv:2512.03097` (Adversarial Consensus) 與 `arXiv:2603.15611` (Code-A1) 的引用與解讀。
4.  **排版與 GenAI 揭露審查**：審查學術大標題（選用方案 A：*Governing Agentic Software Development with Executable Evidence...*）並置入標準 AI Use Disclosure 條款。
