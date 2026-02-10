from playwright.sync_api import Playwright


class APIUtils:

    authorisationToken=""

    def getAuthorisationToken(self,playwright:Playwright):
        apiRequestContext=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        loginResponse=apiRequestContext.post("/api/ecom/auth/login",
                               data={"userEmail": "autismita5@gmail.com",
                                   "userPassword": "Smita@1234"}
                               )

        assert loginResponse.ok
        print(loginResponse.json())
        responseBody=loginResponse.json()
        return responseBody["token"]

    def createOrder(self,playwright:Playwright):

        token=self.getAuthorisationToken(playwright)
        apiRequestContext=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=apiRequestContext.post("/api/ecom/order/create-order",
                              data={"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]},
                              headers={"Authorization":token
                                       }
                              )
        print(response.json())
        orderID=response.json()
        print(orderID["orders"])
        return orderID["orders"][0]