# ALE EXP-001：Test Collusion 最小可行實驗（官方協定）

**狀態 / Status**：Frozen Protocol v1（已凍結,可執行）
**對應白皮書**：`ALE_WhitePaper_v2.4.md` §1.4、§7.1–7.3、§9.7、§10、§12.2
**來源**：採納並正式化 Codex 設計稿 `ALE_EXP-001_Test_Collusion_codex.md`
**日期 / Date**：2026-06-21

> 目的:直接量測不同**測試生成條件**下的 false-pass、缺陷攔截率與成本,以**取代「以單一案例外推 AI-to-AI test collusion」**。本協定凍結後即可執行;pilot 結果不論支持或否定假說,皆回寫白皮書 §7、§9.7、§10、§12.2。

---

## 1. 研究問題（對應白皮書 RQ1/RQ2/C1/C2/C5/C6）

- **RQ1**:從**實作**生成測試,是否比從**規格**生成測試產生更高的 false-pass rate?
- **RQ2**:**更換模型**是否足以降低共享錯誤(換模型 vs 換脈絡,哪個有效)?
- **RQ3**:加入 spec invariants、property tests 與 mutation testing 後,escaped defects 是否下降?
- **RQ4**:各驗證組合增加多少時間與運算成本?

## 2. 最小樣本

- **20–30 個**小型、可容器化的程式任務。
- 每題具明確規格、`acceptance_criteria` 與**人工確認的 golden tests**。
- 每題植入 **2–4 個已知缺陷**,涵蓋:邊界條件、錯誤聚合、重複資料、權限繞過、例外處理、規格遺漏。

## 3. 實驗組（A/B/C/D/E）

| 組別 | PG | V&V 可見內容 | 驗證方式 |
|---|---|---|---|
| **A** 同模型同脈絡 | Model X | 規格＋實作＋PG reasoning | 同模型生成 unit tests |
| **B** 異模型同脈絡 | Model X | 規格＋實作 | Model Y 生成 unit tests |
| **C** 規格隔離 | Model X | **僅規格與 acceptance criteria** | Model Y 生成 tests |
| **D** 機械閘 | Model X | 規格隔離 | C ＋ invariants ＋ property tests ＋ mutation |
| **E** 人工/Golden 基線 | Model X | 人工確認測試 | golden tests |

> 預算有限時,先跑 **A、C、D、E**(B 為「換模型是否足夠」之關鍵對照,資源允許務必納入)。

## 4. 控制變項

- 固定模型版本與推理設定;固定 prompt template;固定 task、缺陷與執行環境。
- 每條件**至少重複 3 次**以觀察取樣變異。
- **測試生成完成後才揭露 golden tests**(避免洩題)。
- 保留完整 prompt、response、code、test、log 與 **hash**。

## 5. 指標

**主要**:false-pass rate(有缺陷但生成測試全過比例)、defect detection rate、escaped defects、mutation score、requirement coverage(需求條款對應至少一測試之比例)。
**次要**:line/branch coverage、測試數與 assertion 數、wall-clock time、token/API/CI cost、flaky rate、人工覆核時間。

## 6. Test Collusion 操作型定義（記為一次 candidate event 須四條同時成立）

1. 實作包含已知缺陷。
2. V&V 產生的測試**全部通過**。
3. Golden test 或獨立不變量**能穩定揭露**該缺陷。
4. 失敗可追溯至測試**沿用了實作的錯誤假設、資料來源或錯誤轉譯**。

> 不可僅因「測試漏抓 bug」即稱 collusion;**須證明存在共享錯誤來源**。

## 7. 分析方法

- 比較各組 false-pass 與 defect detection;以 **task 為配對單位,優先 paired analysis**。
- **回報效果量與信賴區間**,不只平均值。
- 缺陷類型分層,觀察哪類最易產生共享假通過。
- 檢驗:A→B 是否**只降 variance**;C/D 是否**降 shared-source bias**。
- 小樣本 pilot 以**描述統計與個案追蹤**為主,**不過度宣稱統計顯著**。

## 8. Evidence 目錄

```text
experiments/EXP-001/
├── protocol.md
├── tasks/  defects/  prompts/
├── generated-code/  generated-tests/  golden-tests/
├── execution-logs/  metrics/
├── environment.lock
└── report.md
```

每個 artifact 記錄:task ID、condition ID、run ID、model/version、prompt hash、code hash、test hash、environment hash。

## 9. Pilot 成功門檻（不以「證明 ALE 正確」為目標）

1. Protocol 可重跑。
2. Candidate collusion event 可由 evidence 被第三方重建。
3. A/C/D 組可被一致比較。
4. 指標計算自動化。
5. 結果**無論支持或否定假說,皆能回寫白皮書**。

## 10. 白皮書回寫規則（結果 → 修訂）

| 觀察 | 回寫動作 |
|---|---|
| A 的 false-pass 顯著高於 C/D | 支持「共享實作脈絡」風險(C1) |
| B 與 A 接近 | 支持「換模型不足」方向性主張(C5) |
| **B 明顯改善** | **修正** §7.2「多模型只能降 variance」之過強主張 |
| D 未改善 | 檢查 invariant 品質、mutation operator、task 適配 |
| 任一結果 | **必更新** §7、§9.7 Claim–Evidence Matrix、§10、§12.2 |

---

*— EXP-001 Protocol v1（採納自 Codex 設計,凍結可執行）—*
