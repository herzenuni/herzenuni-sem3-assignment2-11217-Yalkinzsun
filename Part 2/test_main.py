import pytest
import hypothesis.strategies as st
from hypothesis import given
import main

class TestEncoding(unittest.TestCase):
  @given(st.lists(st.integers()))
  def test_bubble_sort(self, xs):
	result = sorted(xs)
    self.assertEqual(bubble_sort(xs), result) 
    
  @given(st.lists(st.integers()))
  def test_quicksort(self, xs):
	result = sorted(xs)
    self.assertEqual(quicksort(xs), result)   
                                         
