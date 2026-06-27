# 04 · Evidence（證據・案例・實驗) ← 流水線目前卡在此關

**階段目的**:為主張提供**可稽核證據**。**主實驗 = Skill Capitalization Loop(EXP-002)**:真實案例 → SDLC → 可重用+可驗證 Skill → 重用降本,以 loop 重複實踐 Agentic engineering;EXP-001(test collusion)為其「可驗證關卡」子實驗。這是把 `[研究假說]` 升級為 `[已驗證]` 的關卡。
**上一關**:G3(審閱收斂)｜**下一關**:G4 過關 → 進 `05_DueDiligence`。

---

## 內容

| 檔案/目錄 | 性質 | 狀態 |
|---|---|---|
| `experiments/` | **實驗區索引**(主/子實驗) | ✅ 見 `experiments/README.md` |
| `experiments/EXP-002_Skill_Capitalization_Loop/` | **主實驗**:技能資產化迴圈 | 🟡 Loop 0 素材已存在,待形式化 + 跑 Loop 1 |
| `experiments/EXP-001/` | 子實驗:test collusion(可驗證關卡) | 🟡 scaffold 已建,待接模型端點 |
| `ALE_CaseStudy_EInvoice_v2.md` | 電子發票田野案例(現行) | ✅ §4 真實執行輸出 |
| `ALE_EXP-001_Protocol_v2.md` | test collusion 協定(現行) | ✅ 已凍結 |
| `*_v1*` / `_codex` / `_gemini` | 前版與審閱稿 | 保留軌跡 |

---

## ✅ Gate-Review Checklist — G4（證據 → 盡職調查) ⛔ 未過

**主實驗(EXP-002 · Skill Loop)**
- [x] Loop 0 素材存在(電子發票 → TigerAI 專有交付 skill set〔機密,摘要見 loop0/SKILL_SUMMARY_abstract.md〕,原案 proven)
- [x] Loop 0 **形式化**為 ALE Skill Manifest + 證據鏈 + FSM 狀態(`experiments/EXP-002_.../loop0/`;判定 **Validated**)
- [ ] ⛔ **Loop 1 已跑**(新資料組裝;量 lead time/rework/reuse/defect)→ H1/H3
- [ ] ⛔ 邊際成本曲線(Loop 2+)→ H4
- [ ] ⛔ 晉升治理生效(未過 eval 不得 Certified/取用)→ H2

**子實驗(EXP-001 · Test Collusion,服務 H5)**
- [x] 協定凍結、scaffold + 真實 seeded task(T01)就緒
- [ ] ⛔ 接模型端點跑 pilot(spec-gen vs impl-gen false-pass)

**共同**
- [x] 案例證據真實非虛構(實跑 `vv_crosscheck.py`,PASS/exit 0)
- [ ] ⛔ 結果 → **建議 → 結論**,回寫 §6/§7/§9.7/§10/§12.2(出 v2.6)

> 規則(G4 = ALE「No measured evidence, no sign-off」):**主 loop 未跑出降本/可驗證數據,本關不過**;目前**無任何 `[已驗證]` 主張**。
> 例外:`06` 預印本子路徑(arXiv/Zenodo)可並行鎖優先權;正式 full paper 須過 G4。
