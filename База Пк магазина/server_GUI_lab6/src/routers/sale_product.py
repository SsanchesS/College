from fastapi import APIRouter
from sql_base.models import sale_productM
import resolvers.sale_product

sale_product_router = APIRouter()

@sale_product_router.get('/')
def get_sale_products():
    return f'Response: {{text: Страница со списком Продажи товара}}'

@sale_product_router.get('/{transaction_code}')
def get_sale_product(transaction_code: int):
    get_sale_product1 = resolvers.sale_product.get_sale_product(transaction_code)
    return f'Sale_product: {get_sale_product1}'

@sale_product_router.post('/')
def new_sale_product(sale_product: sale_productM):
    new_transaction_code = resolvers.sale_product.new_sale_product(sale_product)
    return f'{{code: 201, id: {new_transaction_code}}}'

@sale_product_router.put('/{transaction_code}')
def update_sale_product(transaction_code:int,sale_product: sale_productM):
    upd_transaction_code = resolvers.sale_product.upd_sale_product(transaction_code,sale_product)
    return f'Update sale_product {upd_transaction_code}'

@sale_product_router.delete('/{transaction_code}')
def delete_sale_product(transaction_code: int):
    del_transaction_code = resolvers.sale_product.del_sale_product(transaction_code)
    return f'Delete sale_product {del_transaction_code}'