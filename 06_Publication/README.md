# 06 · Publication（投稿・venue・DOI)

**階段目的**:選定 venue、達成投稿要求、取得 DOI、備齊 metadata 與授權,完成發表。
**上一關**:G5(盡職調查通過)｜**下一關**:G6 過關 → 發表。

## ✅ Gate-Review Checklist — G6（投稿 → 發表)

**預印本子路徑(G4 前可並行,鎖優先權)**
- [ ] `CITATION.cff` + `LICENSE(CC BY 4.0)` 備妥
- [ ] Zenodo 上傳取 DOI
- [ ] arXiv `cs.SE` 提交(LaTeX;首投需 endorsement)

**正式發表子路徑(須先過 G4 實證 + G5 盡調)**
- [ ] 名稱/副標 Founder 拍板(metadata 一致)
- [ ] 目標 venue 選定(IEEE Software 首投 / 2027 研討會 / 期刊)
- [ ] 依 venue 重排(IEEE Software 裁 ≤4,200 字 + 3 洞察;研討會用 ACM 模板+匿名)
- [ ] APC 預算確認(走 Gold OA 時)
- [ ] References 零 placeholder、全核驗(承 G5)

> 規則(G6):**venue 要求未達標 / 無 DOI / metadata 不齊,不發表**;預印本可早走,正式 full paper 須先過 G4。

---

本目錄彙整 ALE 白皮書(`../02_Drafts/ALE_WhitePaper_v2.5.md`)可投稿之期刊/研討會的**投稿要求、Impact Factor、APC 費用、截稿日**,並給出**適配分析與建議**。

- **研究日期**:2026-06-21。
- **目錄結構**:本 `README.md`(索引+分析)+ 各 venue 細節檔(`IEEE_Software.md` 等)+ `_raw_snapshots/`(官方頁面原始 HTML 存證)。
- ⚠ **Impact Factor 注意**:同一期刊不同來源(JCR/Scopus/二手站)數字常不一致,本表標明範圍並註來源;**投稿前以官方 JCR(Clarivate)為準**。
- ⚠ **arXiv 編號式 venue 不適用**;此處為正式發表管道。

---

## A. 總覽比較表

| Venue | 類型 | Impact Factor(來源) | 分區 | APC(開放取用) | 投稿模式 | 現狀可投? | ALE 適配 |
|---|---|---|---|---|---|---|---|
| **arXiv `cs.SE`** | 預印本 | — | — | 免費 | 隨時 | ✅ **立即** | 鎖優先權 |
| **Zenodo** | 預印本/DOI | — | — | 免費 | 隨時 | ✅ **立即** | 取 DOI |
| **IEEE Software** | 雜誌(magazine) | ~3.0(2024,另源 2.64) | Q2 | 混合 OA;訂閱為主,OA 選配 | **滾動(隨時)** | ✅ **立即** | ★★★ 最佳近期目標 |
| **JSS**(J. Systems and Software) | 期刊 | 4.1–5.9(來源分歧) | Q1 | ~**USD 3,670**(另源 3,560) | 滾動 | ⚠ 補實證後 | ★★ 框架+案例友善 |
| **IST**(Information & Software Technology) | 期刊 | 4.3(2025-06) | Q1 | **USD 3,890** | 滾動 | ⚠ 補實證後 | ★★ 方法論實證 |
| **EMSE**(Empirical Software Engineering) | 期刊(Springer) | 3.6 | Q1 | ~USD 2,890(OA 選配) | 滾動 | ⚠ 需強實證 | ★★ FORGE 最佳論文轉投處 |
| **Automated Software Engineering**(Springer) | 期刊 | 3.1 | Q1/Q2 | 未查得 | 滾動 | ⚠ 補實證後 | ★ 自動化 SE 主題契合 |
| **AIware 2026** | 研討會(ACM) | —(會議) | — | (會議註冊費) | 年度 | ❌ **截稿已過**(2/15) | ★★★ 主題正中,改投 2027 |
| **FORGE 2026** | 研討會(ACM) | —(會議) | — | (會議註冊費) | 年度 | ❌ **截稿已過**(2025/11/5) | ★★★ 主題正中,改投 2027 |

> 會議 IF 一般不適用(以 CORE rank / 影響力評估);AIware、FORGE 皆為 2024 起新辦、LLM×SE 主題,**最對位但 2026 場次截稿已過**。

---

## B. 關鍵發現(時效性)

1. **兩個最對味的研討會,2026 場次都截稿了**:
   - **FORGE 2026** research papers 截稿 **2025-11-05**(會議 2026-04 Rio);最佳論文獲 ACM SIGSOFT Distinguished + 轉投 **EMSE 特刊**。
   - **AIware 2026** 截稿 **2026-02-15**(會議 2026-07 Montreal,co-located FSE 2026);**全公開 OpenReview 評審**。
   - → 這兩個要等 **2027 場次**(且正好給我們時間做 EXP-001 + 第二案例,full paper 才壓得住)。
