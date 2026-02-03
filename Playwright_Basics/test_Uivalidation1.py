import time

from playwright.async_api import Playwright, Page, expect


def test_UIValidation(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphoneproduct=page.locator("app-card").filter(has_text="iphone X")
    iphoneproduct.get_by_role("button").click()
    iphoneproduct = page.locator("app-card").filter(has_text="Nokia Edge")
    iphoneproduct.get_by_role("button").click()
    page.get_by_text("Checkout ").click()
    page.locator(".media-heading").get_by_text("iphone X").click()
    time.sleep(10)


def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPageInfo:
        page.locator(".blinkingText").click()
        childPage=newPageInfo.value
        text=childPage.get_by_text("Please email us at ").text_content()
        emailAddress="mentor@rahulshettyacademy.com"
        actualEmailAddress=text.split("at")
        print(actualEmailAddress[1])
        finalEmailAddress=actualEmailAddress[1].split(" ")[1]
        assert emailAddress == finalEmailAddress
