import json
import os
def _load_hallgato(neptun: str) -> dict:
    """Beolvassa és visszaadja egy hallgató adatait.

    Args:
        neptun (str): a hallgató Neptun-azonosítója

    Returns:
        dict: a hallgató adatait tartalmazó szótár

    Raises:
        ValueError: ha a Neptun-azonosító nem található

    >>> _load_hallgato("ABC123")
    {'név': 'Kiss Ádám', 'kezdés': '2022_osz', 'félévek': [['FB0137', 'FB0132', 'FB0091'], ['FB0135', 'FB0150']]}
    >>> _load_hallgato("ABCDEF")
    Traceback (most recent call last):
    ...
    ValueError: Neptun-azonosító nem található: ABCDEF
    """
    file = f"hallgatok/{neptun}.json"
    try:
        with open(file, "r", encoding="UTF-8") as f:
            hallgato = json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Neptun-azonosító nem található: {neptun}")
    return hallgato  


def _get_felev_str(start: str, index: int) -> str:
    """Segédfüggvény adott félévtől adott időre lévő félév nevének meghatározásához.

    A félévek elnevezése a következő rendszert követi:
    2021_tavasz
    2021_osz
    2022_tavasz
    2022_osz
    2023_tavasz
    ...

    Args:
        start (str): a referencia félév neve
        index (int): a keresett félév indexe

    Returns:
        str: a keresett félév neve

    Raises:
        ValueError: ha a félév neve érvénytelen formátumban van
    """
    match start.split("_"):
        case [ev, "tavasz"]:
            return f"{int(ev) + index // 2}_" + ["tavasz", "osz"][index % 2]
        case [ev, "osz"]:
            return f"{int(ev) + (index + 1) // 2}_" + ["osz", "tavasz"][index % 2]
        case _:
            raise ValueError(f"Érvénytelen formátumú félév: {start}")


def _get_felev_index(start: str, felev: str) -> int:
    """Segédfüggvény egy félév indexének meghatározásához.

    A félévek elnevezése a következő rendszert követi:
    2021_tavasz
    2021_osz
    2022_tavasz
    2022_osz
    2023_tavasz
    ...

    Args:
        start (str): a referencia félév neve
        felev (str): a keresett félév neve

    Returns:
        int: a keresett félév indexe, ha a start félév indexe 0

    Raises:
        ValueError: ha bármelyik félév neve érvénytelen formátumban van

    >>> _get_felev_index("2021_tavasz", "2021_osz")
    1
    >>> _get_felev_index("2021_tavasz", "2022_tavasz")
    2
    >>> _get_felev_index("2021-tavasz", "2022_tavasz")
    Traceback (most recent call last):
    ...
    ValueError: Érvénytelen formátumú félév: 2021-tavasz
    >>> _get_felev_index("2021_tavasz", "2022/tavasz")
    Traceback (most recent call last):
    ...
    ValueError: Érvénytelen formátumú félév: 2022/tavasz
    """
    def check_format(format):
        darabok = format.split("_")
        try:
            if len(darabok) != 2 or darabok[1] not in ["osz", "tavasz"]:
                raise ValueError()
            ev = int(format.split("_")[0])
        except ValueError:
            raise ValueError(f"Érvénytelen formátumú félév: {format}")
        
    check_format(start) 
    check_format(felev) 
    start_ev = int(start.split("_")[0])
    felev_ev = int(felev.split("_")[0])
    start_evszak = start.split("_")[1]
    felev_evszak = felev.split("_")[1]
    
    d = 2 *  (felev_ev - start_ev)
    if start_evszak + felev_evszak == "tavaszosz":
        d += 1
    elif start_evszak + felev_evszak == "osztavasz":
        d -= 1
    return d  # TODO


