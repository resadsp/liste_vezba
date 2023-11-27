#MINI APLIKACIJA
print(" ")
from datetime import datetime
s = 0
br = 0
while True:
    print("""---MINI APLIKACIJA---
        [1] TRENUTNI DATUM I VREME
        [2] MINI KALKULATOR
        [3] RACUNANJE CENE SA POREZOM I POREZA
        [4] SREDNJA TEMPERATURA
        [Q] IZLAZ IZ APLIKACIJE
        """)
    unos = input("UNESITE OPERACIJU ILI Q ZA IZLAZ: ")

    if unos.strip() == "1":
            print("Trenutni datum i vreme su:",datetime.now())
            print(" ")
            
    elif unos.strip() == "2":
            a = int(input("Unesite prvi broj: "))
            b = int(input("Unesite drugi broj: "))
            op = input("Unesite operaciju +, -, *, / : ")
            if op =="+":
                print("{} + {} = {}".format(a,b,a+b))
            elif op =="-":
                print("{} - {} = {}".format(a,b,a-b))
            elif op =="*":
                print("{} * {} = {}".format(a,b,a*b))
            elif op =="/":
                if b!= 0:
                 print("{} / {} = {}".format(a,b,a/b))
                else:
                 print("Nije moguce deljenje sa nulom.")    
                    
    elif unos.strip() == "3":
            cena = float(input("Unesite osnovnu cenu: "))
            porez = float(input("Unesite porez: "))
            cena_sa_pdv = cena * (1 + porez  / 100)
            pdv = cena / 100 * porez
            print("Osnovna cena je: {}".format(cena))
            print("Cena sa porezom je {:.2f}".format(cena_sa_pdv))
            print("Porez je {:.2f}".format(pdv))
            
        
    elif unos.strip() == "4":
           while True:
               a = input("Unesite temperaturu (ili prekinete sa slovom Q): ")
               if a.upper() == "Q":
                   break
               else:
                   s += int(a)
                   br += 1
           print("Srednja vrednost je: {:.2f} ".format(s/br))
           
    elif unos.strip().upper() == "Q":
            print("DODJITE NAM OPET!")
            break

