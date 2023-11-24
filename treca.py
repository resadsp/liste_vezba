#korisnik unosi tekst a mi brojimo odredjeno slovo.
tekst = input("UNESITE TEKST ZA KOJI ZELITE DA PREBROJIMO DATO SLOVO: ")
slovo = input("UNESITE SLOVO KOJE ZELITE DA PREBROJITE: ")
brojac = 0
for x in tekst:
    if x == slovo:
        brojac +=1
print("U tekstu koji ste uneli, slovo",slovo,"se pojavljuje",brojac,"puta.")
razmak = 0
for x in tekst:
    if x == " ":
        razmak +=1
print("U tekstu se razmak pojavljuje",razmak,"puta.")
print("Tekst ima",len(tekst)-razmak,"karaktera.")
if "kako" in tekst or "Kako" in tekst or "KAKO" in tekst:
    print("Korisnik je uneo rec kako u tesktu.")
else:
    print("Ne postoji rec kako u tekstu.")
    
if len(tekst) > 10:
    print("Tekst je duzi.")
else:
    print("Tekst je kraci.")
    
a = input("Unesite neki visecifreni broj: ")
print("Normalan ispis:",a)
print("Obrnuti ispis:",a[::-1])
s = "" #da pamti cifre kao stringove
for i in range(-1,-len(a)-1,-1):
    s += a[i]
print("Ovrnuti ispis:",s)
e = ""
novi_tekst = input("Unesite neki tekst: ")
for x in range(0,len(novi_tekst),1):
    if novi_tekst[x] == "a":
        e = e + str(x) +","
print(e)
