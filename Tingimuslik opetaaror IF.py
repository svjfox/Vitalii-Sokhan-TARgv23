﻿# 1 Если имя Juku, то пойдем с Juku в кино.

#name=input("Kak tvoe imja: ")
#if name=="Juku":
#    print("Poshli v kino ",name)
#else:
#    print("My ne pojdem v kino")

# 2 Добавьте опцию, где в зависимости от возраста Vega вы решаете, какой билет ему купить.

    #<6 лет - бесплатно
    #6-14 – детский билет
    #15-65 - полный билет
    #>65 - билет со скидкой
    #<0 и >100 ошибок с данными

#vozrast=int(input("Skolko tebe let? "))
#if 0<vozrast<100:
#    if vozrast<6:
#        print("бесплатно")
#    elif 5<vozrast<15:
#        print("детский билет")  
#    elif vozrast>65:
#        print("билет со скидкой")
#    else:
#        print("полный билет")
#else:
#    print("ошибka с данными")
    


# 3 Спросите имена двух человек и объявите, что они сегодня ближайшие соседи

#name=input("Kak tvoe imja? ")
#name2=input("A kak tvoe imja? ")
#print("Vy, ",name,"i",name2,"segodnja blizhaishie sosedi!")



#Запросите длины стен прямоугольной комнаты и вычислите площадь пола. Спросите пользователя, 
#хочет ли он сделать ремонт, если он положительный, то спросите, 
#сколько стоит квадратный метр, и узнайте цену замены пола.

# A=float(input("Kakaja dlinna 1 steny? "))
# B=float(input("Kakaja dlinna 2 steny? "))
# S=A*B
# print("Ploshad pola =",S)
# remont=input("Ty hochesh sdelat remont pola? ")
# if remont=="da" or remont=="yes":
#    cena=float(input("Skolko stoit remont za metr kv? "))
#    summa=S*cena
#    print("Stoimost remonta budet",summa)
# else:
#    print("Ok, togda remont pola ne delaem")


# 4 Найдите цену со скидкой 30%, если первоначальная цена больше 700


# skidka=float(0.3)
# cena=float(input('Какая стоимость товара - '))
# cena_skidka=round(cena-(cena*skidka),2)

# if cena>700:
#     print('При цене в',cena,'i skidke 30% stoimost budet',cena_skidka)
# else:
#     print('При цене в',cena,'скидка не начисляется.')


# 5 Спросите температуру и скажите, выше ли она восемнадцати градусов (зимой предпочтительнее комнатная температура)

#temperatura=float(input("Kakaja seichas temperatura? "))
#if 0<temperatura<18:
#    print("Segodnja prohladno")
#elif temperatura>17:
#    print("Horoshaya pogoda")
#else:
#    print("зимой предпочтительнее комнатная температура")


# 6 Спросите рост человека и скажите, низкий он, средний или высокий (установите пределы сами)

#r=float(input("Kakoj u tebja rost? "))
#if 60<r<120:
#    if 60<r<76:
#        print("Ty nizkij.")
#    elif 75<r<91:
#        print("Ty srednij")
#    elif 90<r<120:
#        print("Ty vysokij")
    
#else:
#    print("Rost ne vernyj")



# 7 Спросите у человека его рост и пол и скажите, низкий он, средний или высокий (несколько блоков условий могут находиться друг в друге).

# pol=input('Какой Ваш пол? ')
# if pol=='мужской' or pol=='женский':
#     r=float(input("Kakoj u tebja rost? "))
#     if 60<r<120:
#         if 60<r<76:
#             print("Ty nizkij.")
#         elif 75<r<91:
#             print("Ty srednij")
#         elif 90<r<120:
#             if 90<r<101:
#                 print("Ty vysokij")
#             elif 100<r<120:
#                 print("Ty ochen vysokij")
#     else:
#         print("Человек не может быть такого роста")
# else:
#     print('Я не совсем понял какой у Вас пол.')



# 8 Отдельно спросите человека в магазине, хочет ли он купить молоко, хлеб или булку. 
# Сложите цены и сообщите мне, сколько будет стоить все, что вы купили.


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# cena_M=2.5
# cena_X=1.0
# cena_B=1.5

