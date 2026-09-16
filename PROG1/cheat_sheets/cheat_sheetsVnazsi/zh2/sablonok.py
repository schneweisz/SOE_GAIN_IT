# ==========================================
# 1. TISZTA FÜGGVÉNYEK, DOCSTRING ÉS DOCTEST
# ==========================================

# Mindig használj típusjelölést (Type Hinting)!
def atlag_kiszamitasa(szamok: list[int]) -> float:
    """
    Egy mondatos leírás arról, mit csinál a függvény.
    
    A doctesthez mindig kell egy normál eset:
    >>> atlag_kiszamitasa([10, 20])
    15.0
    
    És egy szélsőérték (Edge case) eset (pl. mi van, ha üres?):
    >>> atlag_kiszamitasa([])
    0.0
    """
    if len(szamok) == 0:
        return 0.0
        
    # Ne írj for ciklust összegzésre, használd a beépített fgv-eket!
    return round(sum(szamok) / len(szamok), 2)


# ==========================================
# 2. HIBAKEZELÉS: AGRESSZÍV (KIVÉTEL DOBÁS)
# ==========================================

def esemeny_feldolgozo(sor: str) -> tuple[str, str, int]:
    """
    Agresszív hiba esetén a doctestben Traceback-et várunk el!
    
    >>> esemeny_feldolgozo("anna;kave;800")
    ('anna', 'kave', 800)
    >>> esemeny_feldolgozo("hibas_sor")
    Traceback (most recent call last):
    ...
    ValueError: Hibás formátum!
    """
    darabok = sor.strip().split(";")
    
    # 1. Hossz ellenőrzése
    if len(darabok) != 3:
        raise ValueError("Hibás formátum!")
        
    nev = darabok[0].strip()
    termek = darabok[1].strip()
    
    # 2. Típuskonverzió biztonságosan, hiba láncolással (from exc)
    try:
        ar = int(darabok[2].strip())
    except ValueError as exc:
        raise ValueError("Az ár nem szám!") from exc
        
    # Visszatérés Tuple-ként (NINCS print!)
    return nev, termek, ar


# ==========================================
# 3. HIBAKEZELÉS: CSENDES (VISSZATÉRÉS NONE-NAL)
# ==========================================

# Figyeld a fejlécet: | None jelzi, hogy None is lehet a vége!
def csendes_darabolo(sor: str) -> tuple[str, int] | None:
    """
    >>> csendes_darabolo("Anna:10")
    ('Anna', 10)
    >>> csendes_darabolo("hibas") is None
    True
    """
    darabok = sor.split(":")
    if len(darabok) != 2:
        return None  # Csendben kilépünk
        
    try:
        pont = int(darabok[1])
    except ValueError:
        return None  # Csendben kilépünk, ha nem szám
        
    return darabok[0], pont


# ==========================================
# 4. DUPLA SZÓTÁR (NESTED DICTIONARY) ÉPÍTÉSE
# ==========================================

def nagy_iratszekreny_epitese(sorok: list[str]) -> dict[str, dict[str, list[int]]]:
    """
    Felépít egy ilyen struktúrát: {'anna': {'Python': [12, 5]}}
    """
    tarolo: dict[str, dict[str, list[int]]] = {}
    
    for sor in sorok:
        # Tegyük fel, hogy a csendes_darabolo-t hívjuk
        eredmeny = csendes_darabolo(sor)
        
        # Ha a daraboló None-t adott vissza, ugorjuk át a sort!
        if eredmeny is None:
            continue
            
        nev, pont = eredmeny
        kurzus = "Python" # Tegyük fel, hogy ezt is kinyertük
        
        # A 3 LÉPÉSES SZÓTÁRÉPÍTÉS SZABÁLYA:
        
        # 1. Létezik-e a külső fiók (Név)?
        if nev not in tarolo:
            tarolo[nev] = {}
            
        # 2. Létezik-e a belső mappa (Kurzus)?
        if kurzus not in tarolo[nev]:
            tarolo[nev][kurzus] = []
            
        # 3. Érték (Pont) hozzáfűzése a listához
        tarolo[nev][kurzus].append(pont)
        
    return tarolo


# ==========================================
# 5. ÜZLETI LOGIKA ÉS GUARD CLAUSE (KORAI KILÉPÉS)
# ==========================================

def szallitasi_cimke(statusz: str, reszosszeg: float, kupon: float | None) -> str | None:
    """
    A feltételek gyors és elegáns szűrése.
    """
    # GUARD CLAUSE: Azonnal kidobjuk a nem kívánt eseteket
    if statusz != "paid":
        return None
        
    # NONE KEZELÉS egy sorban (Ternary operator)
    kupon_ertek = 0.0 if kupon is None else kupon
    
    # LIMITEK KEZELÉSE a min() és max() függvényekkel
    # Példa: A kedvezmény sosem lehet több 50%-nál (0.5)
    vegleges_kedvezmeny = min(kupon_ertek, 0.5)
    
    return "CIMKE-123"


# ==========================================
# 6. A MAIN.PY BEOLVASÓ CIKLUSA
# ==========================================
# Ezt SOHA ne rakd a logic.py-ba! 

def naplo_beolvasasa() -> list[str]:
    """Folyamatosan kér be sorokat a VEGE szóig."""
    sorok = []
    while True:
        # Itt van az egyetlen hely, ahol input() lehet!
        sor = input() 
        
        # strip() mindig kell az input után!
        if sor.strip() == "VEGE":
            break
            
        sorok.append(sor)
        
    return sorok