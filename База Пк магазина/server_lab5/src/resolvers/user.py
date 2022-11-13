from sql_base.base import BaseWorker
from sql_base import models

def get_user(user: models.users) -> int:
    get_user = BaseWorker.insert_data("SELECT * FROM users WHERE `id` = {user.id};")
    return get_user

def new_user(user: models.users) -> int:
    new_id = BaseWorker.insert_data("INSERT INTO user(username, password, card) "
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (user.username, user.password, user.card))
    return new_id
# 
def upd_user(user: models.users) -> int:
    upd_id = BaseWorker.insert_data(f"UPDATE user SET (username,password,card) WHERE id = {user.id}; "
                                     "VALUES(?,?,?) "
                                     "RETURNING id",
                                     (user.username, user.password, user.card))
    return upd_id

def del_user(user: models.users) -> int:
    del_id = BaseWorker.insert_data(f"DELETE FROM user WHERE id = {user.id} ")
    return del_id