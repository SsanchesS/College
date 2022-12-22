from typing import Optional
from pydantic import BaseModel

class usersM(BaseModel):
    # id: Optional[int]
    username: str
    password: str
    card: Optional[str]

class online_magazineM(BaseModel):
    # id: Optional[int]
    title: str
    short_name: str

class product_typeM(BaseModel):
    # id: Optional[int]
    product_type: str
    note: Optional[str]

class productM(BaseModel):
    # id: Optional[int]
    left_in_stock: int
    note: Optional[str]

class managerM(BaseModel):
    # id: Optional[int]
    user_id: int

class sale_productM(BaseModel):
    # transaction_code: Optional[int]
    online_magazine_id: int
    user_id: int
    product_id: int
    manager_id: int
    date_and_time_of_receipt: str
    title: Optional[str]