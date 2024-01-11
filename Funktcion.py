

from itertools import count


def Lisamine(i:list,p:list,k:int):
    """Andmete lisamine listadesse
    Tagastab listud

    :param list i: Inimesta nimekiri
    :param list p: Palkage loetelu
    :param int k: Inimeste kogus
    :rtype: list, list
    """
    for c in range (k):
        nimi=input("Mis on inimese nimi ")
        palk=int(input("Kui suur palk tal on? "))
        i.append (nimi)
        p.append (palk)
    return i,p

#2-Удалить человека и его зарплату(вводим имя),

def Kustutamine(i:list,p:list):
    """
    """
    nimi=input("Nimi: ")
    n=i.count(nimi)
    
    if n>0:
        for x in i:
            if x==nimi:
                ind=i.index(x)
                i.remove(x)
                p.pop(ind)
    return i,p






#3-Самую большую зарплату и кто ее получает,



def SuurimPalk(i:list,p:list):
    """
    """
    nimi_list=[]
    max_=max(p)
    a=0
    for palk in p:
        if palk==max_:
            ind=p.index(max_,a)
            nimi=i[ind]
            a+=1
            nimi_list.append(nimi)

    return max_, nimi_list





#4-Кто получает самую маленькую зарплату и какую именно,


def MinPalk(i:list,p:list):
    """
    """
    nimi_list=[]
    min_=min(p)
    a=0
    for palk in p:
        if palk==min_:
            ind=p.index(min_,a)
            nimi=i[ind]
            a+=1
            nimi_list.append(nimi)

    return min_, nimi_list



#5-Упорядочить зарплаты в порядке возрастания и убывания вместе с именами,


def Sort(i:list,p:list,a:int):
    """
    """
    N=len(i)
    if a==1:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]<p[m]:
                    kaust=p[n]
                    p[n]=p[m]
                    p[m]=kaust
                    kaust=i[n]
                    i[n]=i[m]
                    i[m]=kaust
    else:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]>p[m]:
                    kaust=p[n]
                    p[n]=p[m]
                    p[m]=kaust
                    kaust=i[n]
                    i[n]=i[m]
                    i[m]=kaust
        pass
    return i,p



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