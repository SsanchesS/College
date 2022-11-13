from sql_base import BaseWorker
from sql_base import models

def new_product(product: models.product) -> int:
    new_id = BaseWorker.insert_data("INSERT INTO product(left_in_stock) "
                                     "VALUES(?) "
                                     "RETURNING id",
                                     (product.left_in_stock))
    return new_id
