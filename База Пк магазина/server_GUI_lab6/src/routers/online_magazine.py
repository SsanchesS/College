from fastapi import APIRouter
from sql_base.models import online_magazineM
import resolvers.online_magazine

online_magazine_router = APIRouter()

@online_magazine_router.get('/')
def get_online_magazines():
    return f'Response: {{text: Страница со списком доступных Магазинов}}'

@online_magazine_router.get('/{online_magazine_id}')
def get_online_magazine(online_magazine_id: int):
    get_online_magazine1 = resolvers.online_magazine.get_online_magazine(online_magazine_id)
    return f'Online_magazine: {get_online_magazine1}'

@online_magazine_router.post('/')
def new_online_magazine(online_magazine: online_magazineM):
    new_id = resolvers.online_magazine.new_online_magazine(online_magazine)
    return f'{{code: 201, id: {new_id}}}'

@online_magazine_router.put('/{online_magazine_id}')
def update_online_magazine(online_magazine_id:int,online_magazine: online_magazineM):
    upd_id = resolvers.online_magazine.upd_online_magazine(online_magazine_id,online_magazine)
    return f'Update online_magazine {upd_id}'

@online_magazine_router.delete('/{online_magazine_id}')
def delete_online_magazine(online_magazine_id: int):
    del_id = resolvers.online_magazine.del_online_magazine(online_magazine_id)
    return f'Delete online_magazine {del_id}'