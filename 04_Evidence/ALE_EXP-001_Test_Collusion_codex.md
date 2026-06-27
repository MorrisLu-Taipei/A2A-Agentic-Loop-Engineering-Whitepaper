# ALE EXP-001：Test Collusion 最小可行實驗

**對應文件**：`ALE_WhitePaper_v2.3.md` §1.4、§7、§10、§12.2  
**目的**：直接量測不同測試生成條件下的 false-pass、缺陷攔截率與成本，避免只以單一案例外推 AI-to-AI test collusion。

## 1. 研究問題

- RQ1：從實作生成測試，是否比從規格生成測試產生更高的 false-pass rate？
- RQ2：更換模型是否足以降低共享錯誤？
- RQ3：加入 spec invariants、property tests 與 mutation testing 後，escaped defects 是否下降？
- RQ4：各種驗證組合增加多少時間與運算成本？

## 2. 最小樣本

- 20–30 個小型、可容器化的程式任務。
- 每題具明確規格、acceptance criteria 與人工確認的 golden tests。
- 每題植入 2–4 個已知缺陷，包含：
  - 邊界條件
  - 錯誤聚合
  - 重複資料
  - 權限繞過
  - 例外處理
  - 規格遺漏

## 3. 實驗組

| 組別 | PG | V&V 可見內容 | 驗證方式 |
|---|---|---|---|
| A 同模型同脈絡 | Model X | 規格＋實作＋PG reasoning | 生成 unit tests |
| B 異模型同脈絡 | Model X | 規格＋實作 | Model Y 生成 unit tests |
| C 規格隔離 | Model X | 僅規格與 acceptance criteria | Model Y 生成 tests |
| D Mechanical Gate | Model X | 規格隔離 | C＋invariants＋property tests＋mutation |
| E Human/Golden Baseline | Model X | 人工確認測試 | golden tests |

若預算有限，先執行 A、C、D、E。

## 4. 控制變項

- 固定模型版本與推理設定。
- 固定 prompt template。
- 固定 task、缺陷與執行環境。
- 每個條件至少重複 3 次，以觀察取樣變異。
- 測試生成完成後才揭露 golden tests。
- 保留完整 prompt、response、code、test、log 與 hash。

## 5. 指標

### 主要指標

- False-pass rate：有缺陷但生成測試全數通過的比例。
- Defect detection rate。
- Escaped defects。
- Mutation score。
- Requirement coverage：需求條款對應至少一個測試的比例。

### 次要指標

- Line / branch coverage。
- 測試數量與 assertion 數量。
- Wall-clock time。
- Token / API / CI cost。
- Flaky test rate。
- 人工覆核時間。

## 6. Test Collusion 的操作型定義

當以下條件同時成立，記為一次 candidate collusion event：

1. 實作包含已知缺陷。
2. V&V 產生的測試全部通過。
3. Golden test 或獨立不變量能穩定揭露該缺陷。
4. 失敗可追溯至測試沿用了實作的錯誤假設、資料來源或錯誤轉譯。

不要僅因測試漏抓 bug 就稱為 collusion；需證明存在共享錯誤來源。

## 7. 分析方法

- 比較各組 false-pass rate 與 defect detection rate。
- 以 task 為配對單位，優先採 paired analysis。
- 回報效果量與信賴區間，不只回報平均值。
- 將缺陷類型分層，觀察哪些錯誤最易產生共享假通過。
- 分析 A→B 是否只降低 variance，C/D 是否降低 shared-source bias。

小樣本 pilot 以描述統計與個案追蹤為主，不過度宣稱統計顯著。

## 8. Evidence 目錄

```text
experiments/EXP-001/
├── protocol.md
├── tasks/
├── defects/
├── prompts/
├── generated-code/
├── generated-tests/
├── golden-tests/
├── execution-logs/
├── metrics/
├── environment.lock
└── report.md
```

每個 artifact 記錄：

- task ID
- condition ID
- run ID
- model/version
- prompt hash
- code hash
- test hash
- environment hash

## 9. Pilot 成功門檻

EXP-001 pilot 不以「證明 ALE 正確」為目標，而以以下條件為成功：

1. Protocol 可重跑。
2. Candidate collusion event 可被第三方由 evidence 重建。
3. A/C/D 組可被一致比較。
4. 指標計算自動化。
5. 結果無論支持或否定假說，都能回寫白皮書。

## 10. 白皮書回寫規則

- 若 A 的 false-pass 顯著高於 C/D：支持共享實作脈絡風險。
- 若 B 與 A 接近：支持「換模型不足」的方向性主張。
- 若 B 明顯改善：修正「多模型只能降 variance」的過強主張。
- 若 D 未改善：檢查 invariant 品質、mutation operator 與 task suitability。
- 不論結果如何，都必須更新 §7、§10 與 §12.2。

