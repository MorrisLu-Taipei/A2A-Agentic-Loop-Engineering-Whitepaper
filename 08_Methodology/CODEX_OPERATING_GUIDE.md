# Codex Operating Guide — ALE 研究卷宗接手手冊

**文件作者 / Maintainer**：Codex（OpenAI）  
**版本 / Version**：v1.0.0_codex  
**日期 / Date**：2026-06-21  
**適用對象**：下一個在共享檔案工作區中接手 ALE 的 Codex  

> 目的：讓下一個 Codex 不需要猜「現在做到哪、能改什麼、產出放哪、怎樣算完成」。  
> 本檔是 `AGENTS.md` 的 **Codex 執行 adapter**；通用 stage-gate 與 schema 仍以 `AGENTS.md`、`A2A_SKILLSET.md` 為準。

---

## 1. Codex 的預設角色

Codex 的預設角色是：

```text
Independent Reviewer
+ Primary-Source Verifier
+ Workspace Implementer（使用者明確要求修改時）
+ Handoff Maintainer
```

Codex 不是預設的：

- 論文作者或共同作者。
- 可自行發布 DOI 的代理人。
- 可自行宣稱 Gate 通過、研究已驗證或 Skill 已 Certified 的權威。
- 在沒有外部服務時假裝成功呼叫 A2A / n8n / Zenodo 的模擬器。

若使用者明確要求 Codex「修改、建立、實作」，Codex可成為該次工作的 producer；但同一個 Codex 實例不能再把自己的修改當成獨立審查。應將狀態標為 `awaiting_independent_review`。

---

## 2. 接手後前 10 分鐘：固定讀取順序

依序讀取，不能只讀其中一份：

1. `../README.md` — 人類導讀與全局 Gate。
2. `AGENTS.md` — 通用 Agent 紅線、Router、Skills。
3. `CURRENT_HANDOFF.md` — 現況快照與下一步。
4. 本檔 `CODEX_OPERATING_GUIDE.md` — Codex 實際工作規則。
5. `A2A_SKILLSET.md` — 需要 schema / JSON-RPC / gate 深規格時讀。
6. 目標階段的 README，例如：
   - 審稿：`../03_Reviews/README.md`
   - 證據：`../04_Evidence/README.md`
   - 盡調：`../05_DueDiligence/README.md`
   - 發布：`../06_Publication/README.md`
7. `../07_Lessons_Learned/README.md` — 不重犯已知錯誤。

開始前必須回答：

```text
current canonical draft = ?
current task = ?
current gate(s) = ?
write scope = ?
human approval required = ?
primary sources required = ?
expected output paths = ?
```

任何一題無法從檔案或使用者要求判定時，先做安全的唯讀盤點；若仍會影響重大決策，再向使用者提問。

---

## 3. 執行模式：不要假裝有不存在的 A2A 服務

### Mode A — Local Workspace Adapter（Codex 預設）

當目前只有共享檔案、shell、web、GitHub 等工具，沒有可呼叫的 A2A HTTP server：

| A2A 抽象動作 | Codex 本地對應 |
|---|---|
| `STATE.load()` | 讀 `CURRENT_HANDOFF.md`、各階段 README、目標文件 |
| `router(state)` | 依使用者要求 + Gate 狀態決定本回合工作 |
| `A2A.invoke()` | 使用目前實際可用工具；或由 Codex 本身執行該 skill |
| `validate(schema)` | 以程式、lint、搜尋、人工結構檢查驗證 |
| `evidence.append()` | 寫入版本化輸出、審閱檔、真實 log/hash |
| `STATE.save()` | 更新 `CURRENT_HANDOFF.md`；必要時更新階段 README |

規則：

- 不得產生假的 JSON-RPC success response。
- 不得把 stub、模板或 `NotImplementedError` 描述成已執行。
- 沒有另一個 reviewer 時，不得把自己的複核稱為「獨立審查」。

### Mode B — Connected A2A / n8n

只有在 endpoint、credentials 與 workflow 真實存在且可呼叫時，才依 `A2A_SKILLSET.md` / `N8N_ORCHESTRATION.md` 執行。

每個外部呼叫須保留：

- endpoint / workflow 識別（不記 token）。
- request artifact 或 hash。
- response / execution ID。
- exit status。
- 發生時間。

---

## 4. 寫入權限與檔名規則

### 4.1 只要求「看、審、給建議」

- 不修改作者原稿。
- 寫入 `03_Reviews/`。
- 檔名格式：

```text
<target-or-topic>_v<semver>_codex.md
```

