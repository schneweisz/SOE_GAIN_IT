def darabolas(adatok:str):
    sorok = adatok.strip().split("\n")
    naplo = {}
    diakok = sorok[-1].strip().split()
    diak1=diakok[0]
    diak2=diakok[1]
    for sor in sorok:
        tiszta_sor = sor.strip()
        # A feldolgozást a VEGE sornál abbahagyjuk
        if tiszta_sor == "VEGE":
            break
        # Csak azokat a sorokat dolgozzuk fel, amik adatot tartalmaznak (pontosvesszővel),
        # így elkerüljük a hibát a diákneveket tartalmazó sornál.
        if ";" in tiszta_sor:
            adat = tiszta_sor.split(";")
            nev = adat[0]
            konyv = adat[1]
            if nev not in naplo:
                naplo[nev] = set()
            naplo[nev].add(konyv)
    return naplo, diak1, diak2

def elemzes(szotar:dict, diak1, diak2):
    set1 = szotar.get(diak1, set())
    set2 = szotar.get(diak2, set())
    return len(set1), len(set2), len(set1 & set2), len(set1 | set2)
if __name__ == "__main__":
    adatok = """
    gabor;gyuruk-ura
    gabor;harry-potter
    gabor;gyuruk-ura
    lilla;harry-potter
    lilla;vajak
    zoli;dune
    VEGE
    gabor lilla
    """
    
    print("--- 1. Feladat Teszt ---")
    
    # 1. Beolvasás és feldarabolás
    szotar, diak1, diak2 = darabolas(adatok)

    # 2. Elemzés elvégzése
    d1_db, d2_db, kozos, osszes = elemzes(szotar, diak1, diak2)
    
    # 3. Kiírás a feladat által kért formátumban
    print(f"diak1_egyedi_db={d1_db}")
    print(f"diak2_egyedi_db={d2_db}")
    print(f"kozos_db={kozos}")
    print(f"osszes_db={osszes}")
