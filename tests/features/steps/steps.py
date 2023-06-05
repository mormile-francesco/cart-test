from behave import *

from source.cart import Cart
from source.discount import Discounts
from source.product import Products


@given('User creates a cart')
def step_impl(context):
    discounts = Discounts()
    products = Products()
    products.load_product_list()
    discounts.load_discounts()
    context.cart = Cart(discounts, products)

@step('{user} adds {units} units of {product}')
def step_impl(context, units, product, user):
    context.cart.add(product, units)
    context.last_added_product = product

@step('User removes {units} units of {product}')
def step_impl(context, units, product):
    context.cart.remove(product, units)

@step('The updated total is {updated_price}')
def step_impl(context, updated_price):
    assert context.cart.total == float(updated_price)

@step('The price for the product is {price}')
def step_impl(context, price):
    for p in context.cart.products_in_cart:
        if p.name == context.last_added_product:
            assert float(price) == p.price

@then('User gets error message "{error_message}"')
def step_impl(context, error_message):
    print(context.cart.last_error)
    assert error_message == context.cart.last_error
