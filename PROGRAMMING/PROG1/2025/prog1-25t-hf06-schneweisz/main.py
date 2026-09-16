from hallgato import print_hallgato_atlag
from kurzus import print_kurzuseredmeny


def main():
    while True:
        choice = input("""\
1: Hallgató féléves átlaga
2: Hallgató kumulatív átlaga
3: Kurzuseredmények
0: Kilépés
Menüpont: """)
        try:
            index = int(choice)
            match index:
                case 0:
                    return
                case 1:
                    print_hallgato_atlag(False)
                case 2:
                    print_hallgato_atlag()
                case 3:
                    print_kurzuseredmeny()
                case _:
                    raise ValueError("Hibás menüpont!")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
