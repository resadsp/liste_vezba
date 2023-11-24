import random
import math
broj = input("Unesite neki visecifreni broj: ") #njegov tip je po automatizmu string
#ispis cifara broja
for x in range(0,len(broj),1): #x je int jer je brojac
    print(x+1,"cifra je",broj[x])
#ispis od kraja do pocetka
print("Obrnuti redosled cifara broja",broj,"galsi",broj[::-1],", prvi nacin") #prvi nacin
s = "" #treba nam kao string da pamti cifre
for x in range(-1,-len(broj)-1,-1): #mora -len()-1 jer se zadnji karakter nije ukljucen po automatizmu
    s += broj[x]
print("Obrnuti redosled cifara broja",broj,"glasi",s,", drugi nacin") #drugi nacin
#zbir cifara visecifrenog broja
suma = 0
for x in range(0,len(broj),1):
    suma = suma + int(broj[x])
print("Suma cifara broja",broj,"je",suma)
sort = ""
x=[i for broj,i in enumerate(broj) ] #pravimo niz od cifara unetog broja
print("Niz sastavljen od cifara broja",broj,"glasi",x)
x.sort() #sortiramo niz
l = ""
for i in range(0,len(broj),1):
    l = l + x[i]
print("Cifre broja",broj,"sortirane od najmanje do najvece glase:",l)
m = input("Unesite broj za koji zelite da saznate pozicije u visecifrenom broju: ")
pozicija = "" #mora str jer necemo sabiranje int nego pamcenje cifara
for x in range(0,len(broj),1):
    if broj[x] == m:
        pozicija = pozicija + str(x) + "," #mora str jer je x brojac pa je int
if len(pozicija)>0:
    print("Broj",m,"se u broju",broj,"nalazi na pozicijama",pozicija,"definisano.")
else:
    print("Broj",m,"se ne nalazi u cifri",broj)
ime = input("unesite vase ime: ")
prezime = input("unesite vase prezime: ")
godina_rodjenja = input("unesite godinu vaseg rodjenja: ")
godina_skolovanja = input("unesite godinu pocetka vaseg skolovanja: ")
godina_rodjenja = int(godina_rodjenja)
godina_skolovanja = int(godina_skolovanja)
godina = godina_skolovanja - godina_rodjenja
print("moje ime je {0:^10} a prezime {1:^10}, rodjen sam {2:^6} godine, fakultet sam upisao {3:>6} godine. dakle, imao sam {4:<6} godina kada sam upisao fakultet.".format(ime.capitalize(),prezime.capitalize(),godina_rodjenja,godina_skolovanja,godina))
a = random.randrange(2,len(ime))
b = random.randrange(2,len(prezime))
novo_ime = ime[0:a] + prezime[0:b]
print("Novo ime sacinjeno od",a,"karaktera imena",ime.capitalize(),"i",b,"karaktera prezimena",prezime.capitalize(),"glasi",novo_ime.capitalize())
a = input("Unesite neki broj: ")
suma = 0
for i in range(0,len(a),1):
    print(i+1,"cifra je",a[i])
for x in range(0,len(a),1):
    suma += int(a[x])
print("suma cifara je",suma)
obrnuti = ""
for x in range(-1, -len(a)-1,-1):
    obrnuti += a[x]
print("obrnuti redosled je",obrnuti)
print("obrnuti redosled je",a[::-1])
for x in a:
    if x == "3":
        continue
    print(x) #ukoliko ne zelimo da stampamo 3
print("")          
for x in a:
    print(x) #ukoliko zelimo da stampamo 3
    if x == "3":
        break 
i = 0
while i<10:
    print("ja volim maidu i atiju")
    i+= 1
    if i==5:
        break
else:
    print("vole i one mene") #ne izvrsava se je je break u while petlji. Da je continue umesto breake, else bi se izvrsilo
sum = 0
duzina = input("Unesite ukupan broj brojeva za koje zelite da racunate aritmeticku sredinu: ")
for x in range(0,int(duzina)): #sad nam treba kao int a ne kao string koji nam je trebao u gornjim slucajevima
  ad = int(input("broj je: "))
  sum += ad
