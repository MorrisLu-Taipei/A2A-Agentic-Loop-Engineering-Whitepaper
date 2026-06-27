# SKILL-9 · Deep Literature Research (探索 + 查證)

> A2A 技能契約(機器可讀)。補上 ALE 既有 WF-4/WF-7 的能力洞:它們只**驗證**一筆已知引用、且**只接 arXiv**;SKILL-9 是**發現**未知的頂級論文並讀全文查證。
> 對應 n8n:`n8n_workflows/WF-9_Deep-Literature-Discovery-Verify.json`。隸屬流程階段:**01 Consolidation(prior-art)** 與 **05 DueDiligence(引文核驗)**;課程對應 **W4 查證**。

---

## 0. 為什麼需要這個技能(問題陳述)

| | WF-4 / WF-7(既有) | **SKILL-9 / WF-9(新增)** |
|---|---|---|
| 任務 | 驗證**你已有的一筆引用** | **發現你還不知道的論文** + 查證 |
| 來源 | **僅 arXiv**(預印本) | **OpenAlex / Semantic Scholar / Crossref**(涵蓋 IEEE/ACM/Springer/Elsevier 等**頂級期刊與會議**) |
| 讀取 | 只比對 metadata(title/year) | 兩階段:掃摘要 → **抓 OA 全文閱讀** |
| 結論查證 | 無(這就是 2512.03097 被講反卻沒擋下的洞) | **強制全文核對主張方向** |
| 風險控制 | — | DOI 驗活 + **預設不可引用,須人核** |

> 一句話:arXiv 查不到「頂級論文」,因為很多頂級成果在**同儕審查的期刊/會議**、不在 arXiv。要查它們,得接**學術索引(OpenAlex/Semantic Scholar/Crossref)**,不是只接 arXiv。

---

## 1. Skill 契約(Contract)

```json
{
  "skill_id": "deep_literature_research",
  "version": "1.0.0",
  "purpose": "Discover top-tier peer-reviewed papers across academic indexes, read full text, and verify before citation.",
  "stage": ["01_Consolidation", "05_DueDiligence"],
  "input": {
    "query": "string (research topic / question)",
    "per_page": "int (default 5)",
    "min_year": "int (optional)",
    "sources": "string[] (default ['openalex']; may add 'semantic_scholar','crossref')"
  },
  "output": {
    "candidates": [{
      "title": "string", "year": "int", "venue": "string",
      "cited_by": "int", "doi": "string|null", "doi_live": "bool",
      "is_oa": "bool", "oa_url": "string|null",
      "gate": {
        "can_cite": "bool (always false from the agent)",
        "needs_fulltext_read": "true",
        "human_review_required": "true",
        "reason": "string"
      }
    }]
  }
}
```

## 2. Pipeline(七步,對齊 deep-research 範式)

1. **Plan** — 把研究問題拆成查詢詞(同義詞、領域術語)。
2. **Discover(多源)** — OpenAlex `api.openalex.org/works?search=…`(免金鑰;`mailto=` 進 polite pool)。可並聯 Semantic Scholar `api.semanticscholar.org`、Crossref `api.crossref.org`。
3. **Screen(兩階段)** — 先掃**摘要**(100+),依被引數/相關度排序;選高相關者進下一步。
4. **Fetch full text** — 取 OA 全文(OpenAlex `open_access.oa_url` / Unpaywall);無 OA 則標 `fulltext_unavailable`,**不得**僅憑摘要定論。
5. **Verify(關鍵)** — **讀全文核對主張方向**(不是只確認標題存在);**DOI 對 doi.org 發 HTTP 驗活**。
6. **Critique loop** — 對抗式自評:「有沒有把結論讀反?有沒有把弱相關當強相關?」(對應 WF-3 reviewer)。
7. **Gate** — 見 §3。

## 3. Gate 述詞(Gate Predicate)

```
can_cite(paper) := doi_live(paper)
                 AND fulltext_read(paper)
                 AND conclusion_matches_claim(paper)   // 人讀全文核對
                 AND human_approved(paper)
```
**任一為偽 → 不得寫入稿件引用。** Agent 永遠輸出 `can_cite=false`;`true` 只能由人類複核後賦予。

## 4. 錯誤碼(沿用 A2A_SKILLSET §4)

| code | 意義 |
|---|---|
| 4041 | `SOURCE_UNREACHABLE`:索引 API 不可達(記錄、不可假裝成功) |
| 4042 | `FULLTEXT_UNAVAILABLE`:無 OA 全文 → 僅憑摘要,降級為「待人取全文」 |
| 4043 | `DOI_DEAD`:DOI 無法驗活 → `doi_live=false`,不可引用 |
| 4031 | `CONCLUSION_MISREAD`:全文與草稿主張方向不符(就是 2512.03097 那種反向錯)→ 駁回並記 Lessons |

## 5. 紅線(Red Lines)

- **探索 agent 可以幻覺 → 所以一律不直接採信**:每筆都要過「全文 + DOI 驗活 + 人核」。
- **不得把摘要當全文結論**;不得把弱相關列為支持證據。
- 模型呼叫走**通用 OpenAI 相容端點**;通知節點 stub;全程 **Docker** 可帶走(不依賴本機)。
- 不外洩任何 token / 金鑰 / 商業機密。

## 6. 取捨說明(為何不照搬 Scopus 範式)

参考實作 Deep-Research-Agent 用 **Scopus(`scopus-mcp`,需 Elsevier 金鑰,付費)** + Exa。本技能預設走**免金鑰的 OpenAlex + Semantic Scholar + Crossref + Unpaywall**——已涵蓋多數頂級期刊/會議的 metadata 與大量 OA 全文,讓「零金鑰可跑」成立;有 Scopus/Exa 金鑰時再加掛。

---

*產製:TigerAI 虎智科技｜本技能為 ALE 方法論之查證能力升級;改版遞增版號、保留舊版。*
