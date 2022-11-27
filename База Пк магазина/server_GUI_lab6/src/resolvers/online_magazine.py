from sql_base.base import base_worker
from sql_base.models import online_magazineM

def get_online_magazine(online_magazine_id) -> int:
    get_online_magazine1 = base_worker.insert_data(f"SELECT * FROM online_magazine WHERE id = {online_magazine_id}",())
    return get_online_magazine1

def new_online_magazine(online_magazine: online_magazineM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO online_magazine (title, short_name) 
                                    VALUES(?,?) RETURNING id;""",
                                    (online_magazine.title, online_magazine.short_name))
    return new_id
# 
def upd_online_magazine(online_magazine_id,online_magazine: online_magazineM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE online_magazine SET title=(?), short_name=(?) WHERE id = {online_magazine_id} RETURNING id;""",
                                     (online_magazine.title, online_magazine.short_name))
    return upd_id

def del_online_magazine(online_magazine_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM online_magazine WHERE id = {online_magazine_id} RETURNING id;",())
    return del_id