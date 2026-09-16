

from feladat1_video_nezetek.logic import (
    felhasznalok_sora_feldolgozasa,
    naplo_feldolgozasa,
    statisztika_keszitese,
    statisztika_szovegge,
    vege_sor_e,
)


def naplo_beolvasasa() -> list[str]:
    """ Beolvassa a napló sorait, a 'VEGE' sorig."""
    sorok = []
    while True:
        sor = input()
        if vege_sor_e(sor):
            break
        sorok.append(sor)
    return sorok


def felhasznalok_beolvasasa() -> tuple[str, str]:
    """Beolvassa és feldolgozza az összehasonlítandó két felhasználó nevét."""
    return felhasznalok_sora_feldolgozasa(input())


def program() -> None:
    """Lefuttatja a teljes beolvasás-feldolgozás-kíirás folyamatot"""
    naplo_sorok = naplo_beolvasasa()
    u1, u2 = felhasznalok_beolvasasa()

    tarolo = naplo_feldolgozasa(naplo_sorok)
    statisztika = statisztika_keszitese(tarolo, u1, u2)

    print(statisztika_szovegge(statisztika))


if __name__ == "__main__":
    program()
