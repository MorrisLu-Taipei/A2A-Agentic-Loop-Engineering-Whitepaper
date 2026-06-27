# Loop 0 · from-scratch Baseline（電子發票案,給 Loop 1 比較用)

> 「降本」是比較出來的。本檔把**發票案(近乎從零做)**整理成 baseline,供 Loop 1(組裝)對照。
> 資料來源:`06_Product/04_EInvoiceDashboard/DEVLOG.md`(非機密,屬產品交付紀錄)。
> ⚠ 誠實限制:當時**未逐項記工時**,故以「階段數 / 交付物 / 踩坑」為 effort 代理(proxy),非精確小時數。Loop 1 起改用計時器精確量。

## Baseline:發票案的 from-scratch 歷程(proxy)

| 階段(DEVLOG) | 做了什麼 | effort proxy / 訊號 |
|---|---|---|
| 第一階段 | 9 資料集抓取 + 聚合腳本 + 六頁注入 + 版型 | 高(從零建管線與模板) |
| 第二階段 | 繞 WAF(TLS 指紋)+ 發現並修金額膨脹 4.5x(去重) | 高(踩坑 + 根因 + 全腳本統一修) |
| 第三階段 | 地圖 + 次月迴歸預估 + 三項 AI 分析 | 高(分析功能從零) |
| 第四階段 | 規則式 Text-to-SQL 後端 + 安全閘 | 中高 |
| 第五階段 | 載入既有 postgres(冪等 SQL) | 中 |
| 06-20 | n8n 三 workflow 上線 + 驗證 | 中 |
| 06-20~21 | Codex review 收斂 + 安全補強 + 全 Docker + V&V 閘 + Demo SQLite | 高(回頭補治理) |

**Baseline 特徵**:
- **多次「踩坑→根因→全面修」**(膨脹、編碼、同源驗證盲點)= from-scratch 的典型成本。
- **治理是事後補的**(去重、V&V 閘、Docker 化在後段才補)。
- 交付物從零產:六頁 + 後端 + 3 workflow + 四件套文件。

## 給 Loop 1 的對照指標(預期方向,待驗)
若 Skill Capitalization 有效,Loop 1(組裝)相對本 baseline 應:
- **lead time ↓**(踩坑已固化進 skill,不必重踩)
- **rework_loc ↓**(以配置為主)
- **reuse_rate ↑**(沿用既有階段技能)
- **治理「內建非事後」**(V&V 閘、Docker、不變量隨 skill 一起來)
- **同類缺陷不再復發**(膨脹/編碼/同源盲點已被 skill 的關卡擋住)

> 這些「預期方向」即 EXP-002 的 H1/H3;Loop 1 跑完用 `../metrics/METRICS_SCHEMA.md` 填真數據驗證。
