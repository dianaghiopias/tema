a=2
b=3
c=5
lista_nr=[]
Lista_nr_prime=[]
n=int(input("Scrieti numarul de numere din lista:"))
for j in range (n):
    nr_lista = int(input("Dati numerele din lista: "))
    lista_nr.append(nr_lista)

for k in range(len(lista_nr)):
    if (lista_nr[k]==2):
        if lista_nr[k] not in Lista_nr_prime:
            Lista_nr_prime.append(lista_nr[k])
    if(lista_nr[k]==3):
        if lista_nr[k] not in Lista_nr_prime:
            Lista_nr_prime.append(lista_nr[k])
    if(lista_nr[k]==5):
        if lista_nr[k] not in Lista_nr_prime:
            Lista_nr_prime.append(lista_nr[k])

for i in range(len(lista_nr)):
    if(lista_nr[i]%a!=0 and lista_nr[i]%b!=0 and lista_nr[i]%c!=0 and lista_nr[i]!=0 and lista_nr[i]!=1):
        if lista_nr[i] not in Lista_nr_prime:
            Lista_nr_prime.append(lista_nr[i])


print("Lista nr:",lista_nr)
print("Lista nr prime: ",Lista_nr_prime)
print("Numarul  de numre prime din lista este de: ",len(Lista_nr_prime))