# Составьте два списка слов, например, на русском и эстонском языках.

# Каждый список сохраните с отдельный текстовый файл (rus.txt, est.txt).

# При помощи функций реализуйте возможности:

#     перевода с эстонского языка на русский и с русского на эстонский.
#     если искомое слово отсутствует в словаре, дайте пользователю возможность добавить его в словарь.
#     если пользователь находит ошибку в словаре, то у него должна быть возможность ее исправить.
#     При желании пользователя проверить знание слов из словаря, реализуйте эту возможность

#          -случайным образом появляются слова из списка,
#          -после ввода перевода, сообщение о правильности или нет
#          -после окончания проверки знания слов  результат в %)

# *Реализуйте возможность text to speech/проговаривание слов(для самостоятельного изучения)

# При работе с кириллицей необходимо помнить про кодировку(текстовый файл сохранить с кодировкой "utf-8" и обращаясь к файлу ее учитывать f=open("rus.txt",'r',encoding="utf-8-sig")).

# --------------------------------------------------

# Код функции для считывания в список данных из файла:

from logging.handlers import WatchedFileHandler
from multiprocessing.managers import ValueProxy


def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

rus:list=loe_failist("rus.txt")

est:list=loe_failist("est.txt")

print(rus)
print(est)

#     перевода с эстонского языка на русский и с русского на эстонский.
Vybor_jazyka='0'
for i in range(1,11) or Vybor_jazyka=='3':
    Vybor_jazyka=input("Выберите язык: 1-русский, 2-эстонский, 3-закрыть: ")
    if Vybor_jazyka=="1":
        print("Вы выбрали русский язык")
        print("Введите слово на русском языке: ")
        slovo=input()
        if slovo in rus:
            index=rus.index(slovo)
            print("Перевод слова: ",est[index])
        else:
            print("Такого слова нет в словаре")
            print("Хотите добавить слово в словарь? 1-да, 2-нет")
            Vybor=input()
            if Vybor=="1":
                print("Введите перевод слова: ")
                perevod=input()
                rus.append(slovo)
                est.append(perevod)
                print("Слово добавлено в словарь")
            else:
                print("Слово не добавлено в словарь")
    elif Vybor_jazyka=="2":
        print("Вы выбрали эстонский язык")
        print("Введите слово на эстонском языке: ")
        slovo=input()
        if slovo in est:
            index=est.index(slovo)
            print("Перевод слова: ",rus[index])
        else:
            print("Такого слова нет в словаре")
            print("Хотите добавить слово в словарь? 1-да, 2-нет")
            Vybor=input()
            if Vybor=="1":
                print("Введите перевод слова: ")
                perevod=input()
                est.append(slovo)
                rus.append(perevod)
                print("Слово добавлено в словарь")
            else:
                print("Слово не добавлено в словарь")
else:
    print("Вы закрыли программу")


            
