import json

import pytest
from playwright.sync_api import Page, Playwright, expect

from Utils.APIBase import APIUtils

##JSON file util access into the test
with open('FrameworkStrategy\Data\credentials.json') as f:
    testdata = json.load(f)
    user_Credentials=testdata["userCredentials"]

#Achive parameterization using different datasets driving data externally from json
@pytest.mark.parametrize('userCredentials',user_Credentials)
def testUIWebAPI(playwright:Playwright, userCredentials): #user_credentials is a fixture
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    #Login User

    page.goto("https://rahulshettyacademy.com/client/")
    page.locator("#userEmail").fill(userCredentials["userName"])
    page.locator("#userPassword").fill(userCredentials["password"])
    page.locator("#login").click()

    #Orders History Page -> Order is present
    apiUtils=APIUtils()

    apiOrderId=apiUtils.createOrder(playwright)
    page.get_by_role("button",name="ORDERS").click()
    row=page.locator("tr").filter(has_text=apiOrderId)
    row.get_by_role("button",name="View").click()

    expect(page.locator(".email-preheader")).to_contain_text("Thank you for Shopping With Us")

    expect(page.locator(".col-text")).to_contain_text(apiOrderId)

    context.close()
