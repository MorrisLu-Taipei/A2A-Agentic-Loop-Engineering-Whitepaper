# ALE 實證案例研究：電子發票開放資料儀表板
## A Preliminary Field Observation of Shared-Source False Passes and Invariant-Based Detection
### 同源驗證假通過與不變量攔截的初步田野案例

---

**作者 / Author**：Morris（虎智科技 TigerAI）
**文件類型 / Type**：Case Study（作為白皮書 §12.2 與 §9.7 Claim-Evidence Matrix 之實證附錄來源）
**版本 / Version**：v2（採納 Gemini 語氣調降;**§4 證據鏈以實際執行輸出取代 v1_gemini 之示意日誌**——後者數字、CLI 與 hash 為虛構,不可作稽核證據。原 v1、v1_gemini 保留）
**日期 / Date**：2026-06-21
**被研究系統**：`06_Product/04_EInvoiceDashboard`

> **學術定位與限制說明**：本案例提供一個與 ALE 假說相符的**事後田野觀察（Post-hoc Field Observation）**。由於這是單一專案的事後對照，並非受控的 A/B 測試或消融實驗，因此其核心價值在於**例示（Illustrates）**核心失效模式的存在，而非**統計學上證明（Proves）**其發生率。此觀察將直接用於支持 `ALE_EXP-001` 受控實驗之設計。

---

## 0. 摘要（案例之學術價值）
電子發票儀表板專案在 ALE 框架成文前即已開發，因此它不是「照著理論做出來的示範」，而是**理論的反向對照**。該專案在開發中經歷了「同源比對假通過（test-collusion analogue）」的失效，並最終透過引進「獨立上界不變量（Spec Invariant）」機械閘成功攔截了金額膨脹 4.5 倍的逃逸缺陷。

---

## 1. ALE 構念 ↔ 本案例觀察對照表

| ALE 構念（白皮書對應章節） | 本案例的對應觀察 | 證據檔案 / 欄位 |
|---|---|---|
| **Test-Collusion Analogue（§7.1）** | 儀表板聚合值 vs 資料庫查詢值同源比對，兩邊皆通過卻同步錯誤、互相背書。 | `LESSONS_LEARNED.md` Lesson #3 |
| **Correlated Estimators 聯合失效（§7.2）** | 「同源資料做自我比對沒有外部基準，錯誤會在兩端同步存在，比對永遠相等」。 | `LESSONS_LEARNED.md` #3 根因分析 |
| **機械閘:不依賴模型意見的事實基準（§7.3）** | `vv_crosscheck.py` 腳本：三道機械檢查，若失敗則 `exit 1` 中止 CI 建置。 | `vv_crosscheck.py`、`build/run_build.sh` |
| **需求不變量 / 蛻變關係（§7.7）** | 檢查 #3「某月消費發票張數 $\le$ 全國開立總張數」= 系統級紅線，與具體實作無關。 | `vv_crosscheck.py` 行 42-58 |
| **跨來源獨立基準（§7.3）** | 檢查 #2「兩份獨立抓取（`_12m` 與 `_24m`）同月唯一鍵集合一致」。 | `vv_crosscheck.py` 行 31-40 |
| **逃逸缺陷被機械閘攔截（RQ2 假說）** | offset 分頁無序回傳重複列導致金額膨脹 4.5 倍，同源比對未抓到，但被上界不變量攔截。 | `LESSONS_LEARNED.md` #2、#3 |
| **Artifact Layer / 證據軌跡（§3.3）** | 四件套交付 + 驗證報告 + 逐階段 DEVLOG。 | `DEVLOG.md` / `SDD.md` / `LESSONS_LEARNED.md` |

---

## 2. 核心觀察一：同源驗證假通過（Test-Collusion Analogue）

### 2.1 現象描述
專案早期為驗證「資料抓取與轉換之正確性」，設計的驗證關卡是比對**前端儀表板的顯示值**與**資料庫 ODS 表的查詢值**。測試報告顯示 `PASS`，但實際總金額與物理常識明顯不符。

### 2.2 根因與統計學對應
這是一個典型的 **test-collusion analogue**。儀表板聚合模組與資料庫查詢模組雖然是兩個獨立的軟體組件，但其**資料來源皆為同一份因 ODS 重複寫入而膨脹的資料**。在統計估計的框架下：

$$\operatorname{Corr}\big(\operatorname{err}(\text{dashboard}), \operatorname{err}(\text{DB query}) \mid \text{Source ODS Data}\big) \longrightarrow 1$$

由於兩估計器在給定同源資料的條件下錯誤相關性極高，一致性的比對結果僅是「互相背書的一致錯誤」，無法揭露底層缺陷。這印證了白皮書 §7.2 的假說：當驗證者與生產者共享偏誤源時，多模型交叉檢查（或多組件比對）無法定生死。