# M=input('Вы хотите купить молоко? (да/нет) ')
# X=input('Вы хотите купить хлеб? (да/нет) ')
# B=input('Вы хотите купить булку? (да/нет) ')

# if M=='да' or X=='да' or B=='да':
    
  
    







# 9 Площадь
# Пользователь вводит стороны квадрата, и программа определяет, может ли это быть квадрат.
# Создайте соответствующую блок-схему и сохраните ее в том же каталоге, что и программа.

# Storona_A=float(input('Сторона А = '))
# Storona_B=float(input('Сторона B = '))
# if Storona_A==Storona_B:
#     Storona_C=float(input('Сторона C = '))
#     if Storona_C==Storona_A:
#          Storona_E=float(input('Сторона E = '))
#          if Storona_E==Storona_A:
#                print('При условии что у фигуры все углы 90 градусов, то это Квадрат')
#          else:
#                print('Данная фигура не является квадратом')
#     else:
#         print('Данная фигура не является квадратом')
# else:
#     print('Данная фигура не является квадратом')

# 10 Математика
#Пользователь вводит два числа, и программа спрашивает пользователя, какое действие он хочет (+-*/), 
#и реализует выбор пользователя.
#Создайте соответствующую блок-схему и сохраните ее в том же каталоге, что и программа.

# A=float(input("Введите первое число: "))
# B=float(input("Введите второе число: "))

# C=input("Выберите операцию (+, -, *, /): ")

# if C == "+":
#     E = A + B
#     print(f"Результат : {E}")
# elif C == "-":
#     E = A - B
#     print(f"Результат : {E}")
# elif C == "*":
#     E = A * B
#     print(f"Результат : {E}")
# elif C == "/":
#        if B != 0:
#         E = A / B
#         print(f"Результат : {E}")
#        else:
#         print("Ошибка: Деление на ноль невозможно.")
# else:
#     print("Пожалуйста, выберите из '+', '-', '*', '/'.")




# 11 юбилей
# Пользователь вводит свой день рождения, и ваша программа сообщает вам, является ли это годовщина.
# Блок-схема не нужна!

# god = float(input("Введите год своего рождения: "))
# vozrast=2023-god
# if vozrast %5==0:
#     print('У вас годовщина!')
# else:
#     print('У Вас обычный день рождения!')



# 12 продаж
#Пользователь вводит цену товара. Если цена достигает 10 евро, он получает скидку 10%. На товары стоимостью более 10 евро предоставляется скидка 20%.
#Укажите окончательную цену товара. Блок-схема не нужна!

# cena = float(input("Введите цену товара в евро: "))

# if cena == 10:
#     discount = 0.1
# elif cena > 10:
#     discount = 0.2
# else:
#     discount = 0

# final_cena = cena * (1 - discount)
# print(f"Окончательная цена товара: {final_cena} евро")



# 13 Футбольная команда
#Вам нужно создать программу, которая проверяет, подходит ли кандидат данной команде.
#Возраст должен быть от 16 до 18 лет, допускаются только мужчины.
#Завершите программу так, чтобы, если заявитель женщина, возраст вообще не спрашивался.

# pol=input('Какой Ваш пол (мужской/женский)? ')
# if pol=='мужской':
#     r=float(input("Kakoj u tebja vozrast? "))
#     if 15<r<19:
#         print("Вы приняты")
#     else:
#         print("Извините, вы не подходите нам по возрасту.")
# else:
#     print('Извините, нам требуются мужчины.')





# 14 Автобусная логистика
# Допустим, нам необходимо перевезти определенное количество людей в автобусах с определенным количеством мест. 
# Сколько автобусов нужно, чтобы доставить всех людей, и сколько человек в последнем автобусе 
# (при условии, что все предыдущие полностью заполнены)? Напишите программу, которая запрашивает количество людей и 
# размер автобусов, а затем решает эту задачу.

L=int(input('Сколько людей нужно перевести? - '))
mest=int(input('Сколько мест в автобусе? - '))
avtobusov=L//mest
ludej_v_posl_avtobuse=L%mest
if ludej_v_posl_avtobuse>0:
    avtobusov+=1
print(f'Нужно {avtobusov}, в последнем автобусе {ludej_v_posl_avtobuse}.')
