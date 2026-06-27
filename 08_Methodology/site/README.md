# 互動網頁介紹 — 部署與使用

「用 3×AI 協助寫期刊論文」方法論互動站(以 ALE 論文發表為案例)。**單一資料夾、零外部資源、全相對路徑** → 本機與 GitHub Pages 都能跑。

## 內容
- `index.html` — 互動站(雙語中/EN、可收合左選單、右下可拖曳說明視窗、4 張 SVG 圖)
- `index_v2.0.0_codex.html` — Codex 故事優先版(保留原站，先用四幕故事向非技術讀者解釋 ALE，再漸進揭露 Stage-Gate、A2A 與 n8n)
- `vendor/` — `shell.css`(公司標準版型)、`tigerai_logo.png`(官方 logo)
- `methodology_flow.svg` / `n8n_topology.svg` — 流程與拓樸向量圖
- `n8n_workflows/` — 8 個可匯入的教學 workflow(零金鑰可跑)

## 本機使用(git clone 後)
直接雙擊 `index.html`,或:
```bash
# 任一靜態伺服器(可選;直接開檔也行)
python -m http.server 8090   # 然後開 http://127.0.0.1:8090/
```

## GitHub Pages 部署
1. 把本 `site/` 內容放進 repo(可放 repo 根、`/docs`,或用 Pages 的 `gh-pages` 分支)。
2. Settings → Pages → 選來源分支/資料夾 → 存。
3. 開 `https://<user>.github.io/<repo>/`(或對應子路徑)即可。
> 全相對路徑,放在任何子目錄都不會壞;無 CDN、無外部字型 → 離線可開。

## 四圖 + 浮動說明(符合公司互動頁標準)
① 架構圖 ② 流程圖 ③ 使用情境故事流程圖 ④ 效益分析;右下「🛟 說明視窗」可拖曳/收合,點概念或階段卡顯示「🔧 執行重點 + 🎯 使用情境」。

## 雙語
預設中文;右上「EN」或網址加 `#en` 直接英文;切換不丟狀態。

*本檔屬本機/Pages 文件,非公開服務的一部分;產製:TigerAI 虎智科技。*
