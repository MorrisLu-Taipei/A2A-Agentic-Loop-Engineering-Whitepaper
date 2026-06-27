# DOI 申請與註冊指南（含踩坑 Lessons Learned)

> 適用於 TigerAI 的所有研究產出(不只 ALE)。**DOI 是好東西**:它把「研究工作」與「論文發表準備」變成**可引用、可追溯、有時間戳優先權**的正式紀錄——即使論文還沒投出去,先發預印本拿 DOI,就等於把你的想法「蓋了郵戳」。

---

## 1. DOI 是什麼、為什麼要先拿

- **DOI(Digital Object Identifier)**:一個永久、不會失效的識別碼(如 `10.5281/zenodo.20261681`),指向你的研究產物。
- **為什麼對我們有用**:
  1. **記錄研究工作**:白皮書、工具包、資料集、報告都能各拿一個 DOI,成為正式學術紀錄。
  2. **時間戳優先權**:先發預印本拿 DOI = 公開宣告「這想法我某月某日就提出了」,防止被搶先。
  3. **可引用**:別人(和你自己的後續論文)能正式 cite。
  4. **發表準備**:預印本 DOI **通常**可在投正式期刊/研討會前先發,但**每個 venue 的 prior-publication / preprint policy 不同,投稿前務必逐一查證**(部分 venue 對預印本有限制)。
- **重點觀念**:**DOI ≠ 同行評審**。預印本 DOI 只證明「存在且公開」,不代表結論被驗證——所以 working draft 也能誠實地先發。

---

## 2. 平台選擇

| 平台 | 角色 | 費用 | 何時用 |
|---|---|---|---|
| **Zenodo** | 開放儲存庫(CERN 營運),上傳即發 DOI(由 DataCite 鑄造) | 免費 | **首選**:白皮書/工具包/資料集/報告 |
| **DataCite** | Zenodo 背後的 DOI 註冊機構 | (Zenodo 已含) | 不用直接操作;但 ORCID 自動同步靠它(見 §4) |
| **arXiv** | 預印本平台(有自己的 ID,也可掛 DOI) | 免費 | cs.SE 等;首投需 endorsement + LaTeX + ORCID |
| **Crossref** | 期刊 DOI 註冊機構 | (出版社處理) | 正式期刊發表時,由出版社負責 |
| **OSF** | 另一個開放研究平台,可發 DOI | 免費 | 替代/補充 Zenodo |

> 我們的常規:**Zenodo 先發預印本 DOI(立即)→ 之後正式期刊由出版社給 Crossref DOI**。兩者並存。

---

## 3. Zenodo 申請步驟(標準流程)

1. **準備檔案**:把要發的文件轉 PDF(中文可先 DOCX 再另存 PDF);可附 `CITATION.cff` / `LICENSE`。
2. **登入 Zenodo**:`zenodo.org`。**⚠ 用 ORCID 登入/連結帳號**(見 §4 為什麼很重要)。
3. **New upload** → 拖入檔案。
4. **填 metadata**:
   - Upload type(Publication → Working paper / Technical report / Preprint;或 Software / Dataset)
   - Title、Authors(**選你已驗證的 ORCID**)、Affiliation
   - Description(摘要)、Version、Language、Keywords
   - **License**(文件建議 CC BY 4.0;程式 Apache 2.0)
5. **Publish** → 立即取得 DOI。
6. **版本觀念**:Zenodo 給兩種 DOI——
   - **Concept DOI**(代表「這個作品的所有版本」,永遠指向最新)
   - **Version DOI**(指向某一特定版本)
   - 改版時用「New version」上傳,Concept DOI 不變、Version DOI 遞增。**引用通常用 Concept DOI。**
7. **回填**:把 DOI 寫回 `CITATION.cff`、研究紀錄、白皮書引用格式。

---

## 4. ⚠ Lessons Learned:ORCID 沒自動同步(真實踩坑,2026-06-21)

### 狀況
作者已發兩筆 Zenodo(`10.5281/zenodo.20261681`、`10.5281/zenodo.20264772`),作者欄也**顯示**了 ORCID(`0009-0006-5373-0586`)。但查 ORCID 公開 API,名下 **works = 0**——這兩筆**完全沒進**個人 ORCID 紀錄。

### 根因
- **在 Zenodo 作者欄「打字填 ORCID」只會顯示,不會回寫你的 ORCID 紀錄。**
- 要自動寫回,需滿足:① ORCID 是「**已驗證**」(你用 ORCID **登入** Zenodo,而非純文字輸入);② **DataCite** 取得授權去更新你的 ORCID。
- 兩者都沒做 → DataCite 不推送 → ORCID 一片空白。

### 解法(做一次)
**A. 把既有的補進去**
- ORCID → **Works → Add → Search & link → 選 DataCite** → 授權 → 匯入;
- 或 **Add DOI** 手動貼 DOI。

**B. 讓以後自動同步**
- ORCID → **Trusted organizations**:允許 **DataCite(和 Crossref)** auto-update;
- Zenodo → **用 ORCID 登入/連結帳號**,之後 deposit 帶「已驗證」iD,新作品自動進 ORCID。

### 教訓(寫死成 SOP)
> **每次上 Zenodo:先用 ORCID 登入,再 deposit。** 純文字填 iD = 不會進你的學術紀錄。發完到 ORCID 確認 works 數有增加,才算真的「記錄」成功。

---

## 4b. ORCID「手動新增 work」欄位對照（Add work manually)

> 優先用 **Search & link → DataCite**(貼 DOI 自動匯入);搜不到才手填。手填對照:

| ORCID 欄位 | 怎麼填 |
|---|---|
| **Work type ✱** | Software(工具包)/ Preprint(預印本)/ Working paper(白皮書) |
| Title ✱ | 作品全名 |
| **Add external identifier ✱(關鍵)** | type=**DOI**,value=`10.5281/zenodo.XXXX`,relationship=**Self** ← 沒填等於白做 |
| Publication date | 發表年月(如 2026-05) |
| Work subtitle | 有副標才填,否則留空 |
| **Journal title** | **留空**(非期刊;Zenodo 不是 journal) |
| Language used in this form | 你輸入文字的語言(英文標題→English;中文→Chinese Traditional) |
| Country/Location of publication | 非必填;可填 Taiwan 或留空 |

## 5. 下一個 DOI 的檢查清單(含 ALE)

- [ ] 檔案轉 PDF(中文字型 OK、圖表有渲染)
- [ ] `CITATION.cff` 完整(title、作者、**已驗證 ORCID**、version、license)
- [ ] `LICENSE` 就位(CC BY 4.0 / Apache 2.0)
- [ ] 機密終檢:無商業機密(如 skill set 細節)、無 placeholder
- [ ] **用 ORCID 登入 Zenodo** → deposit
- [ ] 選對 Upload type + License + Keywords
- [ ] Publish → 取 DOI
- [ ] **回 ORCID 確認 works +1**(沒有就手動 Add DOI)
- [ ] DOI 回填 CITATION.cff / RESEARCH_LOG / 白皮書

---

## 6. 我們已有的 DOI(登錄)
| DOI | 作品 | 類型 |
|---|---|---|
| 10.5281/zenodo.20261681 | GenAI Consulting Methodology Toolkit | Software |
| 10.5281/zenodo.20264772 | AI-Native eBook Production(Design Science) | Preprint |
| (待發) | ALE White Paper v2.5 | Working paper |

> ⚠ 前兩筆需依 §4-A 手動補進 ORCID。

---
*本指南適用 TigerAI 所有研究發表;ALE 專用上傳步驟見 `ZENODO_SUBMISSION.md`。*
