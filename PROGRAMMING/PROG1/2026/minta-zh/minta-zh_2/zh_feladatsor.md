# Programozás 1 - ZH 2 minta

Időtartam: 120 perc  
Összpontszám: 100 pont

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
python -m doctest -v feladat3.py
python -m doctest -v feladat4.py
```

---

## 1. Tanulmányi rendszer naplófeldolgozás

Készíts programot, amely kurzusokhoz tartozó pontszerzési eseményeket dolgoz fel. A feladat lényege nem csak a helyes eredmény, hanem a szépen felbontott, tesztelhető logika.

A bemenet több sorból áll. Minden eseménysor pontosvesszővel elválasztva tartalmazza:

```text
felhasznalonev;kurzus;pont
```

A bemenet eseményrésze a `VEGE` sorig tart. Ezután egy külön sorban két felhasználónév érkezik szóközzel elválasztva. A programnak ezt a két felhasználót kell összehasonlítania.

Példa bemenet:

```text
anna;Python;12
bela;Python;8
anna;Web;15
anna;Python;5
csilla;Adatbazis;10
bela;Web;20
bela;Python;7
anna;Adatbazis;0
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

def esemeny_sor_feldolgozasa(sor: str) -> tuple[str, str, int]:
    ...

def felhasznalok_sora_feldolgozasa(sor: str) -> tuple[str, str]:
    ...

def naplo_feldolgozasa(sorok: list[str]) -> dict[str, dict[str, list[int]]]:
    ...

def felhasznalo_pontjai(tarolo: dict[str, dict[str, list[int]]], felhasznalo: str) -> list[int]:
    ...

def felhasznalo_kurzusai(tarolo: dict[str, dict[str, list[int]]], felhasznalo: str) -> set[str]:
    ...

def atlag(pontok: list[int]) -> float:
    ...

def statisztika_keszitese(tarolo: dict[str, dict[str, list[int]]], u1: str, u2: str) -> dict[str, object]:
    ...

def statisztika_szovegge(statisztika: dict[str, object]) -> str:
    ...
```

Kötelező doctest az alábbi függvényekhez:

- `ures_sor_e`
- `vege_sor_e`
- `esemeny_sor_feldolgozasa`
- `felhasznalok_sora_feldolgozasa`
- `naplo_feldolgozasa`
- `felhasznalo_pontjai`
- `felhasznalo_kurzusai`
- `atlag`
- `statisztika_keszitese`

### Doctest minták

A saját docstringjeidben ehhez hasonló példák szerepeljenek:

```python
def esemeny_sor_feldolgozasa(sor: str) -> tuple[str, str, int]:
    """
    Feldolgoz egy 'felhasznalo;kurzus;pont' formátumú sort.

    >>> esemeny_sor_feldolgozasa("anna;Python;12")
    ('anna', 'Python', 12)
    >>> esemeny_sor_feldolgozasa(" anna ; Web ; 5 ")
    ('anna', 'Web', 5)
    >>> esemeny_sor_feldolgozasa("hibas sor")
    Traceback (most recent call last):
    ...
    ValueError: Hibásan formázott eseménysor
    """
```

Nem kell pontosan ugyanez a hibaüzenet, de hibás bemenetre a doctest mutassa, hogy `ValueError` keletkezik.

### A `main.py` feladata

- olvassa be az eseménysorokat `VEGE`-ig,
- olvassa be a két összehasonlítandó felhasználónevet,
- hívja meg a `logic.py` megfelelő függvényeit,
- írja ki a statisztikát.

A `main.py`-ban nem kell doctest, ha csak beolvasást és kiírást tartalmaz.

### Feldolgozási szabályok

- Az üres sorokat hagyd figyelmen kívül.
- Egy eseménysor akkor érvényes, ha pontosan három része van: felhasználónév, kurzus, pont.
- A felhasználónév és a kurzus nem lehet üres.
- A pont egész számmá alakítható legyen.
- Hibásan formázott eseménysornál dobj `ValueError` kivételt.
- Egy felhasználónak egy kurzushoz több pontszáma is lehet.
- Ha egy felhasználó nem szerepel a naplóban, akkor a pontlistája üres lista, a kurzushalmaza üres halmaz legyen.

### Kimenet

A statisztika az alábbi sorokat tartalmazza ebben a sorrendben:

```text
u1_osszpont=32
u2_osszpont=35
u1_kurzus_db=3
u2_kurzus_db=2
kozos_kurzus_db=2
osszes_kurzus_db=3
u1_atlag=8.0
u2_atlag=11.67
jobb_felhasznalo=bela
```

Az átlagot két tizedesjegyre kerekítsd. Ha egy felhasználónak nincs pontja, az átlaga legyen `0.0`. Ha a két összpont egyenlő, a `jobb_felhasznalo` értéke legyen `dontetlen`.

---

## 2. Jelszóellenőrző modul doctesttel

Készíts `feladat2.py` néven modult, benne az alábbi függvényekkel:

```python
def tartalmaz_szamot(text: str) -> bool:
    ...

