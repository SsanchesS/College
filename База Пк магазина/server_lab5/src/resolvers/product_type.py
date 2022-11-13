from sql_base import BaseWorker
from sql_base import models

def new_product_type(product_type: models.product_type) -> str:
    new_product_type = BaseWorker.insert_data("INSERT INTO product_type(product_type) "
                                     "VALUES(?) "
                                     "RETURNING product_type",
                                     (product_type.product_type))
    return new_product_type
