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

import select
from sqlite3 import *
from sqlite3 import Error
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

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



def insert_brand(conn):
    brand_id = simpledialog.askstring("Введите id бренда:", "Введите id бренда:")
    brand_name = simpledialog.askstring("Введите название бренда:", "Введите название бренда:")
    insert_b = """
    INSERT INTO
        brand (brand_id, brand_name)
    VALUES
        (?, ?);
    """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_b, (brand_id, brand_name))
        conn.commit()  
        print("Бренд успешно добавлен")
    except sqlite3.Error as e:  
        print(f"Ошибка при добавлении бренда: {e}")


def insert_category(conn):
    category_id = simpledialog.askstring("Введите id категории: ", "Введите id категории: ")
    category_name = simpledialog.askstring("Введите название категории: ", "Введите название категории: ")
    insert_c = """
    INSERT INTO
        category (category_id, category_name)
    VALUES
        (?, ?);
    """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_c, (category_id, category_name))
        conn.commit()  
        print("Категория успешно добавлена")
    except sqlite3.Error as e:  
        print(f"Ошибка при добавлении категории: {e}")    


def insert_product(conn):
    product_id = simpledialog.askstring("Введите id продукта: ", "Введите id продукта: ")
    product_name = simpledialog.askstring("Введите название продукта: ", "Введите название продукта: ")
    price = simpledialog.askstring("Введите цену продукта: ", "Введите цену продукта: ")
    category_id = simpledialog.askstring("Введите id категории продукта: ", "Введите id категории продукта: ")
    brand_id = simpledialog.askstring("Введите id бренда продукта: ", "Введите id бренда продукта: ")
    insert_p = """
    INSERT INTO
        product (product_id, product_name, price, category_id, brand_id)
    VALUES
        (?, ?, ?, ?, ?);
    """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_p, (product_id, product_name, price, category_id, brand_id))
        conn.commit()  
        print("Продукт успешно добавлен")
    except sqlite3.Error as e: 
        print(f"Ошибка при добавлении продукта: {e}")


    
# 6. Сделать возможным изменение информации о товарах, категориях и брендах. Придумайте свои критерии.

def update_brand(conn):
    brand_name = simpledialog.askstring("Введите новое название бренда: ", "Введите новое название бренда: ")
    brand_id = simpledialog.askstring("Введите id бренда: ", "Введите новое название бренда: ")
    update_b = """
    UPDATE
        brand
    SET
        brand_name = ?
    WHERE
        brand_id = ?;
    """
    cursor = conn.cursor()
    try:
        cursor.execute(update_b, (brand_name, brand_id))
        conn.commit()  
        print("Название бренда успешно обновлено")
    except sqlite3.Error as e:  
        print(f"Ошибка при обновлении бренда: {e}")


def update_category(conn):
    category_name = simpledialog.askstring("Введите новое название категории: ", "Введите новое название категории: ")
    category_id = simpledialog.askstring("Введите id категории: ", "Введите новое название категории: ")
    update_c = """
    UPDATE
        category
    SET
        category_name = ?
    WHERE
        category_id = ?;
    """
    cursor = conn.cursor()
    try:
        cursor.execute(update_c, (category_name, category_id))
        conn.commit()  
        print("Название категории успешно обновлено")
    except sqlite3.Error as e:  
        print(f"Ошибка при обновлении категории: {e}")
    
def update_product(conn):
    product_name = simpledialog.askstring("Введите новое название продукта: ", "Введите новое название продукта: ")
    product_id = simpledialog.askstring("Введите id продукта: ", "Введите id продукта: ")
    update_p = """
    UPDATE
        product
    SET
        product_name = ?
    WHERE
        product_id = ?;
    """
    cursor = conn.cursor()
    try:
        cursor.execute(update_p, (product_name, product_id))
        conn.commit()  
        print("Название продукта успешно обновлено")
    except sqlite3.Error as e: 
        print(f"Ошибка при обновлении продукта: {e}")


    
# 7. Применяйте запросы для удаления продуктов по определенным критериям (например, все продукты определенной категории или бренда).


def delete_brand(conn):
    brand_id = simpledialog.askstring("Введите id бренда: ", "Введите id бренда: ")
    delete_b = """
    DELETE FROM
        brand
    WHERE
        brand_id = ?;
    """
    cursor = conn.cursor()
    try:
        cursor.execute(delete_b, (brand_id,))
        conn.commit()  
        print("Бренд успешно удален")
    except sqlite3.Error as e:  
        print(f"Ошибка при удалении бренда: {e}")

