
from math import *
from random import *




# for x in range(10):
#     R=float(input("{0}.R: ".format(x+1)))
#     if R>0:
#         S=3.14*R**2
#     else:        
#         S='R peab > kui 0 olema'
#     print("S={0}".format(S))



# x=0
# while True:
#     x+=1
#     R=float(input("{0}.R: ".format(x+1)))
#     if R>0:
#         S=3.14*R**2
#     else:        
#         S='R peab > kui 0 olema'
#     print("S={0}".format(S))
#     if x==10:
#         break



## 10 R
# x=0
# while x<10:
#     x+=1
#     R=float(input("{0}.R: ".format(x)))
#     if R>0:
#         S=3.14*R**2
#     else:        
#         S='R peab > kui 0 olema'
#     print("S={0}".format(S))
  


##10 S
# x=0
# while x<10:
#     R=float(input("{0}.R: ".format(x)))
#     if R>0:
#         S=3.14*R**2
#         x+=1
#     else:        
#         S='R peab > kui 0 olema'
#     print("S={0}".format(S))



## 1. Вводят 15 чисел. Определить, сколько среди них целых.
#
 #t=0
 #for x in range(15):
 #    a=float(input("Sisesta a: "))
 #    if a.is_integer(): # 2.0 == True; 2.45 == False
 #        t+=1
 #print(t)





# 2. Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.

# summa=0
# a=int(input("Sisesta a: "))
# for x in range (1,a+1,1):
#     summa+=x
# print('Summa: {0}'.format(summa))


# # 3.    Вводят 8 чисел. Найти их произведение (только положительных).

#p=1
#lause=''
#for x in range(8):
#    a=float(input("{0}, samm\nSisesta a: ".format(x+1)))
#    if a>0:
#        p*=A
#        lause=lause+str(a)+"*"
#print(lause[:-1],'=',p,end="")


# # 4.    Составьте программу, выводящую на экран квадраты чисел от 10 до 20.


# for x in range (10,21,1):
#    i=sqrt(x)
#    print(round(i,2))
    



# # 5.    Составьте программу, которая вычисляет сумму только отрицательных из N чисел. Значение N вводится с клавиатуры.


# summ=0
# while True:
#    n=float(input("N = "))
#    if n<0:
#        summ+=n
#    print(summ)



# # 6.    С клавиатуры вводятся N чисел.

# # Составьте программу, которая определяет количество отрицательных,

# #  количество положительных и количество нулей среди введенных чисел.  

# # Значение N вводится с клавиатуры.

# summ1=0
# summ2=0
# summ3=0
# while True:
#    n=float(input("N = "))
#    if n<0:
#        summ1+=1
#        print('Количество N<0 =',summ1)
#    elif n>0:
#        summ2+=1
#        print('Количество N>0 =',summ2)
#    elif n==0:
#         summ3+=1
#         print('Количество N=0 =',summ3)




# # 7.    Вывести на экран числа, кратные К из промежутка [А,В].

# K=int(input("K = "))
# a=int(input("A = "))
# b=int(input("B = "))
# for x in range(a,b+1):
#     if x%K==0:
#         print(x,end=" ")
    


# # 8.    Составьте программу, которая печатает таблицу перевода расстояний из дюймов в сантиметры (1 дюйм =
# # 2,5 см) для значений длин от 1 до 20 дюймов.


# x=1
# y=2.5
# Z=x*y
# for x in range (20):
#    x+=1
#    Z=x*y
#    print(f'{x} дюйм. = {Z} см.')




# # 9.    В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?

# S=float(input("Summa evro = "))
# N=int(input("Kolichestvo let = "))
# p=0.03
# for x in range(N):
#    Proc_za_1_god=S*p
#    S+=Proc_za_1_god
# print("Za period summa depozita budet ravna - ",round(S,2))




# # 10. Ввести с клавиатуры 10 пар чисел.  Сравнить числа в каждой паре и напечатать большие из них.

# for x in range(10):
#    A=float(input("A = "))
#    B=float(input("B = "))

#    if A>B:
#        print(f"Bolshee chislo: {A}")
#    elif A<B:
#        print(f"Bolshee chislo: {B}")
#    else:
#        print("Chisla ravny")



# # 11.Найти произведение двузначных нечетных чисел, кратных случайно сгенерированному числу.

# random = randint(1,9)
# print("Random number: ", random)
# for x in range(11, 100, 2):
#     if x%random==0:
#         x*=x
#         print(x, end=" ")
       


# # 12.В бригаде, работающей на уборке сена, имеется N сенокосилок.

# # Первая сенокосилка работала m часов, а каждая следующая на 10 минут больше, чем предыдущая.

# # Сколько часов проработала вся бригада?


#N=randint(2,10)
#m=randint(1,10)
#print("Masinad: ",N)
#print("Tunid: ",m)
#summa=m
#for t in range(N-1):
#     m=(m/6)*7
#     summa+=m
#     print(m)
#print("Kokku masinad tõõtasid:",summa,"tn")





# # 13.Найти все натуральные числа от 100 до 1000 кратные 7.
#И посчитать их колличество и сумму.

#summ=0
#summ2=0
#for x in range(100,1001):
#    if x%7==0:
#        print(x, end=" ")
#        summ+=1
#        summ2+=x
#print("\nКоличество чисел =",summ)
#print("Сумма данных чисел =",summ2)
         


