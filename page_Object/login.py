from page_Object.dashboard import DashboardPage

class LoginPage:
    def __init__(self, page):
        self.page=page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")

    def login(self,userName,password):
        self.page.locator("#userEmail").fill(userName)
        self.page.locator("#userPassword").fill(password)
        self.page.locator("#login").click()
        dashBoardPage=DashboardPage(self.page)
        return dashBoardPage
