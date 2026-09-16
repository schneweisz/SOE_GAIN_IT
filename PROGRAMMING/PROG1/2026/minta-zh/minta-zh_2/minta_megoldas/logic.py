PontTarolo = dict[str, dict[str, list[int]]]


def ures_sor_e(sor: str) -> bool:
    """Eldönti, hogy a sor üres-e vagy csak whitespace karaktereket tartalmaz-e.

    >>> ures_sor_e("")
    True
    >>> ures_sor_e("   ")
    True
    >>> ures_sor_e("anna;Python;12")
    False
    """
    return sor.strip() == ""


def vege_sor_e(sor: str) -> bool:
    """Eldönti, hogy a sor a bemenet végét jelöli-e.

    >>> vege_sor_e("VEGE")
    True
    >>> vege_sor_e("  VEGE  ")
    True
    >>> vege_sor_e("vege")
    False
    """
    return sor.strip() == "VEGE"


def esemeny_sor_feldolgozasa(sor: str) -> tuple[str, str, int]:
    """Feldolgoz egy ``felhasznalonev;kurzus;pont`` formátumú sort.

    >>> esemeny_sor_feldolgozasa("anna;Python;12")
    ('anna', 'Python', 12)
    >>> esemeny_sor_feldolgozasa(" anna ; Web ; 5 ")
    ('anna', 'Web', 5)
    >>> esemeny_sor_feldolgozasa("hibas sor")
    Traceback (most recent call last):
    ...
    ValueError: Hibásan formázott eseménysor
    >>> esemeny_sor_feldolgozasa("anna;;10")
    Traceback (most recent call last):
    ...
    ValueError: Hiányos eseménysor
    """
    darabok = sor.strip().split(";")
    if len(darabok) != 3:
        raise ValueError("Hibásan formázott eseménysor")

    felhasznalo = darabok[0].strip()
    kurzus = darabok[1].strip()
    pont_szoveg = darabok[2].strip()

    if felhasznalo == "" or kurzus == "":
        raise ValueError("Hiányos eseménysor")

    try:
        pont = int(pont_szoveg)
    except ValueError as exc:
        raise ValueError("A pont nem egész szám") from exc

    return felhasznalo, kurzus, pont


def felhasznalok_sora_feldolgozasa(sor: str) -> tuple[str, str]:
    """Két felhasználónevet olvas ki egy szóközzel tagolt sorból.

    >>> felhasznalok_sora_feldolgozasa("anna bela")
    ('anna', 'bela')
    >>> felhasznalok_sora_feldolgozasa("  anna   bela  ")
    ('anna', 'bela')
    >>> felhasznalok_sora_feldolgozasa("anna")
    Traceback (most recent call last):
    ...
    ValueError: Pontosan két felhasználónevet kell megadni
    """
    darabok = sor.strip().split()
    if len(darabok) != 2:
        raise ValueError("Pontosan két felhasználónevet kell megadni")
    return darabok[0], darabok[1]


def naplo_feldolgozasa(sorok: list[str]) -> PontTarolo:
    """Naplósorokból felhasználó-kurzus-pontlista szerkezetet készít.

    Az üres sorokat figyelmen kívül hagyja.

    >>> naplo_feldolgozasa(["anna;Python;12", "anna;Python;5", "bela;Web;3"])
    {'anna': {'Python': [12, 5]}, 'bela': {'Web': [3]}}
    >>> naplo_feldolgozasa(["", "  ", "anna;Web;10"])
    {'anna': {'Web': [10]}}
    >>> naplo_feldolgozasa([])
    {}
    """
    tarolo: PontTarolo = {}
    for sor in sorok:
        if ures_sor_e(sor):
            continue

        felhasznalo, kurzus, pont = esemeny_sor_feldolgozasa(sor)
        if felhasznalo not in tarolo:
            tarolo[felhasznalo] = {}
        if kurzus not in tarolo[felhasznalo]:
            tarolo[felhasznalo][kurzus] = []
        tarolo[felhasznalo][kurzus].append(pont)

    return tarolo


def felhasznalo_pontjai(tarolo: PontTarolo, felhasznalo: str) -> list[int]:
    """Visszaadja egy felhasználó összes pontját kurzustól függetlenül.

    >>> tarolo = {"anna": {"Python": [12, 5], "Web": [15]}}
    >>> felhasznalo_pontjai(tarolo, "anna")
    [12, 5, 15]
    >>> felhasznalo_pontjai(tarolo, "bela")
    []
    >>> felhasznalo_pontjai({}, "anna")
    []
    """
    kurzusok = tarolo.get(felhasznalo, {})
    pontok: list[int] = []
    for kurzus_pontok in kurzusok.values():
        pontok.extend(kurzus_pontok)
    return pontok


