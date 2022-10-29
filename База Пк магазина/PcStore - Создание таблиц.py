import sqlite3
try:
    db = sqlite3.connect('PcStore.db')
    cur = db.cursor() 
    create_database()
    # start()
except:
    print('Error')
def start():
    if db:
        UpdateDtabase()
    else:
        UpdateDtabase()
def create_database():
    file = open('PC_magazine.sql')
    content = file.read()
    file.close()
    cur.executescript(content)
    db.commit()

def UpdateDtabase():
    user = input("Добавить user ? y/n ")
    Create_user(user)
    online_magazine = input("Добавить online_magazine ? y/n ")
    Create_online_magazine(online_magazine)
    product_type = input("Добавить product_type ? y/n ")
    Create_product_type(product_type)
    product = input("Добавить product ? y/n ")
    Create_product(product)
    # manager = input("Добавить manager  ? y/n ")
    # Create_manager(manager)
    sale_product = input("Добавить sale_product  ? y/n ")
    Create_sale_product(sale_product)
def Create_user(user):
    i=0
    while True:
        if user =="y":
            i=i+1
            username = input("Введите username")
            password = input("Введите password")
            card = input("Введите card")
            cur.executescript(f'''
                INSERT INTO user (username,password,card) VALUES ({username},{password},{card});
            ''')
            db.commit()
            Create_manager(i)
            user = input("Добавить user ? y/n ")
        else:
            break
def Create_online_magazine(online_magazine):
    while True:
        if online_magazine =="y":
            title = input("Введите title")
            short_name = input("Введите short_name")
            cur.executescript(f'''
                INSERT INTO online_magazine (title,short_name) VALUES ({title},{short_name});            ''')
            db.commit()
            online_magazine = input("Добавить online_magazine ? y/n ")
        else:
            break
def Create_product_type(product_type):
    while True:
        if product_type =="y":
            product_typeInp = input("Введите product_type")
            cur.executescript(f'''
                INSERT INTO product_type (product_type) VALUES ({product_typeInp});''')
            db.commit()
            product_type = input("Добавить product_type ? y/n ")
        else:
            break
def Create_product(product):
    while True:
        if product =="y":
            left_in_stock = input("Введите product")
            cur.executescript(f'''
                INSERT INTO product (left_in_stock) VALUES ({left_in_stock});            ''')
            db.commit()
            product = input("Добавить product ? y/n ")
        else:
            break
def Create_manager(user_id):
    cur.executescript(f'''
        INSERT INTO manager (user_id) VALUES ({user_id});''')
    db.commit()
def Create_sale_product(sale_product):
    while True:
        if sale_product =="y":
            online_magazine_id = input("Введите online_magazine_id")
            user_id = input("Введите user_id")
            product_id = input("Введите product_id")
            manager_id = input("Введите manager_id")
            date_and_time_of_receipt = input("Введите date_and_time_of_receipt в формате '19-11-2022'")
            cur.executescript(f'''
                INSERT INTO sale_product (online_magazine_id,user_id,product_id,manager_id,date_and_time_of_receipt) VALUES ({online_magazine_id},{user_id},{product_id},{manager_id},{date_and_time_of_receipt});            ''')
            db.commit()
            sale_product = input("Добавить Create_sale_product ? y/n ")
        else:
            break
        

start()