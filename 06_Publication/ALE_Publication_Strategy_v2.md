# ALE 發表與投稿路線策略
## Publication and Venue Strategy

---

**作者 / Author**：Morris（虎智科技 TigerAI）
**文件類型 / Type**：Publication & Venue Strategy
**版本 / Version**：v2（採納 Gemini 修訂:命名決策收斂與預印本工作流細化;取代 v1。原 v1、v1_gemini 保留）
**日期 / Date**：2026-06-21

> **核心前提與現狀**：ALE 目前處於**「理論框架（Framework）+ 單一田野觀察案例（N=1）」**的階段，受控實證研究（`EXP-001`）尚未執行。此階段的論文成熟度不支持直接投遞頂級經驗軟體工程期刊（如 IEEE TSE / ACM TOSEM）。本策略提供一條「搶先獲取 DOI 鎖定優先權 $\rightarrow$ 投遞 vision/practice 軌道 $\rightarrow$ 補充實證數據 $\rightarrow$ 投遞全文期刊」的階梯式發表路線圖。

---

## 1. 命名決策建議 (Naming & Subtitle Recommendation)

> ⚠ **已定案(2026-06-21,方案 B)** —— 原「System Development Agentic Loop Engineering (ALE)」**棄用**(撞 arXiv:2509.06216 §5.2 的 "Agentic Loop Engineering (ALE)")。下為定案標題:

- **正式標題 (Final)**：**Governing Agentic Software Development with Executable Evidence: Mechanical Gates, Human Review, and Skill Capitalization**  
  *理由:標題直含 **Mechanical Gates / Human Review / Skill Capitalization** 三關鍵詞 → 學術檢索曝光高;工程治理導向清楚;完全避開 ALE 撞名。*
- **內部代號**:ALE(TigerAI)— 內文/摘要可保留作專案代號,**但不宣稱 ALE 為學術命名原創**(與 arXiv:2509.06216 無關)。
- **對外一句話定位**:  
  > *From model consensus to executable evidence — an evidence-governed lifecycle for agentic software development.*(此為定位句/tagline,非標題)

---

## 2. 預印本與優先權鎖定工作流 (Pre-print Workflow)

為防範同領域研究搶先發表類似的 "test collusion" 概念，必須在本週內完成預印本發布以鎖定時間戳優先權。

### 2.1 Zenodo 寄存工作流 (立即執行)
Zenodo 是由 CERN 營運的開放科學儲存庫，上傳即可獲得永久性且具學術引用價值的 DOI。

1. **準備文件**：
   - 彙整 `02_Drafts/ALE_WhitePaper_v3.0.md`(現行主稿,轉換為 PDF)。
   - 在目錄下建立 `CITATION.cff` (引文格式描述檔) 與 `LICENSE` (CC BY 4.0)。
2. **Zenodo 註冊與上傳**：
   - 登入 Zenodo.org 並建立帳戶。
   - 上傳 PDF，選擇 **Publication** $\rightarrow$ **Technical Report** 或 **Working Paper**。
   - 填寫 Metadata：
     - Title: *Governing Agentic Software Development with Executable Evidence: Mechanical Gates, Human Review, and Skill Capitalization*
     - Authors: *Yeh-Hsing Lu*(ORCID 0009-0006-5373-0586;Tiger AI Tech)
     - Description: *白皮書之摘要文字。*
     - License: *Creative Commons Attribution 4.0 International (CC BY 4.0)*。
3. **獲取 DOI**：
   - 發布後立即獲取例如 `10.5281/zenodo.xxxxxxx` 的 DOI。

### 2.2 arXiv `cs.SE` (軟體工程) 提交
arXiv 為主流計算機科學預印本平台。

1. **格式轉換**：使用 Pandoc 將 Markdown 轉換為 LaTeX (arXiv 推薦 LaTeX 格式)。
2. **背書 (Endorsement)**：若帳戶需要背書，可請同領域已在 `cs.SE` 發表過文章之研究員點擊背書連結。
3. **提交類別**：首選 `cs.SE` (Software Engineering)，次選 `cs.AI` (Artificial Intelligence) 或 `cs.PL` (Programming Languages)。
4. **版本更新**：待 `EXP-001` 實驗數據產出後，直接在 arXiv 上傳 v2，arXiv 會保留歷史版本並維持原始提交的時間戳優先權。

---

## 3. 階梯投稿路線圖 (Venue Roadmap & Timeline)

```text
[階段 1: 立即] ──────> [階段 2: 2個月內] ───────> [階段 3: 6個月內] ───────> [階段 4: 1年內]
Zenodo (DOI)          IEEE Software (首投)       執行 EXP-001 (補數據)       JSS / IST 期刊
arXiv cs.SE           或 AIware/FORGE 研討會     與第二案例 (RQ3 數據)      (全文實證)
(鎖定優先權)           (Vision / Practice)        (提升成熟度至 L4)           (Peer-reviewed)
```

### 3.1 階段 2：現狀投稿首選 (Vision & Practice)
- **IEEE Software (雜誌)**：  
  *特點：實務與經驗導向，接受架構概念、治理框架與單一案例報告。對實驗規模無硬性要求，重在對業界的啟發性。*  
  *字數限制：通常 $\le 5400$ 字，重圖表與可讀性。*
- **AIware / FORGE (IEEE/ACM Joint Workshop)**：  
  *特點：專門收納 LLM 與軟體工程交叉領域的新想法（New Ideas）與早期成果（Early Results）。評審週期快。*

### 3.2 階段 4：實證全文投稿 (Full Journal)
在 `EXP-001` 與第二案例（補充 RQ3 技能重用之成本數據）完成後，將 ALE 升級為完整實證論文投稿：
- **Journal of Systems and Software (JSS)**：對框架與案例研究十分友善。
- **Information and Software Technology (IST)**：著重軟體方法論的實證評估。

---

## 4. 發表檢核清單 (Pre-Submission Checklist)

- [x] 名稱與副標題決策收斂。
- [x] 完成 `WhitePaper_v2.4_gemini` 中 Related Work 增補，就地引用 loop engineering 既有實務。
- [x] 準備好 CC BY 4.0 宣告與 `CITATION.cff`。
- [ ] 執行 `EXP-001` 的 pilot，並將 false-pass rate 回寫白皮書 §9.7。
- [ ] 將白皮書轉換為 PDF，並利用 Pandoc 輸出 LaTeX 備用。

---

*— End of Publication Strategy v1_gemini —*