# # 14.Составьте программу, которая вычисляет произведение чисел от 1 до N. Значение N создается случайным образом.


#n=randint(2,10)
#print(f"N = {n}")
#t=1
#for x in range (1,n+1):
#    t*=x
#print(f"Произведение чисел от 1 до N = {t}")
    



# # 15.Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, то есть в таком виде:
# # 0 1 2 3 4 5 6 7 8 9
# # 0 1 2 3 4 5 6 7 8 9
# # ...................
# # 0 1 2 3 4 5 6 7 8 9

#for x in range(10):
#    for x in range(10):
#        print(x,end=" ")
#    print()




# # 16.Напишите программу, печатающую столбик строк такого вида:
# # 1 0 0 0 0 0 0 0 0
# # 0 2 0 0 0 0 0 0 0
# # 0 0 3 0 0 0 0 0 0
# # 0 0 0 4 0 0 0 0 0
# # 0 0 0 0 5 0 0 0 0
# # 0 0 0 0 0 6 0 0 0
# # 0 0 0 0 0 0 7 0 0
# # 0 0 0 0 0 0 0 8 0
# # 0 0 0 0 0 0 0 0 9

#x=1
#for x in range(9):
#    for x in range (9):
#        print ("0" ,end=" ")
#    print ()




# # 17.Напишите программу, печатающую столбик таблицу умножения такого вида:
# # 2*1=2
# # 2*2=4
# # 2*3=6
# # 2*4=8
# # 2*5=10
# # 2*6=12
# # 2*7=14
# # 2*8=16
# # 2*9=18

#for x in range (1,10):
#    t=2*x
#    print(f"2*{x}={t}")



# # 18.    Даны натуральные числа от 20 до 50. Напечатать те из них, которые делятся на 3, но не делятся на 5.

# for x in range(20, 51):
#    if x%3==0:
#        if x%5!=0:
#            print(x, end=" ")



# # 19.    Даны натуральные числа от 35 до 87. Найти и напечатать те из них, которые при делении на 7 дают остаток

# # 1, 2 или 5.

#for x in range (35, 88):
#    t=x//7
#    a=x%7
#    if a==1 or a==2 or a==5:
#        print (x, end=(" "))





# # 20.    Даны натуральные числа от 1 до 50. Найти сумму тех из них, которые делятся на 5 или на 7.
#summa=0
#for x in range (1,51):
#    if x%5==0 or x%7==0:
#        print(x, end=(" "))
#        summa+=x
#print (f"\nСумма чисел которые делятся на 5 или на 7 = {summa}")






# # 21.    Ввести с клавиатуры 10 чисел – положительных и отрицательных. Заменить все отрицательные числа их

# # модулями и напечатать все полученные 10 чисел.

# for i in range (1,11):
#     x=int(input(f"{i}. Введите число - "))
#     if x >=0:
#         x==x
#     elif x<0:
#         x=x*(-1)
#     print(f"Модуль числа {x}")
# print 
        




 
# # 22.    Найти сумму чисел от 100 до 200, кратных 17.
 



 
# # 23.    В ЭВМ вводятся координаты N точек. Определить, сколько из них попадает в круг радиусом R с центром в точке (a,b).
 
# # 24.    В ЭВМ вводятся по очереди данные о росте N учащихся класса. Определить средний рост учащихся класса.
 
# # 25.    Задано натуральное число N. Найти количество натуральных чисел, не превосходящих N и не делящихся ни на одно из чисел 2, 3, 5.
 
# # 26.    Два двузначных числа, записанных одно за другим, образуют четырехзначное число, которое

# # делится на их произведение. Найти эти числа.
 
# # 27. Даны два двузначных числа А и В. Из этих чисел составили два четырехзначных числа: первое число

# # получили путем написания сначала числа A, а затем В; для получения второго

# # сначала записали В, а потом А. Найти числа А и В, если известно, что первое

# # четырехзначное число нацело делится на 99, а второе – на 49.

 

# # 28.    Реализуйте "мини лотерею". Пусть компрьютер "задумает число", а пользователь его должен отгадать. В конце сообщив количество попыток.

 

# # 29.Напишите программу, печатающую столбик строк такого вида:
# # x 0 0 0 0 0 0 0 0
# # x x 0 0 0 0 0 0 0
# # x 0 x 0 0 0 0 0 0
# # x 0 0 x 0 0 0 0 0
# # x 0 0 0 x 0 0 0 0
# # x 0 0 0 0 x 0 0 0
# # x 0 0 0 0 0 x 0 0
# # x 0 0 0 0 0 0 x 0
# # x 0 0 0 0 0 0 0 x

# for i in range(9):
#    for x in range(9):
#        if x==0 or x==(i-1)+1:
#            print("x",end=" ")
#        else:
#            print("0", end=" ")
#    print()



# # 30.    В программе создаются 2 случайных числа M и N. И выводятся на экран в срочку 2 последовательности от N к M,

# #  и обратно  .

# # 31.  Губка Боб жарит котлеты. Всего у него К котлет, на одну сковородку помещается М котлет.

# # Расчитать сколько сковородок "полных" надо пожарить и сколько котлет останется еще дожарить на последней.