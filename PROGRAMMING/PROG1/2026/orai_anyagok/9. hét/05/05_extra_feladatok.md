# Programozás 1 – Extra feladatok gyors csoportoknak

## Feladat 41 – Szám és négyzete párok
Adott a lista:
```python
szamok = [1, 2, 3, 4, 5]
```
Készíts listát ilyen elemekkel:
```python
[(1, 1), (2, 4), (3, 9), ...]
```

## Feladat 42 – Magánhangzók száma szavanként
Adott a lista:
```python
szavak = ["alma", "körte", "banán"]
```
Készíts szótárat, ahol a kulcs a szó, az érték pedig a benne lévő magánhangzók száma.

## Feladat 43 – Páros/páratlan dict
Adott a lista:
```python
szamok = [1, 2, 3, 4, 5, 6]
```
Készíts ilyen szótárat:
```python
{"paros": [...], "paratlan": [...]}
```

## Feladat 44 – Leghosszabb szó
Adott a lista:
```python
szavak = ["alma", "körte", "eper", "szilva"]
```
Keresd meg a leghosszabb szót.

## Feladat 45 – Összeg szöveges formában
Adott a lista:
```python
szamok = [10, 20, 30]
```
Számold ki az összeget, és készíts ilyen sztringet:
```python
"10 + 20 + 30 = 60"
```

## Feladat 46 – Egyszerű naplóelemzés
Adott a lista:
```python
logok = [
    "INFO: elindult",
    "ERROR: hiba történt",
    "INFO: fut",
    "WARNING: kevés memória",
    "ERROR: összeomlott"
]
```
Számold meg, hány INFO és hány ERROR van, majd készíts külön listát az ERROR sorokból.

## Feladat 47 – Jelszavak szűrése
Adott a lista:
```python
jelszavak = ["abc123", "jelszo", "Password1", "123456"]
```
Szűrd ki azokat a jelszavakat, amelyek:
- legalább 6 karakter hosszúak,
- tartalmaznak számot.

## Feladat 48 – Számfeldolgozó pipeline
Adott a lista:
```python
szamok = [1,2,3,4,5,6,7,8,9,10]
```
Lépések:
1. csak a párosak,
2. szorozd meg 3-mal,
3. csak a 10-nél nagyobbak maradjanak.

## Feladat 49 – 10-es szorzótábla
Készíts 1-től 10-ig szorzótáblát lista a listában formában.

## Feladat 50 – Mini dolgozat
Írj programot, amely:
- végigmegy egy számlistán,
- kigyűjti a 10-nél nagyobb páros számokat,
- ezekből új listát készít,
- majd kiírja az összegüket.

Adott:
```python
szamok = [4, 11, 16, 23, 8, 42, 7, 10]
```
Oldd meg először ciklussal, majd comprehensionnel is.
