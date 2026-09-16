[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/dAOyrmpL)
## Point

Készítsd el a Point osztályt úgy, hogy az tudja tárolni egy síkbeli pont koordinátáit.

A koordináták `x` és `y` nevű attribútumok legyenek, és lehessen megadni az értéküket példányosításkor: `Point(1, 2)`.
Ha nem adják meg, akkor legyenek 0-k.

Legyen egy `distance` metódusa, ami paraméterben kap egy másik `Point` objektumot, és visszaadja a két pont közti távolságot.

Legyen definiálva az egyenlőség (`==`) operátor két pont között: akkor egyenlők, ha a koordinátáik egyenlők.

Lehessen kiíratni a koordinátákat az objektumot átadva a `print()` függvénynek.
Ilyen formában jelenjen meg: `(x, y)`.

A `__repr__` metódus adja vissza az objektum létrehozásához használható függvényhívást tartalmazó stringet.

## Path

Készítsd el a `Path` osztályt, ami egy pontok (`Point` objektumok) sorozatából álló útvonalat tud tárolni.

Példányosításkor legyen üres a pontok sorozata.

Legyen definiálva a `__len__` metódus, ami adja vissza a pontok számát.
(Ez hívódik meg, ha az objektumot átadjuk a `len()` függvénynek.)

Legyen egy `add` metódusa, ami egy `Point` objektumot vár paraméterben, és hozzáfűzi a pontsorozathoz.
Ha a kapott pont egyezik az utolsó ponttal, ne fűzze hozzá.

Legyen egy `length` metódusa, ami adja vissza az útvonal hosszát, azaz az egymást követő pontok közti távolságok összegét.

Legyen egy `extend` metódusa, ami a paraméterben kapott másik `Path` pontjait hozzáfűzi a pontsorozathoz az `add` metódus segítségével.
(Ha a másik `Path` kezdőpontja egyezik a jelenlegi végponttal, akkor az ne kerüljön hozzáadásra.)

Az objektumot átadva a `print()` függvénynek, írja ki az egyes pontok koordinátáit (a `Point` osztályban definiált formátumban), közöttük `" - "` elválasztó stringekkel.
