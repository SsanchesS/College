from sql_base import BaseWorker
from sql_base import models

def new_online_magazine(online_magazine: models.online_magazine) -> int:
    new_id = BaseWorker.insert_data("INSERT INTO online_magazine(title, short_name) "
                                     "VALUES(?,?) "
                                     "RETURNING id",
                                     (online_magazine.title, online_magazine.short_name))
    return new_id