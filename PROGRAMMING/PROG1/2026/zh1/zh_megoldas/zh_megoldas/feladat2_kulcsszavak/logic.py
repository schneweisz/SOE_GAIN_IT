from collections import Counter


def kisbetusites(szoveg: str) -> str:
    return szoveg.lower()


def betu_vagy_elvalaszto(karakter: str) -> str:
    if karakter.isalpha():
        return karakter
    return " "


def normalizalas(szoveg: str) -> str:
    return "".join(betu_vagy_elvalaszto(karakter) for karakter in szoveg)


def szavakra_bontas(szoveg: str) -> list[str]:
    return szoveg.split()


def ures_elemek_eltavolitasa(szavak: list[str]) -> list[str]:
    return [szo for szo in szavak if szo != ""]


def szovegbol_szavak(szoveg: str) -> list[str]:
    kisbetus = kisbetusites(szoveg)
    normalizalt = normalizalas(kisbetus)
    feldarabolt = szavakra_bontas(normalizalt)
    return ures_elemek_eltavolitasa(feldarabolt)


def gyakorisag_szamolas(szavak: list[str]) -> Counter:
    return Counter(szavak)


def rendezett_gyakorisag(gyakorisagok: Counter) -> list[tuple[str, int]]:
    return sorted(gyakorisagok.items(), key=lambda elem: (-elem[1], elem[0]))


def top_n_szavak(szoveg: str, n: int = 5) -> list[tuple[str, int]]:
    szavak = szovegbol_szavak(szoveg)
    gyakorisagok = gyakorisag_szamolas(szavak)
    rendezett = rendezett_gyakorisag(gyakorisagok)
    return rendezett[:n]


def top_lista_szovegge(top_lista: list[tuple[str, int]]) -> str:
    return "\n".join(f"{szo} {db}" for szo, db in top_lista)
