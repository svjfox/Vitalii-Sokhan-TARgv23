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
        k,v=line.strip().split('-') #k=voti, v=vaartus
        riik_pealin[k]=v
        pealinn_riik[v]=k
        riigid.append(k)
    file.close()
    return riik_pealin, pealinn_riik, riigid
    #kaivitame loodud funktsion
riik_pealinn, pealinn_riik, riigid=faillist_to_dict('riigid_pealinnad.txt')
riigid=list(riik_pealinn.keys())
print(riigid)

while True:
    riik=input('Riik: ')
    print(riik_pealinn[riik])
    pealinn=input('Pealinn: ')
    print(pealinn_riik[pealinn])
    if riik not in riigid:
        print('Нет такой страны')
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

                


