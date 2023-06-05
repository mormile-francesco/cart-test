Feature: Test cart - check discounts behaviour adding and removing items

  Scenario: User Journey - check discount is applied if user adds discount product in more than one step
     Given User creates a cart
      When User adds 1 units of Strawberries
      Then The price for the product is 5
      When User adds 2 units of Strawberries
      Then The price for the product is 15
      When User adds 4 units of Strawberries
      Then The price for the product is 21
      And The updated total is 21


  Scenario: User Journey - check discount is not applied when units in cart goes below the minimum unit rule
     Given User creates a cart
      When User adds 5 units of Strawberries
      Then The price for the product is 15
      When User removes 4 units of Strawberries
      Then The price for the product is 5
      And The updated total is 5


  Scenario: User Journey - check discount when adding more than one product type
      Given User creates a cart
      When User adds 3 units of Strawberries
      Then The price for the product is 15
      And The updated total is 15
      When User adds 3 units of Strawberries
      Then The price for the product is 18
      And The updated total is 18
      When User adds 1 units of Green Tea
      And The updated total is 18
      When User adds 5 units of Coffee
      Then The price for the product is 39.30
      And The updated total is 57.30
