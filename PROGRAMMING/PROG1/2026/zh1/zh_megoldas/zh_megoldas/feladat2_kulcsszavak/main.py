from feladat2_kulcsszavak.logic import top_lista_szovegge, top_n_szavak


def teljes_szoveg_beolvasasa() -> str:
    sorok = []
    try:
        while True:
            sorok.append(input())
    except EOFError:
        pass
    return "\n".join(sorok)


def program() -> None:
    szoveg = teljes_szoveg_beolvasasa()
    top_lista = top_n_szavak(szoveg, 5)
    print(top_lista_szovegge(top_lista))


if __name__ == "__main__":
    program()
