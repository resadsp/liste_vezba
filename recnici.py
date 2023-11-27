#ZADATAK
niz_artikala = []
while True:
    print(" ")
    print("""--------MOJA TRGOVINA--------
        [1] DODAJ NOVI PROIZVOD
        [2] STAMPAJ LAGER LISTU
        [3] KREIRAJ KORPU
        [4] INFORMACIJE O PROIZVODU
        [Q] IZLAZ""")
    print(" ")
    unos = input("IZABERITE JEDNU OD OPCIJA: ")

    
    if unos.strip() == "1":
        
        while True:
            print("------Unesi podatke ili pritisni space za prekid------")
            naziv = input("Unesite naziv artikla: ")
            if naziv == " ":
                break
            else:
                barkod = input("Unesite barkod: ")
                cena = int(input("Unesite cenu artikla: "))
                kolicina = int(input("Unesite kolicinu: "))
                
                artikl = {
                    "naziv" : naziv,
                    "barkod" : barkod,
                    "cena" : cena,
                    "kolicina" : kolicina
                }
                niz_artikala.append(artikl)
                
    if unos.strip() == "2": 
             print(" ")  
             print("ARTIKLE KOJE STE UNELI:") 
             for p in niz_artikala:
                 print(p)
    
    if unos.strip() == "3":
        korpa = []
        s = 0
        while True:
            moj_barkod = input("Unesite barkod proizvoda ili pritisnite space za prekid: ")
            if moj_barkod == " ":
                print(" ")
                break
            else:
                for i in niz_artikala:
                    if i["barkod"] == moj_barkod:
                       i["kol"] = int(input("Unesite kolicinu: "))
                       korpa.append(i)
        for j in korpa:
            s += j["kol"] * j["cena"] 
        print("UKUPNO ZA NAPLATU",s,"rsd")
        novac = int(input("Kupac dao (rsd): "))
        print("Vratiti kupcu:",novac-s,"rsd")
    
    if unos.strip() == "4":
         info = input("Unesite barkod proizvoda za koji zelite da saznate podatke: ")
         for i in niz_artikala:
             if i["barkod"] == info:
                 a = i["naziv"]
                 b = i["barkod"]
                 c = i["cena"]
                 d = i["kolicina"]
                 e = i["kol"]
                 print(" ")
                 print("NAZIV PROIZVODA: ",a)
                 print("BARKOD: ",b)
                 print("CENA: ",c)
                 print("KOLICINA: ",d-e)
                 break
             else:
                print("NE POSTOJI PROIZVOD SA NAVEDENIM BARKODOM!")
    if unos.strip().upper() == "Q":
        print("PRIJATNO!")
        break