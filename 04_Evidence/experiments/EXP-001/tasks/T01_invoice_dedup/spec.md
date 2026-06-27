# T01 · 通路發票張數聚合（spec + acceptance criteria）

> 真實取材:電子發票案的 4.5x 膨脹 bug(`06_Product/04_EInvoiceDashboard` LESSONS #2/#3)。

## 需求（Requirement)
實作 `aggregate_channel_counts(records, year_month)`:
- 輸入 `records`:由分頁 API 取得的發票列(list[dict]),每列含 `id`(唯一鍵)、`invoice_ym`(YYYYMM)、`channel`、`count`(該列張數,>0)。
- 輸入 `year_month`:目標月份字串(YYYYMM)。
- 輸出:該月**各通路**的發票張數加總 `dict[channel] -> int`。

## 驗收準則（Acceptance Criteria)
1. **去重**:`records` 可能含**完全重複的列**(分頁未穩定排序所致);相同 `id` 只能計一次。
2. **月份過濾**:只計 `invoice_ym == year_month` 的列。
3. **加總正確**:每通路輸出 = 該通路、該月、去重後的 `count` 總和。
4. **例外處理**:`count` 為負或缺漏 → 視為無效輸入,**拋出 `ValueError`**(不可默默當 0 或回 None)。
5. **空輸入**:無符合列 → 回空 dict `{}`(不可拋例外)。
