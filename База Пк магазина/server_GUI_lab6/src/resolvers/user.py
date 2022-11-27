from sql_base.base import base_worker
from sql_base.models import usersM

def get_users(user_id) -> int:
    get_user = base_worker.insert_data(f"SELECT * FROM user WHERE id = {user_id}",())
    return get_user

def new_user(user: usersM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO user (username, password, card) 
                                    VALUES(?,?,?) RETURNING id;""",
                                    (user.username, user.password, user.card))
    return new_id
# 
def upd_user(user_id,user: usersM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE user SET username=(?), password=(?), card=(?) WHERE id = {user_id} RETURNING id;""",
                                     (user.username, user.password, user.card))
    return upd_id

def del_user(user_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM user WHERE id = {user_id} RETURNING id;",())
    return del_id