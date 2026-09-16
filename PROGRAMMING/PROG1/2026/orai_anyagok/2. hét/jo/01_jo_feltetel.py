#2féleképpen megnézzük hogy x 3 vagy 4-e

def ellenorzes_ket_modon(x):
    megoldas_1=x==3 or x==4
    
    megoldas_2=x in (3,4)
    return megoldas_1, megoldas_2

tesztek=[2,3,4,5]

for x in tesztek:
    m1,m2=ellenorzes_ket_modon(x)
    print(f"x={x} elso: {m1}  masodik :{m2}")
    