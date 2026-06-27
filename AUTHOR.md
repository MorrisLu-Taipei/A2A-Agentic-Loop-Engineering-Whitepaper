# 作者介紹 · About the Author

> 本檔為**可編輯初稿**(Claude 代擬,作者自行修改)。公開可用之公司資料已預填;個人學經歷以 `[請補充]` 標示。
> 目的有二:(1) 作者簡介;(2) **示範「如何從自我盤點(self-inventory)找出研究主題」**——以 ALE 本身為活例子。

---

## 1. 作者簡介（Bio)

**盧業興 Yeh-Hsing "Morris" Lu**
創辦人暨執行長｜虎智科技 Tiger AI Tech Co., Ltd.
n8n 台北大使 n8n Taipei Ambassador

- **Headline(建議,可改)**:Tiger AI Tech 共同創辦人｜n8n Taipei Ambassador｜專注可治理、可落地的 Agentic AI 工程
- **專業領域**:AI 平台架構、Agentic 軟體工程、地端/受監管產業 AI 導入、顧問方法論(技能:Generative AI、Prompt Engineering、PyTorch)
- **代表性實作**:電子發票開放資料儀表板(本研究實證案例;**線上 Demo**:https://tigerai-ai-dashboard-demo.yesinlu.workers.dev )、[請補充:競標系統、其他]

### 學歷（Education)
- **資訊科技碩士 (M. Information Technology)** — Queensland University of Technology (QUT), Australia(2003–2005;主修 Internet Commerce & Business Intelligence;SIG Enterprise Process Management)
- 人工智慧博士班**肄業**,國立臺灣科技大學 NTUST(2022–2026;研究接觸 Prompt Engineering)。
  > [作者自行決定是否列出此項;若不列可整行刪除]

### 經歷（Experience)
- **共同創辦人** — 虎智科技 Tiger AI Tech(2024-01 – 迄今;Taipei,Hybrid;PyTorch、Generative AI 等)
- **n8n Taipei Ambassador** — n8n(2025-12 – 迄今)
- **共同創辦人** — n8n Taiwan User Group(2025-02 – 迄今;Taipei;Generative AI、Prompt Engineering)
- **副總經理 (Vice President)** — 宏麗數位 yuTOUCH Interactive Tech(力晶集團 Powerchip Group;2016 – 2021)
- **專案顧問 (Project Consultant)** — 台灣賽仕電腦軟體 SAS Taiwan (SAS Institute)(2010 – 2012)
- **專案管理顧問 (PM Consultant)** — 精誠資訊 Systex Corporation([請補充起訖年])
- **技術部副理 (Tech Assistant Manager)** — 台灣大哥大 Taiwan Mobile Co., Ltd.([請補充起訖年])
- **專業證照**:
  - **PMP** — Project Management Professional,Project Management Institute(Credential ID 573170)
  - **n8n Level 1 Certification** — n8n(2024-09;技能:Generative AI、Prompt Engineering)
  - **MCP** — Microsoft Certified Professional,Microsoft(Credential ID 973788)
- **研究興趣**:當 AI Agent 接手軟體生命週期時的**治理與可驗證性**——尤其「驗證 AI 的也是 AI」所衍生的可信度問題。

**聯絡**
- Email:morrislu@tigerai.tw ｜ tiger.ai.tw@gmail.com
- 公司:虎智科技 Tiger AI Tech Co., Ltd.(統編 93489997)
- 地點:臺北 Taipei, Taiwan(詳細地址見正式公司文件,不於公開 repo 列出)
- LinkedIn:https://www.linkedin.com/in/morris-lu-89144821/
- ORCID:https://orcid.org/0009-0006-5373-0586
- 作品 Demo(電子發票開放資料儀表板):https://tigerai-ai-dashboard-demo.yesinlu.workers.dev
- [請補充:個人網站 / 其他作品]

> 📌 投稿小提醒:ORCID 已具備;上 Zenodo/arXiv 時**用 ORCID 登入再 deposit**,作品才會自動進你的 ORCID 紀錄(見 `06_Publication/DOI_GUIDE.md`)。

---

## 2. 研究緣起:從「自我盤點」到「研究主題」

ALE 不是先有理論、再找題目;而是**先有真實的痛,盤點之後才浮出主題**。這正是本研究想示範的方法:

> **研究主題不必向外找,先向內盤點自己做過的事、踩過的坑。** 一個一再出現的結構性痛點,就是一篇論文的種子。

### ALE 的真實緣起(worked example)
1. **做了一個真案子**:電子發票開放資料儀表板(地端、Docker、AI 問數)。
2. **踩到一個真坑**:用「儀表板值 vs 資料庫值」互相驗證,兩邊都 PASS——但兩邊吃的是同一份**膨脹 4.5 倍**的資料,「一起錯還互相背書」。
3. **盤點時問自己**:這只是個 bug,還是一個**會反覆出現的結構性問題**?
4. **發現它有普遍性**:當「產生的」與「驗證的」共享同一個來源/偏誤,驗證就會假性通過——尤其當兩者都是 AI 時(PG Agent 寫碼、V&V Agent 從實作生成測試)。
5. **命名 + 上升為理論**:把它命名為 **test collusion**,再推出解方(機械閘優先於模型共識)——ALE 因此成形。

> 一句話:**「一個真實專案的踩坑紀錄(LESSONS_LEARNED #3),長成了一篇白皮書的核心論點。」**

---

## 3. 方法:自我盤點 → 研究主題（可重複的五步)

給任何想從自身實務找研究題目的人(這也是 TigerAI 顧問方法論的一環):

| 步驟 | 做什麼 | 在本卷宗對應 |
|---|---|---|
| **① 盤點實作** | 列出自己做過的真實專案、交付物、踩過的坑(誠實,連丟臉的也寫) | `06_Product/*/LESSONS_LEARNED.md` |
| **② 找重複模式** | 哪個痛點**跨專案反覆出現**?一次是意外,三次是結構 | `00_Ideas_Inspiration/`(開放問題) |
| **③ 抽象命名** | 把具體 bug 抽象成一個**可命名的失效模式/機制** | test collusion(§7.1) |
| **④ 對外比對** | 查 prior-art:這是不是別人講過了?我的差異化在哪? | `05_DueDiligence/` |
| **⑤ 收斂主題** | 收斂成「可辯護的新穎性 + 一句話定位 + 研究問題」 | `01_Consolidation/` |

> 這五步本身,就是本卷宗 **Stage-Gate 流水線**的前半段(00→01→…)。換句話說:**研究流程 = 把自我盤點工程化。**

---

## 4. 致謝與協作說明（可選,作者自行增刪)

本研究採**多代理人協作**完成(Founder 定向與決策、Claude 操作化與查核、Codex 獨立審稿、Gemini 形式化與校準)——這套協作本身即 ALE「生產者 ≠ 審查者 + 機械事實裁決」原則的實踐。詳見根目錄 `README.md` 之「研究流程中的角色」。

---

*本檔由 Claude 代擬初稿,待作者 Morris 修訂定稿。公開資料以對外文件為準;`[請補充]` 處請作者填寫。*
