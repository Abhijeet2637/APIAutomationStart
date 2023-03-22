import pytest
a=11
#@pytest.mark.skipif(a>10, reason= "not working")
@pytest.mark.sanity
def test_tc_001_login_testcase():
    print("my first sanity test case")
    print("end of test case")
@pytest.mark.smoke
def test_tc_003_logout_testcase():
    print("my third smoke test case")
    print("end of test case")