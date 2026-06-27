# EXP-001 結果模板（test collusion;服務 EXP-002 之 H5)

> 接上模型端點跑 pilot 後填。判定規則見 `../README.md` ④ 與 `../../ALE_EXP-001_Protocol_v2.md`。

## 各組 false-pass / 缺陷攔截（待填)

| 組 | n | false-pass rate | defect detection | escaped | mutation | 成本(token/時間) |
|---|---|---|---|---|---|---|
| A 同模型同脈絡 | _ | _ | _ | _ | _ | _ |
| B 異模型同脈絡 | _ | _ | _ | _ | _ | _ |
| C 規格隔離 | _ | _ | _ | _ | _ | _ |
| D 機械閘 | _ | _ | _ | _ | _ | _ |
| E 人類 golden | _ | _ | _ | _ | _ | _ |

## 假設判定
- H1(impl-gen > spec-gen false-pass):FPR(A,B) vs FPR(C) → _
- H2(換模型不降 bias):FPR(A) vs FPR(B) → _（若 B≪A 則**推翻**,改寫白皮書 §7.2）
- H3(機械閘壓逃逸):escaped(D) → _

## 回寫
- → 白皮書 §7.2 / §9.7（C-A/C-B/C5）、EXP-002 之 H5。
