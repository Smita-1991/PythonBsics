import json

import pytest
from playwright.sync_api import Page, Playwright, expect

from Utils.APIBase import APIUtils

##JSON file util access into the test
with open('Data/credentials.json') as f:
    testdata = json.load(f)
    user_CredentialsList=testdata["userCredentials"]

#Achive parameterization using different datasets driving data externally from json
@pytest.mark.parametrize('userCredential',user_CredentialsList)
def testUIWebAPI(playwright:Playwright, userCredential):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    userName = userCredential["userName"]
    password = userCredential["password"]
    #Login User
    page.goto("https://rahulshettyacademy.com/client/")
    page.locator("#userEmail").fill(userName)
    page.locator("#userPassword").fill(password)
    page.locator("#login").click()

    #Orders History Page -> Order is present
    apiUtils=APIUtils()

    apiOrderId=apiUtils.createOrder(playwright,userCredential)
    page.get_by_role("button",name="ORDERS").click()
    row=page.locator("tr").filter(has_text=apiOrderId)
    row.get_by_role("button",name="View").click()

    expect(page.locator(".email-preheader")).to_contain_text("Thank you for Shopping With Us")

    expect(page.locator(".col-text")).to_contain_text(apiOrderId)

    context.close()