def _get_kurzus_eredmeny(hallgato: str, targy: str, felev: str) -> int:
    """Lekérdezi egy hallgató eredményét egy tárgy adott félévéből.

    Az eredmények a `targyak/[targy]/[felev].csv` fájlokban találhatóak.
    Ha az aláírás oszlopban nem 1-es van, akkor a hallgató nem teljesítette a tárgyat.

    Args:
        hallgato (str): a hallgató Neptun-azonosítója
        targy (str): a keresett tárgy kódja
        felev (str): a keresett félév neve

    Returns:
        int: a kurzus eredménye, vagy 0, ha a hallgató nem teljesítette a tárgyat

    Raises:
        FileNotFoundError: ha a fájl nem található
        ValueError: ha a hallgató nem található a fájlban

    >>> _get_kurzus_eredmeny("ABC123", "FB0091", "2022_osz")
    5
    >>> _get_kurzus_eredmeny("MNO345", "FB0132", "2022_osz")
    0
    >>> _get_kurzus_eredmeny("ABC123", "FB0000", "2022_osz")
    Traceback (most recent call last):
    ...
    FileNotFoundError: [Errno 2] No such file or directory: 'targyak/FB0000/2022_osz.csv'
    >>> _get_kurzus_eredmeny("MNO345", "FB0135", "2023_tavasz")
    Traceback (most recent call last):
    ...
    ValueError: hallgató nem található a kurzusnál: MNO345
    """
    try:
        is_student = False
        with open(f"targyak/{targy}/{felev}.csv", "r", encoding="UTF-8") as f:
            lines = f.readlines()[1:]
        for line in lines:
            if hallgato in line:
                is_student = True
            data = line.strip().split(";")
            if data[0] == hallgato and int(data[1]) == 1:
                return int(data[2])
            elif data[0] == hallgato and int(data[1]) != 1:
                return 0     
        if is_student == False:
            raise ValueError(f"hallgató nem található a kurzusnál: {hallgato}")
    except FileNotFoundError:
        raise FileNotFoundError(f"[Errno 2] No such file or directory: 'targyak/{targy}/{felev}.csv'")


