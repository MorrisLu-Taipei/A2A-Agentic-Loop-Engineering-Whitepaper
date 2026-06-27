# 預印本 DOI 上傳清單（Zenodo,可在 G4 前先走)

**目的**:先發預印本取 DOI,鎖住「shared-context false pass / 機械閘 / Skill Capitalization」的**時間優先權**。Zenodo(CERN 營運)上傳即發永久 DOI。
**誠實前提**:上傳的是 **Working Paper v3.2**,核心主張多為 `[研究假說]`/`[初步證據]`,**無 `[已驗證]`**——這點白皮書已標明,正是可以誠實先發的原因。**正式 full paper 仍須過 G4。**
**命名**:對外框架名採 **Agentic Loop Engineering(ALE)**,但**不宣稱首創此名詞**(arXiv:2509.06216 §5.2 已用);論文標題維持描述性題名。

> 🚦 **目前 GO 狀態(2026-06-22,依 Codex v3.1 前審 + v3.2 修正)**:
> - ✅ **可建立 Zenodo Draft**、✅ **可按「Get a DOI now」預留 DOI**。
> - ❌ **先不要 Publish**;❌ 不要把現版本當成正式 DOI 發布完成。
> - v3.2 已修:命名定位、版本/metadata、§7.7 測試、4.5× 改寫、揭露對齊、絕對語句軟化、**#14/#22 文獻核驗完成**、**§9.7 表格排版修復**、Zenodo 指南 v3.0 殘留清除。
> - **最終 GO 前人工關卡**:全文逐頁人讀核可(+ 視需要做系統性文獻回顧)。通過後才 Publish。

> ⚠ 我(Claude)**無法替你上傳**(需你的 Zenodo 帳號)。本檔備妥所有素材與步驟,你照做即可。

> 🔒 **機密鐵則(發表前必查)**:TigerAI 專有交付 **skill set 是商業機密**。論文/DOI/venue 任何對外輸出**只能用抽象摘要**(它「大概做什麼」),**絕不可**寫出技能清單、資料契約內容、內部結構、檔案路徑或實作。上傳前 grep 確認 PDF 不含這些細節。

---

## A. 上傳前準備
1. **要上傳的檔案**:`02_Drafts/ALE_WhitePaper_v3.2_EN.md`(現行)→ 已備 PDF `06_Publication/ALE_WhitePaper_v3.2_EN.pdf`。
   - Docker 一行轉檔(如需重產):
     ```bash
     docker run --rm -v "$PWD:/data" pandoc/latex \
       02_Drafts/ALE_WhitePaper_v3.2_EN.md -o ALE_WhitePaper_v3.2_EN.pdf \
       --pdf-engine=xelatex -V CJKmainfont="Noto Sans CJK TC"
     ```
   - 可一併附:`CITATION.cff`、`LICENSE`。**⚠ 不要附 `AUTHOR.md`(仍含 `[請補充]` 與內部資訊)、不要附內部研究日誌。**
2. **LICENSE**:已備 `../LICENSE`(CC BY 4.0 全文)。
3. **CITATION.cff**:已備 `../CITATION.cff`(已填 ORCID + v3.2 標題/版本)。
4. **GenAI 使用揭露**:v3.2 已含揭露段(來源見 `../08_Methodology/`);Zenodo description 也加一句「AI-assisted; human author accountable; AI not an author」。

## B. Zenodo metadata(直接貼)
| 欄位 | 值 |
|---|---|
| Upload type | Publication → **Working paper**(或 Technical report) |
| Title | **Governing Agentic Software Development with Executable Evidence: Mechanical Gates, Human Review, and Skill Capitalization**(v3.2;對外框架名 Agentic Loop Engineering(ALE),不宣稱首創此名詞) |
| Authors | Lu, Yeh-Hsing (Morris) |
| Affiliation | Tiger AI Tech Co., Ltd. |
| ORCID | 0009-0006-5373-0586　**⚠ 用 ORCID 登入 Zenodo 再 deposit**(作品才會自動寫回 ORCID;否則只是顯示) |
| Description | 用白皮書中文/英文摘要(Working Draft;主張為研究假說,實驗 EXP-001/EXP-002 進行中) |
| Version | **3.2** |
| Language | Chinese (zh) / 可加 English |
| License | **Creative Commons Attribution 4.0 International (CC BY 4.0)** |
| Keywords | Agentic AI; SDLC; shared-context false pass; mechanical gate; skill capitalization; multi-agent; verifiability; DevSecOps |

## C. 上傳步驟
1. 登入 https://zenodo.org → New upload。
2. 拖入 `ALE_WhitePaper_v3.2_EN.pdf`(+ 選附 CITATION.cff / LICENSE)。
3. 依上表填 metadata;License 選 CC BY 4.0。
4. Publish → 取得 DOI(形如 `10.5281/zenodo.XXXXXXX`)。
5. **回填**:把 DOI 寫回 `../CITATION.cff`(取消 identifiers 註解)、`RESEARCH_LOG.md`、白皮書引用格式。

## D. (可選,稍後)arXiv `cs.SE`
- 需:**ORCID**、LaTeX 版(pandoc 轉 `.tex`)、首投需 **endorsement**(可洽已在 cs.SE 發表過之同仁/共同作者)。
- arXiv 與 Zenodo 可並存;arXiv 之 v1 時間戳亦具優先權。

## D2. 發布封裝:只上傳這些 / 絕不上傳這些（Codex+Gemini 一致)
**只上傳(最小集)**:
- `ALE_WhitePaper_v3.2_EN.pdf`(主稿;PDF metadata title/author 與 Zenodo 一致)
- `CITATION.cff`、`LICENSE`
- (可選)`spec_invariants_engine.py` 教學範例

**絕不上傳(會污染學術紀錄/洩漏)**:
- ❌ `AUTHOR.md`(含 `[請補充]` + 街道地址 + 內部協作備忘)
- ❌ `03_Reviews/`(AI 審閱軌跡,內部用)
- ❌ `RESEARCH_LOG.md`、`07_Lessons_Learned/`(內部研發日誌)
- ❌ `04_Evidence/experiments/` **未完成 runner 原始碼**(含 `NotImplementedError`,會被當 vaporware)
- ❌ 商業機密(skill set 細節 — 已抽象化,但連抽象檔也不必上傳)
- ❌ 任何含內部相對路徑、`待補`、`Working Draft 尚未達門檻` 等編輯標記的檔

## E. 發佈後同步
- [ ] DOI 回填 CITATION.cff / RESEARCH_LOG / 白皮書
- [ ] README 頂部加 DOI badge/連結
- [ ] G6 checklist 之「Zenodo DOI」打勾(`06_Publication/README.md`)

> 名稱/副標**最終以 Founder 拍板為準**;若改名,Title 與 CITATION.cff 一併更新後再上傳。
