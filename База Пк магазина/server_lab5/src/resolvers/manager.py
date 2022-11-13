from sql_base.base import base_worker
from sql_base.models import models

def new_manager(manager: models.manager) -> int:
    new_id = base_worker.insert_data("INSERT INTO manager(user_id) "
                                     "VALUES(?) "
                                     "RETURNING id",
                                     (manager.user_id))
    return new_id