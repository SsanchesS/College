from fastapi import APIRouter
from sql_base.models import productM
import resolvers.product

product_router = APIRouter()

@product_router.get('/')
def get_products():
    return f'Response: {{text: Страница со списком Продуктов}}'

@product_router.get('/{product_id}')
def get_product(product_id: int):
    get_product1 = resolvers.product.get_product(product_id)
    return f'Product: {get_product1}'

@product_router.post('/')
def new_product(product: productM):
    new_id = resolvers.product.new_product(product)
    return f'{{code: 201, id: {new_id}}}'

@product_router.put('/{product_id}')
def update_product(product_id:int,product: productM):
    upd_id = resolvers.product.upd_product(product_id,product)
    return f'Update product {upd_id}'

@product_router.delete('/{product_id}')
def delete_product(product_id: int):
    del_id = resolvers.product.del_product(product_id)
    return f'Delete product {del_id}'