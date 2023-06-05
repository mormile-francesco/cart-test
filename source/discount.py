import yaml
from schema import SchemaError
from yaml.loader import SafeLoader

from resources.schemas.discount_rules import discount_schema


class Discounts(object):
    def __init__(self):
        self.list = []
        self.error = ""

    def load_discounts(self, discount_source='resources/discount_rules.yaml'):
        try:
            loaded_list = load_discounts(discount_source)["discounts"]
            self.list = []
            products_index = []
            for x in range(len(loaded_list)):
                if loaded_list[x]["product_code"] not in products_index:
                    if loaded_list[x]["type"] == "FreeRule":
                        self.list.append(FreeRuleDiscount(loaded_list[x]["type"], loaded_list[x]["product_code"]))
                    elif loaded_list[x]["type"] == "ReducedPriceRule":
                        self.list.append(ReducedPriceRule(loaded_list[x]["type"], loaded_list[x]["product_code"], loaded_list[x]["min_units"], loaded_list[x]["unit_price"]))
                    elif loaded_list[x]["type"] == "FractionPriceRule":
                        self.list.append(FractionPriceRule(loaded_list[x]["type"], loaded_list[x]["product_code"], loaded_list[x]["min_units"], loaded_list[x]["percentage_discount"]))
        except SchemaError:
            self.error = "Invalid YAML file"
        except FileNotFoundError:
            self.error = "The file does not exist!"
        except:
            self.error = "An error occurred when loading the product list, please check the file"
def load_discounts(discount_source):
    with open(discount_source) as f:
        data = yaml.load(f, Loader=SafeLoader)
        discount_schema.validate(data)
        return(data)


class FreeRuleDiscount(object):
    def __init__(self, type, product_code):
        self.type = type
        self.product_code = product_code
        self.min_units = 0

    def calculate(self, units, price=None):
        return 0


class ReducedPriceRule(FreeRuleDiscount):
    def __init__(self, type, product_code, min_units, unit_price):
        super().__init__(type, product_code)
        self.type = type
        self.product_code = product_code
        self.min_units = min_units
        self.unit_price = unit_price

    def calculate(self, units, price=None):
        print(f"Unitary discount price: {self.unit_price}")
        return units * self.unit_price


class FractionPriceRule(FreeRuleDiscount):
    def __init__(self, type, product_code, min_units, percentage_discount):
        super().__init__(type, product_code)
        self.type = type
        self.product_code = product_code
        self.min_units = min_units
        self.percentage_discount = percentage_discount

    def calculate(self, units, price):
        unitary_discount_price = round(price * (1-self.percentage_discount/100), 2)
        print(f"Unitary discount price: {unitary_discount_price}")
        return units * (unitary_discount_price)