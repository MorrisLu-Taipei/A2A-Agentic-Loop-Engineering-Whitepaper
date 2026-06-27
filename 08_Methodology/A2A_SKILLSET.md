# 08 · A2A Skill Set（可被 AI Agent 直接接手執行的規格)

> 目的:**下一個 AI agent 讀完本檔就能自主驅動「3×AI 寫論文」流程**——不是看懂大意,是**照合約執行**。
> 為此每個 skill 都給:`機器可判定的 gate 述詞` + `JSON Schema 的 I/O` + `A2A 呼叫協定` + `self_check 驗收` + `失敗語意`。
> 守密:模型呼叫走通用 OpenAI 相容端點(角色 producer/reviewer/enhancer);不揭露任何商業機密 skill set。

---

## 0A. Runtime Adapter（協定不等於服務已存在）

本文件描述的是**邏輯合約**。執行 Agent 必須先判定 runtime：

```yaml
runtime_mode:
  connected_a2a: 有真實 JSON-RPC/A2A endpoint，可取得 execution id
  connected_n8n: 有真實 n8n workflow，可取得 execution id
  local_workspace: 只有共享檔案與工具，由 Agent 在本地映射 skill
```

在 `local_workspace`：

- `A2A.invoke()` 代表使用現有工具或 Agent 自身完成 skill，不代表發生 HTTP 呼叫。
- `STATE.load/save()` 以 `CURRENT_HANDOFF.md` + 各階段 README 作持久化 adapter。
- 結果仍須符合 output schema 與 gate；不可因沒有 server 就略過驗證。
- 不得偽造 JSON-RPC response、execution id、token、hash、log 或成功狀態。
- Codex 的完整映射與檔名規則見 `CODEX_OPERATING_GUIDE.md`。

只有 connected runtime 才能將 JSON-RPC 範例視為真實 transport。

---

## 0. 接手 Agent 的執行合約（先讀這段,再自我驗證)

你(接手的 orchestrator agent)必須遵守的執行迴圈:

```text
loop:
  state = STATE.load(research_id)                 # §2 schema
  skill = router(state)                           # §5 next-skill 規則
  if skill == "done": break
  assert preconditions(skill, state) == true      # §3 每 skill 的 preconditions
  result = A2A.invoke(skill, build_input(skill, state))   # §4 協定
  assert validate(result, skill.output_schema)    # §3 output_schema
  if not self_check(skill, result): on_fail(skill)         # §3 self_check
  if gate_predicate(skill, state, result) == true:         # §5 gate 述詞(布林)
      state = apply(state, result); STATE.save(state)
      evidence.append(skill, result.hash)          # append-only
  else:
      state = route_back(skill, state)             # 回上一關 + context
```

**自我驗證(你真的能接手嗎?跑這 5 題,全 yes 才開始)**
1. 你能 parse §1 Agent Card 並列出 8 個 skill 的執行順序?
2. 你能對 §2 State Object 做 load/save(任何 KV/DB)?
3. 你能依 §4 用 JSON-RPC 呼叫一個 skill 並驗證 result 符合 output_schema?
4. 你能對任一 skill 評估 §5 的 gate_predicate 得到布林?
5. 你能在 §3 的 invariant 失敗時(producer==reviewer / 未查證 / 造假)中止並記錄?

---

## 1. A2A Agent Card

