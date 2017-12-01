from main import nod
import pytest

@pytest.mark.parametrize("a, b, result", [(10,5,5), (5,10,5), (10,10,10), (0,0,0)])
def test_nod(a,b,result):
  assert(nod(a,b) == result)
