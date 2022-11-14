import sqlite3
import os

class BaseWorker:

    def set_base_path(self, base_path: str):
        self.base_path = base_path

    def check_base(self) -> bool:
        print("Проверка наличия БД")
        return os.path.exists(self.base_path)

    def create_base(self, sql_file: str) -> None:
        print("БД не существует")
        print("Наполняем БД...")
        connection = sqlite3.connect(self.base_path)
        cur = connection.cursor()

        with open(sql_file, 'r') as file:
            scripts = file.read()
            try:
                cur.executescript(scripts)
                connection.commit()
            except sqlite3.Error as error:
                print(error)
            finally:
                connection.close()

    def insert_data(self, query: str, args: tuple[str]):
        print("Работа с БД...")
        # print("""  
        
        
        # """)
        # print(query)
        # print(args)
        # print("""  
        
        
        # """)
        connection = sqlite3.connect(self.base_path, isolation_level=None)
        cur = connection.cursor()
        res = cur.execute(query, args).fetchone()
        connection.commit()
        connection.close()
        return res
base_worker = BaseWorker()