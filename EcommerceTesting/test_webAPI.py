from playwright.sync_api import Page, Playwright, expect

from Utils.APIBase import APIUtils


def testUIWebAPI(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    #Login User
    page.goto("https://rahulshettyacademy.com/client/")
    page.locator("#userEmail").fill("autismita5@gmail.com")
    page.locator("#userPassword").fill("Smita@1234")
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
