# 🧠 PROGRAMOZÁS 1 - 2. ZH TÚLÉLŐKÖNYV ÉS LOGIKAI VÁZLAT (CLEAN CODE)

## 1. Döntési fa: Hogyan induljak el, ha meglátok egy feladatot?

Ne kezdj el azonnal kódolni! Futtaszt le ezt a 4 kérdést a fejedben:

1. **Melyik fájlban vagyok éppen? (Kiírás vs. Logika)**
   - Ha a `main.py`-ban vagyok: Itt használhatok `input()`-ot és `print()`-et. Csak hívom a szerszámokat.
   - Ha a `logic.py` (vagy `feladatX.py`) fájlban vagyok: **SZIGORÚAN TILOS** az `input()` és a `print()`. Mindent paraméterként kapok (`def fgv(adat):`), és mindent `return`-nel adok vissza.

2. **Mi a függvény egyetlen, jól körülhatárolt feladata? (Single Responsibility)**
   - Csak vizsgálni kell (pl. üres-e a sor)? -> `return bool` (Igaz/Hamis).
   - Darabolni kell egy sort? -> `return tuple` (Több adat visszaadása egyszerre).
   - Összesíteni kell egy listát? -> `return dict` (Szótárépítés).
   - _Szabály:_ Ne csinálj szótárépítést és darabolást egyetlen függvényen belül!

3. **Hogyan kell kezelnem a hibás adatokat? (Agresszív vs. Csendes)**
   - Kéri a feladat, hogy álljon le a program hibával? -> `raise ValueError("Hibaüzenet")`
   - Kéri, hogy csak hagyjuk figyelmen kívül? -> `try... except ValueError: return None`

4. **Hogyan fogom ezt letesztelni? (Doctest dizájn)**
   - Mielőtt megírod a logikát, írd meg a docstringben (`"""..."""`), hogy:
     1. Mi a normál kimenet?
     2. Mi történik, ha üres az adat?
     3. Mi történik, ha hibás az adat?

---

## 2. A 4 Leggyakoribb 2. ZH Programozási Minta

### A) A "Szigorú Ajtónálló" (Validáció & Kivétel dobás)

- **Tipikus feladat:** "Egy eseménysor akkor érvényes, ha pontosan három része van... Hibásan formázott sornál dobj ValueError kivételt."
- **Stratégia:** 1. Darabolás (`.split()`). 2. Hossz ellenőrzése (`if len(darabok) != 3: raise ValueError(...)`). 3. Típuskonverzió (`int()`) egy `try... except` blokkban, de itt a `except` ágban is `raise ValueError(...)` következik, egy `from exc` láncolással.

### B) A "Csendes Takarító" (Biztonságos Darabolás)

- **Tipikus feladat:** "Hibásan formázott sort hagyj figyelmen kívül, ne dobj kivételt... térj vissza None értékkel."
- **Stratégia:** Ugyanaz a darabolás, de itt a `raise` helyett `return None` áll. A hívó függvény (a ciklus) pedig így kezeli:
  `eredmeny = fuggveny(sor)`
  `if eredmeny is None: continue`

### C) A "Nagy Iratszekrény" (Dupla szótár építése)

- **Tipikus feladat:** "Naplósorokból felhasználó-kurzus-pontlista szerkezetet készít." (`dict[str, dict[str, list[int]]]`)
- **Stratégia:** Ne ess pánikba a mérettől, haladj lépésről lépésre:
  1. `if felhasznalo not in tarolo: tarolo[felhasznalo] = {}` (Nagy fiók nyitása)
  2. `if kurzus not in tarolo[felhasznalo]: tarolo[felhasznalo][kurzus] = []` (Mappa nyitása a fiókban)
  3. `tarolo[felhasznalo][kurzus].append(pont)` (Lap betétele a mappába)

### D) Az "Üzleti Logika" (Guard Clause és Limitek)

- **Tipikus feladat:** "Szállítási címkét csak akkor adj vissza, ha fizetve van... Kedvezmény maximum 50% lehet."
- **Stratégia:** - _Korai kilépés (Guard Clause):_ `if status != "paid": return None`. Ezzel megúszod a felesleges `else` ágakat.
  - _Biztonságos számolás (Limitek):_ Használd a beépített függvényeket: `kedvezmeny = min(kiszamitott_kedvezmeny, 0.5)`. Így sosem lépi túl a plafont.

---

## 3. A Leggyakoribb ZH Hibák (Erre figyelj!)

- **A Robot Tanár (Doctest) nem bocsát meg:** Ha a docstringben a tesztnél a szöveg `"Alma"`, te pedig `"alma"`-t írsz, elbukik a teszt. Ha egy szóköz lemarad a `Traceback` vagy a `ValueError` körül, elbukik a teszt. Másolj pontosan!
- **A `None` típus elfelejtése a típusjelzésnél (Type Hint):** Ha egy függvény visszatérhet egy tuple-lel VAGY egy `None`-nal (ha hiba volt), kötelező kitenni a `| None` jelzést a fejlécbe: `-> tuple[str, int] | None`.
- **Lokális vs. Globális adatok:** A függvények "csőlátásúak". Csak azt az adatot látják, amit a kerek zárójelben beadtál nekik. Soha ne próbálj egy függvényen belül hivatkozni egy olyan változóra, ami a `main.py`-ban lett létrehozva, kivéve ha átadtad paraméterként!
- **Listák és halmazok (Set) keverése:** Ha azt kérik, "hány _különböző_ kurzust végzett", akkor a listát halmazzá kell alakítani (`set(lista)`), vagy az alapoktól halmazt (`set()`) kell építeni, hogy a duplikátumok eltűnjenek.
- **`sum()` és `len()` újrafeltalálása:** Ne írj `for` ciklust egy lista elemeinek összeadásához vagy megszámlálásához! Használd a beépített `sum(lista)` és `len(lista)` függvényeket.