```json
{
  "schemaVersion": "1.0",
  "name": "research-pipeline-agent",
  "version": "1.0.0",
  "description": "Drive a research idea to a DOI-ready paper via stage-gate, multi-engine adversarial review (evidence over consensus; human accountable).",
  "protocol": { "transport": "JSON-RPC 2.0 over HTTP", "discovery": "this card" },
  "authentication": { "scheme": "bearer", "note": "injected by deployer; no token stored here" },
  "capabilities": ["llm.chat", "http.fetch", "code.exec", "kv.state", "human.approval"],
  "roles": {
    "producer": { "endpoint_env": "OPENAI_BASE_URL", "model_env": "MODEL_PRODUCER" },
    "reviewer": { "endpoint_env": "OPENAI_BASE_URL", "model_env": "MODEL_REVIEWER" },
    "enhancer": { "endpoint_env": "OPENAI_BASE_URL", "model_env": "MODEL_ENHANCER" },
    "human":    { "channel": "approval" }
  },
  "skills": [
    {"id":"s00_ideas","order":0,"method":"ideate.seed"},
    {"id":"s01_consolidation","order":1,"method":"consolidate.scope"},
    {"id":"s02_draft","order":2,"method":"draft.write"},
    {"id":"s03_review_loop","order":3,"method":"review.adversarialLoop"},
    {"id":"s04_evidence","order":4,"method":"evidence.run"},
    {"id":"s05_due_diligence","order":5,"method":"diligence.check"},
    {"id":"s06_publication","order":6,"method":"publish.deposit"},
    {"id":"s07_lessons","order":99,"method":"retrospect.capture"}
  ],
  "globals": { "budget_tokens_env": "BUDGET_TOKENS", "determinism": {"temperature": 0} }
}
```

---

## 2. Shared State Object（JSON Schema)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ResearchState",
  "type": "object",
  "required": ["research_id","current_skill","gate_status","artifacts","budget"],
  "properties": {
    "research_id": {"type":"string"},
    "current_skill": {"type":"string"},
    "draft_version": {"type":"string","pattern":"^v[0-9]+(\\.[0-9]+)?$"},
    "gate_status": {"type":"object",
      "properties":{"G0":{"enum":["pending","pass","fail"]},"G1":{"enum":["pending","pass","fail"]},
        "G2":{"enum":["pending","pass","fail"]},"G3":{"enum":["pending","pass","fail"]},
        "G4":{"enum":["pending","pass","fail","blocked"]},"G5":{"enum":["pending","pass","fail"]},
        "G6":{"enum":["pending","pass","fail"]}}},
    "open_findings": {"type":"array","items":{"$ref":"#/$defs/finding"}},
    "artifacts": {"type":"object","additionalProperties":{"type":"string"}},
    "evidence_uri": {"type":"string"},
    "preprint_ready": {"type":"boolean"},
    "budget": {"type":"object","required":["tokens_used","limit"],
      "properties":{"tokens_used":{"type":"integer"},"limit":{"type":"integer"}}}
  },
  "$defs": {
    "finding": {"type":"object","required":["id","by","claim","verified"],
      "properties":{"id":{"type":"string"},"by":{"enum":["reviewer","enhancer","human"]},
        "claim":{"type":"string"},"severity":{"enum":["low","med","high"]},
        "verified":{"type":["boolean","null"]},"source_checked":{"type":"string"},
        "fabricated":{"type":"boolean"},"resolution":{"enum":["applied","rejected",null]}}}
  }
}
```

---

## 3. Skill 合約（每個 skill 一張;agent 照這個執行)

> 格式固定:`method · capabilities · input_schema · output_schema · preconditions · gate · postconditions · self_check · on_fail · human_required · idempotent · invariants`

### s02_draft（示範完整合約;其餘 skill 同結構)
```yaml
method: draft.write
role: producer
capabilities: [llm.chat]
input_schema:                      # 給 producer 端點的輸入
  type: object
  required: [positioning, RQ, evidence_levels]
  properties:
    positioning: {type: string}
    RQ: {type: array, items: {type: string}}
    evidence_levels: {type: array, items: {enum: [design_principle,engineering_spec,research_hypothesis,preliminary,validated]}}
output_schema:
  type: object
  required: [draft_uri, sections, claims]
  properties:
    draft_uri: {type: string}      # 寫入 02_Drafts/ 的路徑
    sections: {type: array, items: {type: string}}
    claims: {type: array, items: {type: object, required: [text, level],
             properties: {text: {type: string}, level: {type: string}}}}
preconditions:                     # 機器可判定
  - state.gate_status.G1 == "pass"
gate:                              # G2 述詞(布林,見 §5)
  id: G2
  predicate: "sections ⊇ {problem,method,framework,limitations} AND every(claims[*].level != null)"
