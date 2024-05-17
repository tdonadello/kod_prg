## ukol
import random

"""
if odpoved == 1:
  print("Ano")
elif odpoved == 2:
  print("Stopro")
elif odpoved == 3:
  print("Určitě")
elif odpoved == 4:
  print("Možná")
elif odpoved == 5:
  print("Nemyslím si")
elif odpoved == 6:
  print("Ne")
elif odpoved == 7:
  print("Určitě ne")
"""

odpovedi = ["Ano", "Stopro", "Určitě", "Možná", "Nemyslím si", "Ne", "Určitě ne"]

while True:
  otazka = input("Na co se chceš zeptat?\n")
  if otazka == "konec":
    break
  odpoved = random.randint(0, 6)
  print(odpovedi[odpoved])