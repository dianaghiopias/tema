numar_borne = int(input("Dati nr de borne: "))
altitudinea_borne = []
distanta_fata_de_borna_precedenta = []
distanta_actuala = 0
distanta_totala = 0
print("Borna 0 are altitudinea initiala 0")

# Citirea datelor(altitudinea bornelor si ditantele):
for i in range(0, numar_borne):
    altitudinea_borne.append(int(input("Dati altitudinea de la borna {}: ".format(i))))
    distanta_fata_de_borna_precedenta.append(int(input("Dati distanța față de borna precedentă {}: ".format(i))))

# Functii de verificare:
for i in range(0, numar_borne - 1):
    if altitudinea_borne[i] < altitudinea_borne[i + 1]:
        distanta_actuala += distanta_fata_de_borna_precedenta[i + 1]
    else:
        distanta_actuala = 0
    if distanta_actuala > distanta_totala:
        distanta_totala = distanta_actuala

print("Sectiunea cea mai lunga este: ",distanta_totala)
