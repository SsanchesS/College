from sql_base.base import base_worker
from sql_base.models import productM

def get_product(product_id) -> int:
    get_product1 = base_worker.insert_data(f"SELECT * FROM product WHERE id = {product_id}",())
    return get_product1

def new_product(product: productM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO product (left_in_stock, note) 
                                    VALUES(?,?) RETURNING id;""",
                                    (product.left_in_stock, product.note))
    return new_id
# 
def upd_product(product_id,product: productM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE product SET left_in_stock=(?), note=(?) WHERE id = {product_id} RETURNING id;""",
                                     (product.left_in_stock, product.note))
    return upd_id

def del_product(product_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM product WHERE id = {product_id} RETURNING id;",())
    return del_id