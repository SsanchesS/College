from sql_base.base import base_worker
from sql_base.models import product_typeM

def get_product_type(product_type_id) -> str:
    get_product_type1 = base_worker.insert_data(f"SELECT * FROM product_type_table WHERE id = {product_type_id}",())
    return get_product_type1

def new_product_type(product_type1: product_typeM) -> str:
    new_product_type1 = base_worker.insert_data(f"""INSERT INTO product_type_table (product_type, note) 
                                    VALUES(?,?) RETURNING id;""",
                                    (product_type1.product_type, product_type1.note))
    return new_product_type1
# 
def upd_product_type(product_type_id,product_type1: product_typeM) -> str:
    upd_product_type1 = base_worker.insert_data(f"""UPDATE product_type_table SET product_type=(?), note=(?) WHERE id = {product_type_id} RETURNING id;""",
                                     (product_type1.product_type, product_type1.note))
    return upd_product_type1

def del_product_type(product_type_id) -> str:
    del_product_type1 = base_worker.insert_data(f"DELETE FROM product_type_table WHERE id = {product_type_id} RETURNING id;",())
    return del_product_type1