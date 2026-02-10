from PageObject.dashboard import Dashboard


class LoginPage:
    def __init__(self, page):
        self.page=page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")

    def loginPage(self,userName,password):
        self.page.locator("#userEmail").fill(userName)
        self.page.locator("#userPassword").fill(password)
        self.page.locator("#login").click()
        dashBoardPage=Dashboard(self.page)
        return dashBoardPage
