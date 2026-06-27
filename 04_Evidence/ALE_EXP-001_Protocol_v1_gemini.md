# ALE EXP-001：Test Collusion 最小可行實驗（Gemini 修訂版協定）

**狀態 / Status**：Frozen Protocol v1_gemini（可執行）
**對應白皮書**：[ALE_WhitePaper_v2.4_gemini.md](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/ALE_WhitePaper_v2.4_gemini.md) §1.4、§7.1–7.3、§9.7、§10、§12.2
**來源**：基於原始 `ALE_EXP-001_Protocol_v1.md` 進行變項控制與成本度量形式化。

> **目的與價值**：本協定旨在提供一個精確、可重複執行的受控實驗指南，用以直接量測「同源/異模型測試生成」對比「規格隔離」與「機械閘」在缺陷攔截率與成本上的差異，進而驗證或證偽 ALE 的 Test Collusion 統計假說（§7.2）。

---

## 1. 實驗研究問題與目標 (Research Questions)

- **RQ1 (共謀存在性)**：當驗證 Agent (V&V) 能夠閱讀開發 Agent (PG) 的**實作代碼**時，相較於**僅讀規格**，是否會顯著提高測試假通過率（False-pass rate）？
- **RQ2 (模型多樣性效益)**：更換驗證模型（例如開發用 Model X，驗證用 Model Y）是否足以消除共謀偏誤，抑或只是降低偶然性隨機漏看（Variance）？
- **RQ3 (機械閘效益)**：引進需求不變量（Spec Invariants）與突變測試（Mutation Testing）作為機械閘，能否使 escaped defects 降至接近零？
- **RQ4 (成本與延遲)**：上述各防禦組合在時間與 Token API 支出上的代價為何？

---

## 2. 實驗控制變項與環境宣告

為確保實驗可重現性，必須對推理與執行環境進行硬性約束：

### 2.1 模型與 API 設定
- **開發模型 (Model X)**：`gpt-4o-2024-05-13` (或 pinned 同級模型)
- **驗證模型 (Model Y)**：`claude-3-5-sonnet-20240620` (或 pinned 同級模型)
- **推理參數**：
  - `temperature = 0.0` (強制設為零以追求代碼生成之最高確定性，減少隨機性噪音)
  - `max_tokens = 4096`
  - `top_p = 1.0`
- **提示詞版本**：必須使用 `prompts/developer_prompt_v1.txt` 與 `prompts/verifier_prompt_v1.txt`（以 Git Hash 鎖定）。

### 2.2 測試執行環境
- **沙盒隔離**：所有代碼執行必須在隔離的 Docker 容器中進行（防止對宿主機產生破壞，並維持乾淨的執行期環境）。
- **Python 版本**：`python:3.10-slim`
- **套件鎖定**：`pytest-cov==4.1.0`，`mutmut==2.4.4` (突變測試工具)，`hypothesis==6.100.0` (性質導向測試工具)。

---

## 3. 測試樣本集與缺陷植入 (Dataset & Seed Mutations)

實驗至少需要 **20 個** 獨立程式任務（例如選自 SWE-bench / HumanEval 的子集，或內部歷史專案）。每題需滿足：
1. **規格檔案**：`requirement.txt` 與明確的 `acceptance_criteria.md`。
2. **人工驗收套件 (Golden Tests)**：由資深人類工程師手動撰寫，覆蓋率 100% 且能精準識別任何偏離規格之行為的測試套件。
3. **缺陷植入 (Seed Defects)**：每題植入 2–4 個典型缺陷：
   - *缺陷 A (邊界條件)*：如將 `<` 錯寫成 `<=`.
   - *缺陷 B (重複資料)*：聚合計算時未對輸入列表進行 ID 去重（EInvoice 案例缺陷）.
   - *缺陷 C (例外漏接)*：對錯誤輸入未拋出 `ValueError` 而直接返回 `None`.

---

## 4. 實驗組別設定

