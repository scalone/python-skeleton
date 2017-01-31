from nose.tools import *
from skeleton.config import settings

def test_env():
    assert_equal("testadjfoigajodsifjaoidfjgoadif", settings["token"])
