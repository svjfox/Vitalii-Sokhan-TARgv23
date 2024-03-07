from multiprocessing import connection
import select
from sqlite3 import *
from sqlite3 import Error

def create_connection(path:str):
    """ Создание подключения к базе данных SQLite
    """
    connection = None
    try:
        connection = connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}'")

    return connection

def execute_query(connection, query:str):
    """ Создание таблицы в базе данных SQLite
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Данные добавлены")
    except Error as e:
        print(f"Ошибка '{e}'")
        
def execute_read_query(connection, query:str):
    """ Чтение данных из таблицы
    """
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Ошибка '{e}'")
        
def execute_delete_query(connection, query:str):
    """ Удаление таблицы или данных из таблицы
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Таблица или данные из таблицы удалены")
        
    except Error as e:
        print(f"Ошибка '{e}'")
        
#-------------SQL запросы----------------
create_users_table="""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
student BOOLEAN 
 );    
"""
    

create_users= """
INSERT INTO
    users (name,age,gender,student)
VALUES
    ('Mati',45,'mees',false),
    ('Kati',23,'naine',true),
    ('Mati',45,'mees',true),
    ('Kati',23,'naine',true),
    ('Mati',45,'mees',false);
"""

select_users='SELECT * FROM users'

select_users='SELECT * FROM users'
delete_data_from_users='DELETE FROM users where student=true'
delete_tabel_users='DROP TABLE users'


#-------------SQL запуск----------------

conn=create_connection('C:/Users/svjfo/source/repos/svjfox/Vitalii-Sokhan-TARgv23/AppData/data.db')

execute_query(conn,create_users_table)
execute_query(conn,create_users)
users=execute_read_query(conn,select_users)
print('Студенты:')
for user in users:
    print(user)
    
execute_delete_query(conn,delete_data_from_users)
users=execute_read_query(conn,select_users)
print('Студенты удалены, остались=0:')
for user in users:
    print(user)
   
    
# удаление таблицы
execute_delete_query(conn,delete_tabel_users)




# # # # # # # # # # from os import *

# # !!!!!!!!!!!!!!!!!!!!   вариант создания базы данных в самой папке расположения файла !!!!!!!!!!!!!!!!!
# filename=path.abspath(__File__)
# dbdir=filaename.rstrip('Database_Python.py')
# dbpath=path.join(dbdir,'data.db')
# conn=create_connection(dbpath)