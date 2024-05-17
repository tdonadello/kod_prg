import sys

def kladne_zaporne(x):
    if x > 0:
        print("číslo je kladné")
    elif x < 0:
        print("číslo je záporné")
    else:
        print("číslo je nula")

while True:
    try:
        cislo = int(input("Zadej číslo: "))
        kladne_zaporne(cislo)
    except KeyboardInterrupt:
        print("Program manuálně ukončn")
        sys.exit()
    except ValueError:
        print("Špatný input. Zadal/a jsi číslo?")
    else:
        print("Kód proběhl úspěšně")
        break
    finally:
        print("Kód nějak proběhl. Úspěšně nebo neúspěšně")
        #finally se píše vždycky