import os
import json
def print_kurzuseredmeny():
    """Bekéri a tárgy kódját és a félév nevét, majd kiírja a kurzus eredményeit.

    A kurzuseredményeket a következő formában írja ki:
    Tárgy neve: <tárgynév>
    Félév: <félév>
    Létszám: <létszám> fő
    Aláírást szerzett: <aláírás==1> fő
    Bukási arány: <százalék>%
    Átlag: <sum(érdemjegy)/létszám>
    Vizsgajegyek:
        <darab> elégtelen (1)
        <darab> elégséges (2)
        <darab> közepes (3)
        <darab> jó (4)
        <darab> jeles (5)
    """
    # TODO: tárgykód bekérése
    # ha nem található, akkor hibaüzenet és visszatérés
    targykod = input('Tárgykód: ')
    if not targykod:
        print("Tárgykód nem található.")
        return
    # TODO: félév bekérése
    # ha nem található, akkor hibaüzenet és visszatérés
    felev = input('Félév: ')
    if not felev:
        print("Félév nem található.")
        return
    
    # TODO: kurzuseredmények beolvasása
    filename = f"{targykod}_{felev}.json"
    if not os.path.exists(filename):
        print("Hibás oszlopok a fájlban.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except Exception:
        print("Hibás fájlformátum.")
        return
    # ha az oszlopok nem megfelelőek, akkor hibaüzenet és visszatérés
    required_keys = ['targyneve', 'alairas', 'vizsgajegyek']
    if not all(key in data for key in required_keys):
        print("Hibás oszlopok a fájlban.")
        return
    # TODO: kurzuseredmények kiszámítása
    targyneve = data['targyneve']
    alairas = data['alairas']
    vizsgajegyek = data['vizsgajegyek']

    letszam = len(vizsgajegyek)
    if letszam == 0:
        atlag = 0.0
    else:
        atlag = sum(vizsgajegyek) / letszam

    bukottak = vizsgajegyek.count(1)
    bukasi_arany = (bukottak / letszam * 100) if letszam > 0 else 0

    jegyek_szamlalo = {i: vizsgajegyek.count(i) for i in range(1, 6)}
    # ha a létszám 0, akkor az átlag legyen 0.0
    # TODO: kurzuseredmények kiírása
    print(f"Tárgy neve: {targyneve}")
    print(f"Félév: {felev}")
    print(f"Létszám: {letszam} fő")
    print(f"Aláírást szerzett: {alairas} fő")
    print(f"Bukási arány: {bukasi_arany:.2f}%")
    print(f"Átlag: {atlag:.2f}")
    print("Vizsgajegyek:")
    for jegy, darab in jegyek_szamlalo.items():
        print(f"    {darab} {'elégtelen' if jegy == 1 else 'elégséges' if jegy == 2 else 'közepes' if jegy == 3 else 'jó' if jegy == 4 else 'jeles'} ({jegy})")