print("Aritmeticka sredina je {0:.2f}".format(sum/int(duzina))) #dvije cifre iza zareza
#da li je uneti broj deljiv sa 7:
br = int(input("Uesite zeljeni broj za koji ispitujete deljivost sa brojem 7: "))
if br % 7 == 0:
    print(br,"je deljivo sa 7.")
else:
    print(br,"nije deljiv sa 7.")    
#da li je uneti broj pozitivan ili negativan
if br>0:
    print("Uneti broj je pozitivan.")
elif br == 0:
    print("Uneti broj je jednak nuli.")
else:
    print("Uneti broj je negativan.")
#ispistujemo da li je u pitanju trougao, ako jeste da li je jednakokraki, jednakostranican, raznostranican
a = int(input("Unesite stranicu a: "))
b = int(input("Unesite stranicu b: "))
c = int(input("Unesite stranicu c: "))
if a+b>c and a+c>b and b+c>a:
    print("Unete stranice jesu stranice trougla.")
    if a == b or a == c or c == b:
        print("Jednakokraki trougao.")
    if a == b and b == c:
        print("Jednakostranicni trougao.")
    if a != b  and b!= c and a!=c:
        print("Raznovrsni trougao.")
else:
    print("Date stranice ne mogu biti stranice trougla.")   
p = int(input("Unesite broj bodova: "))
if p in range(0,100):
    if p <= 50:
        print("NEDOVOLJAN")
    elif p<=63:
        print("DOVOLJAN")
    elif p<=76:
        print("DOBAR")
    elif p<=89:
        print("VRLO DOBAR")
    elif p<=100:
        print("ODLICAN")
else:
    print("Broj bodova mora biti u opsegu od 0 do 100")

p = 71
if p < 50:
    print("NEDOVOLJAN")
elif p<60:  #if p>50 and p<60
    print("DOVOLJAN")
elif p<70: #znam da je p vece od 70
    print("DOBAR")
else:
    print("P je vece od 70 a to nas ne zanima")
cas = int(input("Unesite tacan broj casova bez minuta: "))
if cas in range(0,24):
    if cas<10:
        print("DOBRO JUTRO!")
    elif cas<12:
        print("DOBRO PREPODNE!")
    elif cas<18: #isto kao da smo pitali if cas>12 and cas<18:
        print("DOBRO PREDVECE!")
    elif cas<22:
        print("DOBRO VECE!")
    else:
        print("LAKU NOC!")
else:
    print("BROJ MORA BITI U OPSEGU OD 0 DO 24, JER DAN IMA 24 CASA.")    
for i in range(0,20,2): #ispis parnih brojeva od 0 do 20. 20 nije ukljuceno
    print(i)
for i in range(10,0,-1): #10 ukljuceno, 0 nije ukljucena, korak -1
    print(i)
def par_nepar(a):
    if a % 2 == 0:
        print("uneti broj je paran ")
    else:
        print("Uneti broj je neparan ")    
par_nepar(10)

#bacanje novcica
a = input("Koliko puta zelite da bacate novcic?")

for x in range(0, int(a)):
    slucaj = random(0,1)
n = int(input("KOLIKO PUTA ZELITE DA BACATE NOVCIC? "))
pismo = 0
glava = 0
for x in range(0,n):
    a = random.randint(0,1)
    if a == 1:
        glava +=1
    else:
        pismo +=1
print(glava)
print(pismo)
pro_glava = glava/n * 100
pro_pismo = pismo/n * 100
print("Glava se pojavila {0} ({2}%) puta, a pismo se pojavilo {1} ({3}%) puta.".format(glava,pismo,pro_glava,pro_pismo))

