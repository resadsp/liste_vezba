#liste
#uredjena, promenljiva i dozvoljava duple clanove
lista_num = [1,2,3,4,5,6,7]
lista_str = ["neka", "lista", "sa", "nekim", "clanovima"]
lista_bool = [True, False]
lista_kombinovana = [10, "rec", False, 10+2j, 3.52]
print(type(lista_num))
print(type(lista_str))
print(type(lista_bool))
print(type(lista_kombinovana))

duzina = int(input("Unesite koliko clanova ce imati vasa lista: "))
l1 = []
for x in range(duzina):
    print(x+1,"clan niza:")
    l1.append(input())
print(l1)

l2 = [13, 15, "24", 18, 26, 15, 13, 11]
print(l2)
l3 = []
l4 = []
for x in l2:
    if int(x)%2==0:
        l3.append(x)
    else: 
        l4.append(x)
print("PARNI BROJEVI SU: ",l3)
print("NEPARNI BROJEVI SU: ",l4)
l5 = []
l6 = []
print("------------------------------------------")
#drugi nacin
for x in l2:
    if not int(x)%2 == 0:
        l5.append(x)
    else:
        l6.append(x)
print("NEPARNI BROJEVI SU: ",l5)
print("PARNI BROJEVI SU: ",l6)

l7 = ["kako", "si", "ti", "sta", "radis"]
print(l7)
for x in l7:
    if x == "ti":
        l7.remove("ti")
print(l7)

l8 = [45,52,56,745,89,75,45,6,12,5]
for x in range(0,len(l8)):
    print(l8[x])

l9 = []
while True:
    a = input("Dodajte clan niza ili pritisnite q za prekid unosa: ")
    if a == "q":
        break
    else:
        l9.append(a)
print(l9)

c = l7.pop(0)
print(c)
print(l7)

l9 = [1,45,65,45,66,45,12,3,45]
print(l9)
l9.remove(45)
print(l9)
for x in l9:
    if x == 45:
        l9.remove(x)
print(l9)

l10 = [45,56,98,45,61,21,45,98]
maximum = l10[0]
for x in l10:
    if x>maximum:
        maximum = x
print(maximum)
minimum = l10[0]
for x in l10:
    if x<minimum:
        minimum = x
print(minimum)

#sortiranje niza
l10 = [45,56,98,45,61,21,45,98]
l10.sort()
print(l10)
l10.sort(reverse=True)
print(l10)

l11 = ["da", "asdasd", "Usdasd", "fsdsd", "Lasdas"]
l11.sort()
print(l11)
l11.sort(key=str.lower)
print(l11)
