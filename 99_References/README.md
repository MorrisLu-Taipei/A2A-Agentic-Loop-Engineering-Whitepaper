# ALE 參考文獻庫與索引（99_References）

本目錄是 ALE 白皮書(`../02_Drafts/ALE_WhitePaper_v2.5.md`)的**參考文獻全文庫與索引**。收錄已可取得 PDF 全文之文獻,並為**每一條**參考文獻記錄:核驗後的書目資料、與 ALE 的關係、取得狀態與本地檔名。

- **核驗原則**:arXiv 文獻下載前先以 arXiv API(`export.arxiv.org/api/query?id_list=...`)逐筆比對「編號 ↔ 題名 ↔ 發表日」;非 arXiv 文獻取官方出處。
- **下載日期**:2026-06-21。
- **檔名規則**:arXiv → `arXiv_<id>_<作者年_短題>.pdf`;其他 → `<會議年_作者_短題>.pdf`。
- **著作權**:所有 PDF 著作權屬原作者,本目錄僅供內部研究核驗。

> ⚠ **核驗更正紀錄**:先前 Web 檢索曾誤報 `2512.03097` 為「2024-12」;經 arXiv API 確認實際首次發表為 **2025-12-01**。其餘 arXiv 編號與題名全部吻合。

---

## A. 館藏狀態總覽

| 類別 | 數量 | 狀態 |
|---|---|---|
| arXiv 全文(已核驗、已下載) | 10 | ✅ 本目錄 |
| USENIX 全文(已下載) | 1（in-toto） | ✅ 本目錄 |
| 標準/文件站(存連結) | 2（SLSA、MCP） | 🔗 連結 |
| 書籍/期刊/技術報告(需另購/館藏) | 8 | 📚 外部 |
| **合計白皮書參考文獻** | **22** | — |

---

## B. 已下載全文（11 篇）

### B-1. 核心論點直接相關（shared-context false pass / verifier / oracle）

| Ref | 檔案 | 書目(核驗) | 與本文的關係 |
|---|---|---|---|
| 23 | `arXiv_2603.15611_2026_Code-A1_self-collusion.pdf` | *Code-A1: Adversarial Evolving of Code LLM and Test LLM via RL*, arXiv:2603.15611(2026-03-16) | ★★ **直接 prior art**:已用 *self-collusion* 描述 code/test 問題,解法為模型分離。本文據此**不主張命名/特化原創**,改定位「整合進 SDLC」 |
| 17 | `arXiv_2512.03097_..._Collusion.pdf` | *Many-to-One Adversarial Consensus...*, arXiv:2512.03097(2025-12-01) | ★ **正確解讀(v3.0 已更正)**:多代理人**共識**不安全(ASR→100%),但**外部指南 verifier 將 ASR→0%**(verifier 有效)。支撐「外部證據 > 模型共識」,**非**「verifier 擋不住」 |
| 18 | `arXiv_2603.20281_..._Fragility...pdf` | *On the Fragility of AI Agent Collusion*, arXiv:2603.20281(2026-03-18) | ○ 相關性**較弱**(主題偏定價演算法共謀);僅作旁證 |
| 20 | `arXiv_2512.02682_2025_Taxonomy-LLM-to-LLM-Risks.pdf` | *Beyond Single-Agent Safety: A Taxonomy of Risks in LLM-to-LLM Interactions*, arXiv:2512.02682(2025-12-02) | ★ 把 test collusion 定位進 LLM-to-LLM 風險分類體系 |
| 19 | `arXiv_2510.04303_2025_Audit-the-Whisper-Steganographic-Collusion.pdf` | *Audit the Whisper: Detecting Steganographic Collusion in Multi-Agent LLMs*, arXiv:2510.04303(2025-10-05) | 相鄰證據:共謀可經隱寫通道,強化「模型評議不可定生死」 |

### B-2. Agentic SWE / 評測基準 / LLM 評審偏誤

| Ref | 檔案 | 書目(核驗) | 與 ALE 的關係 |
|---|---|---|---|
| 16 | `arXiv_2509.06216_2025_Agentic-SWE-Roadmap.pdf` | *Agentic Software Engineering: Foundational Pillars and a Research Roadmap*, arXiv:2509.06216(2025-09-07) | §2.7 最該對位的研究路線;ALE 補其「生成之後的治理」一環 |
| 15 | `arXiv_2310.06770_Jimenez2023_SWE-bench.pdf` | *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*, arXiv:2310.06770(2023-10-10), ICLR 2024 | 代表「衡量生成能力」的基準;ALE 與之互補(衡量治理) |
| 21 | `arXiv_2306.05685_Zheng2023_LLM-as-Judge_MT-Bench.pdf` | *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*, arXiv:2306.05685(2023-06-09), NeurIPS 2023 | LLM-as-judge 自我偏好/位置/冗長偏誤;支持 §7.2「模型評議是相關估計器」 |

### B-3. Agentic 方法論基礎

