# ALE 實證案例研究：電子發票開放資料儀表板
## A Field Case Study of System Development Agentic Loop Engineering (ALE)
### Empirical evidence for the Test-Collusion thesis and the Mechanical-Gate architecture

---

**作者 / Author**：Morris（虎智科技 TigerAI）
**文件類型 / Type**：Case Study（白皮書 §10 Evaluation / §12.2 Limitations 之實證附錄來源）
**版本 / Version**：v1
**日期 / Date**：2026-06-21
**對應理論**：`ALE_WhitePaper_v2.3.md`
**被研究系統**：`06_Product/04_EInvoiceDashboard`（Production + Demo 兩部署）

> 本案例的價值在於:ALE v2.3 §12.2 誠實承認「缺乏實證」。本文以一個**已交付、有完整證據軌跡**的真實專案,為 ALE 兩個最核心、也最易被質疑的主張提供**第一手田野證據**:(1) test collusion 真實存在(RQ1);(2) 機械閘能攔截 same-source 比對攔不到的逃逸缺陷(RQ2)。本文同時誠實界定本案例**不能**證明什麼。

---

## 0. 摘要（為什麼這個案子是 ALE 的「實證」）

電子發票儀表板專案在 ALE 框架尚未成文前即已開發,因此它不是「照著理論做出來的示範」,而是**理論的反向驗證**:一個獨立發生的真實專案,事後檢視竟與 ALE 的預測高度吻合——尤其是它**親身踩到了 test collusion 這個坑,並用機械閘爬出來**。這種「先有現象、後有理論、再回頭印證」的順序,比「照理論搭一個 demo」更有說服力。

三個最強的對應:

1. **Lesson #3 是一次有文字紀錄的 test collusion 事件**——同源自我比對「一起錯還互相背書」,完全對應 §7.2 的相關估計器聯合失效。
2. **`vv_crosscheck.py` 是機械閘的可執行實作**——其第 3 檢查是一條 spec invariant(§7.7),且**實際攔下** 4.5x 金額膨脹缺陷。
3. **四件套交付 + 證據軌跡**——DEVLOG / LESSONS / SDD / 互動架構圖 + n8n VERIFICATION_REPORT(3/3 PASS),對應 §3.3 Artifact Layer 與 §4.3「No evidence, no release」。

---

## 1. ALE 構念 ↔ 本案例證據對照表

| ALE 構念（v2.3 章節） | 本案例的對應實證 | 證據檔案 |
|---|---|---|
| **Test Collusion（§7.1）** | Lesson #3:儀表板值 vs DB 值同源比對,兩邊都 PASS 卻同步錯誤、互相背書 | `LESSONS_LEARNED.md` #3 |
| **Correlated estimators 聯合失效 / Cov→1（§7.2）** | 「同源資料做自我比對沒有外部基準,錯誤會在兩端同步存在,比對永遠相等」 | `LESSONS_LEARNED.md` #3 根因 |
| **機械閘:不問模型意見的事實基準（§7.3）** | `vv_crosscheck.py`:三道機械檢查,失敗 `exit 1` 中止 build | `vv_crosscheck.py`、`build/run_build.sh` |
| **需求不變量 / 蛻變關係（§7.7）** | 檢查#3「某月消費發票張數 ≤ 全國開立總張數」=系統級紅線,與實作無關 | `vv_crosscheck.py` L42–58 |
| **跨來源獨立基準（§7.3）** | 檢查#2「兩份獨立抓取(_12m vs _24m)同月唯一鍵集合一致」 | `vv_crosscheck.py` L31–40 |
| **真正獨立的交叉驗證（§7.2(c)）** | 部署後 Demo **SQLite** vs Production **postgres** 逐筆一致(不同引擎=低相關估計器) | `DEVLOG.md` 2026-06-21、CDN `VERIFICATION_REPORT.md` |
| **逃逸缺陷被機械閘攔截（RQ2）** | offset 分頁無序回傳重複列 → 直接 SUM 金額膨脹 4.5x;同源比對沒抓到,上界檢查抓到 | `LESSONS_LEARNED.md` #2、#3 |
| **Artifact Layer / 證據軌跡（§3.3, §4.3）** | 四件套 + 驗證報告 + 逐階段 DEVLOG | `DEVLOG.md`/`SDD.md`/`LESSONS_LEARNED.md`/`artifacts/system-architecture-v01.html` |
| **Security Gate / DevSecOps 左移（§8）** | NLQ `safe()`(單句 SELECT 白名單 + DENY DML/DDL + timeout + 唯讀帳號)、密碼輪替實測失效、CSP/XFO 標頭、非 root 唯讀根容器 | `nlq/app.py`、`DEVLOG.md` 安全補強段 |
| **Prompt Injection / 攻擊面收斂（§8.7）** | Demo 改瀏覽器內 sql.js「零後端、零憑證」,攻擊面從「一個服務」縮成「一個靜態檔」 | `LESSONS_LEARNED.md` #6 |
| **狀態/證據分離、冪等(§9.3)** | `einvoice_ods.sql` 以 `DROP IF EXISTS`+`BEGIN/COMMIT` 達冪等可重跑 | `load_to_postgres.py`、`einvoice_ods.sql` |
| **全 Docker、可帶走（§9.4）** | builder 容器 + 多階段 Dockerfile;fetch 容器繞 WAF;一次性 psql 容器載入 | `build/Dockerfile`、CDN 多階段 Dockerfile |
| **誠實標限制 / 人類審證據（§7.5, §12.2）** | n8n 通知節點誠實標 stub「不謊報已寄送」;排程已註冊但未到觸發時點照實寫 | `LESSONS_LEARNED.md` #8、`n8n/VERIFICATION_REPORT.md` |
| **元迴圈 / 自我修正（§9.5, §7.6）** | Codex review → 逐項收斂(去重、DB 冪等、NLQ 安全、編碼、密碼)再重驗 | `DEVLOG.md` 2026-06-20~21 |

