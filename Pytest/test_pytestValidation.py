import pytest


@pytest.fixture(scope="module")
def fixtureExample():
    print("fixtureExample")
    return "pass"

#For module scope yield will pause the execution until all the methods will executes and then execute code after the yield
#For function scope yield will pause the execution for every method will executes and then execute code after the yield
@pytest.fixture(scope="module")
def secondWork():
    print("secondWork")
    yield ###pause execute the function from which the fixture is called
    print("tear down validation")


@pytest.mark.skip
def test_initialCheck(fixtureExample):
    print("first test completed")

@pytest.mark.smoke
def test_secondCheck(fixtureExample,secondWork):
    print("second test completed")


def test_moduleFixture(fixtureExample,secondWork):
    if fixtureExample == "pass":
        assert fixtureExample=="pass"
        print("passed")

