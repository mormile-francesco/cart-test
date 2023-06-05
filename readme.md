# Cart automated acceptance tests
## Solution
This project is a _python_ (v3.10) automated test framework implementing a layer of acceptance tests for the cart application coded in _/source_. The tests focuses on cart functionality from the perspective of the User (cart editing, add/remove items etc..) and the Admin (e.g. product list uploading) using _gherking_ language (in _/tests/features_). I made some assumptions in order to elaborate all the test cases (e.g. a discount rules file can contain a rule twice, but the system only gets the first definition). I used allure for easier visualization of tests steps and assertions so that in test reports it is possible to check User/Admin journeys, expected results and attached product and discount custom list files. 
For easier and smoother execution portability I provided a docker-compose file that build and run the tests and start the [allure] service.

### Features 
- Admin operations on product list
- Admin operations on discount rules list
- Discount logic
- User operations on cart
- Cart management errors


### Execution
Run the tests with the following command:

```sh
docker-compose up
```

And then check [allure] results [locally](http://localhost:5050/allure-docker-service/projects/default/reports/latest/index.html).

   [allure]: <https://github.com/allure-framework>
