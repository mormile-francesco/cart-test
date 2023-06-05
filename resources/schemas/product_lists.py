from schema import Schema, Regex

product_code_regex = r"^[A-Z]{2}[0-9]{1,}$"

product_schema = Schema(
    {
        "products": [
            {"product_code": Regex(product_code_regex), "name": str, "price": float}
        ]
    }
    )