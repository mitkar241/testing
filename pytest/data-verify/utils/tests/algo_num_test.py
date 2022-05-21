#!/usr/bin/python3

import utils.algo_num
import pytest

# pytest-3 -m basic algo_num_test.py
# pytest-3 -m comp algo_num_test.py

@pytest.mark.skip
def test_min():
    values = (2, 3, 1, 4, 6)
    val = utils.algo_num.min(values)
    assert val == 1

@pytest.mark.basic
@pytest.mark.parametrize("data, expected",
    [
        ((2, 3, 1, 4, 6), 6),
        ((5, -2, 0, 9, 12), 12),
        ((200, 100, 0, 300, 400), 400)
    ]
)
def test_max(data, expected):
    val = utils.algo_num.max(data)
    assert val == expected

@pytest.mark.basic
def test_sum():
    values = (2, 3, 1, 4, 6)
    val = utils.algo_num.sum(values)
    assert val == 16

@pytest.mark.comp
def test_max_min_pair():
    values = (2, 3, 1, 4, 6)
    max_val = utils.algo_num.max(values)
    min_val = utils.algo_num.min(values)
    assert [max_val, min_val] == [6, 1]

@pytest.fixture
def data():
    return [3, 2, 1, 5, -3, 2, 0, -2, 11, 9]

def test_selection_sort(data):
    sorted_vals = utils.algo_num.selection_sort(data)
    assert sorted_vals == sorted(data)
