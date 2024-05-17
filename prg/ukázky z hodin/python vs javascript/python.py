## Vytváření proměnných
text = "What  is the answer to the ultimate question of life, the universe, and everythin"
cislo = "42"

## Příklad podmínky
skore = input("Jaké je tvé skóre?")

if skore == 90: 
    znamka = "Výborně"
elif skore == 80:
    znamka = "Chvalitebně"
else:
    znamka = "Nedostatečně"

## Příklad cyklu
skore = input("Jaké je tvé skóre?")
while skore > 60:
    print("Snaž se víc")
    skore = input("Jaké je tvé skóre?")
