# -*- coding: utf-8 -*-
"""EXP-001 分析（SKELETON)。讀 metrics/raw_results.json,算各組 FPR、配對差值與效果量,出 report.md。"""
import json, pathlib, statistics

HERE = pathlib.Path(__file__).resolve().parent.parent

def cohens_d(a, b):
    if len(a) < 2 or len(b) < 2: return None
    na, nb = len(a), len(b)
    va, vb = statistics.pvariance(a), statistics.pvariance(b)
    sp = (((na-1)*va + (nb-1)*vb) / (na+nb-2)) ** 0.5 or 1e-9
    return (statistics.mean(a) - statistics.mean(b)) / sp

def main():
    raw = json.loads((HERE/"metrics"/"raw_results.json").read_text(encoding="utf-8"))
    # TODO: 待 raw 內含真實 false_pass(0/1) 後,依 condition 聚合
    by = {}
    for r in raw:
        by.setdefault(r["condition"], []).append(r.get("false_pass"))
    lines = ["# EXP-001 分析報告（待真實數據)\n",
             "| 組 | n | FPR | 說明 |", "|---|---|---|---|"]
    for c, vals in sorted(by.items()):
        clean = [v for v in vals if v in (0, 1)]
        fpr = round(sum(clean)/len(clean), 3) if clean else "—"
        lines.append(f"| {c} | {len(clean)} | {fpr} | {'(TODO 接端點後)' if not clean else ''} |")
    lines += ["", "## 假設判定（H1–H4)", "- H1/H2/H3/H4:待數據後依 README ④ 判定規則填。"]
    (HERE/"results"/"report.md").write_text("\n".join(lines), encoding="utf-8")
    print("[skeleton] wrote results/report.md")

if __name__ == "__main__":
    main()
