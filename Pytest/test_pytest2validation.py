import pytest


### execute the testcases which has group name smoke
@pytest.mark.smoke
def test_initialCheck(browserSetup):
    print("first test completed")
