from playwright.sync_api import Page


def test_ResisterPage(page:Page):
    page.goto("https://rahulshettyacademy.com/client/auth/login")
    page.locator(".text-reset").click()
    page.get_by_placeholder("First Name").fill("Rahul")
    page.get_by_placeholder("Last Name").fill("Shetty")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your number").fill("9856961978")
    page.locator(".custom-select").select_option(value="Engineer")
    page.locator("input[value='Male']").check()
    page.locator("#userPassword").fill("rahul@1234")
    page.locator("#confirmPassword").fill("rahul@1234")
    page.locator("input[name='login']").click()


