# -*- coding: utf-8 -*-
"""T01 人工 golden tests（E 組基線)。
由人類依規格獨立撰寫,不看任何 AI 實作。能精準揪出 D1/D2/D3。
待測模組:solution.aggregate_channel_counts(records, year_month)
"""
import pytest
from solution import aggregate_channel_counts as agg

R = [
    {"id": "a", "invoice_ym": "202604", "channel": "food", "count": 100},
    {"id": "b", "invoice_ym": "202604", "channel": "food", "count": 50},
    {"id": "c", "invoice_ym": "202604", "channel": "retail", "count": 30},
    {"id": "d", "invoice_ym": "202603", "channel": "food", "count": 999},  # 鄰月
]

def test_basic_sum():
    assert agg(R, "202604") == {"food": 150, "retail": 30}

def test_dedup_D1():
    # 完全重複的列不得改變結果(INV-2)
    assert agg(R + R, "202604") == {"food": 150, "retail": 30}

def test_month_filter_D2():
    # 鄰月(202603)不可混入 202604
    assert "food" in agg(R, "202604") and agg(R, "202604")["food"] == 150

def test_empty_returns_empty():
    assert agg([], "202604") == {}
    assert agg(R, "209912") == {}

def test_negative_raises_D3():
    bad = R + [{"id": "x", "invoice_ym": "202604", "channel": "food", "count": -5}]
    with pytest.raises(ValueError):
        agg(bad, "202604")