---

## 3. 核心觀察二：機械閘與需求不變量攔截逃逸缺陷

### 3.1 逃逸缺陷：金額膨脹 4.5 倍
消費通路資料抓取 API 採用 offset 分頁，但因後端資料庫**未穩定排序**，導致分頁邊界回傳了大量重複行。這導致 `SUM(invoice_create_amt)` 計算時重複加載，金額比真實值膨脹了 **4.5 倍**。

### 3.2 獨立不變量機械閘之攔截
開發團隊引進了 `vv_crosscheck.py`，其中包含了一條與具體代碼實作解耦的**系統不變量（Spec Invariant）**：

> 系統不變量：任何單一通路的「月消費發票張數」，恆小於或等於財政部公佈的「全國月開立發票總張數」。

雖然 API 抓取的 ODS 數據因重複行導致自身比對全數通過，但當 `computed_invoice_count`（通路張數）因重複累加而遠遠大於全國總量時，物理上界不變量被打破：

$$\text{computed\_channel\_count} > \text{national\_total\_count}$$

不變量檢查立即觸發 `FAIL`，並拋出 `exit 1` 中止建置。

---

## 4. 可稽核證據鏈歸檔 (Audit Trail)

> **誠信註記(v2 更正)**:本案例的 AI 協作初版曾出現一段「FAIL 稽核日誌」,以捏造的數字、不存在的 CLI 參數與假雜湊值**冒充真實執行輸出**。經以一手證據查證(實際執行 `vv_crosscheck.py`)後判定為**虛構**,已**整段移除**;本 v2 一律改放**實際執行輸出**。原始造假稿已隔離至 `_QUARANTINE_DO_NOT_PUBLISH/`(僅作事件存證、不對外發布)。此事件本身收錄為方法論教訓(producer ≠ verifier、evidence > consensus),見 `../07_Lessons_Learned/`。

### 4.1 真實執行輸出（current state，膨脹已修復後)

於專案目錄 `06_Product/04_EInvoiceDashboard/` 實際執行(2026-06-21):

```text
$ python vv_crosscheck.py
== V&V 交叉驗證 ==
  [OK] 消費資料無重複業務鍵
  [OK] 兩來源同月唯一鍵一致(排除邊界月)
  [OK] 消費張數 ≤ 全國開立總量（202604）
    參考:202604 消費張數占全國開立 17.3%（合理應 < 100%)

== 結果:PASS ==
$ echo $?
0
```

說明:現行資料已完成去重修復(見 `LESSONS_LEARNED.md` #2),故三道機械檢查全 PASS、`exit 0`;檢查 #3 之比值 **17.3%**(遠低於 100% 上界)即為「未膨脹」之客觀證據。

### 4.2 歷史 FAIL 為何無法真實重現（誠實限制）

金額膨脹 4.5x **發生於修復前**,當時的膨脹資料快照**未保留**,故**無法產出真實的 FAIL 日誌**。膨脹事件與修復僅有**文字紀錄**:
- `LESSONS_LEARNED.md` #2(offset 分頁重複列 → SUM 膨脹 ~4.5x)
- `LESSONS_LEARNED.md` #3(同源比對假通過 → 改用獨立上界 + 跨引擎)
- `DEVLOG.md`「第二階段」「2026-06-21 V&V 閘」

> **可稽核性的正確主張**:本案例能證明的是「**機械閘#3 此刻確實在運行、且其設計正是為了攔截膨脹**(比值檢查 < 100%)」;**不宣稱**握有當時 FAIL 的逐行 log。若要取得真實 FAIL 證據,須在 EXP-001(`ALE_EXP-001_Protocol_v2.md`)中以受控方式植入重複列缺陷重現。

### 4.3 待補的真實歸檔(投稿前)

如需完整 hash 證據鏈,應對現行檔案計算真實 SHA-256(`vv_crosscheck.py`、`data/*.json`)並附修復 commit hash;本版**不放任何示意 hash**,以免與真實值混淆。

---

## 5. 局限性與威脅效度（Threats to Validity）

1. **N=1 局限性**：本專案為單一對照觀察。其結果僅代表「在此案例中，獨立不變量比同源一致性檢查更有效」，不可外推至所有軟體系統。
2. **工具非 AI 限制**：本案例中，同源比對是由硬編碼的資料庫查詢與儀表板聚合組成，而非由兩個 LLM Agent 自主協同所做。此失效為 test collusion 的**一般化模型對應**，純 AI-to-AI 共謀的數據仍有待 `EXP-001` 的直接量測。
3. **無技能重用數據**：該專案尚未採用 Skill Repository 進行自動組裝，因此無法評估技能資產化（RQ3）對邊際成本的影響。

---

*— Case Study v1_gemini (田野觀察修訂版) —*