2. **現在就能投的正式管道 = IEEE Software(雜誌,滾動)**:框架/實務/治理導向,**不強求大規模實驗**,最適合 ALE 現狀(框架+N=1)。
3. **期刊(JSS/IST/EMSE)滾動可投,但偏好實證**:建議 EXP-001 + 第二案例後再投全文,命中率高。
4. **預印本立即做**:arXiv `cs.SE` + Zenodo DOI,鎖住「test collusion / 機械閘」優先權。

---

## C. 各 venue 投稿要求摘要（細節見同名 .md)

### IEEE Software(雜誌)— 近期首選
- **長度**:正文 ≤ **4,200 字**(每張圖/表計 250 字);摘要 ≤ **150 字**;參考文獻 ≤ **15** 篇。
- **特別要求**:附 **3 條 practitioner 行動洞察**(bullet)。
- **評審**:peer-reviewed;**滾動投稿**。
- **系統**:https://ieee.atyponrex.com/journal/sw-cs
- **OA**:混合(訂閱為主,OA 選配,非強制付費)。
- **對 ALE 的意義**:需把 v2.5 從「完整白皮書」**裁成 ≤4,200 字的雜誌文**,主打 test collusion + 機械閘 + 電子發票案 + 3 條 CIO/工程主管洞察。

### AIware(ACM 研討會)— 改投 2027
- **長度**:full **8 頁** / short(vision)**2–4 頁** / survey **14–20 頁** + 參考 1–2 頁。
- **模板**:ACM `acmart`(`\documentclass[sigconf,review,anonymous]`)。
- **評審**:double-anonymous + **全公開 OpenReview**。
- **2026(已過)**:截稿 2026-02-15、camera 2026-05-07、會議 2026-07-06~07 Montreal。

### FORGE(ACM 研討會)— 改投 2027
- **長度**:full **10 頁** + 參考 2 頁。
- **獎勵**:最佳論文 ACM SIGSOFT Distinguished + **轉投 EMSE 特刊**。
- **2026(已過)**:research papers 截稿 2025-11-05、通知 2026-01-05、會議 2026-04-12~13 Rio。

### JSS / IST / EMSE(期刊)— 補實證後
- **JSS**:Elsevier、`elsarticle` LaTeX、Editorial Manager;APC ~USD 3,670;Q1。
- **IST**:Elsevier;APC USD 3,890;IF 4.3;Q1。
- **EMSE**:Springer;IF 3.6;APC ~USD 2,890;**重實證**(FORGE 最佳論文轉投處)。

### 預印本
- **arXiv `cs.SE`**:免費,需 endorsement(首投)。PDF 由 LaTeX 產出。
- **Zenodo**:免費,**上傳即發 DOI**(CERN 營運),附 `CITATION.cff` + `LICENSE`。

---

## D. 建議路線(對應現狀:框架 + N=1,EXP-001 未跑)

```text
[即刻] arXiv cs.SE + Zenodo(DOI,鎖優先權)
   │
   ├─[並行,本季] 裁成 ≤4,200 字 → 投 IEEE Software(滾動,現狀最佳正式管道)
   │
   ├─[本季起] 執行 EXP-001 + 第二案例(取得 RQ3 重用數據)
   │
   └─[實證成熟後] 二擇一:
        ├─ 研討會路線:AIware 2027 / FORGE 2027(full paper,主題最對位)
        └─ 期刊路線:JSS 或 IST(全文實證);EMSE(若走 FORGE 特刊)
```

**理由**:
- IEEE Software **現在**就能投、且不卡實驗規模 → 先拿一篇 peer-reviewed 露出。
- 研討會主題最對位但 2026 已過、且 full paper 需實證 → 用等待 2027 的時間補 EXP-001。
- 頂級期刊/會議主軌(TSE/TOSEM/ICSE/FSE)現狀勿投(缺受控評估)。

---

## E. 待你決策
1. **是否同時走「IEEE Software 雜誌文」與「期刊全文」雙軌**(雜誌文需另裁短版,不影響期刊全文)?
2. **APC 預算**:JSS/IST OA 約 USD 3,600–3,900;若走訂閱(非 OA)可免費但讀者付費牆。IEEE Software 可不付 OA。
3. 名稱/副標拍板(影響所有投稿 metadata)。

---

## 來源連結(2026-06-21 擷取)
- IEEE Software 作者資訊:https://www.computer.org/csdl/magazine/so/write-for-us/14426 ｜投稿:https://ieee.atyponrex.com/journal/sw-cs
- AIware 2026:https://2026.aiwareconf.org/track/aiware-2026-papers
- FORGE 2026:https://conf.researchr.org/track/forge-2026/forge-2026-papers ｜日期:https://conf.researchr.org/dates/forge-2026
- JSS:https://www.sciencedirect.com/journal/journal-of-systems-and-software
- IST:https://www.sciencedirect.com/journal/information-and-software-technology
- EMSE:https://link.springer.com/journal/10664 ｜ASE:https://link.springer.com/journal/10515
- IF/APC 數據:resurchify / journalmetrics / bioxbio / research.com(二手,**須以官方 JCR 覆核**)

*產製:虎智科技 TigerAI｜投稿要求屬各出版社,以官方頁面為最終依據。*
