[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/rZeXDXbn)
# 💻 PROGRAMOZÁS GYAKORLAT – ZH FELADATSOR (120 PERC)

**Összpontszám:** 100 pont

**Témakörök:** Összetett adatszerkezetek, szövegfeldolgozás, adattisztítás és statisztikai összesítés.

---

## Mi a ZH célja?

Ez a feladatsor a való életből vett szoftverfejlesztői kihívásokat modellezi. Nemcsak azt mérjük, hogy ismered-e a programozási nyelv szintaxisát, hanem azt is, hogyan látod át az adatok közötti összefüggéseket.

## 1. feladat: Cikknézések elemzése (25 pont)

### Kontextus

Egy weboldal böngészési előzményeit kell elemezned. Szeretnénk összehasonlítani két konkrét felhasználó böngészési szokásait, hogy lássuk, mennyire hasonló az érdeklődési körük.

### Bemenet

- Soronként érkeznek az adatok `user;slug` formátumban (felhasználónév és cikk azonosító).
- A beolvasást a `VEGE` kulcsszóig végezd (ez a sor már nem tartalmaz adatot).
- Az utolsó sor két felhasználó nevét tartalmazza szóközölve:
  `u1 u2`.

### Feladat

Írj egy függvényt, ami a beolvasott adatok alapján meghatározza és visszaadja az alábbi négy számot:

- Hány egyedi cikket nézett meg az `u1` felhasználó?
- Hány egyedi cikket nézett meg az `u2` felhasználó?
- Hány közös cikk van, amit mindketten láttak? (metszet)
- Hány összesen különböző cikk fordult elő kettejüknél? (unió)

Ha egy megadott felhasználó nem szerepel az adatokban, a nézett cikkeinek halmaza üresnek tekintendő.

### Példa bemenet

```text
anna;python-alapok

anna;dict-es-set

anna;python-alapok

bela;python-alapok

bela;fajlkezeles

cili;dict-es-set

VEGE

anna bela
```

### Példa kimenet

```text
u1_egyedi_db=2

u2_egyedi_db=2

kozos_db=1

osszes_db=3
```

---

## 2. feladat: Szógyakoriság normalizálással (25 pont)

### Kontextus

Egy strukturálatlan szövegből kell kinyerned a legfontosabb kifejezéseket, miközben automatizáltan tisztítod a szöveget a felesleges karakterektől.

### Feladat

Dolgozd fel a beolvasott szöveget az alábbi szabályok szerint:

1. Alakíts minden karaktert kisbetűssé.
2. Minden nem betű karaktert (szám, írásjel, szóköz) tekints elválasztónak. Ezek mentén darabold fel a szöveget.
3. Az üresen maradt elemeket távolítsd el.
4. Számold meg a szavak gyakoriságát.

Írj egy függvényt, ami visszaadja a Top 5 leggyakoribb szót az alábbi rendezési szabályok szerint:

- Elsődlegesen a gyakoriság szerint csökkenő sorrendben.
- Azonos gyakoriság (holtverseny) esetén betűrend szerint növekvő (A-Z) sorrendben.

### Példa bemenet

```text
Alma, körte, alma! Sárga körte; alma? Banán.
```

### Példa kimenet

```text
alma 3

körte 2

banán 1

sárga 1
```

---

## 3. feladat: Rendszernapló (log) feldolgozás (50 pont)

### Kontextus

Egy rendszer naplófájlját kell elemezned statisztikai riportok készítéséhez. Az adatok „zajosak”, ezért elengedhetetlen az előzetes szűrés és a megfelelő adatszerkezetek kiválasztása.

### Bemenet

- Az első sor tartalmazza a rekordok számát (`N`).
- Ezután `N` sor következik: `timestamp;user;action;value` formátumban.

### Adattisztítási szabályok (kötelező)

Csak azokat a rekordokat dolgozd fel, ahol:

- Az `action` értéke a következők egyike: `LOGIN`, `VIEW`, `BUY`, `ERROR`.
- Ha az akció `BUY`, a rekord csak akkor érvényes, ha a `value` egy pozitív egész szám.
- Minden egyéb érvényes akció (`LOGIN`, `VIEW`, `ERROR`) marad a rendszerben.

### Részfeladatok

**3/A – Akciók gyakorisága (10 pont):** Számold össze az érvényes akciókat a megadott fix sorrendben: `LOGIN`, `VIEW`, `BUY`, `ERROR`.

**3/B – Top 2 vásárló (15 pont):** Keresd meg a két legtöbbet költő felhasználót (a `BUY` értékek összege alapján). Holtverseny esetén a névsor döntsön.

**3/C – Hibaarány és problémás felhasználó (10 pont):** Számold ki a hibás rekordok (`ERROR`) arányát az összes érvényes rekordhoz képest (százalékban, két tizedesre: `XX.XX%`). Keresd meg azt a felhasználót is, aki a legtöbb hibát produkálta.

**3/D – Összefoglaló riport (10 pont):** Készíts egy riportot névsor szerint növekvő sorrendben. Minden felhasználóhoz írd ki: hány különböző cikket nézett meg, összesen mennyit költött, és hány hibát generált.

**3/E – Első hiba elkövetője (5 pont):** Határozd meg, ki követte el a naplóban szereplő legelső érvényes hibát (`ERROR`).

### Példa bemenet

```text
2026-03-21 10:00;anna;LOGIN;-

2026-03-21 10:01;anna;VIEW;python-alapok

2026-03-21 10:02;bela;VIEW;python-alapok

2026-03-21 10:03;anna;BUY;1200

2026-03-21 10:04;bela;BUY;800

2026-03-21 10:05;bela;ERROR;timeout

2026-03-21 10:06;cili;VIEW;dict-es-set

2026-03-21 10:07;cili;BUY;1000

2026-03-21 10:08;cili;BUY;-5
```

### Példa kimenet

```text
LOGIN=1

VIEW=3

BUY=3

ERROR=1

anna 1200

cili 1000

hibaarany=12.50%

problemas_user=bela (1 error)

anna view_egyedi_db=1 koltes=1200 error_db=0

bela view_egyedi_db=1 koltes=800 error_db=1

cili view_egyedi_db=1 koltes=1000 error_db=0

elso_error_user=bela
```
