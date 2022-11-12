from Create_base.sql import check_base, create_base
BASE_PATH = 'PcStore.db'
def check_create_base():
    if not check_base(BASE_PATH):
        print("БД не существует")
        print("Наполняем БД...")
        create_base(BASE_PATH, "Create_base/sql/base.sql")
#         return True
    else:
        print("БД существует")
#         return False
    
if __name__ == '__main__':
    check_create_base()
