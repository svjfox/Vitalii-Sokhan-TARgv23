from ctypes.wintypes import FLOAT


print("Tere tulemast!".center(50))
kool=input("Mis koolis sa õpid: ") #str kool
kursus=int(input("\tMis kursusel: ")) #int kursus
print("Tere tulemast kooli "+kool.upper()+"!\n0le hea"+str(kursus)+".kursuse õpilaseks!") #kool="TTHK"

print("Tere tulemast kooli",kool.lower(),"!\n0le hea" ,kursus,".kuursuse õpilaseks!") #kool="tthk"

print("Tere tulemast kooli {0}!\n0le hea {1}.kuursuse õpetajaks!".format(kool,kursus)) #kool="Ttkk"
print(type(kool))
print(type(kursus))

ar1=float(input("Arv 1: "))
ar2=float(input("Arv 2: "))


print("Summa {0} ja {1} = {2}".format(arv1,arv2,arv1+arv2)) #summa
print("{0} - {1} = {2}".format(arv1,arv2,arv1-arv2)) #minus
print("{0} * {1} = {2}".format(arv1,arv2,arv1*arv2)) #umnozhenie
print("{0} / {1} = {2}".format(arv1,arv2,arv1/arv2)) #delenie
print("{0} astmes {1} = {2}".format(arv1,arv2,arv1**arv2)) #stepen
print("{0} ja {1} jaak= {2}".format(arv1,arv2,arv1%arv2)) #procent
print("{0} ja {1} jagamise tais osa = {2}".format(arv1,arv2,arv1//arv2)) #