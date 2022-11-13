from sql_base.base import base_worker
from sql_base.models import models

def new_online_magazine(online_magazine: models.online_magazine) -> int:
    new_id = base_worker.insert_data("INSERT INTO online_magazine(title, short_name) "
                                     "VALUES(?,?) "
                                     "RETURNING id",
                                     (online_magazine.title, online_magazine.short_name))
    return new_id