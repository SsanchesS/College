from sql_base import BaseWorker
from sql_base import models

def new_manager(manager: models.manager) -> int:
    new_id = BaseWorker.insert_data("INSERT INTO manager(user_id) "
                                     "VALUES(?) "
                                     "RETURNING id",
                                     (manager.user_id))
    return new_id