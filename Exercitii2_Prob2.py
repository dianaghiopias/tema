contor = 0
contor_1 = 0
lista = (str(input("Scrie caracterele : ")))
print(lista)

if lista[0] == '}':
    print(" Sir gresit ")
    lista = (str(input("Scrie caracterele : ")))

for i in range(0, len(lista)):
    if lista[i] == '{':
        contor += 1
    if lista[i] == '}':
        contor_1 += 1

print(" { deschise = ", contor, "si } inchise = ", contor_1)
if contor_1 == contor:
    print(" Sir corect ")
else:
    print("Sirul este gresit")
