[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tATJpAAO)
# PROGRAMOZÁS GYAKORLAT – ZH

**Összpontszám:** 100 pont

**Témakörök:** Halmazok és szótárak, szöveg-normalizálás, adattisztítás és statisztikai riport.

---

## Mi a feladatsor célja?

A feladatok valós adatelemzési helyzeteket modelleznek: részben zajos bemenetből kell hasznos összesítéseket előállítani. A hangsúly a helyes adatszerkezet-választáson és a pontos feldolgozási szabályokon van.

## Értékelési szempontok

Az értékelés során nemcsak a helyes működés számít, hanem külön fontos szempont:

- a megfelelő adatszerkezet kiválasztása,
- a kód minősége és áttekinthetősége,
- a tiszta, jól elkülönített függvények használata.

---

## 1. feladat: Videók megtekintéseinek összehasonlítása (50 pont)

### Kontextus

Egy videóplatform eseménynaplójából két felhasználó érdeklődési körét szeretnénk összevetni. Egy esemény azt jelzi, hogy valaki megnézett egy videót.

### Bemenet

- Soronként érkeznek az adatok `user;video_id` formátumban.
- A beolvasást a `VEGE` kulcsszóig végezd (ez a sor már nem tartalmaz adatot).
- Az utolsó sor két felhasználó nevét tartalmazza szóközzel elválasztva: `u1 u2`.

### Feladat

Írj egy függvényt, ami a beolvasott adatok alapján meghatározza és visszaadja az alábbi négy számot:

- Hány egyedi videót nézett meg az `u1` felhasználó?
- Hány egyedi videót nézett meg az `u2` felhasználó?
- Hány közös videó van, amit mindketten láttak? (metszet)
- Hány összesen különböző videó fordult elő kettejüknél együtt? (unió)

Ha egy megadott felhasználó nem szerepel az adatokban, a nézett videóinak halmaza üres.

### Példa bemenet

```text
nora;vid-101
nora;vid-102
nora;vid-101

tibi;vid-102
tibi;vid-201

dori;vid-999
VEGE

nora tibi
```

### Példa kimenet

```text
u1_egyedi_db=2
u2_egyedi_db=2
kozos_db=1
osszes_db=3
```

---

## 2. feladat: Kulcsszavak gyakorisága normalizálással (50 pont)

### Kontextus

Egy ügyfélszolgálati jegy (ticket) szövegéből szeretnénk a leggyakoribb szavakat kinyerni. A szöveg sokféle elválasztójelet és vegyes karaktereket tartalmaz.

### Feladat

Dolgozd fel a beolvasott szöveget az alábbi szabályok szerint:

1. Alakíts minden karaktert kisbetűssé.
2. Minden nem betű karaktert (szám, írásjel, szóköz, kötőjel stb.) tekints elválasztónak, és ezek mentén darabold fel a szöveget.
3. Az üres elemeket távolítsd el.
4. Számold meg a szavak gyakoriságát.

Írj egy függvényt, ami visszaadja a Top 5 leggyakoribb szót az alábbi rendezési szabályok szerint:

- Elsődlegesen gyakoriság szerint csökkenő.
- Holtverseny esetén betűrend szerint növekvő (A–Z).

### Példa bemenet

```text
Hiba: Kijelentkezés! hiba... Újra-belépés? BELÉPÉS 2026/03/30.
```

### Példa kimenet

```text
hiba 2
belépés 2
kijelentkezés 1
újra 1
```

Megjegyzés: a példában csak 4 különböző szó szerepel, ezért a „Top 5” lista rövidebb.

---