def felhasznalo_kurzusai(tarolo: PontTarolo, felhasznalo: str) -> set[str]:
    """Visszaadja azoknak a kurzusoknak a halmazát, amelyekhez a felhasználónak pontja van.

    >>> tarolo = {"anna": {"Python": [12, 5], "Web": [15]}}
    >>> felhasznalo_kurzusai(tarolo, "anna") == {"Python", "Web"}
    True
    >>> felhasznalo_kurzusai(tarolo, "bela")
    set()
    >>> felhasznalo_kurzusai({}, "anna")
    set()
    """
    return set(tarolo.get(felhasznalo, {}).keys())


def atlag(pontok: list[int]) -> float:
    """Kiszámolja a pontok átlagát két tizedesjegyre kerekítve.

    >>> atlag([12, 5, 15])
    10.67
    >>> atlag([8, 20, 7])
    11.67
    >>> atlag([])
    0.0
    """
    if len(pontok) == 0:
        return 0.0
    return round(sum(pontok) / len(pontok), 2)


def statisztika_keszitese(tarolo: PontTarolo, u1: str, u2: str) -> dict[str, object]:
    """Összehasonlító statisztikát készít két felhasználóról.

    >>> tarolo = naplo_feldolgozasa([
    ...     "anna;Python;12", "bela;Python;8", "anna;Web;15",
    ...     "anna;Python;5", "csilla;Adatbazis;10", "bela;Web;20",
    ...     "bela;Python;7", "anna;Adatbazis;0",
    ... ])
    >>> statisztika_keszitese(tarolo, "anna", "bela")
    {'u1_osszpont': 32, 'u2_osszpont': 35, 'u1_kurzus_db': 3, 'u2_kurzus_db': 2, 'kozos_kurzus_db': 2, 'osszes_kurzus_db': 3, 'u1_atlag': 8.0, 'u2_atlag': 11.67, 'jobb_felhasznalo': 'bela'}
    >>> statisztika_keszitese({}, "anna", "bela")["jobb_felhasznalo"]
    'dontetlen'
    >>> statisztika_keszitese({"anna": {"Python": [10]}}, "anna", "bela")["u2_atlag"]
    0.0
    """
    u1_pontok = felhasznalo_pontjai(tarolo, u1)
    u2_pontok = felhasznalo_pontjai(tarolo, u2)
    u1_kurzusok = felhasznalo_kurzusai(tarolo, u1)
    u2_kurzusok = felhasznalo_kurzusai(tarolo, u2)
    u1_osszpont = sum(u1_pontok)
    u2_osszpont = sum(u2_pontok)

    if u1_osszpont > u2_osszpont:
        jobb_felhasznalo = u1
    elif u2_osszpont > u1_osszpont:
        jobb_felhasznalo = u2
    else:
        jobb_felhasznalo = "dontetlen"

    return {
        "u1_osszpont": u1_osszpont,
        "u2_osszpont": u2_osszpont,
        "u1_kurzus_db": len(u1_kurzusok),
        "u2_kurzus_db": len(u2_kurzusok),
        "kozos_kurzus_db": len(u1_kurzusok & u2_kurzusok),
        "osszes_kurzus_db": len(u1_kurzusok | u2_kurzusok),
        "u1_atlag": atlag(u1_pontok),
        "u2_atlag": atlag(u2_pontok),
        "jobb_felhasznalo": jobb_felhasznalo,
    }


def statisztika_szovegge(statisztika: dict[str, object]) -> str:
    """A statisztikát a feladatban kért sorrendű sorokká alakítja.

    >>> statisztika_szovegge({"u1_osszpont": 1, "u2_osszpont": 2, "u1_kurzus_db": 1, "u2_kurzus_db": 1, "kozos_kurzus_db": 0, "osszes_kurzus_db": 2, "u1_atlag": 1.0, "u2_atlag": 2.0, "jobb_felhasznalo": "bela"})
    'u1_osszpont=1\\nu2_osszpont=2\\nu1_kurzus_db=1\\nu2_kurzus_db=1\\nkozos_kurzus_db=0\\nosszes_kurzus_db=2\\nu1_atlag=1.0\\nu2_atlag=2.0\\njobb_felhasznalo=bela'
    """
    kulcsok = [
        "u1_osszpont",
        "u2_osszpont",
        "u1_kurzus_db",
        "u2_kurzus_db",
        "kozos_kurzus_db",
        "osszes_kurzus_db",
        "u1_atlag",
        "u2_atlag",
        "jobb_felhasznalo",
    ]
    return "\n".join(f"{kulcs}={statisztika[kulcs]}" for kulcs in kulcsok)
