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

from ast import While
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
        print("Подключение к базе")
    except Error as e:
        print(f"Ошибка '{e}'")

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
CREATE TABLE IF NOT EXISTS brand(
id INTEGER PRIMARY KEY AUTOINCREMENT,
brand_id INTEGER,
brand_name TEXT NOT NULL
);
"""

create_users_table_category="""
CREATE TABLE IF NOT EXISTS category(
id INTEGER PRIMARY KEY AUTOINCREMENT,
category_id INTEGER,
category_name TEXT NOT NULL
);
"""

create_users_table_product="""
CREATE TABLE IF NOT EXISTS product(
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
    

# 4. Напишите несколько (минимум 3) запросов о товарах, включая информацию о категории и бренде.
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


# 5. Реализовать возможность добавления в базу новых товаров, категорий и брендов.
insert_brand = """
INSERT INTO
    brand (brand_id, brand_name)
    VALUES
    (4, 'brand4');
    """
    
insert_category = """
INSERT INTO
    category (category_id, category_name)
    VALUES
    (4, 'category4');
    """

insert_product = """
INSERT INTO
    product (product_id, product_name, price, category_id, brand_id)
    VALUES
    (16, 'product16', 1600, 4, 4);
    """
    
# 6. Сделать возможным изменение информации о товарах, категориях и брендах. Придумайте свои критерии.
update_brand = """
UPDATE
    brand
    SET
    brand_name = 'brand5'
    WHERE
    brand_id = 4;
    """
    
update_category = """
    UPDATE
    category
    SET
    category_name = 'category5'
    WHERE
    category_id = 4;
    """

update_product = """
    UPDATE
    product
    SET
    product_name = 'product5'
    WHERE
    product_id = 16;
    """
    
# 7. Применяйте запросы для удаления продуктов по определенным критериям (например, все продукты определенной категории или бренда).
delete_brand = """
    DELETE FROM
    brand
    WHERE
    brand_id = 4;
    """
    
delete_category = """
    DELETE FROM
    category
    WHERE
    category_id = 4;
    """
    
delete_product = """
    DELETE FROM
    product
    WHERE
    product_id = 16;
    """
    
# 8. Полностью удалите любую таблицу, а затем восстановите ее заново.
delete_brand_table = """
    DROP TABLE brand;
    """
    
delete_category_table = """
    DROP TABLE category;
    """

delete_product_table = """
    DROP TABLE product;
    """
    
# востановление таблиц





# показать таблицы!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
select_br='SELECT * FROM brand'
select_cat='SELECT * FROM category'
select_prod='SELECT * FROM product'
   
    


conn=create_connection('C:/Users/svjfo/source/repos/svjfox/Vitalii-Sokhan-TARgv23/AppData/290224Zadanie.db')

# execute_query(conn,create_users_table_brand)
# execute_query(conn,create_brand)
# brand=execute_read_query(conn,select_br)
# print('Бренды:')
# for br in brand:
#     print(br)
  


# execute_query(conn,create_users_table_category)
# execute_query(conn,create_category)
# category=execute_read_query(conn,select_cat)
# print('Категории:')
# for cat in category:
#     print(cat)


# execute_query(conn,create_users_table_product)
# execute_query(conn,create_product)
# products=execute_read_query(conn,select_prod)
# print('Продукты:')
# for prod in products:
#     print(prod)






# запрос на отображение продуктов, включая информацию о категории и бренде

brand=execute_read_query(conn,select_br)
print('Бренды:')
for br in brand:
    print(br)
category=execute_read_query(conn,select_cat)
print('Категории:')
for cat in category:
    print(cat)
products=execute_read_query(conn,select_prod)
print('Продукты:')
for prod in products:
    print(prod)

    
# создаем диалоговое окно работы с базой данных

for i in range(1,11):
    Vybor_deistvija=input("Выберите действие: 1-добавить, 2-удалить, 3-изменить, 4-выбрать, 5-закрыть: ")
    if Vybor_deistvija=="1":
        print("Вы выбрали добавление")
        Vybor_tablicy=input("Выберите таблицу: 1-бренды, 2-категории, 3-продукты: ")
        if Vybor_tablicy=="1":
            print("Вы выбрали добавление бренда")
            execute_query(conn,insert_brand)
            brand=execute_read_query(conn,select_br)
            print('Бренды:')
            for br in brand:
                print(br)
        elif Vybor_tablicy=="2":
            print("Вы выбрали добавление категории")
            execute_query(conn,insert_category)
            category=execute_read_query(conn,select_cat)
            print('Категории:')
            for cat in category:
                print(cat)
        elif Vybor_tablicy=="3":
            print("Вы выбрали добавление продукта")
            execute_query(conn,insert_product)
            products=execute_read_query(conn,select_prod)
            print('Продукты:')
            for prod in products:
                print(prod)
    elif Vybor_deistvija=="2":
        print("Вы выбрали удаление")
        Vybor_tablicy=input("Выберите таблицу: 1-бренды, 2-категории, 3-продукты: ")
        if Vybor_tablicy=="1":
            print("Вы выбрали удаление бренда")
            execute_query(conn,delete_brand)
            brand=execute_read_query(conn,select_br)
            print('Бренды:')
            for br in brand:
                print(br)
        elif Vybor_tablicy=="2":
            print("Вы выбрали удаление категории")
            execute_query(conn,delete_category)
            category=execute_read_query(conn,select_cat)
            print('Категории:')
            for cat in category:
                print(cat)
        elif Vybor_tablicy=="3":
            print("Вы выбрали удаление продукта")
            execute_query(conn,delete_product)
            products=execute_read_query(conn,select_prod)
            print('Продукты:')
            for prod in products:
                print(prod)
    elif Vybor_deistvija=="3":
        print("Вы выбрали изменение")
        Vybor_tablicy=input("Выберите таблицу: 1-бренды, 2-категории, 3-продукты: ")
        if Vybor_tablicy=="1":
            print("Вы выбрали изменение бренда")
            execute_query(conn,update_brand)
            brand=execute_read_query(conn,select_br)
            print('Бренды:')
            for br in brand:
                print(br)
        elif Vybor_tablicy=="2":
            print("Вы выбрали изменение категории")
            execute_query(conn,update_category)
            category=execute_read_query(conn,select_cat)
            print('Категории:')
            for cat in category:
                print(cat)
        elif Vybor_tablicy=="3":
            print("Вы выбрали изменение продукта")
            execute_query(conn,update_product)
            products=execute_read_query(conn,select_prod)
            print('Продукты:')
            for prod in products:
                print(prod)
    elif Vybor_deistvija=="4":
        print("Вы выбрали выбор")
        Vybor_tablicy=input("Выберите таблицу: 1-бренды, 2-категории, 3-продукты: ")
        if Vybor_tablicy=="1":
            print("Вы выбрали бренды")
            brand=execute_read_query(conn,select_br)
            print('Бренды:')
            for br in brand:
                print(br)
        elif Vybor_tablicy=="2":
            print("Вы выбрали категории")
            category=execute_read_query(conn,select_cat)
            print('Категории:')
            for cat in category:
                print(cat)
        elif Vybor_tablicy=="3":
            print("Вы выбрали продукты")
            products=execute_read_query(conn,select_prod)
            print('Продукты:')
            for prod in products:
                print(prod)
    elif Vybor_deistvija=="5":
        print("Вы выбрали закрыть")
        break
else:
    print("Неверный ввод")
    
    







