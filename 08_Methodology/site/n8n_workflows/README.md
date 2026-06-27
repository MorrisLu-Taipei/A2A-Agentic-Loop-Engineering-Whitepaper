# n8n 課堂教材包：WF-1 ~ WF-8（可匯入)

> 對應 `../COURSE_SYLLABUS.md` 每週的動手 workflow。**全部 stub 化、零金鑰可跑**(WF-4/WF-7 會連 arXiv,需網路、不需金鑰)。

## 匯入方式
n8n → 左上選單 → **Import from File** → 選 `WF-*.json` → Execute Workflow → 點各節點看資料流。

## 清單
| 檔 | 週 | 學什麼 | 需網路/金鑰 |
|---|---|---|---|
| `WF-1_Hello-State.json` | W1 | State Object + Router | 否 |
| `WF-2_Gate-Demo.json` | W2 | stage-gate(IF pass/fail 回 Router) | 否 |
| `WF-3_Review-Loop.json` | W3 | 生產者≠審查者(平行審查→Merge+Verify) | 否(stub) |
| `WF-4_Verify.json` | W4 | ★ 不盲信 AI:真打 arXiv 核驗書目 | 網路 |
| `WF-5_Mechanical-Gate.json` | W5 | 機械閘(覆蓋率+突變雙門檻) | 否(stub) |
| `WF-6_Human-Approval.json` | W6 | 人類核可(Wait 節點) | 否 |
| `WF-7_PriorArt-Verify.json` | W7 | 先前技術核驗(真打 arXiv) | 網路 |
| `WF-8_Publish-Preprint.json` | W8 | 發表 metadata 一致性 →(sandbox)DOI | 否(stub) |

## 把 stub 換成真模型(作業 C)
WF-3 的 `Reviewer stub` / `Enhancer stub` 換成 **HTTP Request**:
```
POST {{ $env.OPENAI_BASE_URL }}/chat/completions
Header: Authorization: Bearer {{ $env.OPENAI_API_KEY }}
Body(JSON): {"model":"{{ $env.MODEL_REVIEWER }}","temperature":0,
  "messages":[{"role":"system","content":"Adversarial reviewer: find overclaims, missing citations, misreadings."},
              {"role":"user","content":"={{ $json.draft }}"}]}
```
鐵則:`MODEL_PRODUCER != MODEL_REVIEWER`(生產者≠審查者)。

## 三個踩坑(課堂提醒)
1. schedule trigger 不能 CLI execute → smoke 用 manual-trigger。
2. healthcheck 用 `127.0.0.1` 不要 localhost。
3. 匯入憑證/工作流 JSON 帶顯式 `id`。

> 這些 workflow 只編排「研究/論文生產」教學,**不涉及任何商業機密 skill set**。
