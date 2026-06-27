# 創新性 × 研究價值 評估卡（Novelty & Research-Value Assessment）

> 目的:把「我們到底查了沒、新穎性到哪、研究價值確認到哪」一次講清楚。服務投稿 novelty statement,也誠實標出**已驗 vs 候選 vs 未確認**。
> 檢查點對應:**創新性主張**=`01_Consolidation`(G1);**創新性驗證**=本檔 + `ALE_PriorArt_RelatedWork_v2.md`(G5);**研究價值實證**=`04_Evidence`(G4)。
> 一句話現況:**「可能是新的」查了(候選);「真的有用」還沒(待 G4)。**

---

## Part 1 · 創新性(Novelty)— 逐貢獻盤點

評分欄:**新穎度**(Novel 全新 / Specialization 特化 / Integration 整合既有 / Public 公共財)、**證據等級**、**狀態**。

| # | 主張的貢獻 | 對照誰(prior art) | 新穎度 | 證據等級 | 狀態 |
|---|---|---|---|---|---|
| C-A | **shared-context false pass** 整合進完整 SDLC 治理(早期稱 test collusion) | **Code-A1 [2603.15611] 已提 code/test self-collusion**;multi-agent collusion [2512.03097];test oracle [Barr 2015] | **Integration**(⚠ 現象與命名**非**原創,降級) | `[研究假說]` | 候選;**不再宣稱命名/特化原創**;貢獻在「整合進 SDLC」 |
| C-B | **以可執行證據取代模型共識**作 release gate | mutation/property/metamorphic(經典);**2512.03097 正確解讀:外部證據 verifier 有效**(非「verifier 不足」) | **Integration** | `[設計原則]`/`[研究假說]` | 候選;與 PDD/formal verification 接近,須擴查 |
| C-C | **Skill Capitalization + 去退化 FSM 治理**:案例→可重用可驗證 Skill,loop 重複 | agentic SWE roadmap(2509.06216)聚焦生成;少有完整治理迴圈 | **Integration** | `[研究假說]` | 候選;待 EXP-002 Loop 1/2 |
| C-D | **三層驗證整合進完整 Agentic SDLC**(機械閘/模型評議/人類審證據) | DevOps/DevSecOps;loop engineering(公共) | **Integration** | `[設計原則]` | 候選;架構主張 |
| — | agent loop / guardrails / mutation testing 本身 | loop engineering、DeMillo 1978 等 | **Public(讓出)** | — | 不主張原創,已引用 |

**創新性小結**:本研究的可辯護新意是 **C-A 特化 + C-B/C-C/C-D 整合**;**沒有**宣稱發明 loop/guardrail/mutation/collusion 大現象。全部標「候選」,因 (i) 檢索未窮盡、(ii) 待實證升級。

---

## Part 2 · 研究價值 / 顯著性(So-What)

| 維度 | 評估 | 確認狀態 |
|---|---|---|
| **問題重要嗎?** | AI 接手驗證後「綠燈但崩潰」是真實且擴大中的風險(發票案親歷 + 2512.03097 + **Code-A1 self-collusion** 等文獻) | ✅ 問題真實(且已有多篇獨立文獻佐證) |
| **誰在意?** | 地端/受監管企業(醫療/金融/製造)、導入 Agentic SDLC 的工程組織、CIO/工程主管 | ✅ 受眾明確 |
| **填補什麼缺口?** | 既有研究多聚焦「生成能力」;ALE 補「生成之後的治理與可驗證性」 | ✅ 缺口清楚 |
| **解法有效嗎?**(核心價值) | 機械閘真的勝過模型共識?技能資產化真的降本? | ❌ **未確認**(待 G4:EXP-001/EXP-002) |
| **效果量多大?** | false-pass 降幅、lead time/rework 降幅、邊際成本曲線 | ❌ **無數據** |
| **可重現嗎?** | 協定凍結、Docker、固定種子;但尚未實跑 | 🟡 設計可重現,結果未產 |

**研究價值小結**:**問題價值、受眾、缺口都成立(✅);但「解法有效、效果多大」這個最關鍵的價值,目前是 0 數據(❌)。** 這正是 G4 要補的,也是為何現在只能發**預印本**、不能投正式期刊。

---

## Part 3 · 綜合判定

- **可現在誠實主張的**:問題真實、定位清楚、可辯護的**候選**新穎性(特化 + 整合)。
- **還不能主張的**:任何「已驗證的有效性 / 效果量 / 普遍性」。
- **對外措辭**:一律「候選貢獻 / 研究假說 / 初步證據」,不用「首創 / 證實 / 無懈可擊」。

---

## Part 4 · 要把「候選」升「確立」還缺什麼

1. **窮盡化 prior-art**(升 G5):擴大檢索平台/query、補非 arXiv 文獻全文核驗、記錄納入排除。→ 提高「新穎性」信心。
2. **跑 EXP-001**(test collusion):spec-gen vs impl-gen false-pass → C-A/C-B 從假說變數據。
3. **跑 EXP-002 Loop 1(+2)**:降本/可組裝/邊際成本 → C-C 從假說變數據(並讓 skill 升 Certified)。
4. **效果量回報**:不只「有差」,要回報幅度 + 信賴區間(小樣本以描述統計 + 個案)。

> 完成 1 = G5 過;完成 2+3 = G4 過 → 才談正式投稿(G6)。

---
*此卡隨 prior-art 擴查與 EXP-001/002 結果更新;與 `ALE_PriorArt_RelatedWork_v2.md`(對照矩陣)、`../02_Drafts` §1.5/§9.7 對齊。*
