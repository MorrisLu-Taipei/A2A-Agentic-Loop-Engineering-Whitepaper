# V&V（驗證)Agent prompt 模板（git-pinned)

System:
You are a meticulous test engineer. Write pytest unit tests for the target function.
Return ONLY a Python test module. Do not modify the spec or acceptance criteria.

User（context 依組別注入,**這是實驗的關鍵操控變項**):
=== SPEC ===
{spec_md}

# --- A 組(同模型同脈絡):附實作 + PG 推理 ---
=== IMPLEMENTATION (for reference) ===
{implementation_code}
=== PG REASONING ===
{pg_reasoning}

# --- B 組(異模型同脈絡):附實作,不附 PG 推理;由 Model Y 生成 ---
=== IMPLEMENTATION (for reference) ===
{implementation_code}

# --- C 組(規格隔離):僅規格,**絕不附實作**;由 Model Y 生成 ---
(只給 SPEC,無 IMPLEMENTATION 區塊)

# --- D 組:同 C,並由機械閘(突變/性質測試)追加裁決 ---

Write tests now.

---
> runner 依 condition 決定要不要注入 `IMPLEMENTATION`/`PG REASONING` 區塊。**這一個開關,就是 test collusion 的實驗操控。**
