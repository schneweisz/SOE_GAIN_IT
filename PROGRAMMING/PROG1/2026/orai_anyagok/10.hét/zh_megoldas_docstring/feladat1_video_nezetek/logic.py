"""
Segédfüggvények a videómegtekintési napló feldolgozásához.
"""
from collections import defaultdict
from typing import DefaultDict, Iterable


def ures_sor_e(sor: str) -> bool:
    """Eldönti, hogy a kapott sor csak üres karakterekből áll-e"""
    return sor.strip() == ""


def vege_sor_e(sor: str) -> bool:
    """Ellenőrzi, hogy a sor a bement végét jelző "VEGE érték-e"""
    return sor.strip() == "VEGE"


def felhasznalok_sora_feldolgozasa(sor: str) -> tuple[str, str]:
    """Két felhasználónevet olvas ki az utolsó sorból"""
    adatok = sor.strip().split()
    if len(adatok) != 2:
        raise ValueError("Az utolsó sornak pontosan két felhasználónevet kell tartalmaznia.")
    return adatok[0], adatok[1]


def esemeny_sor_feldolgozasa(sor: str) -> tuple[str, str]:
    """
        Feldogoz egy 'felhasznalo;video' formátumú eseménysort.
    """
    darabok = sor.strip().split(";")
    if len(darabok) != 2:
        raise ValueError(f"Hibás eseménysor: {sor!r}")

    felhasznalo = darabok[0].strip()
    video_azonosito = darabok[1].strip()

    if felhasznalo == "" or video_azonosito == "":
        raise ValueError(f"Hiányos eseménysor: {sor!r}")

    return felhasznalo, video_azonosito


def uj_tarolo() -> DefaultDict[str, set[str]]:
    """
        Létrehoz egy felhasználóként videóazonosítókat tároló szótárat
    """
    return defaultdict(set)


def esemeny_rogzitese(tarolo: DefaultDict[str, set[str]], felhasznalo: str, video_azonosito: str) -> None:
    """Eltárolja, hogy az adott felhasználó megnézte a videót"""
    tarolo[felhasznalo].add(video_azonosito)


def naplo_feldolgozasa(sorok: Iterable[str]) -> DefaultDict[str, set[str]]:
    """Beolvassa az eseménysorokat, és felhasználónként összegyűjti a videókat"""
    tarolo = uj_tarolo()

    for sor in sorok:
        if ures_sor_e(sor):
            continue
        felhasznalo, video_azonosito = esemeny_sor_feldolgozasa(sor)
        esemeny_rogzitese(tarolo, felhasznalo, video_azonosito)

    return tarolo


def felhasznalo_videohalmaza(tarolo: DefaultDict[str, set[str]], felhasznalo: str) -> set[str]:
    """
        Visszaadja az adott felhasználóhoz tartozó egyedi videókat
    """
    return set(tarolo.get(felhasznalo, set()))


def statisztika_keszitese(tarolo: DefaultDict[str, set[str]], u1: str, u2: str) -> dict[str, int]:
    """ Kiszámolja a statisztikákat a két felhasználó videóhalmazainak segítségével"""
    u1_videok = felhasznalo_videohalmaza(tarolo, u1)
    u2_videok = felhasznalo_videohalmaza(tarolo, u2)

    kozos = u1_videok & u2_videok
    osszes = u1_videok | u2_videok

    return {
        "u1_egyedi_db": len(u1_videok),
        "u2_egyedi_db": len(u2_videok),
        "kozos_db": len(kozos),
        "osszes_db": len(osszes),
    }

def statisztika_szovegge(statisztika: dict[str, int]) -> str:
    """
        Szöveges, sorononkénti kimenetté alakítja a statisztikát
    """
    sorrend = ["u1_egyedi_db", "u2_egyedi_db", "kozos_db", "osszes_db"]
    return "\n".join(f"{kulcs}={statisztika[kulcs]}" for kulcs in sorrend)
