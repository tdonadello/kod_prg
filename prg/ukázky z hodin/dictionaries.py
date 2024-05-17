kocka = {
    "barva" : "černá",
    "jméno" : "Mourek",
    "oblíbené_jídlo" : ["sushi", "myš"],
    "povaha" : "agresivní",
    "počet_nohou" : 4,
    "žije" : True
    }

print(kocka["jméno"])
print(kocka["oblíbené_jídlo"][0])

for jidlo in kocka["oblíbené_jídlo"]:
    print(jidlo)

telefonni_seznam = {
    "Jarmil" : "735 865 312",
    "Květoslava" : "987 654 321",
    "Vašek" : "123 456 789"
}