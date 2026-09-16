from adatok import PONTSZAMOK_TUPLE_LISTA


def atlag(pontok):
    return sum(pontok) / len(pontok) if pontok else 0.0


def hallgatoi_atlagok_lista_alapon(rekordok):
   

    nevek = []
    for nev, _ in rekordok:
        if nev not in nevek:
            nevek.append(nev)

    eredmeny = []
    for nev in nevek:
        pontok = [pont for n, pont in rekordok if n == nev]
        eredmeny.append((nev, atlag(pontok)))

    # Legyen determinisztikus a kiírás (név szerint rendezünk).
    eredmeny.sort(key=lambda x: x[0])
    return eredmeny


def main():
    atlagok = hallgatoi_atlagok_lista_alapon(PONTSZAMOK_TUPLE_LISTA)
    for nev, avg in atlagok:
        print(f"{nev}: {avg:.2f}")


if __name__ == "__main__":
    main()