import random
a = "neki tekst koji ispitujemo sta i kako nen."
print(a)
print(a[2:])
print(a[5:9])
print(a[:9])
print(a[::])
print(a[::2])
print(a[::-1])
print(a[-1])
print(a[0])
c = random.randrange(0,len(a))
print(c)
print(a[0:c])
print(a[-6:-1]) #-1 se ne ispisuje jer je poskednju karakter
print(a[-9:-3])
print(a.replace("n","N"))
print(a.lower())
print(a.upper())
print(a.startswith("n")) #true ili false
print(a.endswith(".")) #true ili false
print(a.find("n")) #samp poziciju prvog n, ostalo bi morali da prebrojimo. ako nwma n vraca -1
print(a.index("")) #samo poziciju prvog n. ostalo bi morali da prebrojimo. ako nema vraca gresku.

i = 1
while i<=10:
    print(i*"*")
    i += 1

j = 1
while j<=8:
    print(" "*(8-j)+"*"*(2*j-1))
    j = j+1

#papir, kamen, makaze
import random
ja = 0
kompa = 0
odgovor = input("Da li zelite da igra pocne: -->  ")
if odgovor.upper() == "DA":
    print("Srecno!")
    opcije = ["papir", "kamen", "makaze"]
    while ja<3 and kompa<3:
        korisnik = input("Unesite vas odgovor: ")
        random_broj = random.randint(0,2)
        kompjuter = opcije[random_broj]
        print("Kompjuter bira: ",kompjuter)
        if korisnik.lower() == "papir" and kompjuter == "papir":
            print("Nereseno")
        if korisnik.lower() == "papir" and kompjuter == "makaze":
            kompa += 1
        if korisnik.lower() == "papir" and kompjuter == "kamen":
            ja += 1
        if korisnik.lower() == "kamen" and kompjuter == "kamen":
            print("Nereseno")
        if korisnik.lower() == "kamen" and kompjuter == "papir":
            kompa += 1
        if korisnik.lower() == "kamen" and kompjuter == "makaze":
            ja += 1
        if korisnik.lower() == "makaze" and kompjuter == "makaze":
            print("Nereseno")
        if korisnik.lower() == "makaze" and kompjuter == "kamen":
            kompa += 1
        if korisnik.lower() == "makaze" and kompjuter == "papir":
            ja += 1
    if ja>kompa:
        print("Cestitam, pobedili ste rezultatom {} naprema {}!!!".format(ja, kompa))
    else:
        print("Nazalost, kompjuter je pobedio rezultatom {} naprema {}!!!".format(kompa, ja))
       
else:
    print("Vratite se kada budete spremni da se igramo!!!")
# II nacin ovog zadatka
#papir, kamen, makaze:
import random
dogadjaji = ["papir", "kamen", "makaze"]
ja_score = 0
kompa_score = 0
while ja_score < 3 and kompa_score < 3:
    ja = input("Unesi papir kamen ili makaze:  ")
    ja = ja.lower()
    if ja not in dogadjaji:
        print("Niste dobro uneli. Unesite ponovo.")
        continue
    racunar = random.randint(0,2)
    izbor_kompjutera = dogadjaji[racunar]
    print("Kompjuter je odabrao:",izbor_kompjutera)
    if ja == izbor_kompjutera:
        print("Nereseno.")
        continue
    if ja == "papir" and izbor_kompjutera == "kamen":
        ja_score += 1
    elif ja == "kamen" and izbor_kompjutera == "makaze":
        ja_score += 1
    elif ja == "makaze" and izbor_kompjutera == "papir":
        ja_score += 1
    else:
        kompa_score += 1
    #if ja_score == 3 or compa_score == 3: (Da smo stavili na pocetku While true)
        #break
if ja_score>kompa_score:
    print("CESTITAM, pobedili ste rezultatom {} naprema {}.".format(ja_score,kompa_score))
else:
    print("IZGUBILI STE, kompjuter je pobedio rezultatom {} naprema {}.".format(kompa_score,ja_score))
    
while True: #radi sve dok ne unesemo q 
    slovo = input("Unesite add ako zelite unos, view ako zelite pregled i q ukoliko zelite prekid i izlaz: ").lower()
    if slovo == "q":
        break
    if slovo == "add":
        ime = input("Unesite vase ime: ")
        prezime = input("Unesite vase prezime: ")
    elif slovo == "view":
        print(ime, prezime)
    else:
        print("Nekorektan unos")
        


