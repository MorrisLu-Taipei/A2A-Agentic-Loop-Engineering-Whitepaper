# EXP-002 量測 schema（reuse loop 成效指標)

> 只量**外部成效指標**(不碰 skill set 內部);資料一到即可填。每個 loop 一筆 `reuse_loop<N>.json`。

## 欄位定義

| 欄位 | 型別 | 說明 | 怎麼量 |
|---|---|---|---|
| `loop_id` | int | 第幾輪(0=發票 baseline,1,2…) | — |
| `case_name` | str | 案名(脫敏代號) | — |
| `mode` | enum | `from_scratch` / `assembled` | 對照組標記 |
| `lead_time_min` | number | 資料進 → 儀表板出 的 wall-clock 分鐘 | 計時器/時間戳 |
| `reuse_rate` | 0–1 | 沿用既有技能模組比例(組裝 vs 新做) | 組裝步驟數 / 總步驟數 |
| `rework_loc` | int | 需手改的程式行數(越少越好) | git diff vs 純配置 |
| `config_only` | bool | 是否「只配置、零改 code」 | — |
| `defects_found` | int | 交付前發現缺陷數 | V&V/審查 |
| `vv_pass` | bool | V&V 機械閘是否通過 | vv 報告 |
| `invariant_hold` | bool | 系統級不變量成立 | 上界/去重檢查 |
| `human_gates` | int | 觸發幾次人類關卡 | 流程記錄 |
| `cost_tokens` | int | (若用模型)token 量 | API 計量 |
| `notes` | str | 質性觀察(踩坑、語意不相容等) | — |

## 範例(待填,非真實數據)
```json
{
  "loop_id": 1, "case_name": "case-X(脫敏)", "mode": "assembled",
  "lead_time_min": null, "reuse_rate": null, "rework_loc": null,
  "config_only": null, "defects_found": null, "vv_pass": null,
  "invariant_hold": null, "human_gates": null, "cost_tokens": null,
  "notes": ""
}
```

## 判定(對 EXP-002 假說)
- **H1 降本**:`lead_time_min(assembled) ≪ baseline(from_scratch)`、`rework_loc` 低、`reuse_rate` 高。
- **H3 可組裝**:`config_only == true` 或 `rework_loc` 很小 ⇒ 支持;大量 rework ⇒ 暴露語意不相容(`notes` 記錄)。
- **H4 邊際成本**:跨 loop 看 `lead_time_min` / `rework_loc` 是否次線性下降。
- **H2 可驗證晉升**:`vv_pass==false` 卻被採用 = 治理失敗(必須為 0)。
