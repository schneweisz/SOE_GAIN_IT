import os

def select_targy() -> str:
    """Tárgy kiválasztása felsorolásból.

    Listázza ki sorszámozva a tárgyak neveit és tárgykódjait (név szerint ábécésorrendben),
    kérjen be egy sorszámot, és adja vissza kiválasztott tárgy kódját.
    """
    print("Tantárgyak:")
    targyak = {}

    try:
        targyak_list = os.listdir("targyak")
    except FileNotFoundError:
        print("Hiba: A 'targyak' mappa nem található.")
        return ""

    for idx, targy in enumerate(sorted(targyak_list), start=1):
        if os.path.isdir(f"targyak/{targy}"):
            targyak[idx] = targy
            print(f"{idx}: {targy}")

    while True:
        try:
            n = int(input("Adja meg a tantárgy sorszámát: "))
            if n in targyak:
                return targyak[n]
            else:
                print("Érvénytelen sorszám! Próbálja újra.")
        except ValueError:
            print("Kérem, csak számot adjon meg!")


def select_targy_felev(targy) -> str:
    """Tárgy félévének kiválasztása felsorolásból.

    Listázza ki sorszámozva a megadott tárgy féléveinek neveit (időrendi sorrendben),
    kérjen be egy sorszámot, és adja vissza kiválasztott félév nevét.
    """
    print("Félévek:")
    felevek = {}

    try:
        felev_list = os.listdir(f"targyak/{targy}")
    except FileNotFoundError:
        print(f"Hiba: A '{targy}' tárgyhoz nem találhatók félévek.")
        return ""

    for idx, felev in enumerate(sorted(felev_list), start=1):
        if felev.endswith(".csv"):
            felevek[idx] = felev[:-4]
            print(f"{idx}: {felev[:-4]}")

    while True:
        try:
            n = int(input("Adja meg a félév sorszámát: "))
            if n in felevek:
                return felevek[n]
            else:
                print("Érvénytelen sorszám! Próbálja újra.")
        except ValueError:
            print("Kérem, csak számot adjon meg!")


def print_kurzuseredmeny():
    """Bekéri a tárgy kódját és a félév nevét, majd kiírja a kurzus eredményeit."""
    targy = select_targy()
    if not targy:
        return

    felev = select_targy_felev(targy)
    if not felev:
        return

    try:
        with open(f"targyak/{targy}/{felev}.csv", "r", encoding="utf8") as f:
            lines = f.readlines()

        header = lines[0].strip().split(",")
        if "neptun" not in header or "aláírás" not in header or "vizsgajegy" not in header:
            print("Hibás oszlopok a fájlban.")
            return

        neptun_idx = header.index("neptun")
        alairas_idx = header.index("aláírás")
        vizsgajegy_idx = header.index("vizsgajegy")

        jegyek = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
        }
        osszes_eredmeny = 0
        alairas_szerzett = 0
        letszam = 0

        for line in lines[1:]:
            row = line.strip().split(",")
            letszam += 1
            if row[alairas_idx] == "1":
                alairas_szerzett += 1
            vizsgajegy = int(row[vizsgajegy_idx])
            osszes_eredmeny += vizsgajegy
            jegyek[str(vizsgajegy)] += 1

        if letszam == 0:
            atlag = 0.0
            bukasi_arany = 0.0
        else:
            atlag = osszes_eredmeny / letszam
            bukasi_arany = (jegyek["1"] / letszam) * 100

        print(f"Tárgy neve: {targy}")
        print(f"Félév: {felev}")
        print(f"Létszám: {letszam} fő")
        print(f"Aláírást szerzett: {alairas_szerzett} fő")
        print(f"Bukási arány: {bukasi_arany:.2f}%")
        print(f"Átlag: {atlag:.2f}")
        print("Vizsgajegyek:")
        print(f"{jegyek['1']} elégtelen (1)")
        print(f"{jegyek['2']} elégséges (2)")
        print(f"{jegyek['3']} közepes (3)")
        print(f"{jegyek['4']} jó (4)")
        print(f"{jegyek['5']} jeles (5)")

    except FileNotFoundError:
        print(f"Hiba: A '{felev}.csv' fájl nem található a '{targy}' tárgyhoz.")
    except ValueError as e:
        print(f"Hiba az adatok feldolgozása közben: {e}")

    # az alábbiakhoz felhasználható a múlt heti házi megoldása:

    # TODO: kurzuseredmények beolvasása
    # ha az oszlopok nem megfelelőek, akkor hibaüzenet és visszatérés
    print("Hibás oszlopok a fájlban.")
    # TODO: kurzuseredmények kiszámítása
    # ha a létszám 0, akkor az átlag legyen 0.0
    # TODO: kurzuseredmények kiírása
