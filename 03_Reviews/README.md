# 03 · Reviews & Feedback（審閱與建議)

**階段目的**:獨立審閱主稿(生產者 ≠ 審查者,= ALE §5.3)。收 AI 審稿(Codex / Gemini)、**其他作者/共同作者建議**、未來同行評審意見,並持續累積。
**上一關**:G2(草稿自洽)｜**下一關**:G3 過關 → 進 `04_Evidence` 補證據。
**回饋對象**:審閱意見回流去修 `02_Drafts`(白皮書)、`04_Evidence`、`05_DueDiligence`。

> 原則(= ALE §5.3):**生產者 ≠ 審查者**。審閱用獨立實例;發現的問題以**機械事實/證據**裁決,不以「誰講得漂亮」。

---

## A. 已收到的審閱（AI 審稿)

| 檔案 | 審閱者 | 內容 | 採納結果 |
|---|---|---|---|
| `ALE_Review_Index_codex.md` | Codex | 審閱索引 + 總判斷 + 優先順序 | → 白皮書 v2.4 校準 |
| `ALE_WhitePaper_v2.3_codex.md` | Codex | 逐節風險/校準(P0/P1/P2) | → v2.4 |
| `ALE_Review_Index_gemini.md` | Gemini | 修訂對照表 | → v2.5 |
| `ALE_WhitePaper_v2.4_gemini.md` | Gemini | 精簡重寫(3 個 gem 已嫁接) | → v2.5 |
| `README_gemini.md` | Gemini | README 修訂建議 | 參採 |
| `ALE_DOI_Review_Index_v1.0.0_codex.md` | Codex | DOI 前審總索引(NO-GO 判定) | → **v3.0** |
| `ALE_DOI_Readiness_Review_v1.0.0_codex.md` | Codex | DOI GO/NO-GO + P0/P1 修正順序 | → v3.0(全收) |
| `ALE_Academic_Naming_Review_v1.0.0_codex.md` | Codex | 命名撞名查核 + 標題建議 | → v3.0 改名 |
| `ALE_Prepublication_File_Audit_v1.0.0_codex.md` | Codex | 全卷宗逐檔審 | → v3.0 + ancillary 修正 |
| `ALE_DOI_Readiness_Review_v1.1.0_gemini.md` | Gemini | **獨立第二審**:確認同 3 個 P0 + 發布封裝衛生 | → 三方交叉確認;補發布排除清單 |
| `ALE_DOI_Review_Index_v1.1.0_gemini.md` | Gemini | Gemini 審閱索引 + GO-Gate tracker | 參採 |
| `ALE_WhitePaper_v3.1_DOI_Review_v1.0.0_codex.md` | Codex | v3.1 PDF、證據、命名、技術範例與 metadata 終檢 | **NO-GO → 建議 v3.2** |

> 🟥 **2026-06-21 第二輪 Codex DOI 前審:NO-GO,3 個 P0 經作者讀原文查證屬實**——(1) 名稱撞 arXiv:2509.06216 的 ALE;(2) 漏 Code-A1 直接 prior art;(3) 誤讀 2512.03097。**已全數修正 → 白皮書 v3.0**;**G1/G3/G5 重新開啟**(撞名/prior-art/誤讀影響收斂、審閱、盡調)。教訓入 `07_Lessons_Learned`。
>
> 🟥 **2026-06-22 v3.1 DOI 終檢仍為 NO-GO**——新增發現包括：ALE 對外命名與稿內「internal codename」矛盾、v3.0/v3.1 metadata 不一致、§7.7 去重測試無法觸發缺陷，以及 4.5× 事件的 post-hoc PASS 被寫得過強。詳見最新 Codex 審查。
> ⚠ 紀錄:Gemini 案例研究稿曾放**虛構稽核日誌**,經查核**否決**,改用真實輸出。審閱有產出,但**定生死靠查核**。

---

## B. 其他作者 / 外部建議（持續累積)

> 共同作者、領域專家、潛在 venue 審稿人之建議放這裡。每則用下列格式,並標「是否採納 + 去哪一稿」。

```md
### YYYY-MM-DD · 來源(姓名/角色)
- 建議:...
- 我方判定:採納 / 部分採納 / 不採納(理由)
- 落點:回寫到 02_Drafts vX.Y / 04_Evidence / 05_DueDiligence 哪一節
```

_(目前尚無外部作者建議;有了即按上格填。)_

---

## C. ✅ Gate-Review Checklist — G3（審閱關卡)

- [x] 收到 ≥1 份**獨立**審閱(非自審)
- [x] **過度宣稱**已校準(Codex P0:絕對措辭移除、主張降為假說)
- [x] 審閱「好的部分」已採納進主稿(v2.4 / v2.5)
- [x] **造假/錯誤已攔截**(Gemini 虛構日誌 → 否決,改真實輸出)
- [x] 審閱稿保留作軌跡(不刪)
- [ ] (持續)新進外部/同行建議已分流回各稿

> 規則(G3):**審閱意見未收斂、或有未處理的造假/過度宣稱,不進證據階段(G4)。**
