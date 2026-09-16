def pont_sor_feldolgozasa(sor: str) -> tuple[str, int] | None:
    """Feldolgoz egy ``Nev:pont`` formátumú sort.

    Hibás formátum vagy nem egész pontszám esetén ``None`` értékkel tér vissza.

    >>> pont_sor_feldolgozasa("Anna:10")
    ('Anna', 10)
    >>> pont_sor_feldolgozasa("hibas") is None
    True
    >>> pont_sor_feldolgozasa("Bela:nemszam") is None
    True
    >>> pont_sor_feldolgozasa("  Cecil : 12 ")
    ('Cecil', 12)
    """
    darabok = sor.split(":")
    if len(darabok) != 2:
        return None

    nev = darabok[0].strip()
    pont_szoveg = darabok[1].strip()
    if nev == "":
        return None

    try:
        pont = int(pont_szoveg)
    except ValueError:
        return None

    return nev, pont


def pontok_osszegzese(sorok: list[str]) -> dict[str, int]:
    """Összegzi az azonos nevekhez tartozó pontokat.

    >>> pontok_osszegzese(["Anna:10", "Bela:7", "Anna:5"])
    {'Anna': 15, 'Bela': 7}
    >>> pontok_osszegzese(["hibas", "Bela:nemszam", "Cecil:12"])
    {'Cecil': 12}
    >>> pontok_osszegzese([])
    {}
    """
    osszegzett_pontok: dict[str, int] = {}
    for sor in sorok:
        feldolgozott = pont_sor_feldolgozasa(sor)
        if feldolgozott is None:
            continue

        nev, pont = feldolgozott
        if nev not in osszegzett_pontok:
            osszegzett_pontok[nev] = 0
        osszegzett_pontok[nev] += pont

    return osszegzett_pontok
