import psycopg2
import uuid
class Database:
    def __init__(self):
        self.__db_connection=psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port=5432
        )
    def __del__(self):
        self.__db_connection.close()
    def select(self, query):
        try:
            cursor = self.__db_connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            return data
        except Exception:
            print('неизвестная ошибка')
    def insert(self, base, values):
        try:
            cursor = self.__db_connection.cursor()
            quercy=f'''insert into {base} values({values})'''
            cursor.execute(quercy)
            cursor.close()
            return 'данные добавлены'
        except Exception:
            print('неизвестная ошибка')




