[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_oyFHIWe)
# Bankszámlák

Készíts egy `Bank` osztályt, ami bankszámlák egyenlegét tárolja, és tud rajtuk műveleteket végezni.

Az osztály példányosításakor paraméterként meg kell adni a tranzakciós díjat.

Pl.: `bank = Bank(transaction_fee=2)`

A banknál lehessen számlát nyitni a számlatulajdonos nevének megadásával: `bank.create_account("Huey")`

A számla kezdeti egyenlege 0.
Ha a megadott névvel már létezik számla, akkor dobjon `ValueError`t.

Lehessen pénzt befizetni a számlára a név és az összeg megadásával: `bank.deposit("Huey", 10)`

A befizetett összegből vonja le a tranzakciós díjat.
Ha a név nem található, vagy a tranzakciós díjnál kisebb lenne az egyenleg, akkor dobjon `ValueError`t.

Lehessen pénzt felvenni a számláról a név és az összeg megadásával: `bank.withdraw("Huey", 5)`

Vonja le a pénzfelvételi díjat is.
Ha a név nem található, vagy nincs elég pénz a számlán, akkor dobjon `ValueError`t és maradjon változatlan az egyenleg.

Lehessen utalni a számlák között a két név (küldő, címzett) és az összeg megadásával: `bank.withdraw("Huey", "Dewey", 1)`

Vonja le az átutalási díjat is a küldőtől.
Ha bármelyik név nem található, vagy nincs elég pénz a küldő számláján, akkor dobjon `ValueError`t és maradjon változatlan mindkét egyenleg.

Lehessen lekérdezni a számlaegyenleget a név megadásával: `bank.balance("Huey")`

Ha a név nem található, dobjon `ValueError`t.

Lehessen lekérdezni a számlatulajdonosok neveit egy listaként: `bank.clients()`