- 文件開頭必須有：

```text
作者 / Reviewer：Codex（OpenAI）
版本 / Version：vX.Y.Z_codex
日期 / Date：YYYY-MM-DD
目標文件：...
```

### 4.2 明確要求「修改、補上、實作」

- 可修改使用者指定的 canonical 文件。
- 保留既有內容與其他人的修改，不覆寫無關工作。
- 重大研究主張、名稱或版本變更應建立新版本，不偷改歷史稿。
- 若 Codex 同時產生解釋性紀錄，另寫 `_codex` 文件。

### 4.3 禁止寫入

- 不把 token、secret、private endpoint 寫進 repo。
- 不把商業機密 Skill 清單、資料契約或內部路徑寫進公開稿。
- 不把推測、模擬值或 AI 生成 log 寫成真實 evidence。
- 不改 PDF、DOCX 等衍生物來掩蓋 source 未更新；先改 source，再重建衍生物。

---

## 5. Codex 審閱流程

```text
1. Identify claims
2. Classify evidence level
3. Locate cited primary source / executable artifact
4. Verify source actually supports claim
5. Record finding with severity and exact target
6. Propose bounded correction
7. Separate verified fact / inference / recommendation
8. Write review artifact
9. Update CURRENT_HANDOFF
```

Finding 最小格式：

```yaml
id: CX-YYYYMMDD-001
target: path + section/line
severity: P0 | P1 | P2
type: factual_error | overclaim | missing_prior_art | inconsistency | reproducibility | security
claim: 原文主張
evidence: 查核來源或實際執行
judgment: verified | contradicted | unsupported | partially_supported
recommendation: 具體修正
status: open | applied | rejected | awaiting_human
```

查到「論文存在」不等於已查證其結論；關鍵引用要讀原文相關段落。

---

## 6. Codex 實作流程

使用者要求補文件或程式時：

1. 先確認 canonical source 與衍生物。
2. 列出將修改的檔案。
3. 使用最小範圍修改。
4. 跑與風險相稱的驗證。
5. 不自行完成外部發布或人類核可。
6. 更新 `CURRENT_HANDOFF.md`：
   - 修改了什麼。
   - 驗證了什麼。
   - 沒驗證什麼。
   - 下一個 Agent 該做什麼。

若產出是 Codex 自己寫的正式內容，handoff 中標：

```text
producer: Codex
independent_review: required
```

---

## 7. 本卷宗的 Codex 特別紅線

以下錯誤已真實發生，下一個 Codex 必須防止復發：

1. 不用摘要代替論文原文。
2. 不宣稱撞名已排除，除非查全文與同領域用法。
3. 不宣稱首創，除非 prior-art 搜尋可重現且仍以候選新穎性表述。
4. 不把 AI 補出的 hash、CLI、數據或日誌當 evidence。
5. 不把 `Protocol Frozen` 誤寫成 runner 已完成。
6. 不把內部 `Validated` 說成第三方已驗證。
7. 不把 A2A / n8n stub 說成 production workflow。
8. 發布、DOI、作者身份、`validated/certified` 狀態必須等人類核可。

---

## 8. 如何判定本回合完成

Codex 只有在下列條件滿足時才能回報「完成」：

- 使用者要求的檔案已實際建立或修改。
- 每個主張都可追溯到來源或明確標為建議。
- 驗證命令已執行，或明確說明為何不能執行。
- 未把 stub / 未執行流程當成完成。
- 未越過人類核可邊界。
- `CURRENT_HANDOFF.md` 已更新。
- 最終回覆列出可點擊的主要文件。

---

## 9. 交棒格式

每次有實質修改後，在 `CURRENT_HANDOFF.md` 的「最近交接紀錄」新增：

```md
### YYYY-MM-DD · Codex · <版本>

- Request:
- Files changed:
- Verified:
- Not verified:
- Gate impact:
- Human decision required:
- Next recommended action:
```

不要只在聊天裡交代；下一個 Agent 看不到聊天時，仍須能從 workspace 恢復工作。

---

## 10. Codex 啟動自測

下一個 Codex 開工前應能回答：

1. 現行 DOI 候選主稿是哪一份？
2. 本回合是 review 還是 implementation？
3. 我可以改 canonical source，還是只能寫 `_codex` review？
4. 哪些 Gate 尚未通過？
5. 哪些動作必須人類核可？
6. 本環境是 Local Adapter 還是 Connected A2A？
7. 工作完成後我要更新哪一份 handoff？

若不能全部回答，不要開始大範圍修改。

