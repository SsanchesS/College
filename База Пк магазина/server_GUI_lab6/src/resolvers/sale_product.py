from sql_base.base import base_worker
from sql_base.models import sale_productM

def get_sale_product(transaction_code) -> int:
    get_sale_product1 = base_worker.insert_data(f"SELECT * FROM sale_product WHERE transaction_code = {transaction_code}",())
    return get_sale_product1

def new_sale_product(sale_product: sale_productM) -> int:
    new_transaction_code = base_worker.insert_data(f"""INSERT INTO sale_product (user_id, product_id, manager_id, date_and_time_of_receipt, title) 
                                    VALUES(?,?,?,?,?) RETURNING transaction_code;""",
                                    (sale_product.user_id, sale_product.product_id, sale_product.manager_id ,sale_product.date_and_time_of_receipt ,sale_product.title ))
    return new_transaction_code
# 
def upd_sale_product(transaction_code,sale_product: sale_productM) -> int:
    upd_transaction_code = base_worker.insert_data(f"""UPDATE sale_product SET online_magazine_id=(?), user_id=(?), product_id=(?), manager_id=(?), date_and_time_of_receipt=(?), title=(?) WHERE transaction_code = {transaction_code} RETURNING transaction_code;""",
                                     (sale_product.online_magazine_id, sale_product.user_id, sale_product.product_id, sale_product.manager_id ,sale_product.date_and_time_of_receipt ,sale_product.title ))
    return upd_transaction_code

def del_sale_product(transaction_code) -> int:
    del_transaction_code = base_worker.insert_data(f"DELETE FROM sale_product WHERE transaction_code = {transaction_code} RETURNING transaction_code;",())
    return del_transaction_code