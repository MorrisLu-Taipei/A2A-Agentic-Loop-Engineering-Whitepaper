# -*- coding: utf-8 -*-
"""EXP-001 runner（SKELETON)。
控制流為真;標 TODO(MODEL) 處需接通用 OpenAI 相容端點才能跑 A/B/C/D 的生成步驟。
E 組(golden)與機械部分(pytest/mutation)可直接跑。
全程在 Docker 容器內執行(見 ../docker-compose.yml)。
"""
import argparse, json, os, subprocess, sys, hashlib, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent  # EXP-001/

def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]

def call_model(model_env, system, user):
    """TODO(MODEL): 接 openai 相容端點。未設定端點則明確報錯,不偽造輸出。"""
    base = os.getenv("OPENAI_BASE_URL"); key = os.getenv("OPENAI_API_KEY")
    if not base or not key or "REPLACE_ME" in (key or ""):
        raise NotImplementedError(
            "未設定模型端點(.env)。A/B/C/D 的生成步驟需要 OPENAI_BASE_URL/API_KEY。"
            "E 組(golden)與機械閘可先獨立跑。")
    # from openai import OpenAI; client = OpenAI(base_url=base, api_key=key)
    # resp = client.chat.completions.create(model=os.getenv(model_env), temperature=..., messages=[...])
    # return resp.choices[0].message.content
    raise NotImplementedError("接上 openai client 後移除此行。")

def inject_defect(ref_code: str, defect_id: str) -> str:
    """TODO: 依 tasks/*/defects.md 將正確參考解轉成含缺陷實作 C_{t,d}。
    D1 移除去重、D2 改月份比較、D3 改例外為 continue。"""
    raise NotImplementedError("實作缺陷注入(對照 defects.md)。")

def run_pytest(workdir) -> bool:
    """回傳 True=全綠(可能 false-pass)。"""
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", workdir],
                       capture_output=True, text=True)
    return r.returncode == 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", default="tasks")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--conditions", default="A,C,D,E")
    args = ap.parse_args()
    conditions = args.conditions.split(",")
    tasks = sorted(p.name for p in (HERE/args.tasks).iterdir() if p.is_dir())

    results = []
    for t in tasks:
        for cond in conditions:
            for run in range(args.runs):
                # 1) PG 產實作(A/B/C/D)  TODO(MODEL)
                # 2) 注入缺陷 → C_{t,d}    inject_defect()
                # 3) V&V 產測試(context 依 cond,見 verifier_prompt.md)  TODO(MODEL)
                #    E 組:用 tasks/<t>/golden_tests/
                # 4) 對每個缺陷變體跑 pytest → 記錄是否 false-pass
                # 5) D 組:額外 mutmut run + hypothesis 性質測試
                # 6) 記 token/時間/hash
                results.append({
                    "task": t, "condition": cond, "run": run,
                    "status": "TODO(MODEL) — 接端點後填",
                })
    out = HERE/"metrics"/"raw_results.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[skeleton] wrote {out}（{len(results)} 列佔位)。接上模型端點後即產真實數據。")

if __name__ == "__main__":
    main()