def tartalmaz_nagybetut(text: str) -> bool:
    ...

def password_strength(password: str) -> str:
    ...
```

Szabályok:

- A `tartalmaz_szamot` akkor adjon `True`-t, ha a szövegben van legalább egy számjegy.
- A `tartalmaz_nagybetut` akkor adjon `True`-t, ha a szövegben van legalább egy nagybetű.
- A `password_strength` visszatérési értéke:
  - `"weak"`, ha a jelszó rövidebb mint 8 karakter,
  - `"medium"`, ha legalább 8 karakter, de nincs benne szám vagy nincs benne nagybetű,
  - `"strong"`, ha legalább 8 karakter, van benne szám és van benne nagybetű.

Minden függvényhez kötelező docstring és legalább 3 doctest példa. Legyen köztük üres sztringes vagy határértékes példa is.
---

## 3. Rendelés feldolgozása tiszta függvényekkel

Készíts `feladat3.py` néven modult. Egy rendelés tételei ilyen tuple-ok:

```python
OrderItem = tuple[str, float, int]
# név, egységár, darabszám
```

Készítsd el az alábbi függvényeket:

```python
def calculate_subtotal(items: list[OrderItem]) -> float:
    ...

def calculate_discount(items: list[OrderItem], is_vip: bool, coupon_percent: float | None) -> float:
    ...

def calculate_final_total(items: list[OrderItem], is_vip: bool, coupon_percent: float | None) -> float:
    ...

def build_shipping_label(order_id: int, customer_name: str, status: str) -> str | None:
    ...
```

Szabályok:

- A részösszeg az `egysegar * darabszam` értékek összege.
- VIP vásárló 10% kedvezményt kap.
- A kupon százalékos kedvezményt jelent. Ha `None`, akkor nincs kupon.
- A kedvezmények összeadódnak, de összesen legfeljebb 50% lehet a kedvezmény.
- Ha a részösszeg legalább 100, a szállítás ingyenes, különben 12.
- A végösszeg: részösszeg - kedvezmény + szállítás.
- Szállítási címkét csak akkor adj vissza, ha a `status` értéke `"paid"`, különben `None`.
- A címke formátuma: `"ORDER-42 | Anna Kovacs"`.

Minden függvényhez kötelező docstring és legalább 2 doctest példa. A doctestek között legyen:

- üres tétellista,
- VIP kedvezmény,
- kuponkedvezmény,
- 50%-os kedvezményplafon,
- fizetett és nem fizetett rendelés.

---

## 4.Kódminőség és javítás

Készíts `feladat4.py` néven modult. Az alábbi kód működik, de rosszul strukturált, nehezen tesztelhető és nincs dokumentálva. Írd át úgy, hogy tiszta függvényekből álljon, legyenek hozzá docstringek és doctestek.

Kiinduló kód:

```python
adatok = ["Anna:10", "Bela:7", "Cecil:12", "Anna:5", "hibas", "Bela:3"]

ossz = {}
for sor in adatok:
    if ":" in sor:
        nev = sor.split(":")[0]
        pont = int(sor.split(":")[1])
        if nev not in ossz:
            ossz[nev] = 0
        ossz[nev] += pont

print(ossz)
```

Elvárt függvények:

```python
def pont_sor_feldolgozasa(sor: str) -> tuple[str, int] | None:
    ...

def pontok_osszegzese(sorok: list[str]) -> dict[str, int]:
    ...
```

Szabályok:

- A `"Nev:pont"` formátumú sorokat dolgozd fel.
- Hibásan formázott sort hagyj figyelmen kívül, ne dobj kivételt.
- Ha a pont nem alakítható egész számmá, a sort hagyd figyelmen kívül.
- Az azonos nevek pontjait add össze.
- Mindkét függvényhez legyen docstring és legalább 3 doctest példa.
