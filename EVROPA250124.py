from random import *

# Составьте словарь, где перечислите часть стран Европы.

# Ключом будет страна, описанием столица или наоборот.

# При помощи функций реализуйте возможности:

#     отображение столицы, если вводиться название государства и наоборот.
#     если искомое слово отсутствует в словаре, дайте пользователю возможность добавить его в словарь.
#     если пользователь находит ошибку в словаре, то у него должна быть возможность ее исправить.
#     При желании пользователя проверить знание слов из словаря, реализуйте эту возможность  
#                 случайным образом появляются названия столиц/стран,
#                 после ввода соответствующего значения, сообщение о правильности или нет
#                 после окончания проверки знаний результат в %)


def faillist_to_dict(f:str):
    riik_pealin={} #sonastik {riik:pealinn}
    pealinn_riik={} #sonastik {pealinn:riik}
    riigid=[] #list riikidest
    file=open(f,'r', encoding="UTF-8-sig")
    for line in file:
        k,v=line.strip().split('-')
        riik_pealin[k]=v
        pealinn_riik[v]=k
        riigid.append(k)
    file.close()
    return riik_pealin, pealinn_riik, riigid
    #kaivitame loodud funktsion
riik_pealinn, pealinn_riik, riigid=faillist_to_dict('riigid_pealinnad.txt')
riigid=list(riik_pealinn.keys())
print(f'Страны и столицы: ',riik_pealinn)

while True:
    riik=input('Страна: ')
    if riik=='':
        print(riik_pealinn[riik])
    else:
        print('Нет такой страны')
    pealinn=input('Столица: ')
    if pealinn=='':        
        print(pealinn_riik[pealinn])
    else:
        print('Нет такой столицы')
    if riik not in riigid:
        print(' ')
        lisada=input('Вы хотите добавить? (y/n)')
        if lisada=='y':
            riik_pealinn[riik]=pealinn
            pealinn_riik[pealinn]=riik
            riigid.append(riik)
            print('Добавленa')
        else:
            print('Не добавлена')
    else:
        print('Такая страна существует')
        muuta=input('Хотите изменить? (y/n)')
        if muuta=='y':
            riik_pealinn[riik]=pealinn
            pealinn_riik[pealinn]=riik
            print('Изменен')
        else:
            print('Не изменен')
#     При желании пользователя проверить знание слов из словаря, реализуйте эту возможность  
#                 случайным образом появляются названия столиц/стран,
#                 после ввода соответствующего значения, сообщение о правильности или нет
#                 после окончания проверки знаний результат в %)
    kontroll=input('Хотите проверить знание? (y/n)')
    if kontroll=='y':
        oige=0
        vale=0
        for i in range(5):
            riik=choice(riigid)
            print(riik)
            pealinn=input('Столица: ')
            if pealinn==riik_pealinn[riik]:
                print('Правильно')
                oige+=1
            else:
                print('Неправильно')
                vale+=1
        print(f'Правильно: {oige} Неправильно: {vale}')
        print(f'Процент правильных ответов: {oige/(oige+vale)*100}%')
    else:
        print('До свидания')
        break           



        
                


