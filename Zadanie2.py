# Задача 

# В программе должны выполняться ниже следующие действия:

#             вывод на экран приветствия "Tere! Olen sinu uus sõber - Python!"
#             присваивание переменной nimi введённого пользователем имени
#             вывод на экран текста: nimi ", oi kui ilus nimi!" 
#             вывод на экран текста: nimi  "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "

#             если ответ равен единице:

#             присваивание переменной pikkus целого значения переменной введенной пользователем
#             присваивание переменной mass значения выражения в формате действительного числа
#             присваивание переменной indeks значения выражения mass /(0.01pikkus)2
#             вывод на экран имени, объединённого с текстом "! Sinu keha indeks on:" indeks с одним знаком после запятой
#             вывод оценки индекса массы тела в соответствии с таблицей ниже:

#                  Vastus	                                       Index
# Tervisele ohtlik alakaal	      < 16
# Alakaal	                     16 - 19
# Normaalkaal	                 19 - 25
# Ülekaal	                     25 - 30
# Rasvumine	                     30 - 35
# Tugev rasvumine	             35 - 40
# Tervisele ohtlik rasvumine     > 40

#             в противном случае (else):

#             вывод на экран текста "Kahju! See on väga kasulik info!"
#             вывод на экран пустой строки

# вывод на экран текста "Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!"

# Обязательна проверка введенных пользователем ответов!

#   try:
#    a=float(input("A "))
#   except:
#    ValueError


print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sisesta oma nimi: ")
print(nimi+", oi kui ilus nimi!")
vastus=int(input(nimi+"! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    
if vastus == 1:
        try:
            pikkus = int(input("Sisesta oma pikkus (cm): "))
            mass = float(input("Sisesta oma kaal (kg): "))
            
            indeks=round(mass/(0.01*pikkus)**2,2)
            print(f'{nimi}! Sinu keha indeks on: {indeks}')
            
            print("Hinnang indeksile:")
            if indeks < 16:
                print("Tervisele ohtlik alakaal")
            elif 16 <= indeks < 19:
                print("Alakaal")
            elif 19 <= indeks < 25:
                print("Normaalkaal")
            elif 25 <= indeks < 30:
                print("Ülekaal")
            elif 30 <= indeks < 35:
                print("Rasvumine")
            elif 35 <= indeks < 40:
                print("Tugev rasvumine")
            else:
                print("Tervisele ohtlik rasvumine")
            
        except ValueError:
            print("Vigane sisend!")
            
else:
    print("Kahju! See on väga kasulik info!")
       
print()
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