def delete_category(conn):
    category_id = simpledialog.askstring("Введите id категории: ", "Введите id категории: ")
    delete_c = """
    DELETE FROM
        category
    WHERE
        category_id = ?;
    """
    cursor = conn.cursor()
    try:
        cursor.execute(delete_c, (category_id,))
        conn.commit()
        print("Категория успешно удалена")
    except sqlite3.Error as e:
        print(f"Ошибка при удалении категории: {e}")

def delete_product(conn):
    product_id = simpledialog.askstring("Введите id продукта: ", "Введите id продукта: ")
    delete_p = """
    DELETE FROM
        product
    WHERE
        product_id = ?;
    """
    cursor = conn.cursor()
    try:
        cursor.execute(delete_p, (product_id,))
        conn.commit()
        print("Продукт успешно удален")
    except sqlite3.Error as e:
        print(f"Ошибка при удалении продукта: {e}")
    

    
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


# import tkinter as tk

# # Предположим, что у вас уже есть функции для выполнения запросов к базе данных

# def handle_show():
#     # Очищаем текстовое поле перед отображением новых данных
#     data_text.delete(1.0, tk.END)
    
#     if table_var.get() == "Бренды":
#         # Здесь должен быть код для отображения данных из таблицы "Бренды"
#         data_text.insert(tk.END, "Данные из таблицы 'Бренды':\n")
#         for row in execute_read_query(conn, select_br):
#             data_text.insert(tk.END, f"{row}\n")
                
#     elif table_var.get() == "Категории":
#         # Здесь должен быть код для отображения данных из таблицы "Категории"
#         data_text.insert(tk.END, "Данные из таблицы 'Категории':\n")
#         for row in execute_read_query(conn, select_cat):
#             data_text.insert(tk.END, f"{row}\n")
            
#     elif table_var.get() == "Продукты":
#         # Здесь должен быть код для отображения данных из таблицы "Продукты"
#         data_text.insert(tk.END, "Данные из таблицы 'Продукты':\n")
#         for row in execute_read_query(conn, select_prod):
#             data_text.insert(tk.END, f"{row}\n")
            
#     pass



# def handle_add():
#     # Здесь должен быть код для добавления данных в выбранную таблицу
#     if table_var.get() == "Бренды":
#         brand_name = add_entry.get()
#         insert_brand(conn)
        
#         # вызов функции для добавления бренда с использованием brand_name
#     elif table_var.get() == "Категории":
#         category_name = add_entry.get()
#         insert_category(conn)
        
#         # вызов функции для добавления категории с использованием category_name
#     elif table_var.get() == "Продукты":
#         product_name = add_entry.get()
#         insert_product(conn)
#         # вызов функции для добавления продукта с использованием product_name
#     pass

# def handle_delete():
#     if table_var.get() == "Бренды":
#         delete_brand(conn)
#         # Здесь должен быть код для удаления данных из выбранной таблицы
    
#     elif table_var.get() == "Категории":
#         delete_category(conn)
#     # Здесь должен быть код для удаления данных из выбранной таблицы
    
#     elif table_var.get() == "Продукты":
#         delete_product(conn)
    
#     pass

# def handle_edit():
#     # Здесь должен быть код для редактирования данных в выбранной таблице
#     if table_var.get() == "Бренды":
#         update_brand(conn)
#         # вызов функции для изменения данных в таблице "Бренды"
#     elif table_var.get() == "Категории":
#         update_category(conn)
#         # вызов функции для изменения данных в таблице "Категории"
#     elif table_var.get() == "Продукты":
#         update_product(conn)
#         # вызов функции для изменения данных в таблице "Продукты"
        
#     pass


# def handle_close():
#     root.destroy()

# root = tk.Tk()
# root.title("Менеджер товаров")

# # Фрейм для отображения данных
# data_frame = tk.Frame(root)
# data_frame.pack(pady=10)

# # Фрейм для радиокнопок выбора таблицы
# table_frame = tk.Frame(root)
# table_frame.pack(pady=5)

# # Фрейм для кнопок действий
# action_frame = tk.Frame(root)
# action_frame.pack(pady=5)

# # Отображение данных
# data_text = tk.Text(data_frame, height=10, width=50)
# data_text.pack()

# # Радиокнопки для выбора таблицы
# table_var = tk.StringVar(value="Бренды")
# tk.Radiobutton(table_frame, text="Бренды", variable=table_var, value="Бренды").pack(side=tk.LEFT)
# tk.Radiobutton(table_frame, text="Категории", variable=table_var, value="Категории").pack(side=tk.LEFT)
# tk.Radiobutton(table_frame, text="Продукты", variable=table_var, value="Продукты").pack(side=tk.LEFT)

