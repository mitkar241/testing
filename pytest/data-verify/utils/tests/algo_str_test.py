#!/usr/bin/python3

import utils.algo_str
import pytest

@pytest.mark.parametrize("word, expected",
    [
        ('kayak', True),
        ('civic', True),
        ('forest', False)
    ]
)
def test_is_palindrome(word, expected):
    val = utils.algo_str.is_palindrome(word)
    assert val == expected
