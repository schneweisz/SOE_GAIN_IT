def tisztitas(szoveg:str):
    kis_szoveg = szoveg.lower()
    tiszta_szoveg = ""
    for karakter in kis_szoveg:
        if karakter.isalpha():
            tiszta_szoveg += karakter
        else:
            tiszta_szoveg += " "
    return tiszta_szoveg.split()

def elemzes(szoveg):
    szotar = {}
    for szo in szoveg:
        if szo not in szotar:
            szotar[szo] = 1
        else:
            szotar[szo] += 1
    sorbaszotar = sorted(szotar.items(), key= lambda x: (-x[1], x[0]))  #ha a szamok - erteket nezem akkor nem kell 2szer sortolni
    return sorbaszotar [:5]






if __name__ == "__main__":
    szoveg = """
    Hiba: Kijelentkezés! hiba... Újra-belépés? BELÉPÉS 2026/03/30.
    """
    tiszta_lista = tisztitas(szoveg)
    #print(tiszta_lista)

    top_szavak = elemzes(tiszta_lista)

    for szo, darab in top_szavak:
        print(f"{szo} {darab}")