postconditions:
  - state.draft_version bumped (vN → vN+1, 舊版保留)
  - artifacts.draft = output.draft_uri
self_check:                        # agent 跑這個驗收自己做對沒
  - "draft_uri 可讀且非空"
  - "claims 每條都有 level 標註(無未標)"
on_fail: "補缺章節/補證據等級標註後重呼一次;連續 2 次失敗 → 升級 human"
human_required: false
idempotent: false
invariants: []
```

### 其餘 skill(摘要合約;欄位同上,只列關鍵差異)
```yaml
s00_ideas:        {method: ideate.seed, role: human+producer, gate: G0,
  input: {field_pain, prior_projects}, output: {open_questions[], seed_problem},
  gate_predicate: "seed_problem != '' AND open_questions.length>0", human_required: true}

s01_consolidation:{method: consolidate.scope, role: producer+reviewer, gate: G1,
  input: {seed_problem, prior_art_hits[]}, output: {positioning, candidate_contributions[], RQ[]},
  gate_predicate: "positioning!='' AND candidate_contributions.length>0 AND public_goods_conceded==true"}

s03_review_loop:  {method: review.adversarialLoop, role: reviewer+enhancer+verifier, gate: G3,
  input: {draft_uri}, output: {findings[], draft_uri_next},
  gate_predicate: "count(findings where verified==null)==0 AND count(findings where fabricated==true && resolution!='rejected')==0 AND no_overclaim==true",
  invariants:
    - "MODEL_PRODUCER != MODEL_REVIEWER"            # 生產者≠審查者
    - "every finding: verified==true OR resolution=='rejected'"   # 一律查證
    - "any finding.fabricated==true ⇒ resolution=='rejected' AND logged to s07"
  steps: [reviewer.critique, enhancer.critique, merge, verify.primarySource, applyOrReject, loopUntilConverged]}

s04_evidence:     {method: evidence.run, role: producer+human, gate: G4,
  input: {hypotheses[], real_case_ref, experiment_protocol_ref}, output: {measured_results, claim_evidence_matrix},
  gate_predicate: "measured_results != null AND matrix.has_any(level=='validated' OR 'preliminary')",
  on_fail: "blocked → 只允許 preprint 子路徑(state.preprint_ready=true),不投正式論文", human_required: true}

s05_due_diligence:{method: diligence.check, role: reviewer+human, gate: G5,
  input: {draft_uri, references[]}, output: {prior_art_matrix, originality_stmt, novelty_assessment},
  gate_predicate: "every(references[*].verified==true) AND placeholder_count==0 AND novelty_class in {integration,specialization}"}

s06_publication:  {method: publish.deposit, role: producer+human, gate: G6,
  input: {final_draft_uri, citation_cff, license}, output: {doi, submission_package},
  gate_predicate: "metadata.title==citation.title AND metadata.author==citation.author AND doi!=null",
  human_required: true,
  invariants: ["deposit 須經 human approval", "作者須以 ORCID 登入(否則不回寫 ORCID)"]}

s07_lessons:      {method: retrospect.capture, role: producer, gate: none,
  input: {rejected_findings[], incidents[]}, output: {lessons[]}, idempotent: true}
```

---

## 4. A2A 呼叫協定（JSON-RPC 2.0)

**Request**
```json
{ "jsonrpc":"2.0", "id":"call-001", "method":"review.adversarialLoop",
  "params": { "research_id":"rp_2026_xxx", "input": { "draft_uri":"02_Drafts/...v3.0.md" },
              "role_overrides": {} } }
```
**Result(成功)**
```json
{ "jsonrpc":"2.0", "id":"call-001",
  "result": { "skill":"s03_review_loop", "output": { "findings":[...], "draft_uri_next":"...v3.1.md" },
              "gate": {"id":"G3","passed":true}, "evidence_hash":"sha256:...","tokens":12000 } }
```
**Error(失敗/不可重試)**
```json
{ "jsonrpc":"2.0", "id":"call-001",
  "error": { "code": 4031, "message":"INVARIANT_VIOLATION: producer==reviewer",
             "data": {"skill":"s03_review_loop","action":"halt+log_s07"} } }
