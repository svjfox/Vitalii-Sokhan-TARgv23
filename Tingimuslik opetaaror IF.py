# 1 Если имя Juku, то пойдем с Juku в кино.
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


#A=float(input("Kakaja dlinna 1 steny? "))
#B=float(input("Kakaja dlinna 2 steny? "))
#S=A*B
#print("Ploshad pola =",S)
#remont=input("Ty hochesh sdelat remont pola? ")
#if remont=="da" or remont=="yes":
#    cena=float(input("Skolko stoit remont za metr kv? "))
#    summa=S*cena
#    print("Stoimost remonta budet",summa)
#else:
#    print("Ok, togda remont pola ne delaem")


# 4 Найдите цену со скидкой 30%, если первоначальная цена больше 700

#cena=int(700)
#skidka=700-700*0.3
#print("Pri cene v 700 i skidke 30% stoimost budet ",skidka)

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

#r=float(input("Kakoj u tebja rost? "))
#if 60<r<120:
#    if 60<r<76:
#        print("Ty nizkij.")
#    elif 75<r<91:
#        print("Ty srednij")
#    elif 90<r<120:
#        if 90<r<101:
#            print("Ty vysokij")
#        elif 100<r<120:
#            print("Ty ochen vysokij")
    
#else:
#    print("Rost ne vernyj")



