Feature: Order transaction
  Test related to order transaction

  Scenario Outline: Verify order success message shown in order details page
    Given place the item order with the <userName> and <password>
    And user is on landing page
    When I login to portal with <userName> and <password>
    And navigate to orders page
    And select the orderID
    Then order message is successfully displayed
    Examples:
      | userName             | password    |
      | rahulshetty@gmail.com| Iamking@000 |