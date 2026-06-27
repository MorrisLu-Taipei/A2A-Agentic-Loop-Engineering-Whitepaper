# ALE 投稿與發表策略

**作者 / Author**：Morris（虎智科技 TigerAI）
**文件類型 / Type**：Publication & Venue Strategy（投稿路線圖）
**版本 / Version**：v1
**日期 / Date**：2026-06-21
**對應**：`ALE_WhitePaper_v2.3.md`、`ALE_PriorArt_RelatedWork_v1.md`、`ALE_CaseStudy_EInvoice_v1.md`

> 核心前提:ALE 目前是**框架(framework)+ N=1 案例研究**,**尚無受控實證**(RQ3 技能重用降本無資料)。此成熟度決定投稿分層——頂級實證期刊現狀投必被「缺 evaluation」退稿,故採「先拿 DOI → 投實務/vision venue → 補實證 → 投全文期刊」的階梯。

---

## 0. 一句話路徑

> **Zenodo DOI(本週)→ IEEE Software 或 AIware/FORGE(首投)→ 補實證(第二案例 + 量化)→ JSS/IST 全文期刊。**
> 切勿把現狀直接送 IEEE TSE / ACM TOSEM / ICSE 主軌。

---

## 1. Tier 0｜先拿 DOI（立即,建立優先權）

| 管道 | 作用 | 備註 |
|---|---|---|
| **Zenodo** | 上傳白皮書即發 DOI,**最快** | 顧問方法論系列已用同套路;附 `CITATION.cff` + `LICENSE` |
| **arXiv `cs.SE`** | 預印本時間戳,搶「test collusion / 機械閘」公開優先權 | 不影響後續投期刊;需 endorsement 時走 cross-list |

**動作**:先做這層,鎖定原創時間點,再從容投正式 venue。授權建議文件用 **CC BY 4.0**;程式/範本沿用既有 Apache 2.0。

---

## 2. Tier 1｜現狀（框架+案例）最容易中的 venue

| Venue | 類型 | 為何適合 | 注意 |
|---|---|---|---|
| **IEEE Software** | 雜誌(magazine) | 接受 framework / experience report / 治理觀點,實務導向,不強求大規模實驗 | 篇幅短、重可讀性。**建議正式首投** |
| **AIware** | ACM 研討會（AI-powered Software Engineering） | 2024 新辦,主題正中靶心,對 vision / early-results 友善 | 查當年 CFP 截止日 |
| **FORGE** | IEEE/ACM 研討會（AI Foundation Models & SE） | 專收 LLM × SE | 查 CFP |
| **ICSE — NIER track** | New Ideas and Emerging Results | 允許未完成大評估的新點子 | **勿投 ICSE 主軌**(缺 eval 必退) |
| **ICSE — SEIP track** | Software Engineering in Practice | 實務導入經驗(電子發票案可當主體) | 同上 |
| LLM-agent / DevSecOps **workshop** | 工作坊 | 拿審稿意見、練 related work | 影響力低,當熱身 |

---

## 3. Tier 2｜補完評估後投全文期刊

**前置條件(先補 §10 Evaluation Plan)**:
- 把電子發票案的 test collusion **量化**(逃逸缺陷數、機械閘攔截率)。
- 加**第二個專案**,提供 RQ3(技能重用降本:lead time / rework / reuse rate)資料。
- 可選:跑一次突變測試,提供 §9.6 成本數據。

| 期刊 | 取向 | 備註 |
|---|---|---|
| **Journal of Systems and Software (JSS)** | 廣納框架類 + 實證 | 對框架+案例相對友善 |
| **Information and Software Technology (IST)** | SE 方法與實證 | 同上 |
| **Automated Software Engineering**（Springer） | 自動化 SE | 多代理人自動化主題契合 |
| **Empirical Software Engineering (EMSE)** | 重實證 | 需較硬的對照研究 |

---

## 4. Tier 3｜頂級（需完整實證,先別投）

IEEE **TSE**、ACM **TOSEM**、**ICSE / FSE / ASE** 主軌——皆要求受控實驗與可重現結果。**現狀投必退**;待 Tier 2 實證成熟後再評估。

---

## 5. 橫切選項｜治理 / 可信 AI 角度

ALE 的地端、受監管、醫療定位,可另投治理社群:
- **ACM FAccT**（Fairness, Accountability, Transparency）
- **AAAI / AIES**（AI, Ethics, and Society）
- **ACM Journal on Responsible Computing**

> 角度切換:對這些 venue,主打「**自主代理人接手驗證時的問責與可稽核性**」,而非 SE 工程細節。

---

## 6. 不適合 / 避雷

- **HRDR（Human Resource Development Review）**:上集顧問方法論投此處,但 ALE 是技術 SE,**讀者不對,勿投**。
- **ICSE / FSE / TSE / TOSEM 主軌(現狀)**:缺受控評估,必退。
- 任何要求「已部署規模證據」的 venue:待第二案例後再說。

---

## 7. 投稿前檢核清單

- [ ] 名稱拍板(見 `ALE_PriorArt_RelatedWork_v1.md` §3 三選項)。
- [ ] 併入 §2.7 Related Work(loop engineering / collusion 文獻),出白皮書 **v2.4**(保留 v2.3)。
- [ ] §7.6 guardrails 就地引用 loop engineering 來源;§7.2 引 arXiv:2512.03097——其「verifier 錨定外部基準可有效防禦」之發現支持本文取向(⚠ 勿誤述為「verifier 不足」,原文相反)。
- [ ] **逐筆核對所有 arXiv 編號與年份**(抓取所得日期有不一致,務必上 arxiv.org 驗證)。
- [ ] 補 `CITATION.cff`、`LICENSE`(CC BY 4.0)、版本沿革(v2.0→v2.1→v2.3 作原創演進證據)。
- [ ] 依目標 venue 調整格式(IEEE / ACM 模板、字數、匿名與否)。
- [ ] 上 Zenodo 取 DOI。

---

## 8. 時間軸建議（粗略）

| 階段 | 內容 | 時點 |
|---|---|---|
| 即刻 | 名稱拍板 + v2.4(併 Related Work)+ Zenodo DOI + arXiv | 本週 |
| 首投 | IEEE Software 或 AIware/FORGE | 查 CFP 後 1–2 月內 |
| 補實證 | 第二案例 + 量化(RQ3) | 並行進行 |
| 全文 | JSS / IST 投稿 | 實證成熟後 |

---

*— End of Publication Strategy v1 —*
