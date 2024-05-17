import csv

#cesta = "H:\\Programování\\Python\\ukázky z hodin\\data.csv"
#with open(cesta, "r") as f:
#    reader = csv.reader(f, delimiter=";")
#    #delimiter...čím oddělujeme hodnotu
#    for x in reader:
#        print(x)

cesta = "H:\\Programování\\Python\\ukázky z hodin\\data.csv"
with open(cesta, "w", newline="") as f:
    jmeno = input("Zadej jméno: ")
    pocet = int(input("Zadej počet: "))
    writer = csv.writer(f, delimiter=";")
    writer.writerow([jmeno, pocet])