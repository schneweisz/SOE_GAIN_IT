"""
TUPLE -rendezett, nem módosítható, fix szerkezetű adat.


"""

from adatok import PONTSZAMOK_TUPLE_LISTA

def orderby_points(records):
    return sorted(records,key=lambda r: r[1], reverse=True)

def main():
    print("Eredeti rekordok:")
    for record in PONTSZAMOK_TUPLE_LISTA:
        print(record)

    print("Rendezve pont szerint(csökk.)")
    for rec in orderby_points(PONTSZAMOK_TUPLE_LISTA):
        print(rec)
        
    #rossz indexelés hamar kiderül:
    
    nev,pont=PONTSZAMOK_TUPLE_LISTA[0]
    print(f"\nElső rekord: {nev=} {pont=}")

if __name__ == "__main__":
    main()