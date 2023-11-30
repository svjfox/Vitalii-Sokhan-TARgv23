from xml.etree.ElementTree import PI


for x in range(1,11):
    R=float(input("{0}.R: ".format(x)))
    if R>0:
        S=PI*R**2
    else:        
        S='R peab > kui 0 olema'
    print("S=(0)".format(S))
        