# 💻 PROGRAMOZÁS GYAKORLAT – GYAKORLÓ ZH (120 PERC)

**Összpontszám:** 100 pont

**Témakörök:** Összetett adatszerkezetek, szövegfeldolgozás, adattisztítás és statisztikai összesítés.

---

## 1. feladat: Könyvtári kölcsönzések elemzése (25 pont)

### Kontextus

Egy egyetemi könyvtár kölcsönzési adatait kell elemezned. Szeretnénk összehasonlítani két diák olvasási szokásait, hogy lássuk, mennyi közös van a szakirodalmi érdeklődésükben.

### Bemenet

- Soronként érkeznek az adatok `olvaso;konyv_cim` formátumban.
- A beolvasást a `VEGE` kulcsszóig végezd (ez a sor már nem tartalmaz adatot).
- Az utolsó sor két diák nevét tartalmazza szóközölve: `diak1 diak2`.

### Feladat

Írj egy függvényt, ami a beolvasott adatok alapján meghatározza és visszaadja az alábbi négy számot:

- Hány egyedi könyvet kölcsönzött ki a `diak1`?
- Hány egyedi könyvet kölcsönzött ki a `diak2`?
- Hány közös könyv van, amit mindketten kivettek legalább egyszer? (metszet)
- Hány összesen különböző könyv fordult elő kettejüknél? (unió)

_(Ha egy megadott olvasó nem szerepel az adatokban, az általa olvasott könyvek halmaza üresnek tekintendő.)_

### Példa bemenet

```text
gabor;gyuruk-ura
gabor;harry-potter
gabor;gyuruk-ura
lilla;harry-potter
lilla;vajak
zoli;dune
VEGE
gabor lilla
```

### Példa kimenet

```text
diak1_egyedi_db=2
diak2_egyedi_db=2
kozos_db=1
osszes_db=3
```

---

## 2. feladat: Termékértékelések kulcsszavai (25 pont)

### Kontextus

Egy webshop vásárlói értékeléseiből kell kinyerned a legjellemzőbb szavakat, hogy a marketingesek lássák, mik a leggyakoribb jelzők a termékkel kapcsolatban. A szöveg viszont tele van írásjelekkel és elütésekkel.

### Feladat

Dolgozd fel a beolvasott szöveget az alábbi szabályok szerint:

1. Alakíts minden karaktert kisbetűssé.
2. Minden **nem betű** karaktert (szám, írásjel, szóköz) tekints elválasztónak. Ezek mentén darabold fel a szöveget.
3. Az üresen maradt elemeket távolítsd el.
4. Számold meg a szavak gyakoriságát.

Írj egy függvényt, ami visszaadja a **Top 3** leggyakoribb szót az alábbi rendezési szabályok szerint:

- Elsődlegesen a gyakoriság szerint **csökkenő** sorrendben.
- Azonos gyakoriság (holtverseny) esetén betűrend szerint **növekvő (A-Z)** sorrendben.

### Példa bemenet

```text
Szuper, gyors! Nagyon szuper termek; gyors kiszallitas? Jo. 10/10 gyors!
```

### Példa kimenet

```text
gyors 3
szuper 2
jo 1
```

_(Megjegyzés: A "kiszallitas", "nagyon", "termek" is 1-szer szerepel, de az ABC sorrend miatt a "jo" kerül a 3. helyre)._

---

## 3. feladat: Online Játékszerver Napló (Log) Feldolgozás (50 pont)

### Kontextus

Egy multiplayer játék szervernaplóját kell elemezned statisztikai riportok készítéséhez. Meg kell találnod a legjobb játékosokat és a leggyakoribb szerverhibákat (szakadások).

### Bemenet

- Az első sor tartalmazza a rekordok számát (`N`).
- Ezután `N` sor következik: `timestamp;player;event;value` formátumban.

### Adattisztítási szabályok (kötelező)

Csak azokat a rekordokat dolgozd fel, ahol:

- Az `event` értéke a következők egyike: `LOGIN`, `MATCH`, `SCORE`, `CRASH`.
- Ha az esemény `SCORE`, a rekord csak akkor érvényes, ha a `value` egy **pozitív egész szám** (a szerzett pont).
- Minden egyéb érvényes esemény (`LOGIN`, `MATCH`, `CRASH`) marad a rendszerben.

### Részfeladatok

**3/A – Események gyakorisága (10 pont):** Számold össze az érvényes eseményeket a megadott fix sorrendben: `LOGIN`, `MATCH`, `SCORE`, `CRASH`.

**3/B – Top 2 Játékos (15 pont):** Keresd meg a két legtöbb pontot gyűjtő játékos (a `SCORE` értékek összege alapján). Holtverseny esetén a névsor döntsön ABC szerint.

**3/C – Szakadási arány és problémás játékos (10 pont):** Számold ki a hibás rekordok (`CRASH`) arányát az összes érvényes rekordhoz képest (százalékban, két tizedesre: `XX.XX%`). Keresd meg azt a játékost is, aki a legtöbb `CRASH`-t szenvedte el.

**3/D – Összefoglaló riport (10 pont):** Készíts egy riportot névsor szerint **növekvő** sorrendben. Minden játékoshoz írd ki: hány _egyedi_ meccsen (`MATCH`) vett részt, összesen mennyi pontot (`SCORE`) gyűjtött, és hány `CRASH`-t szenvedett el.

**3/E – Az első szerverhiba elszenvedője (5 pont):** Határozd meg, ki szenvedte el a naplóban szereplő legelső érvényes szakadást (`CRASH`).

### Példa bemenet

```text
2026-04-10 15:00;alex;LOGIN;-
2026-04-10 15:01;alex;MATCH;arena-1
2026-04-10 15:02;bob;MATCH;arena-1
2026-04-10 15:03;alex;SCORE;500
2026-04-10 15:04;bob;SCORE;300
2026-04-10 15:05;bob;CRASH;lag
2026-04-10 15:06;chloe;MATCH;arena-2
2026-04-10 15:07;chloe;SCORE;750
2026-04-10 15:08;chloe;SCORE;-10
```

### Példa kimenet

```text
LOGIN=1
MATCH=3
SCORE=3
CRASH=1
--------------------------------------------------
chloe 750
alex 500
--------------------------------------------------
crash_arany=12.50%
problemas_player=bob (1 crash)
--------------------------------------------------
alex match_egyedi_db=1 total_score=500 crash_db=0
bob match_egyedi_db=1 total_score=300 crash_db=1
chloe match_egyedi_db=1 total_score=750 crash_db=0
--------------------------------------------------
elso_crash_player=bob
```
