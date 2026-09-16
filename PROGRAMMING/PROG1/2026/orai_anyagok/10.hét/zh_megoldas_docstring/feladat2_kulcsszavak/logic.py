"""Szövegnormalizáló és gyakoriságszámoló segédfüggvények."""

from collections import Counter


def kisbetusites(szoveg: str) -> str:
    """Kisbetűssé alakítja a teljes szöveget."""
    return szoveg.lower()


def betu_vagy_elvalaszto(karakter: str) -> str:
    """A betűket megtartja, minden más karaktert szóközre cserél."""
    if karakter.isalpha():
        return karakter
    return " "


def normalizalas(szoveg: str) -> str:
    """Eltávolítja az írásjeleket és elválasztókat egységes szóközökre cseréli."""
    return "".join(betu_vagy_elvalaszto(karakter) for karakter in szoveg)


def szavakra_bontas(szoveg: str) -> list[str]:
    """Szóközök mentén szavak listájára bontja a szöveget."""
    return szoveg.split()


def ures_elemek_eltavolitasa(szavak: list[str]) -> list[str]:
    """Eltávolítja az esetleges üres sztringeket a szólistából."""
    return [szo for szo in szavak if szo != ""]


def szovegbol_szavak(szoveg: str) -> list[str]:
    """A teljes normalizálási folyamat után visszaadja a szavakat."""
    kisbetus = kisbetusites(szoveg)
    normalizalt = normalizalas(kisbetus)
    feldarabolt = szavakra_bontas(normalizalt)
    return ures_elemek_eltavolitasa(feldarabolt)


def gyakorisag_szamolas(szavak: list[str]) -> Counter:
    """Előfordulásszámot készít a szavak listájából."""
    return Counter(szavak)


def rendezett_gyakorisag(gyakorisagok: Counter) -> list[tuple[str, int]]:
    """Gyakoriság szerint csökkenő, szó szerint növekvő sorrendbe rendez."""
    return sorted(gyakorisagok.items(), key=lambda elem: (-elem[1], elem[0]))


def top_n_szavak(szoveg: str, n: int = 5) -> list[tuple[str, int]]:
    """Visszaadja a szöveg `n` leggyakoribb szavát rendezett listában."""
    szavak = szovegbol_szavak(szoveg)
    gyakorisagok = gyakorisag_szamolas(szavak)
    rendezett = rendezett_gyakorisag(gyakorisagok)
    return rendezett[:n]


def top_lista_szovegge(top_lista: list[tuple[str, int]]) -> str:
    """Soronként `szo db` formátumú szöveggé alakítja a top listát."""
    return "\n".join(f"{szo} {db}" for szo, db in top_lista)
