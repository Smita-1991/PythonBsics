#pytest --html=report.html --tracing on
#pytest -n 3 --html=report.html --tracing on

import json

import pytest
from playwright.sync_api import Playwright

from page_Object.login import LoginPage
from Utils.APIBase import APIUtils

##JSON file util access into the test
with open('Data/credentials.json') as f:
    testdata = json.load(f)
    user_CredentialsList=testdata["userCredentials"]

#Achive parameterization using different datasets driving data externally from json
@pytest.mark.parametrize('userCredential',user_CredentialsList)
def testUIWebAPI(playwright:Playwright,browserInstance, userCredential): #user_credentials is a fixture



    userName=userCredential["userName"]
    password = userCredential["password"]

    #Login User
    loginPage=LoginPage(browserInstance)    # creating Object

    loginPage.navigate()
    dashBoardPage=loginPage.loginPage(userName,password)

    #Orders History Page -> Order is present
    apiUtils=APIUtils()
    apiOrderId=apiUtils.createOrder(playwright,userCredential)

    dashBoardPage.navigateToOrders()
    orderDetails=dashBoardPage.selectOrder(apiOrderId)
    orderDetails.verifyOrderDetails(apiOrderId)

