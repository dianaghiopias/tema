from math import *

raza_cerc=int(input("Scrieti raza cercului: "))
numar_perechi=int(input("Scrieti un nr de perechi: "))
for i in range (numar_perechi):
    latura=sqrt(raza_cerc**2+raza_cerc**2)
    #raza_cerc=latura/2
    print("Raza cerc: ",raza_cerc)
    raza_cerc = latura / 2
    print("Latura patat: ",latura)
