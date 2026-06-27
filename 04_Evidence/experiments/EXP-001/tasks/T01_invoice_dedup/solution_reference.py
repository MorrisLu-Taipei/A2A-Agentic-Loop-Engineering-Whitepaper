# -*- coding: utf-8 -*-
"""T01 正確參考解（runner 以此為基底注入 D1/D2/D3 產生缺陷實作)。
注意:此檔僅供 runner 與 golden 對照;A/B/C 組的「實作」由 PG Agent 生成。"""


def aggregate_channel_counts(records, year_month):
    result = {}
    seen = set()
    for r in records:
        rid = r.get("id")
        if rid in seen:          # D1 去重(移除此段 = 注入 D1)
            continue
        seen.add(rid)
        if r.get("invoice_ym") != year_month:   # D2 月份過濾(改 != 為其他 = 注入 D2)
            continue
        cnt = r.get("count")
        if cnt is None or cnt < 0:               # D3 例外(改為 continue/0 = 注入 D3)
            raise ValueError(f"invalid count for id={rid}: {cnt}")
        result[r["channel"]] = result.get(r["channel"], 0) + cnt
    return result
