import time
from operator import index

from playwright.sync_api import Page, expect

def test_handleTables(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    priceColValue = 0
    #check  the price of rice is equal to 37
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).text_content()=="Price":
            priceColValue=i
            print(f"Column value is: {priceColValue}")


    RiceRow=page.locator("tr").filter(has_text="Rice")
    assert RiceRow.locator("td").nth(priceColValue).text_content()=="37"





