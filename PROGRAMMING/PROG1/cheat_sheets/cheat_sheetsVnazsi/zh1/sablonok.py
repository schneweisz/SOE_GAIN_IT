# ==========================================
# 1. ALAPVETŐ BEOLVASÁS ÉS SZŰRÉS (Folyosó-ellenőr)
# ==========================================

nyers_adatok = """
anna;15
bela;-5

VEGE
cili;20
"""

# Soronkénti beolvasás stringből (a strip eltávolítja a külső \n-eket)
for sor in nyers_adatok.strip().split("\n"):
    
    # Belső tisztítás (láthatatlan szóközök, enterek levágása)
    tiszta_sor = sor.strip()
    
    # Korai kilépés 1: Üres sorok átugrása
    if not tiszta_sor:
        continue
        
    # Korai kilépés 2: Végjel figyelése
    if tiszta_sor == "VEGE":
        break
        
    # Adatok szétvágása és biztonságos kicsomagolása
    reszek = tiszta_sor.split(";")
    nev = reszek[0]
    
    # Típuskonverzió (Mindig castolj, ha számmal fogsz dolgozni!)
    pont = int(reszek[1])
    
    # Korai kilépés 3: Hibás adat (pl. negatív pontszám) kiszűrése
    if pont < 0:
        continue
        

# ==========================================
# 2. ADATSZERKEZETEK ÉPÍTÉSE ÉS AGGREGÁLÁS
# ==========================================

gyujto_lista = {}  # Dict-of-Lists (Minden eseményt megőrzünk)
gyujto_halmaz = {} # Dict-of-Sets (Csak egyedi eseményeket őrzünk meg)
osszesito = {}     # Gyakoriság vagy összeg (Könyvelő)

# A) Hozzáadás LISTÁHOZ (Postázó minta)
if nev not in gyujto_lista:
    gyujto_lista[nev] = []         # Ha nincs még fiókja, csinálunk egy üres listát
gyujto_lista[nev].append(pont)     # Beletesszük az adatot

# B) Hozzáadás HALMAZHOZ
if nev not in gyujto_halmaz:
    gyujto_halmaz[nev] = set()     # Ugyanez, csak halmazzal
gyujto_halmaz[nev].add("cikk_id")  # Halmaznál .add() a parancs, nem append!

# C) Számlálás / Összegzés (Könyvelő minta)
if nev not in osszesito:
    osszesito[nev] = 0             # Kezdőérték beállítása
osszesito[nev] += 1                # Növeljük 1-gyel (vagy a pont értékével)


# ==========================================
# 3. BIZTONSÁGOS LEKÉRDEZÉS ÉS HALMAZMŰVELETEK
# ==========================================

# .get() használata KeyError elkerülésére (ha a kulcs nincs a szótárban, üres halmazt ad)
anna_cikkeinek_halmaza = gyujto_halmaz.get("anna", set())
bela_cikkeinek_halmaza = gyujto_halmaz.get("bela", set())

# A két halmaz metszete (közös elemek)
kozos_elemek = anna_cikkeinek_halmaza & bela_cikkeinek_halmaza

# A két halmaz uniója (összes előforduló egyedi elem)
osszes_egyedi = anna_cikkeinek_halmaza | bela_cikkeinek_halmaza

# Halmaz (vagy lista, szótár) elemeinek száma
darabszam = len(kozos_elemek)


# ==========================================
# 4. RENDEZÉS ÉS TOP N KIVÁLASZTÁS (A Dobogó)
# ==========================================

pontszamok = {"anna": 15, "bela": 20, "cili": 15}

# Szótár iterálása (kulcs és érték egyszerre a .items() segítségével)
for nev, pont in pontszamok.items():
    pass

# TÖBBSZEMPONTOS RENDEZÉS 
# Feladat: Elsődlegesen pont alapján csökkenő, másodlagosan név (ABC) alapján növekvő

# Megoldás 1: Kétlépcsős (stabil) rendezés (A legbiztonságosabb módszer)
# Első lépés: Másodlagos szempont (ABC növekvő)
abc_rendben = sorted(pontszamok.items(), key=lambda x: x[0])
# Második lépés: Elsődleges szempont (Pont alapján csökkenő -> reverse=True)
vegleges_rend = sorted(abc_rendben, key=lambda x: x[1], reverse=True)

# Megoldás 2: A "Mínusz trükk" egy sorban (CSAK SZÁMOKNÁL MŰKÖDIK!)
gyors_rend = sorted(pontszamok.items(), key=lambda x: (-x[1], x[0]))

# Listavágás (Slicing): Csak a Top 2 elem megtartása
top_ketto = vegleges_rend[:2]


# ==========================================
# 5. ADATTISZTÍTÁS ÉS SZÖVEGFELDOLGOZÁS
# ==========================================

piszkos_szoveg = "Alma, körte! 123"
tiszta_szoveg = ""

# A .lower() kisbetűssé tesz mindent
for karakter in piszkos_szoveg.lower():
    
    # A .isalpha() megmondja, hogy a karakter az ABC betűje-e
    # További hasznosak: .isdigit() -> szám-e?
    if karakter.isalpha():
        tiszta_szoveg += karakter
    else:
        # A nem betű karaktereket (szám, írásjel) SZÓKÖZRE cseréljük (sosem simán töröljük!)
        tiszta_szoveg += " "

# A .split() paraméter nélkül automatikusan a szóközök mentén vág,
# és ami a legjobb: LENYELI a felesleges / ismétlődő szóközöket!
szavak_listaja = tiszta_szoveg.split() 