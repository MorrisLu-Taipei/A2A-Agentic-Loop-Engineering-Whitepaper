# EXP-001 實驗卷宗：Test Collusion 受控實驗

> **定位修正**:EXP-001 是**子實驗**——只驗證主實驗 `../EXP-002_Skill_Capitalization_Loop/` 之中「V&V 關卡是否真可驗證、不自我欺騙」(對應 EXP-002 的假說 H5)。主軸是 Skill Capitalization Loop,本實驗服務於它的「可驗證性」。發票去重 task(T01)是這裡的一個 seeded 缺陷,**不是**整個研究的主題。

**目標**:用受控實驗,直接量測「測試從**實作**生成 vs 從**規格**生成」「同模型 vs 異模型」「有/無**機械閘**」在 false-pass、缺陷攔截率與成本上的差異——把白皮書 §7.2 的**研究假說**驗成或證偽。
**對應**:協定 `../../ALE_EXP-001_Protocol_v2.md`、白皮書 `../../../02_Drafts/ALE_WhitePaper_v2.5.md` §7/§9.7/§10/§12.2
**這份卷宗的關卡**:過此實驗 = 卷宗 **G4** 過關。
**鐵則**:全程 Docker(`docker compose`),不依賴本機(對齊 ALE §9.4)。

> 本卷宗依五段推進:**① 實驗設計 → ② 計畫 → ③ 實作/數據 → ④ 假設與驗證 → ⑤ 結果與結論**。③ 的數據與 ⑤ 的結論為**待填模板**,執行後回寫。

---

## ① 實驗設計（Design)

### 對照組(同一批植入缺陷的任務,跑五組)
| 組 | 開發(PG) | 驗證(V&V)可見 | 驗證方式 |
|---|---|---|---|
| **A** 同模型同脈絡 | Model X | 規格＋**實作**＋PG 推理 | 同模型生成 unit tests |
| **B** 異模型同脈絡 | Model X | 規格＋**實作** | Model Y 生成 unit tests |
| **C** 規格隔離 | Model X | **僅規格＋acceptance criteria** | Model Y 生成 tests |
| **D** 機械閘 | Model X | 僅規格＋不變量 | C ＋ 突變≥0.80 ＋ 性質測試 |
| **E** 人類 Golden | Model X | — | 跑人工 golden tests |

### 主要量測
`false-pass rate`(有缺陷卻全綠)、`defect detection rate`、`escaped defects`、`mutation score`、`requirement coverage`;次要:覆蓋率、token/時間/成本、flaky。

### 控制變項
固定模型版本、`temperature=0`、prompt 模板(git hash)、任務/缺陷/環境;每條件 **≥3 次**;**測試生成後才揭露 golden**;全程保留 prompt/code/test/log/hash。

---

## ② 計畫（Plan)

| 階段 | 內容 | 產物 | 狀態 |
|---|---|---|---|
| P0 凍結設計 | 本卷宗 + 協定 v2 | `README.md` | ✅ |
| P1 任務集 | 20–30 題,各植 2–4 缺陷 + golden + 不變量 | `tasks/T*/` | 🟡 T01 已建(發票去重),其餘待擴 |
| P2 容器化 runner | Docker 內跑 5 組 × N 題 × 3 次 | `build/`,`runner/` | 🟡 skeleton 已建,待接模型端點 |
| P3 Pilot | 先跑 A/C/D/E × T01–T05 | `metrics/raw_results.json` | ⬜ 待執行 |
| P4 分析 | paired 分析 + 效果量 | `results/report.md` | ⬜ |
| P5 回寫 | 更新白皮書 §7/§9.7/§10/§12.2 | drafts v2.6 | ⬜ |

**需要的決策(見本檔末「待你拍板」)**:用哪些模型(X/Y)、任務數、是否現在跑、預算上限。

---

## ③ 實作與數據（Implementation & Data)

### 目錄
```
EXP-001/
├── build/Dockerfile         # python3.11 + pytest-cov + mutmut + hypothesis
├── docker-compose.yml       # runner 服務(掛 .env 模型端點)
├── run.sh                   # 一鍵:build → run → analyze
├── tasks/T01_invoice_dedup/ # 真實 seeded task(發票去重膨脹)
│   ├── spec.md              # 需求 + acceptance criteria
│   ├── spec_invariants.md   # 系統級紅線(上界不變量)
│   ├── defects.md           # 已植入缺陷清單
│   └── golden_tests/test_golden.py
├── prompts/{developer,verifier}_prompt.md
├── runner/run_experiment.py # 產碼→產測→執行→量測(skeleton,待接 API)
├── runner/analyze_results.py# paired 分析 + 效果量(skeleton)
├── metrics/                 # raw_results.json 產出處
└── results/RESULTS_TEMPLATE.md  # ④⑤ 待填
```

### 模型端點(保密設計)
runner 只認**通用 OpenAI 相容端點**(`OPENAI_BASE_URL`/`OPENAI_API_KEY` 由 `.env` 注入),不綁特定服務。`.env` 不入 git。

### 執行(待接模型後)
```bash
cp .env.example .env   # 填模型端點
./run.sh               # docker compose:build → run_experiment → analyze
```

> **數據區(待 Pilot 後填)**:`metrics/raw_results.json`、`results/report.md`。

---

## ④ 假設與驗證（Hypotheses & Decision Rules)

| 假說 | 對應白皮書 | 量測 | **判定規則** |
|---|---|---|---|
| **H1** 從實作生成測試 → 更高 false-pass | C1/§7.1 | FPR(A,B) vs FPR(C) | 若 FPR(A)、FPR(B) 顯著 > FPR(C) ⇒ **支持** |
| **H2** 換模型降 variance 不降 bias | C5/§7.2 | FPR(A) vs FPR(B) | 若 FPR(B)≈FPR(A) ⇒ 支持;**若 FPR(B)≪FPR(A) ⇒ 推翻,須改寫 §7.2** |
| **H3** 機械閘把逃逸缺陷壓到近零 | C2/C6/§7.3,§7.7 | escaped defects(D) | 若 D 之 escaped ≈ 0 ⇒ 支持 |
| **H4** 防禦愈強成本愈高 | §9.6 | token/時間(各組) | 描述成本-效益曲線 |

**誠實前提**:小樣本 pilot 以描述統計 + 個案追蹤為主,**不過度宣稱統計顯著**;結果無論支持或否定,**都回寫白皮書**。

---

## ⑤ 實踐結果與結論（Results & Conclusion）— 待 Pilot 後填

> 模板見 `results/RESULTS_TEMPLATE.md`。執行後在此摘要:各組 FPR/攔截率/成本、H1–H4 判定、對 §7/§9.7 的修訂。

| 組 | FPR | defect detection | escaped | mutation | 成本 |
|---|---|---|---|---|---|
| A | _ | _ | _ | _ | _ |
| B | _ | _ | _ | _ | _ |
| C | _ | _ | _ | _ | _ |
| D | _ | _ | _ | _ | _ |
| E | _ | _ | _ | _ | _ |

**結論**:_(待填)_　**白皮書回寫**:_(待填)_

---

## 待你拍板（執行前的決策)
1. **模型**:X(開發)與 Y(驗證)用哪兩個?(建議:不同家以測「異模型」效果;經通用相容端點)
2. **規模**:Pilot 先跑幾題?(建議 T01–T05 × A/C/D/E × 3 次)
3. **現在跑還是先擴任務集**?(T01 已可跑單題 demo)
4. **預算上限**(token/時間)做為 circuit breaker。

> 給我這四項,我就把 runner 接上端點、產 `.env.example`、跑 pilot 並回寫 ⑤。
