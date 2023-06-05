from source.discount import Discounts
from source.product import Products


def apply_discount(units, price, discount):
    return round(discount.calculate(units, price), 2)


class Cart(object):
    def __init__(self, discounts, products):
        self.discounts = discounts.list
        self.available_products = products.list
        self.total = 0
        self.products_in_cart = []
        self.last_error = ""

    def add(self, name, units):
        try:
            units = int(units)
            if units == 0:
                self.last_error = f"Please, select at least 1 item"
            if not self.check_is_available(name):
                self.last_error = f"We don't have {name}, sorry"
            elif units>9999999:
                self.last_error = f"Insufficient availability for {name}"
            else:
                if len(self.products_in_cart) == 0 or name not in [p.name for p in self.products_in_cart]:
                    self.calculate_price(name, units)
                else:
                    for p in self.products_in_cart:
                        if name == p.name:
                            self.total = self.total - p.price
                            self.products_in_cart.remove(p)
                            self.calculate_price(name, units + p.units)
                            break

        except ValueError:
            self.last_error = "Input Error"

    def remove(self, name, units):
        try:
            units = int(units)
            if units == 0:
                self.last_error = f"Please, select at least 1 item"
            for p in self.products_in_cart:
                if name == p.name:
                    if units > p.units:
                        self.last_error = f"Not enough {name} in your cart!"
                    elif units == p.units:
                        self.total = self.total - p.price
                        self.products_in_cart.remove(p)
                    else:
                        self.total = self.total - p.price
                        self.products_in_cart.remove(p)
                        self.calculate_price(name, p.units - units)
                    break
                self.last_error = f"There's no {name} in your cart!"
        except ValueError:
            self.last_error = "Input Error"

    def check_discount(self, name, units):
        for p in self.available_products:
            for d in self.discounts:
                if name == p.name and p.product_code == d.product_code and units >= d.min_units:
                    return d
                else:
                    continue
        return None

    def get_price(self, name):
        for p in self.available_products:
            if name == p.name:
                return p.price

    def check_is_available(self, name):
        return name in [p.name for p in self.available_products]

    def calculate_price(self, name, units):
        discount = self.check_discount(name, units)
        print(f"Unitary price of {name}: {self.get_price(name)}")
        if discount is not None:
            discount_price = apply_discount(units, self.get_price(name), discount)
            print(f"Discount price of {name}: {discount_price}")
            self.total = self.total + discount_price
            self.products_in_cart.append(cart_entry(name, units, discount_price))
        else:
            self.total = self.total + (units * self.get_price(name))
            self.products_in_cart.append(cart_entry(name, units, (units * self.get_price(name))))


class cart_entry(object):
    def __init__(self, name, units, price):
        self.name = name
        self.units = units
        self.price = price