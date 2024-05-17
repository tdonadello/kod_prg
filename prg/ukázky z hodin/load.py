import csv
path = "H:\\Programování\\Python\\ukázky z hodin\\data.csv"
bludistaci = {}

with open(path, "r", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    for radek in reader:
        bludistaci[radek[0]] = int(radek[1])


print(bludistaci)