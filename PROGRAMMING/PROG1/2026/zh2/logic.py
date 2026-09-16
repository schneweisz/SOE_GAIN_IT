NaploTarolo = dict[str, dict[str, list[int]]]


def ures_sor_e(sor: str) -> bool:
    """
    Eldönti, hogy a sor üres-e vagy csak whitespace karaktereket tartalmaz-e.

    >>> ures_sor_e("")
    True
    >>> ures_sor_e("   ")
    True
    >>> ures_sor_e("anna;Dune;14")
    False
    """
    return sor.strip() == ""


def vege_sor_e(sor: str) -> bool:
    """
    Eldönti, hogy a sor a bemenet végét jelöli-e.

    >>> vege_sor_e("VEGE")
    True
    >>> vege_sor_e("  VEGE  ")
    True
    >>> vege_sor_e("vege")
    False
    """
    return sor.strip() == "VEGE"


def kolcsonzes_sor_feldolgozasa(sor: str) -> tuple[str, str, int]:
    """
    Feldolgoz egy 'olvaso;konyv;napok' formátumú sort.

    >>> kolcsonzes_sor_feldolgozasa("anna;Dune;14")
    ('anna', 'Dune', 14)
    >>> kolcsonzes_sor_feldolgozasa(" bela ; Solaris ; 12 ")
    ('bela', 'Solaris', 12)
    >>> kolcsonzes_sor_feldolgozasa("hibas sor")
    Traceback (most recent call last):
    ...
    ValueError: Hibásan formázott kölcsönzési sor
    >>> kolcsonzes_sor_feldolgozasa("anna;Dune;-5")
    Traceback (most recent call last):
    ...
    ValueError: Negatív napszám
    """
    darabok = sor.strip().split(";")
    if len(darabok) != 3:
        raise ValueError("Hibásan formázott kölcsönzési sor")

    olvaso = darabok[0].strip()
    konyv = darabok[1].strip()
    nap_szoveg = darabok[2].strip()

    if not olvaso or not konyv:
        raise ValueError("Hiányos eseménysor")

    try:
        napok = int(nap_szoveg)
    except ValueError as exc:
        raise ValueError("A napok száma nem egész szám") from exc

    if napok < 0:
        raise ValueError("Negatív napszám")

    return olvaso, konyv, napok


def olvasok_sora_feldolgozasa(sor: str) -> tuple[str, str]:
    """
    Két olvasónevet olvas ki egy szóközzel tagolt sorból.

    >>> olvasok_sora_feldolgozasa("anna bela")
    ('anna', 'bela')
    >>> olvasok_sora_feldolgozasa("  anna   bela  ")
    ('anna', 'bela')
    >>> olvasok_sora_feldolgozasa("anna")
    Traceback (most recent call last):
    ...
    ValueError: Pontosan két olvasónevet kell megadni
    """
    darabok = sor.strip().split()
    if len(darabok) != 2:
        raise ValueError("Pontosan két olvasónevet kell megadni")
    return darabok[0], darabok[1]


def naplo_feldolgozasa(sorok: list[str]) -> NaploTarolo:
    """
    Naplósorokból olvasó-könyv-napok lista szerkezetet készít.

    >>> naplo_feldolgozasa(["anna;Dune;14", "anna;Dune;5", "bela;Solaris;12"])
    {'anna': {'Dune': [14, 5]}, 'bela': {'Solaris': [12]}}
    >>> naplo_feldolgozasa(["", "  ", "anna;Solaris;0"])
    {'anna': {'Solaris': [0]}}
    >>> naplo_feldolgozasa([])
    {}
    """
    tarolo: NaploTarolo = {}
    for sor in sorok:
        if ures_sor_e(sor):
            continue

        olvaso, konyv, napok = kolcsonzes_sor_feldolgozasa(sor)
        if olvaso not in tarolo:
            tarolo[olvaso] = {}
        if konyv not in tarolo[olvaso]:
            tarolo[olvaso][konyv] = []
        tarolo[olvaso][konyv].append(napok)

    return tarolo


