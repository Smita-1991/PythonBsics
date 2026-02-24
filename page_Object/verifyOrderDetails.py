from playwright.sync_api import expect


class OrderDetails:
    def __init__(self, page):
        self.page=page

    def verifyOrderDetails(self,apiOrderId):
        expect(self.page.locator(".email-preheader")).to_contain_text("Thank you for Shopping With Us")
        expect(self.page.locator(".col-text")).to_contain_text(apiOrderId)