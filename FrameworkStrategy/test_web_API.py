import json

import pytest
from playwright.sync_api import Page, Playwright, expect
from PageObject.login import LoginPage
from Utils.APIBase import APIUtils

##JSON file util access into the test
with open('FrameworkStrategy\Data\credentials.json') as f:
    testdata = json.load(f)
    user_CredentialsList=testdata["userCredentials"]

#Achive parameterization using different datasets driving data externally from json
@pytest.mark.parametrize('userCredential',user_CredentialsList)
def testUIWebAPI(playwright:Playwright, userCredential): #user_credentials is a fixture

    userName=userCredential["userName"]
    password = userCredential["password"]

    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    #Login User
    loginPage=LoginPage(page)    # creating Object

    loginPage.navigate()
    dashBoardPage=loginPage.loginPage(userName,password)

    #Orders History Page -> Order is present
    apiUtils=APIUtils()
    apiOrderId=apiUtils.createOrder(playwright,userCredential)

    dashBoardPage.navigateToOrders()
    orderDetails=dashBoardPage.selectOrder(apiOrderId)
    orderDetails.verifyOrderDetails(apiOrderId)



    context.close()
