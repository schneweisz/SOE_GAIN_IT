# Programozás 1 - ZH 2
## Fő hangsúly

Ez a ZH nem a rövid, egy soros megoldásokat méri, hanem azt, hogy tudsz-e tiszta, függvényekre bontott, dokumentált és doctesttel ellenőrzött Python kódot írni.

## Általános követelmények

- A megoldás Pythonban készüljön.
- Minden saját függvényhez kötelező docstringet írni.
- Minden fontos feldolgozó függvény docstringjében legyen legalább 2-3 doctest példa.
- Ahol a feladat függvényt kér, ott ne `print`-tel add vissza az eredményt, hanem `return`-nel.
- A parancssoros beolvasást és kiírást különítsd el a feldolgozó logikától.
- A kód legyen olvasható: értelmes változónevek, rövid függvények, felesleges ismétlés nélkül.
- A megoldás végén a doctesteket le kell futtatni.

A doctest futtatása:

```bash
python -m doctest -v logic.py
python -m doctest -v feladat2.py
```

---

## 1. Könyvtári kölcsönzési napló feldolgozása

Készíts programot, amely könyvtári kölcsönzési eseményeket dolgoz fel. A feladat lényege nem csak a helyes eredmény, hanem a szépen felbontott, tesztelhető logika.

A bemenet több sorból áll. Minden eseménysor pontosvesszővel elválasztva tartalmazza:

```text
olvaso;konyv;napok
```

A bemenet eseményrésze a `VEGE` sorig tart. Ezután egy külön sorban két olvasónév érkezik szóközzel elválasztva. A programnak ezt a két olvasót kell összehasonlítania.

Példa bemenet:

```text
anna;Dune;14
bela;Dune;7
anna;Alapitvany;21
anna;Solaris;0
bela;Solaris;12
anna;Dune;5
bela;Metro2033;18
VEGE
anna bela
```

### Elvárt függvények

A `logic.py` modulban készítsd el legalább az alábbi függvényeket. Mindegyikhez legyen docstring, a lenti listában megadott függvényekhez pedig kötelező doctest is.

```python
def ures_sor_e(sor: str) -> bool:
    ...

def vege_sor_e(sor: str) -> bool:
    ...

def kolcsonzes_sor_feldolgozasa(sor: str) -> tuple[str, str, int]:
    ...

def olvasok_sora_feldolgozasa(sor: str) -> tuple[str, str]:
    ...

def naplo_feldolgozasa(sorok: list[str]) -> dict[str, dict[str, list[int]]]:
    ...

def olvaso_napjai(tarolo: dict[str, dict[str, list[int]]], olvaso: str) -> list[int]:
    ...

def olvaso_konyvei(tarolo: dict[str, dict[str, list[int]]], olvaso: str) -> set[str]:
    ...

def atlag(napok: list[int]) -> float:
    ...

def statisztika_keszitese(tarolo: dict[str, dict[str, list[int]]], o1: str, o2: str) -> dict[str, object]:
    ...

def statisztika_szovegge(statisztika: dict[str, object]) -> str:
    ...
```

Kötelező doctest az alábbi függvényekhez:

- `ures_sor_e`
- `vege_sor_e`
- `kolcsonzes_sor_feldolgozasa`
- `olvasok_sora_feldolgozasa`
- `naplo_feldolgozasa`
- `olvaso_napjai`
- `olvaso_konyvei`
- `atlag`
- `statisztika_keszitese`

### Doctest minták

A saját docstringjeidben ehhez hasonló példák szerepeljenek:

```python
def kolcsonzes_sor_feldolgozasa(sor: str) -> tuple[str, str, int]:
    """
    Feldolgoz egy 'olvaso;konyv;napok' formátumú sort.

    >>> kolcsonzes_sor_feldolgozasa("anna;Dune;14")
    ('anna', 'Dune', 14)
    >>> kolcsonzes_sor_feldolgozasa(" bela ; Solaris ; 12 ")
    ('bela', 'Solaris', 12)
    >>> kolcsonzes_sor_feldolgozasa("hibas sor")
    Traceback (most recent call last):
    ...
    ValueError: Hibásan formázott kölcsönzési sor
    """
```

Nem kell pontosan ugyanez a hibaüzenet, de hibás bemenetre a doctest mutassa, hogy `ValueError` keletkezik.

### A `main.py` feladata

- olvassa be az eseménysorokat `VEGE`-ig,
- olvassa be a két összehasonlítandó olvasónevet,
- hívja meg a `logic.py` megfelelő függvényeit,
- írja ki a statisztikát.

A `main.py`-ban nem kell doctest, ha csak beolvasást és kiírást tartalmaz.

### Feldolgozási szabályok

- Az üres sorokat hagyd figyelmen kívül.
- Egy eseménysor akkor érvényes, ha pontosan három része van: olvasó, könyv, napok.
- Az olvasó és a könyv nem lehet üres.
- A napok értéke egész számmá alakítható legyen.
- Negatív napszám hibás adatnak számít, ilyenkor dobj `ValueError` kivételt.
- Hibásan formázott eseménysornál dobj `ValueError` kivételt.
- Egy olvasó ugyanazt a könyvet többször is kikölcsönözheti.
- Ha egy olvasó nem szerepel a naplóban, akkor a naplistája üres lista, a könyvhalmaza üres halmaz legyen.

### Kimenet

A statisztika az alábbi sorokat tartalmazza ebben a sorrendben:

```text
o1_ossznap=40
o2_ossznap=37
o1_konyv_db=3
o2_konyv_db=3
kozos_konyv_db=2
osszes_konyv_db=4
o1_atlag=10.0
o2_atlag=12.33
tobbet_kolcsonzott=anna
```

Az átlagot két tizedesjegyre kerekítsd. Ha egy olvasónak nincs kölcsönzése, az átlaga legyen `0.0`. Ha a két összesített napszám egyenlő, a `tobbet_kolcsonzott` értéke legyen `dontetlen`.

---


## 2. Mozi jegyrendelés feldolgozása tiszta függvényekkel

Készíts `feladat2.py` néven modult. Egy jegytípus ilyen tuple:

```python
TicketItem = tuple[str, float, int]
# jegytípus neve, egységár, darabszám
```

Készítsd el az alábbi függvényeket:

```python
def calculate_subtotal(items: list[TicketItem]) -> float:
    ...

def calculate_discount(items: list[TicketItem], is_student: bool, promo_percent: float | None) -> float:
    ...

def calculate_final_total(items: list[TicketItem], is_student: bool, promo_percent: float | None) -> float:
    ...

def build_booking_code(booking_id: int, customer_name: str, status: str) -> str | None:
    ...
```

Szabályok:

- A részösszeg az `egysegar * darabszam` értékek összege.
- Diák vásárló 15% kedvezményt kap.
- A promóciós kód százalékos kedvezményt jelent. Ha `None`, akkor nincs promóció.
- A kedvezmények összeadódnak, de összesen legfeljebb 60% lehet a kedvezmény.
- Ha a részösszeg legalább 80, a kezelési díj 0, különben 6.
- A végösszeg: részösszeg - kedvezmény + kezelési díj.
- Foglalási kódot csak akkor adj vissza, ha a `status` értéke `"confirmed"`, különben `None`.
- A foglalási kód formátuma: `"BOOKING-42 | Anna Kovacs"`.

Minden függvényhez kötelező docstring és legalább 2 doctest példa. A doctestek között legyen:

- üres tétellista,
- diákkedvezmény,
- promóciós kedvezmény,
- 60%-os kedvezményplafon,
- visszaigazolt és nem visszaigazolt foglalás.

---
