
import random
import time

from lista_peldak import hallgatoi_atlagok_lista_alapon
from szotar_peldak import hallgatoi_atlagok_dict_alapon




def general_rekordok(hallgatok_szama, bejegyzesek_szama):
    nevek = [f"H{idx:04d}" for idx in range(hallgatok_szama)]
    return [(random.choice(nevek), random.randint(1, 5)) for _ in range(bejegyzesek_szama)]


def meres(fn, *args, ism=3):
    idok = []
    for _ in range(ism):
        t0 = time.perf_counter()
        fn(*args)
        idok.append(time.perf_counter() - t0)
    return min(idok)


def main():
    random.seed(0)

    rekordok = general_rekordok(hallgatok_szama=300, bejegyzesek_szama=30_000)

    t_lista = meres(hallgatoi_atlagok_lista_alapon, rekordok)
    t_dict = meres(hallgatoi_atlagok_dict_alapon, rekordok)

    print("Átlag-számítás (kisebb idő a jobb):")
    print(f"- lista-alapú: {t_lista:.4f} s")
    print(f"- dict-alapú : {t_dict:.4f} s")
    """
    - lista-alapú: 0.3282 s
    - dict-alapú : 0.0019 s
    """

if __name__ == "__main__":
    main()
