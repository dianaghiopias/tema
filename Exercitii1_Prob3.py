while 1:
    numere_pare = []
    numere_impare = []
    produsul_nr_pare = 1
    suma_nr_impare = 0
    cod_securitate = int(input("Introduceti codul: "))
    lista_cod = list(str(cod_securitate))
    lista_int = []
    prima_cifra = 0
    if len(lista_cod) <= 9:
        # Urmatorul for converteste codul de tip string intr-o lista de tipul int
        for i in range(len(lista_cod)):
            lista_int.append(int(lista_cod[i]))
        for j in range(len(lista_int)):
            if lista_int[j] % 2 == 0:
                numere_pare.append(lista_int[j])
            elif lista_int[j] % 2 != 0:
                numere_impare.append((lista_int[j]))
        prima_cifra = lista_int[0]
        # Produsul numerelor pare:
        for k in range(len(numere_pare)):
            produsul_nr_pare = produsul_nr_pare * numere_pare[k]
        # Suma numerelor impare:
        for q in range(len(numere_impare)):
            suma_nr_impare = suma_nr_impare + numere_impare[q]
        #Verificare cod:
        if suma_nr_impare % prima_cifra != produsul_nr_pare % prima_cifra:
            print("Incorect")
        else:
            print("Corect")
            break
    else:
        print("Codul este prea lung (<=9)")
