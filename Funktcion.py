

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
def zarplataravna(i:list,p:list):
    """
    """
    nimi_list=[]
    palk_list=[]
    for n in range(len(p)):
        if p[n] not in palk_list:
            palk_list.append(p[n])
            nimi_list.append(i[n])
        else:
            ind=palk_list.index(p[n])
            nimi_list[ind]=nimi_list[ind]+", "+i[n]
    return nimi_list,palk_list


#7-Сделать поиск зарплаты по имени человека. Учесть, что имена могут повторяться,
def otsing(i:list,p:list):
    """
    """
    nimi=input("Nimi: ")
    nimi_list=[]
    palk_list=[]
    for n in range(len(i)):
        if i[n]==nimi:
            nimi_list.append(i[n])
            palk_list.append(p[n])
    return nimi_list,palk_list

#8-Вывести список тех людей(с зарплатами), кто получает больше/меньше чем указанная сумма.
def suurempalk(i:list,p:list):
    """
    """
    nimi_list=[]
    palk_list=[]
    palk=int(input("Palk: "))
    for n in range(len(p)):
        if p[n]>palk:
            nimi_list.append(i[n])
            palk_list.append(p[n])
    return nimi_list,palk_list


#9-Top() - Т самых бедных и самых богатых человека
def top(i:list,p:list):
    """
    """
    n=int(input("N: "))
    nimi_list=[]
    palk_list=[]
    for x in range(n):
        min_=min(p)
        ind=p.index(min_)
        nimi_list.append(i[ind])
        palk_list.append(p[ind])
        p.pop(ind)
        i.pop(ind)
    return nimi_list,palk_list


#10-Keskmine() - Среднюю зарплату и имя человека ее получающего
def keskmine(i:list,p:list):
    """
    """
    summa=0
    for x in p:
        summa+=x
    kesk=summa/len(p)
    nimi_list=[]
    palk_list=[]
    for n in range(len(p)):
        if p[n]==kesk:
            nimi_list.append(i[n])
            palk_list.append(p[n])
    return nimi_list,palk_list


#11-Tulumaks() - Вычислить зарплату, которую человек получит на руки после вычисления подоходного налога.
#tulud
#link
#pangakalkulaator
def tulumaks(i:list,p:list):
    """
    """
    nimi_list=[]
    palk_list=[]
    for n in range(len(p)):
        if p[n]<=1200:
            palk_list.append(p[n])
            nimi_list.append(i[n])
        elif p[n]>1200 and p[n]<=2100:
            palk_list.append(p[n]*0.8)
            nimi_list.append(i[n])
        elif p[n]>2100 and p[n]<=5000:
            palk_list.append(p[n]*0.75)
            nimi_list.append(i[n])
        elif p[n]>5000:
            palk_list.append(p[n]*0.7)
            nimi_list.append(i[n])
    return nimi_list,palk_list


#12- Осуществить сортировку по имени (можно предостваит пользователю выбор от А до Я или от Я до А)
def sort_nimi(i:list,p:list):
    """
    """
    N=len(i)
    for n in range(0,N):
        for m in range(n,N):
            if i[n]>i[m]:
                kaust=i[n]
                i[n]=i[m]
                i[m]=kaust
                kaust=p[n]
                p[n]=p[m]
                p[m]=kaust
    return i,p


#13- Находить тех кто получает зарплату ниже средней и удалить их из списков.
def keskmine(i:list,p:list):
    """
    """
    summa=0
    for x in p:
        summa+=x
    kesk=summa/len(p)
    nimi_list=[]
    palk_list=[]
    for n in range(len(p)):
        if p[n]<kesk:
            nimi_list.append(i[n])
            palk_list.append(p[n])
    return nimi_list,palk_list


#14- Отредактировать списки таким образом, чтоб в списке людей имена были написаны с большой буквы, о зарплаты в формате int.
def redakt(i:list,p:list):
    """
    """
    for n in range(len(i)):
        i[n]=i[n].capitalize()
        p[n]=int(p[n])
    return i,p


#15 - Каждый год работникам фирмы поднимают зарплату на 5%, узнай какой будут зарплаты/зарплата у опрделенного работника через Т лет.
def tulevik(i:list,p:list):
    """
    """
    aasta=int(input("Aasta: "))
    nimi=input("Nimi: ")
    ind=i.index(nimi)
    for x in range(aasta):
        p[ind]=p[ind]*1.05
    return i,p


#16 - "Переименовать" каждого третьего человека. Новые имена вводит пользователь.
def uus_nimi(i:list,p:list):
    """
    """
    uus_nimi=input("Uus nimi: ")
    for n in range(2,len(i),3):
        i[n]=uus_nimi
    return i,p


#17 - Написать функцию для редактирования данных. Пользователь выбирает, что редактировать: имя или зарплату. Измененние данные сохраняются  в список.
def redakt(i:list,p:list):
    """
    """
    v=int(input("Nimi-1, Palk-2: "))
    if v==1:
        nimi=input("Nimi: ")
        uus_nimi=input("Uus nimi: ")
        for n in range(len(i)):
            if i[n]==nimi:
                i[n]=uus_nimi
    elif v==2:
        nimi=input("Nimi: ")
        uus_palk=int(input("Uus palk: "))
        for n in range(len(i)):
            if i[n]==nimi:
                p[n]=uus_palk
    return i,p


#18 -  Найти имена начинающиеся на введенную букву и их зарплаты. Отобразить данные в столбик (Имя-зарплата)
def otsing(i:list,p:list):
    """
    """
    nimi=input("Nimi: ")
    nimi_list=[]
    palk_list=[]
    for n in range(len(i)):
        if i[n]==nimi:
            nimi_list.append(i[n])
            palk_list.append(p[n])
    return nimi_list,palk_list



#19-Придумай свою функцию
def funktsioon(i:list,p:list):
    """
    """
    nimi_list=[]
    palk_list=[]
    for n in range(len(p)):
        if p[n]<=1200:
            palk_list.append(p[n])
            nimi_list.append(i[n])
        elif p[n]>1200 and p[n]<=2100:
            palk_list.append(p[n]*0.8)
            nimi_list.append(i[n])
        elif p[n]>2100 and p[n]<=5000:
            palk_list.append(p[n]*0.75)
            nimi_list.append(i[n])
        elif p[n]>5000:
            palk_list.append(p[n]*0.7)
            nimi_list.append(i[n])
    return nimi_list,palk_list