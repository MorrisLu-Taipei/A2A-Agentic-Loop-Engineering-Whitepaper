# 05 · Due Diligence（新穎性・原創性・盡職調查)

**階段目的**:發表前的學術盡職調查——先前技術檢索、新穎性界定、原創性/誠信聲明、引文核驗。
**上一關**:G4(證據到位)｜**下一關**:G5 過關 → 進 `06_Publication`。

---

## 內容

| 檔案 | 性質 | 狀態 |
|---|---|---|
| `ALE_PriorArt_RelatedWork_v2.md` | 先前技術檢索日誌 + 對比矩陣(現行) | ✅ 已採 Gemini 校準 |
| `ALE_Originality_Statement_v2.md` | 原創性與學術誠信聲明(現行) | ✅ 移除絕對措辭 + 授權建議 |
| `*_v1*.md` / `_codex` / `_gemini` | 前版與審閱稿 | 保留軌跡 |

---

## ✅ Gate-Review Checklist — G5（盡職調查 → 投稿)

- [x] 針對性 repo 查核(agenticloops)— 無實質重用
- [x] 先前技術**檢索日誌可重現**(平台/query/日期/納入排除)
- [x] 對比矩陣填妥、**可辯護新穎性**界定
- [x] **創新性 × 研究價值評估卡**(`NOVELTY_AND_VALUE_ASSESSMENT.md`)——標明:新穎性=候選;研究價值之「有效性」待 G4
- [ ] ⚠ **prior-art 檢索窮盡化**(目前僅數組 query;升信心需擴大平台/query + 記錄納入排除)
- [x] 原創性聲明**措辭校準**(非「無抄襲」絕對式)
- [x] **arXiv 引文已核驗**(10 篇,見 `../99_References/`)
- [ ] ⚠ **非 arXiv 引文待核**(SLSA / in-toto / MCP / DevOps 書 / Barr survey / DS Dojo)
- [ ] References **零 placeholder**(投正式版前)

> 規則(G5):**新穎性界定不清、或有未核驗/造假引文,不投稿**。絕對措辭(無抄襲/全球首創/概念重疊 0)一律禁用。