# # Поле ввода для добавления данных
# add_label = tk.Label(action_frame, text="Введите данные:")
# add_label.pack(side=tk.LEFT, padx=5)
# add_entry = tk.Entry(action_frame)
# add_entry.pack(side=tk.LEFT, padx=5)

# # Кнопки действий
# tk.Button(action_frame, text="Показать", command=handle_show).pack(side=tk.LEFT, padx=5)
# tk.Button(action_frame, text="Добавить", command=handle_add).pack(side=tk.LEFT, padx=5)
# tk.Button(action_frame, text="Удалить", command=handle_delete).pack(side=tk.LEFT, padx=5)
# tk.Button(action_frame, text="Изменить", command=handle_edit).pack(side=tk.LEFT, padx=5)
# tk.Button(action_frame, text="Закрыть", command=handle_close).pack(side=tk.LEFT, padx=5)

# root.mainloop() 
# conn.close()


# import tkinter as tk
# from tkinter import messagebox
# from tkinter import simpledialog

# Предположим, что у вас уже есть функции для выполнения запросов к базе данных

def handle_show():
    # Очищаем текстовое поле перед отображением новых данных
    data_text.delete(1.0, tk.END)
    
    if table_var.get() == "Бренды":
        
        data_text.insert(tk.END, "Данные из таблицы 'Бренды':\n")
        for row in execute_read_query(conn, select_br):
            data_text.insert(tk.END, f"{row}\n")
                
    elif table_var.get() == "Категории":
       
        data_text.insert(tk.END, "Данные из таблицы 'Категории':\n")
        for row in execute_read_query(conn, select_cat):
            data_text.insert(tk.END, f"{row}\n")
            
    elif table_var.get() == "Продукты":
        
        data_text.insert(tk.END, "Данные из таблицы 'Продукты':\n")
        for row in execute_read_query(conn, select_prod):
            data_text.insert(tk.END, f"{row}\n")
            
    pass

def handle_add():
    
    if table_var.get() == "Бренды":
        brand_name = add_entry.get()
        insert_brand(conn)
        
        
       
    elif table_var.get() == "Категории":
        category_name = add_entry.get()
        insert_category(conn)
        
        
    elif table_var.get() == "Продукты":
        product_name = add_entry.get()
        insert_product(conn)
       
    pass

def handle_delete():
    if table_var.get() == "Бренды":
        delete_brand(conn)
        
    
    elif table_var.get() == "Категории":
        delete_category(conn)
    
    
    elif table_var.get() == "Продукты":
        delete_product(conn)
    
    pass

def handle_edit():
    
    if table_var.get() == "Бренды":
        update_brand(conn)
        
    elif table_var.get() == "Категории":
        update_category(conn)
        
    elif table_var.get() == "Продукты":
        update_product(conn)
        
        
    pass


def handle_close():
    root.destroy()

def handle_change():
    new_value = simpledialog.askstring("Изменение", "Введите новое значение:")
    

root = tk.Tk()
root.title("Менеджер товаров")

# отображениe данных
data_frame = tk.Frame(root)
data_frame.pack(pady=10)

# Показ
table_frame = tk.Frame(root)
table_frame.pack(pady=5)

# Кнопки
action_frame = tk.Frame(root)
action_frame.pack(pady=5)

# Данные
data_text = tk.Text(data_frame, height=10, width=50)
data_text.pack()

# Радиокнопки
table_var = tk.StringVar(value="Бренды")
tk.Radiobutton(table_frame, text="Бренды", variable=table_var, value="Бренды").pack(side=tk.LEFT)
tk.Radiobutton(table_frame, text="Категории", variable=table_var, value="Категории").pack(side=tk.LEFT)
tk.Radiobutton(table_frame, text="Продукты", variable=table_var, value="Продукты").pack(side=tk.LEFT)

# Поле ввода для добавления данных
add_label = tk.Label(action_frame, text="Введите данные:")
add_label.pack(side=tk.LEFT, padx=5)
add_entry = tk.Entry(action_frame)
add_entry.pack(side=tk.LEFT, padx=5)

# Кнопки
tk.Button(action_frame, text="Показать", command=handle_show).pack(side=tk.LEFT, padx=5)
tk.Button(action_frame, text="Добавить", command=handle_add).pack(side=tk.LEFT, padx=5)
tk.Button(action_frame, text="Удалить", command=handle_delete).pack(side=tk.LEFT, padx=5)
tk.Button(action_frame, text="Изменить", command=handle_edit).pack(side=tk.LEFT, padx=5)
tk.Button(action_frame, text="Закрыть", command=handle_close).pack(side=tk.LEFT, padx=5)

root.mainloop() 