def _get_targy_krediterteke(targy: str) -> int:
    """Lekérdezi egy tárgy kreditértékét.

    A kreditérték a `targyak/[targy]/adatok.json` fájl "kredit" kulcsánál található.

    Args:
        targy (str): a keresett tárgy kódja

    Returns:
        int: a tárgy kreditértéke

    Raises:
        FileNotFoundError: ha a fájl nem található
        KeyError: ha a fájlban nem található a "kredit" kulcs

    >>> _get_targy_krediterteke("FB0091")
    5
    >>> _get_targy_krediterteke("FB0099")
    Traceback (most recent call last):
    ...
    FileNotFoundError: [Errno 2] No such file or directory: 'targyak/FB0099/adatok.json'
    >>> _get_targy_krediterteke("FB0150")
    Traceback (most recent call last):
    ...
    KeyError: 'kredit'
    """
    try:
        with open(f"targyak/{targy}/adatok.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
        return data['kredit']
    except FileNotFoundError:
        raise FileNotFoundError(f"[Errno 2] No such file or directory: 'targyak/{targy}/adatok.json'")
    except KeyError:
        raise KeyError('kredit')


###########################################################################
# A fentebbi függvények implementációját másold be az előző heti háziból! #
###########################################################################


def select_hallgato() -> str:
    """Hallgató kiválasztása felsorolásból.

    Listázza ki sorszámozva a hallgatók neveit és neptunkódjait (név szerint ábécésorrendben),
    kérjen be egy sorszámot, és adja vissza kiválasztott hallgató neptunkódját.

    A lista formátuma:
    1: Horváth Milán (MNO345)
    2: Király István (STU901)
    3: Kiss Ádám (ABC123)
    4: Kovács Dávid (DEF456)
    """
    print("Hallgatók:")
    # TODO: hallgatók listázása
    sorszam = 0
    hallgatok = {}
    diakok = os.listdir("hallgatok")
    neptunkod = []
    for filename in diakok:
        neptun = filename[:-5]
        with open(f"hallgatok/{filename}", "r", encoding='utf8') as f:
            data = json.load(f)
            nev = data.get("név")
        hallgatok[nev] = neptun
        #print(f"{sorszam}: {nev} ({neptun})") 
    for diak in sorted(hallgatok):
        sorszam += 1
        print(f"{sorszam}: {diak[0:]} ({hallgatok[diak]})")
        neptunkod.append(hallgatok[diak])
    
    n = int(input("Adja meg a hallgató sorszámát: "))
    return neptunkod[n-1]  # TODO


def select_hallgato_felev(hallgato) -> str:
    """Hallgató félévének kiválasztása felsorolásból.

    Listázza ki sorszámozva a megadott hallgató féléveinek neveit (időrendi sorrendben),
    kérjen be egy sorszámot, és adja vissza kiválasztott félév nevét.
    """
    print("Félévek:")
    with open(f"hallgatok/{hallgato}.json", "r", encoding="utf8") as f:
        data = json.load(f)
        felevek = sorted(data.get("félévek", []))
    
    sorszam = 1
    felev_l = []
    for felev in felevek:
        print(f"{sorszam}: {felev}")
        felev_l.append(felev)
        sorszam += 1
    
    while True:
        try:
            n = int(input("Adja meg a félév sorszámát: "))
            if 1 <= n <= len(felev_l):
                return felev_l[n - 1]
            else:
                print("Érvénytelen sorszám! Próbálja újra.")
        except ValueError:
            print("Kérem, csak számot adjon meg!")


def print_hallgato_atlag(osszes_felev: bool = True) -> None:
    """Kiírja a hallgató féléves vagy kumulatív átlagát.

    Az átlag a felvett tárgyak kreditértékével kerül súlyozásra.
    A nem teljesített tárgyak 0-nak számítanak, függetlenül attól, hogy a nem teljesítés
    oka az aláírás hiánya, a vizsgákról való hiányzás, vagy az 1-es érdemjegy.

    Args:
        osszes_felev (bool, optional): ha False, akkor megkérdezi a félévet, különben az
            összes félév tárgyának átlagát számolja ki. Alapértelmezetten True.
    """
    hallgato = select_hallgato()
    if not osszes_felev:
        felev = select_hallgato_felev(hallgato)
    try:
        hallgato_adatok = _load_hallgato(hallgato)
    except ValueError as e:
        print(e)
        return
    osszes_kredit = 0
    osszes_sulyozott_eredmeny = 0

    if felev:
        felevek = [felev]
    else:
        felevek = hallgato_adatok["félévek"]

    for felev in felevek:
        for targy in felev:
            try:
                eredmeny = _get_kurzus_eredmeny(hallgato, targy, felev)
                kredit = _get_targy_krediterteke(targy)
                osszes_kredit += kredit
                osszes_sulyozott_eredmeny += eredmeny * kredit
            except (FileNotFoundError, ValueError, KeyError) as e:
                print(f"Hiba a(z) {targy} tárgy feldolgozása közben: {e}")

    try:
        atlag = osszes_sulyozott_eredmeny / osszes_kredit
    except ZeroDivisionError:
        atlag = 0.0

    if felev:
        print(f"A hallgató {felev} félévének átlaga: {atlag:.2f}")
    else:
        print(f"A hallgató kumulatív átlaga: {atlag:.2f}")

    # az alábbiakhoz felhasználható a múlt heti házi megoldása:

    # TODO
    # súlyozott átlag kiszámítása
    # ha egy tárgy eredményeinek lekérdezésekor kivétel dobódik, írja ki a hibaüzenetet,
    # és hagyja ki a tárgyat a számításból
    # a ZeroDivisionError elkapásával kezelje le, ha a nevező 0, és az átlag legyen 0.0

    # TODO
    # átlag kiírása

