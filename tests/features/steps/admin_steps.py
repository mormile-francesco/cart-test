from behave import *

from source.cart import Cart
from source.discount import Discounts
from source.product import Products
from tests.features.steps.utils import attach_file


@step('Default product list loaded')
def step_impl(context):
    products = Products()
    products.load_product_list()
    context.products = products

@step('Admin creates a cart')
def step_impl(context):
    context.cart = Cart(context.discounts, context.products)

@then('The product list is loaded successfully')
def step_impl(context):
    assert context.products.error == ""

@step('The product list size is {list_size}')
def step_impl(context, list_size):
    assert len(context.products.list) == int(list_size)

@step('Default discount list loaded')
def step_impl(context):
    discounts = Discounts()
    discounts.load_discounts()
    context.discounts = discounts

@then('The discount list is loaded successfully')
def step_impl(context):
    assert context.discounts.error == ""

@step('The discount list size is {list_size}')
def step_impl(context, list_size):
    assert len(context.discounts.list) == int(list_size)

@step('Unitary price for {product} is {price}')
def step_impl(context, product, price):
    print(context.products.get_price(product))
    print(price)
    assert context.products.get_price(product) == float(price)

@step('Custom products list {filename} is loaded')
def step_impl(context, filename):
    products = Products()
    file = f"tests/features/steps/resources/product_lists/{filename}"
    products.load_product_list(file)
    context.list = products
    context.products = products
    attach_file(file)

@step('Custom discounts list {filename} is loaded')
def step_impl(context, filename):
    discounts = Discounts()
    file = f"tests/features/steps/resources/discount_lists/{filename}"
    discounts.load_discounts(file)
    context.discounts = discounts
    products = Products()
    context.products = products
    context.list = discounts
    attach_file(file)

@then('The Admin gets error message "{error_message}"')
def step_impl(context, error_message):
    assert error_message == context.list.error
