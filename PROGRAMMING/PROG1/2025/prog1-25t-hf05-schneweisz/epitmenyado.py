# 1. feladat
"""Olvassa be és tárolja el az utca.txt állományban talált adatokat!

A fájl első sorában a három adósávhoz tartozó négyzetméterenként fizetendő összeg
található A, B, C sorrendben, egy-egy szóközzel elválasztva.

A többi sorban egy-egy építmény adatai szerepelnek egy-egy szóközzel elválasztva.
Az első a telek tulajdonosának ötjegyű adószáma; egy tulajdonosnak több telke is lehet.
A második adat az utca neve, amely nem tartalmazhat szóközt.
A harmadik adat a házszám, majd az adósáv megnevezése, végül az építmény alapterülete.
"""
filename = 'utca.txt'
with open(filename) as f:
    lines = f.readlines()[1:]
telkek = []
for line in lines:
    telkek.append(line.strip().split(" "))

def beolvas_adok(filename: str) -> list[int]:
    with open(filename) as f:
        return [int(p) for p in f.readline().split()]


# 2. feladat
def kiir_telekszam():
    """Hány telek adatai találhatók az állományban?
    Az eredményt írassa ki a mintának megfelelően a képernyőre!

    >>> kiir_telekszam()
    2. feladat. A mintában 543 telek szerepel.
    """
    
    print(f"2. feladat. A mintában {len(telkek)} telek szerepel.")


# 3. feladat
def kiir_tulaj_epuletei(tulaj_adoszam: str):
    """Írassa ki a mintához hasonlóan, hogy melyik utcában, milyen házszám alatt van
    építménye!
    Ha a megadott azonosító nem szerepel az adatállományban, akkor írassa ki a „Nem
    szerepel az adatállományban.” hibaüzenetet!

    >>> kiir_tulaj_epuletei("68396")
    Harmat utca 22
    Szepesi utca 17
    """
    found = False
    for telek in telkek:
        if telek[0] == tulaj_adoszam:
            print(telek[1]+" utca", telek[2] )
            found = True
    if not found: 
        print("Nemszerepel az adatállományban.")


# 4. feladat
def ado(adosav: str, alapterulet: int) -> int:
    """Meghatározza egy adott építmény után fizetendő adót.

    Args:
        adosav (str): "A", "B" vagy "C" adósáv
        alapterulet (int): Az építmény alapterülete [m^2]

    Returns:
        int: Az építmény után fizetendő adó [Ft]

    Az A sávba azok a telkek kerültek, amelyek 300 méternél közelebb vannak a tóhoz.
    A B sáv az előzőn túl 600 méter távolságig terjed, a többi telek a C sávba tartozik.
    Az építmény után négyzetméterenként fizetendő összeg sávonként eltérő, azonban,
    ha az így kiszámított összeg nem éri el a 10.000 Ft-ot, akkor az adott építmény után
    nem kell adót fizetni.
    """
    adosavok = beolvas_adok(filename)
    adosav_index = {"A": 0, "B": 1, "C": 2}
    egyseg_ado = adosavok[adosav_index[adosav]]

    ossz_ado = egyseg_ado * alapterulet

    if ossz_ado < 10000:
        return 0

    return ossz_ado


# 5. feladat
def kiir_savonkenti_osszesites():
    """Határozza meg, hogy hány építmény esik az egyes adósávokba, és mennyi az adó
    összege adósávonként!
    Az eredményt a mintának megfelelően írassa ki a képernyőre!

    >>> kiir_savonkenti_osszesites()
    5. feladat
    A sávba 165 telek esik, az adó 20805600 Ft.
    B sávba 144 telek esik, az adó 13107000 Ft.
    C sávba 234 telek esik, az adó 3479600 Ft.
    """
    telek_db = {"A": 0, "B": 0, "C": 0}
    ado_osszeg = {"A": 0, "B": 0, "C": 0} 

    for telek in telkek: 
        adosav = telek[3]
        terulet = int(telek[4])
        telek_db[adosav] += 1
        ado_osszeg[adosav] += ado(adosav, terulet)

    print("5. feladat")
    for sav in "ABC":
        print(sav, "sávba", telek_db[sav], "telek esik, az adó", ado_osszeg[sav], "Ft.")


# 6. feladat
def kiir_heterogen_utcak():
    """Bár az utcák többé-kevésbé párhuzamosak a tó partjával, az egyes porták távolsága
    a parttól az utcában nem feltétlenül ugyanannyi. Emiatt néhány utcában - az ottani
    tulajdonosok felháborodására - egyes telkek eltérő sávba esnek.
    Listázza ki a képernyőre, hogy melyek azok az utcák, ahol a telkek sávokba sorolását
    emiatt felül kell vizsgálni!
    Feltételezheti, hogy minden utcában van legalább két telek.

    >>> kiir_heterogen_utcak()
    6. feladat. A több sávba sorolt utcák:
    Besztercei
    Gyurgyalag
    Icce
    Kurta
    Rezeda
    Szepesi
    """
    utca_savok = {}

    for telek in telkek:
        utca = telek[1]
        adosav = telek[3]

        if utca not in utca_savok:
            utca_savok[utca] = set()

        utca_savok[utca].add(adosav)

    heterogen = []
    for utca, savok in utca_savok.items():
        if len(savok) > 1:
            heterogen.append(utca)
    print("6. feladat. A több sávba sorolt utcák:")
    for utca in sorted(heterogen):
        print(utca)


# 7. feladat
def export_fizetendo_adok(output_filename: str):
    r"""Határozza meg a fizetendő adót tulajdonosonként!
    A tulajdonos adószámát és a fizetendő összeget írassa ki a mintának megfelelően a
    paraméterben megadott nevű állományba!
    A fájlban minden tulajdonos adatai új sorban szerepeljenek, a tulajdonos adószámát
    egy szóközzel elválasztva kövesse az általa fizetendő adó teljes összege.

    Args:
        output_filename (str): A kimeneti fájl elérési útja

    >>> export_fizetendo_adok("fizetendo.txt")
    >>> result = open("fizetendo.txt").readlines()
    >>> len(result)
    519
    >>> result[:3]
    ['38522 18000\n', '86379 0\n', '79906 12300\n']
    """
    tulaj_adok = {}
    for telek in telkek:
        tulaj = telek[0]
        adosav = telek[3]
        terulet = int(telek[4])
        telek_ado = ado(adosav, terulet)

        if tulaj in tulaj_adok:
            tulaj_adok[tulaj] += telek_ado
        else:
            tulaj_adok[tulaj] = telek_ado
    
    with open(output_filename, "w") as f:
        for tulaj in tulaj_adok.keys():
            f.write(f"{tulaj} {tulaj_adok[tulaj]}\n")





if __name__ == "__main__":
    kiir_telekszam()
    kiir_tulaj_epuletei(input("3. feladat. Egy tulajdonos adószáma: "))
    kiir_savonkenti_osszesites()
    kiir_heterogen_utcak()
    export_fizetendo_adok("fizetendo.txt")
