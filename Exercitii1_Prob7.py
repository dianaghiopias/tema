from math import sqrt

l1=int(input("Prima latura este :"))
l2=int(input("A doua latura este : "))
l3=int(input("A treia latura este : "))
h=1
print("Laturile sunt : ",l1,',',l2,',',l3,'\n')

p = (l1 + l2 + l3)/2   # semiperimetrul
arie = sqrt(p * (p - l1) * (p - l2) * (p - l3))  # aria
print("Semiperimetrul este ", p)
print("Aria este ",arie)

h1=(2*arie)/l1
h2=(2*arie)/l2
h3=(2*arie)/l3

print("Inaltimea 1 este ",h1)
print("Inaltimea 2 este ",h2)
print("Inaltimea 3 este ",h3)

if(l1==l2==l3):
    print("Echilateral")
elif(l1==l2 or l2==l3 or l3==l1):
    print("Isoscel")
elif(l1>l2 and l1>l3 and l1*l1==l2*l2+l3*l3):
    print("Dreptunghic")
elif(l2>l1 and l2>l3 and l2*l2==l1*l1+l3*l3):
    print("Dreptunghic")
elif(l3>l2 and l3>l1 and l3*l3==l2*l2+l1*l1):
    print("Dreptunghic")
else:
    print("OARECARE")
