def kihagy_szokoz_es_nagybetus(szoveg):
    #elvátolítja a szóközt, nagybetűvé alakít, sázmokat megtart.
    return ''.join(c.upper() for c in szoveg if c != ' ' and (c.isalpha() or c.isdigit()))

def szokoz_szama(szoveg):
    return szoveg.count(' ')

def szavak_szama(szoveg):
    return len(szoveg.strip().split(' '))
    

tesztek=[
    "Hello World 123",
    " Szóköz elején és a végén is "
]

for szoveg in tesztek:
    print(f"Input: ",szoveg)
    print(f"Feldolgozás:", kihagy_szokoz_es_nagybetus(szoveg))
    print(f"Szóközök száma:", szokoz_szama(szoveg))
    print(f"Szavak száma:", szavak_szama(szoveg))