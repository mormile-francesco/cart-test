import yaml
from schema import SchemaError
from yaml.loader import SafeLoader

from resources.schemas.product_lists import product_schema


class Products(object):
    def __init__(self):
        self.list = []
        self.error = ""

    def load_product_list(self, products_list_source='resources/products_list.yaml'):
        try:
            list = load_products(products_list_source)["products"]
            products_list = []
            for x in range(len(list)):
                if list[x]["product_code"] not in products_list:
                    self.list.append(Item(list[x]["product_code"], list[x]["name"], float(list[x]["price"])))
        except SchemaError:
            self.error = "Invalid YAML file"
        except FileNotFoundError:
            self.error = "The file does not exist!"
        except:
            self.error = "An error occurred when loading the product list, please check the file"

    def get_price(self, name):
        for p in self.list:
            if name == p.name:
                return p.price


def load_products(products_list_source):
    with open(products_list_source) as f:
        data = yaml.load(f, Loader=SafeLoader)
        product_schema.validate(data)
        return data


class Item(object):
    def __init__(self, product_code, name, price):
        self.product_code = product_code
        self.name = name
        self.price = price
