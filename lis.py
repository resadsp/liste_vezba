n = int(input("Koliko zelite clanova liste: "))
l1 = []
l2 = []
l3 = []
for x in range(n):
    a = int(input("Unesite stavku liste: "))
    l1.append(a)
print("Lista koju ste uneli je:",l1)

for x in l1:
    if x%2 == 0:
        l2.append(x)
    else:
        l3.append(x)
print("Parni brojevi su: ",l2)
print("Neparni brojevi su:",l3)
maximum = l1[0]
for x in l1:
    if x>maximum:
        maximum = x
print("MAX JE: ",maximum)
minimum = l1[0]
for x in l1:
    if x<minimum:
        minimum = x
print("Minimum je:",minimum)
l1.sort()
print("Sortirani od manjeg ka vecem:",l1)
print("Minimalni element je:",l1[0])
l1.sort(reverse=True)
print("Sortirani od veceg ka manjem:",l1)
print("Maximalni element je:",l1[0])    
l4 = []
while True:
    a = input("Unesite stavku liste ili unesite q za prekid: ").lower()
    if a == "q":
        break
    else:
        l4.append(a)
print(l4)
stavka = l4.pop(0)
print("Prva stavka koju izbacujemo:",stavka)
print("Lista bez prve stavke:",l4)

niz = [45,7,6,8,1,23,88,101,88,89,88]
d = len(niz)
e = niz.count(88)
for i in range(0,d-1):
    for j in range(i+1, d):
        if niz[i]>niz[j]:
            a = niz[i]
            niz[i] = niz[j]
            niz[j] = a
print(niz)
niz.sort(reverse=True)
print(niz)
print(e)