from typing import Optional
from pydantic import BaseModel

class users(BaseModel):
    id: Optional[int]
    username: str
    password: str
    card: str

class online_magazine(BaseModel):
    id: Optional[int]
    title: str
    short_name: str

class product_type(BaseModel):
    product_type: str
    note: Optional[str]

class product(BaseModel):
    id: Optional[int]
    left_in_stock: int
    note: Optional[str]

class manager(BaseModel):
    id: Optional[int]
    user_id: int

class sale_product(BaseModel):
    transaction_code: Optional[int]
    online_magazine_id: int
    user_id: int
    product_id: int
    manager_id: int
    date_and_time_of_receipt: str
    title: Optional[str]