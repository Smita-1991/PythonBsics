import json

import pytest
from playwright.sync_api import Playwright
from pytest_bdd import given, when, then, parsers, scenarios

from Utils.APIBase import APIUtils
from page_Object.login import LoginPage

scenarios('Features\orderTransaction.feature')

@pytest.fixture()
def share_data():
    return {}

@given(parsers.parse('place the item order with the {userName} and {password}'))
def place_item_order(playwright:Playwright,userName,password,share_data):
    # Orders History Page -> Order is present
    userCredential={}
    userCredential['userName']=userName
    userCredential['password']=password
    apiUtils = APIUtils()
    apiOrderId = apiUtils.createOrder(playwright, userCredential)
    share_data['order_id']=apiOrderId

@given('user is on landing page')
def user_landing_page(browserInstance,share_data):
    loginPage = LoginPage(browserInstance)  # creating Object
    loginPage.navigate()
    share_data['login_page']=loginPage

@when(parsers.parse('I login to portal with {userName} and {password}'))
def login(userName,password,share_data):
    login_page=share_data['login_page']
    dashBoardPage=login_page.login(userName,password)
    share_data['dashboard_page']=dashBoardPage

@when('navigate to orders page')
def navigate_to_orders_page(browserInstance,share_data):
    dashBoardPage=share_data['dashboard_page']
    dashBoardPage.navigateToOrders()

@when('select the orderID')
def select_orderID(browserInstance,share_data):
    dashBoardPage=share_data['dashboard_page']
    orderDetails = dashBoardPage.selectOrder(share_data['order_id'])
    share_data['order_details']=orderDetails

@then('order message is successfully displayed')
def verify_order_message(browserInstance,share_data):
    orderDetailsPage=share_data['order_details']
    apiOrderId=share_data['order_id']
    orderDetailsPage.verifyOrderDetails(apiOrderId)