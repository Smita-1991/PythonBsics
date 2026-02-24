import json

import pytest
from playwright.async_api import Playwright
from playwright.sync_api import expect

from Utils.APIBase import APIUtils

##JSON file util access into the test
with open('Data/credentials.json') as f:
    testdata = json.load(f)
    user_CredentialsList=testdata["userCredentials"]

#Achive parameterization using different datasets driving data externally from json
@pytest.mark.parametrize('userCredential',user_CredentialsList)
def test_injectSessionCookies(playwright:Playwright,userCredential):

    apiUtils=APIUtils()
    token=apiUtils.getAuthorisationToken(playwright,userCredential)
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    #script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button",name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()