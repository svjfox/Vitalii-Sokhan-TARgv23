from random import *
# def summa3(arv1: float,arv2: float,arv3: float)->float:
#     '''Ищем сумму трех чисел
    
#     :param float arv1: первое число
#     :param float arv2: второе число
#     :param float arv3: третье число
#     :rtype: float
#     '''
#     summa = arv1 + arv2 + arv3
#     return summa


# (1)
# Простейшие арифметические операции

# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, 
# которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; 
# / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

# def aritmetik(a:float, b:float, t:str)->any:
#     '''Функция выполняет арифметические операции над двумя числамию
#     + - сложение
#     - - вычитание
#     * - умножение
#     / - деление
#     :param float a: первое число
#     :param float b: второе число
#     :param str t: операция
#     :rtype: var Maaramata tuup(float, str)
#     '''
#     if t in ['+','-','*','/']:
#         if b == 0 and t=='/':
#             vastus='DIV/0'
#         else:
#             vastus=eval(str(a)+t+str(b))
#     else:
#         vastus='Неизвестная операция'
       
#     return vastus






# 
# 
# (2)
# Високосный год

# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
# 
from tkinter import ROUND
from typing import is_typeddict


# def is_year_leap(god:int)->bool:
#     '''Функция определяет високосный год или нет
#     :param int god: год
#     :rtype: bool
#     '''
#     if god%4==0:
#         v=True
#     else:
#         v=False
#     return v



# 
# (3)
# Квадрат

# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр квадрата, 
# площадь квадрата и диагональ квадрата.

# def square(a:float)->any:
#     '''Функция возвращает периметр, площадь и диагональ квадрата
#     :param float a: сторона квадрата
#     :rtype: var Maaramata tuup(float, float, float)
#     '''
#     P=4*a
#     S=a**2
#     D=a*(2**0.5)
#     return P, S, D




# 
# 
# (4)
# Времена года

# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (talv, kevad, suvi или sügis).

# def season(mesjats:int)->str:
#     '''Функция возвращает время года по номеру месяца
#     :param int mesjats: номер месяца
#     :rtype: str
#     '''
#     if mesjats in [12,1,2]:
#         sezon='Зима'
#     elif mesjats in [3,4,5]:
#         sezon='Весна'
#     elif mesjats in [6,7,8]:
#         sezon='Лето'
#     elif mesjats in [9,10,11]:
#         sezon='Осень'
#     else:
#         sezon='Ошибка'
#     return sezon



# 
# 
# (5)
# Банковский вклад

# Пользователь делает вклад в размере a евро сроком на years лет под 10% годовых 
# (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, 
# и на них в следующем году тоже будут проценты).

# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

# def bank(a:float, years:int)->float:
#     '''Функция возвращает сумму вклада через years лет
#     :param float a: сумма вклада
#     :param int years: срок вклада
#     :rtype: float
#     '''
#     for i in range(years):
#         a=a*1.1
#     return a


# 
# 
# 
# (6)
# Простые числа

# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
# 

# def is_prime(a:randint(0,1000))->bool:
#     '''Функция определяет простое число или нет
#     :param int a: число
#     :rtype: bool
#     '''
#     if 0<=a<=1000:
#         if a==0 or a==1:
#             return False
#         else:
#             for i in range(2,a):
#                 if a%i==0:
#                     return False
#             return True
               
#     else:
#         return 'Число должно быть от 0 до 1000'
# 
# 
# 
# (7)
# Правильная дата

# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.
# 
# def date(den:int,mesjats:int,god:int)->bool:
#     '''Функция определяет правильная дата или нет
#     :param int den: день
#     :param int mesjats: месяц
#     :param int god: год
#     :rtype: bool
#     '''
#     if 0<den<=31 and 0<mesjats<=12 and 0<god<=9999:
#         if mesjats in [1,3,5,7,8,10,12]:
#             if den<=31:
#                 return True
#             else:
#                 return False
#         elif mesjats in [4,6,9,11]:
#             if den<=30:
#                 return True
#             else:
#                 return False
#         elif mesjats==2:
#             if god%4==0:
#                 if den<=29:
#                     return True
#                 else:
#                     return False
#             else:
#                 if den<=28:
#                     return True
#                 else:
#                     return False
#     else:
#         return False

def date(den:int,mesjats:int,god:int)->bool:
    '''Функция определяет правильная дата или нет
    :param int den: день
    :param int mesjats: месяц
    :param int god: год
    :rtype: bool
    '''
    if den in range(1,32) and mesjats in [1,3,5,7,8,10,12]:
        v=True
    elif den in range(1,29) and is_year_leap(god):
        v=True
    elif den in range(1,31) and mesjats in [4,6,9,11]:
        v=True
    else:
        v=False
    return v





# 
# 
# 
# (8)*
# XOR-шифрование

# Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, 
# и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом. 
# Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
