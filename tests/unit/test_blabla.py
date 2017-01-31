from nose.tools import *
from skeleton.blabla import Blabla

def test_sum():
    obj = Blabla("bla", "blabla")
    assert_equal(10, obj.sum(5, 5))

def test_log():
    obj = Blabla("bla", "blabla")
    assert_equal(None, obj.log())
