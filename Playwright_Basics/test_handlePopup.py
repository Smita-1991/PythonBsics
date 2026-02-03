import time

from playwright.sync_api import Page


def test_handlePopup(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice")

    page.on("dialog",lambda dialog:dialog.accept()) # this is an annonimus function which does not need name
    page.locator("#confirmbtn").click()
