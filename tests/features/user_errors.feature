Feature: Test cart - errors

  Scenario: User Journey - Unavailable product
     Given User creates a cart
      When User adds 3 units of Apples
      Then User gets error message "We don't have Apples, sorry"

  Scenario: User Journey - Units format error (add)
     Given User creates a cart
      When User adds three units of Strawberries
      Then User gets error message "Input Error"

  Scenario: User Journey - Units format error (remove)
     Given User creates a cart
      When User adds 4 units of Strawberries
      And User removes two units of Strawberries
      Then User gets error message "Input Error"

  Scenario: User Journey - Item add limit (max)
     Given User creates a cart
      When User adds 99999999 units of Strawberries
      Then User gets error message "Insufficient availability for Strawberries"

  Scenario: User Journey - Item add limit (min)
     Given User creates a cart
      When User adds 0 units of Strawberries
      Then User gets error message "Please, select at least 1 item"

  Scenario: User Journey - Item remove limit (min)
     Given User creates a cart
      When User adds 1 units of Strawberries
      When User removes 0 units of Strawberries
      Then User gets error message "Please, select at least 1 item"

  Scenario: User Journey - Item remove limit (max)
     Given User creates a cart
      When User adds 2 units of Strawberries
      And User removes 3 units of Strawberries
      Then User gets error message "Not enough Strawberries in your cart!"

  Scenario: User Journey - Remove an item that has not been previously added
     Given User creates a cart
      When User adds 2 units of Strawberries
      And User removes 3 units of Coffee
      Then User gets error message "There's no Coffee in your cart!"


