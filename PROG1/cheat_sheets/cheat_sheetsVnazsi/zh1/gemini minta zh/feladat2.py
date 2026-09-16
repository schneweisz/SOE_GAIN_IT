def tisztitas(szoveg:str):
    kis_szoveg = szoveg.lower()
    tiszta_szoveg = ""
    for karakter in kis_szoveg:
        if karakter.isalpha(): # A string beépített isalpha() metódusa használható
            tiszta_szoveg += karakter
        else:
            tiszta_szoveg += " "
    # A tisztított stringet szóközök mentén daraboljuk, hogy szavak listáját kapjuk
    return tiszta_szoveg.split()

def elemzes(szoveg):
    szotar = {}
    for szo in szoveg:
        if szo not in szotar:
            szotar[szo] = 1
        else:
            szotar[szo] += 1
    sorbaszotar = sorted(szotar.items(), key=lambda x: (-x[1], x[0]))
    return sorbaszotar [:3]


if __name__ == "__main__":
    szoveg = "Szuper, gyors! Nagyon szuper termek; gyors kiszallitas? Jo. 10/10 gyors!"
    
    print("--- 2. Feladat Teszt ---")
    
    # 1. Szöveg megtisztítása (csak betűk és szóközök maradhatnak)
    tiszta_lista = tisztitas(szoveg)
    print(tiszta_lista)
    
    # 2. Gyakoriság számolása és rendezése (Top 3)
    top_szavak = elemzes(tiszta_lista)
    
    # 3. Kiírás a kért formátumban
    for szo, darab in top_szavak:
        print(f"{szo} {darab}")