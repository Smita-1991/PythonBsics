import time

import playwright
from playwright.async_api import Playwright
from playwright.sync_api import Page, expect


##playwright is the fixture already defined in the package pytest-playwright
def test_openBrowser(playwright):
    browser=playwright.chromium.launch(headless=False)
    browser.new_context()   # Same like you are opening new in-cognito window
    page=browser.new_page()
    page.goto("https://www.google.com")

###Chromium headless mode,1 single context
def test_playwrightShortcut(page:Page):
    page.goto("https://www.google.com")
    print("Page title is:"+page.title())

#CSS Selector #id and .classname
def testCoreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    # expect(page.get_by_text("Incorrect username/password.")).to_be_visible()  #Incorrect Username/password.

def testCoreLocators2(page:Page):
    page.goto("https://rahulshettyacademy.com/client/auth/login")


def test_fireFoxBrowser(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)
    context=browser.new_context()
    page=browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(10)