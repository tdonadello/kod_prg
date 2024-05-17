def main():
    cecka = {
        "Jakub" : 3,
        "Vašek" : 2,
        "Ema" : 2
    }

    jmeno = input("Koho chceš oceckovat? ").capitalize() #"capitalize" převede 1. písmeno na začátek
    kolik_cecek(cecka, jmeno)

def kolik_cecek(seznam, jmeno):
    if jmeno in seznam:
        print(seznam[jmeno])

def pridej_studenta(seznam, jmeno):
    seznam[jmeno] = 1

if __name__ == "__main__":
    main()
