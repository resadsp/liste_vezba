import math
import random
korsinik = "RESAD"
radnja = "programira"
sat = 4
kafa = "srednji esspreso"
print("{3} voli da {2} i on to radi {1} dnevno. i uz to sve pije {0} kafu. On ukupno popije {1} kafe".format(kafa, sat, radnja, korsinik))
print("Ja se zovem {0}".format(korsinik))
a = 10
b = 12
c = 15
d = 16
print("{0} je u binarnom kodu {0:b}, {1} je u heksadecimalnom kodu {1:x}, {2} je u oktalnom formatu {2:o}, {3} je u dekadnom formatu {3:d}".format(a,b,c,d))
e = 3.456
f = 5.234
e = math.ceil(e) #gornja vrijednost
print(e)
f = math.floor(f) # donja vrijednost
print(f)
print("Veci od brojeva {0} i {1} je broj {2}".format(e,f,max(e,f)))
poruka = "Ja se zovem Resad Spahovic, ozenjen sam i otac sam jedne cerkice."
velikaslova = poruka.upper()
malaslova = poruka.lower()
print("Poruka koja glasi {0} napisana velikim slovima je {2} a napisana malim slovima je {1}".format(poruka, malaslova, velikaslova))
if poruka.startswith("Ja"):
    print("Poruka pocinje sa kljucnom recju Ja")
if poruka.endswith("."):
    print("Poruka zavrsava sa tackom")
print(poruka.startswith("Ja")) #vraca true ako je tacno, tj ako pocinje sa datim recju
print(poruka.endswith(".")) #vraca true ako je tacno, false ako je netacno
print(poruka.find("ozenjen")) # vraca pozciju pocetka date reci ako postoji. vraca -1 ako rec ne postoji. ako se stavi u if uvek ce davati tacan rezultat.
rec = "Individual"
print(rec[1:4]) #pocinje od nulte pozicije. prva stavka uvek ukljucena krajanja nije
print(rec[2:]) #stampa od date pozicije pa do kraja
print(rec[:6]) #stampa od pocetka pa do date pozicije. 6 nije ukljuceno
print(rec[1:7:2]) #stampa sa korakom 2 ili koliko vec korsnik zeli
print(rec[::2]) #od pocetka do kraja sa korakom 2 ili koliko korisnik zeli
print(rec[::-1]) #stampa od pocetka do kraja ali obrnutim redosledom laudividnI
ime = input("Unesite vase ime: ")
prezime = input("Unesite vase prezime: ")
zanimanje = input("Unesite vaas zanimanje: ")
grad = input("Unesite vas grad: ")
m = random.randrange(2,len(ime))
n = random.randrange(2,len(prezime))
k = random.randrange(2, len(zanimanje))
o = random.randrange(2,len(grad))
novoime = ime[0:m] + prezime[0:n]
novoprezime = zanimanje[0:k] + grad[0:o]
print("Uzeli smo od imena",m,"slova.")
print("Uzeli smo od prezimena",n,"slova")
print("Uzeli smo od zanimanja",k,"slova")
print("Uzeli smo od grada",o,"slova.")
print("Moje novo ime je {} a moje novo prezime je {}.".format(novoime.capitalize(), novoprezime.capitalize()))

print(ime.find("ad")) #ne vraca true ili false. vraca -1 ako rijec ne postoji a poziciju prvog slova ako rijec postoji

"""
Tekst udesno: {indeks:>ukupan_broj_karaktera}
• Tekst ulevo: {indeks:<ukupan_broj_karaktera}
• Tekst centar: {indeks:^ukupan_broj_karaktera}
• Tekst ulevo sa popunjavanjem preostalog prostora karakterom #:
{indeks:#<ukupan_broj_karaktera}
• Prikaz broja decimalno: {indeks:d}
• Prikaz broja binarno: {indeks:b}
• Prikaz broja oktalno: {indeks:o}
• Prikaz broja heksadecimalno: {indeks:x}
• Prikaz realnog broja sa dve decimale: {indeks:.2f}
"""


        