```
**錯誤碼**:`4001` precondition_failed · `4011` output_schema_invalid · `4021` self_check_failed(可重試) · `4031` invariant_violation(中止) · `4041` gate_failed(回上一關) · `4291` budget_exceeded(凍結升級人類).

---

## 5. Router 與 Gate 述詞（集中,機器可判定)

```javascript
// next-skill:第一個 gate 未 pass 的 skill;G4 阻塞時走 preprint 子路徑
function router(s){
  const ord=["s00_ideas","s01_consolidation","s02_draft","s03_review_loop","s04_evidence","s05_due_diligence","s06_publication"];
  const g={s02_draft:"G2",s03_review_loop:"G3",s04_evidence:"G4",s05_due_diligence:"G5",s06_publication:"G6",s00_ideas:"G0",s01_consolidation:"G1"};
  if(s.budget.tokens_used>=s.budget.limit) return "HALT_budget";
  let nx=ord.find(k=>s.gate_status[g[k]]!=="pass");
  if(s.gate_status.G4!=="pass" && s.preprint_ready) return "s06_publication_preprint";
  return nx||"done";
}
// gate 述詞:回布林;每個 G# 對應一個純函式(輸入 state+result)
const GATES = {
  G0: (s,r)=> r.seed_problem && r.open_questions.length>0,
  G1: (s,r)=> r.positioning && r.candidate_contributions.length>0 && r.public_goods_conceded===true,
  G2: (s,r)=> ["problem","method","framework","limitations"].every(x=>r.sections.includes(x)) && r.claims.every(c=>c.level),
  G3: (s,r)=> r.findings.every(f=>f.verified!==null) && !r.findings.some(f=>f.fabricated && f.resolution!=="rejected") && r.no_overclaim===true,
  G4: (s,r)=> r.measured_results!=null,
  G5: (s,r)=> r.references.every(x=>x.verified) && r.placeholder_count===0,
  G6: (s,r)=> r.doi && r.metadata_consistent===true && r.human_approved===true
};
```

---

## 6. 端到端 Worked Trace（接手 agent 照抄這條)

```text
1. STATE.init(research_id=rp1, gate_status=all pending, G4=blocked, budget=500k)
2. router→ s00_ideas → invoke ideate.seed → G0 pass → save
3. router→ s01_consolidation → consolidate.scope → G1 pass(讓出公共財) → save
4. router→ s02_draft → draft.write → 產 v1 + claims 標 level → G2 pass → save
5. router→ s03_review_loop:
     reviewer.critique → findings[3]; enhancer.critique → findings[2]
     verify.primarySource:逐條查(HTTP arXiv / code.exec) → 2 條屬實(applied) / 1 條 fabricated(rejected→log s07) / 2 條讀錯(rejected)
     producer 套用 applied → v2;findings 全 verified!=null → G3 pass → save
6. router→ s04_evidence → evidence.run → measured_results==null
     → gate G4 fail → on_fail:blocked;set preprint_ready=true
7. router→ (G4 未 pass 且 preprint_ready) → s06_publication_preprint
     publish.deposit(preprint):metadata 一致 + human approval → doi 取得 → G6(preprint) pass
8. 正式 full paper:等 s04 有 measured_results 才解 G4 → 走 s05 → s06 正式
```

---

## 7. 全域紅線（違反即 4031 中止)
```text
1. MODEL_PRODUCER != MODEL_REVIEWER(生產者≠審查者)
2. 任何 AI 產出(審查/數據/日誌)未經 verify.primarySource 不得標 verified
3. fabricated==true 一律 rejected 並寫 s07_lessons
4. gate_predicate==false 不得 apply、不得前進
5. s06 deposit / 宣稱 validated 須 human approval
6. tokens_used>=limit → 凍結升級人類(4291)
7. 草稿遞增版號、舊版保留;機密只摘要
```

> 這份規格 = ALE 白皮書 §5.6 權限 + §7 三層驗證的**可執行 A2A 版**。落地編排見 `N8N_ORCHESTRATION.md`(每個 method 對應一組 n8n 節點)。
