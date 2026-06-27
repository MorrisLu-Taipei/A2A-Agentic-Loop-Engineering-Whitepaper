# A2A Skill Set 深度規格與 Gemini 編輯代理人操作細則
## A2A Skill Set Specification & Gemini Editor Agent Operating Manual

**文件定位**：本文件為 `08_Methodology` 的深度技術規格（Deep Reference），補齊原 `AGENTS.md` 所引用之缺失 `A2A_SKILLSET.md` 規格。  
**評審與產出人**：Gemini 3.5 Flash (Medium) — 虎智科技 Editor Agent  
**版本 / Version**：v1.1.0_gemini  
**日期 / Date**：2026-06-21  

---

## 1. State Object JSON Schema (狀態物件規格)

Orchestrator Agent 在執行整個論文生產流水線時，必須在資料庫或記憶體中維護此 State Object。以下為其標準 JSON Schema 規格：

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ALE_State_Object",
  "type": "object",
  "required": ["research_id", "current_skill", "draft_version", "gate_status", "open_findings", "artifacts", "evidence_uri", "preprint_ready", "budget"],
  "properties": {
    "research_id": {
      "type": "string",
      "description": "研究案唯一識別碼，格式如 rp_2026_xxx"
    },
    "current_skill": {
      "type": "string",
      "enum": ["s00_ideate", "s01_consolidate", "s02_draft", "s03_review_loop", "s04_evidence", "s05_diligence", "s06_publication", "s07_retrospect"],
      "description": "當前正在執行或剛執行完的技能"
    },
    "draft_version": {
      "type": "string",
      "pattern": "^v[0-9]+(\\.[0-9]+)*$",
      "description": "草稿版本號，如 v1, v2.1"
    },
    "gate_status": {
      "type": "object",
      "required": ["G0", "G1", "G2", "G3", "G4", "G5", "G6"],
      "properties": {
        "G0": { "type": "string", "enum": ["pending", "pass", "fail"] },
        "G1": { "type": "string", "enum": ["pending", "pass", "fail"] },
        "G2": { "type": "string", "enum": ["pending", "pass", "fail"] },
        "G3": { "type": "string", "enum": ["pending", "pass", "fail"] },
        "G4": { "type": "string", "enum": ["pending", "pass", "fail", "blocked"] },
        "G5": { "type": "string", "enum": ["pending", "pass", "fail"] },
        "G6": { "type": "string", "enum": ["pending", "pass", "fail"] }
      }
    },
    "open_findings": {
      "type": "integer",
      "minimum": 0,
      "description": "未解決的審查意見（Findings）數量。G3 Gate 判定前必須為 0"
    },
    "artifacts": {
      "type": "object",
      "required": ["draft_uri", "references_dir"],
      "properties": {
        "draft_uri": { "type": "string", "description": "主稿 Markdown 檔案路徑" },
        "references_dir": { "type": "string", "description": "文獻存放目錄路徑" }
      }
    },
    "evidence_uri": {
      "type": "string",
      "description": "append-only 證據庫 URI，例如 git-commit-hash 或 object-store-hash"
    },
    "preprint_ready": {
      "type": "boolean",
      "description": "當 G4 被標記為 blocked 時，若此欄為 true 則可路由至預印本發布分支"
    },
    "budget": {
      "type": "object",
      "required": ["tokens_used", "limit"],
      "properties": {
        "tokens_used": { "type": "integer", "minimum": 0 },
        "limit": { "type": "integer", "minimum": 10000 }
      }
    }
  }
}
```

---

## 2. 核心技能 I/O JSON Schema (Skills Schemas)

### s02_draft.write (起草技能)
*   **輸入**：`positioning` (新穎性對位)、`RQ[]` (研究問題)。
*   **輸出 Schema**：
```json
{
  "type": "object",
  "required": ["draft_uri", "sections", "claims"],
  "properties": {
    "draft_uri": { "type": "string" },
    "sections": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 4
    },
    "claims": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["text", "level"],
        "properties": {
          "text": { "type": "string" },
          "level": { "type": "string", "enum": ["設計原則", "工程規格", "研究假說", "初步證據", "已驗證"] }
        }
      }
    }
  }
}
```

### s03_review.adversarialLoop (對抗審查技能)
*   **輸入**：`draft_uri` (待審草稿路徑)。
*   **輸出 Schema**：
```json
{
  "type": "object",
  "required": ["findings", "draft_uri_next", "no_overclaim"],
  "properties": {
    "findings": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "by", "claim_text", "verified", "fabricated", "resolution"],
        "properties": {
          "id": { "type": "string" },
          "by": { "type": "string", "enum": ["reviewer", "enhancer"] },
          "claim_text": { "type": "string" },
          "verified": { "type": ["boolean", "null"] },
          "fabricated": { "type": "boolean" },
          "resolution": { "type": ["string", "null"], "enum": ["applied", "rejected", null] }
        }
      }
    },
    "draft_uri_next": { "type": "string" },
    "no_overclaim": { "type": "boolean" }
  }
}
```

---

## 🤖 3. Gemini 編輯代理人操作細則 (Gemini Editor Agent Manual)

當下一代 Gemini Agent 被調度運行時，其主要職責為 **s03_review_loop** 中的 **Enhancer (形式化與補強)** 以及 **s05_diligence_check** 中的 **Citation Validator (文獻核檢)**。

為了使下一個 Gemini 能理解並無縫接軌工作，請嚴格遵守以下四個操作步驟與判定準則：

### 🛠️ 步驟 1：統計形式化審查 (Statistical Formalization Check)
當草稿中包含機率模型、統計估計或 LLM-as-a-judge 偏誤論證時，Gemini 必須執行數學核對。
1.  **檢查條件協方差**：
    *   公式形式：$\operatorname{Corr}\big(\operatorname{err}(PG), \operatorname{err}(V\&V) \mid C_{impl}\big) \longrightarrow 1$。
    *   **判定準則**：確認公式中的條件變數確實為「實作（$C_{impl}$）」，而非無條件的錯誤相關性。若文獻中宣稱「LLM 錯誤必定正相關」，必須修正為「在共享偏誤 $b$ 下的假說」。
2.  **變異 (Variance) 與偏誤 (Bias) 的區隔**：
    *   確認後文不可將「模型投票降 Variance」外推為「消除系統性偏誤（Bias）」。

### 🛠️ 步驟 2：不變量驗證代碼生成 (Spec Invariant Code Synthesis)
為滿足 §7.7 `spec_invariants` 機械閘的要求，Gemini 在審查代碼生成任務時，**必須**能自動提取系統紅線，並生成基於性質（Property-based）的 Python 測試代碼：
*   **代碼範本要求**：必須採用 `Hypothesis` 測試庫。
*   **範例結構**：
```python
# 必須包含給定資料生成器與物理限制 assert 語句
from hypothesis import given, strategies as st
@given(st.lists(...))
def test_invariant(self, data):
    # 執行待測邏輯
    # 斷言紅線邊界
