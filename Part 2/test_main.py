import hypothesis.strategies as st
from hypothesis import given
import main

@given(st.lists(st.integers()))
def test_sort(xs):
    result = sorted(xs)
    assert all(xi <= xj for xi, xj in zip(result, result[1:]))
