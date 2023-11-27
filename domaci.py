# ZADATAK [1/2] I ZADATAK [2/2] SA PREZENTACIJE PPF_5.pdf
print(" ")
niz_automobili = []
while True:
    print(" ")
    print("""--------MENI AUTOMOBIL-------
        [1] DODAJ NOVI AUTOMOBIL
        [2] STAMPAJ LAGER LISTU
        [3] PRETRAGA PO GODINI ILI KONJSKOJ SNAZI
        [Q] IZLAZ""")
    print(" ")
    unos = input("IZABERITE JEDNU OD OPCIJA: ") #korisnik unosi zeljenu opciju od ponudjenih
    
    if unos.strip() == "1": #ukoliko je izabrao opciju 1, unosi trazene podatke sve dok ne prekine unos sa pritiskom na taster space
       
        while True:
            print("------Unesi podatke ili pritisni space za prekid------")
            marka = input("Unesite marku automobila: ")
            if marka == " ":
                break
            else:
                model = input("Unesite model automobila: ")
                godina = input("Unesite godinu proizvodnje: ")
                snaga = int(input("Unesite konjsku snagu automobila: "))  
            
            automobil = {
                "marka" : marka,
                "model" : model,
                "godina" : godina,
                "snaga" : snaga
            }
            niz_automobili.append(automobil) #pravimo niz od automobila
    
            
    if unos.strip() == "2": #ukoliko je korisnik izabaro opciju 2, stampa celu listu automobila sa svim podacima
        for i in niz_automobili:
            print(i)
    
    
    if unos.strip() == "3": #ukoliko je korisnik izabrao opciju 3, odamh bira kako zeli da vrsi pretragu automobila (po godini ili snazi)
        pretraga_po_godini = []
        pretraga_po_snazi = []
        print("""
    DA LI ZELITE DA PRETRAZUJETE PO:
        [1] GODINA PROIZVODNJE 
        [2] KONJSKA SNAGA""")
        print(" ")
        izbor = input("Unesite 1 ili 2: ") #ukoliko je uneo broj 1, pretraga se vrsi po godini
        if izbor.strip() == "1":
            print(" ")
            godina_p = input("Unesite godinu proizvodnje: ")
            print("Rezultati pretrage: ")
            for i in niz_automobili:
                if i["godina"] == godina_p:
                    pretraga_po_godini.append(i)
            for i in pretraga_po_godini:
                a = i["marka"]
                b = i["model"]
                c = i["godina"]
                d = i["snaga"]
                print("MARKA AUTOMOBILA JE: ",a)
                print("MODEL AUTOMOBILA JE: ",b)
                print("GODINA PROIZVODNJE AUTOMOBILA JE: ",c)
                print("KONJSKA SNAGA JE: ",d)
                print(" ")
        if izbor.strip() == "2": #ukoliko je uneo broj 2, pretraga se vrsi po snazi
            print(" ")
            min_snaga = int(input("Unesite minimalnu konjsku snagu: "))
            max_snaga = int(input("Unesite maksimalnu konjsku snagu: "))
            print("Rezultati pretrage: ")
            for i in niz_automobili:
                if i["snaga"] >= min_snaga and i["snaga"] <= max_snaga:
                    pretraga_po_snazi.append(i)
            for i in pretraga_po_snazi:
                a = i["marka"]
                b = i["model"]
                c = i["godina"]
                d = i["snaga"]
                print("MARKA AUTOMOBILA JE: ",a)
                print("MODEL AUTOMOBILA JE: ",b)
                print("GODINA PROIZVODNJE AUTOMOBILA JE: ",c)
                print("KONJSKA SNAGA JE: ",d)
                print(" ")    
                
                   
    if unos.strip().upper() == "Q": #ukoliko je korisnik uneo q ili Q, ispisuje se poruka PRIJATNO i break
        print("PRIJATNO!")
        break        