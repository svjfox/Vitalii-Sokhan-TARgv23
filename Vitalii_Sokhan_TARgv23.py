from sre_constants import IN


print("Tere tulemast!")
kool=input("Mis koolis sa õpid: ") #str kool
kursus=int(input("Mis kursusel: ")) #int kursus
print("Tere tulemast kooli "+kool+"!\n0le hea "+str(kursus)+".kursuse õpilaseks!")
print("Tere tulemast kooli",kool,"!\n0le hea",kursus,".kuursuse õpilaseks!")
print("Tere tulemast kooli {0}!\n0le hea {1}.kuursuse õpetajaks!".format(kool,kursus))

