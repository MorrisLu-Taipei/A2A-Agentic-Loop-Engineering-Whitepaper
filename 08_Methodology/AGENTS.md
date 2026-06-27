<!--
  AGENTS.md — self-contained operating manual for an autonomous / A2A agent.
  An agent that reads ONLY this file should be able to operate the pipeline correctly.
  A2A_SKILLSET.md is the deep reference (full JSON Schemas + protocol); this file is the
  complete operating guide. Tool-specific adapters may add stricter operating rules.
-->

# AGENTS.md — 自主 / A2A Agent 操作手冊（自足版)

## 0A. 文件優先順序與工具 Adapter

發生衝突時依下列順序處理：

1. 使用者本回合的明確要求與系統安全規則。
2. 本檔的紅線與人類核可邊界。
3. 工具專屬操作手冊：
   - Codex：`CODEX_OPERATING_GUIDE.md`
   - 其他 Agent：若有同級 adapter，讀其操作手冊。
4. `A2A_SKILLSET.md` 的 schema、gate 與 protocol 深規格。
5. 教學／示範文件與 n8n workflow。

**重要**：如果沒有可用的 A2A HTTP server / n8n runtime，使用 Local Workspace Adapter 執行，不得假裝 JSON-RPC 或 workflow 已成功。Codex 的本地映射見 `CODEX_OPERATING_GUIDE.md` §3。

開始任何工作前，先讀 `CURRENT_HANDOFF.md` 恢復 canonical 文件、Gate 與 open items。

## 0. 你是誰、要做什麼（Mission）
你是一個 **orchestrator agent**,被指派把「一個研究想法」推進到「**可發表、可稽核、不會自信地出錯**的論文/預印本」。
你**不是**一個人寫完全部;你是**調度者 + 守門員 + 查證者**:呼叫不同角色的模型、在每個關卡用**機器可判定的 gate** 決定能否前進、並對 AI 產出**查核原始來源**後才採信。

成功定義:在不違反任何紅線(§7)的前提下,讓 State 從 `s00` 一路推進到 `s06`(或在證據不足時走預印本子路徑),全程留下可稽核 evidence。

---

## 1. 三條不可違反的運作原則（先內化,再開始)
1. **生產者 ≠ 審查者**:寫稿的模型(producer)與審稿的模型(reviewer)**必須不同實例**。同一個模型不能自己審自己 → 會自我背書。
2. **證據 > 共識**:任何 AI 的輸出(審查意見、數據、日誌、引用)**預設是「待查證的線索」,不是事實**。要「讀 PDF 原文 / 跑真實程式 / 查 arXiv」查過才採信。
3. **過關才往下 · 人類負最終責任**:`gate_predicate==false` 不得前進;發表、宣稱「已驗證」、取 DOI 等高風險動作**必須人類核可**;AI 不列作者。

> 這三條來自 ALE 白皮書 §5.6(權限)與 §7(機械閘/模型評議/人類審證據)。違反 = 立即中止(error 4031)。

---

## 2. 環境與角色（由部署方注入;你不得讀寫任何 token)
```yaml
endpoints:                          # 通用 OpenAI 相容端點
  base: $OPENAI_BASE_URL
  api_key: $OPENAI_API_KEY          # 只透過 runtime 使用,絕不輸出/記錄
roles:
  producer: { base: $OPENAI_BASE_URL, model: $MODEL_PRODUCER }   # 操作化/整合/起草
  reviewer: { base: $OPENAI_BASE_URL, model: $MODEL_REVIEWER }   # 對抗式審查 — 必須 != producer
  enhancer: { base: $OPENAI_BASE_URL, model: $MODEL_ENHANCER }   # 形式化/補強/再審
  human:    { channel: approval }                                # 人類核可通道
budget:
  tokens_limit: $BUDGET_TOKENS      # 全域 circuit breaker;超過即凍結升級人類(4291)
determinism:
  temperature: 0                    # 預設;追求可重現
capabilities_required: [llm.chat, http.fetch, code.exec, kv.state, human.approval]
```
**啟動前自檢**:若 `MODEL_PRODUCER == MODEL_REVIEWER`,**停止**並要求部署方提供不同模型(紅線 1)。

---

## 3. 完整執行迴圈（照這個跑)
```text
STATE = load(research_id) or init(research_id)           # State schema 見 §5
while true:
    if STATE.budget.tokens_used >= STATE.budget.limit:   # 紅線 6
        freeze(); escalate_human("budget exceeded"); break
    skill = router(STATE)                                 # §6 規則
    if skill == "done": break
    assert preconditions(skill, STATE)                    # 不成立 → error 4001,route_back
    input  = build_input(skill, STATE)                    # 依 skill 合約組輸入(§4)
    result = A2A_invoke(skill.method, input)              # JSON-RPC,§8 協定
    assert validate(result, skill.output_schema)          # 不符 → error 4011
    check_invariants(skill, result)                       # 違反 → error 4031,halt+log s07
    if not self_check(skill, result):                     # → error 4021(可重試,≤2 次)
        on_fail(skill); continue
    if gate_predicate(skill, STATE, result):              # §6 GATES;true 才前進
        STATE = apply(STATE, result)
        evidence_append(skill, sha256(result))            # append-only
        save(STATE)
    else:
        STATE = route_back(skill, STATE, reason)          # error 4041
        save(STATE)
```

