# Adott egy egyszerű “bolt”:
# - KESZLET: termékkód → (terméknév, ár)
# - KOSARAK: vásárló neve → a kosárban levő termékkódok listája (duplikátum lehet)
#
# FELADAT:
# 1) Számold ki minden vásárló kosarának végösszegét.
# 2) Add meg a TOP 3 legdrágább különböző terméket, amit bárki valaha kosárba tett.
# 3) Add meg azokat a termékkódokat, amiket MINDEN vásárló kosara tartalmaz.
# 4) Készíts olyan struktúrát, amiből gyorsan meg tudod mondani egy termékkódról,
#    hogy hányan tették kosárba (nem darabszám, hanem hány különböző vásárló).

KESZLET = {
    "A12": ("alma", 149),
    "B34": ("banán", 199),
    "C56": ("csoki", 499),
    "D78": ("tej", 349),
    "E90": ("kenyér", 399),
    "F11": ("sajt", 899),
}

KOSARAK = {
    "Anna": ["A12", "C56", "C56", "D78"],
    "Béla": ["B34", "D78", "E90"],
    "Csilla": ["A12", "B34", "F11"],
    "Dóri": ["A12", "D78", "E90", "F11"],
}


# --- Megoldás ---


def vegosszegek(keszlet, kosarak):
    # dict: vásárló -> összeg (gyors kulcs alapú tárolás/lekérdezés)
    osszegek = {}

    for vasarlo, kodok in kosarak.items():
        total = 0
        for kod in kodok:
            # készletből gyors lekérdezés: termékkód -> (név, ár)
            _, ar = keszlet[kod]
            total += ar
        osszegek[vasarlo] = total

    return osszegek


def top3_legdragabb_termek(keszlet, kosarak):
    # set: különböző termékkódok a kosarakból
    osszes_kod = set()
    for kodok in kosarak.values():
        for kod in kodok:
            osszes_kod.add(kod)

    # rendezés ár szerint
    rendezve = sorted(osszes_kod, key=lambda k: keszlet[k][1], reverse=True)
    return rendezve[:3]


def mindenkinek_benne_van(kosarak):
    # set metszet: mi van benne mindenkinek?
    metszet = None

    for kodok in kosarak.values():
        s = set(kodok)
        if metszet is None:
            metszet = s
        else:
            metszet &= s

    return metszet if metszet is not None else set()


def hanyan_tettek_kosarba(kosarak):
    # dict: termékkód -> set(vásárlók), ebből könnyű a “hányan?”
    termek_vasarlok = {}

    for vasarlo, kodok in kosarak.items():
        # itt a “különböző vásárló” számít, ezért a kosár-kódokat érdemes set-té tenni
        for kod in set(kodok):
            if kod not in termek_vasarlok:
                termek_vasarlok[kod] = set()
            termek_vasarlok[kod].add(vasarlo)

    # alakítsuk át számlálóra (kód -> db)
    db = {}
    for kod, vasarlok in termek_vasarlok.items():
        db[kod] = len(vasarlok)

    return db


def main():
    print("1) Végösszegek:")
    osszegek = vegosszegek(KESZLET, KOSARAK)
    for vasarlo in sorted(osszegek):
        print(f"- {vasarlo}: {osszegek[vasarlo]} Ft")

    print("\n2) Top 3 legdrágább (különböző) termék a kosarakból:")
    top3 = top3_legdragabb_termek(KESZLET, KOSARAK)
    for kod in top3:
        nev, ar = KESZLET[kod]
        print(f"- {kod}: {nev} ({ar} Ft)")

    print("\n3) Mindenkinek a kosarában szereplő termékek:")
    kozosek = mindenkinek_benne_van(KOSARAK)
    print(sorted(kozosek))

    print("\n4) Hány különböző vásárló tette kosárba (termékkód -> db):")
    db = hanyan_tettek_kosarba(KOSARAK)
    for kod in sorted(db):
        print(f"- {kod}: {db[kod]}")


if __name__ == "__main__":
    main()