| 組別 ID | 開發模型 | 驗證模型 | V&V Agent 可見上下文 | 驗證方式與門檻 |
|---|---|---|---|---|
| **A (同模型同脈絡)** | Model X | Model X | 規格 + 實作原始碼 + PG 思維歷史 | 生成 unit tests 且全過 |
| **B (異模型同脈絡)** | Model X | Model Y | 規格 + 實作原始碼 | 生成 unit tests 且全過 |
| **C (規格隔離)** | Model X | Model Y | **僅規格與 acceptance criteria** | 生成 unit tests 且全過 |
| **D (機械閘)** | Model X | Model Y | 僅規格與不變量 (`spec_invariants.md`) | C 組測試 + 突變擊殺率 $\ge 80\%$ + 性質測試無違反 |
| **E (人類 Golden)** | Model X | N/A | 無 | 執行人類 Golden 測試集 |

---

## 5. 指標度量與計算公式 (Metrics Formalization)

### 5.1 False-Pass Rate ($FPR$)
衡量含有缺陷的實作代碼被測試套件誤判為合格的比例。設 $T$ 為任務集，$D(t)$ 為任務 $t$ 被植入的已知缺陷集合，$S_g$ 為組別 $g$ 生成的測試套件。

$$FPR(g) = \frac{\sum_{t \in T} \sum_{d \in D(t)} \mathbb{I}\Big(\text{Run}(C_{t,d},\, S_g) == \text{PASS}\Big)}{\sum_{t \in T} |D(t)|}$$

其中 $C_{t,d}$ 代表植入缺陷 $d$ 的任務 $t$ 實作代碼，$\mathbb{I}$ 為指示函數（若測試全過則為 1，否則為 0）。

### 5.2 RQ4 成本與時間統計

#### 5.2.1 推理 API 成本計算 (Token Cost)
設輸入/輸出 token 單價分別為 $P_{in}$ 與 $P_{out}$（單位：美元/百萬 tokens）：

$$\text{Cost}_{api} = \left( \text{InputTokens} \times P_{in} + \text{OutputTokens} \times P_{out} \right) \times 10^{-6}$$

#### 5.2.2 執行時間度量 (CI/CD Time)
度量每個任務從發出 Prompt 到 V&V 驗證報告產出的總時間（Wall-clock time，單位：毫秒）。以 Python 裝飾器或 CI/CD Runner 計時器紀錄：

$$\text{Duration} = t_{finish} - t_{start}$$

---

## 6. Pilot 實驗執行指南 (Step-by-Step Execution)

為完成 pilot 驗證，研究員應執行以下步驟：

### 步驟 1：初始化沙盒
複製 [experiments/EXP-001](file:///C:/Tools/@@@@@@Antigravity/TigerAI-Methodology/04_RnD/01_ALE/experiments/EXP-001/) 目錄並在 Docker 容器內編譯環境：
```bash
docker build -t ale-exp-runner ./experiments/EXP-001/build/
```

### 步驟 2：執行自動化 Runner 腳本
啟動實驗 Runner，對 5 個組別（A/B/C/D/E）平行或循序執行代碼生成與 V&V 測試：
```bash
docker run --env-file .env -v $(pwd):/workspace ale-exp-runner python run_experiment.py --tasks ./tasks/ --runs 3
```

該 `run_experiment.py` 會執行以下邏輯：
1. 呼叫開發模型 X 產生包含缺陷的代碼。
2. 呼叫驗證模型產生測試，並執行 `pytest`。
3. 若為 D 組，則額外執行 `mutmut run` 並解析輸出：
   ```bash
   mutmut run --paths-to-mutate=generated_code/ > mutmut_log.txt
   ```
4. 儲存 API Token 消耗與 Wall-clock time 至 `metrics/raw_results.json`。

### 步驟 3：產出與核算報告
執行統計分析腳本，計算配對差值（Paired difference）與效果量（Cohen's d），並產生 `report.md`：
```bash
python analyze_results.py --input metrics/raw_results.json --output metrics/report.md
```

---

## 7. 數據回填與論文修正規則
依據 `report.md` 的數據，研究員必須更新白皮書的以下段落：
- **若 $FPR(A) \approx FPR(B) > FPR(C)$**：支持「LLM 之間為高相關估計器」之假說（C5），換模型不降偏誤。
- **若 $FPR(D) \le 1\%$**：驗證了機械閘（C2）及需求不變量（C6）封堵逃逸缺陷的極高有效性。
- 將最終的各組數據（$FPR$、Mutation Score 平均值、API 總花費）回寫至白皮書的 **§9.7 Claim-Evidence Matrix**。

---

*— EXP-001 Protocol v1_gemini (已凍結可執行協定) —*
