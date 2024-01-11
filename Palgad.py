from Funktcion import *


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("Lisamine-1")
    v=int(input())
    if v==1:
        k=int(input("Mitu inimest lisame? "))
        inimesed,palgad=Lisamine(inimesed, palgad,k)
        for i in range(len(palgad)):
            print(inimesed[i], "saab katte",palgad[i])

