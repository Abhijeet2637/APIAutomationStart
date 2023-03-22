import pytest
@pytest.fixture(scope="module")
def fixture_code():
    print("This is the fixture code")
    print("---------------------------------------------------------")
    yield
    print("disconnect db code")
    print("---------------------------------------------------------")
#@pytest.mark.skipif(a>10, reason= "not working")
@pytest.mark.smoke
def test_tc_001_login_testcase(fixture_code):
    print("my first smoke test case")
    print("end of test case")
@pytest.mark.sanity
def test_tc_003_logout_testcase(fixture_code):
    print("my third sanity test case")
    print("end of test case")