---

## 2. 核心實證一：一次真實的 Test Collusion（對應 RQ1）

### 2.1 現象（field observation）
專案早期要驗「資料對不對」,做法是拿**儀表板顯示值**對**資料庫查詢值**。兩邊都 PASS。

### 2.2 為何這是 test collusion 而非單純 bug
兩個被拿來互相驗證的「估計器」(儀表板聚合、DB 查詢)**吃的是同一份已膨脹的資料**。在 §7.2 的語言裡:

$$\operatorname{Corr}\!\big(\text{err}(\text{dashboard}),\ \text{err}(\text{DB query})\ \big|\ \text{同一份資料}\big)\to 1.$$

兩者錯誤完全同向、同步,所以「兩個數字相等」恆成立——**比對永遠 PASS,卻什麼都沒驗到**。這正是「驗證者與被驗證者共享同一偏誤源」的均衡:綠燈滿滿、缺陷直送。專案 LESSONS_LEARNED #3 的原話「**一起錯還互相背書**」,是對 correlated-estimator 聯合失效最精準的田野註腳。

### 2.3 對應理論預測
§7.2 命題預測:**多一個同源的判斷者(哪怕是不同工具/不同模型)無法定生死**,因為偏誤是共享的。本案例獨立證實了這一點——問題不在「比對的工具不夠多」,而在「沒有一條獨立於被驗對象的基準線」。

---

## 3. 核心實證二：機械閘攔截逃逸缺陷（對應 RQ2）

### 3.1 缺陷本體
消費通路資料以 offset 分頁,但後端**未穩定排序**,相鄰頁回傳**完全重複的列**;直接 `SUM(invoice_create_amt)` 把同一筆加好幾次,金額膨脹約 **4.5 倍**。肉眼看「資料都對」,總額卻爆掉——典型逃逸缺陷。

### 3.2 機械閘如何抓到(same-source 抓不到)
`vv_crosscheck.py` 第 3 檢查是一條**與實作無關的系統級不變量**:

> 某月「消費發票張數」必須 ≤ 該月「全國開立發票總張數」。

膨脹時消費張數會 **>> 全國總量**(比值 > 1),違反物理上界,檢查必 `FAIL`、`exit 1` 中止 build。這條檢查的關鍵性在於:它的基準(全國開立總量,來自**另一個獨立資料集** `InvoiceStatic`)**獨立於被驗對象**(消費通路資料),所以不會跟著一起錯。這就是 §7.7「需求不變量作為 Garbage-In 防禦」的可執行版本。

### 3.3 三道機械檢查的角色
| 檢查 | 性質 | 對應理論 |
|---|---|---|
| #1 消費資料無重複業務鍵 | 完整性硬檢查 | 機械閘基本面(§7.3) |
| #2 兩獨立抓取同月唯一鍵集合一致 | 跨來源穩定性 | 獨立基準線(§7.3) |
| #3 消費張數 ≤ 全國開立總量 | 系統級不變量/上界 | spec invariant(§7.7) |

加上部署後 **Demo SQLite vs Production postgres 跨引擎逐筆比對**——這是一個**真正較獨立的估計器**(不同儲存引擎、不同查詢路徑),與 §7.2 區分「同源(高相關,不可定生死)」與「異源(較獨立,可作交叉)」完全吻合。

---

## 4. 本案例支持的 ALE 主張(可寫進白皮書 §10/§12.2)

