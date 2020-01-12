lista_numere = []
nr1 = int(input("Introduceti numarul: "))
lista_numere.append(nr1)
ratia = 0


def progresie_aritmetica():
    global ratia
    ratia = lista_numere[1] - lista_numere[0]
    for i in range(2, len(lista_numere)):
        if lista_numere[i] == lista_numere[i - 1] + ratia:
            print("Exista progresie aritmetica")
        else:
            print("Nu exista progresie aritmetica")
            break


if lista_numere[0] != -1:
    while 1:
        numar = int(input("Intrduceti numarul: "))
        if numar == -1:
            print("Lista este: ", lista_numere)
            if len(lista_numere) >= 3:
                progresie_aritmetica()
            break
        lista_numere.append(numar)
else:
    print("Intrduceti un numar diferit de -1")
