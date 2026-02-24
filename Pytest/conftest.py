#####By adding the fixture we can execute the code which is written in the fixture browserSetup before test_initialcheck()
#by sending the fixture name in the test_initialCheck()
import pytest
from playwright.sync_api import Playwright


##scope="function"  fixture will run before every test
##scope="module"   fixture will run before method at once
##scope="class" fixture will run before class
##scope="Session"  This will execute once per session
@pytest.fixture(scope="session")
def browserSetup():
    print("Browser is started")

@pytest.fixture(scope="session")
def browserInstance(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page

####first method will check the fixture is in file then it will search in the confest.py