from fastapi import APIRouter
from sql_base.models import users
import resolvers.user

users_router = APIRouter()

@users_router.get('/')
def get_users():
    return f'Response: {{text: Страница со списком Пользователей}}'

@users_router.get('/{user_id}')
def get_user(user_id: int):
    get_user1 = resolvers.user.get_users(user_id)
    return f'User: {get_user1}'

@users_router.post('/')
def new_user(user: users):
    new_id = resolvers.user.new_user(user)
    return f'{{code: 201, id: {new_id}}}'

@users_router.put('/{user_id}')
def update_user(user_id:int,user: users):
    upd_id = resolvers.user.upd_user(user_id,user)
    return f'Update user {upd_id}'

@users_router.delete('/{user_id}')
def delelte_user(user_id: int):
    del_id = resolvers.user.del_user(user_id)
    return f'Delete user {del_id}'