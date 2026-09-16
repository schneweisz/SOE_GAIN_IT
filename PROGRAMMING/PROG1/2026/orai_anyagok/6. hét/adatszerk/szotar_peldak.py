from collections import defaultdict

from adatok import PONTSZAMOK_TUPLE_LISTA

"""
"tisztább" és gyorsabb eredmébyt kapunk, ha gyakori a kulcsalapú lekérdezés.
"""

def hallgatoi_atlagok_dict_alapon(rekordok):
    pontok_nevenkent_dict = defaultdict(list)
    #dict-é alakítjuk az adatokat, hogy gyorsabban tudjunk lekérdezni
    
    for nev,pont in rekordok:
        pontok_nevenkent_dict[nev].append(pont)
        
    atlagok={}
    
    #print(pontok_nevenkent_dict)
    #defaultdict(<class 'list'>, {'Anna': [5, 3, 4], 'Béla': [4, 2], 'Csilla': [5, 4], 'Dóri': [4]})
    #print(f"\n")
    #print(pontok_nevenkent_dict.items())
    #dict_items([('Anna', [5, 3, 4]), ('Béla', [4, 2]), ('Csilla', [5, 4]), ('Dóri', [4])])
    for nev,pontok in pontok_nevenkent_dict.items():
        atlagok[nev]=sum(pontok)/len(pontok)
    return atlagok


def main():
    atlagok=hallgatoi_atlagok_dict_alapon(PONTSZAMOK_TUPLE_LISTA)
    for nev in sorted(atlagok):
        print(f"{nev}: {atlagok[nev]:.2f}")
    
    

if __name__ == "__main__":
    main()
