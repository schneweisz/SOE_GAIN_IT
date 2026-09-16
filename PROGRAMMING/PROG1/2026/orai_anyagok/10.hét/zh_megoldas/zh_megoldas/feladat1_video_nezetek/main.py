from feladat1_video_nezetek.logic import (
    felhasznalok_sora_feldolgozasa,
    naplo_feldolgozasa,
    statisztika_keszitese,
    statisztika_szovegge,
    vege_sor_e,
)


def naplo_beolvasasa() -> list[str]:
    sorok = []
    while True:
        sor = input()
        if vege_sor_e(sor):
            break
        sorok.append(sor)
    return sorok


def felhasznalok_beolvasasa() -> tuple[str, str]:
    return felhasznalok_sora_feldolgozasa(input())


def program() -> None:
    naplo_sorok = naplo_beolvasasa()
    u1, u2 = felhasznalok_beolvasasa()

    tarolo = naplo_feldolgozasa(naplo_sorok)
    statisztika = statisztika_keszitese(tarolo, u1, u2)

    print(statisztika_szovegge(statisztika))


if __name__ == "__main__":
    program()