| Ref | 檔案 | 書目(核驗) | 與 ALE 的關係 |
|---|---|---|---|
| 9 | `arXiv_2210.03629_Yao2022_ReAct.pdf` | *ReAct: Synergizing Reasoning and Acting in Language Models*, arXiv:2210.03629(2022-10-06) | §2.2 agentic 推理-行動迴圈之來源 |
| 11 | `arXiv_2305.14325_Du2023_Multiagent-Debate.pdf` | *Improving Factuality and Reasoning through Multiagent Debate*, arXiv:2305.14325(2023-05-23) | §2.2 多代理人辯論;ALE 指出其改善 variance 非 bias |
| 10 | `arXiv_2203.11171_Wang2022_Self-Consistency.pdf` | *Self-Consistency Improves Chain of Thought Reasoning*, arXiv:2203.11171(2022-03-21) | §2.2 自我一致性取樣 |

### B-4. 供應鏈來源證明

| Ref | 檔案 | 書目(核驗) | 與 ALE 的關係 |
|---|---|---|---|
| 13 | `USENIX2019_Torres-Arias_in-toto_supply-chain.pdf` | Torres-Arias, S., Ammula, A. K., Curtmola, R., & Cappos, J. (2019). *in-toto: Securing the Software Supply Chain.* 28th USENIX Security Symposium, 1351–1367 | §8.5 技能供應鏈安全(簽章/來源證明)之方法基礎 |

---

## C. 存連結（非 PDF;標準/文件站)

| Ref | 文獻 | 連結 | 與 ALE 的關係 |
|---|---|---|---|
| 12 | SLSA — Supply-chain Levels for Software Artifacts, v1.0 Spec (OpenSSF, 2023) | https://slsa.dev/spec/v1.0/ | §8.5 技能晉升/簽章之分級框架 |
| 14 | Model Context Protocol (MCP) Specification v0.1.0 (Anthropic, 2024) | https://modelcontextprotocol.io | §2.5/§5.4 技能封裝與跨代理人調用介面 |
| 22 | Data Science Dojo (2026). *Agentic Loops: From ReAct to Loop Engineering (2026 Guide)* | https://datasciencedojo.com/blog/agentic-loops-explained-from-react-to-loop-engineering-2026-guide/ | §2.7 證明「loop engineering」為既有公共術語;ALE 讓出此公共財 |

---

## D. 外部館藏（書籍/期刊/技術報告;需另購或機構館藏)

| Ref | 文獻 | 出處 | 與 ALE 的關係 |
|---|---|---|---|
| 1 | DeMillo, Lipton & Sayward (1978). *Hints on Test Data Selection.* | IEEE Computer 11(4) | §2.3 突變測試之源頭 |
| 2 | Claessen & Hughes (2000). *QuickCheck.* | ICFP | §2.3/§7.7 性質導向測試 |
| 3 | Chen, Cheung & Yiu (1998). *Metamorphic Testing.* | Tech. Report HKUST-CS98-01 | §7.7 蛻變關係/需求不變量 |
| 4 | Barr, Harman, McMinn, Shahbaz & Yoo (2015). *The Oracle Problem in Software Testing: A Survey.* | IEEE TSE 41(5), 507–525 | §2.7/§7.3 測試 oracle 問題;ALE 不變量為 partial oracle |
| 5 | Kim, Humble, Debois & Willis (2016). *The DevOps Handbook.* | IT Revolution Press | §2.1 DevOps 理念 |
| 6 | Forsgren, Humble & Kim (2018). *Accelerate.* | IT Revolution Press | §2.1 以度量驅動改善 |
| 7 | Shostack (2014). *Threat Modeling: Designing for Security.* | Wiley | §2.5/§8 STRIDE 威脅建模 |
| 8 | Dietterich (2000). *Ensemble Methods in Machine Learning.* | Springer LNCS 1857 | §2.4/§7.2 集成需成員獨立性(相關估計器論證之依據) |

---

## E. 取得指令(可重現)

```bash
# arXiv 核驗(下載前)
curl -sSL "https://export.arxiv.org/api/query?id_list=<ID1>,<ID2>,...&max_results=20"
# arXiv 全文
curl -sSL -o "arXiv_<id>_<name>.pdf" "https://arxiv.org/pdf/<id>"
# in-toto (USENIX)
curl -sSL -o "USENIX2019_Torres-Arias_in-toto_supply-chain.pdf" \
     "https://www.usenix.org/system/files/sec19-torres-arias.pdf"
```

---

## F. ✅ Gate-Review Checklist — 證據主幹(非階段,橫貫全程)

`99_References` 對應 ALE 的 **Evidence Repository**:append-only、可核驗、全程回饋各階段。

- [x] 白皮書所有 **arXiv 引文**已下載 PDF(10 篇)
- [x] 每篇**下載前經 API 核驗**(編號↔題名↔日期)
- [x] PDF 完整性檢查(magic-byte `%PDF`)
- [x] in-toto(USENIX)全文已補
- [x] 核驗更正紀錄(2512.03097 日期)留存
- [ ] ⚠ 非 arXiv 文獻(SLSA/MCP 連結;書籍/期刊館藏)正式核驗
- [ ] 投稿前:對現行檔案產生真實 SHA-256 證據鏈

> 規則:**被引用但未入庫/未核驗的文獻 = G5 不過**(見 `../05_DueDiligence/`)。

---

*產製:虎智科技 TigerAI｜下載與核驗日期 2026-06-21｜對應白皮書 `../02_Drafts/ALE_WhitePaper_v2.5.md` §參考文獻。*
