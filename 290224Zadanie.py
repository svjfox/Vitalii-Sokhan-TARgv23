# Напишите функции, позволяющие реализовать следующие задачи:

# 1. Создайте базу данных с тремя связанными таблицами: «Продукты», «Категории» и «Бренды».

# 2. Определить структуру таблиц:

#    - Таблица «Категории» содержит как минимум поля: «category_id», «category_name».

#    - Таблица «Бренды» содержит как минимум следующие поля: «brand_id», «brand_name».

#    - Таблица «Продукты» содержит как минимум поля: «product_id», «product_name», «price», «category_id» (внешний ключ), «brand_id» (внешний ключ).

# 3. Заполните таблицы данными о разных категориях товаров, брендах и товарах.

# 4. Напишите несколько (минимум 3) запросов о товарах, включая информацию о категории и бренде.

# 5. Реализовать возможность добавления в базу новых товаров, категорий и брендов.

# 6. Сделать возможным изменение информации о товарах, категориях и брендах. Придумайте свои критерии.

# 7. Применяйте запросы для удаления продуктов по определенным критериям (например, все продукты определенной категории или бренда).

# 8. Полностью удалите любую таблицу, а затем восстановите ее заново.



# 1. Создайте базу данных с тремя связанными таблицами: «Продукты», «Категории» и «Бренды».
from itertools import product
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
create_users_table_brand="""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
brand_id INTEGER,
brand_name TEXT NOT NULL,
);
"""

create_users_table_category="""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
category_id INTEGER,
category_name TEXT NOT NULL,
);
"""

create_users_table_product="""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_id INTEGER,
product_name TEXT NOT NULL,
price INTEGER,
category_id INTEGER,
brand_id INTEGER,
FOREIGN KEY(category_id) REFERENCES category(id),
FOREIGN KEY(brand_id) REFERENCES brand(id)
);
"""

create_brand = """
INSERT INTO
  brand (brand_id, brand_name)
  VALUES
  (1, 'brand1'),
  (2, 'brand2'),
  (3, 'brand3');
"""
  
create_category = """
INSERT INTO
  category (category_id, category_name)
  VALUES
    (1, 'category1'),
    (2, 'category2'),
    (3, 'category3');
"""

create_product = """
INSERT INTO
    product (product_id, product_name, price, category_id, brand_id)
    VALUES
        (1, 'product1', 100, 1, 1),
        (2, 'product2', 200, 2, 2),
        (3, 'product3', 300, 3, 3),
        (4, 'product4', 400, 1, 2),
        (5, 'product5', 500, 2, 3),
        (6, 'product6', 600, 3, 1),
        (7, 'product7', 700, 1, 3),
        (8, 'product8', 800, 2, 1),
        (9, 'product9', 900, 3, 2),
        (10, 'product10', 1000, 1, 1),
        (11, 'product11', 1100, 2, 2),
        (12, 'product12', 1200, 3, 3),
        (13, 'product13', 1300, 1, 2),
        (14, 'product14', 1400, 2, 3),
        (15, 'product15', 1500, 3, 1);
        
   
    """
    
select_product = """
    SELECT
    product_name,
        category_name,
        brand_name
        FROM
        product
        INNER JOIN category ON product.category_id = category
        INNER JOIN brand ON product.brand_id = brand;
        
        """
        
select_product_price = """
    SELECT
    product_name,
        price
        FROM
        product
        WHERE
        price > 800;
        
        """

select_product_brand = """
    SELECT
    product_name,
        brand_name
        FROM
        product
        INNER JOIN brand ON product.brand_id = brand
        WHERE
        brand_name = 'brand1';
        
        """
        
    
    
#3. Заполните таблицы данными о разных категориях товаров, брендах и товарах.





conn=create_connection("'C:/Users/svjfo/source/repos/svjfox/Vitalii-Sokhan-TARgv23/AppData/290224Zadanie.db'")
execute_query(conn,create_users_table_brand)
execute_query(conn,create_users_table_category)
execute_query(conn,create_users_table_product)
products=execute_read_query(conn,select_product)
brand=execute_read_query(conn,create_brand)
category=execute_read_query(conn,create_category)
print('Бренды:')
for brand in brand:
    print(brand)
print('Категории:')
for category in category:
    print(category)
print('Продукты:')
for product in products:
    print(product)
    







# 3. Заполните таблицы данными о разных категориях товаров, брендах и товарах.






