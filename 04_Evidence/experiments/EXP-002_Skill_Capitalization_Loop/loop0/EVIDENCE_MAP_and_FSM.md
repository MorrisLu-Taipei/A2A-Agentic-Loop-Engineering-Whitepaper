# Loop 0 · 證據對映與 FSM 狀態判定（抽象層級)

> 🔒 **機密界線**:萃取出的 skill set 是 TigerAI 商業機密。本檔**只對映「SDLC 階段 ↔ 證據」與 FSM 狀態**,**不列出**技能模組名稱、資料契約內容或內部結構(那些屬機密)。skill set 的抽象說明見 `SKILL_SUMMARY_abstract.md`。

**目的**:把「電子發票案 → SDLC → 可重用可驗證 Skill」這**已發生的一輪**(Loop 0)形式化為 ALE 證據,並**誠實判定**生命週期狀態。
**結論先講**:該 Skill 現為 **Validated**;**尚未** Certified(需 ≥3 獨立案例,目前 1 案)→ 這正是要跑 Loop 1、Loop 2 的理由。

---

## A. SDLC 階段 ↔ 證據（Loop 0 = 電子發票;技能名稱屬機密,從略)

| ALE SDLC 階段 | Loop 0 證據(電子發票,皆為非機密之案例產物) |
|---|---|
| Context/Requirement | 資料契約比對(輸入:時間=發票月、度量=張數/金額、維度=縣市/行業/載具) |
| Requirement / SA | 案例規劃與報告(見案例研究) |
| SD | `06_Product/04_EInvoiceDashboard/SDD.md` |
| PG | 六頁單檔 HTML、季節預測 / 異常偵測 / Text-to-SQL |
| **V&V(可驗證關卡)** | **`06_Product/04_EInvoiceDashboard/vv_crosscheck.py` 實跑 PASS / exit 0**;上界比值 17.3%<100%;跨引擎一致 |
| Security | 唯讀帳號、密碼輪替、CSP 標頭(DEVLOG 安全補強) |
| Deployment | docker compose;healthcheck;回滾 |
| Monitoring | 3 支 n8n workflow(更新 / 告警 / 月報) |
| 自動化主幹 | `06_Product/04_EInvoiceDashboard/n8n/VERIFICATION_REPORT.md` 3/3 PASS(通知 stub,誠實標) |
| Feedback | 結案 / 經驗教訓(見案例研究) |
| Evidence / Git | Git 證據主幹 |

> 重點(可公開):這套 Skill「**自帶驗證關卡**」——以資料契約 + 不變量機械閘 + smoke 作為交付前客觀檢查(ALE §7.3/§7.7),不是「能跑就好」。**關卡如何實作屬機密。**

---

## B. FSM 狀態判定（誠實,逐條對門檻)

```
Draft ──✅──> Candidate ──✅──> Validated ──❌(未到)──> Certified
```

| 門檻 | 要求(抽象) | Loop 0 現況 | 判定 |
|---|---|---|---|
| → Candidate | 技能定義 + 資料契約 + ≥1 smoke | ✅ 具備 | 過 |
| → Validated | 一案 eval 全過、security 0 critical、evidence 附上 | ✅ 電子發票案全過 | **過 → 目前在此** |
| → Certified | **≥3 獨立案例**、0 blocked、scan 0 critical、人核 | ❌ 目前**僅 1 案** | **未過** |

**∴ 現狀 = `Validated`。** 依 ALE 鐵則「**No validation, no promotion**」與「Certified 需多案實證」,**不可**自封 Certified——這也是 Loop 1、Loop 2 必要的原因(湊滿 ≥3 獨立案例才升 Certified)。

---

## C. 已證明 / 未證明(可公開)
**已證明(初步)**:真實案例**可以**被 SDLC 沉澱成一個**自帶驗證關卡**的可重用 Skill;且在原案 eval 全過 → 達 Validated。
**未證明(待 Loop 1/2)**:重用降本(H1)、可組裝(H3)、邊際成本曲線(H4)、Certified(需 ≥3 案)。

## D. Loop 1 啟動條件
選一份**結構不同**的資料 → Agent 以組裝方式產出儀表板 → 量 lead time / rework / reuse / defect / V&V 通過。**技能內部不外露,只量外部成效指標。**
