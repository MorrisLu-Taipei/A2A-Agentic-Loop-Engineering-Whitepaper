# `ALE_CaseStudy_EInvoice_v1.md` Codex 審閱建議

**目標文件**：`ALE_CaseStudy_EInvoice_v1.md`  
**總評**：這是一個有價值的 preliminary field observation，但不是 RQ1/RQ2 的直接受控驗證。

## 一、證據定位

### 可以支持

- 同源資料的交叉一致性檢查可能產生 false pass。
- 外部上界不變量曾實際攔截資料膨脹缺陷。
- 可執行 gate 與 evidence trail 能提升問題可追查性。
- 案例可作為 EXP-001 的現象來源與實驗動機。

### 尚不能支持

- AI-to-AI test collusion 的發生率。
- 不同 LLM 是否具有高度相關的錯誤。
- Mechanical gate 普遍優於 model review。
- SQLite 與 PostgreSQL 的一致結果代表來源資料正確。
- Skill Capitalization 能降低跨專案成本。

## 二、逐段建議

### §0「理論的反向驗證」

**問題**：post-hoc mapping 容易受 confirmation bias 影響。

**建議改寫**：

> 本案例提供一個與 ALE 假說一致的事後田野觀察。它可用於建立研究假說與設計後續受控實驗，但不構成對理論的獨立驗證。

### §2.2「為何是 test collusion」

建議把它命名為：

> test-collusion analogue / 同源驗證假通過案例

理由：本案觀察到的是 dashboard 與 DB query 共享同一污染資料，不是 PG Agent 與 V&V Agent 的直接 AI-to-AI 行為。

### §2.3「本案例獨立證實」

**建議改寫**：

> 本案例提供 test collusion 一般化機制的初步存在性例示：當驗證者與被驗證者共享同一錯誤來源時，一致結果不代表正確。

### §3.3「真正較獨立的估計器」

SQLite 與 PostgreSQL 使用不同執行引擎，但若輸入資料與轉換邏輯相同，仍可能共享來源錯誤。

**建議改寫**：

> 這是一項跨執行引擎的一致性檢查，可降低特定資料庫實作差異造成的風險；它不能取代外部資料基準或需求 oracle。

### §4「本案例支持的主張」

將標題改為：

> 本案例提供的初步證據與研究假說

並把 RQ2 改寫為：

> 在本案例中，獨立上界不變量攔截了同源一致性檢查未攔截的缺陷。

不要外推成所有 mechanical gate 都優於所有 model panel。

## 三、建議補強的證據附件

為提高可稽核性，案例應附：

1. 缺陷前後的原始資料摘要與 hash。
2. `vv_crosscheck.py` 執行命令、環境與完整輸出。
3. FAIL build 的 exit code 與時間戳。
4. 修復 commit 或 patch。
5. 不變量的來源與商業合理性說明。
6. 證據鏈索引，確認每個主張能追到實際檔案。

## 四、推薦案例標題

英文副標建議由：

> Empirical evidence for the Test-Collusion thesis and the Mechanical-Gate architecture

改為：

> A Preliminary Field Observation of Shared-Source False Passes and Invariant-Based Detection

中文可改為：

> 同源驗證假通過與不變量攔截的初步田野案例

這個標題較保守，但更經得起研究方法審查。

