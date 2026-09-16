def tisztitas(szoveg:str):
    # 1. Kisbetűssé alakítjuk a teljes szöveget a feladatkiírás szerint
    tiszta = szoveg.lower()
    tiszta_szoveg = ""
    for karakter in tiszta:
        # 2. Csak a betűket tartjuk meg
        if karakter.isalpha():
            tiszta_szoveg += karakter #append nem mukodik mert nem listahoz fuzom hozza
        else:
            tiszta_szoveg += " " #ha nem az abc resze akkor szokozt fuzok hozza,hogy utana splittel konnyu dolgom legyen
            
    # 3. A szóközök mentén feldaraboljuk. A paraméter nélküli split() 
    # automatikusan eltávolítja a felesleges üres (dupla szóközös) elemeket is.
    return tiszta_szoveg.split()

def elemzes(szoveg):
    # Üres szótár a szavak gyakoriságának (darabszámának) tárolására
    gyumolcsok = {}
    for gyumolcs in szoveg:
        if gyumolcs not in gyumolcsok:
            gyumolcsok[gyumolcs] = 1
        else:
            gyumolcsok[gyumolcs] += 1
            
    # 1. lépés: Rendezzük a szótár elemeit (szó, darab) ABC sorrendbe a szó (x[0]) alapján.
    abcSorted = sorted(gyumolcsok.items(), key=lambda x: x[0])
    
    # 2. lépés: Az ABC szerint rendezett listát újrarendezzük darabszám (x[1]) szerint, csökkenő (reverse=True) sorrendben.
    # Mivel a Python rendezése "stabil", az azonos darabszámú szavak megtartják a korábbi ABC sorrendjüket.
    # A [:5] segítségével pedig csak az első 5 elemet (Top 5) adjuk vissza.
    return sorted(abcSorted, key=lambda x: x[1], reverse=True)[:5]


if __name__ == "__main__":
    szoveg ="""
    Alma, körte, alma! Sárga körte; alma? Banán.
    """
    tisztaszoveg = tisztitas(szoveg)
    eredmeny = elemzes(tisztaszoveg)
    
    # A kiírás formázása a feladat elvárásainak megfelelően
    # Mivel a függvény (szó, darab) tuple-öket ad vissza, ezeket kicsomagoljuk a for ciklusban
    for szo, darab in eredmeny:
        print(f"{szo} {darab}")