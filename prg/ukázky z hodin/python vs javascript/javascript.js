// Vytváření proměnných
let text =
    "What  is the answer to the ultimate question of life, the universe, and everything"
let cislo = 42

// Příklad podmínky
let skore = window.prompt("Jaké je tvé skóre?")

if (skore === 90) {
    znamka = "Výborně"
} else if (skore === 80) {
    znamka = "Chvalitebně"
} else {
    znamka = "Nedostatečně"
}

// Příklad cyklu
skore = window.prompt("Jaké je tvé skóre?")
while (skore > 60) {
    console.log("Snaž se víc")
    skore = window.prompt("Jaké je tvé skóre?")
}

// for
for (let i = 0; i < 11; i + 1) {
    console.log(i)
}