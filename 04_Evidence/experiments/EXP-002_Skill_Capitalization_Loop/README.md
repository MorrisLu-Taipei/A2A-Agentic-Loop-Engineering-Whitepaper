# EXP-002（主實驗)· Skill Capitalization Loop
## 把真實案例經 SDLC 沉澱成「可被 AI Agent 重用、可驗證」的 Skill,並以 loop 重複實踐 Agentic engineering

**這是 ALE 的主實驗**(對應核心命題 §6、RQ3 降本、RQ4 可稽核)。
**子實驗**:`../EXP-001/`(test collusion)只驗證本 loop 中「V&V 關卡是否真可驗證、不自我欺騙」。
**鐵則(= 你定的研究流程)**:**跑 loop → 蒐集發現/建議/結論(過卷宗 G4)→ 才進 `06_Publication` 發表(G6)。沒有實證,不發論文。**
**全程 Docker**(對齊 ALE §9.4)。

> 研究主張白話:**「同一套 Agent 工程,做一次就把經驗變成可重用、可驗證的 Skill;下一次用組裝的,愈做愈快、愈穩。」** 本實驗就是去量「是不是真的愈做愈快、愈穩」。

---

## 真實素材(loop 不是空想,已有一輪在跑)
> 🔒 **機密界線**:Loop 0 萃取出的交付 skill set 是 TigerAI **商業機密**。本卷宗**只做抽象說明 + 外部成效指標**,**不揭露**技能清單、資料契約、內部結構(細節僅存私有套件)。抽象說明見 `loop0/SKILL_SUMMARY_abstract.md`。

- **案例(Loop 0 輸入)**:電子發票開放資料儀表板 `06_Product/04_EInvoiceDashboard`(已交付:六頁 + 3 n8n workflow + V&V 閘 `vv_crosscheck.py`)。
- **萃取出的 Skill(Loop 0 輸出)**:一套 **TigerAI 專有的「資料 → 自動化儀表板」交付 skill set**(覆蓋完整 SDLC、自帶驗證關卡;**細節為機密,從略**)。
- → **Loop 0 為 retrospectively documented(事後形式化記錄,非 proven)**:電子發票案是已交付實例,但無可重現 skill manifest/eval/工時數據,故**不宣稱 proven**;本實驗把它形式化為 ALE 證據(抽象層級),再跑 Loop 1、2 取得降本數據。「技能資產化降本」一律維持**假說**語氣。

---

## ① 實驗設計（Design)

- **研究對象**:ALE 的 **Skill Capitalization 迴圈**本身。
- **一個 loop** = 真實案例 → 走 ALE SDLC 八階段(每階段有 gate)→ **Skill Extraction**(產 Skill Manifest + eval + evidence)→ 入 Skill Repository(FSM:Draft→Candidate→Validated→Certified)→ **下一案由 Agent 以該 Skill 組裝**。
- **對照**:`from-scratch`(不用 skill,從零做新案) vs `assembled`(用 Certified skill 組裝)。
- **可驗證性是硬條件**:Skill 須通過自身 **eval(data-contract 驗證 + 不變量 + smoke + security)** 才得晉升 Certified、才可被 Orchestrator 取用——**No validation, no promotion**。
- **抗自我欺騙**:Skill 的 V&V 測試須**從 spec/不變量生成、非從實作生成**(嵌 EXP-001),否則「可驗證」是假的。

---

## ② 計畫（Plan / the loops)

| Loop | 案例 | 動作 | 量測 | 狀態 |
|---|---|---|---|---|
| **0** | 電子發票 | 回溯**形式化**:把專有 skill set 對映成 ALE 證據(**抽象**)+ FSM 狀態判定 | 建立基線 | ✅ **已形式化** → `loop0/`(判定 **Validated**) |
| **1** | 新開放資料(待選) | Agent 依資料契約**組裝**出儀表板 | lead time / rework / reuse rate / defect / V&V 通過率 | ⬜ 待選資料 + 執行 |
| **2+** | 第三、四案 | 累積 Certified skills,觀察邊際成本 | 邊際成本曲線(§6 次線性 vs U 形拐點) | ⬜ |

