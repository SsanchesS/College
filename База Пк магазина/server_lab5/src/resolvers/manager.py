from sql_base.base import base_worker
from sql_base.models import managerM

def get_manager(manager_id):
    get_manager1 = base_worker.insert_data(f"SELECT * FROM manager WHERE id = {manager_id}",())
    return get_manager1

def new_manager(manager: managerM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO manager (user_id) 
                                    VALUES(?) RETURNING id;""",
                                    (manager.user_id,))
    return new_id
# 
def upd_manager(manager_id,manager: managerM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE manager SET user_id=(?) WHERE id = {manager_id} RETURNING id;""",
                                     (manager.user_id,))
    return upd_id

def del_manager(manager_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM manager WHERE id = {manager_id} RETURNING id;",())
    return del_id