def olvaso_napjai(tarolo: NaploTarolo, olvaso: str) -> list[int]:
    """
    Visszaadja egy olvasó összes kölcsönzési napját listában.

    >>> t = {'anna': {'Dune': [14, 5], 'Solaris': [10]}}
    >>> olvaso_napjai(t, "anna")
    [14, 5, 10]
    >>> olvaso_napjai(t, "bela")
    []
    """
    konyvek = tarolo.get(olvaso, {})
    napok: list[int] = []
    for konyv_napok in konyvek.values():
        napok.extend(konyv_napok)
    return napok


def olvaso_konyvei(tarolo: NaploTarolo, olvaso: str) -> set[str]:
    """
    Visszaadja az olvasó által kikölcsönzött egyedi könyvek halmazát.

    >>> t = {'anna': {'Dune': [14, 5], 'Solaris': [10]}}
    >>> olvaso_konyvei(t, "anna") == {'Dune', 'Solaris'}
    True
    >>> olvaso_konyvei(t, "bela")
    set()
    """
    return set(tarolo.get(olvaso, {}).keys())


def atlag(napok: list[int]) -> float:
    """
    Kiszámolja a napok átlagát két tizedesjegyre kerekítve.

    >>> atlag([14, 5, 10])
    9.67
    >>> atlag([7, 21])
    14.0
    >>> atlag([])
    0.0
    """
    if not napok:
        return 0.0
    return round(sum(napok) / len(napok), 2)


def statisztika_keszitese(tarolo: NaploTarolo, o1: str, o2: str) -> dict[str, object]:
    """
    Összehasonlító statisztikát készít két olvasóról.

    >>> t = naplo_feldolgozasa(["anna;Dune;14", "bela;Dune;7", "anna;Solaris;10"])
    >>> statisztika_keszitese(t, "anna", "bela")['tobbet_kolcsonzott']
    'anna'
    >>> statisztika_keszitese(t, "anna", "bela")['kozos_konyv_db']
    1
    """
    o1_napok = olvaso_napjai(tarolo, o1)
    o2_napok = olvaso_napjai(tarolo, o2)
    o1_konyvek = olvaso_konyvei(tarolo, o1)
    o2_konyvek = olvaso_konyvei(tarolo, o2)

    o1_ossznap = sum(o1_napok)
    o2_ossznap = sum(o2_napok)

    if o1_ossznap > o2_ossznap:
        tobbet = o1
    elif o2_ossznap > o1_ossznap:
        tobbet = o2
    else:
        tobbet = "dontetlen"

    return {
        "o1_ossznap": o1_ossznap,
        "o2_ossznap": o2_ossznap,
        "o1_konyv_db": len(o1_konyvek),
        "o2_konyv_db": len(o2_konyvek),
        "kozos_konyv_db": len(o1_konyvek & o2_konyvek),
        "osszes_konyv_db": len(o1_konyvek | o2_konyvek),
        "o1_atlag": atlag(o1_napok),
        "o2_atlag": atlag(o2_napok),
        "tobbet_kolcsonzott": tobbet,
    }


def statisztika_szovegge(statisztika: dict[str, object]) -> str:
    """
    A statisztikát a feladatban kért formátumú szöveggé alakítja.

    >>> s = {"o1_ossznap": 40, "o2_ossznap": 37, "o1_konyv_db": 3, "o2_konyv_db": 3, \
             "kozos_konyv_db": 2, "osszes_konyv_db": 4, "o1_atlag": 10.0, "o2_atlag": 12.33, \
             "tobbet_kolcsonzott": "anna"}
    >>> print(statisztika_szovegge(s))
    o1_ossznap=40
    o2_ossznap=37
    o1_konyv_db=3
    o2_konyv_db=3
    kozos_konyv_db=2
    osszes_konyv_db=4
    o1_atlag=10.0
    o2_atlag=12.33
    tobbet_kolcsonzott=anna
    """
    kulcsok = [
        "o1_ossznap", "o2_ossznap", "o1_konyv_db", "o2_konyv_db",
        "kozos_konyv_db", "osszes_konyv_db", "o1_atlag", "o2_atlag",
        "tobbet_kolcsonzott"
    ]
    return "\n".join(f"{k}={statisztika[k]}" for k in kulcsok)
