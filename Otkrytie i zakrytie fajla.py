def Loe_failist(fail: str)-> list:
    jarjend=[]
    f=open(fail, 'r', encoding="UTF-8-sig")
    for rida in f:
        jarjend.append(rida.strip()) # разделитель может быть любым в кавычках
    f.close()
    return jarjend




def Kirjuta_failisse(fail: str, jarjend: list):
    f=open(fail, 'w', encoding="UTF-8-sig")
    for item in jarjend:
        f.write(item+"\n")
    f.close()
    
paevad=Loe_failist("TextFile1.txt")
print(paevad)

list_=[]
for i in range(5):
    nimi=input(str(i+1)+'.Nimi')
    list_.append(nimi)
Kirjuta_failisse("Nimed.txt", list_)

with open('Nimed.txt', 'r') as f:
    print(f.read())
    
