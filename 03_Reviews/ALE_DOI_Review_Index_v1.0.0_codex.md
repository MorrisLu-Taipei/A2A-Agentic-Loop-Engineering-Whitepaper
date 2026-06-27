# ALE DOI 投稿前 Codex 總審索引

**作者 / Reviewer**：Codex（OpenAI）  
**版本 / Version**：v1.0.0_codex  
**日期 / Date**：2026-06-21  
**審閱範圍**：`04_RnD/01_ALE/` 全目錄  
**審閱性質**：Zenodo DOI / Working Paper 發布前獨立總審  

## 本次 Codex 交付

| 文件 | 主要用途 | 主要針對文件 |
|---|---|---|
| `ALE_DOI_Readiness_Review_v1.0.0_codex.md` | DOI 發布 GO / NO-GO 判定與修正順序 | 主稿、CITATION、Zenodo、作者、證據、引用 |
| `ALE_Academic_Naming_Review_v1.0.0_codex.md` | 網路與學術文獻命名查核、最終標題建議 | 主稿標題、CITATION、所有 Publication metadata |
| `ALE_Prepublication_File_Audit_v1.0.0_codex.md` | 全卷宗逐區、逐文件審閱紀錄 | `00`–`06`、`99`、根目錄文件 |

## 最終判定

**目前狀態：NO-GO（暫緩按下 Zenodo Publish）。**

這不是否定 ALE，也不是要求等完整期刊實驗後才能取得 DOI。Zenodo Working Paper 可以在 EXP-001 / EXP-002 完成前發布，但至少須先完成下列 P0：

1. 更換與既有文獻直接撞名的 `Agentic Loop Engineering (ALE)`。
2. 補入直接 prior art：`Code-A1` 已於 2026-03 使用 **self-collusion** 描述 Code LLM / Test LLM 的同類問題。
3. 修正對 `arXiv:2512.03097` 的誤讀：該文的 verifier 是有效防禦，不是「證明 verifier 擋不住」。
4. 摘要、貢獻與 Related Work 改成與證據等級一致。
5. 新增 GenAI 使用揭露；作者本人對全文與引用負責。
6. 統一標題、作者、版本、日期、狀態與 DOI metadata。
7. 產出正式 PDF 並完成逐頁終檢。

完成以上項目後，可發布：

> **Resource type**：Working Paper / Technical Report  
> **狀態**：Conceptual Framework and Research Agenda  
> **證據聲明**：包含初步田野觀察；受控實驗尚未完成。

## 最重要的對角線

```text
既有研究已使用 Agentic Loop Engineering (ALE)
× Code-A1 已直接提出 code/test self-collusion
× ALE 卷宗真正較強的價值是 evidence governance + lifecycle integration + skill capitalization
→ 不再搶「ALE / collusion 現象首創」，改以「從模型共識轉向可執行證據」作為論文主軸。
```

