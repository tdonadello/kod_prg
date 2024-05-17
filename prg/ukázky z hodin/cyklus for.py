for x in range(5):
  print(x)


seznam = ["banány", "pizza", "rýže", "koláče", "kebab"]
print(seznam[1])


for jidlo in seznam:
  print(jidlo, end=" ")

print()

slovo = "ano"
print(slovo[0])

for pismeno in slovo:
  print(pismeno)

print(seznam[0][0])

for i, polozka in enumerate(seznam):
  print(i+1, polozka)
