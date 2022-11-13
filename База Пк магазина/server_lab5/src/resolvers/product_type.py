from sql_base.base import base_worker
from sql_base.models import models

def new_product_type(product_type: models.product_type) -> str:
    new_product_type = base_worker.insert_data("INSERT INTO product_type(product_type) "
                                     "VALUES(?) "
                                     "RETURNING product_type",
                                     (product_type.product_type))
    return new_product_type
