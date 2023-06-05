Feature: Test admin operations - edit products list
  Background:
    Given Default discount list loaded
    Given Default product list loaded


  Scenario: Admin Journey - check product list (happy path)
     Then The product list is loaded successfully
     And The product list size is 3


  Scenario: Admin Journey - add a list with error (price is string)
    Given Custom products list products_list_schema_error.yaml is loaded
     Then The Admin gets error message "Invalid YAML file"


  Scenario: Admin Journey - add a missing list
    Given Custom products list products_list_missing.yaml is loaded
    Then The Admin gets error message "The file does not exist!"


  Scenario: Admin Journey - add a custom product list
     Then Unitary price for Coffee is 11.23
     When Custom products list products_list_update_coffee.yaml is loaded
     Then The product list is loaded successfully
     Then Unitary price for Coffee is 16.50


  Scenario: Admin Journey - add a custom product list with a duplicated entry for Strawberries (price in first occurrence is 5, in second one is 8)
    Given Custom products list products_list_duplicated_strawberries.yaml is loaded
     When Admin creates a cart
     And Admin adds 2 units of Strawberries
     Then The price for the product is 10

