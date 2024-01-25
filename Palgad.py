from Funktcion import *
#1-Добавить еще несколько человек и зарплат(кол-во говорит пользователь),



#2-Удалить человека и его зарплату(вводим имя),



#3-Самую большую зарплату и кто ее получает,

#4-Кто получает самую маленькую зарплату и какую именно,

#5-Упорядочить зарплаты в порядке возрастания и убывания вместе с именами,

#6-Узнать, кто получает одинаковую зарплату, найти сколько таких людей вывести их данные на экран.

#7-Сделать поиск зарплаты по имени человека. Учесть, что имена могут повторяться,

#8-Вывести список тех людей(с зарплатами), кто получает больше/меньше чем указанная сумма.

#9-Top() - Т самых бедных и самых богатых человека

#10-Keskmine() - Среднюю зарплату и имя человека ее получающего

#11-Tulumaks() - Вычислить зарплату, которую человек получит на руки после вычисления подоходного налога.
#tulud
#link
#pangakalkulaator

#12- Осуществить сортировку по имени (можно предостваит пользователю выбор от А до Я или от Я до А)

#13- Находить тех кто получает зарплату ниже средней и удалить их из списков.

#14- Отредактировать списки таким образом, чтоб в списке людей имена были написаны с большой буквы, о зарплаты в формате int.

#15 - Каждый год работникам фирмы поднимают зарплату на 5%, узнай какой будут зарплаты/зарплата у опрделенного работника через Т лет.

#16 - "Переименовать" каждого третьего человека. Новые имена вводит пользователь.

#17 - Написать функцию для редактирования данных. Пользователь выбирает, что редактировать: имя или зарплату. Измененние данные сохраняются  в список.

#18 -  Найти имена начинающиеся на введенную букву и их зарплаты. Отобразить данные в столбик (Имя-зарплата)

#19-Придумай свою функцию

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
print(palgad)
print(inimesed)

while True:
    print("Lisamine-1\nKustutamine-2\nSuurimPalk-3\nSort-5\nzarplataravna-6")
    v=int(input())
    if v==1:
        k=int(input("Mitu inimest lisame? "))
        inimesed,palgad=Lisamine(inimesed, palgad,k)
        for i in range(len(palgad)):
            print(inimesed[i], "saab katte",palgad[i])
    elif v==2:
        inimesed,palgad=Kustutamine(inimesed, palgad)
        print(inimesed)
        print(palgad)
    elif v==3:
        maxpalk, nimi=SuurimPalk(inimesed,palgad)
        print(nimi,"saab katte",maxpalk,"Eur")
    elif v==5:
        i=int(input("Kasvad-0,Kahaned-1"))
        inimesed,palgad=Sort(inimesed,palgad,i)
        for i in range(len(palgad)):
            print(palgad[i],"on",inimesed[i],"-l")
    elif v==6:
        inimesed,palgad=zarplataravna(inimesed,palgad)
        for i in range(len(palgad)):
            print(inimesed[i], "saab katte",palgad[i])
    else:
        print("Vale valik")
print("Kas soovite veel midagi teha? (y/n)")
        