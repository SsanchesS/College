from sql_base.base import base_worker
from sql_base.models import models

def new_product(product: models.product) -> int:
    new_id = base_worker.insert_data("INSERT INTO product(left_in_stock) "
                                     "VALUES(?) "
                                     "RETURNING id",
                                     (product.left_in_stock))
    return new_id
