Feature: Test cart - check discount logic, considering behaviour at minimum unit limit edges

  Scenario Outline: User Journey - FreeRule discount
     Given User creates a cart
      When User adds <UNITS> units of <PRODUCT>
      Then The price for the product is <TOTAL>
      And The updated total is <TOTAL>

    Examples:
      | PRODUCT       | UNITS | TOTAL     |
      | Green Tea     | 1     | 0         |
      | Green Tea     | 10    | 0         |


  Scenario Outline: User Journey - ReducedPriceRule discount
     Given User creates a cart
      When User adds <UNITS> units of <PRODUCT>
      Then The price for the product is <TOTAL>
      And The updated total is <TOTAL>

    #Minimum units for ReducedPriceRule discount configured for Strawberries is 4, price set to 3
    Examples:
      | PRODUCT       | UNITS | TOTAL     |
      | Strawberries  | 1     | 5         |
      | Strawberries  | 3     | 15        |
      | Strawberries  | 4     | 12        |


  Scenario Outline: User Journey - FractionPriceRule discount
     Given User creates a cart
      When User adds <UNITS> units of <PRODUCT>
      Then The price for the product is <TOTAL>
      And The updated total is <TOTAL>

    #Minimum units for FractionPriceRule discount configured for Coffee is 5, 30% price reduction
    Examples:
      | PRODUCT | UNITS | TOTAL     |
      | Coffee  | 1     | 11.23     |
      | Coffee  | 4     | 44.92     |
      | Coffee  | 5     | 39.30     |