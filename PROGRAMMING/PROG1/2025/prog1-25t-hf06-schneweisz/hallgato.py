import json

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
    try:
        with open(f"hallgatok/{neptun}.json", "r", encoding="UTF-8") as f:
            hallgato = json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Neptun-azonosító nem található: {neptun}")
    return hallgato  # TODO


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
    

def print_hallgato_atlag(osszes_felev: bool = True) -> None:
    """Kiírja a hallgató féléves vagy kumulatív átlagát.

    Az átlag a felvett tárgyak kreditértékével kerül súlyozásra.
    A nem teljesített tárgyak 0-nak számítanak, függetlenül attól, hogy a nem teljesítés
    oka az aláírás hiánya, a vizsgákról való hiányzás, vagy az 1-es érdemjegy.

    Args:
        osszes_felev (bool, optional): ha False, akkor megkérdezi a félévet, különben az
            összes félév tárgyának átlagát számolja ki. Alapértelmezetten True.
    """
    # Hallgató Neptun-kódjának bekérése
    neptun = input("Neptun kód: ")
    try:
        hallgato = _load_hallgato(neptun)
    except ValueError:
        return "Ez a Neptun-kód nem található."
        

    # Ha nem kell az összes félév, akkor félév bekérése
    if not osszes_felev:
        felev_input = input("Hány félév: ")
        try:
            felev_index = int(felev_input) - 1
            if felev_index < 0 or felev_index >= len(hallgato["félévek"]):
                print("Érvénytelen félév sorszám.")
                return
            felevek = [hallgato["félévek"][felev_index]]
        except ValueError:
            felevek = [felev for felev in hallgato["félévek"] if _get_felev_str(hallgato["kezdés"], hallgato["félévek"].index(felev)) == felev_input]
            if not felevek:
                print("Érvénytelen félév név.")
                return
    else:
        felevek = hallgato["félévek"]

    # TODO
    # súlyozott átlag kiszámítása
    # ha egy tárgy eredményeinek lekérdezésekor kivétel dobódik, írja ki a hibaüzenetet,
    # és hagyja ki a tárgyat a számításból
    # a ZeroDivisionError elkapásával kezelje le, ha a nevező 0, és az átlag legyen 0.0
    osszes_kredit = 0
    osszes_ertek = 0
    for felev in felevek:
        for targy in felev:
            try:
                eredmeny = _get_kurzus_eredmeny(neptun, targy, _get_felev_str(hallgato["kezdés"], hallgato["félévek"].index(felev)))
                kredit = _get_targy_krediterteke(targy)
                osszes_kredit += kredit
                osszes_ertek += eredmeny * kredit
            except Exception as e:
                print(f"Hiba a(z) {targy} tárgynál: {e}")
    try:
        atlag = osszes_ertek / osszes_kredit
    except ZeroDivisionError:
        atlag = 0.0
    # TODO
    # átlag kiírása
     # Átlag kiírása
    if osszes_felev:
        print(f"A hallgató kumulatív súlyozott átlaga: {atlag:.2f}")
    else:
        print(f"A hallgató kiválasztott félévének súlyozott átlaga: {atlag:.2f}")


#print_hallgato_atlag()
if __name__ == "__main__":
    neptun = "ABC123"
    print(_load_hallgato(neptun))
    diak = _load_hallgato(neptun)
    current = diak['kezdés']
    felev_count = len(diak["félévek"])
    idx = _get_felev_index(current, _get_felev_str(current, 1))
    print("Félévek száma: ", felev_count)
    try:
        for felev in diak['félévek']:
            for targy in felev:
                print(f"{targy}, eredmény: {_get_kurzus_eredmeny(neptun, targy, current)}, kredit: {_get_targy_krediterteke(targy)}")
            current =_get_felev_str(diak['kezdés'], idx)
    except Exception as e:
        print(f"{e} hiba, a '{targy}' kurzusnál")