> **待你選**:Loop 1 用哪份資料?(建議:另一個政府 ODS,或一份客戶交易/銷售資料——與發票結構不同,才測得出「可組裝性」與「語意相容」。)

---

## ③ 實作與數據（Implementation & Data)

- **Skill 摘要記錄**:`loop0/SKILL_SUMMARY_abstract.md`(抽象層級;**技能清單/契約/結構屬機密,不在此**)。
- **可驗證流程**(loop 的關卡,抽象描述):
  1. 資料契約驗證(輸入結構符合?**契約內容機密**)
  2. **不變量機械閘**(`vv_crosscheck.py` 式上界 + 去重蛻變,見 EXP-001 §INV)
  3. **smoke**(原案已有;Loop 1 產新案 smoke)
  4. security / 無寫死憑證
  → 全過才 `Validated`;多案實證 + 人核 → `Certified`。
- **量測框架(已備好,等資料即跑)**:`metrics/METRICS_SCHEMA.md`(成效指標定義)、`loop0/BASELINE_einvoice.md`(from-scratch 基準)、`results/RESULTS_TEMPLATE.md`(④⑤ 模板)。
- **數據區(待 Loop 1 後填)**:`metrics/reuse_loop1.json`。

---

## ④ 假設與驗證（Hypotheses & Decision Rules)

| 假說 | 對應 | 量測 | 判定規則 |
|---|---|---|---|
| **H1 降本** | RQ3/§6 | lead time、rework | assembled 顯著 < from-scratch ⇒ 支持 |
| **H2 可驗證晉升** | §5.5 | eval 通過率 vs 晉升 | 未過 eval 卻被取用 = 治理失敗(必須為 0) |
| **H3 可組裝** | §5.4/§12.2(5) | 自動組裝成功率 | 成功 ⇒ 支持;失敗 ⇒ 暴露語意不相容,需 contract test |
| **H4 邊際成本** | §6 | 逐 loop 單位成本 | 次線性下降 ⇒ 支持;反彈 ⇒ 找 U 形拐點(策展成本) |
| **H5 抗共謀(嵌 EXP-001)** | §7 | spec-gen vs impl-gen 測試之 false-pass | impl-gen 顯著較高 ⇒ V&V 須規格隔離才算「真可驗證」 |

**誠實前提**:loops 數少時以描述統計 + 個案追蹤為主,不過度宣稱統計顯著;結果無論支持或否定,**都回寫白皮書 §6/§7/§9.7/§10/§12.2**。

---

## ⑤ 結果 → 建議 → 結論（→ 才發表)　[待 loops 後填]

執行 Loop 1(及 2+)後,在此產出:

1. **結果**:各 loop 的 lead time / rework / reuse / defect / 成本曲線(對照 from-scratch)。
2. **建議(可操作)**:給想導入 ALE 的團隊——哪些階段最該 skill 化、晉升門檻怎麼設、策展成本怎麼壓(維持次線性)、V&V 怎麼避開 test collusion。
3. **結論**:H1–H5 判定 + 對核心命題(§6 技能資產化、§7 反自我欺騙)的修訂。
4. **→ 然後才發表**:把以上回寫進 `02_Drafts` 出 v2.6,Claim–Evidence Matrix 升級,**過 G4 → 進 06_Publication**。

> 模板:`results/RESULTS_TEMPLATE.md`(待建)。

---

## 待你拍板
1. **Loop 1 用哪份資料**?(決定後我建 `tasks/`/契約對映並設計組裝步驟)
2. **組裝由誰跑**:n8n 主幹 + Agent?(該 skill set 本就以 n8n 為主幹)
3. 是否**先做 Loop 0 形式化**(把現有 skill pack 對映成 ALE Manifest + 證據,馬上可做,不需新資料)?
