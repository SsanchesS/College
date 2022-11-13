from sql_base import BaseWorker
from sql_base import models

def new_sale_product(sale_product: models.sale_product) -> int:
    new_id = BaseWorker.insert_data("INSERT INTO sale_product(online_magazine_id,user_id,product_id,manager_id,date_and_time_of_receipt) "
                                     "VALUES(?,?,?,?,?) "
                                     "RETURNING id",
                                     (sale_product.online_magazine_id,sale_product.user_id,sale_product.product_id,sale_product.manager_id,sale_product.date_and_time_of_receipt,))
    return new_id