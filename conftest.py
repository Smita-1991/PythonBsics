import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def userCredentials(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption("--browser_name", default="chrome", action="store")
    parser.addoption("--url_name", default="https://rahulshettyacademy.com/client", action="store")

@pytest.fixture
def browserInstance(playwright:Playwright,request):
    browser=None
    browser_name=request.config.getoption("browser_name")
    url_name=request.config.getoption("url_name")
    if browser_name=="chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name=="firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    # page.goto(url_name)
    yield page
    context.close()
    browser.close()




