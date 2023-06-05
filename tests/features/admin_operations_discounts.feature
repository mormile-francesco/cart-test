Feature: Test admin operations - edit discount list
  Background:
    Given Default discount list loaded
    Given Default product list loaded


  Scenario: Admin Journey - check discount list (happy path)
     Then The discount list is loaded successfully
     And The discount list size is 3


  Scenario: Admin Journey - add a list with error (specified an invalid rule)
    Given Custom discounts list discount_rules_schema_error.yaml is loaded
     Then The Admin gets error message "Invalid YAML file"


  Scenario: Admin Journey - add a missing list
    Given Custom discounts list discount_list_missing.yaml is loaded
    Then The Admin gets error message "The file does not exist!"


  Scenario: Admin Journey - add a custom discount list, check discount applies only on new cart
    Given Admin creates a cart
     When Admin adds 5 units of Coffee
     Then Unitary price for Coffee is 11.23
     Then The price for the product is 39.30
     When Custom discounts list discount_rules_update_coffee.yaml is loaded
     Then The product list is loaded successfully
     And The price for the product is 39.30

    Given Admin creates a cart
     When Admin adds 5 units of Coffee
     Then The price for the product is 0


  Scenario: Admin Journey - add a custom discount list with a duplicated rule (FreeRule) for product Coffee
    Given Custom discounts list discount_rules_duplicated_coffee.yaml is loaded
     When Admin creates a cart
     And Admin adds 5 units of Coffee
     Then The price for the product is 39.30

