import pytest
actual_Result = "Testing"
#@pytest.mark.skipif(a>10, reason= "not working")
@pytest.mark.Regression
@pytest.mark.smoke
def test_tc_001_login_testcase():
    print("my first smoke test case")
    print("end of test case")
    assert actual_Result != "Testing", "This is failed"

@pytest.mark.sanity
def test_tc_003_logout_testcase():
    print("my third sanity test case")
    print("end of test case")