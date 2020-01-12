lungime_saritura = int(input("Dati lungimea sariturii a iepurasului: "))
nr_secunde = int(input("Dati durata saltului inainte ca iepurele sa oboseasca: "))
durata_totala = int(input("Dati durata totala a deplasarii iepurasului: "))
distanta = lungime_saritura

for i in range(nr_secunde, durata_totala, nr_secunde):
    distanta = distanta + lungime_saritura / 2
    lungime_saritura = lungime_saritura / 2
print(distanta)
