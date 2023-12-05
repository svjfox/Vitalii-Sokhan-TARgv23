# Написать программу для проверки знаний по математике.

# Предложить пользователю выбрать сложность заданий.
# Например:

#     Tase 1, Tase 2, Tase 3
#     количество действий(+,-,/,*,**)
#     величину случайно генерируемых чисел.


# В программе случайным образом "задаются" примеры, с учетом сложности провряемых знаний.
# После введенного пользователем ответа, проверяется его правильностью.

# Придумать условие выхода из цикла.(можно сначала указать количество примеров)

# В конце работы программы, надо сообщить тестируемому оценку.
# <60% - Hinne 2
# 60-75% - Hinne 3
# 75-90% - Hinne 4
# >90% - Hinne 5

from random import *
from math import *

print("<<<Программа для проверки знаний по математике>>>")
print()
print("Выберите сложность заданий:")
tase=int(input("1.Легкие\n2.Средние\n3.Сложные\n"))
print()
N_zadanij=int(input("Введите количество заданий: "))
print()
pravilnyh_otvetov=0

for i in range(N_zadanij):
    if tase==1:
        a=randint(1,10)
        b=randint(1,10)
        c=randint(2,3)
        znak=randint(1,5)
        if znak==1:
            otvet=int(input(f"{a}+{b}="))
            if otvet==a+b:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==2:
            otvet=int(input(f"{a}-{b}="))
            if otvet==a-b:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==3:
            otvet=int(input(f"{a}*{b}="))
            if otvet==a*b:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==4:
            otvet=float(input(f"{a}/{b}="))
            if otvet==round(a/b,2):
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==5:
            otvet=int(input(f"{a}^{c}="))
            if otvet==a**c:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
    elif tase==2:
        a=randint(1,100)
        b=randint(1,100)
        c=randint(2,3)
        znak=randint(1,5)
        if znak==1:
            otvet=int(input(f"{a}+{b}="))
            if otvet==a+b:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==2:
            otvet=int(input(f"{a}-{b}="))
            if otvet==a-b:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==3:
            otvet=int(input(f"{a}*{b}="))
            if otvet==a*b:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==4:
            otvet=float(input(f"{a}/{b}="))
            if otvet==round(a/b,2):
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==5:
            otvet=int(input(f"{a}^{c}="))
            if otvet==a**c:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
    elif tase==3:
        a=randint(1,1000)
        b=randint(1,1000)
        c=randint(2,3)
        znak=randint(1,5)
        if znak==1:
            otvet=int(input(f"{a}+{b}="))
            if otvet==a+b:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==2:
            otvet=int(input(f"{a}-{b}="))
            if otvet==a-b:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==3:
            otvet=int(input(f"{a}*{b}="))
            if otvet==a*b:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==4:
            otvet=float(input(f"{a}/{b}="))
            if otvet==round(a/b,2):
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
        elif znak==5:
            otvet=int(input(f"{a}^{c}="))
            if otvet==a**c:
                print("Правильно!")
                pravilnyh_otvetov+=1
            else:
                print("Неправильно!")
                
print()
print(f"Правильных ответов: {pravilnyh_otvetov}")
procent=round(pravilnyh_otvetov/N_zadanij*100)
print(f"Процент правильных ответов: {procent}%")
if procent<60:
    print("Hinne 2")
elif 60<=procent<75:
    print("Hinne 3")
elif 75<=procent<90:
    print("Hinne 4")
elif procent>=90:
    print("Hinne 5")
print()
print("<<<Программа завершена>>>")

            
    
    
    
