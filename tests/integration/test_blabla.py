from nose.tools import *
from skeleton.blabla import Blabla

def test_sum2():
    obj = Blabla("bla", "blabla")
    assert_equal(10, obj.sum(5, 5))
