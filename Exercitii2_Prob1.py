n = int(input("Dati numarul n: "))
sirDeNumere = []
for j in range(n):
    sirDeNumere.append(int(input("Dati numarul: ")))
numereDivizibile = []
for i in range(1, len(sirDeNumere)):
    if sirDeNumere[i] % sirDeNumere[i - 1] == 0:
        numereDivizibile.append(sirDeNumere[i])
        numereDivizibile.append("se divide cu ")
        numereDivizibile.append(sirDeNumere[i - 1])

print(numereDivizibile)
