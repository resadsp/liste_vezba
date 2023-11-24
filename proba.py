#prvi zadatak
ceo = int(input("Unesite neki ceo broj: "))
kvadrat = ceo ** 2
kub = ceo ** 3
binarni = bin(ceo)
heksa = hex(ceo)
print("{0:^10} -> {0:^10} dati broj".format(ceo))
print("{0:^10} -> {1:^10} kvadrat unetog broja".format(ceo,kvadrat))
print("{0:^10} -> {1:^10} kub unetog broja".format(ceo,kub))
print("{0:^10} -> {1:^10} binarni zapis unetog broja".format(ceo,binarni))
print("{0:^10} -> {1:^10} heksadecimalni zapis unetog broja".format(ceo,heksa))

#drugi zadatak
a = int(input("Unesite prvi ceo broj: "))
b = int(input("Unesite drugi ceo broj: "))
zbir = a + b
razlika = a - b
proizvod = a * b
kolicnik = a / b
prnadr = a ** b
drnapr = b ** a
print("{0:^4} + {1:^4} = {2:^4}".format(a,b,zbir))
print("{0:^4} - {1:^4} = {2:^4}".format(a,b,razlika))
print("{0:^4} * {1:^4} = {2:^4}".format(a,b,proizvod))
print("{0:^4} / {1:^4} = {2:^4}".format(a,b,kolicnik))
print("{0:^4} na {1:^4} = {2:^4}".format(a,b,prnadr))
print("{1:^4} na {0:^4} = {2:^4}".format(a,b,drnapr))



