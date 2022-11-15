from fastapi import FastAPI
import uvicorn
from routers.users import users_router
from routers.online_magazine import online_magazine_router
from routers.product_type import product_type_router
from routers.product import product_router
from routers.manager import manager_router
from routers.sale_product import sale_product_router

from sql_base.base import base_worker

#https://metanit.com/python/fastapi/2.3.php

BASE_PATH = 'PcStore.db'
base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base('../sql/base.sql')
else:
    print("БД существует")
    

app = FastAPI()

app.include_router(users_router, prefix='/users')
app.include_router(online_magazine_router, prefix='/online_magazine')
app.include_router(product_type_router, prefix='/product_type')
app.include_router(product_router, prefix='/product')
app.include_router(manager_router, prefix='/manager')
app.include_router(sale_product_router, prefix='/sale_product')

if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, host="127.0.0.1", reload=True)
