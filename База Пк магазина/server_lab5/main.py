from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse
import sqlite3

from Create_base.main import check_create_base

# https://metanit.com/python/fastapi/2.3.php

check_create_base()
db = sqlite3.connect('PcStore.db')
cur = db.cursor() 

app = FastAPI()
  
@app.get("/")
async def main():
    return {404:"404"}
    # return FileResponse("public/index.html")
  
@app.get("/api/users")
async def get_users():
    cur.execute(f'''
    SELECT id,username FROM user''')
    record = cur.fetchall()
    obj = {}
    for item in record:
        obj[item[0]] = item[1]
    return obj

@app.get("/api/users/{id}")
async def get_user(id):
    cur.execute(f'''
    SELECT id,username FROM user;''')
    record = cur.fetchall()
    for item in record:
        if f"{item[0]}" == id:
            return item
    return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})

# @app.post("/api/users")
# def create_person(data  = Body(), db: Session = Depends(get_db)):
#     person = Person(name=data["name"], age=data["age"])
#     db.add(person)
#     db.commit()
#     db.refresh(person)
#     return person
  
# @app.put("/api/users")
# def edit_person(data  = Body(), db: Session = Depends(get_db)):
   
#     # получаем пользователя по id
#     person = db.query(Person).filter(Person.id == data["id"]).first()
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if person == None: 
#         return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
#     # если пользователь найден, изменяем его данные и отправляем обратно клиенту
#     person.age = data["age"]
#     person.name = data["name"]
#     db.commit() # сохраняем изменения 
#     db.refresh(person)
#     return person
  
  
# @app.delete("/api/users/{id}")
# def delete_person(id, db: Session = Depends(get_db)):
#     # получаем пользователя по id
#     person = db.query(Person).filter(Person.id == id).first()
   
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if person == None:
#         return JSONResponse( status_code=404, content={ "message": "Пользователь не найден"})
   
#     # если пользователь найден, удаляем его
#     db.delete(person)  # удаляем объект
#     db.commit()     # сохраняем изменения
#     return person