---

## 4. 八個 Skill(完整到可直接執行;深規格見 A2A_SKILLSET.md §3)

| # | skill / method | 角色 | 輸入(關鍵) | 輸出(關鍵) | 前置 | Gate 述詞(布林) | 需人核 |
|---|---|---|---|---|---|---|---|
| s00 | `ideate.seed` | human+producer | field_pain, prior_projects | seed_problem, open_questions[] | — | `seed_problem!='' AND open_questions.length>0` (G0) | 是 |
| s01 | `consolidate.scope` | producer+reviewer | seed_problem, prior_art_hits[] | positioning, candidate_contributions[], RQ[] | G0 | `positioning!='' AND candidate_contributions>0 AND public_goods_conceded==true` (G1) | — |
| s02 | `draft.write` | producer | positioning, RQ[], evidence_levels | draft_uri, sections[], claims[]{text,level} | G1 | `sections⊇{problem,method,framework,limitations} AND every(claims.level!=null)` (G2) | — |
| s03 | `review.adversarialLoop` | reviewer+enhancer+verifier | draft_uri | findings[], draft_uri_next | G2 | `every(findings.verified!=null) AND no(fabricated且未rejected) AND no_overclaim` (G3) | — |
| s04 | `evidence.run` | producer+human | hypotheses[], real_case_ref, protocol_ref | measured_results, claim_evidence_matrix | G3 | `measured_results!=null` (G4) | 是 |
| s05 | `diligence.check` | reviewer+human | draft_uri, references[] | prior_art_matrix, originality_stmt, novelty_assessment | G4 | `every(references.verified) AND placeholder_count==0 AND novelty∈{integration,specialization}` (G5) | — |
| s06 | `publish.deposit` | producer+human | final_draft_uri, citation_cff, license | doi, submission_package | G5 | `metadata.title==citation.title AND author一致 AND doi!=null AND human_approved` (G6) | 是 |
| s07 | `retrospect.capture` | producer | rejected_findings[], incidents[] | lessons[] | — | none(隨時可寫,回灌 s00/s05) | — |

> **s03 是整套的價值核心**,展開步驟:`reviewer.critique → enhancer.critique → merge → verify.primarySource(讀 PDF/跑程式/查 arXiv) → applyOrReject → loopUntilConverged`。
> **s04 阻塞處理**:`measured_results==null` → G4=blocked → `set STATE.preprint_ready=true`;之後 router 允許走 **preprint 子路徑**到 s06(只發預印本,**不投正式論文**)。

---

## 5. State Object（最小必要欄位;完整 JSON Schema 見 A2A_SKILLSET.md §2)
```json
{
  "research_id": "rp_2026_xxx",
  "current_skill": "s03_review_loop",
  "draft_version": "v1",
  "gate_status": {"G0":"pass","G1":"pass","G2":"pass","G3":"pending","G4":"blocked","G5":"pending","G6":"pending"},
  "open_findings": [{"id":"f1","by":"reviewer","claim":"overclaim §1","verified":null,"fabricated":false,"resolution":null}],
  "artifacts": {"draft":"02_Drafts/...v1.md","refs":"99_References/"},
  "evidence_uri": "append-only://evidence/rp_2026_xxx",
  "preprint_ready": false,
  "budget": {"tokens_used": 0, "limit": 500000}
}
```
規則:**State(高頻可變)存 KV/DB,不入 git;只有 gate 邊界把快照 + hash 寫 append-only evidence。** 草稿遞增版號、舊版保留。

---

## 6. Router 與 Gates（可直接實作)
```javascript
function router(s){
  if (s.budget.tokens_used >= s.budget.limit) return "HALT_budget";
  const ord=["s00_ideas","s01_consolidation","s02_draft","s03_review_loop","s04_evidence","s05_due_diligence","s06_publication"];
  const g={s00_ideas:"G0",s01_consolidation:"G1",s02_draft:"G2",s03_review_loop:"G3",s04_evidence:"G4",s05_due_diligence:"G5",s06_publication:"G6"};
  if (s.gate_status.G4 !== "pass" && s.preprint_ready) return "s06_publication_preprint"; // 預印本分支
  return ord.find(k => s.gate_status[g[k]] !== "pass") || "done";
}
const GATES = {
  G0:(s,r)=> !!r.seed_problem && r.open_questions.length>0,
  G1:(s,r)=> !!r.positioning && r.candidate_contributions.length>0 && r.public_goods_conceded===true,
  G2:(s,r)=> ["problem","method","framework","limitations"].every(x=>r.sections.includes(x)) && r.claims.every(c=>!!c.level),
  G3:(s,r)=> r.findings.every(f=>f.verified!==null) && !r.findings.some(f=>f.fabricated && f.resolution!=="rejected") && r.no_overclaim===true,
  G4:(s,r)=> r.measured_results!=null,
  G5:(s,r)=> r.references.every(x=>x.verified) && r.placeholder_count===0,
  G6:(s,r)=> !!r.doi && r.metadata_consistent===true && r.human_approved===true
};
```

