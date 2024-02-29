﻿from multiprocessing import connection
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
        cursor=connection.cursor()
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


#-------------SQL запуск----------------

conn=create_connection('C:/Users/svjfo/source/repos/svjfox/Vitalii-Sokhan-TARgv23/AppData/data.db')

execute_query(conn,create_users_table)
execute_query(conn,create_users)
users=execute_read_query(conn,select_users)
print('Студенты:')
for user in users:
    print(user)