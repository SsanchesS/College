from fastapi import APIRouter
from sql_base.models import product_typeM
import resolvers.product_type

product_type_router = APIRouter()

@product_type_router.get('/')
def get_product_types():
    return f'Response: {{text: Страница со списком Типов продуктов}}'

@product_type_router.get('/{product_type_id}')
def get_product_type(product_type_id: int):
    get_id = resolvers.product_type.get_product_type(product_type_id)
    return f'Product_type: {get_id}'

@product_type_router.post('/')
def new_product_type(product_type: product_typeM):
    new_id = resolvers.product_type.new_product_type(product_type)
    return f'{{code: 201, id: {new_id}}}'

@product_type_router.put('/{product_type_id}')
def update_product_type(product_type_id: int,product_type: product_typeM):
    upd_id = resolvers.product_type.upd_product_type(product_type_id,product_type)
    return f'Update product_type {upd_id}'

@product_type_router.delete('/{product_type_id}')
def delete_product_type(product_type_id: int):
    del_id = resolvers.product_type.del_product_type(product_type_id)
    return f'Delete product_type {del_id}'