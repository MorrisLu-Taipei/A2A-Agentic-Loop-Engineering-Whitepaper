# 以可執行證據治理 AI 軟體開發：Agentic 工程與 n8n 實作
### Governing Agentic Software Development with Executable Evidence — Agentic Engineering & Hands-on n8n

**一句話**：教學生用「多個 AI 互相把關 + 人類查證 + 過關才往下」的紀律,把一個真實題目做到**可發表、可稽核、不會自信地出錯**——並用 **n8n** 把整套流程變成跑得動的 workflow。

---

| | |
|---|---|
| **對象** | 資工/資管 大三~碩一、在職專班 |
| **先備** | Python 基礎、Git;**不需先會 n8n**(課內教);**無 API 金鑰也能上**(用 stub) |
| **形式** | 每週 講 1/3 + 動手 2/3;全程 Docker;每週交一個可跑的 n8n workflow |
| **時數** | 8 週短課(可擴 16 週);3 學分建議 |

### 為什麼這門課不一樣
市面教「怎麼叫 AI 寫程式」;本課教**「當驗證 AI 的也是 AI 時,如何不自我欺騙」**——以**可執行證據取代模型共識**(機械閘),用 n8n 把 stage-gate、對抗式審查、人類核可變成可稽核流程。教材源自講師**真實研究**(已抓出並修正 3 個會污染學術紀錄的錯誤)。

### 學習成果(修完能做到)
1. 設計帶 gate 的 Agentic 流程,辨識並防止「AI 驗 AI 的自我背書」。
2. 用 n8n 做出 State→Router→Gate、對抗審查迴圈、人類核可的可稽核流程。
3. 把真實題目用 stage-gate 推進到**預印本 DOI**(誠實標證據等級)。
4. 做先前技術查核、引文查證、GenAI 使用揭露(學術誠信)。

### 八週動線(每週一個可匯入 n8n workflow)
| 週 | 主題 | 動手 WF |
|---|---|---|
| 1 | 為何「AI 驗 AI」會崩:同源假通過 | WF-1 State |
| 2 | stage-gate:過關才往下 | WF-2 Gate |
| 3 | 生產者≠審查者:對抗式審查 | WF-3 Review-Loop |
| 4 | ★ 不盲信 AI:查原始來源(真打 arXiv) | WF-4 Verify |
| 5 | 機械閘:覆蓋率/突變 | WF-5 Mechanical-Gate |
| 6 | 人類關卡 + 安全/權限 | WF-6 Human-Approval |
| 7 | 先前技術/引文查證/誠信 | WF-7 PriorArt |
| 8 | 發表:預印本 DOI(誠實) | WF-8 Publish |
| 期末 | Capstone:串成完整 pipeline,跑自己題目到「預印本就緒」 | WF-9 Full-Pipeline |

### 評量
週實作 40% · 期中(對抗審查+查證)20% · 期末 capstone 30% · 學術誠信 10%。

### 教材(隨課提供)
可匯入 n8n workflow ×8(零金鑰可跑)、流程圖/拓樸向量圖、白皮書、實驗協定、踩坑教案、投影片大綱。

### 講師
**盧業興 Yeh-Hsing Lu (Morris)** — 虎智科技 Tiger AI Tech 共同創辦人｜**n8n 台北大使**｜PMP / n8n L1 / MCP｜ORCID 0009-0006-5373-0586｜已發表 Zenodo DOI(顧問方法論、AI-Native eBook 等)。

---
*聯絡:morrislu@tigerai.tw｜本課程教材編排「研究/論文生產」教學,不涉及任何商業機密。*