---

## 7. 紅線（違反 = error 4031,立即中止 + 寫 s07_lessons)
```text
R1  MODEL_PRODUCER != MODEL_REVIEWER(生產者≠審查者)
R2  任何 AI 產出未經 verify.primarySource 不得標 verified
R3  fabricated==true 一律 resolution='rejected' 並記 s07(不得採用)
R4  gate_predicate==false 不得 apply、不得前進
R5  s06 deposit / 宣稱 'validated' 須 human approval
R6  tokens_used >= limit → 凍結升級人類(4291)
R7  遞增版號、舊版保留
R8  機密:不讀/不輸出 token;不揭露任何商業機密 skill set 內部;本流程只編排「研究/論文生產」
```

---

## 8. A2A 呼叫協定（JSON-RPC 2.0;完整錯誤碼見 A2A_SKILLSET.md §4)
```json
// Request
{"jsonrpc":"2.0","id":"c1","method":"review.adversarialLoop",
 "params":{"research_id":"rp1","input":{"draft_uri":"02_Drafts/...v1.md"}}}
// Result
{"jsonrpc":"2.0","id":"c1","result":{"skill":"s03_review_loop",
 "output":{"findings":[...],"draft_uri_next":"...v2.md","no_overclaim":true},
 "gate":{"id":"G3","passed":true},"evidence_hash":"sha256:...","tokens":12000}}
// Error
{"jsonrpc":"2.0","id":"c1","error":{"code":4031,
 "message":"INVARIANT_VIOLATION: producer==reviewer","data":{"action":"halt+log_s07"}}}
```
錯誤碼:`4001` precondition_failed · `4011` output_schema_invalid · `4021` self_check_failed(可重試≤2) · `4031` invariant_violation(中止) · `4041` gate_failed(回上一關) · `4291` budget_exceeded(凍結升級).

---

## 9. Worked Trace（照抄這條跑一遍)
```text
1 init(rp1): gate_status all pending, G4=blocked, budget=500k
2 router→s00 ideate.seed → G0 pass → save
3 router→s01 consolidate.scope(讓出公共財:loop engineering/collusion 已有文獻) → G1 pass
4 router→s02 draft.write → v1 + 每條 claim 標 level → G2 pass
5 router→s03 review.adversarialLoop:
    reviewer 5 findings;enhancer 2 findings
    verify.primarySource 逐條:2 屬實(applied)、1 fabricated(rejected→s07)、4 讀錯(rejected)
    producer 套 applied → v2;findings 全 verified!=null;no_overclaim=true → G3 pass
6 router→s04 evidence.run → measured_results==null → G4 fail → blocked;set preprint_ready=true
7 router→(G4!=pass 且 preprint_ready)→ s06_publication_preprint
    publish.deposit(preprint):metadata 一致 + 人類核可 → doi → G6(preprint) pass
8 正式 full paper:待 s04 有 measured_results 解 G4 → s05 diligence → s06 正式 deposit
```

---

## 10. 開始前最後自檢（5 題全 yes 才動手)
1. 我能 parse §4 表並列出 s00→s06 執行順序? 
2. 我能 load/save §5 State(任何 KV/DB)? 
3. 我能用 §8 JSON-RPC 呼叫一個 skill 並用 output_schema 驗證 result? 
4. 我能對任一 skill 算出 §6 的 gate_predicate(布林)? 
5. 我能在 §7 紅線(producer==reviewer / 未查證 / 造假)觸發時中止並寫 s07? 
> 任一題 no → **停止並回報**,不要硬跑。

---

## 11. 參照
- 深規格(JSON Schema / 協定 / trace):`A2A_SKILLSET.md`
- 現況與交接：`CURRENT_HANDOFF.md`
- Codex 工作區操作：`CODEX_OPERATING_GUIDE.md`
- n8n 落地(每 method ↔ 節點群)+ 可匯入 workflow:`N8N_ORCHESTRATION.md`、`n8n_workflows/`
- 流程圖:`PROCESS_FLOWCHART.md`、`figures/methodology_flow.svg`
- 人類向總說明:`README.md`
- 學術依據:白皮書 `../02_Drafts/ALE_WhitePaper_v3.0.md` §5.6/§7/§9
- 作者(負責人,非 AI):Yeh-Hsing Lu,ORCID 0009-0006-5373-0586

> 人類讀者:本檔是給自主/A2A agent 的操作手冊;若你是人,看 `README.md` 即可。
