def darabolas(adatok):
    """
    A bemeneti stringet feldolgozza és egy szótár adatszerkezetet, valamint
    két felhasználónevet ad vissza.
    """
    # A bemeneti szöveget sorokra bontjuk, és a felesleges szóközöket eltávolítjuk.
    sorok = adatok.strip().split("\n")
    
    # Létrehozunk egy üres szótárat, ahol a felhasználók által nézett cikkeket tároljuk.
    # A struktúra: {'felhasználónév': {'cikk1', 'cikk2'}, ...}
    felhasznalok = {}
    
    # Az utolsó sor tartalmazza a két összehasonlítandó felhasználót, szóközzel elválasztva.
    # Kiolvassuk őket.
    userek = sorok[-1].strip().split(" ")
    u1 = userek[0]
    u2 = userek[1]
    
    # Ciklussal végigmegyünk az összes soron.
    for sor in sorok:
        # Eltávolítjuk a sor elejéről/végéről a felesleges whitespace karaktereket.
        tiszta_sor = sor.strip()
        # Ha a sor üres, ugorjuk át.
        if not tiszta_sor:
            continue
        # Ha elérjük a "VEGE" jelet, a feldolgozásnak vége, kilépünk a ciklusból.
        if tiszta_sor == "VEGE":
            break
        else:
            # A sort a pontosvessző mentén kettévágjuk.
            adat = tiszta_sor.split(";")
            nev = adat[0]
            cikk = adat[1]
            # Ha a felhasználó még nem szerepel a szótárban, létrehozunk neki egy bejegyzést egy üres halmazzal.
            if nev not in felhasznalok:
                felhasznalok[nev] = set()
            # Hozzáadjuk a cikket a felhasználóhoz tartozó halmazhoz.
            # A halmaz (set) automatikusan biztosítja, hogy minden cikk csak egyszer szerepeljen.
            felhasznalok[nev].add(cikk)
            
    # Visszaadjuk a kész szótárat és a két kiolvasott felhasználónevet.
    return felhasznalok, u1, u2

def elemzes(szotar, nev1, nev2):
    """
    Két felhasználó böngészési szokásait elemzi a kapott szótár alapján.
    Meghatározza a megtekintett egyedi cikkek számát, a közös cikkeket és az összes cikket.
    """
    # Lekérjük a felhasználók halmazait (ha nem létezik, üres halmazt kapunk)
    set1 = szotar.get(nev1, set())
    set2 = szotar.get(nev2, set())
    
    # Kiszámoljuk a kért értékeket
    return len(set1), len(set2), len(set1 & set2), len(set1 | set2)
    # A `&` a metszet (intersection), a `|` pedig az unió (union) operátora



if __name__ == "__main__":
    adatok = """
    anna;python-alapok
    anna;dict-es-set
    anna;python-alapok
    bela;python-alapok
    bela;fajlkezeles
    cili;dict-es-set
    VEGE
    anna bela
    """
    # Főprogram: a szkript belépési pontja.
    print("1.feladat \n")
    
    # 1. Lépés: A nyers adatok feldolgozása a 'darabolas' függvénnyel.
    szotar, u1, u2 = darabolas(adatok)
    print("Szótár:", szotar)
    print("Felhasználók:", u1, u2)
    print("-"*40,"\n")
    
    # 2. Lépés: Az elemzés elvégzése a 'darabolas' által visszaadott adatokon.
    u1_db, u2_db, kozos, osszes = elemzes(szotar, u1, u2)
    
    # 3. Lépés: Az eredmények kiíratása a képernyőre a feladatban kért formátumban.
    print(f"u1_egyedi_db={u1_db}")
    print(f"u2_egyedi_db={u2_db}")
    print(f"kozos_db={kozos}")
    print(f"osszes_db={osszes}")