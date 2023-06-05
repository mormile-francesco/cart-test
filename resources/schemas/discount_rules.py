from schema import Schema, Regex, Optional

from resources.schemas.product_lists import product_code_regex

discount_types_regex = r"^(FreeRule|ReducedPriceRule|FractionPriceRule)$"

discount_schema = Schema(
    {
        "discounts": [
            {"type": Regex(discount_types_regex),
             "product_code": Regex(product_code_regex),
             Optional("min_units"): int,
             Optional("unit_price"): float,
             Optional("percentage_discount"): int,
             }
        ]
    }
    )