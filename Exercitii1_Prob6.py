numar = int(input("Dati numarul: "))
copie_numar = numar
if numar == 2 or numar == 4:
    print("Nu exista")
elif numar % 2 != 0:
    print(numar // 2, " + ", numar // 2 + 1)
else:
    print(numar // 2 - 1, " + ", numar // 2 + 1, " = ", numar)
