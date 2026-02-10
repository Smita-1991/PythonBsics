import time

from playwright.sync_api import Page


def test_ResisterPage(page:Page):
    page.goto("https://rahulshettyacademy.com/client/auth/login")
    page.locator("#userEmail").fill("autismita5@gmail.com")
    page.locator("#userPassword").fill("Smita@1234")
    page.locator("#login").click()
