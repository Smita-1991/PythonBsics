from page_Object.verifyOrderDetails import OrderDetails


class DashboardPage:
    def __init__(self,page):
        self.page=page

    def navigateToOrders(self):
        self.page.get_by_role("button", name="ORDERS").click()

    def selectOrder(self,apiOrderId):
        row = self.page.locator("tr").filter(has_text=apiOrderId)
        row.get_by_role("button", name="View").click()
        verifyOrderDetails=OrderDetails(self.page)
        return verifyOrderDetails
