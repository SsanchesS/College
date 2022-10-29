from sql import check_base, create_base
BASE_PATH = 'base.db'

if __name__ == '__main__':
    if not check_base(BASE_PATH):
        create_base(BASE_PATH, 'sql/base.sql')