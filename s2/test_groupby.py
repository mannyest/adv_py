#!/usr/bin/env python

import pytest
import pandas as pd
from pandas.util.testing import assert_frame_equal
import ad_buys_agg as aba

LOT_STRUCT = [(1, 'Alpha Corp', 64), (2, "Mike's Ads", 44), (4, 'Jones Kraft', 19)]

DF_STRUCT = pd.DataFrame({ 'company_id': [1, 2, 4], 
                           'company_name': ['Alpha Corp', "Mike's Ads", 'Jones Kraft'], 
                           'volume': [64, 44, 19] },
                           index=[0, 1, 2])

def test_by_builtin():
    struct = aba.by_builtin()
    assert struct == LOT_STRUCT

def test_by_sql():
    struct = aba.by_sql()
    assert struct == LOT_STRUCT

def test_by_pandas():
    df = aba.by_pandas()
    df.index = range(0, len(df))
    assert_frame_equal(df, DF_STRUCT, check_dtype=False)


