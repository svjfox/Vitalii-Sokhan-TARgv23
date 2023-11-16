from base64 import b16decode
from ctypes.wintypes import FLOAT
from math import *
from tkinter import ROUND
from xml.etree.ElementTree import PI # mat biblioteka
from random import *



#print("Tere tulemast!".center(50))
#kool=input("Mis koolis sa õpid: ") #str kool
#kursus=int(input("\tMis kursusel: ")) #int kursus
#print("Tere tulemast kooli "+kool.upper()+"!\n0le hea"+str(kursus)+".kursuse õpilaseks!") #kool="TTHK"

#print("Tere tulemast kooli",kool.lower(),"!\n0le hea" ,kursus,".kuursuse õpilaseks!") #kool="tthk"

#print("Tere tulemast kooli {0}!\n0le hea {1}.kuursuse õpetajaks!".format(kool,kursus)) #kool="Ttkk"
#print(type(kool))
#print(type(kursus))

#ar1=float(input("Arv 1: "))
#ar2=float(input("Arv 2: "))


#print("Summa {0} ja {1} = {2}".format(ar1,ar2,ar1+ar2)) #summa
#print("{0} - {1} = {2}".format(ar1,ar2,ar1-ar2)) #minus
#print("{0} * {1} = {2}".format(ar1,ar2,ar1*ar2)) #umnozhenie
#print("{0} / {1} = {2}".format(ar1,ar2,ar1/ar2)) #delenie
#print("{0} astmes {1} = {2}".format(ar1,ar2,ar1**ar2)) #stepen
#print("{0} ja {1} jaak= {2}".format(ar1,ar2,ar1%ar2)) #procent
#print("{0} ja {1} jagamise tais osa = {2}".format(ar1,ar2,ar1//ar2)) #

##1

#print("Privet mir!")
#name=input("Kak tebja zovut: ")
#print("Privet " + name)
#vozrast=input("Skolko tebe let: ")
#print("Privet mir! "+"Privet "+ name +". "+"Tebe "+vozrast+" let!" )



##2

#vanus = 18 #type(vanus)-> int
#eesnimi = "Jaak" #str
#pikkus = 16.5 #float
#kas_käib_koolis = True #bool

###3

#kon=int(input("Skolko konfet na stole: "))
#print("Konfet na stole: ", kon)
#kon2=int(input("Skolko ty hochesh zabrat: "))
#V=kon-kon2
#print("Na stole ostalos: ",V )


##4

#C=float(input("Dlina okruzhnosti: ")) #C=2*pi*r=pi*d
#d=round(C/pi,2)
#print("Dlina okruzhnosti: ",d)
#print("Dlina okruzhnosti: {0}".format(round(d,2)))

#5

#N=float(input("Dlina "))
#M=float(input("Shyrina "))
#D=sqrt(N**2+M**2)
#D1=hypot(N,M)
#print("D=",D)
#print("D1=",D1)

#6

#aeg = float(input("Mitu tundi kulus sõiduks? "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus = teepikkus / aeg
#print("Sinu kiirus oli " + str(kiirus) + " km/h")
#try:
#    aeg = float(input("Mitu tundi kulus sõiduks? "))
#    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#    kiirus = teepikkus / aeg
#    print("Sinu kiirus oli " + str(kiirus) + " km/h")
#except :
    #print("Andmetuubi viga!")


#7

#a=int(input("A= "))
#b=int(input("B= "))
#c=int(input("C= "))
#d=int(input("D= "))
#i=int(input("I= "))
#S=(a+b+c+d+i) / 5
#print("Sredneje arifm ",S)


#a1=randint(1,10)
#a2=randint(1,10)
#a3=randint(1,10)
#a4=randint(1,10)
#a5=randint(1,10)
#print("Arvude {0},{1},{2},{3} ja {4} aritmeetiline keskmine on {5}".format(a1,a2,a3,a4,a5(a1+a2+a3+a4+a5)/5))

#8


#print("    @..@")
#print("   (----)")
#print("  ( \__/ )")
#print("  ^^ '' ^^") 

#9

#a=int(input("a= "))
#b=int(input("b= "))
#c=int(input("c= "))
#P=a+b+c
#print("P=a+b+c=",a,"+",b,"+",c,"=",P)

#10

#a=float(12.90) #cena
#b=float(0.1) #10%
#c=a*b
#S=round((a+c)/2,2)
#print("Kazhdyi drug dolzhen zaplatit ",S)