1. **RQ1 得到存在性證據**:test collusion 不是理論臆測,而是**在真實專案中被觀測、被記錄**的失效模式。
2. **RQ2 得到方向性證據**:當 same-source 比對(對應 model panel 的同源版本)PASS 時,**獨立基準的機械閘 FAIL 並攔下缺陷**——機械閘抓到了同源比對抓不到的逃逸缺陷。
3. **§7.7 需求不變量可落地**:一條「物理上界」不變量即攔下整類膨脹缺陷,證明不變量防禦的成本效益。
4. **§8 / §8.7 安全左移可落地**:NLQ 唯讀白名單、密碼輪替、Demo 零後端,都是 SD 階段安全左移的真實實作。
5. **§4.3 證據軌跡可落地**:四件套 + VERIFICATION_REPORT 構成可稽核 evidence trail。

---

## 5. 誠實界定：本案例**不能**證明什麼（Threats to Validity）

依 §12.2 的自省精神,明確標出本案例的證據邊界:

1. **N=1,非受控實驗**:這是單一專案的事後對照(post-hoc),不是 §10 Evaluation Plan 要求的 A/B 或消融研究。它**例示(illustrates)**主張,不**統計證明(proves)**發生率。
2. **test collusion 的「AI 對 AI」版本尚未直接量測**:本案例的同源比對是「儀表板 vs DB」(工具層),嚴格說是 collusion 的**一般化形式**;PG-Agent 寫碼、V&V-Agent 從實作生成測試的**純 AI 共謀**仍待專門實驗(RQ1 完整版)。
3. **RQ3(技能資產化降本)未被本案例驗證**:本專案尚未把經驗萃取為 Certified Skill 並在後續專案重用,故邊際成本遞減/U 形(§6)在此**無資料**。這是下一個專案才能提供的證據。
4. **機械閘成本未量測**:本案例的 V&V 是輕量交叉檢查,未跑突變測試,故 §9.6 的成本黑洞問題在此**未觸及**。
5. **部分自動化仍 stub**:n8n 通知為 stub、真實排程觸發未捕捉(誠實記於 DEVLOG)。

> 一句話:本案例把 ALE 從「聽起來合理」推進到「**至少在一個真實專案中,核心失效模式確實出現、且核心對策確實有效**」——這是把框架性貢獻接上地氣的第一塊磚,但不是終點。

---

## 6. 兩個問題的答覆

### #1 如何讓這個案子「補足理論基礎的驗證」
- 把 §2、§3 的兩條田野證據寫進白皮書 **§10 Evaluation Plan** 作為「初步證據(preliminary evidence)」小節,並在 **§12.2** 把「缺乏實證」調整為「已有單案例例示、待受控研究量化」。
- 把 `vv_crosscheck.py` 檢查#3 升格為白皮書 **§7.7 的範例程式碼**(目前 §7.7 只有概念,可補一段真實程式)。
- 在白皮書 §7.2 條件協方差段落,加一個**腳註**指向本案例 Lesson #3 作為真實觀測。

### #2 如何讓這個案子「變成理論佐證的案例」
- 本文件即為**白皮書附錄 C(Case Study)** 的來源稿。建議在白皮書末新增「附錄 C:電子發票案例」,以 §1 對照表 + §2/§3 兩條核心實證為主體。
- 在電子發票專案的 `artifacts/system-architecture-vNN.html` 增一張「**ALE 對應圖**」:把四件套、vv_crosscheck、跨引擎比對標註為 ALE 的哪一個構念(讓 demo 同時是產品展示與方法論佐證)。
- 後續**刻意**把本案的去重不變量、NLQ 安全閘萃取為 Skill,放進 Skill Repository——這樣下一個專案就能提供 **RQ3(技能重用降本)** 的證據,補上 §5 的缺口。

---

## 附:關鍵證據檔案索引

- `06_Product/04_EInvoiceDashboard/vv_crosscheck.py` — 機械閘(§7.3/§7.7)可執行實作
- `06_Product/04_EInvoiceDashboard/LESSONS_LEARNED.md` #2/#3 — 缺陷本體 + test collusion 事件
- `06_Product/04_EInvoiceDashboard/DEVLOG.md` — 逐階段證據軌跡、跨引擎比對、安全補強
- `06_Product/04_EInvoiceDashboard/n8n/VERIFICATION_REPORT.md` — 管線驗證 3/3 PASS
- `06_Product/04_EInvoiceDashboard/nlq/app.py` — Security Gate(§8)實作
- `06_Product/04_EInvoiceDashboard/build/Dockerfile` — 全 Docker 可帶走(§9.4)

---

*— End of Case Study v1 —*
