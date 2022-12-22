from fastapi import APIRouter
from sql_base.models import managerM
import resolvers.manager

manager_router = APIRouter()

@manager_router.get('/')
def get_managers():
    return f'Response: {{text: Страница со списком Менеджеров, которые обслуживают покупателей по их id}}'

@manager_router.get('/{manager_id}')
def get_manager(manager_id: int):
    get_manager1 = resolvers.manager.get_manager(manager_id)
    return f'Manager: {get_manager1}'

@manager_router.post('/')
def new_manager(manager: managerM):
    new_id = resolvers.manager.new_manager(manager)
    return f'{{code: 201, id: {new_id}}}'

@manager_router.put('/{manager_id}')
def update_manager(manager_id:int,manager: managerM):
    upd_id = resolvers.manager.upd_manager(manager_id,manager)
    return f'Update manager {upd_id}'

@manager_router.delete('/{manager_id}')
def delete_manager(manager_id: int):
    del_id = resolvers.manager.del_manager(manager_id)
    return f'Delete manager {del_id}'