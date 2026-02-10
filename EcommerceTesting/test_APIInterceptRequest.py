import time

from playwright.sync_api import Page, Playwright
from pytest_playwright.pytest_playwright import new_context

from Utils.APIBase import APIUtils

#API call made from the browser-> API call contact server return back response to browser-> Browser user response to generate a html

#mocking the request before sending to the browser by changing the order id

fakePlayLoadResponse={"data":[],"message":"No Orders"}

def intercept_request(route):  #route is storing the get-orders-for-customer request, response, Body,Headers
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6984d82cc941646b7ad7deae")

def  testAPIIntercept(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_request) #intercept_response is a method as an event
    page.locator("#userEmail").fill("autismita5@gmail.com")
    page.locator("#userPassword").fill("Smita@1234")
    page.locator("#login").click()

    page.get_by_role("button",name="ORDERS").click()

    page.get_by_role("button", name="View").nth(0).click()

    time.sleep(10)

