def ispis():
    print("Ova funkcija samo stampa odredjeni tekst i to onda kada bude pozvana.")
ispis()
for i in range(0,5):
    ispis()


def moje_ime(ime):
    print("MOJE IME JE {} A PREZIME JE SPAHOVIC.".format(ime))

moje_ime("RESAD")
moje_ime("MAIDA")
moje_ime("ATIJA")
moje_ime("ADEM")

a = input("UNESITE IME: ")
moje_ime(a)

def ime_prezime(ime, prezime):
    print("Vase ime je {} a vase prezime je {}.".format(ime,prezime))

while True:
    b = input("Unesite vase ime ili pritisnite space za prekid: ").capitalize()
    if b == " ":
        break
    else:
         c = input("Unesite vase prezime: ").capitalize()
         ime_prezime(b,c)

def deca(*dete):
    print("najstarije dijete je {} a najmladje dijete je {}".format(dete[0],dete[1]))

deca("atija","adem","uma","davud")

def zbir(a,b,c):
    print(a+b+c)
zbir(4,54,6)

def zbir(a,b,c):
    return a+b+c
print(zbir(4,54,6))

def podrazumevano(drzava = "Srbija"):
    print("ja sam iz drzave {}.".format(drzava))
podrazumevano("bih")
podrazumevano("nemacka")
podrazumevano("francuska")
podrazumevano("italija")
podrazumevano()

niz = [0,1,2,3,4,5,6,7,8,9,10]
def suma(neki_niz):
    s = 0
    for i in range(0,len(neki_niz)):
        s += i
    return s
suma(niz)
print(suma(niz))

brojevi = range(0,51)
def sumarum(l):
    su = 0
    for i in l:
        su += i
    return(su)
a = sumarum(brojevi)
print(a)
print(a*10)

x = lambda a: a + 100 + 2* a
print(x(2))

y = lambda b: b*100
print(y(10))

z = lambda c: c * 5 + c * 6
print(z(4))

def funkcija(n):
    return lambda a: a*n

neka = funkcija(4) # neka = lambda a: a*4
print(neka(8))

a = lambda br: br * 10
print(a(10))

b = lambda g,h,j,l: g*h*j*l
print(b(4,5,6,7))

def fja(broj):
    return lambda x: x * broj

g = fja(10)
# g = lambda x : x * 10
print(g(10))


def paran(n):
    if n%2 == 0:
        print("Uneti broj je paran")
    else:
        print("Uneti broj je neparan")       
        
def pozitivan(a):
    if a>0:
        print("Uneti broj je pozitivan")
    else:
        print("Uneti broj je negativan.")

br = int(input("Unesite broj: "))
paran(br)
pozitivan(br)


#faktorijel
def fact(n):
    if n ==1: #ovo stavljamo da bi smo prekinuli for petlju nekada
        return 1
    return fact(n - 1)*n
print(fact(5))

def faktorijel(m):
    if m == 1:
        return 1   
    return faktorijel(m-1)*m
print(faktorijel(6))

a = lambda x : x * 10
print(a(10))

def lam(r):
    return lambda  y: y * r #pom = lambda y : y * 10

pom = lam(10)  
print(pom(10))

niz = ["maja", "atija", "resad", "adem"]
drugi = ["amra", "farah", "rajif", "jaman"]
drugi2 = ["amra", "farah", "rajif", "jaman", "resad", "maida", "atija", "adem"]

def stampa(nesto):
    for i in range(0,len(nesto)): #for i in nesto: print i
        print(nesto[i])
print(" ")
stampa(niz)
print(" ")
stampa(drugi)
print(" ")
stampa(drugi2)

a = []
def unos():
    #a =[] a ako hocemo da nam pamti rezultate onda ovo a stavljamo ispred def unos()
    while True:
        c = input("UNESITE IME: ").capitalize()
        if c == " ":
            break
        else:
            a.append(c)
    print(a)
print("PRVI NIZ JE: ")
unos()
print("DRUGI NIZ JE: ")
unos()
        


  


