# T01 · 系統級紅線不變量（spec_invariants)

這些不變量**與具體實作無關**,餵入機械閘(D 組)的 property-based 測試。即使功能需求寫錯或測試從實作長出來,違反紅線即 FAIL。

## INV-1 物理上界(對應發票案檢查 #3)
任一通路、任一月份的聚合張數,**恆 ≤ 該月全國開立發票總張數**(由獨立基準提供)。
```
sum(result.values()) <= NATIONAL_TOTAL[year_month]
```

## INV-2 去重後不增(蛻變關係)
對**同一份資料**,**加入完全重複的列**後再聚合,結果**不得改變**。
```
aggregate(records) == aggregate(records + duplicate_of(records))
```

## INV-3 非負
所有輸出值 `>= 0`;且若有任何 `count < 0` 的輸入,應在驗收準則 4 被擋下(拋 ValueError)。

## INV-4 過濾單調
`year_month` 篩選更嚴(僅一月)之結果張數,**不得大於**不篩選(全部月)之同通路總和。