```

### 🛠️ 步驟 3：文獻與先前技術核對 (Literature & Citation Audit)
在 `s05_diligence` 關卡，Gemini 必須扮演「對抗式文獻查核官」，查驗 `99_References` 目錄下 PDF 檔案的真實性，徹底杜絕 AI 幻覺與文獻誤讀：
1.  **核對真實存在性**：
    *   讀取 PDF 的第一頁，核對 Title、Author、Year 與 arXiv 編號是否與 `References` 與 `CITATION.cff` 記載一致。
2.  **防止文獻誤讀（P0 防線）**：
    *   **重點對象**：對 `arXiv:2512.03097` (Adversarial Consensus) 進行查驗。如果草稿中宣稱「該文證明增加 verifier 無效」，**必須予以駁回 (Reject)**。正確結論應為「該文的 verifier 連接外部 guidelines 時能將攻擊成功率降為 0%，屬於有效防禦」。
3.  **競爭先前技術核檢**：
    *   **重點對象**：`arXiv:2603.15611` (Code-A1)。Gemini 必須確認草稿已引述此文對 `self-collusion` 現象的發現，並將 ALE 框架的貢獻收斂在「完整 SDLC 的生命週期證據治理與 Skill FSM 整合」，不可侵佔前人的新穎性宣稱。

### 🛠️ 步驟 4：格式與學術排版調整 (Academic Formatting & Copy-Editing)
1.  **學術命名約束**：
    *   在處理 DOI 前置發布時，必須確保全域棄用撞名的 `Agentic Loop Engineering (ALE)` 標題。
    *   強制使用以下學術命名：
        *Title*: **Governing Agentic Software Development with Executable Evidence: Mechanical Gates, Human Review, and Skill Capitalization**
2.  **GenAI 使用揭露**：
    *   確認草稿已加入 `Generative AI Use Disclosure` 條款，明確寫出各模型（Claude, Codex, Gemini）的具體分工，且人類作者為責任人。

---

## 4. JSON-RPC 錯誤碼與異常處理 (Error Handling)

A2A Agent 在執行過程中，若遇到違反 `AGENTS.md §7` 之紅線或判定失敗時，必須拋出對應的標準錯誤：

```json
{
  "jsonrpc": "2.0",
  "error": {
    "code": 4031,
    "message": "INVARIANT_VIOLATION: Shared-context false pass detected. Verification gate failed to kill mutation.",
    "data": {
      "action": "halt_and_route_to_s07",
      "evidence_hash": "sha256:<RUNTIME_FILLS_REAL_DIGEST>",
      "timestamp": "<RUNTIME_FILLS_ISO8601>"
    }
  },
  "id": "req_01"
}
```

*   **`4001` Precondition Failed**：前置條件未滿足（例如在 G0 未過時執行 s02）。
*   **`4011` Schema Invalid**：技能輸出不符合 JSON Schema 約束。
*   **`4021` Self-Check Failed**：內部一致性自檢失敗（如發現程式碼無法通過語法檢查，容許重試 $\le 2$ 次）。
*   **`4031` Invariant Violation (Fatal)**：違反系統紅線（例如發現 `MODEL_PRODUCER == MODEL_REVIEWER`，或未經 primarySource 查證即標記 verified）。管線立即中止，並調度 `s07_retrospect` 寫入 Lessons learned。
*   **`4041` Gate Failed**：IF Gate 條件未通過，狀態回滾至前一階段。
*   **`4291` Budget Exceeded**：Token 或 API 消耗量超過全域 circuit breaker 限制，管線凍結並升級為人類手動介入。
