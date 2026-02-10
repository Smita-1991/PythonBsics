import time
from threading import Thread

from playwright.sync_api import Page

#API call made from the browser-> API call contact server return back response to browser-> Browser user response to generate a html

##mocking the response after getting the response from the server

fakePlayLoadResponse="{\"data\":[],\"message\":\"No Orders\"}"

def intercept_response(route):  #route is storing the get-orders-for-customer request, response, Body,Headers
    route.fulfill(
        json=fakePlayLoadResponse
    )

def testAPIIntercept(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")

    #intercept_response is a method as an event
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)
    page.locator("#userEmail").fill("autismita5@gmail.com")
    page.locator("#userPassword").fill("Smita@1234")
    page.locator("#login").click()

    page.get_by_role("button",name="ORDERS").click()

    ###Verify the response of the order page is "No Orders are present" even if the orders are available
    orderText=page.locator(".mt-4").text_content()
    print(orderText)

    time.sleep(10)
