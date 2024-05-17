import csv, sys

cesta = "H:\\Programování\\Python\\ukázky z hodin\\data.csv"

def main():
    bludistaci = {}

    nacist_data(bludistaci)

    print("Vítej uživateli")
    print("Zvol možnost: ")
    print("Pro vypsání všech Bludišťáků zvol 1")
    print("Pro vypsání jednoho studenta zvol 2")
    print("Pro přidání Bludišťáka zvol 3")
    print("Pro odebrání Bludišťáka zvol 4")
    print("Pro vypsání nejlepšího studenta zvol 5")
    print("Pro přidání studenta zvol 6")
    print("Pro ukončení zvole 7")

    
    while True:
        try:
            zvolena_moznost = int(input())
            break
        except ValueError:
            print("Nezadal jsi číso. Zadej číslo")


    match zvolena_moznost:
        case 1:
            vypisVse(bludistaci)
        case 2:
            vypisBludistakyPro(bludistaci)
        case 3:
            pridejBludistaka(bludistaci)
        case 4:
            odeberBludistaka(bludistaci)
        case 5:
            nejvyssiSkore(bludistaci)
        case 6:
            pridejStudenta(bludistaci)
        case 7:
          print("Bye!")
          sys.exit()
        case _:
            print("Zvol číslo mezi 1 - 7")
            
    uloz_data(bludistaci)
          



def vypisBludistakyPro(bludistaci):
  jmeno = input("Koho chceš zkontrolovat? ").capitalize()
  print(jmeno, bludistaci[jmeno])


def vypisVse(bludistaci):
  for i in bludistaci:
    print(i, bludistaci[i])


def pridejBludistaka(bludistaci):
  pridat = input("Komu chceš bludišťáka přidat? ").capitalize()
  bludistaci[pridat] += 1
  print(pridat, bludistaci[pridat])


def odeberBludistaka(bludistaci):
  odebrat = input("Komu chceš bludišťáka odebrat? ").capitalize()
  bludistaci[odebrat] -= 1
  print(odebrat, bludistaci[odebrat])


def pridejStudenta(bludistaci):
  student = input("Přidej studenta/ku: ").capitalize()
  bludistaci[student] = 1
  print(student, bludistaci[student])


def nejvyssiSkore(bludistaci):
  nejvic = max(bludistaci, key=bludistaci.get)
  print("Nejvíce bludišťáku má: ")
  print(nejvic, bludistaci[nejvic])

def nacist_data(bludistaci):
  with open(cesta,"r", newline="",) as f:
    reader = csv.reader(f, delimiter=";")
    for x in reader:
        bludistaci[x[0]] = int(x[1])

def uloz_data(bludistaci):
    with open(cesta,"w", newline="",) as f:
      writer = csv.writer(f, delimiter=";")
      for x in bludistaci:
          writer.writerow([x, bludistaci[x]])

if __name__ == "__main__":
    main()